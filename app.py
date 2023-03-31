import os
import time
import traceback
import threading

class FileModified(threading.Thread):
    def __init__(self, file_path, callback):
        threading.Thread.__init__(self)
        self.file_path = file_path
        self.callback = callback
        self.modifiedOn = os.path.getmtime(file_path)
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            time.sleep(0.5)
            modified = os.path.getmtime(self.file_path)
            if modified != self.modifiedOn:
                self.modifiedOn = modified
                if self.callback():
                    self.stop_event.set()

    def stop(self):
        self.stop_event.set()

dir_path = "/path/to/directory"

for file_name in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file_name)):
        file_path = os.path.join(dir_path, file_name)
        file = FileModified(file_path, lambda: os.system('cmd /c "git add . && git commit -m "test" && git push orgin master"'))
        file.start()
