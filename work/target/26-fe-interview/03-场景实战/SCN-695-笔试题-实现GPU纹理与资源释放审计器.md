---
title: [SCN-695] 笔试题——实现 3D 资源释放审计器（场景卸载全量 dispose）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-695：手写 3D 资源释放审计器

**需求与边界**：
- 需求：切换孪生场景时全量释放旧场景资源（geometry/material/texture/renderer target）；审计输出「未释放清单」；支持白名单（常驻资源）。
- 边界：① 递归遍历对象树；② 共享材质只释放一次（引用计数）；③ WeakRef 检测泄漏对象（GC 后仍可达即泄漏）。

**答**：
```javascript
function disposeScene(root, { keep = new Set() } = {}) {
  const seen = new Set();                              // 共享资源去重
  const released = [], leaked = [];
  function disposeObj(obj) {
    obj.traverse(child => {
      if (child.geometry && !seen.has(child.geometry)) {
        seen.add(child.geometry); child.geometry.dispose(); released.push('geometry');
      }
      const mats = Array.isArray(child.material) ? child.material : [child.material];
      for (const m of mats ?? []) {
        if (!m || seen.has(m) || keep.has(m.uuid)) continue;
        seen.add(m);
        for (const key of Object.keys(m)) {            // 材质上的纹理
          const tex = m[key];
          if (tex?.isTexture && !seen.has(tex) && !keep.has(tex.uuid)) {
            seen.add(tex); tex.dispose(); released.push('texture');
          }
        }
        m.dispose(); released.push('material');
      }
    });
  }
  disposeObj(root);
  // 泄漏检测：WeakRef 观察已释放对象，2 次 GC 后仍非 undefined 说明外部仍引用
  const refs = released.map(uuid => new WeakRef(getObject(uuid)));
  setTimeout(() => {
    globalGC?.();                                      // 测试环境手动 GC
    refs.forEach((r, i) => r.deref() !== undefined && leaked.push(i));
    report({ released: released.length, leaked });
  }, 10_000);
  renderer.renderLists.dispose();                      // 渲染缓存清理
  return { releasedCount: released.length, leaked };
}
```

**评分点**:
- 递归遍历 + 三类资源（geometry/material/texture）全 dispose。
- seen 去重（共享材质/纹理只释放一次）+ 白名单。
- renderLists 等渲染器级缓存清理。
- WeakRef 泄漏审计（释放后被引用即泄漏）。
