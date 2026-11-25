---
title: 01 异步与 Promise 体系 · 手写题专题
date: 2026-11-24
categories: [前端手写]
tags: [前端面试, 笔试题, HW, 异步]
type: 笔试题
---

# 01 异步与 Promise 体系

> 异步手写题是面试区分度最高的一块：**写对只说明你会用，写全边界才说明你用过**。能力分层：L1 能写对 → L2 能写全边界 → L3 能讲清「为什么这样设计」。这一块所有题都围绕同一组底层概念——状态机、微任务时序、并发槽位、取消语义。把这四个词讲透，20 多道题其实是同一道题的不同外壳。

## 能力分层

| 层级 | 题目 | 面试要求 |
|---|---|---|
| L1 必会 | Promise.all / race / allSettled / any / promisify / 带超时请求 | 5 分钟内写对，能主动说空数组与保序 |
| L2 进阶 | Promise 核心 then 链 / p-limit / 指数退避 retry / async 执行器 / 顺序执行器 | 15 分钟内写对，边界能边说边补 |
| L3 深水 | 可取消 Promise / 优先级任务队列 / 并发分组合流 / SWR 缓存 / 令牌桶 | 讲清设计取舍、替代方案与失效场景 |

判断自己是否真的会：给你一张白纸，5 分钟内写出 `Promise.all` 并同时说出「空数组 / 非 Promise 值 / 保序 / fail-fast 不取消底层请求」四个点，才算 L1 过关；能被追问三个「那如果……」而不卡壳，才算 L2；能主动对比原生实现与业界库的差异，才算 L3。

## 本专题原卡全景

| 编号 | 题目 | 层级 | 关键考点 |
|---|---|---|---|
| [HW-001](../06-算法与手写/HW-001-手写-Promise-核心-then-链.md) | 手写 Promise 核心（then 链） | L2 | 状态机、thenable 吸收、值穿透 |
| [HW-002](../06-算法与手写/HW-002-手写-Promiseall.md) | 手写 Promise.all | L1 | 保序赋值、计数器、fail-fast |
| [HW-003](../06-算法与手写/HW-003-手写-Promiserace.md) | 手写 Promise.race | L1 | 首个落定、空数组永远 pending |
| [HW-004](../06-算法与手写/HW-004-手写-PromiseallSettled.md) | 手写 Promise.allSettled | L1 | 不 fail-fast、value/reason 字段 |
| [HW-005](../06-算法与手写/HW-005-手写-Promiseany.md) | 手写 Promise.any | L1 | 首个成功、AggregateError 保序 |
| [HW-006](../06-算法与手写/HW-006-手写-async-执行器-Generator-自.md) | async 执行器（Generator 自动执行） | L2 | next/throw 注入、递归驱动 |
| [HW-007](../06-算法与手写/HW-007-手写-plimit-并发控制.md) | p-limit 并发控制 | L2 | 槽位 + 等待队列、finally 释放 |
| [HW-008](../06-算法与手写/HW-008-手写-retry-重试.md) | retry 重试 | L1 | 重新调用 fn、抛最后错误 |
| [HW-009](../06-算法与手写/HW-009-手写-promisify.md) | promisify | L1 | err-first 回调、this 透传 |
| [HW-010](../06-算法与手写/HW-010-手写带超时的请求包装.md) | 带超时的请求包装 | L1 | race + clearTimeout + 真取消 |
| [HW-049](../06-算法与手写/HW-049-手写-Promise-超时取消.md) | Promise 超时取消 | L2 | cancel 主动 reject、结果不回写 |
| [HW-061](../06-算法与手写/HW-061-手写-Promise-取消与中断.md) | 可取消 Promise（CancelToken） | L3 | 哨兵值、卸载后回调不执行 |
| [HW-062](../06-算法与手写/HW-062-手写-Promise-withResolvers-与-deferred.md) | deferred / withResolvers | L1 | 结算权外移、回调转 Promise |
| [HW-063](../06-算法与手写/HW-063-手写-Promise-重试带指数退避.md) | 指数退避重试 | L2 | 退避系数、抖动、条件重试 |
| [HW-064](../06-算法与手写/HW-064-手写-令牌桶限流器.md) | 令牌桶限流器 | L3 | 惰性补桶、突发容量、排队 |
| [HW-065](../06-算法与手写/HW-065-手写-并发分组合流器.md) | 并发分组合流器 | L2 | 单项失败不阻塞、整体超时 |
| [HW-066](../06-算法与手写/HW-066-手写-优先级任务队列.md) | 优先级任务队列 | L3 | 分桶取最高优先级、key 去重 |
| [HW-085](../06-算法与手写/HW-085-手写-Promise-顺序链执行器.md) | Promise 顺序执行器 | L2 | 失败策略、进度回调 |
| [HW-086](../06-算法与手写/HW-086-手写-async-队列Worker-常驻.md) | 常驻异步 Worker 队列 | L3 | 单消费循环、背压、优雅关闭 |
| [HW-087](../06-算法与手写/HW-087-手写-带缓存的异步函数.md) | 带缓存的异步函数（SWR） | L3 | 在途去重、旧值优先、错误不缓存 |
| [HW-161](../06-算法与手写/HW-161-手写-防抖的-AbortSignal-集成.md) | 防抖的 AbortSignal 集成 | L2 | 定时器与取消信号统一 |

## 精讲（6 题）

### 精讲 1 · [HW-001] 手写 Promise 核心（then 链）

**为什么考这个**：这是唯一一道能同时验证「状态机思维」「微任务时序」「错误传播」三件事的题。很多人背得下 then 链，却答不出「为什么回调必须异步」——而这道题的所有坑都长在这个问题上。

**标准实现**：

