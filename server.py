from flask import Flask, render_template, Response
import os
import threading
import cv2
import feed
gens = feed.getGenerators()


app = Flask(__name__)

@app.route('/')
def index():
    return Response('OK!')

def gen_frames(camid):
    while True:
        frame, frame_info = next(gens[int(camid)])
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/cam/<camid>')
def cam(camid):
    return Response(gen_frames(camid), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print("Hello World!")
    app.run(host='0.0.0.0', debug=True, use_reloader=False)