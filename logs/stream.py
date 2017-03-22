import flask
import time

import eventlet
eventlet.monkey_patch()

app = flask.Flask(__name__)

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def reads():
    logfile = open("D:\logs\output.txt","r")
    loglines = follow(logfile)
    for line in loglines:
        print line
        yield "data: {}\n\n".format(line)

@app.route( '/stream' )
def stream():
    return flask.Response(reads(), mimetype= 'text/event-stream' )


@app.route('/page')
def get_page():
    return flask.send_file('page.html')

if __name__ == "__main__":
    app.run(port=8088,processes=10)