```javascript
class MyPromise {
  constructor(executor) {
    this.state = 'pending';        // pending → fulfilled / rejected，单向不可逆
    this.value = undefined;
    this.callbacks = [];           // pending 期间注册的回调先存着

    const settle = (state, value) => {
      if (this.state !== 'pending') return;             // 第二次 resolve 无效
      // thenable 吸收：resolve 一个 Promise 要等它落定，而不是把 Promise 当值
      if (state === 'fulfilled' && value && typeof value.then === 'function') {
        value.then(v => settle('fulfilled', v), e => settle('rejected', e));
        return;
      }
      this.state = state;
      this.value = value;
      const cbs = this.callbacks;
      this.callbacks = [];                              // 先清空再遍历，防止回调里再注册
      cbs.forEach(cb => queueMicrotask(cb));
    };
    const resolve = v => settle('fulfilled', v);
    const reject = e => settle('rejected', e);
    try { executor(resolve, reject); } catch (e) { reject(e); }   // 同步抛错也转 reject
  }

  then(onFulfilled, onRejected) {
    return new MyPromise((resolve, reject) => {         // 每次 then 都产新 Promise
      const run = () => {
        const handler = this.state === 'fulfilled' ? onFulfilled : onRejected;
        if (typeof handler !== 'function') {            // 值穿透 / 异常穿透
          return this.state === 'fulfilled' ? resolve(this.value) : reject(this.value);
        }
        try {
          resolve(handler(this.value));                 // 返回值可能是 Promise，交给 settle 递归吸收
        } catch (e) {
          reject(e);                                    // 回调抛错 → 沿链向下传
        }
      };
      if (this.state === 'pending') this.callbacks.push(run);
      else queueMicrotask(run);                         // 已落定也异步，保证执行顺序一致
    });
  }

  catch(onRejected) { return this.then(undefined, onRejected); }

  finally(onFinally) {
    return this.then(
      v => MyPromise.resolve(onFinally()).then(() => v),          // 不改变值
      e => MyPromise.resolve(onFinally()).then(() => { throw e; })// 不吞异常
    );
  }
  static resolve(v) { return v instanceof MyPromise ? v : new MyPromise(r => r(v)); }
  static reject(e) { return new MyPromise((_, j) => j(e)); }
}
```

**必须覆盖的边界**：

- **状态单向**：`settle` 开头判断 `state !== 'pending'`，否则第二次 resolve 会覆盖第一次。
- **then 返回新实例**：返回 `this` 就永远只有一条链，无法做值变换，也无法隔离错误。
- **回调异步**：必须 `queueMicrotask`（或 then 里包一层），否则「先 then 后 resolve」和「先 resolve 后 then」时序不一致。
- **pending 缓存**：注册时状态未定，回调要进队列，落定时统一 flush。
- **thenable 吸收**：`resolve(promise)` 不能把 Promise 当普通值存起来，否则 `.then(v => ...)` 拿到的是 Promise 本身。
- **回调抛错转 reject**：`try/catch` 包住 handler，这是错误能沿链传递的唯一途径。
- **值穿透**：`then()` 不传参时值要继续往下走，`catch` 正是靠这点实现的。
- **executor 同步抛错**：`throw` 在构造函数里等价于 `reject`。

**追问链**：

1. 为什么 Promise 回调一定异步？→ 规范要求（then 必须在当前执行栈清空后调用），这样「先注册 then 后 resolve」与「先 resolve 后注册 then」行为一致，避免 Zalgo（有时同步有时异步）。
2. `then` 里 `return` 一个 thenable 会怎样？→ 递归展开，直到拿到非 thenable 的终值；这也是 `.then(() => fetch(...))` 能自动等待的原因。
3. `then` 里返回自己（`p.then(() => p)`）？→ 原生抛 `TypeError: Chaining cycle detected`，因为会无限递归；手写版可加 `if (x === promise) reject(new TypeError(...))`。
4. 和 Promises/A+ 规范差在哪？→ 规范还要求：读取 `x.then` 只能读一次（防 getter 副作用）、getter 抛错要 reject、`onFulfilled` 必须只调用一次、必须用微任务。面试说得出「读一次 then」这一点就够亮眼。
5. `async/await` 和它的关系？→ `await x` 等价于 `Promise.resolve(x).then(...)`，把后续代码放进微任务；区别是 await 会暂停函数执行上下文，且 `try/catch` 能捕获同步与异步错误。

### 精讲 2 · [HW-002] 手写 Promise.all

**为什么考这个**：一句话——它同时考「并发发起」「结果保序」「失败短路」三件事。三者都写对，说明你真的理解「并发完成顺序 ≠ 结果顺序」，这是异步思维的分水岭。

**标准实现**：

```javascript
function promiseAll(iterable) {
  return new Promise((resolve, reject) => {
    // 1. 入参校验：规范要求可迭代（数组、Set、generator 都行）
    if (iterable == null || typeof iterable[Symbol.iterator] !== 'function') {
      throw new TypeError('argument must be iterable');
    }
    const list = Array.from(iterable);
    const len = list.length;
    if (len === 0) return resolve([]);          // 边界：空数组必须立即结算

    const results = new Array(len);             // 2. 预分配，按索引写，不用 push
    let settled = 0;

    list.forEach((item, i) => {
      Promise.resolve(item).then(v => {         // 3. 非 Promise 值统一包装
        results[i] = v;                         // 完成顺序无关，位置由 i 决定
        if (++settled === len) resolve(results);// 4. 计数器判全部完成
      }, reject);                               // 5. 任一失败立刻 reject
    });
  });
}
```

**必须覆盖的边界**：

