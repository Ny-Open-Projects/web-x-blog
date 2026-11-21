---
title: [Q1559] fail-fast 与错误聚合:校验错误的两种收场
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1559 · fail-fast 与错误聚合:校验错误的两种收场

> 难度:★★★☆☆ | 标签:校验, 错误处理, 设计模式

**问**:表单/配置校验要一次报出所有错误,还是第一个错就停?两种模式的代码结构差在哪?

**答**:fail-fast 与错误聚合按「错是谁犯的」分野:程序员的错(契约破坏、内部不变量)fail-fast,第一个错就抛、栈是现场;用户的错(表单、配置、批处理)聚合,一次报全所有问题,逐条修复体验最好。聚合器结构:每条校验独立判定不互相中断,结果收集成结构化错误对象列表(字段、消息、实际值),全部通过才执行主逻辑。要点:① 错误对象别用裸 str——前端定位、i18n、测试断言都靠结构化字段;② 报告按输入顺序排列,保证可复现;③ 混合策略:格式类错误继续收集,结构类致命错误(文件不存在、连接失败)立即 fail-fast;④ 聚合不等于吞——收集完无错才放行,有错就以汇总异常或非零退出收场。

```python
# file: code/01_语言核心与底层/q1559_error_aggregation.py


class FieldError:
    def __init__(self, field, message, value):
        self.field = field
        self.message = message
        self.value = value

    def __repr__(self):
        return "%s: %s (got %r)" % (self.field, self.message, self.value)


def validate_config(cfg):
    """聚合所有错误,而不是第一个就抛。"""
    errors = []

    def check(field, predicate, message):
        value = cfg.get(field)
        if not predicate(value):
            errors.append(FieldError(field, message, value))

    def is_int(value):
        try:
            return value == int(value)
        except (TypeError, ValueError):
            return False

    def is_nonempty(value):
        return isinstance(value, str) and value.strip() != ""

    check("port", lambda v: is_int(v) and 1 <= int(v) <= 65535,
          "必须是 1-65535 的整数")
    check("host", is_nonempty, "host 不能为空")
    check("retries", lambda v: is_int(v) and int(v) >= 0, "必须是非负整数")
    check("mode", lambda v: v in ("dev", "prod"), "mode 只能是 dev 或 prod")
    return errors


if __name__ == "__main__":
    bad_cfg = {"port": "99999", "host": "  ", "retries": -1, "mode": "qa"}
    errors = validate_config(bad_cfg)
    print("%d 个错误, 一次报全:" % len(errors))
    for e in errors:
        print("  -", e)

    good_cfg = {"port": 5432, "host": "db.internal", "retries": 3, "mode": "prod"}
    print("good cfg errors:", validate_config(good_cfg))

    # fail-fast 对比:结构类致命错误立即抛
    try:
        raise FileNotFoundError("config.yaml 不存在")
    except FileNotFoundError as err:
        print("fatal, fail-fast:", err)
```

**追问**:1) 错误聚合的对象该是 str 还是结构体?——结构体(字段、消息、期望值),前端定位与 i18n 都靠它;str 只该在最终展示层拼接。2) fail-fast 与聚合怎么选?——流程型失败(第 1 步错后面全没意义)fail-fast;表单/批量校验聚合全部错误一次返回——用户体验与修复成本决定;混合场景:聚合校验、fail-fast 执行。3) 聚合结构设计?——errors 是 (field, code, message, expected) 列表,一次 raise ValidationError(errors);错误码稳定(前端/监控依赖),消息可变。4) 生产陷阱?——只报第一个错让用户反复提交;聚合对象里塞函数/对象导致不可序列化;错误码与文档脱节;聚合层吞掉系统级异常(OOM/取消)。
