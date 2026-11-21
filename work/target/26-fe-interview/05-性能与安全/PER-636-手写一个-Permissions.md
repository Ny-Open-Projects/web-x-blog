---
title: [PER-636] 手写一个 Permissions-Policy 与 iframe allow 的合规校验器：扫描页面所有 iframe 并输出违规清单
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-636：手写一个 Permissions-Policy 与 iframe allow 的合规校验器：扫描页面所有 iframe 并输出违规清单

**答**：
- 校验逻辑：遍历 iframe -> 检查 sandbox 是否存在、是否包含危险组合（allow-scripts+allow-same-origin）、allow 属性是否包含未在业务理由清单登记的能力、src 域是否在 frame-src 允许清单。
- 要点：危险组合判定要精确（token 化解析 sandbox 值）；业务理由清单（能力-域名-理由）作为配置输入；输出按违规级别排序，阻断级（危险组合）置顶。
- 边界：无 src 的 iframe（占位/懒加载）跳过；同域 iframe（自家微前端）允许 same-origin 但要有标记。
- 评分点：token 化解析与理由清单比对。

```javascript

const REASONS = {   // 能力-域-理由 登记（没有登记的 allow 一律违规）
  'https://partner.com': [{ cap: 'fullscreen', why: '视频组件全屏按钮' }],
  'https://maps.example.com': [{ cap: 'geolocation', why: '门店地图定位' }],
};
function auditIframes(doc = document) {
  const issues = [];
  doc.querySelectorAll('iframe[src]').forEach(f => {
    const src = f.getAttribute('src');
    const origin = new URL(src, location.href).origin;
    const sb = (f.getAttribute('sandbox') ?? '').split(/\s+/).filter(Boolean);
    if (!sb.length) issues.push({ src, level: 'high', why: '无 sandbox，第三方全权' });
    else if (sb.includes('allow-scripts') && sb.includes('allow-same-origin') &&
             !src.startsWith(location.origin))
      issues.push({ src, level: 'high', why: 'scripts+same-origin 组合等于无沙箱' });
    (f.getAttribute('allow') ?? '').split(';').filter(Boolean).forEach(cap => {
      const c = cap.trim().split('=')[0].trim();
      const ok = (REASONS[origin] ?? []).some(r => r.cap === c);
      if (!ok) issues.push({ src, level: 'medium', why: `能力 ${c} 未在理由清单登记` });
    });
  });
  return issues.sort((a, b) => (a.level === 'high' ? 0 : 1) - (b.level === 'high' ? 0 : 1));
}
console.table(auditIframes());
```