- **空数组** → 立即 `resolve([])`。漏掉这一步 Promise 永远 pending，是最常见的"看起来对但跑不通"。
- **非 Promise 值** → `Promise.resolve()` 包装，否则 `.then` 直接报错；也顺带支持 thenable。
- **保序** → 必须 `results[i] = v`；`push` 得到的是完成顺序，慢请求会错位。
- **fail-fast** → 任一 reject 立即整体 reject，不必等其他任务；但要主动说明「**其他请求并没有被取消**，仍在后台跑完」——能说出这点是加分项。
- **计数器而非 `results.length`** → 稀疏数组下 `length` 不可靠，且并发写入 `length` 与完成数不等价。
- **可迭代而非仅数组** → `Array.from` 兼容 Set/Map keys/generator。
- **`throw` 与 `reject` 的区别** → executor 内同步 `throw` 等价于 reject，但更好读的是显式 reject。

**追问链**：

1. 「任一失败也要等其他完成」怎么写？→ `allSettled`：每个任务映射成 `{status, value|reason}`，永不 reject。
2. 「只要最快的成功」呢？→ `any`：每个任务失败时计数，全部失败才 reject `AggregateError`（注意 errors 按索引保序，不是失败顺序）。
3. 「最快的落定，不管成败」？→ `race`：`then(resolve, reject)` 直接挂到同一个出口，先到先得；空数组永远 pending，这是反向考点。
4. 100 个请求限并发 5 个？→ `p-limit`，核心是「完成一个补一个」而不是分批（分批有木桶等待：5 个里 4 个秒回，第 6 个仍要等最慢那个）。
5. 为什么不用 `reduce` 串起来写？→ 那是串行，失去并发意义；`reduce((acc, p) => acc.then(() => p))` 只在「必须按顺序执行」时使用（如依赖前一步结果）。

### 精讲 3 · [HW-007] 手写 p-limit 并发控制

**为什么考这个**：这是「Promise 语法题」和「工程题」的分界线。业务里一次上传 200 张图、一次拉 50 个详情接口，浏览器会把连接池打满、首屏被拖死。面试官想看的不是你会不会写计数，而是你知不知道「为什么是完成一个补一个」。

**标准实现**：

```javascript
function pLimit(concurrency) {
  if (!Number.isInteger(concurrency) || concurrency < 1) {
    throw new RangeError('concurrency must be a positive integer');
  }
  let active = 0;          // 当前执行中的任务数
  const queue = [];        // 等待队列：{ fn, resolve, reject }

  const next = () => {
    if (active >= concurrency || queue.length === 0) return;
    const { fn, resolve, reject } = queue.shift();
    active++;
    // 用 Promise.resolve().then(fn) 包一层：fn 同步 throw 也能进入 reject 分支
    Promise.resolve().then(fn).then(resolve, reject)
      .finally(() => {
        active--;
        next();            // 完成一个立刻补一个，不等整批
      });
  };

  return function limit(fn) {
    // 返回的 Promise 与这个任务一一对应，resolve/reject 不能串台
    return new Promise((resolve, reject) => {
      queue.push({ fn, resolve, reject });
      next();
    });
  };
}

// 用法：200 张图，最多同时传 5 张
const limit = pLimit(5);
const uploadAll = files => Promise.all(files.map(f => limit(() => upload(f))));
```

**必须覆盖的边界**：

- **并发数校验** → 0 或负数会让 `next` 永远不执行，整个队列静默卡死；非整数（2.5）语义模糊，直接拒。
- **调度必须在 `finally`** → 放在 `.then` 里，任务 reject 后槽位永不释放，池子会越跑越窄直到死锁。
- **任务同步抛错** → `fn()` 直接抛不会经过 Promise 链，`Promise.resolve().then(fn)` 才能统一成 reject。
- **Promise 对号入座** → `resolve/reject` 与具体任务绑定，不能共用一个全局回调。
- **结果顺序** → `p-limit` 本身不保证结果顺序，只是调用顺序入队；需要保序请在外面配 `Promise.all`（它天然按索引）。
- **空队列** → `next` 里的 `queue.length === 0` 提前返回，避免 `shift()` 出 `undefined` 再解构报错。

**追问链**：

1. 为什么不用「每 5 个一组 `chunk` + `Promise.all`」？→ 分批有木桶效应：一批里最慢的决定下一批开始时间，整体耗时接近 `ceil(n/k) × max`；「完成即补位」接近 `n/k × avg`，吞吐更高。
2. 怎么支持运行中动态改并发？→ 把 `concurrency` 换成 getter 或 `setConcurrency(n)`，改完调一次 `next()`（调大要主动补位，调小靠自然收缩）。
3. 怎么中途取消整个池？→ 传 `AbortSignal`，`next()` 开头判 `signal.aborted` 就不再出队，队列里所有任务的 Promise 统一 reject `AbortError`，已发出的请求靠各自的 `fetch(url, { signal })` 真中断。
4. 和 `Promise.all` 的关系？→ `p-limit` 管「同时跑几个」，`all` 管「什么时候都结束」；两者组合才是生产写法。
5. 浏览器到底限几个并发？→ HTTP/1.1 同域 6 个左右，HTTP/2 多路复用后限制放宽但服务端仍有 QPS 限制；所以前端限并发更多是为了「别把首屏带宽抢光」，属于产品体验决策。

### 精讲 4 · [HW-063] 手写指数退避重试（退避系数 + 抖动）

**为什么考这个**：重试是分布式系统的常识，但绝大多数人只会写 `for (let i = 0; i < 3; i++)`。加上「指数退避 + 抖动 + 条件重试」，考的就是你有没有真的在线上被重试风暴打过。

**标准实现**：

