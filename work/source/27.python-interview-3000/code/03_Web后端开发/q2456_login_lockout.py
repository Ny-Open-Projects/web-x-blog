"""登录失败锁定: 计数窗口 与 锁定期(纯标准库)。"""
import time


class Lockout:
    """同一身份在 window 秒内失败 max_fails 次则锁定 lock 秒。"""

    def __init__(self, max_fails=5, window=900, lock=900, now=time.time):
        self.max_fails, self.window, self.lock = max_fails, window, lock
        self.now = now
        self.fails = {}                          # ident -> [失败时刻]

    def _prune(self, ident):
        horizon = self.now() - self.window
        self.fails[ident] = [t for t in self.fails.get(ident, []) if t > horizon]

    def fail(self, ident):
        self._prune(ident)
        self.fails.setdefault(ident, []).append(self.now())

    def locked(self, ident):
        """锁定判定必须在验证密码之前做。"""
        self._prune(ident)
        recent = self.fails.get(ident, [])
        if len(recent) >= self.max_fails:
            return True, max(recent) + self.lock - self.now()
        return False, 0.0

    def success(self, ident):
        self.fails.pop(ident, None)


clock = {"now": 1000.0}
guard = Lockout(max_fails=5, window=900, lock=900, now=lambda: clock["now"])


def login(ident, password_ok):
    locked, retry_in = guard.locked(ident)
    if locked:
        return "locked", "已锁定, 剩余 {:.0f} 秒".format(retry_in)
    if password_ok:
        guard.success(ident)
        return "ok", "登录成功"
    guard.fail(ident)
    return "fail", "用户名或密码错误"


for i in range(1, 6):
    state, msg = login("bob", False)
    print("第 {} 次失败 -> {} {}".format(i, state, msg))
state, msg = login("bob", True)                  # 即使密码正确也拒绝
print("密码正确也拒绝 -> {} {}".format(state, msg))
assert state == "locked"

clock["now"] = 1000.0 + 899                       # 还在锁定期内
state, msg = login("bob", True)
assert state == "locked"
clock["now"] = 1000.0 + 901                       # 锁定期结束
state, msg = login("bob", True)
print("锁定期结束   -> {} {}".format(state, msg))
assert state == "ok"

state, msg = login("alice", False)
print("其他身份不受牵连 -> {} {}".format(state, msg))
assert state == "fail"
print("要点: 失败计数带滑动窗口避免永久误伤, 锁定判定先于密码验证, "
      "成功登录清零计数, 高危系统还应叠加验证码与设备指纹")
