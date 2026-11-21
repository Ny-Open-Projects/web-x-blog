import Docker from 'dockerode';
import { runSandboxed, SandboxResult, SandboxOptions, SANDBOX_CONFIG, sha256 } from './sandbox';

/**
 * M8：容器级硬隔离执行器。
 *
 * 与 vm 软隔离的本质区别：不可信脚本在**独立的一次性容器**内运行，
 * 与 Node 主进程内核/PID/网络/文件系统隔离。即使脚本逃逸出 JS 运行时，
 * 也只能触及这个被剥夺一切能力（CapDrop ALL / no-new-privileges / 非 root /
 * 只读根 / 禁网 / 内存+CPU+PID 限额）且“用完即焚”的容器。
 *
 * 商业场景（多租户、对外开放脚本编辑）必须开启本模式。
 * 容器不可用（无 Docker / 镜像缺失 / 权限不足）时按配置回退到 vm 软隔离，
 * 并在结果的 isolation 与 fallbackReason 中如实标注，绝不假装硬隔离。
 */

export type SandboxMode = 'vm' | 'container';

export interface HardSandboxConfig {
  /** 运行模式：vm=软隔离；container=容器硬隔离（失败自动回退 vm）。 */
  mode: SandboxMode;
  /** 脚本执行容器镜像（需本地已有或可拉取）。 */
  image: string;
  /** 容器内存上限（字节）。 */
  memoryBytes: number;
  /** CPU 配额（NanoCpus，1e9 = 1 核）。 */
  nanoCpus: number;
  /** 容器进程数上限（防 fork 炸弹）。 */
  pidsLimit: number;
  /** Docker socket 路径（Windows 走命名管道，Linux/macOS 走 unix socket）。 */
  socketPath?: string;
}

export const HARD_SANDBOX_CONFIG: HardSandboxConfig = {
  mode: (process.env.WF_SANDBOX_MODE as SandboxMode) || 'vm',
  image: process.env.WF_SANDBOX_IMAGE || 'node:20-alpine',
  memoryBytes: Number(process.env.WF_SANDBOX_MEMORY_BYTES || 128 * 1024 * 1024),
  nanoCpus: Number(process.env.WF_SANDBOX_NANO_CPUS || 500_000_000), // 0.5 核
  pidsLimit: Number(process.env.WF_SANDBOX_PIDS_LIMIT || 64),
  socketPath: process.env.WF_DOCKER_SOCKET || undefined,
};

/** 容器内 runner：从环境变量读取 base64 载荷，执行后把结果写到 stdout。
 *
 * 纵深防御两层：
 *  1) **容器层（硬边界）**：非 root / 只读根 / 禁网 / 无挂载 / 资源限额 —— 逃逸出 JS 也只能困在这个容器里。
 *  2) **JS 层（软边界）**：用户脚本在受限 vm 上下文中执行，拿不到 require/process/fs，
 *     与 vm 隔离模式语义一致，避免在容器内直接暴露 Node 能力。
 *  runner 自身作用域做容器安全属性自检 probe（非 root / 只读根 / 禁网），与用户脚本隔离。 */
