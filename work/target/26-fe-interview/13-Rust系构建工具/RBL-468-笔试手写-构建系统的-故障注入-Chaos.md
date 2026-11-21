---
title: [RBL-468] 笔试：手写构建系统故障注入器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-468：手写构建系统故障注入器
**需求**：实现 `createChaos(orchestrator)`：1) 注入场景：缓存服务断连（验证回退本地）/ runner OOM（验证任务隔离重试）/ registry 慢（验证镜像切换）/ 磁盘满（验证配额拒绝与清理）；2) 注入方式：环境级（tc/netem 网络延迟）或进程级（包装 fetch 拦截）；3) 验证断言：注入后的预期行为（降级自动切换/重试成功/优雅失败）——断言失败即降级路径缺陷；4) 演练报告：注入场景 × 预期行为 × 实际行为 × MTTR；5) 生产安全：演练窗口 + 一键恢复 + 影响面声明。

```javascript
export function createChaos(orchestrator) {
  const log = []

  const scenarios = {
    'cache-disconnect': {
      inject: () => orchestrator.blockHost('cache.internal'),
      expect: (r) => r.cacheFellBackToLocal === true && r.buildOk === true,
      description: '缓存断连 → 自动回退本地缓存，构建不阻断',
    },
    'runner-oom': {
      inject: () => orchestrator.limitMemory('build-worker', 256 * 1024 * 1024),
      expect: (r) => r.oomTasks.every((t) => t.retried || t.failed === 'expected'),
      description: 'runner OOM → 任务重试或优雅失败，不阻塞其他任务',
    },
    'registry-slow': {
      inject: () => orchestrator.addLatency('registry.npm', 8000),
      expect: (r) => r.usedMirror === true || r.installOk === true,
      description: 'registry 慢 → 镜像切换或超时优雅处理',
    },
    'disk-full': {
      inject: () => orchestrator.fillDisk('/cache', 0.99),
      expect: (r) => r.cacheRejected === 'quota' && r.buildOk === true,
      description: '磁盘满 → 配额拒绝降级不缓存，构建继续',
    },
  }

  async function run(scenarioName) {
    const s = scenarios[scenarioName]
    if (!s) throw new Error(`unknown scenario ${scenarioName}`)
    const started = Date.now()
    await s.inject()
    const result = await orchestrator.runBuild()
    const passed = s.expect(result)
    log.push({ scenario: scenarioName, passed, mttr: Date.now() - started, at: Date.now() })
    await orchestrator.recover()
    return { scenario: scenarioName, passed, mttr: Date.now() - started,
      actual: { buildOk: result.buildOk, cacheFellBackToLocal: result.cacheFellBackToLocal } }
  }

  async function runAll() {
    const out = []
    for (const name of Object.keys(scenarios)) out.push(await run(name))
    return { out, md: out.map((r) => `- ${r.passed ? '✅' : '❌'} ${r.scenario}（MTTR ${r.mttr}ms）`).join('\n') }
  }

  return { run, runAll, log: () => log }
}
```
**评分点**：
- 四场景覆盖构建系统主要降级路径（缓存/内存/registry/磁盘）
- 断言式验证（expect 函数验证降级行为——不是跑完就完）
- MTTR 度量（恢复时间——演练的核心指标）
- 一键恢复 + 报告输出（演练闭环）
