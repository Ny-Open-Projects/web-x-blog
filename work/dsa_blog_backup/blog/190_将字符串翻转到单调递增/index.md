# 190 · 将字符串翻转到单调递增（第十阶段 · 动态规划 · Medium）

> **难度**：⭐⭐ Medium ｜ **专题**：动态规划
> **学习定位**：第十阶段 · 动态规划第 190 篇 ｜ **解法数**：2
> **内容总结**：**将字符串翻转到单调递增**（动态规划 · Medium）：共 2 个方案，主线思路「迭代指针处理」；时间 O(n)（单趟线性扫描）；动画演示DP 表填充过程，附录给出 11 种语言 × 全部方案的可运行实现。

---

## 题目描述

如果一个二进制字符串，是以一些 `0`（可能没有 `0`）后面跟着一些 `1`（也可能没有 `1`）的形式组成的，那么该字符串是 单调递增 的。

给你一个二进制字符串 `s`，你可以将任何 `0` 翻转为 `1` 或者将 `1` 翻转为 `0` 。

返回使 `s` 单调递增的最小翻转次数。

- 主函数签名：`function treeToLevel(root: any): any[]`

**用例（来自原题）**：

**示例 1**

```text
输入：s = "00110"
输出：1
```

解释：翻转最后一位得到 00111.

**示例 2**

```text
输入：s = "010110"
输出：2
```

解释：翻转得到 011111，或者是 000111。

**示例 3**

```text
输入：s = "00011000"
输出：2
```

