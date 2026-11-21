---
title: [Q7597] SAGA 补偿在 LLM 工具调用链的落地
date: 2026-11-19
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7597 · LLM 工具链的 SAGA 补偿

> 难度:★★★ | 标签:SAGA, 补偿事务, 事故复盘

**问**：Agent 执行「创建云资源 → 配置 DNS → 通知用户」三步工具链，第二步失败——不补偿会留下什么（半成品资源与幽灵状态）？每个工具的「补偿动作」怎么定义（哪些工具天然不可补偿），补偿自身的失败怎么处理（补偿风暴与死信），LLM 编排层怎么记录执行日志才支持事后补偿？

**答**：① 半成品问题：工具链步骤间无事务，第二步失败后「资源已创建但 DNS 没配」——用户视角是幽灵状态（资源存在但不可用），且下次重试可能再建一个资源（重复扣费）。② SAGA 在工具链的映射：**每个带副作用的工具必须声明补偿对**（`create_resource` ↔ `delete_resource`；`send_email` 是**不可补偿**的——邮件发出去收不回，所以它必须在链路末端或加「预检查 + 确认门」）；不可补偿工具的纪律：**放最后一步**（前面全失败不影响它）+ 幂等键防重发。③ 补偿自身失败：删除资源时 API 超时——补偿进重试队列（指数退避），N 次失败转**死信**（人工介入清单 + 期末对账任务兜底扫半成品资源）——补偿风暴的防法与业务重试同构（A101 预算）。④ 编排层执行日志：每步记录 `{step, tool, args, result, saga_id}` 持久化（DB/发件箱），崩溃恢复时按日志重放或补偿——「日志先行」是补偿可行的前提。

```python
# 全部标准库；demo 实现 SAGA 编排：补偿对注册 + 崩溃恢复 + 死信
import json, time

class Saga:
    """日志先行的 SAGA：步骤持久化 → 失败逆向补偿 → 补偿失败进死信。"""
    def __init__(self, saga_id: str, log, dlog: list):
        self.id, self.log, self.dlog = saga_id, log, dlog   # log 持久化（demo 用 list）
        self.steps: list[dict] = []
    def step(self, name: str, action, compensate=None):
        self.steps.append({"name": name, "run": action, "undo": compensate})

    def run(self, ctx: dict) -> dict:
        done = []
        for s in self.steps:
            try:
                out = s["run"](ctx)
                self.log.append({"saga": self.id, "step": s["name"],
                                 "args": ctx.get("audit", {}), "result": "ok"})
                done.append(s)
            except Exception as e:
                self.log.append({"saga": self.id, "step": s["name"], "result": f"fail:{e}"})
                return self.compensate(done, ctx)
        return {"status": "done"}

    def compensate(self, done: list, ctx: dict):
        for s in reversed(done):                 # 逆向补偿
            try:
                if s["undo"]:
                    s["undo"](ctx)
                    self.log.append({"saga": self.id, "step": f"undo:{s['name']}", "result": "ok"})
            except Exception as e:
                self.dlog.append({"saga": self.id, "step": s["name"], "err": str(e)})  # 死信
                self.log.append({"saga": self.id, "step": f"undo:{s['name']}", "result": "dead"})
        return {"status": "compensated", "dead_letter": len(self.dlog)}

def make_world():
    resources, dns, mails, dlog = [], [], [], []
    def create_res(ctx): resources.append(ctx["name"]); return resources[-1]
    def del_res(ctx): resources.remove(ctx["name"])
    def config_dns(ctx): raise TimeoutError("DNS API 超时")        # 第二步失败触发补偿
    def send_mail(ctx):
        if ctx["mail"] not in mails: mails.append(ctx["mail"])    # 幂等键
    return resources, dns, mails, dlog

if __name__ == "__main__":
    resources, dns, mails, dlog = make_world()
    saga = Saga("s-1", log=[], dlog=dlog)
    saga.step("create", create_res, del_res)                     # 可补偿对
    saga.step("dns", config_dns, None)
    saga.step("mail", send_mail, None)                           # 末端不可补偿工具
    result = saga.run({"name": "vm-42", "mail": "user@x.com"})
    print(result)                                                # compensated
    assert resources == [], "第一步已回滚，无半成品资源 ✅"
    assert mails == [], "邮件在失败步骤之后，从未发出 ✅"
    print("执行日志:", saga.log[:2], "...（日志先行，事后可审计/重放）")
    # 不可补偿工具纪律：放末端 + 幂等键 + 前置确认门（Q7516）；
    # 死信兜底：人工清单 + 期末对账扫描「有资源无 DNS」的幽灵状态。
```

**追问**：1) 为什么不可补偿工具必须放链路末端？——SAGA 的补偿从失败点逆向回滚，「末端」意味着它执行时前面全部成功、它自己失败也无须补偿别人（它自己不可补偿，失败即全链失败但无残留副作用）。2) 补偿与重试的边界怎么划？——瞬时错误（超时/限流）重试原步骤；确定性失败（参数错/配额不足）转补偿——分类靠错误类型（Q6512 口径），盲目「失败就重试」会放大半成品。3) 并发 SAGA 之间的资源冲突怎么防？——资源创建加业务幂等键（name=uuid），同名冲突走唯一约束拒绝（Q6517）；编排层对同一目标资源的并发 saga 串行化（锁/队列）。

## 背诵要点
1. 工具链无事务：第二步失败留半成品 + 重试重复扣费——带副作用的工具链必须 SAGA。
2. 补偿对注册（create↔delete）；不可补偿工具（邮件/支付）放末端 + 幂等键 + 确认门。
3. 补偿失败进死信（人工清单+对账扫描幽灵状态）；执行日志先行（每步持久化）是补偿可行的前提。

## 复盘追问
1. 补偿动作本身有副作用（delete_resource 发了审计事件），业务上「看起来像删了又建」，产品怎么接受？（提示：对账口径以终态为准（资源净额=0）+ 审计事件带 saga_id 关联展示为一次失败的尝试，而非两次操作）
2. LLM 决定「跳过补偿直接重试」怎么防？（提示：补偿逻辑在编排代码层（确定性），不在模型提示层——LLM 只决定业务路径，崩溃恢复/补偿是系统职责，模型不可越权）
