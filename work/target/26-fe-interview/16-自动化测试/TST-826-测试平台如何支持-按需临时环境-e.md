---
title: [TST-826] 测试平台如何支持「按需临时环境」(ephemeral environment) 与测试？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-826：测试平台如何支持「按需临时环境」(ephemeral environment) 与测试？
**答**：
- 结论：每条测试分支/每个 PR 拉起一套隔离的临时环境（前端预览 + 后端桩/沙箱库），测完即销毁，根治环境争抢与脏数据。
- 实现：用容器/Preview Deploy 按 PR 创建环境，URL 注入到测试用例；MSW/契约桩替代不稳定依赖。
- 生命周期：环境随 PR 创建、随合并/关闭销毁，超时自动回收，控制成本。
- 取舍：临时环境贵且慢，核心回归用稳定环境，PR 级验证才用临时环境，分级使用。
- 追问钩子：临时环境数量暴涨导致成本失控，你如何做「环境配额」与复用？

```javascript
// 临时环境生命周期管理
class EphemeralEnv {
  constructor() { this.envs = new Map(); }
  async create(prId) {
    const url = `https://pr-${prId}.preview.example.com`;
    this.envs.set(prId, { url, createdAt: Date.now(), status: 'ready' });
    return url;
  }
  async destroy(prId) { this.envs.delete(prId); }
  gc(ttlMs = 2 * 3600_000) { // 超时回收，控制成本
    const now = Date.now();
    for (const [id, env] of this.envs)
      if (now - env.createdAt > ttlMs) this.destroy(id);
  }
}
const mgr = new EphemeralEnv();
mgr.create(1024).then(url => console.log('测试环境:', url));
```
