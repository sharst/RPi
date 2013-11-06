import subprocess, select
import pylab as pp
import numpy as np
from multiprocessing import Process, Queue
from Queue import Empty
from steering import steering

def readData(hook, line):
    
    if hook in line:
        # This line might look different for other phones!!
        data = line.split()[-1]
        if data == 'true': data = 1.
        if data == 'false': data = 0.
        else: 
            try: data = float(data)
            except ValueError: data = None
        
    else:
        data = None
    return data


def read(q, hooks):
    #hooks = sys.argv[1:]
    data = {}
    for hook in hooks: data[hook]=None
    
    command = ["./adb_pc","logcat", "-s"]  #  replace by adb executable for RPi
    command.extend(hooks)
    print command


    p1 = subprocess.Popen(command, stdout=subprocess.PIPE)


    while True:
        rlist, _, _ = select.select([p1.stdout],[],[])
        for stdout in rlist:
            line = stdout.readline()
            #print line
            for hook in hooks:
                dat = readData(hook, line)
                if dat is not None:
                    data[hook] = dat
                    
            # Put data into queue for other thread.
            try: q.get(0)
            except Empty: pass
            q.put(data)

class autonomous():
    def __init__(self):
        self.q = Queue(maxsize = 1)
        p = Process(target=read, args=(self.q,["LON","LAT","AZI","FIE","ACC"]))  # provide a list of hooks here.
        p.start()
        
        self.steer = steering()
        self.stayAt(0)
        

    def stayAt(self,deg):
        while 1:
            try:
                azi = self.q.get(0)['AZI']
            except Empty: pass
            
            # Make the strength of steering relative to angle
            direction = np.sin(np.radians((azi-deg)/2.))*100
            if direction < 30: direction = 30
            
            self.steer([direction,50])





