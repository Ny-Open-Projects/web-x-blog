---
title: [TST-160] test.skip / only / fixme / todo 怎么治理？被禁用的测试去哪了？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-160：test.skip / only / fixme / todo 怎么治理？被禁用的测试去哪了？
**答**：
- 三类语义要分清：`skip`（已知不跑，需理由）、`fixme`（有 bug 暂时禁用，必须关联 issue）、`todo`（计划要写的用例）。`.only` 在主干必须被禁止——CI 加检测脚本，发现 `.only` 直接 fail（本地调试允许，提交前 lint 拦截）。
- skip 的治理规则：① 必须带注释或 issue 链接（`test.skip('...')` 的理由写进 describe）；② 有 TTL——CI 每周输出 skip 清单与时长，超过 2 周的 skip 升级到站会强制处理（修/删/转 tracking issue）；③ skip 数量是质量指标，纳入看板。
- 反模式：「测试挂了先 skip 保 CI 绿」——正确做法是「隔离（移出门禁套件）而不是静默」，skip 挂在原地会让人以为它还在守护；隔离到 `describe.sequential('quarantine')` 或独立 job 每天跑。
- eslint 工具链：`eslint-plugin-jest` 的 `no-disabled-tests`（要求理由）、`no-focused-tests`（禁 .only）+ 自定义 CI 预检脚本。
- 追问钩子：被禁用的测试最后去哪？——三个出口：修复恢复、确认为过时直接删（Git 历史可找回）、转为 tracking issue 带上原始用例内容。绝不允许「永久 skip」。

```javascript
// ❌ 无理由 skip
test.skip('退款流程', () => {});

// ✅ 有理由、有跟踪、有期限
// FIXME(JIRA-4521, owner: wang, due: 2026-12-01): 支付沙箱不稳定，修复后恢复
test.skip('退款流程', () => {});

// CI 预检脚本：禁 .only + skip 必须带 FIXME 标记
// .eslintrc
{
  "rules": {
    "jest/no-focused-tests": "error",        // .only 直接 fail
    "jest/no-disabled-tests": "warn"          // skip 告警，清单化跟踪
  }
}
```
