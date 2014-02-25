#main entrance point of execution
import observer_frames
from mainFrame import FGFrame
import wx
import time
import sys
import os
import stomp
import wx.html2
import messaging

class MyListener(object):
  
    def __init__(self, conn, frame):
        self.conn = conn
        self.count = 0
        self.start = time.time()
        self.frame = frame
  
    def on_error(self, headers, message):
        print('received an error %s' % message)

    def on_message(self, headers, message):
        self.frame.updateFGObjs(message)
        if message == "SHUTDOWN":   
            diff = time.time() - self.start
            print("Received %s in %f seconds" % (self.count, diff))
            conn.disconnect()
            sys.exit(0)
        else:
            if self.count==0:
                self.start = time.time()
        
            self.count += 1
            print("Received %s message: %s" % (self.count,message))

class FGTCMApp(wx.App):
    def OnInit(self):
        self.frame = FGFrame(None, size=(1024,700), title = "Traffic Control Monitor")
        user = os.getenv("ACTIVEMQ_USER") or "admin"
        password = os.getenv("ACTIVEMQ_PASSWORD") or "password"
        host = os.getenv("ACTIVEMQ_HOST") or "localhost"
        port = os.getenv("ACTIVEMQ_PORT") or 61613
        conn2 = stomp.Connection(host_and_ports = [(host, port)])
        conn2.set_listener('', MyListener(conn2,self.frame))
        conn2.start()
        conn2.connect(login=user,passcode=password)
        conn2.subscribe(destination="TEST.FOO", id=1, ack='auto')
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = FGTCMApp(False)

    app.MainLoop()
