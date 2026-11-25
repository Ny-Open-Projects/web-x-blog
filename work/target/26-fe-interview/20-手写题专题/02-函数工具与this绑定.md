---
title: 02 函数工具与 this 绑定 · 手写题专题
date: 2026-11-24
categories: [前端手写]
tags: [前端面试, 笔试题, HW, 函数工具]
type: 笔试题
---

# 02 函数工具与 this 绑定

> 这一块是「L1 必刷区」：call/apply/bind、防抖、节流几乎是每场面试的暖场题。**能力分层**：L1 能 5 分钟写对 → L2 能补全 immediate/cancel/flush/maxWait → L3 能讲清「为什么要这样设计、什么场景不该用」。

## 能力分层

| 层级 | 题目 | 面试要求 |
|---|---|---|
| L1 必会 | call/apply/bind / new / instanceof / 防抖 / 节流 / once | 5 分钟内写对，不看提示 |
| L2 进阶 | 防抖节流合并可配置 / 柯里化含占位符 / compose / EventEmitter | 15 分钟内写对，边界边说边补 |
| L3 深水 | 防抖边界大全（maxWait/flush）/ memoize 缓存策略 / 惰性函数 | 讲清取舍、失效场景与替代方案 |

判断是否真的会：不看答案写出 `bind` 并说明「`new` 调用时 this 为什么不是绑定的对象」；写出防抖后主动补 `cancel`，并说出 `immediate` 模式下为什么 `cancel` 必须把 timer 置空。这两点能说清，L1 就稳了。

## 本专题原卡全景

| 编号 | 题目 | 层级 | 关键考点 |
|---|---|---|---|
| [HW-011](../06-算法与手写/HW-011-手写-call---apply---bind.md) | 手写 call / apply / bind | L1 | Symbol 挂载、this 装箱、new 优先级 |
| [HW-012](../06-算法与手写/HW-012-手写-new.md) | 手写 new | L1 | 原型挂载、返回对象覆盖实例 |
| [HW-013](../06-算法与手写/HW-013-手写-instanceof.md) | 手写 instanceof | L1 | 原型链遍历、右侧必须是函数 |
| [HW-014](../06-算法与手写/HW-014-手写防抖-含-immediate---cance.md) | 防抖（含 immediate / cancel） | L1 | 闭包 timer、this 透传 |
| [HW-015](../06-算法与手写/HW-015-手写节流.md) | 手写节流 | L1 | 时间戳与定时器互补 |
| [HW-016](../06-算法与手写/HW-016-手写深拷贝.md) | 手写深拷贝 | L1 | 递归、类型分派、WeakMap |
| [HW-017](../06-算法与手写/HW-017-手写浅比较.md) | 手写浅比较 | L1 | 同引用短路、Object.is |
| [HW-018](../06-算法与手写/HW-018-手写-memoize.md) | 手写 memoize | L2 | key 策略、cache 可观测 |
| [HW-019](../06-算法与手写/HW-019-手写-compose---pipe.md) | 手写 compose / pipe | L2 | reduce 组合、执行方向 |
| [HW-020](../06-算法与手写/HW-020-手写-EventEmitter.md) | 手写 EventEmitter | L2 | 订阅表、once 与 off 匹配 |
| [HW-048](../06-算法与手写/HW-048-手写防抖节流合并版-可配置.md) | 防抖节流合并版（可配置） | L2 | 同一骨架、mode 切换、maxWait |
| [HW-051](../06-算法与手写/HW-051-手写惰性函数.md) | 手写惰性函数 | L2 | 函数重写自身、只探测一次 |
| [HW-052](../06-算法与手写/HW-052-手写柯里化-含占位符.md) | 手写柯里化（含占位符） | L3 | 占位符补位、fn.length 局限 |
| [HW-055](../06-算法与手写/HW-055-手写-once-幂等.md) | 手写 once 幂等 | L1 | 缓存首次结果、错误是否重试 |
| [HW-115](../06-算法与手写/HW-115-手写-防抖的-Edge-Case-大合集.md) | 防抖边界大全 | L3 | leading/trailing/cancel/flush/maxWait |
| [HW-118](../06-算法与手写/HW-118-手写-深度冻结对象.md) | 手写 deepFreeze | L2 | 递归冻结、isFrozen 幂等、deopt |

## 精讲（6 题）

### 精讲 1 · [HW-011] 手写 call / apply / bind

**为什么考这个**：这是唯一一道同时考「this 绑定规则」「原型链」「new 的优先级」的题。很多人能写出 `ctx.fn = this`，但答不出「为什么用 Symbol」「为什么 bind 出来的函数还能被 new」「new 时 this 为什么不是绑定的对象」——这三个问题才是真正的分水岭。

**标准实现**：

