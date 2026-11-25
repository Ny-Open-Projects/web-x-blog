---
title: [WCN-781] 设计系统如何做到「默认合规」的可访问性，而非事后修补？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-781：设计系统如何做到「默认合规」的可访问性，而非事后修补？

**答**：
- 结论：把 a11y 内建到组件基座——语义化标签、role/aria 默认正确、键盘导航（focus/Enter/Esc）、对比度达标作为组件验收门槛，而非上线后扫描补洞。
- 建立 a11y 基线（WCAG 2.1 AA）与自动化检查（axe）接入 CI；每个组件提供键盘操作说明与测试用例如「仅键盘能否完成主流程」。
- 追问钩子：视觉设计师追求的低对比度效果与 a11y 冲突怎么办？考察「设计阶段介入 + 提供合规替代方案」而非开发期妥协。

```javascript
// 组件默认合规示例：可关闭的对话框
class DsDialog extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <div role="dialog" aria-modal="true" aria-labelledby="t" tabindex="-1">
        <h2 id="t">标题</h2><button aria-label="关闭">×</button>
      </div>`;
    this.querySelector('button').addEventListener('click', () => this.close());
    this.addEventListener('keydown', (e) => { if (e.key === 'Escape') this.close(); });
  }
  close() { this.remove(); }
}
console.log('默认含 role/aria/键盘支持');
```