解释：翻转得到 00000000。
> ✅ **官方验证**：全部 TypeScript 解法已通过 leetcode.cn 官方示例用例验证（自动注入运行，全部 PASS）。题面与 [leetcode.cn 官方](https://leetcode.cn/problems/flip-string-to-monotone-increasing/)一致，示例配图取自官方题面。

**数据范围与注意事项**：

- `1 <= s.length <= 10^5`
- `s[i]` 为 `'0'` 或 `'1'`
- **易错点**：初始化（第 0 行或列）的含义要想清楚，它决定后续转移是否成立。

## 题目分析

**场景是什么**：把大问题拆成小问题并记住结果，对应真实开发里的编辑距离、资源规划。本题就是该场景的 Medium 级练习，主线做法是「迭代指针处理」。

**主线怎么解**：把主解法从头到尾过一遍，它其实在依次做这几件事：队列或堆的调度。

## 解题思路

**方案对比**（共 2 个方案，由浅入深）：

| 方案 | 时间复杂度 | 空间复杂度 |
|---|---|---|
| 方案 1 · 迭代指针处理 | O(n)（单趟线性扫描） | O(1) 到 O(n)（视辅助结构） |
| 方案 2 · 直接实现 | O(n) 量级 | O(n) |

**由浅入深的路径**：迭代指针处理 → 直接实现；每往右一步，都在补上一步的短板。

**方案间的取舍**：方案 1（迭代指针处理）；方案 2（直接实现）。数据规模小、可读性优先时选靠前的方案；规模大、性能优先时选靠后的方案。

**怎么读这一篇**：

- 🐣 **新手路线**：把「题目描述」的示例 1 在纸上手推一遍 → 读方案 1（最直观的写法）与它的代码走读 → 按「运行方式」本地跑通看 PASS → 回头对比方案 2 之后的写法差在哪
- 🦅 **大佬路线**：直接锁定最优方案 1（迭代指针处理，O(n)（单趟线性扫描））→ 跳读该方案代码与走读 → 用「逐步拆解与面试追问」补齐复杂度推导与边界追问

### 动态算法图（DP 表填充，GIF 自动循环）

![动态算法图 · DP 表填充](animation.gif)

动画演示动态规划专题里DP 表填充的典型过程；每个方案在「TypeScript 解题方案」一节还配了专属动画与专属流程图。

### 主解法流程图（真实控制流）

```mermaid
graph TD
    N0["开始：拿到输入"]
    N1{"非 vals 或 vals.length == 0 ？"}
    N2["命中条件，直接返回"]
    N3["计算 root"]
    D1["……（中间计算步骤）"]
    N6["当 (q.length 且 i ＜ vals.length) 时反复执行"]
    D2["……（中间计算步骤）"]
    N16["返回 root"]
    N0 --> N1
    N1 -- 是 --> N2
    N1 -- 否 --> N3
    N6 --> N16
    N2 --> N3
    N3 --> D1
    D1 --> N6
    N6 --> D2
    D2 --> N16
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N3,D1,D2 n;
    class N6 lp;
    class N1 dc;
    class N2,N16 tm;
```

## TypeScript 解题方案（2 个方案逐个讲）

> **运行与提交**：每个方案都是自包含文件（内嵌用例自测，输出 PASS），整块复制到 `.ts` 文件后 `node 文件名` 即可运行。提交 LeetCode 时，把 `demo` 内的算法函数与辅助类型/函数整体取出、置于文件顶层即可。涉及交互/特殊接口的题以题面给定签名为准。

### 方案 1：迭代指针处理

**分析与思路**：核心做法是「迭代指针处理」。代码里依次做这些事：队列或堆的调度。

**运行方式**：`node 本文件`，内嵌用例全部通过会输出 PASS。

![方案 1 动画 · 迭代指针处理](animation_1.gif)

**方案专属流程图**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 迭代指针处理：开始"]
    N1{"非 vals 或 vals.length == 0 ？"}
    N2["命中条件，直接返回"]
    N3["计算 root"]
    D1["……（中间计算步骤）"]
    N6["当 (q.length 且 i ＜ vals.length) 时反复执行"]
    D2["……（中间计算步骤）"]
    N16["返回 root"]
    N0 --> N1
    N1 -- 是 --> N2
    N1 -- 否 --> N3
    N6 --> N16
    N2 --> N3
    N3 --> D1
    D1 --> N6
    N6 --> D2
    D2 --> N16
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N3,D1,D2 n;
    class N6 lp;
    class N1 dc;
    class N2,N16 tm;
```

```typescript
class TreeNode {
  // 定义类型
  val: any;
  left: any;
  right: any; // 值: any; 左边界: any; 右边界: any;
  constructor(val?: any, left?: any, right?: any) {
    // constructor(值?: any, 左边界?: any, 右边界?: any) {
    this.val = val === undefined ? 0 : val; // 把 (值 全等于 undefined ? 0 : 值); 写入 值
    this.left = left === undefined ? null : left; // 把 (左边界 全等于 undefined ? null : 左边界); 写入 左边界
    this.right = right === undefined ? null : right; // 把 (右边界 全等于 undefined ? null : 右边界); 写入 右边界
  }
}
function buildTree(vals: any): any {
  // 定义函数/方法 buildTree
  if (!vals || vals.length === 0) return null; // 若 取反 vals 或 vals.长度 全等于 0，直接返回 null
  const root = new TreeNode(vals[0]);
  const q: any[] = [root];
  let i = 1;
  while (q.length && i < vals.length) {
    // 循环，直到不满足「节点.长度 且 下标 i 小于 vals.长度」
    const node = q.shift(); // 把 节点.shift() 存入 节点
    if (vals[i] !== null && vals[i] !== undefined) {
      node.left = new TreeNode(vals[i]);
      q.push(node.left);
    }
    i++; // 下标 i 加一
    if (i < vals.length && vals[i] !== null && vals[i] !== undefined) {
      node.right = new TreeNode(vals[i]);
      q.push(node.right);
    }
    i++; // 下标 i 加一
  }
  return root; // 返回 根节点
}
function treeToLevel(root: any): any[] {
  // 定义函数/方法 treeToLevel
  if (!root) return []; // 若 取反 根节点，直接返回 []
  const out: any[] = [];
  const q: any[] = [root]; // 把 []; const 节点: any[] 赋值为 [根节点]; 写入 const out: any[]
  while (q.length) {
    // 循环，直到不满足「节点.长度」
    const n = q.shift(); // 把 节点.shift() 存入 元素个数
    if (n === null || n === undefined) {
      out.push(null);
      continue;
    }
    out.push(n.val);
    q.push(n.left);
    q.push(n.right); // 把 元素个数.值 压入栈/数组尾部
  }
  while (out.length && out[out.length - 1] === null) out.pop(); // 循环，直到不满足「out.长度 且 out[out.长度 减 1] 全等于 null) out 弹出 );」
  return out; // 返回 out
}
class ListNode {
  // 定义类型
  val: any;
  next: any; // 值: any; 下一个: any;
  constructor(val?: any, next?: any) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
function buildList(vals: any): any {
  // 定义函数/方法 buildList
  const dummy = new ListNode(0);
  let cur = dummy; // 把 new ListNode(0); let 当前值 赋值为 哨兵节点 存入 哨兵节点
  for (const v of vals) {
    cur.next = new ListNode(v);
    cur = cur.next;
  } // 把 new ListNode(值); 当前值 赋值为 当前值.下一个; } 写入 下一个
  return dummy.next; // 返回 哨兵节点.下一个
}
function listToArray(head: any): any[] {
  // 定义函数/方法 listToArray
  const out: any[] = [];
  let p = head; // 把 []; let 节点 赋值为 头节点; 写入 const out: any[]
  while (p) {
    out.push(p.val);
    p = p.next;
  } // 循环，直到不满足「节点) { out 追加 节点.值); 节点 赋值为 节点.下一个; }」
  return out; // 返回 out
}
// python-runtime shims
function pyLen(a: any): number {
  // 定义函数/方法 pyLen
  if (a === null || a === undefined) return 0; // 若 数组 全等于 null 或 数组 全等于 undefined，直接返回 0
  if (
    typeof a === 'string' ||
    Array.isArray(a) ||
    a instanceof Set ||
    a instanceof Map
  )
    return a.length ?? a.size;
  if (typeof a === 'object') return Object.keys(a).length; // 若 typeof 数组 全等于 'object'，直接返回 Object.keys(数组).长度
  return 0; // 返回 0
}
function pySlice(a: any, i: any, j: any, step?: any): any {
  // 定义函数/方法 pySlice
  if (typeof a === 'string') {
    const r = [...a].slice(i ?? 0, j ?? a.length);
    return step ? r.reverse().join('') : r.join('');
  }
  const arr = Array.isArray(a) ? a : [...a]; // 把 Array.isArray(数组) ? 数组 : 复制的 数组 存入 数组
  return arr.slice(i ?? 0, j ?? arr.length); // 返回 数组 截取 下标 i ?? 0, 下标 j ?? 数组.长度)
}
function pyRange(a: any, b?: any, step?: any): any[] {
  // 定义函数/方法 pyRange
  let s = 0,
    e = a,
    st = 1; // 把 0, e 赋值为 数组, st 赋值为 1 存入 字符串
  if (b !== undefined) {
    s = a;
    e = b;
  } // 若 b 不等于 undefined) { 字符串 赋值为 数组; e 赋值为 b; }
  if (step !== undefined) st = step; // 若 步数 不等于 undefined) st 赋值为 步数;
  const out: any[] = []; // 把 []; 写入 const out: any[]
  if (st > 0) for (let i = s; i < e; i += st) out.push(i);
  else for (let i = s; i > e; i += st) out.push(i); // 否则
  return out; // 返回 out
}
function pyIn(x: any, coll: any): boolean {
  // 定义函数/方法 pyIn
  if (coll === null || coll === undefined) return false; // 若 coll 全等于 null 或 coll 全等于 undefined，直接返回 false
  if (Array.isArray(coll)) return coll.includes(x); // 若 Array.isArray(coll)，直接返回 coll 是否包含 x)
  if (coll instanceof Set || coll instanceof Map) return coll.has(x); // 若 coll instanceof Set 或 coll instanceof Map，直接返回 coll.has(x)
  if (typeof coll === 'object') return x in coll; // 若 typeof coll 全等于 'object'，直接返回 x in coll
  if (typeof coll === 'string') return coll.indexOf(x) >= 0; // 若 typeof coll 全等于 'string'，直接返回 coll 查找 x) 不低于 0
  return false; // 返回 false
}
function pySorted(a: any): any[] {
  // 定义函数/方法 pySorted
  const arr = typeof a === 'string' ? [...a] : [...a]; // 把 (typeof 数组 全等于 'string') ? 复制的 数组 : 复制的 数组 存入 数组
  return arr.sort((x: any, y: any) => (x < y ? -1 : x > y ? 1 : 0));
}
function pyMin(a: any, b?: any): any {
  if (b !== undefined) return Math.min(a, b);
  if (Array.isArray(a) || a instanceof Set) return Math.min(...a);
  return Math.min(a);
} // 定义函数/方法 pyMin
function pyMax(a: any, b?: any): any {
  if (b !== undefined) return Math.max(a, b);
  if (Array.isArray(a) || a instanceof Set) return Math.max(...a);
  return Math.max(a);
} // 定义函数/方法 pyMax
function pySum(a: any): number {
  let s = 0;
  for (const v of a) s += v;
  return s;
} // 定义函数/方法 pySum
function pyAbs(x: any): number {
  return Math.abs(x);
} // 定义函数/方法 pyAbs
function pyEnumerate(a: any): any[] {
  const out: any[] = [];
  let i = 0;
  for (const v of a) {
    out.push([i, v]);
    i++;
  }
  return out;
} // 定义函数/方法 pyEnumerate
function pyZip(a: any, b: any): any[] {
  const n = Math.min(a.length, b.length);
  const out: any[] = [];
  for (let i = 0; i < n; i++) out.push([a[i], b[i]]);
  return out;
} // 定义函数/方法 pyZip
function pyDictGet(d: any, k: any, def?: any): any {
  return k in d ? d[k] : def === undefined ? null : def;
} // 定义函数/方法 pyDictGet
function pyPrint(...args: any[]): void {
  console.log(
    args
      .map((a) => (typeof a === 'object' && a !== null ? JSON.stringify(a) : a))
      .join(' '),
  );
} // 定义函数/方法 pyPrint
// collections / heapq
function heapPush(h: any[], x: any): void {
  h.push(x);
  let i = h.length - 1;
  while (i > 0) {
    const p = (i - 1) >> 1;
    if (h[p] <= h[i]) break;
    [h[p], h[i]] = [h[i], h[p]];
    i = p;
  }
} // 定义函数/方法 heapPush
function heapPop(h: any[]): any {
  const top = h[0];
  const last = h.pop();
  if (h.length) {
    h[0] = last;
    let i = 0;
    const n = h.length;
    while (true) {
      let l = 2 * i + 1,
        r = 2 * i + 2,
        s = i;
      if (l < n && h[l] < h[s]) s = l;
      if (r < n && h[r] < h[s]) s = r;
      if (s === i) break;
      [h[s], h[i]] = [h[i], h[s]];
      i = s;
    }
  }
  return top;
} // 定义函数/方法 heapPop
class Deque {
  private a: any[] = [];
  push(x: any) {
    this.a.push(x);
  }
  pushLeft(x: any) {
    this.a.unshift(x);
  }
  pop() {
    return this.a.pop();
  }
  popLeft() {
    return this.a.shift();
  }
  get length() {
    return this.a.length;
  }
  toArray() {
    return this.a.slice();
  }
} // 定义类型
function Counter(iter: any): any {
  const m: any = {};
  for (const v of iter) m[v] = (m[v] || 0) + 1;
  return m;
} // 定义函数/方法 Counter
function gcd(a: any, b: any): any {
  while (b) {
    [a, b] = [b, a % b];
  }
  return a;
} // 定义函数/方法 gcd
function pyInf(): number {
  return Infinity;
} // 定义函数/方法 pyInf

function norm(x: any): any {
  // 定义函数/方法 norm
  if (x === null || x === undefined) return null; // 若 x 全等于 null 或 x 全等于 undefined，直接返回 null
  if (typeof x === 'object') {
    // 若 typeof x 全等于 'object'
    if (x instanceof Deque) return x.toArray(); // 若 x instanceof Deque，直接返回 x.toArray()
    if (Array.isArray(x)) return x.map(norm); // 若 Array.isArray(x)，直接返回 x.映射表(norm)
    if (
      typeof x.val === 'number' &&
      (typeof x.left !== 'undefined' || typeof x.right !== 'undefined')
    )
      return treeToLevel(x);
    if (typeof x.next !== 'undefined' && typeof x.val === 'number')
      return listToArray(x);
    if (x instanceof Set) return [...x].sort(); // 若 x instanceof Set，直接返回 复制的 x 排序 )
    if (x instanceof Map) return Object.fromEntries(x); // 若 x instanceof Map，直接返回 Object.fromEntries(x)
    const o: any = {};
    for (const k of Object.keys(x)) o[k] = norm(x[k]);
    return o;
  }
  return x; // 返回 x
}
function eq(a: any, b: any): boolean {
  // 定义函数/方法 eq
  const x = norm(a),
    y = norm(b); // 把 norm(数组), y 赋值为 norm(b) 存入 x
  if (x === y) return true; // 若 x 全等于 y，直接返回 true
  if (x === null || y === null) return x === y; // 若 x 全等于 null 或 y 全等于 null，直接返回 x 全等于 y
  if (Array.isArray(x) && Array.isArray(y)) {
    // 若 Array.isArray(x) 且 Array.isArray(y
    if (x.length !== y.length) return false; // 若 x.长度 不等于 y.长度，直接返回 false
    for (let i = 0; i < x.length; i++) if (!eq(x[i], y[i])) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 x.长度 就继续
    return true; // 返回 true
  }
  if (typeof x === 'object' && typeof y === 'object') {
    // 若 typeof x 全等于 'object' 且 typeof y 全等于 'object'
    const kx = Object.keys(x),
      ky = Object.keys(y); // 把 Object.keys(x), ky 赋值为 Object.keys(y) 存入 kx
    if (kx.length !== ky.length) return false; // 若 kx.长度 不等于 ky.长度，直接返回 false
    for (const k of kx) if (!eq(x[k], y[k])) return false;
    return true; // 返回 true
  }
  return x === y; // 返回 x 全等于 y
}

function minFlipsMonoIncr(s) {
  // 定义函数/方法 minFlipsMonoIncr
  let ones = 0,
    flips = 0; // 把 0, flips 赋值为 0 存入 ones
  for (const c of s) {
    // for (const 字符 of 字符串) {
    if (c === '1')
      ones++; // 若 字符 全等于 '1') ones 加一 ;
    else flips = Math.min(flips + 1, ones); // 否则
  }
  return flips; // 返回 flips
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases = [
    { in: ['00110'], want: 1 },
    { in: ['010110'], want: 2 },
    { in: ['000110'], want: 1 },
    { in: [''], want: 0 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = minFlipsMonoIncr(...c.in); // 把 minFlipsMonoIncr(...字符.in) 存入 got
    if (!eq(got, c.want)) {
      fail = true;
      console.log(
        'FAIL',
        JSON.stringify(c.in),
        '=>',
        JSON.stringify(got),
        'want',
        JSON.stringify(c.want),
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error('FAILED');
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
```

### 方案 2：直接实现

**分析与思路**：核心做法是「直接实现」。

**运行方式**：`node 本文件`，内嵌用例全部通过会输出 PASS。

![方案 2 动画 · 直接实现](animation_2.gif)

**方案专属流程图**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 直接实现：开始"]
    N1["计算 a"]
    N2["计算 e"]
    N3["若 a ≠ e：处理 throw new Error("]
    N4["处理 throw new Error("]
    N5["更新 actual"]
    N6["处理 )"]
    N7["返回结果"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N3,N4,N5,N6 n;
    class N7 tm;
```

```typescript
function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function minFlipsMonoIncr(s: string): number {
  // 定义函数/方法 minFlipsMonoIncr
  let one = 0,
    dp = 0; // 把 0, DP 表 赋值为 0 存入 one
  for (const c of s) {
    // for (const 字符 of 字符串) {
    if (c === '0')
      dp = Math.min(one, dp + 1); // 若 字符 全等于 '0') DP 表 赋值为 Math.取较小值 one, DP 表 加 1);
    else one++; // 否则
  }
  return dp; // 返回 DP 表
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(minFlipsMonoIncr('00110'), 1, 'mf'); // 断言校验
  assertEq(minFlipsMonoIncr(''), 0, 'empty'); // 断言校验
  assertEq(minFlipsMonoIncr('1'), 0, 'one'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
```

## 逐步拆解与面试追问

**复杂度**：时间 O(n)（单趟线性扫描），空间 O(1) 到 O(n)（视辅助结构）

**为什么是这个量级**：每个元素被常数次访问，辅助哈希或栈的开销与 n 同阶

**面试官可能会追问**：

- 状态定义为什么是它？
- 遍历顺序由什么决定？
- 能否滚动数组压空间？

## 关键 API 速查（TS 主解法实际用到，附官方链接）

| API | 作用 | 使用要点 | 官方文档 |
|---|---|---|---|
| `Array.prototype.sort()` | 原地排序 | 默认按字符串 Unicode 序（10 会排在 2 前），数字必须传 (a,b)=>a-b；V8 用 TimSort，稳定，O(n log n)；返回原数组引用 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) |
| `Array.prototype.map()` | 逐元素映射为新数组 | 回调 (v,i,arr)；返回等长新数组，不改变原数组；稀疏位跳过；链式调用注意中间数组开销 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/map) |
| `Array.prototype.push()` | 尾部追加 | 返回新长度；可一次多个；均摊 O(1)；会改变原数组 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/push) |
| `Array.prototype.pop()` | 尾部弹出 | 返回被删元素（空数组返回 undefined）；O(1) | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/pop) |
| `Array.prototype.shift()` | 头部取出 | O(n)（后续元素整体前移）；大量头部操作请用链表或双端结构 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/shift) |
| `Array.prototype.unshift()` | 头部插入 | O(n)；与 shift 组合可当双端队列 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift) |
| `Array/String includes()` | 是否包含 | 数组用 SameValueZero（NaN 可判）；字符串按子串；第二个参数为起始下标 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/includes) |
| `Array/String indexOf()` | 首次出现的下标 | 找不到返回 -1；无法判 NaN（用 includes）；字符串可传起始位 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf) |
| `Array/String slice()` | 切片（不改原数组） | slice(start,end) 含头不含尾；负数从尾计；常用于复制数组（slice()） | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) |
| `Array.prototype.join()` | 数组拼接为字符串 | undefined/null 转空串；嵌套数组会展平一层；join('') 用于字符数组还原 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/join) |
| `Object.keys()` | 对象键名数组 | 仅自身可枚举字符串键（不含 symbol）；配 length 可当计数器 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/keys) |
| `Object.fromEntries()` | 键值对数组转对象 | 参数为 [k,v] 可迭代；map 出来的键值对可直接转对象 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries) |
| `JSON.stringify()` | 序列化为 JSON 字符串 | 常用于结构化比较（深度相等判定）；undefined/函数/循环引用会被丢弃或抛错 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) |
| `Math.max()` | 最大值 | 配展开 Math.max(...arr)；空参返回 -Infinity；超大数组注意展开参数上限 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/max) |
| `Math.min()` | 最小值 | 同 max；空参返回 Infinity | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/min) |
| `Math.abs()` | 绝对值 | 入参会被隐式转数字；-0 返回 +0 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/abs) |

