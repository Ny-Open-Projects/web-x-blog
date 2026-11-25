---
title: [Q5115] hashlib 摘要算法吞吐成本账
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5115 · hashlib 摘要算法吞吐成本账

> 难度:★★★★☆ | 标签:成本工程, hashlib, 算法选型

**问**:去重服务要给每条上传内容算指纹，团队纠结 sha256、blake2b、还是 md5。摘要算法的吞吐差异有多大？选型除了速度还要看什么？（合规侧另见 Q5097 的 usedforsecurity/FIPS 演进）

**答**:结论：同一数据量下各算法吞吐**同量级（数百 MB/s）但差异明显**：blake2b/blake2s 常领先，md5 居中，sha256 因轮数多通常最慢（实测可为 blake2b 的 60% 左右）——具体排序随 OpenSSL 版本浮动，选型前应在目标机器上实测（本卡代码即是实测框架）。成本差累积：百万级/天 的服务一年省的 CPU 相当可观。但选型是四维权衡：a) **吞吐**；b) **抗碰撞强度**：md5/sha1 已被实际碰撞攻击攻破，只可用于非对抗性去重（缓存键、分片校验），对抗场景必须 sha256 或 blake2（blake2 未被攻破且比 sha256 快）；c) **摘要长度**：`blake2b(digest_size=16)` 可自定义长度，直接省一半存储与传输；d) **合规**：FIPS 环境只允许 sha2/sha3 家族（见 Q5097）。实战姿势：大文件摘要别一次性 `hashlib.file_digest`（3.11+ 有 file_digest，内部按块读）；增量场景用 `h.update()` 分块喂入，块长 1MB 级时 Python 侧调用开销可忽略。

```python
import hashlib, os, timeit

data = os.urandom(64 * 1024 * 1024)          # 64MB 样本
algos = ["md5", "sha1", "sha256", "blake2b", "blake2s"]

print(f"{'算法':<8}{'耗时(s)':<10}{'吞吐(MB/s)':<12}")
base = None
for name in algos:
    h = getattr(hashlib, name)()
    t = timeit.timeit(lambda: (lambda hh: (hh.update(data), hh.hexdigest()))(getattr(hashlib, name)()), number=1)
    thr = len(data) / 1e6 / t
    base = base or thr
    print(f"{name:<8}{t:<10.3f}{thr:<12.0f}相对首行={thr/base:.2f}")

# blake2b 自定义摘要长度：碰撞强度与存储成本可调
h16 = hashlib.blake2b(data[:1024], digest_size=16)
h32 = hashlib.blake2b(data[:1024], digest_size=32)
print("digest_size=16:", len(h16.hexdigest()), "字节;  =32:", len(h32.hexdigest()), "字节")

# 大文件：hashlib.file_digest（3.11+）分块读取，峰值内存 O(块)
with open("/dev/null", "rb") as f:
    import sys
    if sys.version_info >= (3, 11):
        d = hashlib.file_digest(f, "sha256")
        print("file_digest:", d.hexdigest()[:16], "...")
    else:
        print("3.10- 降级: 手写分块 update")

# keyed 摘要：blake2b 内置 key 参数，可替代 HMAC 的部分场景
k = hashlib.blake2b(b"payload", key=b"sixteen_byte_key00", digest_size=16)
print("keyed:", k.hexdigest()[:16])
```

**追问一层**:为什么 blake2b 比 sha256 快——是算法轮数、内存访问模式还是 OpenSSL 实现差异？多核场景 hashlib 会释放 GIL 吗（引 Q5593）？
**追二层**:"非对抗性去重用 md5 也没事"这句话什么时候会翻车？提示：用户可上传内容时，构造碰撞制造不同内容同指纹的替换攻击。

**背诵要点**
- 吞吐同量级但有差：blake2b 常领先，sha256 常为其 ~60%，排序随 OpenSSL 版本浮动，先实测再选型。
- md5/sha1 已被攻破，只用于非对抗场景；对抗与合规场景 sha256/blake2。
- blake2b 支持 digest_size 与 key 参数，长度可省存储；大文件用 3.11+ `hashlib.file_digest`。

**复盘追问**
- 存量系统里 10 亿条 md5 指纹要换 sha256，迁移怎么做才不双算双存？提示：新指纹字段双写、读侧兼容旧值、灰度切换（引 Q6032 协议升级思路）。
- 指纹服务 CPU 打满怎么先定位是算法还是调用频次？提示：Q6034 单请求成本画像 + py-spy。
