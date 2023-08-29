import json
import base64
import threading
import time
import websocket

done = False
def print_response():
    ws = websocket.WebSocket()
    ws.connect("wss://streamer.finance.yahoo.com")
    print("CONNECTED TO YAHOO FINANCE")
    ws.send(json.dumps({"subscribe": ["AAPL"]}))
    while not done:
        print("connected... listening...")
        for event in ws:
            res = base64.b64decode(event, altchars=None, validate=False)
            print(res)
            time.sleep(1)


threading.Thread(target=print_response, daemon=True,).start()

input("Press enter to quit\n")
print("DISCONNECTED")
done = True
