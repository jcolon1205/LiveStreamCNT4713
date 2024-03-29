from flask import Flask,render_template, Response
import cv2


app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/LiveStream/", methods=['POST'])
def move_LiveStream():
    #Moving forward code
    LiveStream_message = "Moving LiveStream..."
    return render_template('LiveStream.html', LiveStream_message=LiveStream_message)

@app.route("/Speakers/", methods=['POST'])
def move_Speakers():
    Speakers_message = "Moving Speakers..."
    return render_template('Speakers.html', Speakers_message=Speakers_message)
    

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)