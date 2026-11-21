---
title: [Q7088] pickle 反序列化加载模型的任意代码执行事故复盘
date: 2026-11-20
categories: [Python数据分析与工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7088 · pickle 反序列化加载模型的任意代码执行事故复盘

难度：P6/P7 ｜ 标签：安全 / 序列化 / 事故复盘

**问**：ML 平台允许研究员上传 `.pkl` 模型文件供线上加载。一次事故中，上传的 pickle 文件在推理服务里执行了任意代码。为什么会这样？怎么复盘和防？

**答**：
- **结论**：pickle 是基于字节码的图灵完备序列化协议——反序列化时执行 `REDUCE` 操作码，会调用任意可调用对象（`__reduce__` 返回 `os.system` 即可 RCE）。"不反序列化不可信来源的 pickle"是硬规则，ML 场景恰恰天天反序列化（sklearn/老版 torch 的 `.pkl`/`.pt`）。事故链：上传口 → 对象存储 → 推理服务 `pickle.load` → RCE。基础防线不是"扫描恶意字节码"（绕过极容易），而是换协议或隔离执行。
- **取舍**：三种方案的取舍：① 换安全协议：模型权重用 safetensors（纯张量无代码）/ONNX（计算图限定算子集），sklearn 用 joblib+safetensors 化的中间层——治本但要求模型可转换；② 沙箱执行：独立进程/容器 + 无网 + 只读文件系统 + 资源限额，兼容性好但运维成本高；③ 限制反序列化目标（`RestrictedUnpickler` 只放行白名单类）——只防已知 gadget，绕过容易，只能算辅助。
- **实战**：复盘四步：① 全量审计对象存储里的 pickle 来源与上传者；② 换 safetensors/ONNX 作为平台标准格式，pickle 只允许在训练环境使用；③ 推理服务改隔离执行池（每次加载新容器，进程级隔离防跨请求污染）；④ 上传口加内容嗅探（magic bytes 检查）+ 平台签名校验（模型文件经 CI 签名，线上验签）。

```python
# RestrictedUnpickler 白名单反序列化 + 平台验签门禁（纯标准库）
# 基线：Python 3.9+

import hashlib
import hmac
import io
import pickle
from pickle import Unpickler


class RestrictedUnpickler(Unpickler):
    """只放行基础类型与白名单全局，阻断 os.system 等 gadget"""
    ALLOWED_GLOBALS = {"collections": {"OrderedDict"}}

    def find_class(self, module: str, name: str):
        if module in self.ALLOWED_GLOBALS and name in self.ALLOWED_GLOBALS[module]:
            return super().find_class(module, name)
        raise pickle.UnpicklingError(f"forbidden global {module}.{name}")


def safe_loads(data: bytes):
    return RestrictedUnpickler(io.BytesIO(data)).load()


def verify_signature(data: bytes, sig: bytes, key: bytes) -> bool:
    return hmac.compare_digest(hmac.new(key, data, hashlib.sha256).digest(), sig)


def main() -> None:
    ok = pickle.dumps({"a": 1})  # 基础类型可过
    print("基础类型:", safe_loads(ok))
    # 演示白名单放行：构造一个引用白名单全局的对象
    import collections
    payload = pickle.dumps(collections.OrderedDict(x=1))
    print("白名单全局:", safe_loads(payload))

    data = b"model-bytes"
    key = b"platform-secret"
    sig = hmac.new(key, data, hashlib.sha256).digest()
    print("验签:", verify_signature(data, sig, key))
    assert verify_signature(data, sig, key)
    assert not verify_signature(data, sig + b"x", key)


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"扫描 pickle 里的危险字节码"不可靠？
→ 一句话提示：REDUCE 可以动态 import 与属性链拼接，混淆方式无穷多，黑名单/模式匹配注定漏报——安全上"执行图灵完备输入"本身错误，与扫描能力无关。

**追问 2**：safetensors 为什么能免 RCE？
→ 一句话提示：它只存张量数据 + JSON 头，没有可执行语义，解析器是纯数据读取，攻击面天然消失——代价是不支持含自定义 Python 逻辑的对象（如 sklearn pipeline），要转换或拆分。

## 背诵要点
- pickle 的 REDUCE 操作码 = 任意代码执行，"不 load 不可信 pickle"是硬规则；ML 场景是高发区。
- 方案取舍：safetensors/ONNX 治本（限定语义）> 沙箱隔离（兼容但贵）> RestrictedUnpickler 只辅助。
- 平台级防线：CI 签名 + 线上验签 + 上传口 magic bytes 嗅探 + 推理隔离执行池。

## 复盘追问
- 为什么训练环境可以用 pickle 而线上不行？提示：信任边界不同，训练环境来源可控且失败影响小，线上加载不可控输入必须按敌意输入处理。
- 事故后如何发现"还有哪些服务在 load 用户可控文件"？提示：代码机检 grep pickle.load/torch.load/joblib.load 调用点 + 追踪文件来源是否出对象存储的用户目录。
