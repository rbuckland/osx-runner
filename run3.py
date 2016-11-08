#!/usr/bin/python

import yaml 
import rumps
import os
import threading


class OSXRunner(rumps.App):
    def __init__(self, cfg):
        menu_entries = menu = map(lambda x: x['name'], cfg['menuitems'])
        super(OSXRunner, self).__init__(name = "run3", title = None, icon = 'runner.png', menu = menu_entries)

    def set_menu_items(self, items):
        for i in items:
            rumps.MenuItem(i['name'])
            print i['name']

#    @rumps.clicked("Preferences")
#    def prefs(self, _):
#        rumps.alert("jk! no preferences available!")        

def tail(self):
    threading.Timer(5, tail, [self, ]).start()
    self.title = os.popen("/sbin/route get default | awk '/gateway/ {printf \"gw:%s\",$3}'").read()[0:-1][0:50]

def load_config(path):
    return yaml.load(file(path, 'r'))

if __name__ == '__main__':

    cfg = load_config('run3.yml')
    OSXRunner(cfg).run()
