STDERR=2
STDOUT=1
import os
import sys
import tempfile

class captured:
    def __init__(self, fd=STDERR):
        self.fd = fd
        self.prevfd = None

    def __enter__(self):
        t = tempfile.NamedTemporaryFile()
        print 'Piping your output to ' + t.name
        self.prevfd = os.dup(self.fd)
        os.dup2(t.fileno(), self.fd)
        return t

    def __exit__(self, exc_type, exc_value, traceback):
        os.dup2(self.prevfd, self.fd)


with captured(STDOUT) as tmp:
    os.system('cat imbfile.txt')

print("Captured:", open(tmp.name).read())