### 各语言官方文档导航

- **TypeScript / JS**：[MDN 中文参考](https://developer.mozilla.org/zh-CN/)
- **Python**：[Python 官方文档](https://docs.python.org/zh-cn/3/)
- **Go**：[Go 标准库](https://pkg.go.dev/std)
- **Java**：[JDK 17 API](https://docs.oracle.com/en/java/javase/17/docs/api/)
- **Rust**：[Rust 标准库](https://doc.rust-lang.org/std/)
- **Lua**：[Lua 5.4 手册](https://www.lua.org/manual/5.4/)
- **C**：[Cppreference C](https://zh.cppreference.com/w/c)
- **C++**：[Cppreference C++](https://zh.cppreference.com/w/cpp)
- **R**：[R 官方手册](https://stat.ethz.ch/R-manual/)
- **Zig**：[Zig 语言文档](https://ziglang.org/documentation/master/)
- **Dart**：[Dart API](https://api.dart.dev/)

## 附录：其他 10 种语言全部实现（每种语言列举其全部方案）

> TypeScript 的全部方案见「TypeScript 解题方案」一节；下面是其余 10 种语言的对应实现，每种语言的每个方案都带思路分析、代码走读与专属运行架构图。
> 每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）。
> 完整解法文件见 `dsa/<语言>/dp/lc_926_将字符串翻转到单调递增/`。

### Python 实现（2 种方案）

Python 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Python 版用切片与字典推导式简化操作，突出可读性。**走读**：方案 1 · 迭代指针处理：开始 → 更新 n → 更新 dp0 → 更新 dp1 → 循环 i：从 0 到 n 前 → 更新 c → 更新 dp0New → 更新 dp1New → 若 c == 1：更新 + → 更新 + → 更新 + → 更新 dp0 → 更新 dp1 → 返回 min(dp0, dp1)。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 迭代指针处理：开始"]
    N1["更新 n"]
    N2["更新 dp0"]
    N3["更新 dp1"]
    N4["循环 i：从 0 到 n 前"]
    N5["更新 c"]
    N6["更新 dp0New"]
    N7["更新 dp1New"]
    N8["若 c == 1：更新 +"]
    N9["更新 +"]
    N10["更新 +"]
    N11["更新 dp0"]
    N12["更新 dp1"]
    N13["返回 min(dp0, dp1)"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    N9 --> N10
    N10 --> N11
    N11 --> N12
    N12 --> N13
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N3,N5,N6,N7,N8,N9,N10,N11,N12 n;
    class N4 lp;
    class N13 tm;
```

```python
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级

def minFlipsMonoIncr(s):  # 定义函数 minFlipsMonoIncr（参数：字符串）
    n = len(s)  # 把 长度(字符串) 存入 元素个数
    dp0 = 0  # 把 0 存入 dp0
    dp1 = 0  # 把 0 存入 dp1
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        c = s[i]  # 把 字符串[下标 i] 存入 字符
        dp0New = dp0  # 把 dp0 存入 dp0New
        dp1New = min(dp0, dp1)  # 把 取较小值 dp0, dp1) 存入 dp1New
        if c == "1":  # 若 字符 等于 '1'
            dp0New += 1  # dp0New累加 1
        else:  # 否则
            dp1New += 1  # dp1New累加 1
        dp0 = dp0New  # 把 dp0New 存入 dp0
        dp1 = dp1New  # 把 dp1New 存入 dp1
    return min(dp0, dp1)  # 返回 取较小值 dp0, dp1)

if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minFlipsMonoIncr("00110"))  # 打印输出
```

#### 方案 2：直接实现

**思路与代码分析**：核心是「直接实现」。Python 版用切片与字典推导式简化操作，突出可读性。**走读**：方案 2 · 直接实现：开始 → 更新 one → 填写 DP 表 → 遍历 s: 中的每个元素 c → 若 c == 0：填写 DP 表 → 填写 DP 表 → 更新 + → 返回 dp。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 直接实现：开始"]
    N1["更新 one"]
    N2["填写 DP 表"]
    N3["遍历 s: 中的每个元素 c"]
    N4["若 c == 0：填写 DP 表"]
    N5["填写 DP 表"]
    N6["更新 +"]
    N7["返回 dp"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N4,N5,N6 n;
    class N3 lp;
    class N7 tm;
```

```python
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级

def minFlipsMonoIncr(s):  # 定义函数 minFlipsMonoIncr（参数：字符串）
    one = 0  # 把 0 存入 one
    dp = 0  # 把 0 存入 DP 表
    for c in s:  # 逐个取出 字符串 的元素（字符）
        if c == "0":  # 若 字符 等于 '0'
            dp = min(one, dp + 1)  # 把 取较小值 one, DP 表 加 1) 存入 DP 表
        else:  # 否则
            one += 1  # one累加 1
    return dp  # 返回 DP 表

if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minFlipsMonoIncr("00110"))  # 打印输出
```

### Go 实现（2 种方案）

Go 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Go 版用切片与多返回值惯用法，显式处理索引边界。**走读**：方案 1 · 迭代指针处理：开始 → 更新 : → 遍历循环 → 返回 dp0 → 返回 dp1。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 迭代指针处理：开始"]
    N1["更新 :"]
    D1["……（中间计算步骤）"]
    N4["遍历循环"]
    D2["……（中间计算步骤）"]
    N16["返回 dp0"]
    N17["返回 dp1"]
    N0 --> N1
    N16 --> N17
    N1 --> D1
    D1 --> N4
    N4 --> D2
    D2 --> N16
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,D1,D2 n;
    class N4 lp;
    class N16,N17 tm;
```

```go
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func minFlipsMonoIncr(s string) int { // 定义函数/方法 minFlipsMonoIncr
	n := len(s)              // 把 长度(字符串) 写入 n :
	dp0 := 0                 // 把 0 写入 dp0 :
	dp1 := 0                 // 把 0 写入 dp1 :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		c := s[i]      // 把 字符串[下标 i] 写入 c :
		dp0New := dp0  // 把 dp0 写入 dp0New :
		dp1New := dp0  // 把 dp0 写入 dp1New :
		if dp1 < dp0 { // 若 dp1 小于 dp0
			dp1New = dp1 // 把 dp1 写入 dp1New
		}
		if c == '1' { // 若 字符 等于 '1'
			dp0New++ // dp0New 加一
		} else { // 否则
			dp1New++ // dp1New 加一
		}
		dp0 = dp0New // 把 dp0New 写入 dp0
		dp1 = dp1New // 把 dp1New 写入 dp1
	}
	if dp0 < dp1 { // 若 dp0 小于 dp1
		return dp0 // 返回 dp0
	}
	return dp1 // 返回 dp1
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   string // in string
		want int    // want int
	}{ // }{
		{"00110", 1},
		{"010110", 2},
		{"", 0},
		{"100", 1},
		{"1010", 2},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := minFlipsMonoIncr(c.in); got != c.want { // 若 got : 赋值为 minFlipsMonoIncr(字符.in); got 不等于 字符.want
			ok = false                                                              // 把 false 写入 ok
			fmt.Printf("FAIL minFlipsMonoIncr(%q)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
```

#### 方案 2：直接实现

**思路与代码分析**：核心是「直接实现」。Go 版用切片与多返回值惯用法，显式处理索引边界。**走读**：方案 2 · 直接实现：开始 → 更新 : → 更新 : → 遍历循环 → 更新 : → 处理 if c == '0' → 处理 if one ＜ dp+1 → 填写 DP 表 → 填写 DP 表 → 处理 one++ → 返回 dp。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 直接实现：开始"]
    N1["更新 :"]
    N2["更新 :"]
    N3["遍历循环"]
    N4["更新 :"]
    N5["处理 if c == '0'"]
    N6["处理 if one ＜ dp+1"]
    N7["填写 DP 表"]
    N8["填写 DP 表"]
    N9["处理 one++"]
    N10["返回 dp"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    N9 -- 下一轮 --> N3
    N3 --> N10
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N4,N5,N6,N7,N8,N9 n;
    class N3 lp;
    class N10 tm;
```

```go
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func minFlipsMonoIncr(s string) int { // 定义函数/方法 minFlipsMonoIncr
	one := 0                      // 把 0 写入 one :
	dp := 0                       // 把 0 写入 dp :
	for i := 0; i < len(s); i++ { // 让 下标 i 从 0 开始计数
		c := s[i]     // 把 字符串[下标 i] 写入 c :
		if c == '0' { // 若 字符 等于 '0'
			if one < dp+1 { // 若 one 小于 DP 表 加 1
				dp = one // 把 one 写入 DP 表
			} else { // 否则
				dp = dp + 1 // 把 DP 表 加 1 写入 DP 表
			}
		} else { // 否则
			one++ // one 加一
		}
	}
	return dp // 返回 DP 表
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   string // in string
		want int    // want int
	}{ // }{
		{"00110", 1},
		{"010110", 2},
		{"", 0},
		{"100", 1},
		{"1010", 2},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := minFlipsMonoIncr(c.in); got != c.want { // 若 got : 赋值为 minFlipsMonoIncr(字符.in); got 不等于 字符.want
			ok = false                                                              // 把 false 写入 ok
			fmt.Printf("FAIL minFlipsMonoIncr(%q)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
```

### Java 实现（2 种方案）

Java 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Java 版用类与静态方法组织，集合操作显式明了。代码里依次做这些事：单循环线性扫描。**走读**：方案 1 · 迭代指针处理：开始 → 更新 n → 更新 dp0 → 遍历循环 → 更新 c → 更新 dp0New → 更新 dp1New → 若 c == '1' 则： → 处理 dp0New++ → 处理 dp1New++ → 更新 dp0 → 更新 dp1 → 返回 Math.min(dp0, dp1)。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 迭代指针处理：开始"]
    N1["更新 n"]
    N2["更新 dp0"]
    N3["遍历循环"]
    N4["更新 c"]
    N5["更新 dp0New"]
    N6["更新 dp1New"]
    N7["若 c == '1' 则："]
    N8["处理 dp0New++"]
    N9["处理 dp1New++"]
    N10["更新 dp0"]
    N11["更新 dp1"]
    N12["返回 Math.min(dp0, dp1)"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    N9 --> N10
    N10 --> N11
    N11 -- 下一轮 --> N3
    N3 --> N12
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N4,N5,N6,N7,N8,N9,N10,N11 n;
    class N3 lp;
    class N12 tm;
```

```java
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc926_solution111 { // 定义类型
  public int minFlipsMonoIncr(String s) { // 定义函数/方法 minFlipsMonoIncr
    int n = s.length(); // 把 字符串.长度() 存入 元素个数
    int dp0 = 0, dp1 = 0; // 把 0, dp1 赋值为 0 存入 dp0
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      char c = s.charAt(i); // 逐字符处理
      int dp0New = dp0; // 把 dp0 存入 dp0New
      int dp1New = Math.min(dp0, dp1); // 把 Math.取较小值 dp0, dp1) 存入 dp1New
      if (c == '1') { // 若 字符 等于 '1'
        dp0New++; // dp0New 加一
      } else { // 否则
        dp1New++; // dp1New 加一
      }
      dp0 = dp0New; // 把 dp0New; 写入 dp0
      dp1 = dp1New; // 把 dp1New; 写入 dp1
    }
    return Math.min(dp0, dp1); // 返回 Math.取较小值 dp0, dp1)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc926_solution111 s =
        new lc926_solution111(); // 把 new lc926_solution111(); 写入 lc926_solution111 s
    int got = s.minFlipsMonoIncr("00110"); // 把 字符串.minFlipsMonoIncr(「00110」) 存入 got
    if (got != 1) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
```

#### 方案 2：直接实现

**思路与代码分析**：核心是「直接实现」。Java 版用类与静态方法组织，集合操作显式明了。代码里依次做这些事：单循环线性扫描。**走读**：方案 2 · 直接实现：开始 → 更新 one → 填写 DP 表 → 遍历循环 → 更新 c → 若 c == '0' 则： → 填写 DP 表 → 处理 one++ → 返回 dp。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 直接实现：开始"]
    N1["更新 one"]
    N2["填写 DP 表"]
    N3["遍历循环"]
    N4["更新 c"]
    N5["若 c == '0' 则："]
    N6["填写 DP 表"]
    N7["处理 one++"]
    N8["返回 dp"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 -- 下一轮 --> N3
    N3 --> N8
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N4,N5,N6,N7 n;
    class N3 lp;
    class N8 tm;
```

```java
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc926_solution222 { // 定义类型
  public int minFlipsMonoIncr(String s) { // 定义函数/方法 minFlipsMonoIncr
    int one = 0; // 把 0 存入 one
    int dp = 0; // 把 0 存入 DP 表
    for (int i = 0; i < s.length(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 字符串.长度() 就继续
      char c = s.charAt(i); // 逐字符处理
      if (c == '0') { // 若 字符 等于 '0'
        dp = Math.min(one, dp + 1); // 把 Math.取较小值 one, DP 表 加 1); 写入 DP 表
      } else { // 否则
        one++; // one 加一
      }
    }
    return dp; // 返回 DP 表
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc926_solution222 s =
        new lc926_solution222(); // 把 new lc926_solution222(); 写入 lc926_solution222 s
    int got = s.minFlipsMonoIncr("00110"); // 把 字符串.minFlipsMonoIncr(「00110」) 存入 got
    if (got != 1) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
```

### Rust 实现（2 种方案）

Rust 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Rust 版用所有权移动与切片借用改写同一逻辑，注意 Option 与引用边界。**走读**：方案 1 · 迭代指针处理：开始 → 计算 ones → 计算 flips → 遍历 s.bytes() 中的每个元素 c → 处理 if c == b'1' → 更新 + → 更新 + → 处理 if ones ＜ flips → 更新 flips → 处理 flips → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 迭代指针处理：开始"]
    N1["计算 ones"]
    N2["计算 flips"]
    N3["遍历 s.bytes() 中的每个元素 c"]
    N4["处理 if c == b'1'"]
    N5["更新 +"]
    N6["更新 +"]
    N7["处理 if ones ＜ flips"]
    N8["更新 flips"]
    N9["处理 flips"]
    N10["返回结果"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 -- 下一轮 --> N3
    N3 --> N9
    N9 --> N10
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N4,N5,N6,N7,N8,N9 n;
    class N3 lp;
    class N10 tm;
```

```rust
// LeetCode 926. 将字符串翻转到单调递增 — Rust 版（方案1）
fn min_flips_mono_incr(s: String) -> i32 {
    // 定义函数/方法 min_flips_mono_incr
    let mut ones = 0i32; // 把 0i32; 写入 let mut ones
    let mut flips = 0i32; // 把 0i32; 写入 let mut flips
    for c in s.bytes() {
        // 逐个取出 字符串 的元素（字符）
        if c == b'1' {
            ones += 1;
        }
        // 若 字符 等于 b'1' { ones 累加 1; }
        else {
            // 否则
            flips += 1; // flips累加 1
            if ones < flips {
                flips = ones;
            } // 若 ones 小于 flips { flips 赋值为 ones; }
        }
    }
    flips // flips
}
fn main() {
    assert_eq!(min_flips_mono_incr("00110".into()), 1);
    assert_eq!(min_flips_mono_incr("010110".into()), 2);
    assert_eq!(min_flips_mono_incr("00011000".into()), 2);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
```

#### 方案 2：直接实现

**思路与代码分析**：核心是「直接实现」。Rust 版用所有权移动与切片借用改写同一逻辑，注意 Option 与引用边界。**走读**：方案 2 · 直接实现：开始 → 计算 ones → 计算 flips → 遍历 s.bytes() 中的每个元素 c → 处理 if c == b'1' → 更新 + → 更新 + → 处理 if ones ＜ flips → 更新 flips → 处理 flips → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 直接实现：开始"]
    N1["计算 ones"]
    N2["计算 flips"]
    N3["遍历 s.bytes() 中的每个元素 c"]
    N4["处理 if c == b'1'"]
    N5["更新 +"]
    N6["更新 +"]
    N7["处理 if ones ＜ flips"]
    N8["更新 flips"]
    N9["处理 flips"]
    N10["返回结果"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 -- 下一轮 --> N3
    N3 --> N9
    N9 --> N10
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N4,N5,N6,N7,N8,N9 n;
    class N3 lp;
    class N10 tm;
```

```rust
// LeetCode 926. 将字符串翻转到单调递增 — Rust 版（方案2）
fn min_flips_mono_incr(s: String) -> i32 {
    // 定义函数/方法 min_flips_mono_incr
    let mut ones = 0i32; // 把 0i32; 写入 let mut ones
    let mut flips = 0i32; // 把 0i32; 写入 let mut flips
    for c in s.bytes() {
        // 逐个取出 字符串 的元素（字符）
        if c == b'1' {
            ones += 1;
        }
        // 若 字符 等于 b'1' { ones 累加 1; }
        else {
            // 否则
            flips += 1; // flips累加 1
            if ones < flips {
                flips = ones;
            } // 若 ones 小于 flips { flips 赋值为 ones; }
        }
    }
    flips // flips
}
fn main() {
    assert_eq!(min_flips_mono_incr("00110".into()), 1);
    assert_eq!(min_flips_mono_incr("010110".into()), 2);
    assert_eq!(min_flips_mono_incr("00011000".into()), 2);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
```

### Lua 实现（2 种方案）

Lua 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Lua 版用表与 ipairs 遍历，注意 ipairs 遇 nil 即停的语义。**走读**：方案 1 · 迭代指针处理：开始 → 更新 flips → 循环 i：从 1 到 #s do → 更新 c → 处理 if c == 1 then → 更新 ones → 更新 flips → 处理 if ones ＜ flips then → 更新 flips → 返回 flips。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 迭代指针处理：开始"]
    N1["更新 flips"]
    N2["循环 i：从 1 到 #s do"]
    N3["更新 c"]
    N4["处理 if c == 1 then"]
    N5["更新 ones"]
    N6["更新 flips"]
    N7["处理 if ones ＜ flips then"]
    N8["更新 flips"]
    N9["返回 flips"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N3,N4,N5,N6,N7,N8 n;
    class N2 lp;
    class N9 tm;
```

```lua
-- LeetCode 926. 将字符串翻转到单调递增 — Lua 版（方案1）
local function min_flips_mono_incr(s) -- local function min_flips_mono_incr(字符串)
	local ones, flips = 0, 0 -- 把 0, 0 写入 local ones, flips
	for i = 1, #s do -- 把 1, #字符串 do 写入 for i
		local c = s:sub(i, i) -- 把 字符串:sub(下标 i, 下标 i) 写入 local c
		if c == "1" then
			ones = ones + 1 -- 若 字符 等于 「1」 then ones 赋值为 ones 加 1
		else -- 否则
			flips = flips + 1 -- 把 flips 加 1 存入 flips
			if ones < flips then
				flips = ones
			end -- 若 ones 小于 flips then flips 赋值为 ones 终点
		end -- 终点
	end -- 终点
	return flips -- 返回 flips
end -- 终点
assert(min_flips_mono_incr("00110") == 1) -- 断言校验
assert(min_flips_mono_incr("010110") == 2) -- 断言校验
assert(min_flips_mono_incr("00011000") == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
```

#### 方案 2：直接实现

**思路与代码分析**：核心是「直接实现」。Lua 版用表与 ipairs 遍历，注意 ipairs 遇 nil 即停的语义。**走读**：方案 2 · 直接实现：开始 → 更新 flips → 循环 i：从 1 到 #s do → 更新 c → 处理 if c == 1 then → 更新 ones → 更新 flips → 处理 if ones ＜ flips then → 更新 flips → 返回 flips。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 直接实现：开始"]
    N1["更新 flips"]
    N2["循环 i：从 1 到 #s do"]
    N3["更新 c"]
    N4["处理 if c == 1 then"]
    N5["更新 ones"]
    N6["更新 flips"]
    N7["处理 if ones ＜ flips then"]
    N8["更新 flips"]
    N9["返回 flips"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N3,N4,N5,N6,N7,N8 n;
    class N2 lp;
    class N9 tm;
```

```lua
-- LeetCode 926. 将字符串翻转到单调递增 — Lua 版（方案2）
local function min_flips_mono_incr(s) -- local function min_flips_mono_incr(字符串)
	local ones, flips = 0, 0 -- 把 0, 0 写入 local ones, flips
	for i = 1, #s do -- 把 1, #字符串 do 写入 for i
		local c = s:sub(i, i) -- 把 字符串:sub(下标 i, 下标 i) 写入 local c
		if c == "1" then
			ones = ones + 1 -- 若 字符 等于 「1」 then ones 赋值为 ones 加 1
		else -- 否则
			flips = flips + 1 -- 把 flips 加 1 存入 flips
			if ones < flips then
				flips = ones
			end -- 若 ones 小于 flips then flips 赋值为 ones 终点
		end -- 终点
	end -- 终点
	return flips -- 返回 flips
end -- 终点
assert(min_flips_mono_incr("00110") == 1) -- 断言校验
assert(min_flips_mono_incr("010110") == 2) -- 断言校验
assert(min_flips_mono_incr("00011000") == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
```

### C 实现（2 种方案）

C 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。C 版手动管理下标与内存，循环边界全部显式写出。代码里依次做这些事：单循环线性扫描。**走读**：方案 1 · 迭代指针处理：开始 → 更新 ones → 遍历循环 → 若 *p == '1'：处理 ones++ → 处理 ones++ → 处理 flips++ → 若 ones ＜ flips：更新 flips → 更新 flips → 返回 flips。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 迭代指针处理：开始"]
    N1["更新 ones"]
    N2["遍历循环"]
    N3["若 *p == '1'：处理 ones++"]
    N4["处理 ones++"]
    N5["处理 flips++"]
    N6["若 ones ＜ flips：更新 flips"]
    N7["更新 flips"]
    N8["返回 flips"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 -- 下一轮 --> N2
    N2 --> N8
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N3,N4,N5,N6,N7 n;
    class N2 lp;
    class N8 tm;
```

```c
/* LeetCode 926. 将字符串翻转到单调递增 — C 版（方案1） */
#include <stdio.h>                              // 引入头文件
#include <string.h>                             // 引入头文件
static int min_flips_mono_incr(const char *s) { // 定义函数/方法 min_flips_mono_incr
    int ones = 0, flips = 0;                    // 把 0, flips 赋值为 0 存入 ones
    for (const char *p = s; *p; p++) { // 把 字符串; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        if (*p == '1')
            ones++;  // 若 乘 节点 等于 '1') ones 加一 ;
        else {       // 否则
            flips++; // flips 加一
            if (ones < flips)
                flips = ones; // 若 ones 小于 flips) flips 赋值为 ones;
        }
    }
    return flips; // 返回 flips
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (min_flips_mono_incr("00110") != 1) {
        printf("FAIL 1\n");
        return 1;
    }
    if (min_flips_mono_incr("010110") != 2) {
        printf("FAIL 2\n");
        return 1;
    }
    if (min_flips_mono_incr("00011000") != 2) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS
```

#### 方案 2：直接实现

**思路与代码分析**：核心是「直接实现」。C 版手动管理下标与内存，循环边界全部显式写出。代码里依次做这些事：单循环线性扫描。**走读**：方案 2 · 直接实现：开始 → 更新 ones → 遍历循环 → 若 *p == '1'：处理 ones++ → 处理 ones++ → 处理 flips++ → 若 ones ＜ flips：更新 flips → 更新 flips → 返回 flips。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 直接实现：开始"]
    N1["更新 ones"]
    N2["遍历循环"]
    N3["若 *p == '1'：处理 ones++"]
    N4["处理 ones++"]
    N5["处理 flips++"]
    N6["若 ones ＜ flips：更新 flips"]
    N7["更新 flips"]
    N8["返回 flips"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 -- 下一轮 --> N2
    N2 --> N8
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N3,N4,N5,N6,N7 n;
    class N2 lp;
    class N8 tm;
```

```c
/* LeetCode 926. 将字符串翻转到单调递增 — C 版（方案2） */
#include <stdio.h>                              // 引入头文件
#include <string.h>                             // 引入头文件
static int min_flips_mono_incr(const char *s) { // 定义函数/方法 min_flips_mono_incr
    int ones = 0, flips = 0;                    // 把 0, flips 赋值为 0 存入 ones
    for (const char *p = s; *p; p++) { // 把 字符串; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        if (*p == '1')
            ones++;  // 若 乘 节点 等于 '1') ones 加一 ;
        else {       // 否则
            flips++; // flips 加一
            if (ones < flips)
                flips = ones; // 若 ones 小于 flips) flips 赋值为 ones;
        }
    }
    return flips; // 返回 flips
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (min_flips_mono_incr("00110") != 1) {
        printf("FAIL 1\n");
        return 1;
    }
    if (min_flips_mono_incr("010110") != 2) {
        printf("FAIL 2\n");
        return 1;
    }
    if (min_flips_mono_incr("00011000") != 2) {
        printf("FAIL 3\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS
```

### C++ 实现（2 种方案）

C++ 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。C++ 版用 STL 容器与迭代器，减少手写下标错误。代码里依次做这些事：单循环线性扫描。**走读**：方案 1 · 迭代指针处理：开始 → 更新 ones → 遍历循环 → 若 c == '1'：处理 ++ones → 处理 ++ones → 处理 ++flips → 更新 flips → 返回 flips。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 迭代指针处理：开始"]
    N1["更新 ones"]
    N2["遍历循环"]
    N3["若 c == '1'：处理 ++ones"]
    N4["处理 ++ones"]
    N5["处理 ++flips"]
    N6["更新 flips"]
    N7["返回 flips"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 -- 下一轮 --> N2
    N2 --> N7
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N3,N4,N5,N6 n;
    class N2 lp;
    class N7 tm;
```

```cpp
// LeetCode 926. 将字符串翻转到单调递增 — C++ 版（方案1）
#include <algorithm>                                // 引入头文件
#include <cassert>                                  // 引入头文件
#include <iostream>                                 // 引入头文件
#include <string>                                   // 引入头文件
static int minFlipsMonoIncr(const std::string &s) { // 定义函数/方法 minFlipsMonoIncr
    int ones = 0, flips = 0;                        // 把 0, flips 赋值为 0 存入 ones
    for (char c : s) {                              // for (char 字符 : 字符串) {
        if (c == '1')
            ++ones;                        // 若 字符 等于 '1') 加一 ones;
        else {                             // 否则
            ++flips;                       // 加一 flips;
            flips = std::min(flips, ones); // 把 std::取较小值 flips, ones); 写入 flips
        }
    }
    return flips; // 返回 flips
}
int main() {
    assert(minFlipsMonoIncr("00110") == 1);
    assert(minFlipsMonoIncr("010110") == 2);
    assert(minFlipsMonoIncr("00011000") == 2);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS
```

#### 方案 2：直接实现

**思路与代码分析**：核心是「直接实现」。C++ 版用 STL 容器与迭代器，减少手写下标错误。代码里依次做这些事：单循环线性扫描。**走读**：方案 2 · 直接实现：开始 → 更新 ones → 遍历循环 → 若 c == '1'：处理 ++ones → 处理 ++ones → 处理 ++flips → 更新 flips → 返回 flips。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 直接实现：开始"]
    N1["更新 ones"]
    N2["遍历循环"]
    N3["若 c == '1'：处理 ++ones"]
    N4["处理 ++ones"]
    N5["处理 ++flips"]
    N6["更新 flips"]
    N7["返回 flips"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 -- 下一轮 --> N2
    N2 --> N7
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N3,N4,N5,N6 n;
    class N2 lp;
    class N7 tm;
```

```cpp
// LeetCode 926. 将字符串翻转到单调递增 — C++ 版（方案2）
#include <algorithm>                                // 引入头文件
#include <cassert>                                  // 引入头文件
#include <iostream>                                 // 引入头文件
#include <string>                                   // 引入头文件
static int minFlipsMonoIncr(const std::string &s) { // 定义函数/方法 minFlipsMonoIncr
    int ones = 0, flips = 0;                        // 把 0, flips 赋值为 0 存入 ones
    for (char c : s) {                              // for (char 字符 : 字符串) {
        if (c == '1')
            ++ones;                        // 若 字符 等于 '1') 加一 ones;
        else {                             // 否则
            ++flips;                       // 加一 flips;
            flips = std::min(flips, ones); // 把 std::取较小值 flips, ones); 写入 flips
        }
    }
    return flips; // 返回 flips
}
int main() {
    assert(minFlipsMonoIncr("00110") == 1);
    assert(minFlipsMonoIncr("010110") == 2);
    assert(minFlipsMonoIncr("00011000") == 2);
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS
```

### R 实现（2 种方案）

R 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。R 版用向量化思维与 1 起始下标，注意 1:n 的降序陷阱。代码里依次做这些事：单循环线性扫描。**走读**：方案 1 · 迭代指针处理：开始 → 处理 chars ＜- strsplit(s, )[[1] → 处理 ones ＜- 0L → 处理 flips ＜- 0L → 循环 c：遍历 chars → 若 c == 1：处理 ones ＜- ones + 1L → 处理 ones ＜- ones + 1L → 处理 flips ＜- flips + 1L → 若 ones ＜ flips：处理 flips ＜- ones → 处理 flips ＜- ones → 处理 flips → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 迭代指针处理：开始"]
    N1["处理 chars ＜- strsplit(s, )[[1]"]
    N2["处理 ones ＜- 0L"]
    N3["处理 flips ＜- 0L"]
    N4["循环 c：遍历 chars"]
    N5["若 c == 1：处理 ones ＜- ones + 1L"]
    N6["处理 ones ＜- ones + 1L"]
    N7["处理 flips ＜- flips + 1L"]
    N8["若 ones ＜ flips：处理 flips ＜- ones"]
    N9["处理 flips ＜- ones"]
    N10["处理 flips"]
    N11["返回结果"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    N9 -- 下一轮 --> N4
    N4 --> N10
    N10 --> N11
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N3,N5,N6,N7,N8,N9,N10 n;
    class N4 lp;
    class N11 tm;
```

```r
# 将字符串翻转到单调递增 — R 版（方案1） 定义函数 min_flips_mono_incr（参数：字符串）
min_flips_mono_incr <- function(s) {
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    ones <- 0L
    flips <- 0L  # 把 0L; flips 小于 减 0L 存入 ones
    for (c in chars) {
        # for (字符 in chars) { 否则
        if (c == "1")
            ones <- ones + 1L  # 若 字符 等于 「1」) ones 小于 减 ones 加 1L
 else {
            flips <- flips + 1L  # 把 flips 加 1L 存入 flips
            if (ones < flips)
                flips <- ones  # 若 ones 小于 flips) flips 小于 减 ones
        }
    }
    flips  # flips
}
stopifnot(min_flips_mono_incr("00110") == 1)  # 断言校验
stopifnot(min_flips_mono_incr("010110") == 2)  # 断言校验
stopifnot(min_flips_mono_incr("00011000") == 2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
```

#### 方案 2：直接实现

**思路与代码分析**：核心是「直接实现」。R 版用向量化思维与 1 起始下标，注意 1:n 的降序陷阱。代码里依次做这些事：单循环线性扫描。**走读**：方案 2 · 直接实现：开始 → 处理 chars ＜- strsplit(s, )[[1] → 处理 ones ＜- 0L → 处理 flips ＜- 0L → 循环 c：遍历 chars → 若 c == 1：处理 ones ＜- ones + 1L → 处理 ones ＜- ones + 1L → 处理 flips ＜- flips + 1L → 若 ones ＜ flips：处理 flips ＜- ones → 处理 flips ＜- ones → 处理 flips → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 直接实现：开始"]
    N1["处理 chars ＜- strsplit(s, )[[1]"]
    N2["处理 ones ＜- 0L"]
    N3["处理 flips ＜- 0L"]
    N4["循环 c：遍历 chars"]
    N5["若 c == 1：处理 ones ＜- ones + 1L"]
    N6["处理 ones ＜- ones + 1L"]
    N7["处理 flips ＜- flips + 1L"]
    N8["若 ones ＜ flips：处理 flips ＜- ones"]
    N9["处理 flips ＜- ones"]
    N10["处理 flips"]
    N11["返回结果"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    N9 -- 下一轮 --> N4
    N4 --> N10
    N10 --> N11
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N3,N5,N6,N7,N8,N9,N10 n;
    class N4 lp;
    class N11 tm;
```

```r
# 将字符串翻转到单调递增 — R 版（方案2） 定义函数 min_flips_mono_incr（参数：字符串）
min_flips_mono_incr <- function(s) {
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    ones <- 0L
    flips <- 0L  # 把 0L; flips 小于 减 0L 存入 ones
    for (c in chars) {
        # for (字符 in chars) { 否则
        if (c == "1")
            ones <- ones + 1L  # 若 字符 等于 「1」) ones 小于 减 ones 加 1L
 else {
            flips <- flips + 1L  # 把 flips 加 1L 存入 flips
            if (ones < flips)
                flips <- ones  # 若 ones 小于 flips) flips 小于 减 ones
        }
    }
    flips  # flips
}
stopifnot(min_flips_mono_incr("00110") == 1)  # 断言校验
stopifnot(min_flips_mono_incr("010110") == 2)  # 断言校验
stopifnot(min_flips_mono_incr("00011000") == 2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
```

### Zig 实现（2 种方案）

Zig 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Zig 版显式分配与清零，整型边界处理严格。代码里依次做这些事：单循环线性扫描。**走读**：方案 1 · 迭代指针处理：开始 → 计算 ones → 计算 flips → 遍历集合元素 → 若 c == '1' 则： → 更新 + → 更新 + → 若 ones ＜ flips：更新 flips → 返回 flips。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 迭代指针处理：开始"]
    N1["计算 ones"]
    N2["计算 flips"]
    N3["遍历集合元素"]
    N4["若 c == '1' 则："]
    N5["更新 +"]
    N6["更新 +"]
    N7["若 ones ＜ flips：更新 flips"]
    N8["返回 flips"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 -- 下一轮 --> N3
    N3 --> N8
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N4,N5,N6,N7 n;
    class N3 lp;
    class N8 tm;
```

```zig
// LeetCode 926. 将字符串翻转到单调递增 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn minFlipsMonoIncr(s: []const u8) i32 { // 定义函数/方法 minFlipsMonoIncr
    var ones: i32 = 0; // 把 0; 写入 var ones: i32
    var flips: i32 = 0; // 把 0; 写入 var flips: i32
    for (s) |c| { // 逐个取出 字符串 的元素（字符）
        if (c == '1') { // 若 字符 等于 '1'
            ones += 1; // ones累加 1
        } else { // 否则
            flips += 1; // flips累加 1
            if (ones < flips) flips = ones; // 若 ones 小于 flips) flips 赋值为 ones;
        }
    }
    return flips; // 返回 flips
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (minFlipsMonoIncr("00110") != 1) return error.TestFailed; // 若 minFlipsMonoIncr(「00110」) 不等于 1，直接返回 error.TestFailed
    if (minFlipsMonoIncr("010110") != 2) return error.TestFailed; // 若 minFlipsMonoIncr(「010110」) 不等于 2，直接返回 error.TestFailed
    if (minFlipsMonoIncr("00011000") != 2) return error.TestFailed; // 若 minFlipsMonoIncr(「00011000」) 不等于 2，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
```

#### 方案 2：直接实现

**思路与代码分析**：核心是「直接实现」。Zig 版显式分配与清零，整型边界处理严格。代码里依次做这些事：单循环线性扫描。**走读**：方案 2 · 直接实现：开始 → 计算 ones → 计算 flips → 遍历集合元素 → 若 c == '1' 则： → 更新 + → 更新 + → 若 ones ＜ flips：更新 flips → 返回 flips。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 直接实现：开始"]
    N1["计算 ones"]
    N2["计算 flips"]
    N3["遍历集合元素"]
    N4["若 c == '1' 则："]
    N5["更新 +"]
    N6["更新 +"]
    N7["若 ones ＜ flips：更新 flips"]
    N8["返回 flips"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 -- 下一轮 --> N3
    N3 --> N8
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N4,N5,N6,N7 n;
    class N3 lp;
    class N8 tm;
```

```zig
// LeetCode 926. 将字符串翻转到单调递增 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn minFlipsMonoIncr(s: []const u8) i32 { // 定义函数/方法 minFlipsMonoIncr
    var ones: i32 = 0; // 把 0; 写入 var ones: i32
    var flips: i32 = 0; // 把 0; 写入 var flips: i32
    for (s) |c| { // 逐个取出 字符串 的元素（字符）
        if (c == '1') { // 若 字符 等于 '1'
            ones += 1; // ones累加 1
        } else { // 否则
            flips += 1; // flips累加 1
            if (ones < flips) flips = ones; // 若 ones 小于 flips) flips 赋值为 ones;
        }
    }
    return flips; // 返回 flips
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (minFlipsMonoIncr("00110") != 1) return error.TestFailed; // 若 minFlipsMonoIncr(「00110」) 不等于 1，直接返回 error.TestFailed
    if (minFlipsMonoIncr("010110") != 2) return error.TestFailed; // 若 minFlipsMonoIncr(「010110」) 不等于 2，直接返回 error.TestFailed
    if (minFlipsMonoIncr("00011000") != 2) return error.TestFailed; // 若 minFlipsMonoIncr(「00011000」) 不等于 2，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
```

### Dart 实现（2 种方案）

Dart 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Dart 版用可空类型标注与集合方法，注意空安全。代码里依次做这些事：单循环线性扫描。**走读**：方案 1 · 迭代指针处理：开始 → 计算 ones → 遍历循环 → 若 c == '1' 则： → 处理 ones++ → 处理 flips++ → 若 ones ＜ flips：更新 flips → 返回 flips。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 迭代指针处理：开始"]
    N1["计算 ones"]
    N2["遍历循环"]
    N3["若 c == '1' 则："]
    N4["处理 ones++"]
    N5["处理 flips++"]
    N6["若 ones ＜ flips：更新 flips"]
    N7["返回 flips"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 -- 下一轮 --> N2
    N2 --> N7
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N3,N4,N5,N6 n;
    class N2 lp;
    class N7 tm;
```

```dart
// LeetCode 926. 将字符串翻转到单调递增 — Dart 版（方案1）
int minFlipsMonoIncr(String s) {
  // 定义函数/方法 minFlipsMonoIncr
  var ones = 0, flips = 0; // 把 0, flips 赋值为 0 存入 ones
  for (final c in s.split('')) {
    // for (final 字符 in 字符串.split('')) {
    if (c == '1') {
      ones++;
    } // 若 字符 等于 '1') { ones 加一 ; }
    else {
      // 否则
      flips++; // flips 加一
      if (ones < flips) flips = ones; // 若 ones 小于 flips) flips 赋值为 ones;
    }
  }
  return flips; // 返回 flips
}

void main() {
  if (minFlipsMonoIncr('00110') != 1) throw StateError('c1');
  if (minFlipsMonoIncr('010110') != 2) throw StateError('c2');
  if (minFlipsMonoIncr('00011000') != 2) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
```

#### 方案 2：直接实现

**思路与代码分析**：核心是「直接实现」。Dart 版用可空类型标注与集合方法，注意空安全。代码里依次做这些事：单循环线性扫描。**走读**：方案 2 · 直接实现：开始 → 计算 ones → 遍历循环 → 若 c == '1' 则： → 处理 ones++ → 处理 flips++ → 若 ones ＜ flips：更新 flips → 返回 flips。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 直接实现：开始"]
    N1["计算 ones"]
    N2["遍历循环"]
    N3["若 c == '1' 则："]
    N4["处理 ones++"]
    N5["处理 flips++"]
    N6["若 ones ＜ flips：更新 flips"]
    N7["返回 flips"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 -- 下一轮 --> N2
    N2 --> N7
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N3,N4,N5,N6 n;
    class N2 lp;
    class N7 tm;
```

```dart
// LeetCode 926. 将字符串翻转到单调递增 — Dart 版（方案2）
int minFlipsMonoIncr(String s) {
  // 定义函数/方法 minFlipsMonoIncr
  var ones = 0, flips = 0; // 把 0, flips 赋值为 0 存入 ones
  for (final c in s.split('')) {
    // for (final 字符 in 字符串.split('')) {
    if (c == '1') {
      ones++;
    } // 若 字符 等于 '1') { ones 加一 ; }
    else {
      // 否则
      flips++; // flips 加一
      if (ones < flips) flips = ones; // 若 ones 小于 flips) flips 赋值为 ones;
    }
  }
  return flips; // 返回 flips
}

void main() {
  if (minFlipsMonoIncr('00110') != 1) throw StateError('c1');
  if (minFlipsMonoIncr('010110') != 2) throw StateError('c2');
  if (minFlipsMonoIncr('00011000') != 2) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
```

---

## 内容总结

- **将字符串翻转到单调递增**（动态规划 · Medium）：共 2 个方案，主线思路「迭代指针处理」；时间 O(n)（单趟线性扫描）；动画演示DP 表填充过程，附录给出 11 种语言 × 全部方案的可运行实现。
- 来源博客：[https://blog.csdn.net/tyro_java/article/details/144831489](https://blog.csdn.net/tyro_java/article/details/144831489)
- 导航：[📋 总目录](../) ｜ [← 189 石子游戏](../189_石子游戏/) ｜ [191 不同的子序列 →](../191_不同的子序列/)
