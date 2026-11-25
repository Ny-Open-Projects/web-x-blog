---
title: [MFW-322] SSR 与 CDN 双层失效的联动协议
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-322：双层失效联动

**答**:
- 两层各自失效不同步的事故：应用层 revalidateTag 成功但 CDN 仍持旧 s-maxage 副本（用户拿到旧页直到 SWR 过期）——失效必须双通道同发
- 统一协议：数据变更事件 → ①应用层 tag 失效（下次渲染取新）②边缘 purge（surrogate-key/Cache-Tag 精确清除该 URL 族）——一次事件两个执行器，顺序「先应用后边缘」（边缘回源时已能拿到新渲染）
- key 对齐：CDN surrogate-key 与应用 tag 用同一命名（domain:id）——两套命名必然漂移（对账脚本比对头与代码注册表）
- 验证：变更后多节点 curl 比对（含 CDN 命中头 x-cache: HIT/MISS）——「失效成功」以全网新值为准

```javascript
// 统一失效执行器
async function invalidateEverywhere(domain, id) {
  await appCache.revalidate(`${tag}:${id}')       // ① 应用层
  await cdn.purgeByKey(`${domain}:${id}')          // ② 边缘（tag 同名）
}
// 对账：采集响应 x-cache-keys ↔ 代码 tag 注册表 diff
```
