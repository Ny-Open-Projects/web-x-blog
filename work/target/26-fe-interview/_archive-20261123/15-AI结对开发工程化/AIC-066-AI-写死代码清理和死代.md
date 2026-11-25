---
title: [AIC-066] 用 AI 清理死代码和废弃 API 有什么风险？「引用分析」为什么必须走在删除之前？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-066：用 AI 清理死代码和废弃 API 有什么风险？「引用分析」为什么必须走在删除之前？
**答**：
- 风险根源：AI 判断「没被引用」靠文本匹配，会漏掉动态引用——字符串拼接的组件名（懒加载）、re-export 中转、运行时反射调用、外部项目引用。
- 正确顺序：先用确定性工具（ts-prune/knip/ESLint unused、构建产物的 tree-shaking 报告）产出死代码候选清单，AI 只负责「解释每个候选为什么安全/不安全 + 生成删除 PR」。
- 分批删除：每批 ≤ 10 个符号，删完跑全量构建与冒烟；灰度观察一天再下一批——删除类变更出问题往往在线上而非测试。
- 特殊保护区：公共包的导出（下游可能在用）、配置文件里字符串引用的路径、埋点 key——这些静态分析也看不出来，必须人工圈定。
- 追问钩子：「删了又被引用回来」的回收事件是最好教材，用来说明为什么清单工具 + AI 解释 + 人拍板缺一不可。

```javascript
// 死代码候选 → AI 解释 → 分批删除
async function safeDeadCodeRemoval(candidates, { batchSize = 10 } = {}) {
  const batches = chunk(candidates, batchSize);
  for (const batch of batches) {
    const report = await callLLM(`逐个解释以下符号删除是否安全，注意动态引用：\n${batch.join('\n')}`);
    const unsafe = report.filter(r => !r.safe);
    if (unsafe.length) continue; // 有不确定符号则整批跳过
    removeSymbols(batch);
    await runBuildAndSmoke(); // 失败即回滚
  }
}
```
