---
title: [Q2079] 异常对象的属性携带:args 与自定义属性
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2079 · 异常对象的属性携带:args 与自定义属性

> 难度:★★★☆☆ | 标签:异常, 结构化数据, API 设计

**问**:想抛一个「带上下文数据」的异常,数据该放 args 里还是自定义属性上?

**答**:分工明确:args 是异常的「人读」部分,决定 str(e)、repr(e) 与默认 pickle 行为,super().__init__(message) 保持 str(e) 干净;自定义属性是「程序读」的结构化字段,让 handler 能按 status、request_id 做路由与上报,而不是去解析字符串。惯例是 __init__ 里先 super().__init__(message) 再挂属性,这样日志能直接打印消息、监控能直接读字段。异常实例也是普通对象,抛出前仍可事后附加属性,但那属于调试手段而非接口契约(参考 Q1277 的消息设计与 Q1817 的错误码体系)。

```python
# file: code/01_语言核心与底层/q2079_exception_attrs.py
"""异常对象的属性携带:args、自定义属性与结构化取数。"""


class ApiError(Exception):
    def __init__(self, message, status=0, *, request_id=""):
        super().__init__(message)       # args 只放消息,str(e) 干净
        self.status = status
        self.request_id = request_id


def call_api(status, request_id):
    if status >= 500:
        raise ApiError("服务端错误", status=status, request_id=request_id)
    if status >= 400:
        raise ApiError("请求被拒绝", status=status, request_id=request_id)
    return "ok"


if __name__ == "__main__":
    try:
        call_api(503, "req-42")
    except ApiError as e:
        print("args 元组:", e.args)
        print("str(e):", str(e))
        print("结构化字段:", e.status, e.request_id)

    try:
        call_api(403, "req-7")
    except ApiError as e:
        print("按状态码路由:", "稍后重试" if e.status >= 500 else "检查权限")

    e = ApiError("仅构造")
    e.hint = "查看网关日志"             # 异常实例也是普通对象,可事后附加
    print("事后附加属性:", e.hint)
```

**追问**:1) 为什么消息放 args、数据放属性?——args 决定 str(e) 与 pickle 的默认行为,属性才是可编程的结构化接口;自定义属性会被 pickle 带走吗?——默认不会,异常默认只序列化 args,要带上属性须自定义 __reduce__。2) 自定义异常的设计清单?——__init__ 接收 (message, **业务字段),属性只读化;__str__ 模板化输出;错误码属性 .code 供出口映射(Q1817);继承链保持「可按父类捕获」。3) args 的角色?——args 元组是异常的「事实标准载荷」;str(e) 默认 str(args[0]);跨进程传输(日志/队列)序列化主要靠它。4) 生产陷阱?——把结构化数据全塞消息字符串(下游只能正则解析);属性被外部改写;异常对象进队列因属性丢失败。
