"""
    Basic Flask application for NEU Co-Op Team M1's Project, Sauron
"""

import logging
from flask import Flask, flash

# Make yo app gurl
app = Flask(__name__)

# TODO: Set up logging?

# TODO: You're gonna wanna do some basic config eventually
#app.config()

# Data's gotta come from somehwere, hopefully it isn't mongo
def init_db():
    return

# What, you think you just needed one function?
def connect_db():
    return

# let's try *not* to leak db connections
#@app.teardown_appcontext
def close_db():
    return

# TODO: I'll just leave this here...
#@app.before_request
#def before():
#    return

#@app.after_request
#def after():
    #Probably want to send signal to unlock door or request PIN here?
    #Make sure to log the shit here


@app.route('/found_face', methods=['POST'])
def face_detected():
    """
    Camera will constantly be scanning for faces.
    When it detects one, start querying the database for a face that matches
    :return:
    """
    return

# Do we want this to be one big binary package?
# Or should it be something like user_name, uuid
@app.route('/rfid/', methods=['POST'])
def check_rfid():
    """
    When a student signs into the dorm, they'll give the proctor their card, which has an RFID chip.
    Record the Name and RFID of the user with this card and save it to the flask global variable
    so we can use it with the request we get with the face information
    :return:
    """
    return

def rfid_face_match():
    """
    Check UUID associated with current face (store that in G) and make sure it is the same UUID associated with the
    current RFID.
    If they match, return the signal to unlock the door.
    If they don't match:
      - If the face doesn't match the RFID --- request PIN
      - If the face doesn't match one in the DB --- check again, but that should mean no entry
      - If the RFID isn't found in the DB --- also means no entry
      - If the face can't be found in the images --- request PIN
    :return:
    """
    return

@app.route('/PIN/', methods=['GET', 'POST'])
def check_PIN(name, pin):
    """
    :param name: Name of guest requesting entry
    :param pin: PIN of guest
    :return: True if PIN from DB matches PIN here, else false
    """
    return

#TODO: Still need to add enpoints and logic for guests (non-residents and non-NUID)
#TODO: This is gonna need to be multi-threaded. Gevent?

@app.route('/')
def hello_world():
    return 'yo dawg, I heard you like back ends\n'

if __name__ == '__main__':
    app.run()