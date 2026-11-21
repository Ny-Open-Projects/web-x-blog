---
title: [JS-325] eval 与 new Function 的风险与替代
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## JS-325：eval 与 new Function 的风险与替代

**答**：
- 共同风险：任意代码执行（XSS 放大器）、作用域穿透、CSP 直接拦截（unsafe-eval）、性能差（无法优化）
- 差异：eval 沿用当前作用域（可读写局部变量）；new Function 全新函数作用域（只能碰全局）——后者略可控
- CSP 视角：两者都需 unsafe-eval，线上站点几乎必禁——依赖 eval 的库（旧版模板引擎）直接被判死刑
- 替代清单：模板字符串/模板引擎（预编译）、JSON.parse（数据）、Function 构造降级为查表映射、new Function 场景改 Web Worker（独立作用域仍受限 CSP）
- 历史包袱：JSONP 回调、部分拖拽库——现代代码审查中 eval 是必查红线

```javascript
// ❌ 危险：用户输入直达 eval
const expr = userInput; // "1); alert(document.cookie"
// eval('calc(' + expr + ')');
// ✅ 替代：白名单映射或受限解析
const OPS = { '+': (a, b) => a + b, '-': (a, b) => a - b };
function calc(op, a, b) {
  const fn = OPS[op];
  if (!fn) throw new Error('不支持的操作'); // 白名单拒绝
  return fn(a, b);
}
```
