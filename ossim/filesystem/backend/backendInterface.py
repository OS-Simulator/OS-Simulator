from .status import Status
from .status2 import Status2
import random
from operator import itemgetter

class file:
    def __init__(self):
        self.name = ""
    def addname(self, name):
        self.name = name;

class folder:
    def __init__(self):
        self.files =  [ ]
        self.dirs = [ ]
        self.name = ""
        self.fsize = 0
        self.dsize = 0
    def addfile(self, name):
        temp = file()
        temp.addname(name)
        self.files.append(temp)
        self.fsize += 1
    def addname(self, name):
        self.name = name
    def adddir(self, name):
        temp = folder()
        temp.addname(name)
        self.dirs.append(temp)
        self.dsize += 1

class Tree:
    def __init__(self):
        self.root = folder()
        self.root.addname('root')
        self.cur_dir = self.root
        self.path = [ ]
        self.path.append(self.root.name)
    def passCmd(self, p, cmd):
        Status.flag = 0
        if(cmd == "cd"):
            # if(cur_dir == ""):
            N = len(p)
            self.cur_dir = self.root
            for i in range(N-1):
                dirname  = p[i+1]
                for d in self.cur_dir.dirs:
                    if d.name == dirname:
                        self.cur_dir = d
            # else:
                # print("Invalid")
        if(cmd == "touch"):
            filename = p[-1]

            for i in range(self.cur_dir.fsize):
                if filename == self.cur_dir.files[i].name:
                    Status.flag = 1

            if Status.flag == 0:
                self.cur_dir.addfile(filename)

            p = p[0:len(p)-1]

        if(cmd == "rm"):
            filename = p[-1]
            self.cur_dir.files = [ f for f in self.cur_dir.files if f.name != filename]
            self.cur_dir.fsize -= 1
            p = p[0:len(p)-1]

        if(cmd == "mkdir"):
            dirname = p[-1]
            for i in range(self.cur_dir.dsize):
                if dirname == self.cur_dir.dirs[i].name:
                    Status.flag = 1

            if Status.flag == 0:
                self.cur_dir.adddir(dirname)
            p = p[0:len(p)-1]

        if(cmd == "rmdir"):
            dirname = p[-1]
            self.cur_dir.dirs = [u for u in self.cur_dir.dirs if u.name != dirname ]
            self.cur_dir.dsize -= 1
            p = p[0:len(p)-1]

        Status.filelis = [u.name for u in self.cur_dir.files] + [u.name for u in self.cur_dir.dirs]
        Status.path = p

class Two:
    def __init__(self):
        self.root = folder()
        self.root.addname('root')
        self.cur_dir = self.root
    def passCmd(self, path, cmd):
        Status2.flag = 0
        Status2.flag1 = 0
        Status2.flag2 = 0
        if(cmd == "cd"):
            # if(cur_dir == ""):
            N = len(path)
            self.cur_dir = self.root
            for i in range(N-1):
                dirname  = path[i+1]
                for d in self.cur_dir.dirs:
                    if d.name == dirname:
                        self.cur_dir = d
            # else:
                # print("Invalid")
        if(cmd == "touch"):
            filename = path[-1]
            if self.cur_dir.name == 'root':
                Status2.flag1 = 1

            else:
                for i in range(self.cur_dir.fsize):
                    if filename == self.cur_dir.files[i].name:
                        Status2.flag = 1

                if Status2.flag == 0:
                    self.cur_dir.addfile(filename)
            path = path[0:len(path)-1]

        if(cmd == "rm"):
            filename = path[-1]
            self.cur_dir.files = [ f for f in self.cur_dir.files if f.name != filename]
            self.cur_dir.fsize -= 1
            path = path[0:len(path)-1]

        if(cmd == "mkdir"):
            dirname = path[-1]
            if self.cur_dir.name != 'root':
                Status2.flag2 = 1

            else:
                for i in range(self.root.dsize):
                    if dirname == self.root.dirs[i].name:
                        Status2.flag = 1

                if Status2.flag == 0:
                    self.root.adddir(dirname)
            path = path[0:len(path)-1]

        if(cmd == "rmdir"):
            dirname = path[-1]
            self.root.dirs = [u for u in self.root.dirs if u.name != dirname ]
            self.root.dsize -= 1
            path = path[0:len(path)-1]

        Status2.filelis = [u.name for u in self.cur_dir.files] + [u.name for u in self.cur_dir.dirs]
        Status2.path = path
#
# def BackendInterface(path, command):
#     if(command == 'mkdir' or command=='touch'):
#         Status.filelis.append(path[-1])
#
#     elif(command == 'rmdir' or command == 'rm'):
#         Status.filelis.remove(path[-1])
#
#     elif(command == 'cd'):
#         Status.path = path
#         num = random.randrange(1, 10)
#         Status.filelis=[]
#         for i in range(num+1):
#             Status.filelis.append('Folder ' + str(i))