```javascript
const sleep = (ms, signal) => new Promise((resolve, reject) => {
  if (signal?.aborted) return reject(new DOMException('aborted', 'AbortError'));
  const timer = setTimeout(resolve, ms);
  // 睡眠期间被取消要立刻退出，否则 await 还要白等一个退避周期
  signal?.addEventListener('abort', () => {
    clearTimeout(timer);
    reject(new DOMException('aborted', 'AbortError'));
  }, { once: true });
});

async function retry(task, {
  retries = 3,          // 额外重试次数：总尝试 = retries + 1
  delay = 300,          // 首次退避基数
  factor = 2,           // 退避系数：delay * factor^attempt
  maxDelay = 8000,      // 单次退避上限，防止指数爆炸
  jitter = true,        // 抖动：打散重试时刻，防惊群
  shouldRetry = () => true,
  signal,
} = {}) {
  let lastError;
  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      return await task(attempt);            // 把尝试序号传出去，方便打日志/埋点
    } catch (err) {
      lastError = err;
      // 最后一次不再等待；不可重试错误（401/403/400）直接抛
      if (attempt === retries || !shouldRetry(err)) break;
      let wait = Math.min(delay * factor ** attempt, maxDelay);
      // 半抖动：保留一半固定值保证下限，另一半随机打散
      if (jitter) wait = wait / 2 + Math.random() * (wait / 2);
      await sleep(wait, signal);
    }
  }
  throw lastError;                           // 抛最后一次的真实错误，不是 undefined
}
```

**必须覆盖的边界**：

- **重试次数语义** → 先说清「`retries` 是额外次数」还是「总尝试次数」，否则 3 次到底是 3 还是 4 会吵架；代码里注释写死。
- **抛最后一次错误** → 常见 bug 是循环结束 `reject(undefined)`，排查时完全没线索。
- **每次重新调用 `task()`** → 绝不能缓存第一次的 Promise 反复 `await`（同一个已 reject 的 Promise 永远不会变成功）。
- **`maxDelay` 封顶** → `300 × 2^10 ≈ 5 分钟`，没有上限的重试等于挂死。
- **抖动** → 上千客户端同时断网恢复，固定退避会让它们在同一个毫秒齐刷刷重连，把服务打挂第二次。
- **条件重试** → 4xx 是客户端错误，重试无意义且可能触发风控；只对 429/5xx/网络错误重试。
- **取消** → 组件的 `AbortSignal` 要能中断「等待中的退避」，而不只是中断请求本身。

**追问链**：

1. 抖动有哪几种？→ Full jitter（`random(0, cap)`）、Equal jitter（`cap/2 + random(0, cap/2)`，即本例）、Decorrelated（`random(base, prev*3)`）；AWS 的结论是 full jitter 总重试次数最低，equal jitter 更平滑。
2. 重试和熔断什么关系？→ 重试是「单次调用层」的乐观策略，熔断是「服务层」的保护：连续失败达到阈值就快速失败一段时间，避免重试把雪崩放大。两者必须配合用。
3. 为什么说重试要求幂等？→ 请求可能已经到达服务端只是响应丢了，重试会重复扣款/重复下单；所以要么接口带幂等键（`Idempotency-Key`），要么只对 GET/查询类重试。
4. 怎么加总超时？→ 用 `Promise.race` 或 `AbortSignal.timeout(total)` 包住整个 `retry`，否则「3 次 × 8s 退避 + 每次 10s 请求」可能卡 50s。
5. 和 `retry`（HW-008）的区别？→ HW-008 是固定间隔的最小版，考点是「重新调用 + 抛最后错误」；这里多了退避、抖动、条件、取消，是工程版。

### 精讲 5 · [HW-061] 手写可取消的 Promise（CancelToken）

**为什么考这个**：Promise 规范里根本没有 cancel，这是语言设计上的著名遗憾。面试官问这题，本质是问：**「组件卸载了、路由切走了，你怎么让一个已经发出的请求不再影响 UI？」** 能答出「包装 + 哨兵 + 通知底层」三层结构，才是真的理解取消。

**标准实现**：

```javascript
class CancelToken {
  constructor() {
    this.canceled = false;
    this.reason = undefined;
    this.listeners = new Set();
  }
  // 注册取消回调，返回解绑函数（避免 listener 泄漏）
  onCancel(fn) {
    if (this.canceled) { fn(this.reason); return () => {}; }
    this.listeners.add(fn);
    return () => this.listeners.delete(fn);
  }
  cancel(reason = 'canceled') {
    if (this.canceled) return;          // 幂等：重复取消无副作用
    this.canceled = true;
    this.reason = reason;
    this.listeners.forEach(fn => fn(reason));
    this.listeners.clear();
  }
}

function withCancel(task, token) {
  return new Promise((resolve, reject) => {
    let settled = false;
    const finish = (fn, val) => { if (!settled) { settled = true; fn(val); } };

    // 取消信号 → 主动 reject，让 await 立刻退出，而不是等底层请求返回
    token.onCancel(reason =>
      finish(reject, new DOMException(String(reason), 'AbortError')));

    // 原任务照常执行，只是结果不再回写给调用方
    Promise.resolve().then(task).then(v => finish(resolve, v), e => finish(reject, e));
  });
}

// 用法：组件卸载 / 路由切换时取消
const token = new CancelToken();
onUnmounted(() => token.cancel('component unmounted'));
const data = await withCancel(() => fetch('/api/user').then(r => r.json()), token);
```

**必须覆盖的边界**：

- **取消后必须主动 reject** → 只在 then 里判断 `canceled` 不够：底层请求可能还要 10 秒才回来，这 10 秒里 `await` 一直挂着，组件早已卸载。
- **结果不能回写** → 用 `settled` 单次结算标记，取消后底层成功/失败都不再影响外部状态。
- **不能吞掉底层结果** → 包装器只控制「上层是否关心」，底层请求本身要照常结束（或主动 abort），否则连接和内存不会释放。
- **幂等** → `cancel()` 调两次不应触发两次 reject、不应重复遍历 listener。
- **错误类型可识别** → 统一用 `DOMException(..., 'AbortError')` 或带 `__CANCELED__` 标记的对象，调用方好区分「真失败」和「主动取消」，避免把取消当成错误上报。
- **listener 清理** → 每次包装都注册回调，不清理会随组件数量线性泄漏。

