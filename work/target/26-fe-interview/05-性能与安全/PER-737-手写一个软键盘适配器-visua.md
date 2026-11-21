---
title: [PER-737] 手写一个软键盘适配器：visualViewport 驱动 + 输入框自动滚入可视区 + 键盘收起恢复
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-737：手写一个软键盘适配器：visualViewport 驱动 + 输入框自动滚入可视区 + 键盘收起恢复

**答**：
- 完整实现：监听 viewport resize -> 计算键盘高度 -> 聚焦输入框滚入可视区（getBoundingClientRect + scrollTo，等 viewport 稳定后执行）-> 失焦恢复布局。
- 要点：聚焦处理延迟到 viewport resize 后（iOS 键盘动画 300ms 内 viewport 才稳定，立即算会错）；滚动用 smooth 但要防与用户滚动竞争（仅当输入框确实不可见时滚）；恢复时回滚到键盘弹起前位置（记录 anchor）。
- 边界：外接键盘（viewport 不变）跳过；多输入框 Tab 切换连续触发要防抖合并；WebView 关闭键盘调整模式时降级 JS 方案。
- 评分点：等 viewport 稳定再算与 anchor 恢复。

```javascript

class KeyboardAdapter {
  constructor(container) {
    this.container = container; this.anchorY = scrollY;
    const vv = window.visualViewport;
    if (!vv) return;
    vv.addEventListener('resize', () => this.onViewportChange());
  }
  onViewportChange() {
    const vv = window.visualViewport;
    this.kbHeight = innerHeight - vv.height;                    // 稳定后再算
    if (this.kbHeight > 100) this.ensureFocusedVisible();       // 键盘弹起
    else this.restore();
  }
  ensureFocusedVisible() {
    const active = document.activeElement;
    if (!(active instanceof HTMLInputElement || active instanceof HTMLTextAreaElement)) return;
    requestAnimationFrame(() => {
      const rect = active.getBoundingClientRect();
      const vv = window.visualViewport;
      const visibleBottom = vv.offsetTop + vv.height;
      if (rect.bottom > visibleBottom) {                        // 确实不可见才滚
        scrollTo({ top: scrollY + rect.bottom - visibleBottom + 12, behavior: 'smooth' });
      }
    });
  }
  restore() {                                                   // 收起恢复 anchor
    if (this.anchorY && Math.abs(scrollY - this.anchorY) > 50)
      scrollTo({ top: this.anchorY });
  }
  onFocus(input) { this.anchorY = scrollY; }                    // 聚焦时记 anchor
}
```