```javascript
Function.prototype.myCall = function (ctx, ...args) {
  if (typeof this !== 'function') throw new TypeError('not callable');
  // null/undefined → 全局对象；原始值 → 装箱（严格模式下不装箱，可作加分讨论）
  ctx = ctx === null || ctx === undefined ? globalThis : Object(ctx);
  const key = Symbol('fn');        // 唯一 key：不会覆盖对象已有属性，也不会被枚举到
  Object.defineProperty(ctx, key, { value: this, configurable: true });
  try {
    return ctx[key](...args);      // 借对象调用，this 自然指向 ctx
  } finally {
    delete ctx[key];               // 必须清理，否则宿主对象被污染
  }
};

Function.prototype.myApply = function (ctx, args) {
  if (args != null && !Array.isArray(args)) throw new TypeError('args must be array');
  return this.myCall(ctx, ...(args || []));   // 与 call 的唯一区别是参数形态
};

Function.prototype.myBind = function (ctx, ...preset) {
  const fn = this;
  function bound(...args) {
    // new.target 有值说明是 new 调用：this 已是新实例，忽略绑定的 ctx（new 优先级更高）
    return new.target
      ? fn.myCall(this, ...preset, ...args)     // 预设参数 + 调用参数拼接（柯里化）
      : fn.myCall(ctx, ...preset, ...args);
  }
  if (fn.prototype) {
    // 只有函数才有 prototype（对象字面量方法没有），硬挂 undefined 会抛 TypeError
    bound.prototype = Object.create(fn.prototype);  // 让 new bound() instanceof fn 成立
    Object.setPrototypeOf(bound, fn);               // 静态属性/方法继承
  }
  return bound;                                     // 返回新函数，不改原函数
};
```

**必须覆盖的边界**：

- **this 回退** → `null` / `undefined` 在非严格模式回退 `globalThis`，否则 `ctx[key]` 直接抛错。
- **原始值装箱** → `myCall(1)` 时 `Object(1)` 才让 `Number.prototype` 上的方法可用；严格模式下原生 call 不装箱，这是加分讨论点。
- **Symbol 做 key** → 字符串 key 有覆盖风险（对象恰好有同名属性）；且 `Symbol` 属性不会被 `Object.keys` 枚举，污染面更小。
- **必须清理** → `finally` 里 `delete`，否则宿主对象上多一个不可见函数，长生命周期对象会累积。
- **apply 参数校验** → 非数组要抛错，null/undefined 视为空参数（与原生一致）。
- **bind 的 new 优先级** → `new (fn.bind(obj))()` 中 this 是实例而非 `obj`；这是 bind 最容易错的地方。
- **bind 原型链** → 手动 `Object.create(fn.prototype)`，否则 `instanceof` 失效、原型方法拿不到。
- **预设参数拼接** → `bind(obj, 1)(2)` 等价 `fn.call(obj, 1, 2)`，顺序是预设在前。

**追问链**：

1. 原生 bind 出来的函数有 `prototype` 吗？→ 没有。规范里 BoundFunction 没有 prototype 属性，`new boundFn()` 会构造 target；我们手写版为了演示 `instanceof` 才显式挂上去，可主动说明差异。
2. 为什么 `new` 的优先级高于 bind？→ 绑定发生在函数创建时，而 `new` 发生在调用时；调用时的 `[[Construct]]` 会新建实例，若让绑定生效就等于「构造到别人身上」，语义不通。
3. 箭头函数能 call/bind 吗？→ 不能改变 this。箭头函数的 this 在定义时词法确定，`call/apply/bind` 传的 this 会被忽略（参数仍生效）。
4. 严格模式下 `myCall(null)` 应该怎样？→ 原生 call 在严格模式不替换 this，仍是 `null`；我们的版本统一回退 `globalThis`，属于简化，面试中要主动说这是取舍。
5. 除了挂载法还有别的实现吗？→ `Reflect.apply(fn, ctx, args)` 是标准做法（不污染对象），面试可先写挂载法讲原理，再补 `Reflect.apply` 作为生产实现。

### 精讲 2 · [HW-014] 手写防抖（immediate + cancel）

**为什么考这个**：防抖是最高频的手写题，但它藏着三个必考点：`this` 与参数透传、`immediate` 模式的"静默期恢复"、`cancel` 为什么必须把 timer 置空。能写出「看起来对」的防抖只要 6 行，写对这三个边界才是及格线。

**标准实现**：

```javascript
function debounce(fn, wait, { immediate = false } = {}) {
  let timer = null;

  function debounced(...args) {
    // immediate 模式：只有"静默期的第一次"立即执行
    // 注意此处用 !timer 判断，而不是时间戳——timer 存在就说明还在静默期
    const callNow = immediate && !timer;

    clearTimeout(timer);          // 每次触发都重新计时
    timer = setTimeout(() => {
      timer = null;               // 必须置空：否则 immediate 的 !timer 永远为 false，只能触发一次
      if (!immediate) fn.apply(this, args);   // 非 immediate：末尾执行
    }, wait);

    if (callNow) fn.apply(this, args);        // 立即执行放在设置定时器之后，保证 timer 已存在
  }

  debounced.cancel = function () {
    clearTimeout(timer);
    timer = null;                 // 只 clear 不置空，immediate 模式会永久失效
  };

  return debounced;               // 用普通函数而非箭头：需要动态 this
}
```

**必须覆盖的边界**：

