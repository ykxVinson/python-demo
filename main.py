# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from websocket import create_connection
import websocket
import requests
import json


def on_message(ws, message):
    # print("message")
    print(message)


def on_error(ws, error):
    print("error")
    print(error)


def on_close(ws):
    print("close connection")


def on_open(ws):
    print("websocket connected.")
    print("Is Receiving data, please wait...")


def get_token():
    headers = {'content-type': 'application/json'}
    url = 'http://20.239.19.155:30000/oauth2/token?grant_type=password&password=123456&username=nlu&client_id=maxnerva1&client_secret=maxnerva-secret'
    params = {'grant_type': 'password', 'password': '123456', 'username': 'nlu', 'client_id': 'maxnerva1', 'client_secret': 'maxnerva-secret'}
    response = requests.post(url, data=params, headers=headers)
    if response.status_code == 200:
        item = json.loads(response.text)
        return item['access_token']
    return ''


def test_vehicle_twin(token):
    url = 'ws://20.239.127.120:10088/vehicle/state?vin=VSIM_vhsim0_1'
    ws = websocket.WebSocketApp(url,
                                header=["token:" + token,
                                        "mode:pwd",
                                        "client_id:maxnerva1",
                                        "client_secret:maxnerva-secret"],
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


if __name__ == '__main__':
    token = get_token()
    if token:
        print("token: ", token)
        test_vehicle_twin(token)
    else:
        print("Token is NULL.")



