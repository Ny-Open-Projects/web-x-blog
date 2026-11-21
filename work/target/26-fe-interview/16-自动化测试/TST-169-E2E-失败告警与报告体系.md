---
title: [TST-169] E2E 的报告与失败告警体系怎么设计？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-169：E2E 的报告与失败告警体系怎么设计？
**答**：
- 报告设计目标：让「没跑过测试的人」5 分钟内知道挂了什么、为什么挂、去哪看现场。核心要素：通过率/耗时总览、失败用例清单（错误首行）、失败截图 + trace 链接、与上轮对比（新增失败优先展示）、flaky 标记（重试通过的用例单独列）。
- 失败即留痕：Playwright `screenshot: 'only-on-failure'` + `trace: 'on-first-retry'` + `video: 'retain-on-failure'`，artifact 上传 CI；HTML 报告链接贴进 PR 评论与告警消息。
- 告警分级：PR 阶段失败 → 阻断 + PR 评论（不需要群告警）；每夜全集失败 → 群机器人告警（@ 失败用例的 owner，从 CODEOWNERS/用例元数据映射）；核心链路（下单）失败 → 电话/ stronger 通道，因为它阻塞发版。
- 告警降噪：同一条用例连续失败合并为一条告警（首报 + 恢复通知）；重试通过的不告警但计入 flaky 看板；已知的 flaky 用例走独立 job，告警阈值不同。
- owner 映射：用例文件按目录归属业务域，失败告警直接路由到负责人的 IM 群——「谁的用例谁处理」，否则告警会被集体无视。

```javascript
// playwright.config.ts 报告链路
export default defineConfig({
  reporter: [
    ['html', { open: 'never' }],                    // CI artifact
    ['json', { outputFile: 'e2e.json' }],           // 供自研看板
    ['custom-notify'],                              // 自定义：失败→飞书机器人
  ],
  use: { trace: 'on-first-retry', screenshot: 'only-on-failure', video: 'retain-on-failure' },
});

// custom-notify 核心逻辑：失败用例 → owner 路由 → 飞书卡片
const failures = json.suites.flatMap(flattenSpecs).filter((s) => s.ok === false);
for (const f of failures) {
  const owner = mapOwner(f.file);                   // 目录 → owner 映射
  await postFeishu(`❌ ${f.title}\nowner: @${owner}\ntrace: ${traceUrl(f)}`);
}
```
