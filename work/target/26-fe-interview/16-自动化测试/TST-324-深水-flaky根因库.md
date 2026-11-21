---
title: [TST-324] flaky 用例治理如何从「逐个修」升级为「根因库批量治」？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-324：flaky 用例治理如何从「逐个修」升级为「根因库批量治」？
**答**：
- 失败聚类：按错误特征（超时/元素未找到/断言差异）聚类统计。
- 根因库：每类根因（等待不足/共享数据/时钟依赖）配标准修法与工具函数。
- 批量治理：同根因用例批量应用标准修法（如统一 stableWait 工具）。
- 度量收敛：flaky 率周趋势，根因库覆盖的类别逐步清零。

```javascript
const flakyRootCauses = {
  'race-wait': { fix: 'stableWait工具（自动等待+重试断言）', affected: 45 },
  'shared-data': { fix: '数据工厂命名空间隔离', affected: 12 },
  'clock': { fix: 'page.clock 冻结', affected: 8 },
};
r
```
