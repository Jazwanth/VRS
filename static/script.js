const socket = io.connect("http://localhost:5000");
let user_id;
let room;
let localStream;
let peerConnection;
const servers = { iceServers: [{ urls: "stun:stun.l.google.com:19302" }] };

function joinCall() {
    const name = document.getElementById("name").value;
    room = document.getElementById("room").value;

    fetch("/join", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, room }),
    })
    .then(res => res.json())
    .then(data => {
        user_id = data.user_id;
        socket.emit("join_room", { user_id });

        document.getElementById("video-section").style.display = "block";
        startVideo();
    });
}

function startVideo() {
    navigator.mediaDevices.getUserMedia({ video: true, audio: true })
    .then(stream => {
        localStream = stream;
        document.getElementById("localVideo").srcObject = stream;

        socket.on("user_joined", (data) => {
            console.log(data.name + " joined");
            startCall();
        });

        socket.on("user_left", (data) => {
            console.log(data.name + " left");
            endCall();
        });

        socket.on("receive_message", (data) => {
            document.getElementById("chat-box").innerHTML += `<p><strong>${data.name}:</strong> ${data.message}</p>`;
        });
    });
}

function startCall() {
    peerConnection = new RTCPeerConnection(servers);
    localStream.getTracks().forEach(track => peerConnection.addTrack(track, localStream));

    peerConnection.ontrack = (event) => {
        document.getElementById("remoteVideo").srcObject = event.streams[0];
    };
}

function leaveCall() {
    socket.emit("leave_room", { user_id });
    localStream.getTracks().forEach(track => track.stop());
    document.getElementById("video-section").style.display = "none";
}

function sendMessage() {
    const message = document.getElementById("message").value;
    socket.emit("message", { room, name: document.getElementById("name").value, message });
}
