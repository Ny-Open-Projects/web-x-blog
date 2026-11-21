---
title: [ARC-528] 前端的 IME（输入法）兼容架构与国际化输入如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-528：IME 兼容架构与国际化输入
**答**:
- IME 三阶段：compositionstart → compositionupdate → compositionend——组合期间的行为约定：不触发搜索/校验/自动保存（用拼音中间态触发是中文输入最大 bug 源 ARC-HW 系列延伸）。
- 架构收口：输入组件统一基类（onCompositionStart/End 状态管理，isComposing 判断进 keydown/change 分发）——业务组件不直接处理原生 input 事件。
- 各场景的 IME 约定：搜索（compositionend 后防抖触发）、快捷键（isComposing 时忽略 ARC-498）、自动保存（compositionend + debounce）、计数器（显示组合中文本需标注"输入中"）。
- 国际化输入差异：日文/韩文 romaji 转换更长、RTL 语言输入与光标方向、emoji 代理对（长度计数按 code point 而非 UTF-16 单元）。
- 测试策略：真机 IME 矩阵测试（各平台输入法差异大，模拟器不可靠）、自动化用 composition 事件模拟序列。
```javascript
// IME 感知输入基类
class ImeAwareInput extends Input {
  #composing = false;
  oncompositionstart() { this.#composing = true; }
  oncompositionend(e) { this.#composing = false; this.emit('final', e.data); } // 只发最终值
  oninput(e) { if (!this.#composing) this.emit('final', e.data); }             // 非组合直发
  onkeydown(e) { if (e.isComposing || e.keyCode === 229) return; }             // 229 兼容
}
```
