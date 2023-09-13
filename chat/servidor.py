from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Lista para armazenar as mensagens
messages = []

@app.route('/')
def index():
    return render_template('chat.html', messages=messages)

@socketio.on('message')
def handle_message(message):
    messages.append(message)
    
    # Salvar as mensagens em um arquivo
    with open('chat_history.txt', 'a') as file:
        file.write(message + '\n')

    emit('message', message, broadcast=True)  # Enviar mensagem para todos os clientes conectados

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=2023, debug=True)
    