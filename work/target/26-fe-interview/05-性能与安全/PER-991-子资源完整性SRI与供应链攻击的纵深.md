---
title: [PER-991] 子资源完整性（SRI）与供应链攻击的纵深组合
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-991：子资源完整性（SRI）与供应链攻击的纵深组合

**答**：
- SRI：CDN 返回的脚本带 integrity hash 校验，CDN 被篡改（投毒）时浏览器拒载——防 CDN 层供应链攻击。
- 局限：只防"CDN 静态文件被改"，不防 npm 包本身被投毒（代码进了你的 bundle）；需 lockfile + 依赖审计 + 私有镜像。
- 组合拳：integrity + crossorigin="anonymous"（否则校验失败静默降级为不加载错误）；构建期给产物自动计算 hash。
- 监控：onerror 上报 SRI 失败事件，区分"CDN 污染（安全事件）"与"版本不一致（发布事故）"。

```javascript
<script src="https://cdn.example.com/lib.min.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
  crossorigin="anonymous"
  onerror="reportSRI('lib.min.js')"></script>
<script>
function reportSRI(file) {
  navigator.sendBeacon('/sec', JSON.stringify({
    type: 'sri-fail', file, ts: Date.now(),
    ua: navigator.userAgent, ver: __BUILD_ID__,
  }));   // 同版本集中出现 -> 疑似 CDN 污染，立即切源
}
</script>
```
