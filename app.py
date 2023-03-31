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

dir_path = "C:\\Users\\melkmeshi\\Documents\\Projects\\Python\\git"
for file_name in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file_name)):
        file_path = os.path.join(dir_path, file_name)
        print(file_path)
        file = FileModified(file_path, lambda: os.system('cmd /c "git add . && git commit -m "test" && git push orgin master"'))
        file.start()