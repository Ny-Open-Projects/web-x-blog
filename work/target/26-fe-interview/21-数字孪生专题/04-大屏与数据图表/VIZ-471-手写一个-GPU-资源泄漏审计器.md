---
title: [VIZ-471] 手写一个 GPU 资源泄漏审计器
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## VIZ-471：手写一个 GPU 资源泄漏审计器

**答**：
- 需求：implement ResourceAudit(gl)。包装 createTexture/createBuffer/createProgram 记录 { obj, tag, stack, at }；对应 delete 时移除；report() 输出 { active, olderThan1Min: [tag], totalCreated }；tag 必填（缺省 unnamed）。
- 边界：重复 delete 忽略；活跃数 > 5000 告警；stack 只保留前 3 行。
- 评分点：GL 方法包装；注册与删除；超时筛；告警

```javascript
function ResourceAudit(gl) {
  const registry = new Map();
  const wrap = (method, del, create) => {
    const origC = gl[create], origD = gl[del];
    gl[create] = (...a) => {
      const obj = origC.apply(gl, a);
      registry.set(obj, { tag: gl.__currentTag ?? 'unnamed',
        at: Date.now() });
      return obj;
    };
    gl[del] = (obj) => {
      registry.delete(obj);
      return origD.call(gl, obj);
    };
  };
  wrap(gl, 'deleteTexture', 'createTexture');
  wrap(gl, 'deleteBuffer', 'createBuffer');
  wrap(gl, 'deleteProgram', 'createProgram');
  return {
    report() {
      const now = Date.now();
      const old = [...registry.values()].filter(r => now - r.at > 60_000);
      return { active: registry.size, olderThan1Min: old.map(r => r.tag),
        totalCreated: registry.size,
        alert: registry.size > 5000 ? '资源数异常，疑似泄漏' : 'ok' };
    },
  };
}
```
