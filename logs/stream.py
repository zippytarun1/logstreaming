import flask
import time

import eventlet
eventlet.monkey_patch()

#this is done to spawn the request

app = flask.Flask(__name__)

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
#reads function will follow the latest stream
def reads():
    logfile = open("D:\logs\output.txt","r")
    loglines = follow(logfile)
    for line in loglines:
        print line
        yield "data: {}\n\n".format(line)

@app.route( '/stream' )
def stream():
    return flask.Response(reads(), mimetype= 'text/event-stream' )
#this function will return data in the form of stream

@app.route('/page')
def get_page():
    return flask.send_file('page.html')

#Streamed data will appear in 127.0.0.1:8080/page

#application will run at 8088 and processes will tell you how many request this webservice can handle at one point of time
if __name__ == "__main__":
    app.run(port=8088,processes=10)