- **this 透传** → 返回普通函数 + `fn.apply(this, args)`；用箭头函数会锁死 this，方法调用场景直接错。
- **参数透传** → 只保留最后一次调用的参数（这正是防抖的语义：中间的输入被丢弃）。
- **immediate 的"恢复"** → 静默期内连续触发全部丢弃，静默期过后再触发才重新立即执行；靠 `timer` 是否为空来判断。
- **timer 置空** → 定时器回调里 `timer = null`，否则 `immediate` 只生效一次；`cancel` 里同样要置空。
- **cancel** → 清 timer + 置空 + （可选）暴露 `pending()` 查询状态；Vue/React 卸载时必须调用，否则回调仍会跑。
- **执行顺序** → `callNow` 的判断必须在 `clearTimeout` **之前**，否则永远拿不到"静默期第一次"。

**追问链**：

1. 防抖和节流一句话区别？→ 防抖是「等你停下来再执行」，节流是「固定频率最多执行一次」；输入搜索用防抖，滚动监听用节流。
2. `immediate` 模式适合什么？→ 按钮防连点、提交表单：第一次立刻响应，后续抖动全部忽略，避免用户以为没点上而狂点。
3. 为什么 `cancel` 后 `immediate` 能恢复正常？→ 因为 `timer` 被置空，下一次触发 `!timer` 为 true，重新进入"静默期第一次"。若只 `clearTimeout` 不置空，`timer` 是个已失效的 id，判断永远 false。
4. 怎么让它返回 Promise？→ 见 [HW-161]：把 `resolve` 存进闭包，在定时器回调里 resolve；配合 `AbortSignal` 让取消变成 reject。
5. lodash 的 `debounce` 还多了什么？→ `leading/trailing/maxWait/flush/cancel` 五件套，以及 `flush` 返回最后一次执行结果；完整版见精讲 3 与 [HW-115]。

### 精讲 3 · [HW-048] 防抖节流合并版（可配置 + maxWait）

**为什么考这个**：单一防抖或节流背模板就能过，但面试官常追问「能不能一个函数同时支持两种模式」——考的是你抽象公共骨架的能力。更要命的是 `maxWait`：连续输入 30 秒，纯防抖会一次都不执行，用户看到输入框像卡死。这道题考的就是「防抖为主、节流兜底」的工程直觉。

**标准实现**：

```javascript
function throttleDebounce(fn, wait, {
  mode = 'debounce',        // 'debounce' | 'throttle'
  leading = false,          // 首次是否立即执行
  trailing = true,          // 结束后是否补执行
  maxWait = Infinity,       // 防抖兜底：最长等待多久必须执行一次
} = {}) {
  let timer = null;
  let lastInvoke = 0;       // 上次真正执行的时间
  let firstAt = 0;          // 本轮连续触发的起点（maxWait 用）
  let result;

  const invoke = (ctx, args) => {
    lastInvoke = Date.now();
    result = fn.apply(ctx, args);
    return result;
  };

  function runner(...args) {
    const now = Date.now();
    if (!firstAt) firstAt = now;

    if (mode === 'throttle') {
      // 节流：距上次执行已过 wait 就立即执行
      if (now - lastInvoke >= wait) {
        clearTimeout(timer); timer = null;
        return invoke(this, args);
      }
      // 否则安排一次"补末次"，保证停止触发后还能收到最后一次
      if (!timer && trailing) {
        timer = setTimeout(() => {
          timer = null;
          invoke(this, args);
        }, wait - (now - lastInvoke));
      }
      return;
    }

    // 防抖：首触发立即（leading）
    if (leading && !timer && now - lastInvoke >= wait) invoke(this, args);

    clearTimeout(timer);
    // maxWait 兜底：本轮已持续 firstAt 起 elapsed 毫秒，剩余额度不多了就提前结算
    const elapsed = now - firstAt;
    const delay = Math.min(wait, Math.max(0, maxWait - elapsed));
    timer = setTimeout(() => {
      timer = null;
      firstAt = 0;                       // 结算后开启新一轮
      if (trailing) invoke(this, args);
    }, delay);
  }

  runner.cancel = () => {
    clearTimeout(timer); timer = null; firstAt = 0; lastInvoke = 0;
  };
  // flush：立即结算挂起的调用（如输入框失焦、组件卸载前）
  runner.flush = function (...args) {
    const hasPending = !!timer;
    runner.cancel();
    return hasPending ? invoke(this, args) : result;
  };
  return runner;
}
```

**必须覆盖的边界**：

- **骨架复用** → 两种模式共用 `timer + lastInvoke + firstAt`，只在分支逻辑上分叉；能讲清「共用哪几个状态」比代码本身更重要。
- **`leading + trailing` 同时开** → 首尾各执行一次，中间全部丢弃；要保证首参和末参分别传给两次执行。
- **`maxWait` 的计时起点** → 是「本轮第一次触发」而不是「上次执行」；否则连续触发时永远差一点，永远不会触发兜底。
- **`delay` 不能为负** → `Math.max(0, maxWait - elapsed)`，到点立即结算（`setTimeout(0)`）。
- **`flush` 返回值** → 有挂起任务时返回真正执行的结果；没有则返回上次结果，方便失焦时取最终值做校验。
- **`cancel` 重置完整状态** → 只清 timer 会导致 `leading` 判断错乱，`lastInvoke` / `firstAt` 也要归零。
- **this 与参数** → 用普通函数 + `apply`，`flush` 也要能接收外部参数。

**追问链**：