const RUNNER = `
const payload = JSON.parse(Buffer.from(process.env.LC_PAYLOAD || '', 'base64').toString('utf8'));
const code = payload.code, bag = payload.bag, maxBytes = payload.maxOutputBytes, codeTimeout = payload.timeoutMs;
let output;
const setOutput = (v) => { output = v; };
let probe = {};
try {
  const os = require('os');
  probe.netIfaces = Object.keys(os.networkInterfaces() || {}).sort();
  probe.uid = (typeof process.getuid === 'function') ? process.getuid() : null;
  try { require('fs').writeFileSync('/etc/lowcode_probe.txt', 'x'); probe.fsWrite = 'WROTE'; }
  catch (e) { probe.fsWrite = 'ERR:' + (e.code || e.message); }
  try { require('fs').writeFileSync('/tmp/lowcode_probe.txt', 'x'); probe.tmpWrite = 'WROTE'; }
  catch (e) { probe.tmpWrite = 'ERR:' + (e.code || e.message); }
} catch (e) { probe.err = String((e && e.message) || e); }
try {
  const vm = require('vm');
  const sandbox = {
    data: bag,
    setOutput: setOutput,
    console: { log: function(){}, info: function(){}, warn: function(){}, error: function(){}, debug: function(){} },
  };
  const context = vm.createContext(sandbox);
  vm.runInContext('"use strict";\\n' + code, context, { timeout: codeTimeout, filename: 'workflow-script.js' });
  const out = output === undefined ? bag : output;
  const bytes = Buffer.byteLength(JSON.stringify(out ?? null), 'utf8');
  if (bytes > maxBytes) {
    process.stdout.write('__LC_RESULT__' + JSON.stringify({ status: 'error', error: '脚本输出超出配额 ' + maxBytes + ' 字节（实际 ' + bytes + '）', outputBytes: bytes, probe: probe }));
  } else {
    process.stdout.write('__LC_RESULT__' + JSON.stringify({ status: 'success', out: out, probe: probe }));
  }
} catch (e) {
  const msg = String((e && e.message) || e);
  const isTimeout = /timeout|Script execution timed out/i.test(msg);
  process.stdout.write('__LC_RESULT__' + JSON.stringify({ status: isTimeout ? 'timeout' : 'error', error: msg, probe: probe }));
}
`;

function defaultSocket(): string {
  if (HARD_SANDBOX_CONFIG.socketPath) return HARD_SANDBOX_CONFIG.socketPath;
  return process.platform === 'win32' ? '//./pipe/docker_engine' : '/var/run/docker.sock';
}

/**
 * 在一次性容器里执行脚本。任何基础设施错误（Docker 不可用/镜像缺失/权限不足）
 * 都会 throw，由 executeWithFallback 决定是否回退，不在这里吞掉。
 */
async function runInContainer(
  code: string,
  bag: Record<string, unknown>,
  opts: SandboxOptions,
  image: string,
): Promise<HardSandboxResult> {
  const timeoutMs = opts.timeoutMs ?? SANDBOX_CONFIG.timeoutMs;
  const maxOutputBytes = opts.maxOutputBytes ?? SANDBOX_CONFIG.maxOutputBytes;
  const start = Date.now();

  const docker = new Docker({ socketPath: defaultSocket() });
  const payload = Buffer.from(
    JSON.stringify({
      code,
      bag,
      maxOutputBytes,
      // 容器内 JS 层的超时（略小于宿主 kill 阈值，由宿主兜底强杀）
      timeoutMs: Math.max(50, timeoutMs - 200),
    }),
    'utf8',
  ).toString('base64');

  let container: Docker.Container;
  try {
    container = await docker.createContainer({
      Image: image,
      Cmd: ['node', '-e', RUNNER],
      Env: [`LC_PAYLOAD=${payload}`],
      User: '10001:10001', // 非 root（顶层字段）
      // 顶层禁网（不挂入默认 bridge）
      NetworkDisabled: true,
      HostConfig: {
        AutoRemove: true, // 用完即焚，退出即删
        Memory: HARD_SANDBOX_CONFIG.memoryBytes,
        MemorySwap: HARD_SANDBOX_CONFIG.memoryBytes, // 禁用 swap，防 OOM 拖垮宿主
        NanoCpus: HARD_SANDBOX_CONFIG.nanoCpus,
        PidsLimit: HARD_SANDBOX_CONFIG.pidsLimit,
        CapDrop: ['ALL'], // 剥夺全部 Linux capability
        SecurityOpt: ['no-new-privileges:true'],
        ReadonlyRootfs: true, // 根文件系统只读
        Tmpfs: { '/tmp': 'rw,noexec,nosuid,size=1m' },
      },
    } as any) as Docker.Container;
  } catch (e: any) {
    throw new Error(`容器创建失败（请确认 Docker 已启动且镜像 ${image} 可用）: ${e?.message ?? e}`);
  }

  // 超时强杀：无论容器内外是否卡死，宿主侧到点 kill。
  let timedOut = false;
  const killer = setTimeout(() => {
    timedOut = true;
    container.kill().catch(() => {});
  }, timeoutMs + 200);

  try {
    const stream = await container.attach({ stream: true, stdout: true, stderr: true });
    await container.start();

    const stdoutChunks: Buffer[] = [];
    const stderrChunks: Buffer[] = [];
    await new Promise<void>((resolve, reject) => {
      docker.modem.demuxStream(stream as NodeJS.ReadableStream, {
        write: (c: Buffer) => { stdoutChunks.push(Buffer.from(c)); return true; },
      } as any, {
        write: (c: Buffer) => { stderrChunks.push(Buffer.from(c)); return true; },
      } as any);
      (stream as any).on('end', resolve);
      (stream as any).on('error', reject);
      container.wait().then(() => resolve()).catch(reject);
    });

    clearTimeout(killer);
    if (timedOut) {
      return { out: undefined, durationMs: Date.now() - start, status: 'timeout', error: '容器脚本执行超时（宿主已强杀容器）', outputBytes: 0, isolation: 'container' };
    }

    const stdout = Buffer.concat(stdoutChunks).toString('utf8');
    const marker = '__LC_RESULT__';
    const idx = stdout.indexOf(marker);
    if (idx < 0) {
      const stderr = Buffer.concat(stderrChunks).toString('utf8').slice(0, 500);
      return {
        out: undefined,
        durationMs: Date.now() - start,
        status: 'error',
        error: `容器未返回结果${stderr ? ': ' + stderr : ''}`,
        outputBytes: 0,
        isolation: 'container',
      };
    }
    const parsed = JSON.parse(stdout.slice(idx + marker.length));
    return {
      out: parsed.out,
      durationMs: Date.now() - start,
      status: parsed.status,
      error: parsed.error,
      outputBytes: parsed.outputBytes ?? Buffer.byteLength(JSON.stringify(parsed.out ?? null), 'utf8'),
      isolation: 'container',
      probe: parsed.probe,
    };
  } finally {
    clearTimeout(killer);
    // 兜底清理：AutoRemove 正常会删；异常路径强制删除一次。
    container.remove({ force: true }).catch(() => {});
  }
}

