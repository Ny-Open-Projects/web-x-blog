---
title: [Q516] JSON 编码定制:default 与排序
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q516 · JSON 编码定制:default 与排序

> 难度:★★☆☆ | 标签:JSON, 序列化

**问**:json.dumps 遇到 datetime/Decimal/Enum 抛 TypeError,正确的扩展点是什么?

**答**:两条路:json.dumps 的 default 参数(或 JSONEncoder 子类的 default 钩子)——它只被「无法序列化的对象」调用,返回可序列化替身;反之解析侧用 object_hook 处理嵌套 dict。decimal 千万别转 float(精度丢失),转 str 并在文档里约定;datetime 用 isoformat;Enum 取 value 或 name。工程要点:统一一个项目级 encoder 类而不是散落的 lambda;sort_keys 让输出稳定(利于 diff 与缓存键);ensure_ascii=False 输出真 UTF-8 并在响应头声明编码。

```python
# file: code/01_语言核心与底层/q516_json_encoder.py
import json
from datetime import datetime
from decimal import Decimal
from enum import Enum

class Status(Enum):
    OK = "ok"
    FAIL = "fail"

class AppEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, Decimal):
            return str(o)                     # 不转 float:保精度
        if isinstance(o, Enum):
            return o.value
        return super().default(o)

if __name__ == "__main__":
    payload = {
        "at": datetime(2026, 11, 1, 10, 0),
        "price": Decimal("19.99"),
        "status": Status.OK,
    }
    print(json.dumps(payload, cls=AppEncoder, sort_keys=True, ensure_ascii=False))
    try:
        json.dumps(payload)
    except TypeError as e:
        print("plain encoder:", e)
```

**追问**:1) default 与 object_hook 的方向?——default 管「对象 → JSON」的兜底出口,object_hook 管「JSON → 对象」的入口重构;往返都要保真时两侧都要定制并写round-trip测试。2) json.dumps 还有哪些静默坑?——非字符串 dict 键自动转字符串可能改变结构;float 用最短往返表示,跨语言丢精度;ensure_ascii 默认 True 把中文转义;datetime 不支持必须 default 兜底。3) 底层实现?——C 加速编码器 c_make_encoder 走快路径,传 indent/自定义 default 会退回 Python 慢路径;parse_float/parse_constant 是解析侧钩子,可处理 NaN/大数。4) 生产陷阱?——numpy 类型没接 default 直接 TypeError;id 大整数往返被当 float 失真;sort_keys 换取可复现但有性能成本;对不可信 JSON 挂 object_hook 谨慎(回调执行任意代码)。
