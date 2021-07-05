from flask import Flask, render_template, Response
import os
import threading
import cv2
import feed, av
gens = feed.getGenerators()
jpegs = [None]*len(gens)

app = Flask(__name__)

@app.route('/')
def index():
    return Response('OK!')

def fillJpegArray(camid):
    while True:
        frame, frame_info, video_stats = next(gens[int(camid)])
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        jpegs[camid] = (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


def jpegGenerator(camid):
    while True:
        yield jpegs[camid]

@app.route('/cam/<camid>')
def cam(camid):
    return Response(jpegGenerator(int(camid)), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print("Hello World!")
    threads = []
    for i in range(len(gens)):
        threads.append(threading.Thread(target=fillJpegArray, args=[i]))
        threads[i].start()
    app.run(host='0.0.0.0', debug=True, use_reloader=False)