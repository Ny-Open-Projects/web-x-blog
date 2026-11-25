---
title: [TST-930] 微前端共享依赖（React 版本、lodash）如何做「版本契约」测试防止重复实例？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-930：微前端共享依赖（React 版本、lodash）如何做「版本契约」测试防止重复实例？
**答**：
- 结论：共享依赖要锁定「单一版本 + 单一实例」——主应用通过 externals/shared 提供，子应用禁止自带副本，用构建产物分析验证。
- 测法：构建后扫描 bundle，断言 react 只出现一次；运行时检查 window.__react_version__ 与子应用内 require('react') 是同一对象引用。
- 风险：双实例会导致 hooks 报错（Invalid hook call）、context 丢失、包体积翻倍。
- 追问钩子：大促主应用升级 React 18，某个子应用仍打包了 React 17，E2E 没报错但线上 hooks 偶发崩，你怎么提前发现？

```javascript
// 构建产物分析：断言 react 只被打包一次
const { stats } = await build();
const reactModules = stats.modules.filter(m => /node_modules\/react\//.test(m.name));
const versions = [...new Set(reactModules.map(m => m.version))];
if (versions.length > 1) throw new Error(`检测到多个 React 版本: ${versions.join(', ')}`);

// 运行时：主子应用共享同一实例
test('React 单实例契约', async () => {
  const same = await page.evaluate(() => {
    const main = window.__SHARED_REACT__;
    const sub = window.subAppRequire('react');
    return main === sub;
  });
  expect(same).toBe(true);
});
```
