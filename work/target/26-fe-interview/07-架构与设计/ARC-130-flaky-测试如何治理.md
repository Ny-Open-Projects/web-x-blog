---
title: [ARC-130] flaky 测试如何治理？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-130：flaky 测试如何治理？
**答**：
- 识别：CI 每次运行上报结果，重跑通过的用例自动标记 suspect；连续 N 次 flaky 率超阈值进隔离区（quarantine）——隔离区用例仍然运行但不阻塞合并，且有 owner 与处理期限。
- 根因分类统计（治本）：时序/异步等待不当（占大头）→ 用 waitFor/假时钟替代；共享状态（全局单例、DB 残留）→ 用例隔离与 beforeEach 清理；外部依赖（真实网络/时钟）→ msw/假时钟；断言过严（顺序/浮动比较）→ 修断言。
- 制度：flaky 率作为团队质量 SLO（如主干 flaky 率 < 0.5%）；重试只是止血，"靠 retry 绿灯"的用例必须限期修复，否则删除。
- 红线：禁止用例间依赖顺序、禁止依赖真实第三方网络——这两条规则能预防大多数 flaky。

```typescript
// flaky 治理：上报 + 隔离区机制
interface TestResult { suite: string; name: string; status: 'pass' | 'fail' | 'flaky'; durationMs: number }

class FlakyTracker {
  // 1. CI 结果上报：同一次 CI 内先 fail 后 retry-pass → flaky
  async report(r: TestResult, attempt: number) {
    if (r.status === 'pass' && attempt > 1) {
      r.status = 'flaky';
      await db.insert('flaky_events', { ...r, ciRunId: runId, detectedAt: Date.now() });
    }
  }
  // 2. 周期计算 flaky 率，超标入隔离区
  async quarantineSweep() {
    const stats = await db.query(`
      SELECT suite, name, count(*) FILTER (WHERE status = 'flaky') * 100.0 / count(*) AS rate
      FROM flaky_events WHERE detected_at > now() - interval '14 days'
      GROUP BY 1, 2 HAVING rate > 20`);
    for (const s of stats) {
      await this.markQuarantined(s, { owner: await codeOwnerOf(s.suite), deadline: addDays(14) });
      notify(s.owner, `用例 ${s.name} flaky 率 ${s.rate}%，14 天内修复，否则删除`);
    }
  }
}
// 3. 测试执行器消费隔离区：quarantined 用例跑但失败不阻塞
// 配置方式：vitest.config 中 exclude 引入隔离区清单文件（自动生成）
```
