import os
import time
import traceback

class FileModified():
    def __init__(self, file_path, callback):
        self.file_path = file_path
        self.callback = callback
        self.modifiedOn = os.path.getmtime(file_path)

    def start(self):
        while (True):
            time.sleep(0.5)
            modified = os.path.getmtime(self.file_path)
            if modified != self.modifiedOn:
                self.modifiedOn = modified
                if self.callback():
                    break

file = FileModified('test.txt', lambda: os.system('cmd /c "git add . && git commit -m "test" && git push orgin master && git push orgin master"'))
file.start()