1. `maxWait` 的本质是什么？→ 给防抖加一个"最大延迟"上限，等价于「防抖的 leading 边沿被节流约束」。lodash 的实现里 `maxWait` 会复用同一个定时器，用 `maxWait - (now - lastInvoke)` 与 `wait - (now - lastInvoke)` 取小。
2. 什么时候必须用 `flush`？→ 输入框失焦、表单提交、组件卸载前——否则最后一次输入还没触发就被销毁，数据丢了。
3. 防抖 + 节流能不能都用 `requestAnimationFrame` 替代？→ 滚动/动画类用 rAF 更贴合帧率（见 [HW-116]），但输入搜索、接口调用不能用 rAF（帧率不等于业务节奏）。
4. 为什么不用 `Date.now()` 而用 `performance.now()`？→ 系统时间被改（NTP 校时、用户手动改）会让 `Date.now()` 跳变，导致节流窗口异常；`performance.now()` 单调递增，更可靠。
5. 合并版会不会更难维护？→ 会。生产里更常见的是「两个独立函数 + 共享一个内部 `createRateLimiter`」，而不是一个函数两套分支；面试可以主动说这个取舍。

### 精讲 4 · [HW-052] 手写柯里化（含占位符）

**为什么考这个**：基础柯里化 8 行就写完，所以面试官一定加占位符。占位符的难点不在递归，而在「新参数要填到前面空出来的位置」——这考的是数组操作与状态合并的细致度。能写出 `curried(1)(_, 3)(2) === 6`，基本就赢了。

**标准实现**：

```javascript
const PLACEHOLDER = Symbol('curry.placeholder');

function curry(fn, arity = fn.length) {
  if (typeof fn !== 'function') throw new TypeError('fn must be a function');

  return function curried(...args) {
    // 1. 参数够数且没有占位符 → 真正执行（多余参数丢弃，与原生语义一致）
    const enough = args.length >= arity;
    const hasHole = args.slice(0, arity).includes(PLACEHOLDER);
    if (enough && !hasHole) return fn.apply(this, args.slice(0, arity));

    // 2. 否则返回收集器，等待下一批参数
    return function next(...more) {
      const merged = args.slice();
      let cursor = 0;
      // 关键：新参数优先填到已有占位符的位置，而不是无脑 push 到末尾
      for (let i = 0; i < merged.length && cursor < more.length; i++) {
        if (merged[i] === PLACEHOLDER) merged[i] = more[cursor++];
      }
      // 剩下的新参数追加到尾部
      while (cursor < more.length) merged.push(more[cursor++]);
      return curried.apply(this, merged);
    };
  };
}

curry.placeholder = PLACEHOLDER;

// curry(add3)(1)(2)(3) === 6
// curry(add3)(1, 2)(3) === 6
// curry(add3)(curry.placeholder, 2)(1)(3) === 6
```

**必须覆盖的边界**：

- **占位符补位而非追加** → `curried(_, 2)(1)(3)`：第一次留下坑位，第二次的 1 要填到下标 0，而不是变成 `[_, 2, 1]`。
- **参数够了但还有占位符** → 继续返回收集器，不能执行（否则 `fn(undefined, 2, 3)` 静默算错）。
- **多轮补参** → 每次合并后递归回 `curried`，而不是只在两层里处理；`curried(_, _, _)(1)(2)(3)` 也要成立。
- **`fn.length` 的局限** → 默认参数、剩余参数、解构参数都不计入 `length`；如 `(a, b = 1) => {}` 的 length 是 1，柯里化会少收一个参数。解决：显式传 `arity`。
- **this 透传** → `curried.apply(this, ...)`，方法柯里化时 this 不能丢。
- **多余参数** → 传统柯里化丢弃多余参数；如果业务需要「全部收集」，去掉 `slice(0, arity)`。
- **占位符唯一性** → 用 `Symbol` 而不是 `'_'` 字符串，避免用户真的想传下划线字符。

**追问链**：

1. 柯里化有什么用？→ 参数复用（`const add10 = add(10)`）、延迟执行（等依赖就绪再调用）、函数组合（`compose` 里每个函数最好单参）。
2. 柯里化和偏函数（partial）区别？→ 柯里化是「一次一个参数，直到凑满」，偏函数是「先固定部分参数，随时可调用」；`bind` 本质就是偏函数。
3. 为什么 `fn.length` 不可靠？→ 只统计「第一个默认值/剩余参数之前」的形参个数；TS 里可通过泛型 + 元组类型做编译期检查，运行时仍需显式 arity。
4. 占位符能用 `undefined` 吗？→ 不能，`undefined` 是合法实参；必须用独立哨兵（Symbol 或唯一对象）。
5. 支持异步的柯里化？→ 本质不变，只是 `fn` 返回 Promise；组合时用 `composeAsync`（见精讲 5）串起来。

### 精讲 5 · [HW-019] 手写 compose / pipe

**为什么考这个**：它是函数式编程的入口题，代码只有 3 行，但能问出「为什么用 reduce 而不是循环」「compose 和 pipe 差在哪」「异步怎么组合」「中间件为什么是反向的」。这题答得好，会显得你有抽象能力；答不好，会暴露「只会背一行 reduce」。

**标准实现**：

