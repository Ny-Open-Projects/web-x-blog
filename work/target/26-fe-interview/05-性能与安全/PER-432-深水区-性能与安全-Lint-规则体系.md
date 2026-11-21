---
title: [PER-432] 性能与安全的 Lint 规则体系：哪些问题应该在代码评审前被自动拦住？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-432：性能与安全的 Lint 规则体系：哪些问题应该在评审前被自动拦住？

**答**:
- 价值：人工评审漏检率高的机械性问题（读写交错/危险 API/反模式）交给 lint，评审聚焦架构与业务。规则体系分三级：error（CI 拦截）、warn（评审提示）、info（建议）。
- 性能规则清单：no-layout-thrashing（读写交错模式，PER-404）、no-sync-layout-in-loop、限制单文件大依赖导入（如 import lodash 全量）、禁止在 render 中创建大对象、虚拟列表阈值提醒（列表 map 超 200 条提示虚拟化）、图片组件强制使用（禁用原生 <img> 大图场景）。
- 安全规则清单：禁 innerHTML 直赋（必须过净化组件）、禁 eval/new Function、禁 hardcode 密钥（模式匹配）、禁 target=_blank 不带 rel=noopener、postMessage origin 通配检测、dangerouslySetInnerHTML 白名单组件。
- 规则治理：规则本身要评审（误报率 > 20% 的规则回炉）；规则带文档（为什么/怎么改）；新规则先 warn 一季度再升 error。

```text
性能与安全 Lint 规则（三级）：
性能：
  error: no-layout-thrashing / no-sync-layout-in-loop
  warn:  大依赖全量导入 / render 内大对象分配 / 列表>200 未虚拟化提示
  info:  图片组件强制使用建议
安全：
  error: 禁 eval/Function / innerHTML 直赋（非净化组件） / hardcode 密钥模式
  warn:  target=_blank 缺 noopener / postMessage origin '*' / dangerouslySetInnerHTML
规则治理：误报率 > 20% 回炉；每规则带文档；新规则 warn 一季度 → error
```