**追问链**：

1. 为什么 Promise 不能原生取消？→ 取消需要「多方协调」：一个 Promise 可能被多个消费者共享，取消会影响其他人；且已开始的副作用无法回滚。所以标准选择了 `AbortSignal` 这条「外部信号」路线。
2. `AbortController` 和 CancelToken 的区别？→ 前者是 WHATWG 标准，`signal` 可复用于 fetch/XHR/addEventListener/stream；后者是 axios 自造的（现已支持 signal）。新代码一律用 `AbortController`。
3. 怎么做到「真取消」而不只是「不关心」？→ 把 `signal` 透传给底层：`fetch(url, { signal })`、`xhr.abort()`、`reader.cancel()`。这才是释放连接。
4. `async/await` 里怎么取消？→ await 本身不可中断，只能让被 await 的 Promise reject（如本例）；或者在每个 await 之后检查 `signal.aborted` 提前 return。
5. 和 [HW-049] 超时取消怎么组合？→ `AbortSignal.timeout(ms)` 或「定时器内调 `controller.abort()`」，把「超时」变成「取消」的一种原因；这样超时和用户取消走同一条清理路径。

### 精讲 6 · [HW-066] 手写优先级任务队列（并发上限 + 优先级 + 去重）

**为什么考这个**：这题是 p-limit 的升维版，考的是「有限资源下的调度」。真实场景：埋点上报、图片预加载、首屏关键请求、后台数据同步同时在抢 6 个连接位——先发谁？能给出「分桶取最高优先级 + 同优先级 FIFO + key 去重」三件套，说明你写过调度器而不是玩具。

**标准实现**：

```javascript
class PriorityQueue {
  constructor(concurrency = 4) {
    this.limit = concurrency;
    this.active = 0;
    this.buckets = new Map();   // priority -> job[]，同优先级天然 FIFO
    this.keys = new Map();      // dedupeKey -> 已排队任务的 Promise
  }

  push(task, { priority = 0, dedupeKey } = {}) {
    // 去重：同一 key 的任务只排队一份，所有调用方共享同一个结果
    if (dedupeKey && this.keys.has(dedupeKey)) return this.keys.get(dedupeKey);

    const promise = new Promise((resolve, reject) => {
      const bucket = this.buckets.get(priority) || [];
      this.buckets.set(priority, bucket);
      bucket.push({ task, resolve, reject });
      this.#drain();                       // 有空槽就立刻尝试调度
    });

    if (dedupeKey) {
      this.keys.set(dedupeKey, promise);
      // 落定后释放 key，否则后续同名任务永远拿到旧结果
      promise.finally(() => this.keys.delete(dedupeKey)).catch(() => {});
    }
    return promise;
  }

  #pick() {
    let best = null;                       // 找当前优先级最高的非空桶
    for (const [priority, bucket] of this.buckets) {
      if (bucket.length === 0) continue;
      if (!best || priority > best.priority) best = { priority, bucket };
    }
    return best ? best.bucket.shift() : null;
  }

  #drain() {
    while (this.active < this.limit) {
      const job = this.#pick();
      if (!job) return;                    // 没活了，退出循环
      this.active++;
      Promise.resolve().then(job.task).then(job.resolve, job.reject)
        .finally(() => { this.active--; this.#drain(); });   // 完成即补位
    }
  }
}

// 用法：首屏关键请求 priority=10，埋点 priority=0
const q = new PriorityQueue(4);
q.push(() => fetch('/api/critical'), { priority: 10, dedupeKey: 'critical' });
q.push(() => beacon('/log'), { priority: 0 });
```

**必须覆盖的边界**：

- **同优先级 FIFO** → 用 `Map<priority, array>` 分桶 + `shift()`，天然满足；若用单一数组每次 `sort`，同优先级顺序会因排序稳定性与耗时抖动。
- **抢占的真实语义** → 队列里能抢占（挑优先级最高的出队），**已运行的任务不能抢占**（Promise 无法暂停）。说清这点，比吹「支持抢占」满分。
- **去重 key 的释放时机** → 必须在落定后删除，且在 `.finally` 上挂 `catch` 兜一层，否则会产生 unhandledRejection。
- **失败不影响队列** → `job.reject` 交给调用方，`finally` 依然释放槽位；去重场景下所有调用方都会收到同一个 reject。
- **空桶清理** → 桶空了可 `delete`，否则高优先级 key 会无限堆积（本例靠 `pick` 跳过，可再加删除）。
- **优先级数值方向** → 明确「数字越大越优先」，或改成小顶堆；面试时先说约定。
- **公平性 / 饥饿** → 持续涌入高优先级任务会让低优先级永远排不上，进阶要加「老化」（等待越久优先级越高）。

**追问链**：

1. 为什么用分桶而不是每次都排序？→ 分桶插入 O(1)、取最高只需遍历桶数（优先级种类通常个位数）；排序是 O(n log n) 且每次都排。优先级种类多时改用二叉堆 O(log n)。
2. 优先级反转 / 饥饿怎么解？→ 老化（aging）：记录入队时间，实际优先级 = 基础优先级 + 等待时长系数；或给每级设配额（如每执行 3 个高优必须放 1 个低优）。
3. 怎么和浏览器调度对齐？→ `scheduler.postTask(cb, { priority: 'user-blocking' | 'user-visible' | 'background' })` 是标准化的三档；自研队列通常映射到这三档（见 [HW-148]）。
4. 去重和缓存有什么区别？→ 去重只合并「同一时刻在途/排队」的请求，落定即释放；缓存保留结果一段时间（见 [HW-087]）。两者组合就是请求层标配：`dedupe + TTL cache`。
5. 怎么优雅关闭队列？→ `close()` 置标记拒绝新任务，等 `active === 0 && queue 空` 再 resolve；关闭过程中的排队任务要统一 reject 并让调用方感知（见 [HW-086]）。