```javascript
// compose：从右往左，compose(f, g)(x) === f(g(x))，贴合数学书写习惯
function compose(...fns) {
  if (fns.some(fn => typeof fn !== 'function')) {
    throw new TypeError('all arguments must be functions');
  }
  if (fns.length === 0) return x => x;              // 空组合 = 恒等函数
  // 注意 reduce 的初始值是「函数」，不是值：每次把已有函数包进新函数里
  return fns.reduce((acc, fn) => (...args) => acc(fn(...args)));
}

// pipe：从左往右，读代码的顺序就是数据流动的顺序，业务里更常用
const pipe = (...fns) => compose(...fns.reverse());

// 异步版：把值串成 Promise 链，任一环节 reject 会中断后续
const composeAsync = (...fns) => input =>
  fns.reduceRight((acc, fn) => acc.then(fn), Promise.resolve(input));

// 用法：const format = pipe(trim, toLower, capitalize);
```

**必须覆盖的边界**：

- **执行方向** → `compose(f, g)(x)` 先 `g` 后 `f`；`pipe` 相反。写反了测试一跑就露馅，面试时先说约定。
- **首个函数可多参** → 严格 compose 只有最右（pipe 最左）的函数能接收多参，其余都是单参；上面的 `(...args)` 实现让最外层保留多参能力。
- **空组合** → 返回恒等函数，而不是 `undefined`（否则链式调用崩）。
- **非函数入参** → 提前抛 `TypeError`，别等到运行时 `fn is not a function`。
- **this 语义** → 组合后的函数被当作方法调用时，`this` 应该传给谁？通常是第一个执行的函数，实现里用普通函数保留 this 更严谨。
- **异步错误传播** → `composeAsync` 里 reject 会跳过后续 `.then`，但要保证错误原样抛出，不要吞掉。
- **中间件顺序** → Koa/Redux 的中间件是 `compose` 语义（后注册的先执行内层），理解这题就能理解 `next()` 的洋葱模型。

**追问链**：

1. 为什么用 `reduce` 而不是 `for` 循环？→ 声明式、无中间变量、天然表达「累积成新函数」；但可读性上 `for` 对新手更友好，面试可提这点取舍。
2. `compose` 和管道操作符 `|>` 的关系？→ 提案中的 `x |> f |> g` 就是 `pipe(f, g)`，从左到右；目前需 Babel 插件。
3. 中间件为什么是「洋葱模型」？→ `compose` 把 `(next) => ...` 层层包裹，进入时正序、`await next()` 后逆序，形成先进后出。
4. 怎么让组合支持多返回值 / 解构？→ 让上一环节返回数组、下一环节解构接收；或引入 `ap` / 元组类型，超出面试范围可点到为止。
5. `compose` 和 `curry` 怎么配合？→ 柯里化让每个函数变成单参，正好满足 compose「只接收一个值」的约束，两者是函数式管道的标配。

### 精讲 6 · [HW-020] 手写 EventEmitter

**为什么考这个**：事件总线是「最少代码、最多坑」的题。看起来就是 Map 存数组，但 `once` 与 `off` 的匹配、`emit` 过程中 `off` 导致索引错乱、监听器泄漏——每一个都是真实事故。能主动说出「遍历前拷贝快照」，面试官就知道你写过事件系统。

**标准实现**：

```javascript
class EventEmitter {
  constructor() {
    this.events = new Map();      // type -> Set<fn>，Set 天然去重
  }

  on(type, cb) {
    if (typeof cb !== 'function') throw new TypeError('listener must be function');
    if (!this.events.has(type)) this.events.set(type, new Set());
    this.events.get(type).add(cb);
    return this;                  // 返回 this 支持链式调用（Node 风格）
  }

  once(type, cb) {
    // 包装函数：执行前先注销自己，保证只触发一次
    const wrapper = (...args) => {
      this.off(type, wrapper);
      cb.apply(this, args);
    };
    wrapper._origin = cb;         // 记录原函数，让 off(type, cb) 也能注销
    return this.on(type, wrapper);
  }

  off(type, cb) {
    const set = this.events.get(type);
    if (!set) return this;
    for (const fn of set) {
      // 同时匹配包装函数和它的原函数
      if (fn === cb || fn._origin === cb) set.delete(fn);
    }
    if (set.size === 0) this.events.delete(type);   // 顺手清理空桶，防止 type 无限增长
    return this;
  }

  emit(type, ...args) {
    const set = this.events.get(type);
    if (!set) return false;
    // 关键：拷贝快照再遍历。回调里 off 自己/别人不会打乱本次遍历
    for (const fn of [...set]) fn.apply(this, args);
    return true;
  }

  listenerCount(type) {
    return this.events.get(type)?.size || 0;
  }
}
```

**必须覆盖的边界**：

- **emit 时拷贝快照** → 用数组下标遍历时，回调里 `off` 会导致后续元素前移、跳过执行；拷贝成数组最稳。
- **once 与 off 的匹配** → `off(type, originalFn)` 必须能注销 `once` 注册的包装函数，否则「注册一次却永远删不掉」，这是最高频追问。
- **once 内部先注销再执行** → 顺序反了的话，回调里抛错会导致包装函数永远留在表里。
- **空桶清理** → 注销后 `size === 0` 就 `delete` 该 type，否则 `events` 会随 type 数量无限膨胀（SSR 长驻进程里是泄漏）。
- **Set 而非数组** → 同一函数重复 `on` 只保留一份；若业务要「重复注册多次触发」，改用数组并明确语义。
- **错误隔离** → 一个监听器抛错会中断后续监听器；生产版应 `try/catch` 后异步抛出（`setTimeout(() => { throw e })`），避免一个坏监听器拖垮全部。
- **返回 this** → 链式调用是 Node 兼容性细节，也方便写 `ee.on(a).on(b)`。

