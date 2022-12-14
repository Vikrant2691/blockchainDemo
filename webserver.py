# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer

import json
import time
import requests


# import all the functions from our function file
from web3helpers import *


hostName = "0.0.0.0"
serverPort = 8081

class MyServer(BaseHTTPRequestHandler): 
    def do_GET(self):
        self.send_response(200) 
        self.send_header("Content-type", "text/html") 
        self.end_headers() 
        self.wfile.write(bytes("<html><head><title>ETH APIGET</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8")) 
        self.wfile.write(bytes("<body>", "utf-8")) 
        self.wfile.write(bytes("<p>This is an example web server.</p>","utf-8"))

    def do_POST(self):
        
        self.query_string =self.rfile.read(int(self.headers['Content-Length'])) 
        data = json.loads(self.query_string)

        if self.path=="/eth":
            amount = data["amount"] 
            address = data["address"] 
            status=ethTransfer(address, amount)
            if(status):
                self.send_response(201) 
                self.send_header("Content-type", "text/html") 
                self.end_headers() 
                self.wfile.write(bytes("<html><head><title>Transfer Success</title></head>"+
                "<body>The amount of "+str(amount)+" was sent to address "+str(address)+"</body><html>", "utf-8")) 
            else:
                self.send_response(503) 
                self.send_header("Content-type", "text/html") 
                self.end_headers()
                self.wfile.write(bytes("<html><head><title>Transfer Failure</title></head>"+
                "<body>The amount transfer of "+str(amount)+" was not sent to address "+str(address)+" due an error </body><html>", "utf-8")) 
        if self.path=="/token": 
            address = data["address"] 
            status=tokenTransfer(address)
            if(status):
                self.send_response(201) 
                self.send_header("Content-type", "text/html") 
                self.end_headers() 
                self.wfile.write(bytes("<html><head><title>Transfer Success</title></head>"+
                    "<body>The amount was sent to address "+str(address)+"</body><html>", "utf-8")) 
            else:
                self.send_response(503) 
                self.send_header("Content-type", "text/html") 
                self.end_headers() 
                self.wfile.write(bytes("<html><head><title>Transfer Failure</title></head>"+
                "<body>The amount was not sent to address "+str(address)+" due an error </body><html>", "utf-8"))


if __name__ == "__main__":        
    # tokenTransfer("0x972e91330E79b111e1eFB878009Bd851339526Cd")
    # ethTransfer("0x972e91330E79b111e1eFB878009Bd851339526Cd", 1000)
    

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

# curl command for token transfer
# curl --header "Content-Type: application/json" --request POST --data '{"address":"0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C"}' http://localhost:8080/token

# curl command for eth transfer
# curl --header "Content-Type: application/json" --request POST --data '{"address":"0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C", "amount":"0.05"}' http://localhost:8080/eth

# basic curl check
# curl http://localhost:8080/amiworking