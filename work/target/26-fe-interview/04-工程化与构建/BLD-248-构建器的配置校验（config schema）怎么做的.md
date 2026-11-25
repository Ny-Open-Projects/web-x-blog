---
title: [BLD-248] 构建配置的校验（config schema/防呆）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-248：配置校验怎么做？
**答**：
- 校验层：schema 校验（未知字段警告——拼错配置名静默无效是头号坑）、语义校验（互斥选项冲突警告）、值校验（路径存在/版本兼容）。
- 常见防呆点：alias 指向不存在路径（警告）、resolve.extensions 重复、插件顺序依赖声明、define 值非字面量（SCN-BLD-229 DCE 失效警告）。
- 错误信息的可行动性（SCN-BLD-223 标准）——配置错误带修复建议。
- preset 场景：override 与 preset 的冲突检测（项目覆盖破坏 preset 假设）。
- 追问钩子：为什么「未知字段警告」比「未知字段报错」更合理——配置对象的扩展性（插件可注入自有字段）与拼写防呆是矛盾体；警告让拼写错误可见（提示「你是不是想配 cache？」）而不破坏合法扩展——schema 防呆的甜点是警告级。

```javascript
// config schema 校验
validateConfig(config, viteConfigSchema, {
  unknownField: (path) => warn(`未知配置 ${path}——拼写检查（是否想配 cache？）`),
  conflict: (a, b) => warn(`${a} 与 ${b} 互斥`),
  literalCheck: (k, v) => k.startsWith('define') && typeof v !== 'boolean'
    && warn(`define.${k} 应为字面量（否则 DCE 失效）`),
});
```
