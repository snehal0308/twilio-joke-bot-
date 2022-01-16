from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import pyjokes
app = Flask(__name__)

jokes = pyjokes.get_joke(language="en", category="neutral")
default_msgs = 'Hi There! \n I am a joke bot \n Type (Tell a joke) to get a joke '

@app.route("/sms", methods=['POST'])
def sms_reply():

    msg = request.form.get('Body').lower()
    resp = MessagingResponse()


    if msg == 'Tell a joke'.lower(): 
        resp.message(jokes)
    else:
        resp.message(default_msgs)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)