## 其余 15 题速查

> 这 15 题不用背长实现，但每题都要能 30 秒说出「核心 3 行 + 1 个边界」。下面给的是可直接粘进控制台验证的最小版。

### [HW-003] Promise.race

```javascript
function promiseRace(iterable) {
  return new Promise((resolve, reject) => {
    for (const item of iterable) Promise.resolve(item).then(resolve, reject); // 首个落定生效
  });
}
```

考点：成败都走同一出口；空数组与原生一致**永远 pending**（这正是超时控制能奏效的前提）；非 Promise 值会被立刻兑现，所以 `race([1, slow])` 恒为 1。

### [HW-004] Promise.allSettled

```javascript
function promiseAllSettled(iterable) {
  const list = Array.from(iterable);
  return Promise.all(list.map(p => Promise.resolve(p).then(
    value => ({ status: 'fulfilled', value }),
    reason => ({ status: 'rejected', reason })
  )));
}
```

考点：永不 reject，适合「批量上报，失败也要统计」；字段名是 `value` / `reason`（不是 `data` / `error`），记错直接判为「背的」；天然保序。

### [HW-005] Promise.any

```javascript
function promiseAny(iterable) {
  return new Promise((resolve, reject) => {
    const list = Array.from(iterable);
    if (list.length === 0) return reject(new AggregateError([], 'All promises were rejected'));
    const errors = new Array(list.length);
    let failed = 0;
    list.forEach((p, i) => Promise.resolve(p).then(resolve, err => {
      errors[i] = err;                                    // 按索引收集，保序
      if (++failed === list.length) reject(new AggregateError(errors, 'All promises were rejected'));
    }));
  });
}
```

考点：首个成功即胜出，全败才 reject `AggregateError`；与 race 的区别一句话——**race 看谁先落定，any 看谁先成功**；CDN 多源兜底就是典型用法。

### [HW-006] async 执行器（Generator 自动执行）

```javascript
function run(genFn) {
  return new Promise((resolve, reject) => {
    const gen = genFn();
    const step = (method, arg) => {
      let ret;
      try { ret = gen[method](arg); } catch (e) { return reject(e); }  // generator 内部抛错
      if (ret.done) return resolve(ret.value);
      Promise.resolve(ret.value).then(
        v => step('next', v),          // 成功：值回填到 yield 表达式左侧
        e => step('throw', e)          // 失败：把异常抛进 generator，让 try/catch 接住
      );
    };
    step('next', undefined);
  });
}
```

考点：`next(v)` 与 `throw(e)` 是两个方向相反的注入口，缺一个就无法支持 `try/catch`；这就是 babel 编译 async 函数时 `_asyncToGenerator` 的原理；`done` 时 resolve 的是 `return` 值。

### [HW-008] retry（固定间隔最小版）

```javascript
function retry(fn, times = 3, delay = 200) {
  return new Promise((resolve, reject) => {
    const attempt = left => {
      Promise.resolve().then(fn).then(resolve, err => {
        if (left <= 0) return reject(err);            // 抛最后一次真实错误
        setTimeout(() => attempt(left - 1), delay);   // 每次都重新调用 fn
      });
    };
    attempt(times);                                   // 语义：times 为额外重试次数
  });
}
```

考点：**必须重新调用** `fn()`，不能复用已 reject 的 Promise；`times` 语义要口头约定；生产版见精讲 4（指数退避）。

### [HW-009] promisify

```javascript
function promisify(fn) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      let called = false;
      fn.call(this, ...args, (err, ...rest) => {
        if (called) return;                     // 有些库会多次回调，加 once 保护
        called = true;
        err ? reject(err) : resolve(rest.length > 1 ? rest : rest[0]);
      });
    });
  };
}
```

考点：Node err-first 约定 `(err, data)`；`fn.call(this, ...)` 保留 this；支持多返回值收集（`fs.read` 的 `(err, bytes, buffer)`）；`util.promisify.custom` 可自定义返回。

### [HW-010] 带超时的请求包装

```javascript
function withTimeout(promise, ms, msg) {
  let timer;
  const timeout = new Promise((_, reject) => {
    timer = setTimeout(() => reject(new Error(msg || `timeout ${ms}ms`)), ms);
  });
  // race 之后必须 clearTimeout，否则短请求结束后仍残留一个 pending 定时器
  return Promise.race([promise, timeout]).finally(() => clearTimeout(timer));
}
```

考点：`finally` 清 timer 是必答项（长连接服务里是泄漏点）；只 race 不 abort 属于「上层不等了，底层还在跑」，真取消要 `controller.abort()`；超时错误要给可识别类型（`name === 'TimeoutError'`）。

### [HW-049] Promise 超时取消

```javascript
function makeCancelable(promise) {
  let canceled = false;
  let cancelReason;
  const wrapped = new Promise((resolve, reject) => {
    promise.then(
      v => (canceled ? reject(cancelError()) : resolve(v)),
      e => (canceled ? reject(cancelError(e)) : reject(e))
    );
  });
  const cancelError = cause => Object.assign(new Error('canceled'), { name: 'AbortError', cause, reason: cancelReason });
  return {
    promise: wrapped,
    cancel(reason = 'canceled') { canceled = true; cancelReason = reason; },
  };
}
```

考点：与 HW-010 的差异是「cancel 后底层结果一律转成取消错误」；但**只在 then 里判断不够**——上层 `await` 仍要等底层返回才退出，所以真正可用版要像精讲 5 那样在取消时主动 reject。