**追问链**：

1. 为什么用 `Map` 不用普通对象？→ 对象 key 只能是 string/symbol，且 `__proto__`、`constructor` 等键会与原型冲突（原型污染风险）；Map 任意 key 且无原型链干扰。
2. `once` 的回调里 `this` 指向谁？→ 本例指向 emitter；Node 的 EventEmitter 也是绑定到 emitter 实例，若需业务 this 请用箭头函数或 `bind`。
3. 怎么实现 `emit` 的异步版本？→ 每个监听器包 `Promise.resolve().then(() => fn(...))`，`emitAsync` 返回 `Promise.allSettled`，让调用方等全部完成。
4. 事件命名空间怎么做？→ `emit('user:login')` 时先精确匹配，再按 `:` 逐级冒泡到 `user:*` / `*`；实现上是字符串前缀匹配 + 通配符表。
5. 怎么防内存泄漏？→ 提供 `off` / `removeAllListeners` / `setMaxListeners` 告警；React 里在 `useEffect` 返回清理函数，Vue 里在 `onUnmounted` 解绑。

## 其余 10 题速查

> 每题给最小可跑版 + 一句核心考点。深拷贝在 [03 专题](./03-对象数组与数据结构.md) 有完整版，这里只留速写骨架。

### [HW-012] 手写 new

```javascript
function myNew(Ctor, ...args) {
  if (typeof Ctor !== 'function') throw new TypeError('not a constructor');
  const obj = Object.create(Ctor.prototype);   // ① 建空对象 ② 挂原型（一步完成）
  const result = Ctor.apply(obj, args);        // ③ 以新对象为 this 执行构造
  // ④ 构造函数显式返回对象/函数则覆盖，返回原始值则忽略
  return result !== null && (typeof result === 'object' || typeof result === 'function')
    ? result : obj;
}
```

考点：四步顺序不能乱；`null` 是 `typeof === 'object'` 的坑，必须先判 `!== null`；「返回原始值被忽略」是最常被追问的一点。

### [HW-013] 手写 instanceof

```javascript
function myInstanceof(left, right) {
  if (typeof right !== 'function' || right === null) return false;   // 右侧必须是函数
  if (left === null || (typeof left !== 'object' && typeof left !== 'function')) return false;
  let proto = Object.getPrototypeOf(left);
  while (proto) {                          // 沿原型链向上，直到 null
    if (proto === right.prototype) return true;
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}
```

考点：右侧校验很多人漏写；原始值直接 false（不再取原型）；`Symbol.hasInstance` 可自定义行为，是加分点。

### [HW-015] 手写节流

```javascript
function throttle(fn, wait) {
  let prev = 0;            // 上次执行时间（时间戳版：首次立即执行）
  let timer = null;
  return function (...args) {
    const now = Date.now();
    const remain = wait - (now - prev);
    if (remain <= 0) {
      if (timer) { clearTimeout(timer); timer = null; }   // 切换路径时清掉挂起 timer
      prev = now;
      fn.apply(this, args);
    } else if (!timer) {
      timer = setTimeout(() => {                          // 补末次：停止触发也不丢最后一次
        timer = null; prev = Date.now();
        fn.apply(this, args);
      }, remain);
    }
  };
}
```

考点：时间戳版「首次立即、末次丢失」，定时器版「首次延迟、末次必执行」，合并版两者兼得；切换分支必须清 timer，否则会重复执行。

### [HW-016] 手写深拷贝

```javascript
function deepClone(input, seen = new WeakMap()) {
  if (input === null || typeof input !== 'object') return input;   // 原始值 + 函数
  if (seen.has(input)) return seen.get(input);                    // 循环引用
  if (input instanceof Date) return new Date(input.getTime());
  if (input instanceof RegExp) return new RegExp(input.source, input.flags);
  const clone = Array.isArray(input) ? [] : Object.create(Object.getPrototypeOf(input));
  seen.set(input, clone);                                         // 先登记再递归
  for (const key of Reflect.ownKeys(input)) {
    const desc = Object.getOwnPropertyDescriptor(input, key);
    if (!desc || !desc.enumerable) continue;                      // 跳过不可枚举
    clone[key] = deepClone(input[key], seen);
  }
  return clone;
}
```

考点：`seen.set` 必须在递归之前；`Reflect.ownKeys` 覆盖 Symbol；Map/Set/Blob/TypedArray 需要单独分派，完整版见 [03 专题](./03-对象数组与数据结构.md)。

### [HW-017] 手写浅比较

```javascript
function shallowEqual(a, b) {
  if (Object.is(a, b)) return true;            // 同引用短路，同时正确处理 NaN / +0
  if (a === null || b === null || typeof a !== 'object' || typeof b !== 'object') return false;
  const keysA = Object.keys(a);
  const keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;          // key 数不同直接否
  return keysA.every(k => Object.prototype.hasOwnProperty.call(b, k) && Object.is(a[k], b[k]));
}
```

