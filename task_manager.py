'''
Example:

def hello(name, task):
    print('hello, %s!' % name)
    print('flag: %s' % task.flag)
    if name == "li huan":
        task.set_flag(True)


tm = TaskMgr()
tm.add_task(Task(hello, "li huan"))
tm.add_task(Task(hello, "he jianhong"))
tm.start()
'''
from apscheduler.schedulers.background import BlockingScheduler
from datetime import datetime


class Moment:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


class Task:
    def __init__(self, func, params):
        self.func = func
        self.params = params
        self.flag = True

    def run(self):
        self.func(self.params, self)

    def set_flag(self, flag):
        self.flag = flag


class TaskMgr:
    def __init__(self):
        self.scheduler = BlockingScheduler()
        self.update_time = Moment(hour=0, minute=0, second=0)
        self.list_task = []

    def add_task(self, task):
        self.list_task.append(task)

    def set_moment(self, hour):
        self.update_time.hour = hour

    def _at_the_moment(self):
        now = datetime.now()
        option_moment = datetime(year=now.year, month=now.month, day=now.day, hour=0, minute=0, second=0)
        option_moment = option_moment.replace(hour=self.update_time.hour)
        return self._time_equal(t1=now.timestamp(), t2=option_moment.timestamp(), delta=30)

    def _time_equal(self, t1, t2, delta):
        if t1 > t2 - delta and t1 < t2 + delta:
            return True
        return False

    def _cron(self):
        for task in self.list_task:
            if self._at_the_moment() or not task.flag:
                task.run()

    def start(self, run_immedately=True):
        try:
            if run_immedately:
                for task in self.list_task:
                    task.run()
            self.scheduler.add_job(func=self._cron, trigger='cron', minute=0, second=0)
            self.scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            self.scheduler.shutdown()
