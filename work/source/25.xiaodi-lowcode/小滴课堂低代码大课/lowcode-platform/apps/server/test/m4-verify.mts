/**
 * M4 沙箱隔离 验证脚本（不依赖 MySQL / 网络）。
 * 运行：node --experimental-strip-types apps/server/test/m4-verify.mts
 */
import { runSandboxed, SANDBOX_CONFIG } from '../src/modules/workflow/nodes/sandbox.ts';
import { createLlmProvider, MockLlmProvider } from '../src/modules/workflow/nodes/llm.ts';

let pass = 0;
let fail = 0;
function check(name: string, cond: boolean, extra = '') {
  if (cond) {
    pass++;
    console.log(`  ✅ ${name} ${extra}`);
  } else {
    fail++;
    console.log(`  ❌ ${name} ${extra}`);
  }
}

async function main() {
  console.log('== M4 沙箱隔离验证 ==');
  console.log('默认沙箱配置:', JSON.stringify(SANDBOX_CONFIG));

  // 1. 正常脚本：读取 data，产出 output
  {
    const r = await runSandboxed('setOutput({ status: "ok", n: data.n * 2 })', { n: 21 });
    check('正常脚本执行成功', r.status === 'success', `-> ${JSON.stringify(r.out)}`);
    check('输出数据正确', JSON.stringify(r.out) === JSON.stringify({ status: 'ok', n: 42 }));
  }

  // 2. 输入隔离：脚本内改 data 不影响原始 bag
  {
    const bag = { secret: 'x' };
    await runSandboxed('data.secret = "modified"; setOutput(data)', bag);
    check('输入对象被深拷贝隔离', (bag as any).secret === 'x');
  }

  // 3. 危险 API 不可达：process / require 未定义 -> 被捕获为 error，引擎不崩
  {
    const r = await runSandboxed('setOutput(process.pid)', {});
    check('危险 API(process)不可达', r.status === 'error', `-> ${r.error}`);
  }

  // 4. 同步死循环：被 vm timeout 中断（status=timeout）
  {
    const r = await runSandboxed('while(true){}', {});
    check('同步死循环被超时中断', r.status === 'timeout', `(${r.durationMs}ms)`);
  }

  // 5. 输出配额：超出 maxOutputBytes 视为 error
  {
    const r = await runSandboxed('setOutput("x".repeat(10000))', {}, { maxOutputBytes: 100 });
    check('输出超配额被拦截', r.status === 'error', `-> ${r.error}`);
  }

  // 6. LLM mock：不连网即可产出
  {
    const p = createLlmProvider();
    check('默认 LLM 为 mock provider', p.name === 'mock');
    const r = await p.complete([{ role: 'user', content: '你好' }]);
    check('mock LLM 返回文本', typeof r.text === 'string' && r.text.length > 0, `-> ${r.text}`);
  }

  console.log(`\n结果：${pass} 通过 / ${fail} 失败`);
  if (fail > 0) process.exit(1);
}

main().catch((e) => {
  console.error('验证脚本异常:', e);
  process.exit(1);
});
