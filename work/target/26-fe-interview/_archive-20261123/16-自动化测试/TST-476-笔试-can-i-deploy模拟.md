---
title: [TST-476] 笔试：模拟 Pact broker 的 can-i-deploy 判定。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-476：笔试：模拟 Pact broker 的 can-i-deploy 判定。
**题目**：输入验证记录 `[{provider, providerVersion, consumer, consumerVersion, verified, env}]`。判定：provider 版本要部署到 env 时，需「该环境内所有该 provider 的 consumer 版本」都已 verified。输出 `{allowed, blockers}`。

```javascript
function canDeploy(records, { provider, version, env }) {
  const consumers = records.filter(r => r.provider === provider && r.env === env)
    .map(r => r.consumer);
  const unique = [...new Set(consumers)];
  const blockers = unique.filter(c => {
    const rec = records.filter(r => r.provider === provider && r.consumer === c
      && r.providerVersion === version).sort((a, b) => b.verifiedAt - a.verifiedAt)[0];
    return !rec || !rec.verified;
  });
  return { allowed: blockers.length === 0,
    blockers: blockers.map(c => `consumer ${c} 未验证 provider ${provider}@${version}`) };
}

```

**评分点**：
- 按环境过滤在役 consumer。
- 每个 consumer 找对应 providerVersion 的验证记录（取最新）。
- blockers 列出未验证的 consumer（可执行修复）。
- 无 consumer 的 provider 允许部署（首发布语义）。
