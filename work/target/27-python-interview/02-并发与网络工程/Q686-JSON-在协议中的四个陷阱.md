---
title: [Q686] JSON 在协议中的四个陷阱
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q686 · JSON 在协议中的四个陷阱

> 难度:★★☆ | 标签:JSON, 陷阱, 互操作

**问**:都说 JSON 简单,作为线上协议它有哪些真实的坑?

**答**:四个高频坑:1) 数字精度——超出 2^53 的整数(JS 消费方)与 float 精度(0.1+0.2)都会静默失真,金额/ID 类要传字符串;2) 类型宽泛——dict 的 int key 会被转成字符串,解析回来类型变了;3) 非法扩展——Python 默认允许 NaN/Infinity 序列化(不是合法 JSON,其他语言解析直接炸);4) 重复键与编码——重复 key 解析时后者覆盖(校验绕过源),ensure_ascii 默认转义使中文体积翻三倍。工程对策:协议文档明确"字段类型+取值域",入口处 schema 校验,序列化参数显式化(allow_nan=False, ensure_ascii=False)。

```python
# file: code/02_并发与网络工程/q686_json_pitfalls.py
import json


def show(label: str, fn) -> None:
    try:
        print(f"  [{label}] {fn()}")
    except Exception as e:
        print(f"  [{label}] 异常: {e!r}")


if __name__ == "__main__":
    print("1) 大整数精度 (JS 消费方视角):")
    big = 2 ** 53 + 1
    show("python roundtrip", lambda: json.loads(json.dumps(big)) == big)
    show("JS 相当于 Number",
         lambda: float(big) == float(2 ** 53), )  # 9007199254740992 分不清
    print("     → 订单号/雪花ID 跨语言请传字符串")

    print("2) float 精度:")
    show("0.1+0.2", lambda: json.loads(json.dumps(0.1 + 0.2)))
    show("金额建议分", lambda: json.dumps({"cents": 1050}))

    print("3) dict 非字符串 key:")
    show("int key roundtrip",
         lambda: json.loads(json.dumps({1: "a", 2: "b"})))
    show("tuple key", lambda: json.dumps({(1, 2): "x"}))

    print("4) NaN/Infinity 非 JSON 标准:")
    show("默认 dumps NaN", lambda: json.dumps(float("nan")))
    show("严格模式", lambda: json.dumps(float("nan"), allow_nan=False))

    print("5) 中文与 ensure_ascii:")
    zh = json.dumps({"city": "上海"})
    print(f"     默认: {zh} ({len(zh)} 字节)")
    print(f"     关闭转义: {json.dumps({'city': '上海'}, ensure_ascii=False)}")

    print("6) 重复键: 解析取最后一个 (校验绕过风险)")
    show("dup key", lambda: json.loads('{"role": "user", "role": "admin"}'))

    print("\n工程建议: 入口 schema 校验 + 显式序列化参数 + 金额/ID 字符串化")
```

**追问**:1) JSON Numbers 为什么注定不能承载全部数值?——ECMAScript 规定 Number 是 IEEE754 double,跨到 JS 生态的整数超过 2^53 必丢精度;Python 端虽然 int 无限,但线上格式只有一整套标准,取最弱者。2) 重复键为什么是校验绕过源?——解析「后者覆盖」,而校验层可能只检查第一个同名键:{"role":"user","role":"admin"} 检查看到 user、应用拿到 admin;防御:入口 schema 校验+拒绝重复键(对象对不允许)。3) NaN/Infinity 与 ensure_ascii 的对策?——json.dumps 默认 allow_nan=True 产出非法 JSON,其他语言解析直接炸,显式 allow_nan=False 提前报错;ensure_ascii=False 让中文不再 \u 转义(体积省 3 倍),前提传输层是 UTF-8。4) 生产陷阱?——float 存金额(0.1 累加误差,用 Decimal 或整数分);int key 的 dict 序列化后 key 变字符串,消费方类型断言崩;日期字段没约定格式(ISO 8601 字符串是惯例)。

---
