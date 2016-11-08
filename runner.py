#!/usr/bin/env python
import rumps
import os
import threading
 
 
class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Awesome App", "Title")
        tail(self)
 
 
def tail(self):
    threading.Timer(5, tail, [self, ]).start()
    self.title = os.popen("/sbin/route get default | awk '/gateway/ {printf \"gw:%s\",$3}'").read()[0:-1][0:50]
 
AwesomeStatusBarApp().run()
