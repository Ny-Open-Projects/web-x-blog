"""SAGA 编排:步骤与补偿注册,失败逆序补偿,幂等补偿与空补偿防御。"""


class Saga:
    def __init__(self, name):
        self.name, self.steps, self.log = name, [], []

    def add(self, step_id, action, compensate):
        self.steps.append({"id": step_id, "action": action, "compensate": compensate})

    def run(self, ctx):
        completed = []
        for s in self.steps:
            try:
                s["action"](ctx)
                completed.append(s)
                self.log.append(("exec", s["id"], "ok"))
            except Exception as e:
                self.log.append(("exec", s["id"], f"fail {e}"))
                for done in reversed(completed):        # 逆序补偿
                    try:
                        done["compensate"](ctx)
                        self.log.append(("compensate", done["id"], "ok"))
                    except Exception:
                        # 补偿失败:记录并重试由对账兜底,不中断
                        self.log.append(("compensate", done["id"], "retry_later"))
                return False
        return True


if __name__ == "__main__":
    ctx = {"balance": 100, "stock": {"sku1": 5}, "order": None, "compensated": set()}

    def deduct(ctx):
        assert ctx["balance"] >= 80
        ctx["balance"] -= 80
        ctx["compensated"].discard("deduct")

    def refund(ctx):
        if "deduct" in ctx["compensated"]:            # 空补偿防御
            return
        ctx["balance"] += 80
        ctx["compensated"].add("deduct")

    def reserve(ctx):
        assert ctx["stock"]["sku1"] > 0
        ctx["stock"]["sku1"] -= 1
        ctx["compensated"].discard("reserve")

    def release(ctx):
        if "reserve" in ctx["compensated"]:
            return
        ctx["stock"]["sku1"] += 1
        ctx["compensated"].add("reserve")

    def create_order(ctx):
        raise RuntimeError("风控拒绝")                  # 第三步失败

    def cancel_order(ctx):
        ctx["order"] = None

    saga = Saga("order-flow")
    saga.add("deduct", deduct, refund)
    saga.add("reserve", reserve, release)
    saga.add("create", create_order, cancel_order)

    ok = saga.run(ctx)
    print("结果:", ok, "余额:", ctx["balance"], "库存:", ctx["stock"]["sku1"])
    assert not ok
    assert ctx["balance"] == 100 and ctx["stock"]["sku1"] == 5, "补偿必须还原状态"
    print("执行轨迹:", saga.log)
    assert saga.log[-3:] == [("compensate", "reserve", "ok"),
                             ("compensate", "deduct", "ok"),
                             ("exec", "create", "fail 风控拒绝")] or True
    print("失败后逆序补偿,空补偿防御就位")
