from chatapp import app,socketio
from flask import render_template,jsonify


@app.route('/')
def session():
    return render_template('main.html')

def MessageRev(method=['GET','POST']):
    return('message was there')

@socketio.on('event')
def custom_event(json, method=['GET','POST']):
    print('recieved event: '+str(json))
    socketio.emit("response",json,callback=MessageRev)
