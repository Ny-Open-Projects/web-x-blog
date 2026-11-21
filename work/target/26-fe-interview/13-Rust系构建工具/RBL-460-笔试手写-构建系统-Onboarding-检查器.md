---
title: [RBL-460] 笔试：手写新成员 Onboarding 检查器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-460：手写新成员 Onboarding 检查器
**需求**：实现 `createOnboardingChecker(env)`：1) 检查新成员本地环境就绪度：Node 版本匹配 / pnpm 安装 / .env 就绪（有默认值可跑）/ 依赖安装完整 / 首次构建通过；2) 输出分步指引（每项失败给出精确修复命令——不是文档链接而是可复制命令）；3) 时间预估（首次构建预热时间告知——预期管理）；4) 一键修复尝试（safe 项自动修复：如 pnpm install；危险项仅提示）；5) 结果持久化（onboarding 进度跟踪——卡在哪一步可见，驱动文档改进）。

```javascript
import { execSync } from 'node:child_process'

export function createOnboardingChecker(env /* { requiredNode, requiredPnpm } */) {
  const steps = []
  function check(name, ok, fix, { safe = false, estimateMin = 0 } = {}) {
    steps.push({ name, ok, fix, safe, estimateMin })
    return ok
  }

  function run() {
    // Node 版本
    const nodeOk = process.version.startsWith(env.requiredNode)
    check('Node 版本', nodeOk, nodeOk ? null : `nvm install ${env.requiredNode} && nvm use ${env.requiredNode}`)

    // pnpm
    let pnpmOk = false
    try { execSync('pnpm --version', { stdio: 'ignore' }); pnpmOk = true } catch {}
    check('pnpm 安装', pnpmOk, pnpmOk ? null : 'corepack enable && corepack prepare pnpm@latest --activate', { safe: true })

    // .env
    let envOk = false
    try { envOk = !!fs.readFileSync('.env', 'utf8') } catch {}
    check('.env 就绪', envOk, envOk ? null : 'cp .env.example .env && 填写必要变量')

    // 依赖与首次构建（safe 自动尝试）
    let depsOk = false
    try { execSync('pnpm install --frozen-lockfile', { stdio: 'ignore' }); depsOk = true } catch {}
    check('依赖安装', depsOk, depsOk ? null : 'pnpm install（已自动尝试）', { safe: true, estimateMin: 3 })

    const failed = steps.filter((s) => !s.ok)
    persist(steps)                                              // 进度跟踪
    return {
      ready: failed.length === 0,
      steps,
      next: failed[0]?.fix ?? '环境就绪，可以开始开发',
      totalEstimateMin: failed.reduce((s, x) => s + x.estimateMin, 0),
    }
  }

  async function autoFixSafe() {                                // safe 项自动修复
    for (const s of steps.filter((x) => !x.ok && x.safe)) {
      try { execSync(s.fix, { stdio: 'ignore' }); s.ok = true } catch {}
    }
    return run()
  }

  return { run, autoFixSafe }
}

function persist(steps) { /* 上报 onboarding 卡点（文档改进数据源） */ }
```
**评分点**：
- 可复制修复命令（不是文档链接——DX 的执行语义）
- safe 自动修复分级（install 类自动、env 填写类提示——自动化边界）
- 预期管理（首次构建时长预估）
- 进度持久化（卡点数据驱动文档改进——onboarding 是可运营的）
