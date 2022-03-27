from flask import Flask, render_template, request
from Puzzle8 import makeEnvironment
from AStar import Search
from time import sleep
import numpy as np
import os

env = makeEnvironment()

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent=True)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

def call_state():
    global aa,ab,ac,ba,bb,bc,ca,cb,cc

    aa, ab, ac, ba, bb, bc, ca, cb, cc = env()
    

@app.route('/', methods=["GET", "POST"])
def html():
    
    call_state()
    if request.method == "POST":
        if request.form['action'] == "Shuffle":
            env.shuffle()
        elif request.form['action'] == str(aa):
            env.try_move(0,0)
        elif request.form["action"] == str(ab):
            env.try_move(0,1)
        elif request.form["action"] == str(ac):
            env.try_move(0,2)
        elif request.form["action"] == str(ba):
            env.try_move(1,0)
        elif request.form["action"] == str(bb):
            env.try_move(1,1)
        elif request.form["action"] == str(bc):
            env.try_move(1,2)
        elif request.form["action"] == str(ca):
            env.try_move(2,0)
        elif request.form["action"] == str(cb):
            env.try_move(2,1)
        elif request.form["action"] == str(cc):
            env.try_move(2,2)
        elif request.form["action"] == "A* Solver":
            svr = Search(env)

            for act in svr():
                env.action(act)
                sleep(1)
                call_state()
            
        elif request.form["action"] == "Instant Solve":
            env.current_state = np.array([[1,2,3],[4,5,6],[7,8,0]])

            

    call_state()
    return render_template('main.html', aa= aa, ab= ab, ac= ac, \
                                        ba= ba, bb= bb, bc= bc, \
                                        ca= ca, cb= cb, cc= cc, \
                                        warning= env.warning, \
                                        hex= env.color)

if __name__ == '__main__':

    app.run(debug=True)