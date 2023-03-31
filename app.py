import os
import time
import glob
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

def fileprosses():
    os.system('cmd /c "git add . && git commit -m "test" && git push orgin master"')
    print("fileprosses")

files = [i for i in glob.glob('*')]
for i in files:
    file = FileModified(i, fileprosses)
    file.start()
