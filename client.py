import socketio

# Создаем клиент Socket.IO
sio = socketio.Client()


# Обработчик события 'hello'
@sio.on("hello")
def hello_handler(data):
    print(f"Получено приветственное сообщение от сервера: {data['message']}")


# Обработчик любых событий
@sio.event
def handle_event(sid, data):
    print(f"Получено событие от сервера ({sid}): {data}")


# Обработчик события подключения
@sio.event
def connect():
    print("Подключено к серверу")


# Обработчик события отключения
@sio.event
def disconnect():
    print("Отключено от сервера")


# Запускаем клиент и подключаемся к серверу
sio.connect("http://localhost:8080")

# Ждем, пока не произойдет отключение
sio.wait()
