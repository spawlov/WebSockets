import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins="*")

app = socketio.WSGIApp(sio)


# @sio.event
# def connect(sid, environ):
#     pprint.pprint(environ)
#     print(f"Client {sid} is connected")


@sio.event
def disconnect(sid):
    print(f"Client {sid} is disconnected")

@sio.on("connect")
def connect(sid, environ):
    print(f"Client {sid} is connected")

@sio.on("hello")
def hello(sid,environ):
    sio.emit("hello", to=sid, data={"message": "hello socket"})


# @sio.on("*")
# def catch_all(event, sid, data):
#     sio.emit("error", to=sid, data={"message": f"No handler for event {event}"})
#     print("Event received: ", event)
#     print("Data: ", data)




eventlet.wsgi.server(eventlet.listen(("", 8080)), app)
