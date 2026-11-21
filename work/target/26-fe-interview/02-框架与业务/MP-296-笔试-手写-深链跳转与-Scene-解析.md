---
title: [MP-296] 笔试：手写深链 Scene 参数解析器（二维码/分享/搜索多来源）
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 笔试题, 19]
type: 笔试题
---

## MP-296：笔试：手写 Scene 参数解析器
**题**：onLoad 收到 options：scene（二维码 getQuery 解码后的字符串）、query 参数、path。实现 parseEntry(options)：统一输出 { source: 'qr'|'share'|'search'|'direct', params }；scene 支持 a=1&b=2 与 JSON 两种格式；未知来源兜底；参数白名单过滤。

```javascript
function parseEntry(options = {}) {
  let params = {}, source = 'direct'
  if (options.scene) {
    source = 'qr'
    const raw = decodeURIComponent(options.scene)
    if (raw.includes('=')) {
      raw.split('&').forEach(kv => {
        const [k, v] = kv.split('=')
        params[k] = v
      })
    } else {
      try { params = JSON.parse(raw) } catch { params = {} }
    }
  } else if (options.inviterId) {
    source = 'share'
    params = options
  } else if (options.q) {
    source = 'search' // 搜索直达也走 scene 编码
    params = parseScene(decodeURIComponent(options.q))
  }
  const WHITELIST = ['id', 'inviterId', 'activityId', 'tab']
  return { source, params: Object.fromEntries(Object.entries(params).filter(([k]) => WHITELIST.includes(k))) }
}
```
**评分点**：
- scene 的 decodeURIComponent + 两种格式（kv/JSON）兼容。
- 来源判定优先级清晰。
- 白名单过滤（防参数注入）。
- 直接打开/分享/二维码三来源全覆盖。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-0182258a-26e6-4c17-9a46-c418a7678326-cwd'; fi
exit "$__zcode_status"