### [HW-062] deferred / Promise.withResolvers

```javascript
function deferred() {
  let resolve, reject;
  const promise = new Promise((res, rej) => { resolve = res; reject = rej; });
  return { promise, resolve, reject };     // 结算权被"提"到外部作用域
}
// ES2024 原生：Promise.withResolvers()，老环境可 polyfill：
if (!Promise.withResolvers) Promise.withResolvers = deferred;
```

考点：把回调式 API 转 Promise（`ws.onmessage = e => d.resolve(e.data)`）；也用于「事件等待」「任务队列手动放行」；**不能当取消用**（取消见 HW-061），resolve/reject 多次调用只有第一次生效。

### [HW-064] 令牌桶限流器

```javascript
class TokenBucket {
  constructor(rate, capacity = rate) {   // rate：每秒补几个令牌
    this.rate = rate; this.capacity = capacity;
    this.tokens = capacity; this.last = Date.now();
  }
  #refill() {                            // 惰性补桶：不依赖 setInterval
    const now = Date.now();
    this.tokens = Math.min(this.capacity, this.tokens + ((now - this.last) / 1000) * this.rate);
    this.last = now;
  }
  acquire() {
    return new Promise(resolve => {
      const tryTake = () => {
        this.#refill();
        if (this.tokens >= 1) { this.tokens -= 1; return resolve(); }
        // 算出"下一个令牌可用"的精确时刻，而不是固定 100ms 轮询
        setTimeout(tryTake, Math.ceil(((1 - this.tokens) / this.rate) * 1000));
      };
      tryTake();
    });
  }
}
```

考点：令牌桶允许**突发**（桶容量），漏桶强制**匀速**；惰性补桶避免定时器空转与漂移；`rate/capacity` 的关系决定「平均速率」与「突发上限」。

### [HW-065] 并发分组合流器

```javascript
function parallelSettle(tasks, { timeout = 8000, onEach } = {}) {
  let timer;
  const timeoutP = new Promise((_, reject) => {
    timer = setTimeout(() => reject(new Error('整体超时')), timeout);
  });
  const all = Promise.allSettled(tasks.map((t, i) => Promise.resolve().then(t)))
    .then(results => {
      // 单项完成即回调：先回来的先渲染，不等最慢的
      results.forEach((r, i) => onEach?.(i, r.status === 'fulfilled' ? r.value : null, r.reason));
      return results;
    });
  return Promise.race([all, timeoutP]).finally(() => clearTimeout(timer));
}
```

考点：`allSettled` 保证「单项失败不炸整体」，`race` 保证「整体有兜底」；`onEach` 才是「谁先回先渲染」的关键，`all` 只负责收口；超时后要能联动取消（`AbortController`），否则只是不等了。

### [HW-085] Promise 顺序执行器

```javascript
async function runSequential(tasks, { strategy = 'fail-fast', onProgress } = {}) {
  const results = [], errors = [];
  for (let i = 0; i < tasks.length; i++) {
    try {
      results[i] = await tasks[i](i);      // 传索引，便于任务知道自己第几步
    } catch (e) {
      errors.push({ index: i, error: e });
      if (strategy === 'fail-fast') return { results, errors, stoppedAt: i };
      results[i] = undefined;              // skip：占位保持索引对齐
    }
    onProgress?.(i + 1, tasks.length);
  }
  return { results, errors };
}
```

考点：`for + await` 才是真串行（`forEach` 里 await 是并发）；三种策略 `fail-fast / skip / collect` 要能一句话说清；跳过时保留 `undefined` 占位，否则结果索引会错位。

### [HW-086] 常驻异步 Worker 队列

```javascript
class AsyncWorker {
  constructor(handler, { maxQueue = 3 } = {}) {
    this.handler = handler; this.maxQueue = maxQueue;
    this.queue = []; this.running = false; this.closed = false;
    this.waiters = [];                    // 背压：等空位的生产者
  }
  push(job) {
    if (this.closed) return Promise.reject(new Error('worker closed'));
    if (this.queue.length >= this.maxQueue) {
      // 队列满 → 挂起生产者，等消费腾位再重试（真正的背压）
      return new Promise(res => this.waiters.push(res)).then(() => this.push(job));
    }
    return new Promise((resolve, reject) => {
      this.queue.push({ job, resolve, reject });
      this.#drain();
    });
  }
  async #drain() {
    if (this.running) return;             // 单消费循环，避免并发重复消费
    this.running = true;
    while (this.queue.length) {
      const { job, resolve, reject } = this.queue.shift();
      this.waiters.shift()?.();            // 腾出空位，唤醒一个被背压的生产者
      try { resolve(await this.handler(job)); } catch (e) { reject(e); }
    }
    this.running = false;
  }
  async close() {
    this.closed = true;                    // 拒新任务，等在途任务自然收尾
    while (this.running || this.queue.length) await new Promise(r => setTimeout(r, 5));
  }
}
```

考点：**常驻消费循环**（不每次重建，避免冷启动）；**背压**是对生产者的限流，而不是简单丢任务；**优雅关闭**要先拒新、再等旧，否则丢数据。

### [HW-087] 带缓存的异步函数（SWR）

```javascript
function cachedAsync(loader, { ttl = 1000, onRevalidate } = {}) {
  const cache = new Map();
  return function (key) {
    const hit = cache.get(key);
    if (hit?.pending) return hit.pending;          // 在途去重：并发调用共享一次请求
    const fresh = hit && Date.now() - hit.at < ttl;
    if (fresh) return Promise.resolve(hit.data);

    const pending = Promise.resolve().then(() => loader(key)).then(data => {
      cache.set(key, { data, at: Date.now() });
      onRevalidate?.(key, data);
      return data;
    }).catch(e => { cache.delete(key); throw e; }); // 错误不缓存，允许立刻重试

    cache.set(key, { data: hit?.data, at: hit?.at ?? 0, pending });
    // SWR：有旧值先给旧值，后台悄悄刷新
    return hit ? Promise.resolve(hit.data) : pending;
  };
}
```

