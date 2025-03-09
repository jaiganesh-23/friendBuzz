async_mode = 'eventlet'

import os
import socketio

sio = socketio.Server(async_mode=async_mode,cors_allowed_origins=[
    "http://localhost:5173", 
    "http://127.0.0.1:5173"])

@sio.event
def connection_event(sid, message):
    print('connection_event, message: ', message)
    sio.emit('connection_response', message, sid)

@sio.event
def my_message(sid, message):
    sio.emit('message_response', message)