export interface HardSandboxResult extends SandboxResult {
  fallbackReason?: string;
  /** 容器安全属性自检结果（uid / 只读根 / 网络接口），仅 container 模式有值。 */
  probe?: {
    netIfaces?: string[];
    uid?: number | null;
    fsWrite?: string;
    tmpWrite?: string;
    err?: string;
  };
}

/**
 * 统一入口：按配置选择隔离层；container 模式失败时自动回退 vm，并如实标注。
 */
export async function executeWithFallback(
  code: string,
  bag: Record<string, unknown>,
  opts: SandboxOptions = {},
  modeOverride?: SandboxMode,
  imageOverride?: string,
): Promise<HardSandboxResult> {
  const mode = modeOverride ?? HARD_SANDBOX_CONFIG.mode;
  if (mode === 'vm') {
    return runSandboxed(code, bag, opts);
  }
  const image = imageOverride ?? HARD_SANDBOX_CONFIG.image;
  try {
    return await runInContainer(code, bag, opts, image);
  } catch (e: any) {
    const reason = `容器隔离不可用（镜像 ${image}），已回退 vm 软隔离: ${e?.message ?? e}`;
    const r = await runSandboxed(code, bag, opts);
    return { ...r, fallbackReason: reason };
  }
}

/** 启动期自检：container 模式下探测 Docker 是否可用（不阻塞启动）。 */
export async function probeDocker(): Promise<{ ok: boolean; detail: string }> {
  try {
    const docker = new Docker({ socketPath: defaultSocket() });
    const info = await docker.info();
    return { ok: true, detail: `Docker 可用（${info.ServerVersion ?? 'unknown'}），镜像=${HARD_SANDBOX_CONFIG.image}` };
  } catch (e: any) {
    return { ok: false, detail: `Docker 不可用: ${e?.message ?? e}` };
  }
}

export { sha256 };
