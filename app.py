from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import uuid

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}  # Store connected users {user_id: {name, room}}
messages = []  # Store chat messages

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/join", methods=["POST"])
def join_call():
    data = request.json
    user_id = str(uuid.uuid4())
    users[user_id] = {"name": data["name"], "room": data["room"]}
    return jsonify({"user_id": user_id})

@socketio.on("join_room")
def handle_join(data):
    user_id = data["user_id"]
    room = users[user_id]["room"]
    join_room(room)
    emit("user_joined", {"name": users[user_id]["name"]}, room=room)

@socketio.on("leave_room")
def handle_leave(data):
    user_id = data["user_id"]
    room = users[user_id]["room"]
    leave_room(room)
    emit("user_left", {"name": users[user_id]["name"]}, room=room)
    del users[user_id]

@socketio.on("message")
def handle_message(data):
    room = data["room"]
    messages.append({"name": data["name"], "text": data["message"]})
    emit("receive_message", {"name": data["name"], "message": data["message"]}, room=room)

if __name__ == "__main__":
    socketio.run(app, debug=True)
