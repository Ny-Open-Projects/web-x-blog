---
title: [HW-141] 手写输入法（IME）兼容的搜索输入——compositionstart/end 期间不触发搜索与计数
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：中文输入法（IME）在 composition 期间（拼音串）会触发 input 事件——防抖搜索会在"拼音没确认"时发起错误请求。正确处理：compositionstart 置 composing=true（期间忽略 input），compositionend 时立即触发一次搜索（用户确认拼音的瞬间响应）。

```javascript
function attachIMESearch(input, onSearch) {
  let composing = false;
  input.addEventListener('compositionstart', () => { composing = true; });
  input.addEventListener('compositionend', () => {
    composing = false;
    onSearch(input.value);                            // 拼音确认瞬间立即搜索（不等防抖）
  });
  input.addEventListener('input', () => {
    if (composing) return;                            // IME 期间：不触发搜索
    onSearch(input.value);                            // 英文/数字：正常防抖路径
  });
}
// <input id="q" /> attachIMESearch(q, debounce(search, 300))
// 反例：不处理 composition —— 用户打"搜索"会依次触发 s/sou/suos/搜索 四次搜索
// 计数器类（字数统计）同理：composition 期间不计入（拼音串不是最终内容）
// Safari 的 compositionend 在 input 之后/之前的顺序差异：以 compositionend 为准设 composing=false
```

**评分点**：
- compositionstart/end 的忽略与恢复语义正确——中文场景核心考点。
- compositionend 立即触发（不等防抖）——即时性正确。
- 能说出反例后果（拼音串逐字母触发搜索）。
- 字数统计同理 + Safari 时序差异意识。
