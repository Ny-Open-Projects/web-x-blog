---
title: [AV-023] CDN 在流媒体里扮演什么角色？边缘节点、回源、预热是什么？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-023：CDN 在流媒体里扮演什么角色？边缘节点、回源、预热是什么？
**答**：
- 角色：把海量观众请求就近收敛到边缘节点，源站只服务少量边缘（回源），实现扩展性与成本最优。
- 关键概念：边缘节点（就近服务）、回源（边缘未命中向源站/二级节点拉取）、预热（开播前把分片推到边缘避免首波回源风暴）、鉴权（URL 签名防盗链）。
- 直播特殊性：内容实时生成，无法传统预热，靠"分片拉取透传 + 边缘缓存窗口"实现；拉流爆发（开播瞬间）要靠调度与预热 playlist。
- 流媒体 HTTPS 首次回源耗时是首帧慢的常见根因；录制回源上传也是 CDN 侧能力。
- 前端关联：多 CDN 调度（测速选路）、HTTPDNS 防劫持、CDN 5xx 时的备用域名切换。

```javascript
// 多 CDN 测速选路（简化）：并发探测各 CDN 的探测 URL，选最快
async function pickBestCDN(cdns) {
  const tasks = cdns.map(async (cdn) => {
    const start = performance.now();
    const res = await fetch(`${cdn.probeUrl}`, { cache: 'no-store' });
    if (!res.ok) throw new Error(cdn.name);
    return { name: cdn.name, rtt: performance.now() - start };
  });
  const results = await Promise.allSettled(tasks);
  const ok = results.filter((r) => r.status === 'fulfilled')
    .map((r) => r.value).sort((a, b) => a.rtt - b.rtt);
  return ok[0]?.name ?? 'default-cdn';
}
pickBestCDN([
  { name: 'cdnA', probeUrl: 'https://a.cdn.com/probe.bin' },
  { name: 'cdnB', probeUrl: 'https://b.cdn.com/probe.bin' },
]).then(console.log);

// 防盗链签名 URL 生成（前端只做展示，签名应在服务端）
const signedUrl = (base, stream, expires) =>
  `${base}/${stream}.m3u8?auth_key=${expires}-0-0-${md5Token}`;
```

---

## 四、WebRTC 核心（AV-024 ~ AV-033）
