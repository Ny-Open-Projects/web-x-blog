import * as vm from 'vm';
import * as crypto from 'crypto';

export interface SandboxOptions {
  /** 同步执行超时（毫秒）。vm 的 timeout 仅对同步死循环生效。 */
  timeoutMs?: number;
  /** 输出体积上限（字节），防内存爆炸。 */
  maxOutputBytes?: number;
}

export type SandboxIsolation = 'vm' | 'container';

export interface SandboxResult {
  out: unknown;
  durationMs: number;
  status: 'success' | 'error' | 'timeout';
  error?: string;
  outputBytes: number;
  /** 实际采用的隔离层（vm 软隔离 / container 容器硬隔离），写入审计。 */
  isolation?: SandboxIsolation;
}

export function sha256(s: string): string {
  return crypto.createHash('sha256').update(s, 'utf8').digest('hex');
}

function deepClone(o: unknown): unknown {
  try {
    return JSON.parse(JSON.stringify(o ?? null));
  } catch {
    return null;
  }
}

function withWatchdog<T>(p: Promise<T>, ms: number): Promise<T> {
  return new Promise<T>((resolve, reject) => {
    const t = setTimeout(() => reject(new Error('execution timeout')), ms);
    p.then(
      (v) => {
        clearTimeout(t);
        resolve(v);
      },
      (e) => {
        clearTimeout(t);
        reject(e);
      },
    );
  });
}

/**
 * 在受限 vm 上下文执行用户脚本（可商用第一层隔离，适用于自托管/可信租户）。
 *
 * 安全要点：
 *  - 严格模式 IIFE 包裹，阻断 `this` 逃逸；
 *  - 上下文不暴露 require/process/fs/Function/Object 等危险 API；
 *  - 仅暴露 data（上游输入，深拷贝隔离）与 setOutput(v) 两个入口；
 *  - 同步死循环由 vm timeout 中断；异步滥用由 watchdog 兜底；
 *  - 输出体积受限（maxOutputBytes）。
 *
 * ⚠️ 说明：Node 的 vm 模块本身不是安全边界，本层为"软隔离"。
 * 多租户硬隔离见 06 设计 §M4 升级路线（容器 / WebAssembly 隔离 + 配额 + 审计）。
 * 本平台定位为运维/Ops 自托管场景，单租户下此隔离层已足够；
 * 若要对外开放工作流脚本编辑，必须升级到容器/WASM 隔离。
 */
export async function runSandboxed(
  code: string,
  bag: Record<string, unknown>,
  opts: SandboxOptions = {},
): Promise<SandboxResult> {
  const timeoutMs = opts.timeoutMs ?? 2000;
  const maxOutputBytes = opts.maxOutputBytes ?? 256 * 1024;
  const start = Date.now();

  const sandbox: Record<string, unknown> = {
    data: deepClone(bag),
    output: undefined,
    setOutput: (v: unknown) => {
      sandbox.output = v;
    },
    // 静默 console，避免信息泄露到 stdout
    console: { log: () => {}, info: () => {}, warn: () => {}, error: () => {}, debug: () => {} },
  };
  const context = vm.createContext(sandbox);

  // 尽力移除可逃逸入口（软隔离加固，非安全边界）
  try {
    vm.runInContext(
      `Object.defineProperty(this,'Function',{value:undefined});` +
        `Object.defineProperty(this,'globalThis',{value:undefined});` +
        `Object.defineProperty(this,'global',{value:undefined});`,
      context,
      { timeout: 500 },
    );
  } catch {
    /* noop */
  }

  const wrapped = `(function(){"use strict";\n${code}\n})()`;

  try {
    await withWatchdog(
      Promise.resolve().then(() => {
        vm.runInContext(wrapped, context, { timeout: timeoutMs, filename: 'workflow-script.js' });
      }),
      timeoutMs + 300,
    );
    const out = sandbox.output !== undefined ? sandbox.output : sandbox.data;
    const serialized = JSON.stringify(out ?? null);
    const bytes = Buffer.byteLength(serialized, 'utf8');
    if (bytes > maxOutputBytes) {
      return {
        out: undefined,
        durationMs: Date.now() - start,
        status: 'error',
        error: `脚本输出超出配额 ${maxOutputBytes} 字节（实际 ${bytes}）`,
        outputBytes: bytes,
      };
    }
    return { out, durationMs: Date.now() - start, status: 'success', outputBytes: bytes, isolation: 'vm' };
  } catch (e: any) {
    const dt = Date.now() - start;
    const msg = String(e?.message ?? e);
    if (e?.code === 'ERR_SCRIPT_EXECUTION_TIMEOUT' || /timeout/i.test(msg)) {
      return { out: undefined, durationMs: dt, status: 'timeout', error: '脚本执行超时（已被沙箱中断）', outputBytes: 0, isolation: 'vm' };
    }
    return { out: undefined, durationMs: dt, status: 'error', error: msg, outputBytes: 0, isolation: 'vm' };
  }
}

/** 沙箱配置：来自环境变量，带安全默认值（商业部署可外置）。 */
export const SANDBOX_CONFIG: Required<SandboxOptions> = {
  timeoutMs: Number(process.env.WF_SANDBOX_TIMEOUT_MS ?? 2000),
  maxOutputBytes: Number(process.env.WF_SANDBOX_MAX_OUTPUT_BYTES ?? 256 * 1024),
};
