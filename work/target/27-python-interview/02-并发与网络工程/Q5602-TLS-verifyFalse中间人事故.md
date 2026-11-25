---
title: [Q5602] TLS verify=False 中间人事故复盘
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5602 · TLS verify=False 中间人事故复盘

> 难度:★★★★☆ | 标签:事故复盘, TLS, 安全

**问**:为了"先跑通"把证书校验关了，代码上线半年没人发现，风险评估与治理怎么做？

**答**:结论：`verify=False`（requests）或 `CERT_NONE`（ssl）意味着不再验证服务端身份与证书链，TLS 退化为纯加密通道——任何能介入网络路径的人（内网 ARP、代理、恶意 Wi-Fi）都可以冒充对端拿数据、改响应。风险面：出向凭据泄露、响应被注入、合规审计项直接红牌。治理动作分三层：① 代码层——CI 里静态扫描 `verify=False`/`CERT_NONE`/`_create_unverified_context`，发现即阻断；② 运行层——`PYTHONHTTPSVERIFY` 这类旁路手段不复存在（requests 只认参数），用自签内网 CA 时走 `REQUESTS_CA_BUNDLE`/`ssl.create_default_context(cafile=...)` 加载私有信任锚，而不是关校验；③ 事故复盘层——按"哪些主机被关过校验、期间是否有异常流量"回溯。取舍：内网自签证书的运维成本确实高，正确姿势是统一注入 CA 而非逐点开关。

```python
import ssl, socket, sys

# 正解：显式加载私有 CA，校验不缺席（文件缺失要有显式失败路径）
try:
    ctx = ssl.create_default_context(cafile="private-ca.pem")
except (FileNotFoundError, ssl.SSLError) as e:
    print("私有 CA 缺失应 fail-fast 而不是关校验:", type(e).__name__)
ctx = ssl.create_default_context()
print("默认协议:", ctx.protocol, "| 校验:", ctx.verify_mode == ssl.CERT_REQUIRED)

# 事故现场：关校验的正确"写法"长这样——CI 必须扫掉这三类
BAD_PATTERNS = ("CERT_NONE", "check_hostname = False", "CERT_OPTIONAL")
def audit(source: str) -> list[str]:
    return [p for p in BAD_PATTERNS if p in source]
src = 'ctx2 = ssl._create_unverified_context(); ctx2.check_hostname = False; ctx2.verify_mode = ssl.CERT_NONE'
print("扫描命中:", audit(src))

# 缺库/无证书文件降级：至少记录并收敛到显式白名单主机
try:
    with socket.create_connection(("pypi.org", 443), timeout=5) as raw:
        with ctx.wrap_socket(raw, server_hostname="pypi.org") as s:
            print("TLS 握手:", s.version())
except Exception as e:
    print("演示环境无外网，降级打印:", type(e).__name__)
```

**追问一层**:`check_hostname=False` 但 `verify_mode=CERT_REQUIRED` 会留下什么风险？
**追二层**:TLS 1.3 下 MITM 与 0-RTT 重放的区别？为什么关校验后重放类攻击更隐蔽（引 Q5511）？

**背诵要点**
- verify=False=只加密不认证，中间人可完整冒充对端。
- 自签内网 CA 的正解是注入信任锚（cafile/REQUESTS_CA_BUNDLE），不是关校验。
- CI 静态扫描三类写法：CERT_NONE、_create_unverified_context、check_hostname=False。

**复盘追问**
- 如何在运行期检测"某条连接实际没做校验"？提示：包装 ssl 模块断点/审计钩子（Q5022）。
- 第三方 SDK 内部写死 verify=False 怎么治理？提示：fork 补丁/代理层 TLS 终结。
