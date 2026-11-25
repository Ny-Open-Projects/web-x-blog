---
title: [AIC-020] AI 生成的代码出了线上事故，责任怎么算？团队流程上如何区分「AI 引入」的缺陷？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-020：AI 生成的代码出了线上事故，责任怎么算？团队流程上如何区分「AI 引入」的缺陷？
**答**：
- 责任人永远是提交者与审批者：AI 是工具，代码合入的每一步都有人的签名（commit author + reviewer），事故归因到流程失效而不是工具。
- 但归因信息要采集：缺陷工单打标 `ai-assisted: true/false`，积累数据才能回答「AI 代码缺陷率是否更高、高在哪类缺陷」。
- 流程上的防复发按归因分支：AI 引入 → 补规则/补测试模板/收紧 agent 权限；人为引入 → 正常 review 流程复盘。两者改进手段不同，所以打标有工程价值。
- 常见 AI 特征缺陷类型：臆造 API、依赖版本幻觉、mock 了被测逻辑的假测试、静默吞错误——这些方向可定向加门禁。
- 追问钩子：能说出「事故复盘要问的是流程为什么放过了它，而不是谁写的」体现成熟度。

```text
缺陷打标流程（工单系统字段）：

root_cause_type: hallucinated_api | logic_error | race | config | ...
ai_assisted: true
ai_tool: cursor-agent | copilot | ...
escaped_gate: review | unit-test | e2e | none   ← 哪道门禁漏了它

复盘输出两分支：
AI 引入 → 更新 .cursor/rules + 新增对应 lint/测试模板
人为引入 → 评审 checklist 修订 + 培训
```
