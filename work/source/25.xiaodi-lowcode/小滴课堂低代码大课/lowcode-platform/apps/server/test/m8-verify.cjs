/**
 * M8 硬隔离验证（连真实 Docker，基于 nest build 产物）。
 * 运行：node apps/server/test/m8-verify.cjs
 *
 * 覆盖：
 *  - vm 模式回归（行为与 M4 一致，不被 M8 破坏）
 *  - container 硬隔离：正常执行 / 死循环强杀 / 禁网 / 非 root 只读
 *  - 回退语义：镜像缺失时自动回退 vm 并如实标注 fallbackReason（业务不中断）
 */
const path = require('path');
const base = path.resolve(__dirname, '../dist/modules/workflow/nodes');
const { executeWithFallback, probeDocker, HARD_SANDBOX_CONFIG } = require(
  path.join(base, 'container-sandbox.js'),
);

let ok = 0;
let bad = 0;
const assert = (name, cond, extra = '') => {
  cond ? (ok++, console.log('  ✅', name, extra)) : (bad++, console.log('  ❌', name, extra));
};

(async () => {
  console.log('=== 0. Docker 探测 ===');
  const probe = await probeDocker();
  console.log('  ', probe.detail);

  console.log('\n=== 1. vm 模式回归（M4 行为不被破坏）===');
  {
    const r = await executeWithFallback('setOutput({ v: data.a * 2 })', { a: 21 }, { timeoutMs: 2000 }, 'vm');
    assert('vm 正常脚本', r.status === 'success' && r.out && r.out.v === 42, JSON.stringify(r.out));
    assert('vm 标记隔离层', r.isolation === 'vm', `isolation=${r.isolation}`);

    const t = await executeWithFallback('while(true){}', {}, { timeoutMs: 500 }, 'vm');
    assert('vm 死循环超时', t.status === 'timeout', `status=${t.status}`);
  }

  if (probe.ok) {
    console.log(`\n=== 2. container 硬隔离（镜像 ${HARD_SANDBOX_CONFIG.image}）===`);
    {
      const r = await executeWithFallback(
        'setOutput({ v: data.a * 3, s: (1+2) })',
        { a: 14 },
        { timeoutMs: 8000 },
        'container',
      );
      assert('容器内正常执行', r.status === 'success', `status=${r.status} err=${r.error || ''}`);
      assert('容器结果正确', r.out && r.out.v === 42 && r.out.s === 3, JSON.stringify(r.out));
      assert('隔离层标记为 container', r.isolation === 'container', `isolation=${r.isolation}`);
      assert('无回退', !r.fallbackReason, r.fallbackReason || '');
    }

    {
      const t = await executeWithFallback('while(true){}', {}, { timeoutMs: 1500 }, 'container');
      assert('容器死循环被中断', t.status === 'timeout', `status=${t.status} err=${t.error || ''}`);
      assert('确为容器层隔离执行（非 vm 回退）', t.isolation === 'container', `isolation=${t.isolation}`);
    }

    {
      // 容器安全属性自检：非 root / 只读根 / 禁网 / 用户脚本拿不到 require
      const r = await executeWithFallback(
        "let req='AVAILABLE'; try { req = typeof require; } catch(e) { req='THREW'; } setOutput({ req });",
        {},
        { timeoutMs: 8000 },
        'container',
      );
      assert('容器内脚本执行并回传', r.status === 'success', `status=${r.status} err=${r.error || ''}`);
      const out = r.out || {};
      const probe = r.probe || {};
      assert('用户脚本拿不到 require（容器内也无法读写文件/联网）', out.req === 'undefined', `require=${out.req}`);
      assert('容器内以非 root 运行', typeof probe.uid === 'number' && probe.uid !== 0, `uid=${probe.uid}`);
      assert('根文件系统只读（写 /etc 失败）', String(probe.fsWrite || '').startsWith('ERR:'), `fsWrite=${probe.fsWrite}`);
      assert('/tmp 可写（tmpfs 生效）', probe.tmpWrite === 'WROTE', `tmpWrite=${probe.tmpWrite}`);
      assert(
        '网络被禁用（无 eth0 等外部网卡）',
        Array.isArray(probe.netIfaces) && probe.netIfaces.every((i) => i === 'lo'),
        `netIfaces=${JSON.stringify(probe.netIfaces)}`,
      );
    }
  } else {
    console.log('\n=== 2. container 硬隔离：跳过（Docker 不可用）===');
  }

  console.log('\n=== 3. 回退语义（镜像缺失 → 回退 vm 并标注）===');
  {
    const r = await executeWithFallback(
      'setOutput({ ok: true })',
      {},
      { timeoutMs: 3000 },
      'container',
      'lowcode-no-such-image:never', // 故意用不存在的镜像触发基础设施失败
    );
    assert('容器不可用时不抛异常（业务不中断）', r.status === 'success', `status=${r.status}`);
    assert('已回退到 vm', r.isolation === 'vm', `isolation=${r.isolation}`);
    assert('标注回退原因（不假装硬隔离）', !!r.fallbackReason, r.fallbackReason || '');
  }

  console.log(`\n===== M8 结果：${ok} 通过 / ${bad} 失败 =====`);
  process.exit(bad ? 1 : 0);
})().catch((e) => {
  console.error('测试异常:', e);
  process.exit(1);
});