考点：先短路再判类型；用 `Object.is` 而非 `===`（`NaN` 相等、`+0/-0` 不等）；只比一层，嵌套对象靠引用相等——这正是 `React.memo` 默认行为。

### [HW-018] 手写 memoize

```javascript
function memoize(fn, resolver) {
  const cache = new Map();
  function memoized(...args) {
    const key = resolver ? resolver.apply(this, args) : args[0];   // 默认首参做 key
    if (cache.has(key)) return cache.get(key);
    const value = fn.apply(this, args);                            // 保留 this
    cache.set(key, value);
    return value;
  }
  memoized.cache = cache;      // 暴露缓存：便于测试与手动失效
  return memoized;
}
```

考点：`cache.has` 而非 `cache.get` 判存在（值可能是 `undefined`）；对象做 key 时用 `WeakMap` 防泄漏；多参数必须自定义 resolver，否则参数变了也命中旧值。

### [HW-051] 手写惰性函数

```javascript
// 版本 A：函数重写自身（模块级绑定可被重写，适合特性检测）
let addEvent = function (el, type, handler) {
  if (el.addEventListener) {
    addEvent = (el, type, handler) => el.addEventListener(type, handler);
  } else {
    addEvent = (el, type, handler) => el.attachEvent('on' + type, handler);
  }
  return addEvent(el, type, handler);   // 首次调用也要返回正确结果
};

// 版本 B：闭包缓存（不改函数引用，适合初始化一次的资源）
function lazy(factory) {
  let cached; let ready = false;
  return function (...args) {
    if (!ready) { cached = factory(); ready = true; }
    return typeof cached === 'function' ? cached.apply(this, args) : cached;
  };
}
```

考点：核心是「判断只发生一次」，把探测成本从每次调用降到一次；版本 A 换的是引用（外部可见），版本 B 换的是内部状态（签名不变）；场景：XHR 兼容、`document.documentElement.style` 前缀探测。

### [HW-055] 手写 once 幂等

```javascript
function once(fn) {
  let called = false;
  let result;
  return function (...args) {
    if (!called) {
      called = true;
      result = fn.apply(this, args);     // 缓存首次结果（含 this）
    }
    return result;                       // 后续调用参数不同也返回首次结果
  };
}
```

考点：「只执行一次 + 结果复用」是两个能力，很多人只做了前者；抛错后是否允许重试要说清（lodash 不允许，可加 `retryOnError` 选项）；场景：支付按钮防重、单例初始化。

### [HW-115] 防抖边界大全

```javascript
function debounceFull(fn, wait, { leading = false, trailing = true, maxWait } = {}) {
  let timer = null;
  let lastArgs = null, lastThis = null;
  let lastInvoke = 0;      // 上次真正执行的时间，供 leading 判断
  let firstAt = 0;         // 本轮连续触发的起点，供 maxWait 判断
  let result;

  function invoke() {
    const ctx = lastThis, args = lastArgs;   // 先取再清空，顺序不能反
    result = fn.apply(ctx, args);
    lastInvoke = Date.now();
    lastArgs = lastThis = null;
    return result;
  }

  function debounced(...args) {
    const now = Date.now();
    lastArgs = args;
    lastThis = this;

    // 1) leading：本轮第一次触发立即执行（距上次执行足够久才算新一轮）
    if (leading && !timer && (!firstAt || now - firstAt >= wait)) {
      firstAt = now;
      invoke();
    }
    if (!firstAt) firstAt = now;

    // 2) 重新计时：静默 wait 后补 trailing
    clearTimeout(timer);
    // 3) maxWait：连续触发太久也要强制结算，防止一直饿死
    const elapsed = now - firstAt;
    const delay = maxWait != null ? Math.max(0, Math.min(wait, maxWait - elapsed)) : wait;

    timer = setTimeout(() => {
      timer = null;
      const pending = lastArgs !== null;
      if (trailing && pending) invoke();
      firstAt = 0;                        // 结算后开启新一轮
      if (!trailing) lastArgs = lastThis = null;
    }, delay);
  }

  debounced.cancel = () => {
    clearTimeout(timer);
    timer = null; lastArgs = lastThis = null; firstAt = 0; lastInvoke = 0;
  };
  debounced.flush = () => {
    if (!timer) return result;            // 无待执行任务：返回上次结果
    clearTimeout(timer); timer = null; firstAt = 0;
    return lastArgs !== null && trailing ? invoke() : result;
  };
  debounced.pending = () => timer !== null;
  return debounced;
}
```

考点：`leading` 首执行、`trailing` 末执行、`cancel` 清理、`flush` 立即结算、`maxWait` 防饿死——五个开关的组合语义要能画成时序图；`invoke` 里必须**先取参数再置空**，否则 `fn.apply(null, null)` 直接抛错；`maxWait` 的计时起点是「本轮第一次触发」而不是「上次执行」。

### [HW-118] 手写 deepFreeze

