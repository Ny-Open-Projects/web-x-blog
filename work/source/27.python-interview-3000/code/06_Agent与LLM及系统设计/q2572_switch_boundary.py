"""Q2572 切换的生效边界:在途调用按发起时还是结束时政策算。

调用发起时合法、完成时政策已翻黑,结果算不算数?start-check
按发起时政策放行,延迟低但对危险工具不安全;end-check 在完成时
复核,期间翻黑立即作废结果,敏感工具一律推荐 end-check。
"""


class Executor:
    def __init__(self):
        self.policy = {"search": "allow"}
        self.version = 1
        self.events = []

    def flip(self, tool, mode, reason):
        self.policy[tool] = mode
        self.version += 1
        self.events.append("v" + str(self.version) + ":" + tool + "=" + mode + "(" + reason + ")")

    def run(self, tool, semantics, mid_hook=None):
        start_ok = self.policy.get(tool) == "allow"
        if mid_hook:
            mid_hook()  # 模拟工具在途期间政策切换
        end_ok = self.policy.get(tool) == "allow"
        if semantics == "start-check":
            return start_ok
        return start_ok and end_ok


def main():
    ex1 = Executor()
    ex2 = Executor()

    def flip1():
        ex1.flip("search", "deny", "审计叫停")

    def flip2():
        ex2.flip("search", "deny", "审计叫停")

    r1 = ex1.run("search", "start-check", flip1)
    r2 = ex2.run("search", "end-check", flip2)
    assert r1 is True and r2 is False
    assert ex1.version == 2 and ex2.version == 2
    print("start-check 在途放行:", r1, "← 危险工具不安全")
    print("end-check 完成时复核:", r2, "← 结果作废,敏感工具推荐")
    print("切换事件:", ex2.events)


if __name__ == "__main__":
    main()
