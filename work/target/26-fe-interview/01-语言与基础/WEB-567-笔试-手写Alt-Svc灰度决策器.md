---
title: [WEB-567] 笔试：手写 Alt-Svc 灰度决策器
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 网络]
type: 笔试题
---

## WEB-567：笔试：手写 Alt-Svc 灰度决策器

**答**：实现网关侧的 Alt-Svc 下发决策函数 `decideAltSvc(req, config)`。要求：① 按用户 ID 哈希落入灰度百分比（`rollout` 字段）；② 命中地区黑名单（`blockedRegions`）不下发；③ UA 在兼容性黑名单（如老 WebView）不下发；④ 返回 `{ enabled, ma }`，ma 值在紧急回滚模式（`rollback: true`）下返回 0 并要求覆盖旧值。给出实现与关键测试用例。

```javascript
function hashUserId(uid) {
  let h = 0;
  for (const c of String(uid)) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  return h % 1000 / 1000; // 0~1
}

function decideAltSvc(req, config) {
  if (config.rollback) return { enabled: true, ma: 0, note: '紧急回滚：空值覆盖' };
  if (config.blockedRegions.includes(req.region)) return { enabled: false, ma: 0 };
  if (config.uaBlacklist.some(re => re.test(req.ua))) return { enabled: false, ma: 0 };
  if (hashUserId(req.uid) >= config.rollout) return { enabled: false, ma: 0 };
  return { enabled: true, ma: config.ma ?? 86400 };
}

// 用例: uid 固定 → 结果可复现（同 uid 同配置永远同结果）
console.log(decideAltSvc({ uid: 'u1', region: 'cn-north', ua: 'Chrome/120' },
  { rollout: 0.5, blockedRegions: [], uaBlacklist: [] })); // { enabled: true|false, ma: 86400 }
console.log(decideAltSvc({ uid: 'u1', region: 'x', ua: 'Chrome/120' },
  { rollout: 1, blockedRegions: ['x'], uaBlacklist: [] })); // { enabled: false }
console.log(decideAltSvc({ uid: 'u1', region: 'x', ua: 'Chrome/120' },
  { rollback: true })); // { enabled: true, ma: 0 }
```

**评分点**：
- 哈希分桶对同一 uid 稳定（请求级随机是错误答案）
- rollback 分支优先级最高且返回空 Alt-Svc 覆盖，理解「ma=0 即停止引导」
- 地区/UA 黑名单短路在灰度判断之前，边界顺序正确
- 提及 ma 值是客户端缓存期限，控制回滚生效速度
