---
title: [OPS-148] SRI 怎么实操？有哪些坑？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-148：SRI 怎么实操？有哪些坑？
**答**：
- SRI：script/link 标签加 integrity 属性（内容哈希），资源被 CDN/中间层篡改时浏览器直接拒绝执行，配合 crossorigin 才生效。
- 哈希用 openssl 一条命令生成；构建期对 index.html 引用的第三方库自动计算注入。
- 硬坑清单：动态版本（latest）资源不能用 SRI（内容会变）；资源被服务端压缩/改写会失配；integrity 与 crossorigin 必须成对出现。
- 只覆盖 script/link，CSS 内 @import 与动态 fetch 不在保护范围，需另行治理。
- 版本锁死 + 自建反代（统一出网）是比 SRI 更基础的动作，SRI 是纵深防御的一层。

```bash
# SRI 实操：计算哈希 → 构建注入 → 验证
# 1. 计算某资源的 integrity 值（sha384 + base64）
SRI=$(curl -s https://cdn.example.com/lib/vue.3.4.21.min.js \
  | openssl dgst -sha384 -binary | openssl base64 -A)
echo "sha384-$SRI"

# 2. 注入后的标签形态（integrity 与 crossorigin 必须成对，否则 CORS 校验失败直接拒载）
#    <script src="https://cdn.example.com/lib/vue.3.4.21.min.js"
#            integrity="sha384-xxxx"
#            crossorigin="anonymous"></script>

# 3. 验证：篡改 CDN 文件内容，浏览器应报
#    "Failed to find a valid digest in the 'integrity' attribute"
curl -s https://www.example.com/ | grep -o 'integrity="[^"]*"' | head -3

# 4. 坑位：latest 等动态版本不能用 SRI；资源经服务端改写（压缩/注入）会失配；
#    SRI 只保护 script/link，CSS @import 与 fetch 需要单独治理
```
