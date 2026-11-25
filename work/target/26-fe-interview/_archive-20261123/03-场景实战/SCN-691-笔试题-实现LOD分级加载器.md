---
title: [SCN-691] 笔试题——实现 LOD 分级加载器（视距切换 + 加载防抖）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-691：手写 LOD 分级加载器

**需求与边界**：
- 需求：对象按相机距离切三级 LOD（高模/低模/点）；切换有迟滞（防边界抖动：进入更高一级需距离 < 阈值×0.9）；低模未加载完成期间用占位。
- 边界：① 加载请求去重；② 卸载远级模型释放显存（dispose）；③ 每帧检查对象数量上限（视距内最多 N 个高模）。

**答**：
```javascript
function createLODManager(camera, { levels = [50, 200], maxHigh = 100 } = {}) {
  const items = new Map();                             // id -> { obj, high?, low?, level }
  const loading = new Set();
  function update() {
    let highCount = 0;
    for (const [id, it] of items) {
      const d = camera.position.distanceTo(it.obj.position);
      const want = d < levels[0] * 0.9 ? 0 : d < levels[0] ? it.level ?? 1   // 迟滞
                 : d < levels[1] ? 1 : 2;
      if (want === it.level) continue;
      it.level = want;
      if (want === 0) {
        if (highCount >= maxHigh) { it.level = 1; continue; }  // 高模数量上限
        highCount++;
        if (!it.high && !loading.has(id)) {
          loading.add(id);
          loadModel(id, 'high').then(m => {              // 异步加载，期间用低模占位
            it.high = m; swap(it, m); loading.delete(id);
          });
        } else if (it.high) swap(it, it.high);
      } else if (want === 1) {
        if (!it.low) it.low = buildLowProxy(it.obj);      // 低模/占位
        swap(it, it.low);
        if (it.high) dispose(it.high), it.high = null;    // 卸载高模释放显存
      } else {
        showAsPoint(it.obj);                              // 远处点表达
      }
    }
  }
  const swap = (it, m) => { it.obj.remove(it.current); it.obj.add(m); it.current = m; };
  return { register: (id, obj) => items.set(id, { obj, level: 2 }), update };
}
function dispose(m) {
  m.geometry?.dispose();
  (m.material ?? []).concat(m.material ?? []).forEach(x => x.dispose?.());
}
```

**评分点**:
- 迟滞区间（0.9 系数）防边界距离抖动。
- 高模数量上限 + 加载去重。
- 降级时 dispose 高模释放显存（泄漏意识）。
- 高模加载期间低模占位（无空窗）。
