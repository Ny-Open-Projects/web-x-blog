---
title: [PER-171] 安全事件的分级响应怎么做？P0 XSS 如何应急脚本化？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-171：安全事件的分级响应怎么做？P0 XSS 如何应急脚本化？

**答**：
- 分级标准：**P0** 数据外泄/全站挂马/凭证泄漏（15 分钟响应、1 小时止血）、**P1** 单页 XSS/可提权越权（24 小时修复）、**P2** 低危泄漏/头缺失（下迭代修复）。
- P0 XSS 止血四步脚本化：**入口下线或降级**（关功能开关）→ **紧急 CSP**（先 Report-Only 观察再强制）→ **内容清洗**（扫存储型字段转义 + 刷 CDN）→ **凭证加固**（会话 token 全量轮换）。
- 全程保留攻击 payload 与日志作为证据，不做破坏性清理动作。
- 事后 5 个工作日复盘，漏洞根因回写进安全规范总表与 Checklist。

```yaml
# 安全事件分级响应：P0 到 P3，每级有明确动作与时限
security_incident_playbook:
  levels:
    P0:
      definition: 数据外泄、全站 XSS 挂马、凭证泄漏
      response_sla: 15 分钟内响应，1 小时内止血
      actions:
        - 下线受影响入口或开启功能降级开关
        - 注入 Content-Security-Policy-Report-Only 紧急策略
        - 强制全员登出并轮换会话密钥
        - 清洗被注入的内容与外链并刷新 CDN
        - 保留攻击日志与 payload 作为证据
    P1:
      definition: 单页面 XSS、可提权越权
      response_sla: 2 小时响应，24 小时修复
    P2:
      definition: 低危信息泄漏、点击劫持头缺失
      response_sla: 下个迭代修复
  p0_xss_steps_order:
    - 1_止损：关开关或下线入口，阻断新增注入
    - 2_清洗：扫存储型字段转义，再刷 CDN 缓存
    - 3_加固：会话 token 全量轮换，刷新令牌作废重发
    - 4_取证：payload 与日志归档，供溯源与法务
  postmortem: 5 个工作日出报告，根因回写安全规范总表
```
