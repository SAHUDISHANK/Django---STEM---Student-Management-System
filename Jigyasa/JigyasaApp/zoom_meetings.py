import jwt
import requests
import json
from time import time

# Enter your API key and your API secret

API_KEY = 'sr9jnMHjQ7OOpKHRcdUMhQ'
API_SEC = '1KovySSvFWo8BIShgl3Tc5H786tIgUUnkSWJ'

# create a function to generate a token
# using the pyjwt library


def generateToken():
    token = jwt.encode(

        # Create a payload of the token containing
        # API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},

        # Secret used to generate token signature
        API_SEC,

        # Specify the hashing alg
        algorithm='HS256'
    )
    return token
# create json data for post requests
# send a request with headers including
# a token and meeting details

def createMeeting(meetingdetails):
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings', 
      headers=headers, data=json.dumps(meetingdetails))
    y = json.loads(r.text)
    return y

meetingdetails = {
                        'host_email': 'sahudishank@gmail.com',
                        'schedule_for':'sahudishank@gmail.com',
                        "topic":'Dishanks meeting',
                        "type": 2,
                        "start_time":  " 2021/11/08 T 23:12",
                        "duration": "45",
                        "timezone": "Asia/Calcutta",
                        "agenda": "test",
                        'password': '12345',
                        "recurrence": {"type": 1,
                                        "repeat_interval": 1
                                    },
                        "settings": {
                            "host_video": "true",
                            "participant_video": "true",
                            "join_before_host": "False",
                            "mute_upon_entry": "False",
                            "watermark": "true",
                            "audio": "voip",
                            "auto_recording": "cloud"
                            },
                        "registrants_email_notification": "true"
                        }




createMeeting(meetingdetails)