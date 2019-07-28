# Schedule

## Description
A simple example of apschedule


- 1. Excute the task at 0:00(UTC) everyday unconditionly which could be reset by TaskMgr.set_moment;
- 2. If the last one fails to set flag, execute the task every hour until it succeeds.

## Example

```
from task_manager import TaskMgr, Task

def hello(name, task):
    print('hello, %s!' % name)
    print('flag: %s' % task.flag)
    if name == "li huan":
        task.set_flag(True)


tm = TaskMgr()
# Force to excute task at 9:00 everyday unconditionly
tm.set_moment(hour=9)
tm.add_task(Task(hello, "li huan"))
tm.add_task(Task(hello, "he jianhong"))
tm.start(run_immedately=True)


```
