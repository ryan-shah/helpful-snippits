# By ryan-shah - 2/21/22
from datetime import datetime, timedelta

# Timer for many values
class Timer():
    init = 0
    start_times = {}
    end_times = {}

    def __init__(self):
        self.init = datetime.now()
	self.start_times = {}
	self.end_times = {}

    def __repr__(self):
        diff = (datetime.now() - self.init).total_seconds()*1000
        results = {k:(self.end_times[k] - self.start_times[k]).total_seconds()*1000 for k in self.end_times.keys()}
        str = f"Total Time: {round(diff, 2)}\n"
        for k,v in sorted(results.items()):
            str += f"\t{k}: {round(v, 2)}\n"
        return str


    def start(self, key):
        self.start_times[key] = datetime.now()

    def end(self, key):
        self.end_times[key] = datetime.now()

t = Timer()
t.start('loop')
for i in range(1000):
    continue
t.end('loop')
print(t)
