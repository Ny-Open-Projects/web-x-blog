---
title: [PER-601] 前端项目怎么做威胁建模？STRIDE 模型在前端场景如何应用？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-601：前端项目怎么做威胁建模？STRIDE 模型在前端场景如何应用？

**答**：
- 威胁建模在发版前做，把想起什么防什么变成系统性排查：对页面上的每个数据流（用户输入 -> 前端处理 -> API -> 存储）逐项过 STRIDE 六类威胁。
- 前端场景映射：Spoofing（伪造身份——token 窃取、伪造 postMessage 发送方）、Tampering（篡改——接口参数改包、本地存储数据篡改）、Repudiation（抵赖——操作无日志）、Information Disclosure（敏感数据暴露——前端明文缓存、越权渲染）、Denial of Service（前端 DoS——超大数据渲染卡死）、Elevation of Privilege（越权——隐藏按钮但接口不校验）。
- 前端输出物：一张数据流图 + 威胁清单 + 处置方案表，威胁标注风险等级与 owner，进需求评审，高危项作为发版卡口。
- 实操要点：前端威胁建模不用追求后端那种精度，重点是输入面"（URL/query/存储/postMessage/iframe/文件上传）和输出面"（innerHTML/动态样式/URL 跳转）两端。

```javascript

// STRIDE 前端威胁清单模板（评审时逐行过）
const threatModel = [
  { flow: 'URL query -> 渲染', threats: {
    S: '无', T: 'query 注入 DOM (DOM-XSS)',
    I: 'query 里的 token 被埋点采集外传',
    fix: '统一 safeRender；埋点脱敏过滤器', risk: 'high' } },
  { flow: 'postMessage -> 父页面', threats: {
    S: '任意来源伪造消息', T: '消息触发状态变更',
    fix: 'origin 白名单 + schema 校验', risk: 'medium' } },
  { flow: 'localStorage -> 结算页', threats: {
    S: '无', T: '用户篡改价格字段', I: '地址簿明文存储',
    fix: '价格以服务端为准；地址簿加密或改 sessionStorage', risk: 'high' } },
  { flow: '隐藏管理按钮', threats: {
    E: '前端隐藏但接口未校验 -> 水平越权',
    fix: '接口层强制鉴权，前端隐藏只是 UX', risk: 'high' } },
];
// 输出：高风险项进发版卡口，medium 进迭代排期
```