```javascript
function deepFreeze(obj, seen = new WeakSet()) {
  if (obj === null || typeof obj !== 'object') return obj;
  if (seen.has(obj) || Object.isFrozen(obj)) return obj;   // 幂等 + 防环
  seen.add(obj);
  Object.freeze(obj);
  for (const key of Reflect.ownKeys(obj)) deepFreeze(obj[key], seen);
  return obj;
}
```

考点：`isFrozen` 先判，避免重复递归；`WeakSet` 防循环引用（冻结一个自引用对象会无限递归）；`Object.freeze` 是浅冻结，只冻结自身属性；代价是 V8 对冻结对象写入路径有 deopt，热路径大对象别冻。

## 横向对比：防抖 / 节流 / 惰性 / once

| 工具 | 触发次数 | 时间语义 | 典型场景 | 不适用 |
|---|---|---|---|---|
| debounce | 停止后 1 次 | 静默 wait 后执行 | 搜索联想、表单校验 | 需要实时反馈的滚动 |
| throttle | 每 wait 最多 1 次 | 固定频率 | 滚动监听、拖拽、resize | 输入框（会丢字） |
| debounce + maxWait | 至少每 maxWait 1 次 | 防抖为主、节流兜底 | 自动保存草稿 | 对延迟极敏感的操作 |
| 惰性函数 | 首次探测 1 次 | 环境判断只做一次 | 兼容性探测 | 环境会变化的场景 |
| once | 全生命周期 1 次 | 首次结果复用 | 单例、支付防重 | 需要重试的初始化 |

## 常见扣分点

| 扣分点 | 后果 | 正确做法 |
|---|---|---|
| `myCall` 用字符串 key 挂载 | 覆盖对象同名属性，污染宿主 | `Symbol` + `finally` 清理 |
| `this` 为 null 不兜底 | `ctx[key]` 抛 TypeError | 回退 `globalThis` 或 `Object(ctx)` |
| `bind` 忽略 `new` | `new (fn.bind(o))` 的 this 错成 `o` | 用 `new.target` 判断 |
| `bind` 硬挂 `fn.prototype` | 对象字面量方法没有 prototype，直接抛错 | `if (fn.prototype)` 守卫 |
| 防抖用箭头函数 | this 锁死在定义处，方法调用全错 | 普通函数 + `apply` |
| 防抖 `cancel` 不置空 timer | `immediate` 模式永久失效 | 清 timer 且 `timer = null` |
| 防抖在 `clearTimeout` 后判 `!timer` | `immediate` 判断失效 | 先判 `callNow` 再清理 |
| 节流切换分支不清 timer | 一次触发执行两次 | 立即执行前 `clearTimeout` |
| `once` 只防重复不缓存结果 | 后续调用返回 `undefined` | 缓存首次返回值与 this |
| `once` 抛错后置 `called` | 失败后永远无法重试 | 明确策略：成功后才置位 |
| 柯里化把新参数直接 push | 占位符位置永远补不上 | 先填占位符再追加 |
| `curry` 依赖 `fn.length` | 默认参数导致少收参数 | 显式传 `arity` |
| `compose` 用 `reduceRight` 却写成值累加 | 组合结果变成值而非函数 | 累积的是函数，初始值是 `x => x` |
| `emit` 直接遍历原 Set | 回调里 `off` 导致跳过监听器 | 遍历 `[...set]` 快照 |
| `once` 不记 `_origin` | `off(type, 原函数)` 删不掉 | 包装函数挂 `_origin` |
| `deepFreeze` 不防环 | 自引用对象栈溢出 | `WeakSet` 记录已访问 |
| `memoize` 用 `cache.get` 判命中 | 值为 `undefined` 时误判未命中 | `cache.has` |

## 手写节奏（白板 8 分钟）

1. **先问语义**（30 秒）：要不要改 this？要不要支持 new？要不要立即执行？——三句话定下骨架。
2. **写主干**（3 分钟）：call/bind 写挂载 + 清理，防抖写 timer + apply，先把正常路径跑通。
3. **补边界**（3 分钟）：null this、cancel 置空、new 优先级、参数透传。
4. **报差异**（1.5 分钟）：主动说「生产里用 `Reflect.apply`」「防抖还有 maxWait/flush」「lodash 的 once 不支持失败重试」。

## 自测清单

- [ ] 不看答案 5 分钟写出 call/apply/bind，并说清 `new (fn.bind(o))` 里 this 为什么是实例。
- [ ] 能解释为什么 `myCall` 必须用 `Symbol` 且必须 `finally` 清理。
- [ ] 能写出带 `immediate` 与 `cancel` 的防抖，并解释 `cancel` 为什么要置空 timer。
- [ ] 能区分时间戳版与定时器版节流各自丢哪一次，并写出合并版。
- [ ] 能画出 `leading + trailing + maxWait` 的触发时序图（至少 6 个触发点）。
- [ ] 能写出支持占位符的柯里化，并跑通 `curried(1)(_, 3)(2)`。
- [ ] 能说清 `compose` 与 `pipe` 的方向、空组合、异步版错误传播。
- [ ] 能解释 EventEmitter 为什么遍历前要拷贝快照、`once` 为什么要挂 `_origin`。
- [ ] 能说出 `fn.length` 在什么情况下不可靠，以及怎么绕过。
- [ ] 能对比 once 与 memoize：一个是「只执行一次」，一个是「同参只算一次」。
