---
title: [WCN-709] 组件 API 发生 breaking change 时，如何用 codemod 帮调用方自动迁移？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-709：组件 API 发生 breaking change 时，如何用 codemod 帮调用方自动迁移？

**答**：
- 结论：codemod 是基于 AST 的批量代码改写脚本（jscodeshift/ts-morph），比正则安全；对每个 breaking change 配一条 transform 规则。
- 流程：变更同时产出迁移规则 → 在 CI 对引用仓库跑 dry-run → 生成 diff 供 review → 人工确认后提交；保留回滚说明。
- 追问钩子：codemod 无法 100% 覆盖的场景怎么处理？考察「自动改写 + 显式告警 + 迁移文档」的分层策略。

```javascript
// 伪代码：属性重命名 codemod 的 AST 访问器
function transform(oldProp, newProp) {
  return (file, api) => {
    const j = api.jscodeshift;
    const root = j(file.source);
    // 把 <Comp oldProp={x} /> 改成 <Comp newProp={x} />
    root.findJSXElements().forEach((path) => {
      const attrs = path.node.openingElement.attributes;
      attrs.forEach((a) => {
        if (a.type === 'JSXAttribute' && a.name.name === oldProp) {
          a.name.name = newProp;
        }
      });
    });
    return root.toSource();
  };
}
console.log('为每类 breaking change 配一条 transform');
```
