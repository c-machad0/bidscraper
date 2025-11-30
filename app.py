"""
app_apresentacao.py

Interface web para apresentação do Radar Licita.
Permite execução manual e visualização em tempo real.
"""
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from threading import Thread
from datetime import datetime
import os

from main import Main
from database import BidDatabase
from config import CITIES_URLS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'radar-licita-demo-2024'
socketio = SocketIO(app, cors_allowed_origins="*")

class InterfaceController:
    def __init__(self):
        self.is_running = False
        self.results = []
    
    def status_callback(self, event_type, data):
        """Callback para receber atualizações do scraper"""
        socketio.emit('update', {
            'type': event_type,
            'data': data,
            'timestamp': datetime.now().strftime('%H:%M:%S')
        })
        
        if event_type == 'complete':
            self.is_running = False
            self.load_results()
    
    def load_results(self):
        """Carrega licitações do banco de dados"""
        try:
            db = BidDatabase()
            data = db.list_database()
            db.close_database()
            
            self.results = [
                {
                    'id': row[0],
                    'cidade': row[1],
                    'resumo': row[2][:150] + '...' if len(row[2]) > 150 else row[2],
                    'modalidade': row[3],
                    'data': row[4][:10] if len(row) > 4 else 'N/A',
                    'portal': CITIES_URLS.get(row[1], '#')
                }
                for row in data
            ]
        except Exception as e:
            print(f"Erro ao carregar resultados: {e}")
            self.results = []

controller = InterfaceController()

@app.route('/')
def index():
    """Página principal"""
    controller.load_results()
    return render_template('index.html', 
                          cities=list(CITIES_URLS.keys()),
                          total_results=len(controller.results))

@app.route('/api/status')
def get_status():
    """Status atual da aplicação"""
    return jsonify({
        'running': controller.is_running,
        'results_count': len(controller.results)
    })

@app.route('/api/results')
def get_results():
    """Retorna licitações encontradas"""
    return jsonify(controller.results)

@socketio.on('start_scraping')
def handle_start_scraping():
    """Inicia o processo de scraping"""
    if controller.is_running:
        emit('error', {'message': 'Scraping já está em execução'})
        return
    
    controller.is_running = True
    emit('update', {
        'type': 'started',
        'data': {'status': 'Iniciando Radar Licita...'},
        'timestamp': datetime.now().strftime('%H:%M:%S')
    })
    
    def run_scraper():
        app_main = Main(callback=controller.status_callback)
        app_main.run_app()
    
    thread = Thread(target=run_scraper)
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🏛️  RADAR LICITA - MODO APRESENTAÇÃO")
    print("="*60)
    print(f"\n✅ Servidor iniciado!")
    print(f"🌐 Acesse: http://localhost:5000")
    print(f"📱 Ou pelo IP local na rede\n")
    print("Pressione Ctrl+C para encerrar")
    print("="*60 + "\n")
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=False, allow_unsafe_werkzeug=True)
