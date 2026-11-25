---
title: [WCN-823] 企业 WC 迁移的「定期合规巡检」怎么落地？（跨仓扫描）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-823：企业 WC 迁移的「定期合规巡检」怎么落地？（跨仓扫描）

**答**：
- 结论先行：标准发布后最大的风险是「写了规范没人遵守」——合规巡检就是把规范变成定期自动扫描，输出可追踪的整改清单，而不是靠人肉 review。
- 巡检内容：是否用了弃用的旧 API、是否绕过 token 写裸值、组件版本是否过旧/有漏洞、a11y 关键属性是否缺失、是否私自分发了未注册的组件。
- 实现方式：CI 集成静态扫描（AST 分析 import/tagName/属性）+ 运行时探针（采样真实页面的 DOM 与版本）+ 依赖锁文件审计，三者互补——静态覆盖源码、运行时覆盖真实用法。
- 输出与闭环：生成「仓库 × 违规项 × 严重级别」报告，自动建 issue 指派 owner，设整改 SLA；把巡检结果纳入团队健康分，形成持续压力。
- 渐进治理：先「只报告不阻断」，给整改期；达标率提升后再升级为「CI 阻断」，避免一上来就卡死业务。
- 追问钩子：面试官会问「扫描误报太多业务方抗议怎么办」——答：分级处理——高置信规则才阻断、低置信 rule 只提示并给白名单机制，同时持续优化规则精度，别让巡检变成噪音制造机。

```javascript
// 合规巡检：静态扫描结果汇总 + 严重分级 + 整改 issue 生成
const RULES = {
  'bare-color':   { level: 'warn',  desc: '检测到硬编码颜色，应使用 token' },
  'deprecated-api':{ level: 'error', desc: '使用了已弃用的 API' },
  'old-version':  { level: 'error', desc: '组件版本低于安全基线' },
};
function inspect(findings) {
  const issues = [];
  for (const f of findings) {
    const rule = RULES[f.rule];
    if (!rule) continue;
    issues.push({ repo: f.repo, file: f.file, level: rule.level,
                  desc: rule.desc, assignee: f.owner });
  }
  const blocking = issues.filter(i => i.level === 'error');
  return { issues, shouldBlock: blocking.length > 0, blockingCount: blocking.length };
}
console.log(inspect([{ repo: 'web-a', file: 'x.tsx', rule: 'deprecated-api', owner: 'TeamA' }]));
```
