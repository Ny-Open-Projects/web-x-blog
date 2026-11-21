from functools import partial, partialmethod


class Robot:
    def _move(self, dx, dy, label):
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        return "%s: now at %s" % (label, self.pos)

    move_up = partialmethod(_move, 0, 1, label="up")
    move_down = partialmethod(_move, 0, -1, label="down")

    def _set_mode(self, mode):
        self.mode = mode
        return "mode -> " + mode

    fast = partialmethod(_set_mode, "fast")
    safe = partialmethod(_set_mode, "safe")

    # 反例:partial 不是描述符,这样写调用时会炸(仅作展示)
    broken = partial(_move, 0, 0, label="broken")


if __name__ == "__main__":
    r = Robot()
    r.pos = (0, 0)
    print(r.move_up())
    print(r.move_down())
    r.fast()
    print(r.move_up())
    r.safe()
    print("mode:", r.mode)

    try:
        r.broken()
    except TypeError as err:
        print("partial in class ->", type(err).__name__, "-", err)
