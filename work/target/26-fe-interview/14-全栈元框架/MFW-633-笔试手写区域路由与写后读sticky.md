---
title: [MFW-633] 笔试：手写区域路由与写后读 sticky
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-633：笔试：手写区域路由

**答**：实现 `routeRequest(req, cfg)`。cfg: `{ primaryRegion, regions, stickySec, now }`。req: `{ cookies: Record, cfRegion }`. 规则：1) sticky cookie（recent-write，未过期）→ 路由 primaryRegion；2) 否则：cfRegion ∈ regions → cfRegion；不在 → primaryRegion（fallback）；3) 返回 `{ region, isSticky }`。`afterWrite(res, cfg)`：设置 sticky cookie（maxAge = stickySec）。边界：无 cfRegion（fallback primary）；sticky 过期（按 cfRegion 正常路由）；regions 不含 primary（primary 恒可用——写入目标）。

```javascript
function routeRequest(req, cfg) {
  const { primaryRegion, regions = [], stickySec = 10, now = Date.now } = cfg;
  const stickyCookie = req.cookies?.['recent-write'];
  if (stickyCookie) {
    const [ts] = stickyCookie.split('|');
    if (now() - +ts < stickySec * 1000)
      return { region: primaryRegion, isSticky: true };
  }
  const region = regions.includes(req.cfRegion) ? req.cfRegion : primaryRegion;
  return { region, isSticky: false };
}
function afterWrite(res, { stickySec = 10, primaryRegion, now = Date.now }) {
  res.cookies = res.cookies ?? {};
  res.cookies['recent-write'] = `${now()}|${primaryRegion}`;
  res.cookies.maxAge = stickySec;
  return res;
}

// 自测
const nowState = { t: 1000000 };
const cfg = { primaryRegion: 'us-east', regions: ['us-east', 'eu-west', 'ap-south'],
  stickySec: 10, now: () => nowState.t };

// 正常路由：cfRegion 命中
console.log(routeRequest({ cookies: {}, cfRegion: 'eu-west' }, cfg).region === 'eu-west');
console.log(routeRequest({ cookies: {}, cfRegion: 'eu-west' }, cfg).isSticky === false);
// 未知区域 fallback
console.log(routeRequest({ cookies: {}, cfRegion: 'mars' }, cfg).region === 'us-east');
// 无 cfRegion
console.log(routeRequest({ cookies: {} }, cfg).region === 'us-east');

// sticky：刚写过
nowState.t = 1000000;
const w = afterWrite({ cookies: {} }, cfg);
const stickyReq = { cookies: w.cookies, cfRegion: 'eu-west' };
console.log(routeRequest(stickyReq, cfg).region === 'us-east');   // 写后读主区
console.log(routeRequest(stickyReq, cfg).isSticky === true);

// sticky 过期
nowState.t = 1000000 + 11000;                            // 11s 后过期
console.log(routeRequest(stickyReq, cfg).region === 'eu-west');
console.log(routeRequest(stickyReq, cfg).isSticky === false);

// regions 不含 primary 也能写（primary 恒可用）
const cfg2 = { ...cfg, regions: ['eu-west'] };
console.log(routeRequest({ cookies: {} }, cfg2).region === 'us-east');
```

**评分点**：
- sticky 语义正确（写后 N 秒路由主区——写后读一致性窗口）；过期回归正常路由
- fallback（未知区域→主区）；primary 恒可写（regions 列表不含主区也 OK）
- 边界（无 cfRegion/过期/无 cookie）；cookie 携带时间戳（绝对过期而非相对）
- 能说清「写后读一致性是多区域架构的隐形杀手——sticky 窗口用跨区 RTT 换一致性保证」属于加分
