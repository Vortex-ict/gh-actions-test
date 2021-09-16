from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#  pip3 install watchdog for these packages to work

import os
import time
import json


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/' + filename
            new_destignation = folder_destination + '/' + filename
            os.rename(src, new_destignation)


folder_to_track = '/Users/renev/test01'
folder_destination = '/Users/renev/test02'

event_handler = MyHandler()

observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
