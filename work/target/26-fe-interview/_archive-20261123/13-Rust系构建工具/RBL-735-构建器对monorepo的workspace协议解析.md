---
title: [RBL-735] workspace 协议解析：workspace:*、injection 策略与发布态转换
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-735：workspace 协议解析：workspace:*、injection 策略与发布态转换

**答**:
- workspace 协议的三种声明：`workspace:*`（任意版本）、`workspace:^`（开发态保留 ^）、`workspace:~`——语义差异在发布态转换：pnpm/yarn 发布时把 `workspace:*` 替换为依赖包的**实际版本**（^ 保留 ^ 前缀）；构建器解析时要知道「开发态指向 symlink 源码、发布态指向 registry 版本」的双态语义。
- injection 策略（pnpm 的 injectWorkspace）：workspace 依赖默认 symlink（源码直连），inject 模式把 workspace 包复制安装（模拟 registry 行为——验证发布态解析）；构建器配置里 mode: 'dev'|'prod' 要与 injection 策略对齐，否则「开发没问题发布坏」。
- 发布态转换的验证：CI 里「发布演练」（pack 后检查依赖声明是否正确替换、产物是否可独立安装）——workspace 协议漏转换（发布包里残留 workspace:*）是 npm 安装失败的经典事故，registry 直接拒绝。
- 构建器的双态支持：dev 模式 resolve 到源码（RBL-701），release 构建模拟 registry 解析（node_modules 里没有 workspace 依赖时按声明版本解析）——「release 构建 = 发布后世界」的提前验证。
- 追问钩子：为什么「发布演练」必须用干净环境？——开发态的 node_modules 是 symlink 世界的（workspace 依赖物理存在），演练要模拟「只装 registry 依赖」的世界——pnpm deploy/CI 专用目录才接近发布真相；在开发目录里演练是自欺。

```javascript
// workspace 协议解析与发布态转换
function resolveWorkspaceDep(spec, targetVersion, mode) {
  if (!spec.startsWith('workspace:')) return spec;       // 普通 semver 原样
  const op = spec.slice('workspace:'.length);            // * / ^ / ~
  if (mode === 'dev') return op === '*' ? '*' : op + targetVersion;   // 开发态
  // 发布态：转换成真实版本
  if (op === '*') return targetVersion;                  // workspace:* -> 1.2.3
  return op + targetVersion;                             // workspace:^ -> ^1.2.3
}
// 发布演练（干净环境验证）
async function dryPack(pkg) {
  const out = await exec(`pnpm pack --pack-destination /tmp/pack-test`, { cwd: pkg.dir });
  const tarball = JSON.parse(await exec(`npm view ./tmp/pack-test/${out} dependencies --json`));
  for (const [name, spec] of Object.entries(tarball))
    if (spec.startsWith('workspace:'))
      fail(`${name} 残留 workspace 协议：发布态未转换（registry 将拒绝）`);
}
```
