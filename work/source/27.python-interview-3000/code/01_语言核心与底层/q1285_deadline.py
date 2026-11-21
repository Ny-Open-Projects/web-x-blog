import time


class DeadlineExceeded(Exception):
    pass


class Deadline:
    def __init__(self, seconds=None, parent=None):
        if parent is not None:
            left = parent.remaining()
            seconds = left if seconds is None else min(seconds, left)
        self._at = None if seconds is None else time.perf_counter() + seconds

    def remaining(self):
        if self._at is None:
            return None
        return self._at - time.perf_counter()

    def check(self, point=""):
        left = self.remaining()
        if left is not None and left <= 0:
            raise DeadlineExceeded("deadline exceeded at " + point)


def do_step(deadline, name, cost):
    deadline.check(name)
    time.sleep(cost)
    deadline.check(name + " after")


if __name__ == "__main__":
    dl = Deadline(0.15)
    do_step(dl, "step1", 0.05)
    print("step1 ok, remaining: %.2fs" % dl.remaining())
    try:
        do_step(dl, "step2", 0.2)          # 超出整体预算
    except DeadlineExceeded as e:
        print("stopped ->", e)
    child = Deadline(parent=dl, seconds=10)
    print("child inherits tighter parent: %.2fs" % child.remaining())
