---
title: [MFW-608] Turborepo Remote Cache 与本地缓存协同
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-608：Turborepo Remote Cache 协同

**答**:
- 缓存层级协同：本地缓存（.turbo——个人机器）→ remote cache（团队共享——CI 之间/同事之间复用 RBL-637）；命中顺序：本地 → remote → 全量执行；「remote 命中」= 下载产物（网络延迟 < 本地构建时长才值得——大产物的下载成本）。
- remote cache 的签名校验（RBL-638）：产物 hash 验证——防篡改；「签名的密钥管理」（CI 主分支可写、PR 只读——权限分级）。
- 缓存失效的正确性：任务输入指纹（源码 hash + 依赖闭包 + 环境变量 RBL-582）——「指纹完备性」是缓存正确性的根基（RBL-587）；「remote 缓存的污染防护」：签名 + 键完备性。
- 追问钩子：为什么「remote cache 的产物下载」值得即使本地有构建能力？——CI 场景：PR 的 build 与 main 已构建的不同部分（shared 包已构建——remote 直接复用）→ CI 时长从 20min → 2min；「构建的计算成本 vs 下载成本」：产物 50MB 下载 10s vs 构建 15min——缓存命中是纯赚；「缓存的经济学」：复用次数 × 节省时间 − 下载时间（RBL-614 公共依赖下沉的缓存版）。

```bash
# turborepo remote cache
# .turbo/config.json
{ "remoteCache": { "signature": true, "teamId": "org" } }
# CI 配置：TURBO_TOKEN/TURBO_TEAM
# 命中顺序
turbo build
# 1. 本地 .turbo/cache 指纹命中 → 直接用
# 2. remote cache 指纹命中 → 下载 + 签名校验 + 解压
# 3. 全部 miss → 执行 + 上传产物到 remote
# 任务指纹构成
# { "inputs": ["src/**", "package.json"], "env": ["NEXT_PUBLIC_*"], "outputs": ["dist/**"] }
# 环境变量进指纹（NEXT_PUBLIC_* 影响 bundle——漏了 = 错缓存 RBL-587）
```
