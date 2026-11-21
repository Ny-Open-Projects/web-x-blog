---
title: [PER-605] 手写一个运行时 XSS 检测钩子：拦截 innerHTML 赋值并在测试环境自动标记可疑注入
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-605：手写一个运行时 XSS 检测钩子：拦截 innerHTML 赋值并在测试环境自动标记可疑注入

**答**：
- 在静态扫描之外做运行时兜底：重写 `Element.prototype` 的 innerHTML/outerHTML setter，检测赋值内容是否包含可疑模式（`<script`、`on*=`、`javascript:`），测试环境记录、生产环境可选上报。
- 要点：用 `Object.defineProperty` 覆盖 setter 时要保留原生行为（赋值后仍真正写入）；hook 自身性能要低（简单正则，不做完整解析）；React/Vue 场景只在开发环境开启（框架自身有转义，hook 用于查业务代码绕过点）。
- 边界：hook 要排除监控 SDK 自身的写入；对受信任的常量模板（白名单标记）不告警。
- 评分点：setter 覆盖保留原语义与白名单排除。

```javascript

function installRuntimeXssHook({ report, whitelist = [] } = {}) {
  const DESC = Object.getOwnPropertyDescriptor(Element.prototype, 'innerHTML');
  const SUSPICIOUS = /<script|on\w+\s*=|javascript:/i;
  Object.defineProperty(Element.prototype, 'innerHTML', {
    set(value) {
      const trusted = whitelist.some(w => typeof value === 'string' && value.includes(w));
      if (!trusted && typeof value === 'string' && SUSPICIOUS.test(value)) {
        report({ hook: 'innerHTML', suspect: value.slice(0, 200),
          stack: new Error().stack?.split('\n')[2] });       // 调用方归因
      }
      DESC.set.call(this, value);                             // 保留原生写入
    },
    get() { return DESC.get.call(this); },
    configurable: true,
  });
}
// 测试环境开启 + e2e 跑完后汇总可疑赋值清单 -> 逐个修成安全 API
```
