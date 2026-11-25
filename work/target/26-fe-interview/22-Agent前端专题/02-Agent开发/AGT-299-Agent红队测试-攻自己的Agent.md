---
title: [AGT-299] Agent 红队测试——怎么系统地攻击自己的 Agent？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-299：上线前的红队测试怎么设计——攻击面与用例库怎么建？

**答**:
- 攻击面清单：提示注入（直接/间接/多轮，AGT-281/288）、越权（诱导调用未授权工具/读取越权数据）、数据外泄（诱导外发/打印敏感数据）、拒绝服务（循环调用/资源耗尽）、内容安全（越狱生成违规内容）、投毒（恶意文档入库，AGT-287）——按攻击面建用例库。
- 用例库组织：每类攻击含模板与变体（改写/混淆/多语言），持续从公开漏洞（红队报告/社区披露）与内部 incident 扩充；样本带"期望行为"断言（拒绝/降级/人审触发）。
- 执行方式：自动化红队（攻击生成器批量变体跑，程序断言）+ 人工红队（探索性攻击，找自动化覆盖不到的新模式）结合；上线前全量跑，上线后每版本回归。
- 结果处置：发现的漏洞分级（高危阻断上线/中危限期修复/低危记录），修复后回归验证；红队发现进安全回归集——红队的价值在于变成持续资产而非一次性报告。

```javascript
const redteamSuite = {
  injection: loadCases('injection/*.yaml'),    // 模板+变体
  exfil: loadCases('exfil/*.yaml'),
  jailbreak: loadCases('jailbreak/*.yaml'),
};
async function runRedTeam(agent) {
  for (const [cat, cases] of Object.entries(redteamSuite)) {
    for (const c of cases) {
      const r = await agent.run(c.input, c.env);
      const ok = c.expect(r);                 // 断言期望行为
      report({ cat, id: c.id, ok, sev: c.severity });
    }
  }
}
// 高危失败 → 阻断上线；修复 → 回归验证 → 入回归集
```
