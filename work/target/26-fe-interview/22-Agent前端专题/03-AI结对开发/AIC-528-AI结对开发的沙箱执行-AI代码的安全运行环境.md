---
title: [AIC-528] AI 代码的沙箱执行环境
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-528：AI 代码的沙箱执行

**答**:
- AI 代码的沙箱需求：Agent 生成的代码需要**运行验证**（测试/编译/lint）——但 AI 生成的代码不可信（可能含恶意代码/副作用/资源耗尽）——沙箱 = 安全执行环境：1) **进程隔离**（子进程执行——crash 不影响宿主 RBL-557；2) **资源限制**（CPU 时间/内存/文件系统/网络——Agent 的代码不能耗尽宿主资源；3) **文件系统隔离**（chroot/容器——AI 只能写指定目录；4) **网络隔离**（禁止外网——AI 代码不应发网络请求（除非显式允许）。
- 沙箱的实现层次：1) **进程级**（child_process spawn + timeout——轻量但安全性弱（子进程可访问宿主 FS）；2) **容器级**（Docker container——文件系统/网络/资源全隔离（重量级但安全）；3) **VM 级**（Firecracker microVM——最强隔离（AWS Lambda 的底层）；选择：CI 环境 → 容器；IDE 内 → 进程 + 资源限制。
- 追问钩子：为什么「Agent 的代码执行」必须沙箱化？——Agent 的代码 = LLM 生成（不可信——可能含 rm -rf / 或 curl evil.com）；LLM 的 prompt injection 可能导致 Agent 执行恶意命令（"运行这个命令清理临时文件" 实际是 rm -rf /）；沙箱 = 最后一道防线（即使 prompt injection 成功——沙箱限制破坏范围 RBL-942 的运行时版）；沙箱的必要性 = Agent 的自主执行权（Agent 可以不经人审直接执行——沙箱是自主执行的安全保障）。

```typescript
// Agent 沙箱执行器
import { spawn } from 'child_process';
interface SandboxOptions {
  timeoutMs?: number;         // 默认 30s
  maxMemoryMB?: number;       // 默认 512
  allowedPaths?: string[];    // 可写路径白名单
  networkEnabled?: boolean;   // 默认 false
}
async function sandboxExecute(cmd: string, args: string[], opts: SandboxOptions = {}) {
  const { timeoutMs = 30000, maxMemoryMB = 512 } = opts;
  return new Promise((resolve) => {
    const child = spawn(cmd, args, {
      timeout: timeoutMs,
      env: { PATH: process.env.PATH, NODE_OPTIONS: `--max-old-space-size=${maxMemoryMB}` },
      cwd: '/sandbox',                                     // 隔离工作目录
    });
    let stdout = '', stderr = '';
    child.stdout?.on('data', (d) => { stdout += d; });
    child.stderr?.on('data', (d) => { stderr += d; });
    const timer = setTimeout(() => {
      child.kill('SIGKILL');
      resolve({ code: -1, stdout, stderr: 'Sandbox timeout' });
    }, timeoutMs);
    child.on('close', (code) => {
      clearTimeout(timer);
      resolve({ code: code ?? -1, stdout, stderr });
    });
  });
}
// Agent 使用沙箱运行测试
const result = await sandboxExecute('npx', ['vitest', 'run'], { timeoutMs: 60000 });
if (result.code !== 0) {
  // Agent 读 stderr 修复代码
}
```