考点：三层叠加——**在途去重**（Promise 级缓存）、**SWR**（先旧后新）、**TTL + 错误不缓存**；缓存 Promise 而不是结果，才能真正合并并发；`onRevalidate` 是告诉 UI「可以替换成新数据了」。

### [HW-161] 防抖的 AbortSignal 集成

```javascript
function debounceSignal(fn, wait, { signal } = {}) {
  let timer = null;
  return (...args) => new Promise((resolve, reject) => {
    clearTimeout(timer);
    if (signal?.aborted) return reject(new DOMException('aborted', 'AbortError'));
    const onAbort = () => { clearTimeout(timer); reject(new DOMException('aborted', 'AbortError')); };
    signal?.addEventListener('abort', onAbort, { once: true });
    timer = setTimeout(() => {
      signal?.removeEventListener('abort', onAbort);     // 正常执行后解绑，避免泄漏
      try { resolve(fn(...args)); } catch (e) { reject(e); }
    }, wait);
  });
}
```

考点：定时器与取消信号统一到一条清理路径；`signal.aborted` 要在入口和 `onAbort` 两处判断（错过信号前已 abort 的情况）；返回 Promise 让调用方能 `await`，也能被 `AbortController` 联动组件卸载。

## 横向对比：四个「批量」API 该选谁

| 需求 | 用哪个 | 结果形态 | 失败行为 |
|---|---|---|---|
| 全部成功才继续 | `all` | 值数组（保序） | 任一失败立刻 reject |
| 全都要结果，失败也要 | `allSettled` | `{status, value/reason}[]` | 永不 reject |
| 只要最快成功的 | `any` | 首个成功值 | 全败 reject `AggregateError` |
| 最快落定的（含失败） | `race` | 首个落定值/错误 | 首个 reject 即 reject |
| 100 个限并发 5 | `p-limit` | 与 `all` 组合 | 单任务失败不影响其他 |
| 有旧值先渲染 | `cachedAsync` (SWR) | 旧值 → 新值 | 错误不写缓存 |

## 常见扣分点

| 扣分点 | 后果 | 正确做法 |
|---|---|---|
| `all` 用 `push` 收集结果 | 结果顺序变成完成顺序，慢请求错位 | `results[i] = v` 按索引写 |
| 漏掉空数组分支 | Promise 永远 pending，页面白屏 | 入口先 `if (len === 0) resolve([])` |
| `race` 后不清定时器 | 残留 pending timer，长驻服务泄漏 | `finally(() => clearTimeout(timer))` |
| `allSettled` 用 `data/error` 字段 | 与规范不兼容，调用方取不到值 | `value` / `reason` |
| `any` 的 errors 用 push | 错误顺序与入参不一致 | `errors[i] = err` 按索引存 |
| `p-limit` 在 `then` 里释放槽位 | 任务失败后槽位不还，池子逐渐死锁 | 放 `finally` |
| `p-limit` 直接 `fn()` | 同步抛错逃出 Promise 链，Promise 永远 pending | `Promise.resolve().then(fn)` |
| retry 复用同一个 Promise | 重试永远拿到同一个 reject，等于没重试 | 每次重新 `fn()` |
| retry 结束抛 `undefined` | 排查时无堆栈无信息 | `throw lastError` |
| 取消只置标记不 reject | `await` 要等底层返回才退出，卸载后仍执行 | 取消时主动 `reject(AbortError)` |
| 把取消当错误上报 | 监控里 AbortError 淹没真实错误 | 按 `name === 'AbortError'` 过滤 |
| 优先级队列用 `sort` 每次排序 | O(n log n) 且同优先级顺序不稳 | 分桶或堆 |
| 去重 key 不释放 | 同名任务永远命中旧结果 | 落定后 `keys.delete` |
| SWR 缓存了失败的 Promise | 一次网络抖动导致该 key 永久失败 | `catch` 里 `cache.delete` |
| 令牌桶用 `setInterval` 补桶 | 定时器空转 + 时间漂移 | 惰性补桶（按需计算） |

## 手写节奏（白板 10 分钟）

1. **先问语义**（1 分钟）：保序还是按完成顺序？失败要短路还是全收？要不要能取消？——三个问题决定实现骨架，也能挡住「写完才被要求改」。
2. **写主干**（4 分钟）：Promise + 计数器 + 按索引写入，先把 happy path 跑通。
3. **补边界**（3 分钟）：空数组、非 Promise 值、同步抛错、finally 清理。
4. **报取舍**（2 分钟）：主动说「fail-fast 不会取消其他请求」「race 空数组永远 pending」「限并发是完成即补位不是分批」——这三句是区分 L1 与 L2 的关键。

## 自测清单

- [ ] 不看答案 5 分钟写出 `promiseAll`，并通过空数组、非 Promise、乱序完成、中途 reject 四个用例。
- [ ] 能解释「为什么 then 回调必须异步」，并说出 Zalgo 是什么。
- [ ] 能手写 `p-limit` 并指出「为什么释放槽位必须放 finally」。
- [ ] 能说清 `all / allSettled / any / race` 四者的失败行为差异，各举一个业务场景。
- [ ] 能写出带抖动与条件重试的 `retry`，并解释抖动防的是什么。
- [ ] 能说清 CancelToken 的三层结构（包装 / 哨兵 / 通知底层），以及为什么必须主动 reject。
- [ ] 能对比「分桶」与「堆」实现优先级队列的复杂度差异。
- [ ] 能说出 SWR 的三个组成部分，以及为什么错误不能进缓存。
