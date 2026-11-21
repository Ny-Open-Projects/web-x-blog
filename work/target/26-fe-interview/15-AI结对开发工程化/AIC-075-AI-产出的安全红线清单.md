---
title: [AIC-075] 团队的「AI 产出安全红线清单」应该包含哪些条目？怎么让它真的被执行而不是挂在墙上？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-075：团队的「AI 产出安全红线清单」应该包含哪些条目？怎么让它真的被执行而不是挂在墙上？
**答**：
- 条目分层：数据红线（真实用户数据、生产日志、密钥不进 prompt）；产出红线（无校验的 eval/new Function、硬编码凭据、危险权限提升）；流程红线（安全相关模块 AI 产出必须双人复核、不允许 AI 产物直接上生产而不经 CI）。
- 执行靠「自动化检查 + 门禁」而非口头约定：密钥扫描（gitleaks 类）、危险 API 静态检查、CI 强制 ai-review 安审项（AIC-045）——墙上的清单要翻译成 grep 规则。
- 教育配套：红线违反案例做匿名复盘分享，让团队知道「为什么有这条」；规则文件里同步写红线（让 AI 自己先守）。
- 审计留痕：每次红线条目的触发与豁免都记录，月度报告给管理层——没有度量的清单三个月就会死。
- 追问钩子：红线也要「最小化」——20 条执行不了不如 5 条全部自动检查，宁少勿多。

```javascript
// 红线的可执行化：静态检查规则示例
const redlineChecks = [
  { id: 'RL-01', desc: '禁止硬编码凭据', test: src => /(api[_-]?key|secret|password)\s*[:=]\s*['"][^'"]{8,}/i.test(src) },
  { id: 'RL-02', desc: '禁止动态执行', test: src => /\b(eval|new Function)\s*\(/.test(src) },
  { id: 'RL-03', desc: '禁止生产数据进 prompt', test: prompt => /(身份证|手机号1[3-9]\d{9})/.test(prompt) },
];
function scanRedlines(artifacts) {
  return artifacts.flatMap(a => redlineChecks
    .filter(c => c.test(a.content)).map(c => ({ file: a.file, rule: c.id, desc: c.desc })));
}
```
