'''
Declaration:

1. Excute the task at 0:00(UTC) everyday which could be set by TaskMgr.set_moment;
2. If the last one fails to set flag, execute the task every hour until it succeeds.
'''


from task_manager import TaskMgr, Task

def hello(name, task):
    print('hello, %s!' % name)
    print('flag: %s' % task.flag)
    if name == "li huan":
        task.set_flag(True)


def main():
    tm = TaskMgr()
    tm.set_moment(hour=9)
    tm.add_task(Task(hello, "li huan"))
    tm.add_task(Task(hello, "he jianhong"))
    tm.start(run_immedately=True)


if __name__ == "__main__":
    main()
