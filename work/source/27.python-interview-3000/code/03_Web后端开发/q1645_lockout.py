"""渐进式锁定: 延迟翻倍、封顶与解锁(纯标准库)。"""

BASE_DELAY, CAP, HARD_LIMIT = 1.0, 3600.0, 10


class Account:
    def __init__(self):
        self.fail_count = 0

    def on_fail(self, now):
        self.fail_count += 1
        if self.fail_count < HARD_LIMIT:
            delay = min(CAP, BASE_DELAY * 2 ** (self.fail_count - 1))
            return f"再试需等待 {int(delay)}s"
        return "账号已锁定, 请通过邮箱解锁或联系客服"

    def on_success(self):
        self.fail_count = 0
        return "计数归零"


acct = Account()
for i in range(4):
    print(f"第{i + 1}次失败:", acct.on_fail(i))
print("成功登录:", acct.on_success(), "fail_count =", acct.fail_count)
for i in range(12):
    acct.on_fail(i)
print("连败 12 次后:", acct.on_fail(12))
print("要点: 渐进延迟让撞库脚本的单位成本指数上升; 锁定话术与限速保持一致, 不给枚举者反馈")
