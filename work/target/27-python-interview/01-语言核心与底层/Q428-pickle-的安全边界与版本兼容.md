---
title: [Q428] pickle 的安全边界与版本兼容
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q428 · pickle 的安全边界与版本兼容

> 难度:★★★★☆ | 标签:pickle, 安全, 序列化

**问**:为什么 pickle 文档说"永远不要 unpickle 不受信来源的数据"?攻击面在哪?`pickle.loads` 能 restricted 吗?跨版本/跨平台的兼容坑有哪些,什么时候该换 JSON/MessagePack?

**答**:pickle 流是**虚拟机指令序列**,还原时执行 `REDUCE`/`BUILD` 等操作码,可调用任意 callable——经典攻击是 `cos.system('...')` 的 REDUCE 链,无需任何 bug,unpickle 即代码执行。`pickle.Unpickler.find_class` 是唯一合法钩子:重写它做模块白名单可以在受控场景收窄攻击面(不是安全边界,是缓解);Python 3 曾有 `RestrictedUnpickler` 的说法即此模式。兼容性坑:protocol 版本(0-5,3.8 起 `DEFAULT_PROTOCOL` 为 4、`HIGHEST_PROTOCOL` 为 5,升级写出协议时要确认读取方能解)、类 `__reduce__` 依赖类路径(**重构模块路径会破坏旧数据**)、大对象分帧、以及 pickle 不保证跨语言。因此:内部持久化/缓存且可信环境才用 pickle;跨服务/跨版本一律 JSON(数据)/MessagePack/arrow;对象图含闭包/lambdas/打开的句柄时 pickle 本就不适用。

```python
# file: code/01_语言核心与底层/q428_pickle_safety.py
import io
import pickle
import pickletools

print("default protocol:", pickle.DEFAULT_PROTOCOL, "| highest:", pickle.HIGHEST_PROTOCOL)

# 恶意负载演示:仅构造,绝不 loads
payload = pickle.dumps({"ok": 1})
pickletools.dis(io.BytesIO(payload))   # 可见 REDUCE/BUILD 等操作码即虚拟机指令

# 白名单缓解:RestrictedUnpickler
import builtins

class SafeUnpickler(pickle.Unpickler):
    ALLOWED = {("builtins", "dict"), ("builtins", "set")}
    def find_class(self, module, name):
        if (module, name) not in self.ALLOWED:
            raise pickle.UnpicklingError(f"forbidden {module}.{name}")
        return getattr(builtins, name)

try:
    SafeUnpickler(io.BytesIO(payload)).load()
    print("safe load ok")
except pickle.UnpicklingError as e:
    print("blocked:", e)

# 版本兼容坑:类路径重构即破坏旧数据
class Old:
    pass
blob = pickle.dumps(Old())
print("roundtrip:", type(pickle.loads(blob)).__name__)
# 若把 Old 改名/挪模块,旧 blob 将 UnpicklingError: 路径被编进流里
```

**追问**:1) `protocol=5` 解决什么?——PEP 574 out-of-band data,大 buffer(如 numpy)可配合 `buffer_callback` 零拷贝传输。2) json 与 pickle 在"非 ASCII 与 int64 精度"上的差异?——json 默认 ensure_ascii 转义与 float 双精度(int 超 2^53 精度丢失需字符串化),pickle 原生保留 Python 类型与精度,但代价是绑死 Python。
