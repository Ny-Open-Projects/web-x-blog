"""部分失败的补偿事务: 每步登记逆操作, 失败逆序补偿"""

class Flow:
    def __init__(self):
        self.done = []   # (描述, 逆操作)

    def step(self, desc, do, undo):
        try:
            do()
        except Exception as e:
            print("  步骤[%s]失败: %s" % (desc, e))
            self.rollback_all()
            return False
        self.done.append((desc, undo))
        print("  步骤[%s]成功" % desc)
        return True

    def rollback_all(self):
        for desc, undo in reversed(self.done):
            undo()
            print("  补偿[%s]完成" % desc)

class Booking:
    def __init__(self):
        self.seat = "free"
        self.points = 100

    def lock(self):
        self.seat = "locked"
    def unlock(self):
        self.seat = "free"
    def deduct(self):
        if self.points - 500 < 0:
            raise ValueError("积分不足")
        self.points -= 500
    def refund(self):
        self.points += 500          # 幂等前提: 与扣减严格配对
    def issue(self):
        raise RuntimeError("出票服务 5xx")

bk = Booking()
flow = Flow()
print("预订流程开始")
flow.step("锁座", bk.lock, bk.unlock)
flow.step("扣积分", bk.deduct, bk.refund)
flow.step("出票", bk.issue, None)
flow.rollback_all()                 # 补偿重复执行验证幂等
print("终态 座位=%s 积分=%d <- 与初始等价" % (bk.seat, bk.points))
print("补偿必须幂等且可重试, 补偿失败要落表重试, 不可逆动作不进同步流程")
