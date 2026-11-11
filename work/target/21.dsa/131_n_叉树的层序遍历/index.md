# 131 · n 叉树的层序遍历（第六阶段 · 二叉树 · Medium）

> **难度**：⭐⭐ Medium ｜ **专题**：二叉树
> **学习定位**：第六阶段 · 二叉树第 131 篇 ｜ **解法数**：2
> **内容总结**：**n 叉树的层序遍历**（二叉树 · Medium）：共 2 个方案，主线思路「双重循环枚举」；时间 O(n²)（两层嵌套扫描）；动画演示DFS 点亮过程，附录给出 11 种语言 × 全部方案的可运行实现。

---

## 题目描述

给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。

- 主函数签名：`function levelOrder(root: Node | null): number[][]`

**用例（来自原题）**：

**示例 1**

![示例 1 配图](imgs/1_1.png)

```text
输入：root = [1,null,3,2,4,null,5,6]
输出：[[1],[3,2,4],[5,6]]
```

**示例 2**

![示例 2 配图](imgs/2_1.png)

```text
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
```
> 题面与 [leetcode.cn 官方](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/)一致，示例配图取自官方题面。

**数据范围与注意事项**：

- 树的高度不会超过 `1000`
- `树的节点总数在 `[0, 10^4]` 之间`
- **易错点**：递归出口（空节点）必须先写，否则直接空指针。

## 题目分析

**场景是什么**：树是分层数据的标准形态，这类题练的是递归分治与遍历序，对应真实开发里的目录树、组件树。本题就是该场景的 Medium 级练习，主线做法是「双重循环枚举」。

**主线怎么解**：把主解法从头到尾过一遍，它其实在依次做这几件事：双重循环遍历 → 队列或堆的调度。

## 解题思路

**方案对比**（共 2 个方案，由浅入深）：

| 方案 | 时间复杂度 | 空间复杂度 |
|---|---|---|
| 方案 1 · 双重循环枚举 | O(n²)（两层嵌套扫描） | O(1) 到 O(n) |
| 方案 2 · 迭代指针处理 | O(n)（单趟线性扫描） | O(1) 到 O(n)（视辅助结构） |

**由浅入深的路径**：双重循环枚举 → 迭代指针处理；每往右一步，都在补上一步的短板。

**方案间的取舍**：方案 1（双重循环枚举）；方案 2（迭代指针处理）。数据规模小、可读性优先时选靠前的方案；规模大、性能优先时选靠后的方案。

**怎么读这一篇**：

- 🐣 **新手路线**：把「题目描述」的示例 1 在纸上手推一遍 → 读方案 1（最直观的写法）与它的代码走读 → 按「运行方式」本地跑通看 PASS → 回头对比方案 2 之后的写法差在哪
- 🦅 **大佬路线**：直接锁定最优方案 2（迭代指针处理，O(n)（单趟线性扫描））→ 跳读该方案代码与走读 → 用「逐步拆解与面试追问」补齐复杂度推导与边界追问

### 动态算法图（DFS 点亮，GIF 自动循环）

![动态算法图 · DFS 点亮](animation.gif)

动画演示二叉树专题里DFS 点亮的典型过程；每个方案在「TypeScript 解题方案」一节还配了专属动画与专属流程图。

### 主解法流程图（真实控制流）

```mermaid
graph TD
    N0["开始：拿到输入"]
    N1{"非 root ？"}
    N2["命中条件，直接返回"]
    N3["计算 res"]
    N4["计算 q"]
    N5["当 (q.length) 时反复执行"]
    N6["计算 lvl"]
    N7["计算 n"]
    N8["循环 k：从 0 起步，当 k ＜ n 时继续，每轮 k++"]
    N9["计算 x"]
    N10["向 lvl 追加记录"]
    N11["遍历 x.children 中的每个元素 c"]
    N12["向 res 追加记录"]
    N13["返回 res"]
    N0 --> N1
    N1 -- 是 --> N2
    N1 -- 否 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    N9 --> N10
    N10 --> N11
    N11 -- 下一轮 --> N8
    N8 --> N12
    N12 -- 下一轮 --> N5
    N5 --> N13
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N3,N4,N6,N7,N9,N10,N12 n;
    class N5,N8,N11 lp;
    class N1 dc;
    class N2,N13 tm;
```

## TypeScript 解题方案（2 个方案逐个讲）

> **运行与提交**：每个方案都是自包含文件（内嵌用例自测，输出 PASS），整块复制到 `.ts` 文件后 `node 文件名` 即可运行。提交 LeetCode 时，把 `demo` 内的算法函数与辅助类型/函数整体取出、置于文件顶层即可。**提交备注**：注意：原题为 N 叉树（节点含 children 数组），提交时需按题面给定的 Node 定义组织代码。

### 方案 1：双重循环枚举

**分析与思路**：核心做法是「双重循环枚举」。代码里依次做这些事：双重循环遍历；队列或堆的调度。

**运行方式**：`node 本文件`，内嵌用例全部通过会输出 PASS。

![方案 1 动画 · 双重循环枚举](animation_1.gif)

**方案专属流程图**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 双重循环枚举：开始"]
    N1{"非 root ？"}
    N2["命中条件，直接返回"]
    N3["计算 res"]
    N4["计算 q"]
    N5["当 (q.length) 时反复执行"]
    N6["计算 lvl"]
    N7["计算 n"]
    N8["循环 k：从 0 起步，当 k ＜ n 时继续，每轮 k++"]
    N9["计算 x"]
    N10["向 lvl 追加记录"]
    N11["遍历 x.children 中的每个元素 c"]
    N12["向 res 追加记录"]
    N13["返回 res"]
    N0 --> N1
    N1 -- 是 --> N2
    N1 -- 否 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    N9 --> N10
    N10 --> N11
    N11 -- 下一轮 --> N8
    N8 --> N12
    N12 -- 下一轮 --> N5
    N5 --> N13
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N3,N4,N6,N7,N9,N10,N12 n;
    class N5,N8,N11 lp;
    class N1 dc;
    class N2,N13 tm;
```

```typescript
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class Node {
    val: number;
    children: Node[] = [];
    constructor(v: number) {
      this.val = v;
    }
  } // 定义类型
  function levelOrder(root: Node | null): number[][] {
    if (!root) return [];
    const res: number[][] = [];
    let q: Node[] = [root];
    while (q.length) {
      const lvl: number[] = [];
      const n = q.length;
      for (let k = 0; k < n; k++) {
        const x = q.shift()!;
        lvl.push(x.val);
        for (const c of x.children) q.push(c);
      }
      res.push(lvl);
    }
    return res;
  } // 定义函数/方法 levelOrder
  const c5 = new Node(5),
    c6 = new Node(6);
  const c3 = new Node(3);
  c3.children = [c5, c6];
  const c2 = new Node(2),
    c4 = new Node(4);
  const root = new Node(1);
  root.children = [c3, c2, c4];
  if (
    JSON.stringify(levelOrder(root)) !==
    JSON.stringify([[1], [3, 2, 4], [5, 6]])
  ) {
    console.log('FAIL');
    throw new Error('FAILED');
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
```

### 方案 2：迭代指针处理

**分析与思路**：核心做法是「迭代指针处理」。代码里依次做这些事：队列或堆的调度。

**运行方式**：`node 本文件`，内嵌用例全部通过会输出 PASS。

![方案 2 动画 · 迭代指针处理](animation_2.gif)

**方案专属流程图**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 迭代指针处理：开始"]
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
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
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

class NNode {
  // 定义类型
  val: any;
  children: any[]; // 值: any; children: any[];
  constructor(val?: any, children?: any[]) {
    // constructor(值?: any, children?: any[]) {
    this.val = val === undefined ? 0 : val; // 把 (值 全等于 undefined ? 0 : 值); 写入 值
    this.children = children === undefined ? [] : children; // 把 (children 全等于 undefined ? [] : children); 写入 this.children
  }
}
function buildNary(vals: any): any {
  // 定义函数/方法 buildNary
  if (vals === null || vals === undefined) return null; // 若 vals 全等于 null 或 vals 全等于 undefined，直接返回 null
  if (!Array.isArray(vals)) return new NNode(vals); // 若 取反 Array.isArray(vals)，直接返回 new NNode(vals)
  if (vals.length === 0) return null; // 若 vals.长度 全等于 0，直接返回 null
  const root = new NNode(vals[0]); // 把 new NNode(vals[0]) 存入 根节点
  for (let i = 1; i < vals.length; i++) root.children.push(buildNary(vals[i])); // 让 下标 i 从 1 开始计数，下标 i 小于 vals.长度 就继续
  return root; // 返回 根节点
}
function levelOrder(root: any): any[] {
  // 定义函数/方法 levelOrder
  const res: any[] = []; // 把 []; 写入 const res: any[]
  if (!root) return res; // 若 取反 根节点，直接返回 结果
  let q: any[] = [root]; // 把 [根节点]; 写入 let q: any[]
  while (q.length) {
    // 循环，直到不满足「节点.长度」
    const cur: any[] = [];
    const nq: any[] = []; // 把 []; const nq: any[] 赋值为 []; 写入 const cur: any[]
    for (const n of q) {
      cur.push(n.val);
      for (const c of n.children) nq.push(c);
    } // 把 元素个数.值 压入栈/数组尾部
    res.push(cur);
    q = nq; // 把 当前值 压入栈/数组尾部
  }
  return res; // 返回 结果
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases = [
    { in: [buildNary([1, [2], [3, 4]])], want: [[1], [2, 3], [4]] },
    { in: [buildNary([1, [2, 3], [4, 5]])], want: [[1], [2, 4], [3, 5]] },
    { in: [buildNary([1])], want: [[1]] },
    { in: [buildNary([])], want: [] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = levelOrder(...c.in); // 把 levelOrder(...字符.in) 存入 got
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
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
```

## 逐步拆解与面试追问

**复杂度**：时间 O(n²)（两层嵌套扫描），空间 O(1) 到 O(n)

**为什么是这个量级**：外层定起点、内层扫终点，n 个起点各扫 n 次

**面试官可能会追问**：

- 递归和迭代写法各自的空间开销？
- 能否用层序统一处理？
- 空节点的边界如何约定？

## 关键 API 速查（TS 主解法实际用到，附官方链接）

| API | 作用 | 使用要点 | 官方文档 |
|---|---|---|---|
| `Array.prototype.push()` | 尾部追加 | 返回新长度；可一次多个；均摊 O(1)；会改变原数组 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/push) |
| `Array.prototype.shift()` | 头部取出 | O(n)（后续元素整体前移）；大量头部操作请用链表或双端结构 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/shift) |
| `JSON.stringify()` | 序列化为 JSON 字符串 | 常用于结构化比较（深度相等判定）；undefined/函数/循环引用会被丢弃或抛错 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) |

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
> 完整解法文件见 `dsa/<语言>/tree/lc_429_n_叉树的层序遍历/`。

### Python 实现（2 种方案）

Python 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：双重循环枚举

**思路与代码分析**：核心是「双重循环枚举」。Python 版用切片与字典推导式简化操作，突出可读性。**走读**：方案 1 · 双重循环枚举：开始 → 命中条件，直接返回 → 更新 res → 更新 q → 当 q: 时反复执行 → 更新 level → 更新 nxt → 遍历 q: 中的每个元素 node → 向 level 追加记录 → 遍历 (node.children or []): 中的每个元素 child → 向 nxt 追加记录 → 向 res 追加记录 → 更新 q → 返回 res。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 双重循环枚举：开始"]
    N1{"not root ？"}
    N2["命中条件，直接返回"]
    N3["更新 res"]
    N4["更新 q"]
    N5["当 q: 时反复执行"]
    N6["更新 level"]
    N7["更新 nxt"]
    N8["遍历 q: 中的每个元素 node"]
    N9["向 level 追加记录"]
    N10["遍历 (node.children or []): 中的每个元素 child"]
    N11["向 nxt 追加记录"]
    N12["向 res 追加记录"]
    N13["更新 q"]
    N14["返回 res"]
    N0 --> N1
    N1 -- 是 --> N2
    N1 -- 否 --> N3
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
    N13 --> N14
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N3,N4,N6,N7,N9,N11,N12,N13 n;
    class N5,N8,N10 lp;
    class N1 dc;
    class N2,N14 tm;
```

```python
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级

def levelOrder(root):  # 定义函数 levelOrder（参数：N 叉树根节点）
    if not root:  # 空树返回
        return []
    res = []  # 结果
    q = [root]  # 队列
    while q:  # 逐层处理
        level = []  # 当前层值
        nxt = []  # 下一层节点
        for node in q:  # 遍历当前层
            level.append(node.val)
            for child in (node.children or []):  # 子节点入下一层
                nxt.append(child)
        res.append(level)
        q = nxt
    return res  # 返回 结果

if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(levelOrder(None))  # 打印输出
```

#### 方案 2：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Python 版用切片与字典推导式简化操作，突出可读性。**走读**：方案 2 · 迭代指针处理：开始 → 命中条件，直接返回 → 更新 res → 更新 q → 当 q: 时反复执行 → 更新 level → 更新 nxt → 遍历 q: 中的每个元素 node → 向 level 追加记录 → 遍历 node.children or []: 中的每个元素 child → 向 nxt 追加记录 → 向 res 追加记录 → 更新 q → 返回 res。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 迭代指针处理：开始"]
    N1{"not root ？"}
    N2["命中条件，直接返回"]
    N3["更新 res"]
    N4["更新 q"]
    N5["当 q: 时反复执行"]
    N6["更新 level"]
    N7["更新 nxt"]
    N8["遍历 q: 中的每个元素 node"]
    N9["向 level 追加记录"]
    N10["遍历 node.children or []: 中的每个元素 child"]
    N11["向 nxt 追加记录"]
    N12["向 res 追加记录"]
    N13["更新 q"]
    N14["返回 res"]
    N0 --> N1
    N1 -- 是 --> N2
    N1 -- 否 --> N3
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
    N13 --> N14
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N3,N4,N6,N7,N9,N11,N12,N13 n;
    class N5,N8,N10 lp;
    class N1 dc;
    class N2,N14 tm;
```

```python
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级

def levelOrder(
    root,
):  # 定义函数 levelOrder（参数：N 叉树根节点）：逐层取最大? 本题为层序遍历
    if not root:  # 空树返回
        return []
    res = []  # 结果
    q = [root]  # 队列
    while q:  # 逐层处理
        level = []  # 当前层值
        nxt = []  # 下一层节点
        for node in q:  # 遍历当前层
            level.append(node.val)
            for child in node.children or []:  # 子节点入下一层
                nxt.append(child)
        res.append(level)
        q = nxt
    return res  # 返回 结果

if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(levelOrder(None))  # 打印输出
```

### Go 实现（2 种方案）

Go 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：双重循环枚举

**思路与代码分析**：核心是「双重循环枚举」。Go 版用切片与多返回值惯用法，显式处理索引边界。**走读**：方案 1 · 双重循环枚举：开始 → 更新 : → 处理 if root == nil → 返回 res → 更新 : → 遍历循环 → 更新 : → 更新 : → 遍历循环 → 更新 : → 更新 q → 更新 row → 遍历 n.Children 的下标与元素 c → 更新 q → 更新 res → 返回 res。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 双重循环枚举：开始"]
    N1["更新 :"]
    N2["处理 if root == nil"]
    N3["返回 res"]
    N4["更新 :"]
    N5["遍历循环"]
    N6["更新 :"]
    N7["更新 :"]
    N8["遍历循环"]
    N9["更新 :"]
    N10["更新 q"]
    N11["更新 row"]
    N12["遍历 n.Children 的下标与元素 c"]
    N13["更新 q"]
    N14["更新 res"]
    N15["返回 res"]
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
    N13 -- 下一轮 --> N12
    N12 -- 下一轮 --> N8
    N8 --> N14
    N14 -- 下一轮 --> N5
    N5 --> N15
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,N2,N4,N6,N7,N9,N10,N11,N13,N14 n;
    class N5,N8,N12 lp;
    class N3,N15 tm;
```

```go
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

type NNode struct { // 定义类型
	Val      int      // Val int
	Children []*NNode // Children [] 乘 NNode
}

func levelOrder(root *NNode) [][]int { // 定义函数/方法 levelOrder
	res := [][]int{} // 把 [][]int{} 写入 res :
	if root == nil { // 若 根节点 等于 nil
		return res // 返回 结果
	}
	q := []*NNode{root} // 把 [] 乘 NNode{根节点} 写入 q :
	for len(q) > 0 {    // for 长度(节点) 超过 0 {
		size := len(q)              // 把 长度(节点) 写入 size :
		row := []int{}              // 把 []int{} 写入 row :
		for i := 0; i < size; i++ { // 让 下标 i 从 0 开始计数
			n := q[0]                      // 把 节点[0] 写入 n :
			q = q[1:]                      // 把 节点[1:] 写入 节点
			row = append(row, n.Val)       // 把 append(row, 元素个数.Val) 写入 row
			for _, c := range n.Children { // 同时取 _ 与 字符 遍历
				q = append(q, c) // 把 append(节点, 字符) 写入 节点
			}
		}
		res = append(res, row) // 把 append(结果, row) 写入 结果
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                                 // 把 true 写入 ok :
	if got := levelOrder(nil); len(got) != 0 { // 若 got : 赋值为 levelOrder(nil); 长度(got) 不等于 0
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL nil got=%v\n", got) // 打印输出
	}
	root := &NNode{Val: 1}                  // 把 按位与 NNode{Val: 1} 写入 root :
	c3 := &NNode{Val: 3}                    // 把 按位与 NNode{Val: 3} 写入 c3 :
	c2 := &NNode{Val: 2}                    // 把 按位与 NNode{Val: 2} 写入 c2 :
	c4 := &NNode{Val: 4}                    // 把 按位与 NNode{Val: 4} 写入 c4 :
	c5 := &NNode{Val: 5}                    // 把 按位与 NNode{Val: 5} 写入 c5 :
	c6 := &NNode{Val: 6}                    // 把 按位与 NNode{Val: 6} 写入 c6 :
	root.Children = []*NNode{c3, c2, c4}    // 把 [] 乘 NNode{c3, c2, c4} 写入 root.Children
	c3.Children = []*NNode{c5, c6}          // 把 [] 乘 NNode{c5, c6} 写入 c3.Children
	got := levelOrder(root)                 // 把 levelOrder(根节点) 写入 got :
	want := [][]int{{1}, {3, 2, 4}, {5, 6}} // 把 [][]int{{1}, {3, 2, 4}, {5, 6}} 写入 want :
	if !reflect.DeepEqual(got, want) {      // 若 取反 reflect.DeepEqual(got, want
		ok = false                                     // 把 false 写入 ok
		fmt.Printf("FAIL got=%v want=%v\n", got, want) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
```

#### 方案 2：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Go 版用切片与多返回值惯用法，显式处理索引边界。**走读**：方案 2 · 迭代指针处理：开始 → 处理 if root == nil → 返回 [][]int → 更新 : → 更新 : → 遍历循环 → 更新 : → 更新 : → 遍历循环 → 更新 : → 更新 q → 更新 lvl → 遍历 node.Children 的下标与元素 ch → 更新 q → 更新 res → 返回 res。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 迭代指针处理：开始"]
    N1["处理 if root == nil"]
    N2["返回 [][]int"]
    N3["更新 :"]
    N4["更新 :"]
    N5["遍历循环"]
    N6["更新 :"]
    N7["更新 :"]
    N8["遍历循环"]
    N9["更新 :"]
    N10["更新 q"]
    N11["更新 lvl"]
    N12["遍历 node.Children 的下标与元素 ch"]
    N13["更新 q"]
    N14["更新 res"]
    N15["返回 res"]
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
    N13 -- 下一轮 --> N12
    N12 -- 下一轮 --> N8
    N8 --> N14
    N14 -- 下一轮 --> N5
    N5 --> N15
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,N3,N4,N6,N7,N9,N10,N11,N13,N14 n;
    class N5,N8,N12 lp;
    class N2,N15 tm;
```

```go
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖
type Node struct {
	Val      int
	Children []*Node
} // 定义类型
func levelOrder(root *Node) [][]int { // 定义函数/方法 levelOrder
	if root == nil {
		return [][]int{}
	} // 若 根节点 等于 nil { return [][]int{} }
	res := [][]int{}
	q := []*Node{root} // 把 [][]int{}; 节点 : 赋值为 [] 乘 Node{根节点} 写入 res :
	for len(q) > 0 {   // for 长度(节点) 超过 0 {
		lvl := []int{}
		n := len(q)              // 把 []int{}; 元素个数 : 赋值为 长度(节点) 写入 lvl :
		for k := 0; k < n; k++ { // 让 下标 k 从 0 开始计数
			node := q[0]
			q = q[1:]
			lvl = append(lvl, node.Val)
			for _, ch := range node.Children {
				q = append(q, ch)
			} // 同时取 _ 与 字符 遍历
		}
		res = append(res, lvl) // 把 append(结果, lvl) 写入 结果
	}
	return res // 返回 结果
}
func main() { // 程序入口：跑内嵌自测用例
	c5 := &Node{Val: 5}
	c6 := &Node{Val: 6} // 把 按位与 Node{Val: 5}; c6 : 赋值为 按位与 Node{Val: 6} 写入 c5 :
	c3 := &Node{Val: 3, Children: []*Node{c5, c6}}
	c2 := &Node{Val: 2}
	c4 := &Node{Val: 4}
	root := &Node{Val: 1, Children: []*Node{c3, c2, c4}}
	if got := levelOrder(root); !reflect.DeepEqual(got, [][]int{{1}, {3, 2, 4}, {5, 6}}) {
		fmt.Println("FAIL", got)
		os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
```

### Java 实现（2 种方案）

Java 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：双重循环枚举

**思路与代码分析**：核心是「双重循环枚举」。Java 版用类与静态方法组织，集合操作显式明了。**走读**：方案 1 · 双重循环枚举：开始 → 返回 new ArrayList＜＞()。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 双重循环枚举：开始"]
    N1["返回 new ArrayList＜＞()"]
    N0 --> N1
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```java
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc429_solution_1_1_____1_______ { // 定义类型
  static class Node {
    int val;
    List<Node> children = new ArrayList<>();

    Node(int v) {
      val = v;
    }
  }

  public static List<List<Integer>> levelOrder(Node root) {
    return new ArrayList<>(); // 返回 new ArrayList 小于 超过 ()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<List<Integer>> got = levelOrder(null); // 把 levelOrder(null); 写入 List<List<Integer>> got
    if (!got.isEmpty()) {
      System.out.println("FAIL");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
```

#### 方案 2：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Java 版用类与静态方法组织，集合操作显式明了。**走读**：方案 2 · 迭代指针处理：开始 → 更新 val → 更新 children → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 迭代指针处理：开始"]
    N1["更新 val"]
    N2["更新 children"]
    N3["返回结果"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,N2 n;
    class N3 tm;
```

```java
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc429_solution_2_2_____2_____ { // 定义类型
  static class Node { // static class Node {
    int val; // int 值;
    List<Node> children; // List 小于 Node 超过 children;

    Node(int v) {
      val = v;
      children = new ArrayList<>();
    }
  }

  public List<List<Integer>> levelOrder(Node root) { // 定义函数/方法 levelOrder
    return new ArrayList<>(); // 返回 new ArrayList 小于 超过 ()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc429_solution_2_2_____2_____ s = new lc429_solution_2_2_____2_____();
    List<List<Integer>> got =
        s.levelOrder(null); // 把 字符串.levelOrder(null); 写入 List<List<Integer>> got
    if (!got.isEmpty()) {
      System.out.println("FAIL");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
```

### Rust 实现（2 种方案）

Rust 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：双重循环枚举

**思路与代码分析**：核心是「双重循环枚举」。Rust 版用所有权移动与切片借用改写同一逻辑，注意 Option 与引用边界。**走读**：方案 1 · 双重循环枚举：开始 → 计算 res → 当 非 q.is_empty() 时反复执行 → 遍历 q 中的每个元素 n → 遍历 &n.children 中的每个元素 c → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 双重循环枚举：开始"]
    N1["计算 res"]
    D1["……（中间计算步骤）"]
    N6["当 非 q.is_empty() 时反复执行"]
    D2["……（中间计算步骤）"]
    N9["遍历 q 中的每个元素 n"]
    D3["……（中间计算步骤）"]
    N11["遍历 &n.children 中的每个元素 c"]
    D4["……（中间计算步骤）"]
    N16["返回结果"]
    N0 --> N1
    N11 -- 下一轮 --> N9
    N1 --> D1
    D1 --> N6
    N6 --> D2
    D2 --> N9
    N9 --> D3
    D3 --> N11
    N11 --> D4
    D4 --> N16
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,D1,D2,D3,D4 n;
    class N6,N9,N11 lp;
    class N16 tm;
```

```rust
// LeetCode 429. N叉树的层序遍历 — Rust 版（方案1）
use std::cell::RefCell;
use std::rc::Rc; // 引入依赖 // 引入依赖

#[derive(Debug)]
struct TreeNode {
    // 定义类型
    val: i32,
    left: Option<Rc<RefCell<TreeNode>>>,
    right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    // 实现块
    fn new(val: i32) -> Rc<RefCell<TreeNode>> {
        // 定义函数/方法 new
        Rc::new(RefCell::new(TreeNode {
            val,
            left: None,
            right: None,
        })) // Rc::new(RefCell::new(TreeNode { 值, 左边界: None, 右边界: None }))
    }
}

fn build_tree(vals: &[Option<i32>]) -> Option<Rc<RefCell<TreeNode>>> {
    // 定义函数/方法 build_tree
    if vals.is_empty() || vals[0].is_none() {
        // 若 vals 是否为空 或 vals[0].is_none(
        return None; // 返回 None
    }
    let root = TreeNode::new(vals[0].unwrap()); // 把 TreeNode::new(vals[0].unwrap()) 存入 根节点
    let mut queue: Vec<Rc<RefCell<TreeNode>>> = vec![root.clone()];
    let mut i = 1; // 把 1; 写入 let mut i
    while !queue.is_empty() && i < vals.len() {
        // while 取反 队列 是否为空 且 下标 i 小于 vals.长度() {
        let node = queue.remove(0); // 把 队列 弹出 0) 存入 节点
        if i < vals.len() {
            // 若 下标 i 小于 vals.长度(
            if let Some(v) = vals[i] {
                // 若 let Some(值) 赋值为 vals[下标 i]
                let child = TreeNode::new(v); // 把 TreeNode::new(值) 存入 子节点
                node.borrow_mut().left = Some(child.clone()); // 把 Some(子节点.clone()); 写入 左边界
                queue.push(child); // 把 子节点 压入栈/数组尾部
            }
            i += 1; // 下标 i累加 1
        }
        if i < vals.len() {
            // 若 下标 i 小于 vals.长度(
            if let Some(v) = vals[i] {
                // 若 let Some(值) 赋值为 vals[下标 i]
                let child = TreeNode::new(v); // 把 TreeNode::new(值) 存入 子节点
                node.borrow_mut().right = Some(child.clone()); // 把 Some(子节点.clone()); 写入 右边界
                queue.push(child); // 把 子节点 压入栈/数组尾部
            }
            i += 1; // 下标 i累加 1
        }
    }
    Some(root) // Some(根节点)
}

struct Node {
    val: i32,
    children: Vec<Node>,
} // 定义类型
impl Node {
    fn new(v: i32) -> Node {
        Node {
            val: v,
            children: Vec::new(),
        }
    }
} // 定义函数/方法 new
fn level_order(root: Option<&Node>) -> Vec<Vec<i32>> {
    // 定义函数/方法 level_order
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    let root = match root {
        Some(x) => x,
        None => return res,
    };
    let mut q: Vec<&Node> = vec![root]; // 把 vec取反 [根节点]; 写入 let mut q: Vec<&Node>
    while !q.is_empty() {
        // while 取反 节点 是否为空 {
        let mut level = Vec::new(); // 把 Vec::new(); 写入 let mut level
        let mut nxt = Vec::new(); // 把 Vec::new(); 写入 let mut nxt
        for n in q {
            // 逐个取出 节点 的元素（元素个数）
            level.push(n.val); // 把 元素个数.值 压入栈/数组尾部
            for c in &n.children {
                nxt.push(c);
            } // 逐个取出 元素个数 的元素（字符）
        }
        res.push(level); // 把 level 压入栈/数组尾部
        q = nxt; // 把 nxt; 写入 节点
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut root = Node::new(1); // 把 Node::new(1); 写入 let mut root
    let mut c3 = Node::new(3); // 把 Node::new(3); 写入 let mut c3
    c3.children = vec![Node::new(5), Node::new(6)]; // 把 vec取反 [Node::new(5), Node::new(6)]; 写入 c3.children
    root.children = vec![c3, Node::new(2), Node::new(4)]; // 把 vec取反 [c3, Node::new(2), Node::new(4)]; 写入 root.children
    assert_eq!(
        level_order(Some(&root)),
        vec![vec![1], vec![3, 2, 4], vec![5, 6]]
    ); // 断言校验
    assert!(level_order(None).is_empty()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
```

#### 方案 2：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Rust 版用所有权移动与切片借用改写同一逻辑，注意 Option 与引用边界。**走读**：方案 2 · 迭代指针处理：开始 → 计算 res → 当 非 q.is_empty() 时反复执行 → 遍历 q 中的每个元素 n → 遍历 &n.children 中的每个元素 c → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 迭代指针处理：开始"]
    N1["计算 res"]
    D1["……（中间计算步骤）"]
    N6["当 非 q.is_empty() 时反复执行"]
    D2["……（中间计算步骤）"]
    N9["遍历 q 中的每个元素 n"]
    D3["……（中间计算步骤）"]
    N11["遍历 &n.children 中的每个元素 c"]
    D4["……（中间计算步骤）"]
    N16["返回结果"]
    N0 --> N1
    N11 -- 下一轮 --> N9
    N1 --> D1
    D1 --> N6
    N6 --> D2
    D2 --> N9
    N9 --> D3
    D3 --> N11
    N11 --> D4
    D4 --> N16
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,D1,D2,D3,D4 n;
    class N6,N9,N11 lp;
    class N16 tm;
```

```rust
// LeetCode 429. N叉树的层序遍历 — Rust 版（方案2）
use std::cell::RefCell;
use std::rc::Rc; // 引入依赖 // 引入依赖

#[derive(Debug)]
struct TreeNode {
    // 定义类型
    val: i32,
    left: Option<Rc<RefCell<TreeNode>>>,
    right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    // 实现块
    fn new(val: i32) -> Rc<RefCell<TreeNode>> {
        // 定义函数/方法 new
        Rc::new(RefCell::new(TreeNode {
            val,
            left: None,
            right: None,
        })) // Rc::new(RefCell::new(TreeNode { 值, 左边界: None, 右边界: None }))
    }
}

fn build_tree(vals: &[Option<i32>]) -> Option<Rc<RefCell<TreeNode>>> {
    // 定义函数/方法 build_tree
    if vals.is_empty() || vals[0].is_none() {
        // 若 vals 是否为空 或 vals[0].is_none(
        return None; // 返回 None
    }
    let root = TreeNode::new(vals[0].unwrap()); // 把 TreeNode::new(vals[0].unwrap()) 存入 根节点
    let mut queue: Vec<Rc<RefCell<TreeNode>>> = vec![root.clone()];
    let mut i = 1; // 把 1; 写入 let mut i
    while !queue.is_empty() && i < vals.len() {
        // while 取反 队列 是否为空 且 下标 i 小于 vals.长度() {
        let node = queue.remove(0); // 把 队列 弹出 0) 存入 节点
        if i < vals.len() {
            // 若 下标 i 小于 vals.长度(
            if let Some(v) = vals[i] {
                // 若 let Some(值) 赋值为 vals[下标 i]
                let child = TreeNode::new(v); // 把 TreeNode::new(值) 存入 子节点
                node.borrow_mut().left = Some(child.clone()); // 把 Some(子节点.clone()); 写入 左边界
                queue.push(child); // 把 子节点 压入栈/数组尾部
            }
            i += 1; // 下标 i累加 1
        }
        if i < vals.len() {
            // 若 下标 i 小于 vals.长度(
            if let Some(v) = vals[i] {
                // 若 let Some(值) 赋值为 vals[下标 i]
                let child = TreeNode::new(v); // 把 TreeNode::new(值) 存入 子节点
                node.borrow_mut().right = Some(child.clone()); // 把 Some(子节点.clone()); 写入 右边界
                queue.push(child); // 把 子节点 压入栈/数组尾部
            }
            i += 1; // 下标 i累加 1
        }
    }
    Some(root) // Some(根节点)
}

struct Node {
    val: i32,
    children: Vec<Node>,
} // 定义类型
impl Node {
    fn new(v: i32) -> Node {
        Node {
            val: v,
            children: Vec::new(),
        }
    }
} // 定义函数/方法 new
fn level_order(root: Option<&Node>) -> Vec<Vec<i32>> {
    // 定义函数/方法 level_order
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    let root = match root {
        Some(x) => x,
        None => return res,
    };
    let mut q: Vec<&Node> = vec![root]; // 把 vec取反 [根节点]; 写入 let mut q: Vec<&Node>
    while !q.is_empty() {
        // while 取反 节点 是否为空 {
        let mut level = Vec::new(); // 把 Vec::new(); 写入 let mut level
        let mut nxt = Vec::new(); // 把 Vec::new(); 写入 let mut nxt
        for n in q {
            // 逐个取出 节点 的元素（元素个数）
            level.push(n.val); // 把 元素个数.值 压入栈/数组尾部
            for c in &n.children {
                nxt.push(c);
            } // 逐个取出 元素个数 的元素（字符）
        }
        res.push(level); // 把 level 压入栈/数组尾部
        q = nxt; // 把 nxt; 写入 节点
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut root = Node::new(1); // 把 Node::new(1); 写入 let mut root
    let mut c3 = Node::new(3); // 把 Node::new(3); 写入 let mut c3
    c3.children = vec![Node::new(5), Node::new(6)]; // 把 vec取反 [Node::new(5), Node::new(6)]; 写入 c3.children
    root.children = vec![c3, Node::new(2), Node::new(4)]; // 把 vec取反 [c3, Node::new(2), Node::new(4)]; 写入 root.children
    assert_eq!(
        level_order(Some(&root)),
        vec![vec![1], vec![3, 2, 4], vec![5, 6]]
    ); // 断言校验
    assert!(level_order(None).is_empty()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
```

### Lua 实现（2 种方案）

Lua 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：双重循环枚举

**思路与代码分析**：核心是「双重循环枚举」。Lua 版用表与 ipairs 遍历，注意 ipairs 遇 nil 即停的语义。**走读**：方案 1 · 双重循环枚举：开始 → 处理 if not vals or #vals == 0 or → 返回 nil → 当 head ≤ #queue and i ≤ #vals do 时反复执行 → 返回 root。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 双重循环枚举：开始"]
    N1["处理 if not vals or #vals == 0 or"]
    N2["返回 nil"]
    D1["……（中间计算步骤）"]
    N7["当 head ≤ #queue and i ≤ #vals do 时反复执行"]
    D2["……（中间计算步骤）"]
    N20["返回 root"]
    N0 --> N1
    N1 --> N2
    N2 --> D1
    D1 --> N7
    N7 --> D2
    D2 --> N20
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,D1,D2 n;
    class N7 lp;
    class N2,N20 tm;
```

```lua
-- LeetCode 429. N叉树的层序遍历 — Lua 版（方案1）
local TreeNode = {} -- 把 {} 写入 local TreeNode
TreeNode.__index = TreeNode -- 把 TreeNode 写入 TreeNode.__index
function TreeNode.new(val) -- function TreeNode.new(值)
	return setmetatable({ val = val, left = nil, right = nil }, TreeNode)
end -- 终点

local function build_tree(vals) -- local function build_tree(vals)
	if not vals or #vals == 0 or vals[1] == "null" then
		return nil
	end
	local root = TreeNode.new(vals[1]) -- 把 TreeNode.new(vals[1]) 写入 local root
	local queue = { root } -- 把 {根节点} 写入 local queue
	local head = 1 -- 把 1 写入 local head
	local i = 2 -- 把 2 写入 local i
	while head <= #queue and i <= #vals do -- 把 #队列 and 下标 i 不超过 #vals do 写入 while head <
		local node = queue[head] -- 把 队列[头节点] 写入 local node
		head = head + 1 -- 把 头节点 加 1 存入 头节点
		if i <= #vals then -- 若 下标 i 不超过 #vals then
			if vals[i] ~= "null" then -- 若 vals[下标 i] ~ 赋值为 「null」 then
				node.left = TreeNode.new(vals[i]) -- 把 TreeNode.new(vals[下标 i]) 写入 左边界
				queue[#queue + 1] = node.left -- 把 节点.左边界 写入 queue[#queue + 1]
			end -- 终点
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
		if i <= #vals then -- 若 下标 i 不超过 #vals then
			if vals[i] ~= "null" then -- 若 vals[下标 i] ~ 赋值为 「null」 then
				node.right = TreeNode.new(vals[i]) -- 把 TreeNode.new(vals[下标 i]) 写入 右边界
				queue[#queue + 1] = node.right -- 把 节点.右边界 写入 queue[#queue + 1]
			end -- 终点
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
	end -- 终点
	return root -- 返回 根节点
end -- 终点

local function new_node(v)
	return { val = v, children = {} }
end
local function level_order(root) -- local function level_order(根节点)
	if not root then
		return {}
	end -- 若 not 根节点 then return {} 终点
	local res = {} -- 把 {} 写入 local res
	local q = { root } -- 把 {根节点} 写入 local q
	while #q > 0 do -- while #节点 超过 0 do
		local level = {} -- 把 {} 写入 local level
		local nxt = {} -- 把 {} 写入 local nxt
		for i = 1, #q do -- 把 1, #节点 do 写入 for i
			local n = q[i] -- 把 节点[下标 i] 写入 local n
			level[#level + 1] = n.val -- 把 元素个数.值 写入 level[#level + 1]
			for _, c in ipairs(n.children) do
				nxt[#nxt + 1] = c
			end -- 遍历取 字符
		end -- 终点
		res[#res + 1] = level -- 把 level 写入 res[#res + 1]
		q = nxt -- 把 nxt 存入 节点
	end -- 终点
	return res -- 返回 结果
end -- 终点
local root = new_node(1) -- 把 new_node(1) 写入 local root
local c3 = new_node(3) -- 把 new_node(3) 写入 local c3
c3.children = { new_node(5), new_node(6) } -- 把 {new_node(5), new_node(6)} 写入 c3.children
root.children = { c3, new_node(2), new_node(4) } -- 把 {c3, new_node(2), new_node(4)} 写入 root.children
local a = level_order(root) -- 把 level_order(根节点) 写入 local a
assert(#a == 3 and a[1][1] == 1 and a[2][1] == 3 and a[2][2] == 2 and a[2][3] == 4 and a[3][1] == 5 and a[3][2] == 6) -- 断言校验
assert(#level_order(nil) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
```

#### 方案 2：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Lua 版用表与 ipairs 遍历，注意 ipairs 遇 nil 即停的语义。**走读**：方案 2 · 迭代指针处理：开始 → 处理 if not vals or #vals == 0 or → 返回 nil → 当 head ≤ #queue and i ≤ #vals do 时反复执行 → 返回 root。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 迭代指针处理：开始"]
    N1["处理 if not vals or #vals == 0 or"]
    N2["返回 nil"]
    D1["……（中间计算步骤）"]
    N7["当 head ≤ #queue and i ≤ #vals do 时反复执行"]
    D2["……（中间计算步骤）"]
    N20["返回 root"]
    N0 --> N1
    N1 --> N2
    N2 --> D1
    D1 --> N7
    N7 --> D2
    D2 --> N20
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,D1,D2 n;
    class N7 lp;
    class N2,N20 tm;
```

```lua
-- LeetCode 429. N叉树的层序遍历 — Lua 版（方案2）
local TreeNode = {} -- 把 {} 写入 local TreeNode
TreeNode.__index = TreeNode -- 把 TreeNode 写入 TreeNode.__index
function TreeNode.new(val) -- function TreeNode.new(值)
	return setmetatable({ val = val, left = nil, right = nil }, TreeNode)
end -- 终点

local function build_tree(vals) -- local function build_tree(vals)
	if not vals or #vals == 0 or vals[1] == "null" then
		return nil
	end
	local root = TreeNode.new(vals[1]) -- 把 TreeNode.new(vals[1]) 写入 local root
	local queue = { root } -- 把 {根节点} 写入 local queue
	local head = 1 -- 把 1 写入 local head
	local i = 2 -- 把 2 写入 local i
	while head <= #queue and i <= #vals do -- 把 #队列 and 下标 i 不超过 #vals do 写入 while head <
		local node = queue[head] -- 把 队列[头节点] 写入 local node
		head = head + 1 -- 把 头节点 加 1 存入 头节点
		if i <= #vals then -- 若 下标 i 不超过 #vals then
			if vals[i] ~= "null" then -- 若 vals[下标 i] ~ 赋值为 「null」 then
				node.left = TreeNode.new(vals[i]) -- 把 TreeNode.new(vals[下标 i]) 写入 左边界
				queue[#queue + 1] = node.left -- 把 节点.左边界 写入 queue[#queue + 1]
			end -- 终点
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
		if i <= #vals then -- 若 下标 i 不超过 #vals then
			if vals[i] ~= "null" then -- 若 vals[下标 i] ~ 赋值为 「null」 then
				node.right = TreeNode.new(vals[i]) -- 把 TreeNode.new(vals[下标 i]) 写入 右边界
				queue[#queue + 1] = node.right -- 把 节点.右边界 写入 queue[#queue + 1]
			end -- 终点
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
	end -- 终点
	return root -- 返回 根节点
end -- 终点

local function new_node(v)
	return { val = v, children = {} }
end
local function level_order(root) -- local function level_order(根节点)
	if not root then
		return {}
	end -- 若 not 根节点 then return {} 终点
	local res = {} -- 把 {} 写入 local res
	local q = { root } -- 把 {根节点} 写入 local q
	while #q > 0 do -- while #节点 超过 0 do
		local level = {} -- 把 {} 写入 local level
		local nxt = {} -- 把 {} 写入 local nxt
		for i = 1, #q do -- 把 1, #节点 do 写入 for i
			local n = q[i] -- 把 节点[下标 i] 写入 local n
			level[#level + 1] = n.val -- 把 元素个数.值 写入 level[#level + 1]
			for _, c in ipairs(n.children) do
				nxt[#nxt + 1] = c
			end -- 遍历取 字符
		end -- 终点
		res[#res + 1] = level -- 把 level 写入 res[#res + 1]
		q = nxt -- 把 nxt 存入 节点
	end -- 终点
	return res -- 返回 结果
end -- 终点
local root = new_node(1) -- 把 new_node(1) 写入 local root
local c3 = new_node(3) -- 把 new_node(3) 写入 local c3
c3.children = { new_node(5), new_node(6) } -- 把 {new_node(5), new_node(6)} 写入 c3.children
root.children = { c3, new_node(2), new_node(4) } -- 把 {c3, new_node(2), new_node(4)} 写入 root.children
local a = level_order(root) -- 把 level_order(根节点) 写入 local a
assert(#a == 3 and a[1][1] == 1 and a[2][1] == 3 and a[2][2] == 2 and a[2][3] == 4 and a[3][1] == 5 and a[3][2] == 6) -- 断言校验
assert(#level_order(nil) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
```

### C 实现（2 种方案）

C 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：双重循环枚举

**思路与代码分析**：核心是「双重循环枚举」。C 版手动管理下标与内存，循环边界全部显式写出。**走读**：方案 1 · 双重循环枚举：开始 → 更新 *n → 更新 n->val → 返回 n。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 双重循环枚举：开始"]
    N1["更新 *n"]
    N2["更新 n->val"]
    N3["返回 n"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,N2 n;
    class N3 tm;
```

```c
/* LeetCode 429. N叉树的层序遍历 — C 版（方案1） */
#include <stdio.h>                   // 引入头文件
#include <stdlib.h>                  // 引入头文件
#define INT_MIN_SN (-2147483647 - 1) // #define INT_MIN_SN ( 减 2147483647 减 1)

typedef struct TreeNode {   // typedef struct TreeNode {
    int val;                // int 值;
    struct TreeNode *left;  // 定义类型
    struct TreeNode *right; // 定义类型
} TreeNode;                 // } TreeNode;

static TreeNode *build_tree(const int *vals,
                            int n) { // static TreeNode 乘 build_tree(const int 乘 vals, int 元素个数) {
    if (n == 0 || vals[0] == INT_MIN_SN)
        return NULL; // 若 元素个数 等于 0 或 vals[0] 等于 INT_MIN_SN，直接返回 NULL
    TreeNode *root = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 TreeNode *root
    root->val = vals[0];
    root->left = root->right = NULL;
    TreeNode **queue =
        malloc(sizeof(TreeNode *) * n); // 把 malloc(sizeof(TreeNode 乘 ) 乘 元素个数); 写入 TreeNode **queue
    int head = 0, tail = 0, i = 1; // 把 0, 尾节点 赋值为 0, 下标 i 赋值为 1 存入 头节点
    queue[tail++] = root;          // 把 根节点; 写入 queue[tail++]
    while (head < tail && i < n) { // 循环，直到不满足「头节点 小于 尾节点 且 下标 i 小于 元素个数」
        TreeNode *node = queue[head++];                // 把 队列[头节点 加一 ]; 写入 TreeNode *node
        if (i < n) {                                   // 若 下标 i 小于 元素个数
            if (vals[i] != INT_MIN_SN) {               // 若 vals[下标 i] 不等于 INT_MIN_SN
                node->left = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 node->left
                node->left->val = vals[i];
                node->left->left = node->left->right = NULL;
                queue[tail++] = node->left; // 把 节点 减 超过 左边界; 写入 queue[tail++]
            }
            i++; // 下标 i 加一
        }
        if (i < n) {                                    // 若 下标 i 小于 元素个数
            if (vals[i] != INT_MIN_SN) {                // 若 vals[下标 i] 不等于 INT_MIN_SN
                node->right = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 node->right
                node->right->val = vals[i];
                node->right->left = node->right->right = NULL;
                queue[tail++] = node->right; // 把 节点 减 超过 右边界; 写入 queue[tail++]
            }
            i++; // 下标 i 加一
        }
    }
    free(queue); // free(队列);
    return root; // 返回 根节点
}

static void free_tree(TreeNode *n) { // 定义函数/方法 free_tree
    if (!n)
        return;          // 若 取反 元素个数) return;
    free_tree(n->left);  // free_tree(元素个数 减 超过 左边界);
    free_tree(n->right); // free_tree(元素个数 减 超过 右边界);
    free(n);             // free(元素个数);
}

typedef struct NNode {
    int val;
    struct NNode *children[16];
    int nch;
} NNode;
static NNode *nnew(int v) {              // static NNode 乘 nnew(int 值) {
    NNode *n = calloc(1, sizeof(NNode)); // 把 calloc(1, sizeof(NNode)); 写入 NNode *n
    n->val = v;                          // 把 值; 写入 n->val
    return n;                            // 返回 元素个数
}
static int level_order(NNode *root, int out[][64], int sizes[]) { // 定义函数/方法 level_order
    if (!root)
        return 0;                        // 若 取反 根节点，直接返回 0
    NNode *q[256];                       // NNode 乘 节点[256];
    int head = 0, tail = 0, nl = 0;      // 把 0, 尾节点 赋值为 0, nl 赋值为 0 存入 头节点
    q[tail++] = root;                    // 把 根节点; 写入 q[tail++]
    while (head < tail) {                // 循环，直到不满足「头节点 小于 尾节点」
        int size = tail - head, cnt = 0; // 把 尾节点 减 头节点, 计数 赋值为 0 存入 大小
        for (int i = 0; i < size; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
            NNode *n = q[head++];        // 把 节点[头节点 加一 ]; 写入 NNode *n
            out[nl][cnt++] = n->val;     // 把 元素个数 减 超过 值; 写入 out[nl][cnt++]
            for (int k = 0; k < n->nch; k++)
                q[tail++] =
                    n->children[k]; // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 减 超过 nch 就继续
        }
        sizes[nl++] = cnt; // 把 计数; 写入 sizes[nl++]
    }
    return nl; // 返回 nl
}
int main(void) {                           // 程序入口：跑内嵌自测用例
    NNode *root = nnew(1), *c3 = nnew(3);  // 把 nnew(1), 乘 c3 赋值为 nnew(3); 写入 NNode *root
    c3->children[c3->nch++] = nnew(5);     // 把 nnew(5); 写入 c3->children[c3->nch++]
    c3->children[c3->nch++] = nnew(6);     // 把 nnew(6); 写入 c3->children[c3->nch++]
    root->children[root->nch++] = c3;      // 把 c3; 写入 root->children[root->nch++]
    root->children[root->nch++] = nnew(2); // 把 nnew(2); 写入 root->children[root->nch++]
    root->children[root->nch++] = nnew(4); // 把 nnew(4); 写入 root->children[root->nch++]
    int out[64][64], sizes[64];            // int out[64][64], sizes[64];
    int n = level_order(root, out, sizes); // 把 level_order(根节点, out, sizes) 存入 元素个数
    if (n != 3 || sizes[0] != 1 || sizes[1] != 3 || sizes[2] != 2) {
        printf("FAIL shape\n");
        return 1;
    }
    if (out[0][0] != 1 || out[1][0] != 3 || out[1][1] != 2 || out[1][2] != 4 || out[2][0] != 5 ||
        out[2][1] != 6) {
        printf("FAIL vals\n");
        return 1;
    }
    if (level_order(NULL, out, sizes) != 0) {
        printf("FAIL nil\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
```

#### 方案 2：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。C 版手动管理下标与内存，循环边界全部显式写出。**走读**：方案 2 · 迭代指针处理：开始 → 更新 *n → 更新 n->val → 返回 n。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 迭代指针处理：开始"]
    N1["更新 *n"]
    N2["更新 n->val"]
    N3["返回 n"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,N2 n;
    class N3 tm;
```

```c
/* LeetCode 429. N叉树的层序遍历 — C 版（方案2） */
#include <stdio.h>                   // 引入头文件
#include <stdlib.h>                  // 引入头文件
#define INT_MIN_SN (-2147483647 - 1) // #define INT_MIN_SN ( 减 2147483647 减 1)

typedef struct TreeNode {   // typedef struct TreeNode {
    int val;                // int 值;
    struct TreeNode *left;  // 定义类型
    struct TreeNode *right; // 定义类型
} TreeNode;                 // } TreeNode;

static TreeNode *build_tree(const int *vals,
                            int n) { // static TreeNode 乘 build_tree(const int 乘 vals, int 元素个数) {
    if (n == 0 || vals[0] == INT_MIN_SN)
        return NULL; // 若 元素个数 等于 0 或 vals[0] 等于 INT_MIN_SN，直接返回 NULL
    TreeNode *root = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 TreeNode *root
    root->val = vals[0];
    root->left = root->right = NULL;
    TreeNode **queue =
        malloc(sizeof(TreeNode *) * n); // 把 malloc(sizeof(TreeNode 乘 ) 乘 元素个数); 写入 TreeNode **queue
    int head = 0, tail = 0, i = 1; // 把 0, 尾节点 赋值为 0, 下标 i 赋值为 1 存入 头节点
    queue[tail++] = root;          // 把 根节点; 写入 queue[tail++]
    while (head < tail && i < n) { // 循环，直到不满足「头节点 小于 尾节点 且 下标 i 小于 元素个数」
        TreeNode *node = queue[head++];                // 把 队列[头节点 加一 ]; 写入 TreeNode *node
        if (i < n) {                                   // 若 下标 i 小于 元素个数
            if (vals[i] != INT_MIN_SN) {               // 若 vals[下标 i] 不等于 INT_MIN_SN
                node->left = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 node->left
                node->left->val = vals[i];
                node->left->left = node->left->right = NULL;
                queue[tail++] = node->left; // 把 节点 减 超过 左边界; 写入 queue[tail++]
            }
            i++; // 下标 i 加一
        }
        if (i < n) {                                    // 若 下标 i 小于 元素个数
            if (vals[i] != INT_MIN_SN) {                // 若 vals[下标 i] 不等于 INT_MIN_SN
                node->right = malloc(sizeof(TreeNode)); // 把 malloc(sizeof(TreeNode)); 写入 node->right
                node->right->val = vals[i];
                node->right->left = node->right->right = NULL;
                queue[tail++] = node->right; // 把 节点 减 超过 右边界; 写入 queue[tail++]
            }
            i++; // 下标 i 加一
        }
    }
    free(queue); // free(队列);
    return root; // 返回 根节点
}

static void free_tree(TreeNode *n) { // 定义函数/方法 free_tree
    if (!n)
        return;          // 若 取反 元素个数) return;
    free_tree(n->left);  // free_tree(元素个数 减 超过 左边界);
    free_tree(n->right); // free_tree(元素个数 减 超过 右边界);
    free(n);             // free(元素个数);
}

typedef struct NNode {
    int val;
    struct NNode *children[16];
    int nch;
} NNode;
static NNode *nnew(int v) {              // static NNode 乘 nnew(int 值) {
    NNode *n = calloc(1, sizeof(NNode)); // 把 calloc(1, sizeof(NNode)); 写入 NNode *n
    n->val = v;                          // 把 值; 写入 n->val
    return n;                            // 返回 元素个数
}
static int level_order(NNode *root, int out[][64], int sizes[]) { // 定义函数/方法 level_order
    if (!root)
        return 0;                        // 若 取反 根节点，直接返回 0
    NNode *q[256];                       // NNode 乘 节点[256];
    int head = 0, tail = 0, nl = 0;      // 把 0, 尾节点 赋值为 0, nl 赋值为 0 存入 头节点
    q[tail++] = root;                    // 把 根节点; 写入 q[tail++]
    while (head < tail) {                // 循环，直到不满足「头节点 小于 尾节点」
        int size = tail - head, cnt = 0; // 把 尾节点 减 头节点, 计数 赋值为 0 存入 大小
        for (int i = 0; i < size; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
            NNode *n = q[head++];        // 把 节点[头节点 加一 ]; 写入 NNode *n
            out[nl][cnt++] = n->val;     // 把 元素个数 减 超过 值; 写入 out[nl][cnt++]
            for (int k = 0; k < n->nch; k++)
                q[tail++] =
                    n->children[k]; // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 减 超过 nch 就继续
        }
        sizes[nl++] = cnt; // 把 计数; 写入 sizes[nl++]
    }
    return nl; // 返回 nl
}
int main(void) {                           // 程序入口：跑内嵌自测用例
    NNode *root = nnew(1), *c3 = nnew(3);  // 把 nnew(1), 乘 c3 赋值为 nnew(3); 写入 NNode *root
    c3->children[c3->nch++] = nnew(5);     // 把 nnew(5); 写入 c3->children[c3->nch++]
    c3->children[c3->nch++] = nnew(6);     // 把 nnew(6); 写入 c3->children[c3->nch++]
    root->children[root->nch++] = c3;      // 把 c3; 写入 root->children[root->nch++]
    root->children[root->nch++] = nnew(2); // 把 nnew(2); 写入 root->children[root->nch++]
    root->children[root->nch++] = nnew(4); // 把 nnew(4); 写入 root->children[root->nch++]
    int out[64][64], sizes[64];            // int out[64][64], sizes[64];
    int n = level_order(root, out, sizes); // 把 level_order(根节点, out, sizes) 存入 元素个数
    if (n != 3 || sizes[0] != 1 || sizes[1] != 3 || sizes[2] != 2) {
        printf("FAIL shape\n");
        return 1;
    }
    if (out[0][0] != 1 || out[1][0] != 3 || out[1][1] != 2 || out[1][2] != 4 || out[2][0] != 5 ||
        out[2][1] != 6) {
        printf("FAIL vals\n");
        return 1;
    }
    if (level_order(NULL, out, sizes) != 0) {
        printf("FAIL nil\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
```

### C++ 实现（2 种方案）

C++ 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：双重循环枚举

**思路与代码分析**：核心是「双重循环枚举」。C++ 版用 STL 容器与迭代器，减少手写下标错误。代码里依次做这些事：双重循环遍历；栈的后进先出操作。**走读**：方案 1 · 双重循环枚举：开始 → 处理 std::vector＜std::vector＜int＞ → 命中条件，直接返回 → 当 (非 q.empty()) 时反复执行 → 遍历循环 → 遍历循环 → 返回 res。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 双重循环枚举：开始"]
    N1["处理 std::vector＜std::vector＜int＞"]
    N2{"非 root ？"}
    N3["命中条件，直接返回"]
    D1["……（中间计算步骤）"]
    N6["当 (非 q.empty()) 时反复执行"]
    D2["……（中间计算步骤）"]
    N9["遍历循环"]
    D3["……（中间计算步骤）"]
    N13["遍历循环"]
    D4["……（中间计算步骤）"]
    N16["返回 res"]
    N0 --> N1
    N1 --> N2
    N2 -- 是 --> N3
    N6 --> N16
    N3 --> D1
    D1 --> N6
    N6 --> D2
    D2 --> N9
    N9 --> D3
    D3 --> N13
    N13 --> D4
    D4 --> N16
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,D1,D2,D3,D4 n;
    class N6,N9,N13 lp;
    class N2 dc;
    class N3,N16 tm;
```

```cpp
// LeetCode 429. N叉树的层序遍历 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <cstdint>  // 引入头文件
#include <iostream> // 引入头文件
#include <optional> // 引入头文件
#include <queue>    // 引入头文件
#include <vector>   // 引入头文件

struct TreeNode {    // 定义类型
    int val;         // int 值;
    TreeNode *left;  // TreeNode 乘 左边界;
    TreeNode *right; // TreeNode 乘 右边界;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

static TreeNode *build_tree(const std::vector<std::optional<int>> &vals) {
    if (vals.empty() || !vals[0].has_value())
        return nullptr; // 若 vals 是否为空 或 取反 vals[0].has_value()，直接返回 nullptr
    auto *root = new TreeNode(*vals[0]); // 把 new TreeNode( 乘 vals[0]); 写入 auto *root
    std::queue<TreeNode *> q;            // std::队列 小于 TreeNode 乘 超过 节点;
    q.push(root);                        // 把 根节点 压入栈/数组尾部
    size_t i = 1;                        // 把 1; 写入 size_t i
    while (!q.empty() &&
           i < vals.size()) { // 循环，直到不满足「取反 节点 是否为空 且 下标 i 小于 vals.大小(」
        TreeNode *node = q.front();                  // 把 节点.front(); 写入 TreeNode *node
        q.pop();                                     // 弹出栈顶元素
        if (i < vals.size()) {                       // 若 下标 i 小于 vals.大小(
            if (vals[i].has_value()) {               // 若 vals[下标 i].has_value(
                node->left = new TreeNode(*vals[i]); // 把 new TreeNode( 乘 vals[下标 i]); 写入 node->left
                q.push(node->left);                  // 把 节点 减 超过 左边界 压入栈/数组尾部
            }
            ++i; // 加一 下标 i;
        }
        if (i < vals.size()) {                        // 若 下标 i 小于 vals.大小(
            if (vals[i].has_value()) {                // 若 vals[下标 i].has_value(
                node->right = new TreeNode(*vals[i]); // 把 new TreeNode( 乘 vals[下标 i]); 写入 node->right
                q.push(node->right); // 把 节点 减 超过 右边界 压入栈/数组尾部
            }
            ++i; // 加一 下标 i;
        }
    }
    return root; // 返回 根节点
}

static void free_tree(TreeNode *n) { // 定义函数/方法 free_tree
    if (!n)
        return;          // 若 取反 元素个数) return;
    free_tree(n->left);  // free_tree(元素个数 减 超过 左边界);
    free_tree(n->right); // free_tree(元素个数 减 超过 右边界);
    delete n;            // delete 元素个数;
}

struct NNode {                        // 定义类型
    int val;                          // int 值;
    std::vector<NNode *> children;    // std::vector 小于 NNode 乘 超过 children;
    explicit NNode(int v) : val(v) {} // explicit NNode(int 值) : 值(值) {}
};
static std::vector<std::vector<int>> levelOrder(NNode *root) {
    std::vector<std::vector<int>> res; // std::vector 小于 std::vector 小于 int 超过 超过 结果;
    if (!root)
        return res;                            // 若 取反 根节点，直接返回 结果
    std::queue<NNode *> q;                     // std::队列 小于 NNode 乘 超过 节点;
    q.push(root);                              // 把 根节点 压入栈/数组尾部
    while (!q.empty()) {                       // 循环，直到不满足「取反 节点.empty(」
        int size = static_cast<int>(q.size()); // 把 static_cast 小于 int 超过 (节点.大小()) 存入 大小
        std::vector<int> level;                // std::vector 小于 int 超过 level;
        for (int i = 0; i < size; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
            auto *n = q.front();         // 把 节点.front(); 写入 auto *n
            q.pop();                     // 弹出栈顶元素
            level.push_back(n->val);     // level 追加 元素个数 减 超过 值);
            for (auto *c : n->children)
                q.push(c); // 把 字符 压入栈/数组尾部
        }
        res.push_back(std::move(level)); // 结果 追加 std::move(level));
    }
    return res; // 返回 结果
}
int main() {                                     // 程序入口：跑内嵌自测用例
    auto *root = new NNode(1);                   // 把 new NNode(1); 写入 auto *root
    auto *c3 = new NNode(3);                     // 把 new NNode(3); 写入 auto *c3
    c3->children = {new NNode(5), new NNode(6)}; // 把 {new NNode(5), new NNode(6)}; 写入 c3->children
    root->children = {c3, new NNode(2),
                      new NNode(4)}; // 把 {c3, new NNode(2), new NNode(4)}; 写入 root->children
    assert((levelOrder(root) == std::vector<std::vector<int>>{{1}, {3, 2, 4}, {5, 6}})); // 断言校验
    assert(levelOrder(nullptr).empty());                                                 // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
```

#### 方案 2：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。C++ 版用 STL 容器与迭代器，减少手写下标错误。代码里依次做这些事：双重循环遍历；栈的后进先出操作。**走读**：方案 2 · 迭代指针处理：开始 → 处理 std::vector＜std::vector＜int＞ → 命中条件，直接返回 → 当 (非 q.empty()) 时反复执行 → 遍历循环 → 遍历循环 → 返回 res。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 迭代指针处理：开始"]
    N1["处理 std::vector＜std::vector＜int＞"]
    N2{"非 root ？"}
    N3["命中条件，直接返回"]
    D1["……（中间计算步骤）"]
    N6["当 (非 q.empty()) 时反复执行"]
    D2["……（中间计算步骤）"]
    N9["遍历循环"]
    D3["……（中间计算步骤）"]
    N13["遍历循环"]
    D4["……（中间计算步骤）"]
    N16["返回 res"]
    N0 --> N1
    N1 --> N2
    N2 -- 是 --> N3
    N6 --> N16
    N3 --> D1
    D1 --> N6
    N6 --> D2
    D2 --> N9
    N9 --> D3
    D3 --> N13
    N13 --> D4
    D4 --> N16
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,D1,D2,D3,D4 n;
    class N6,N9,N13 lp;
    class N2 dc;
    class N3,N16 tm;
```

```cpp
// LeetCode 429. N叉树的层序遍历 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <cstdint>  // 引入头文件
#include <iostream> // 引入头文件
#include <optional> // 引入头文件
#include <queue>    // 引入头文件
#include <vector>   // 引入头文件

struct TreeNode {    // 定义类型
    int val;         // int 值;
    TreeNode *left;  // TreeNode 乘 左边界;
    TreeNode *right; // TreeNode 乘 右边界;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

static TreeNode *build_tree(const std::vector<std::optional<int>> &vals) {
    if (vals.empty() || !vals[0].has_value())
        return nullptr; // 若 vals 是否为空 或 取反 vals[0].has_value()，直接返回 nullptr
    auto *root = new TreeNode(*vals[0]); // 把 new TreeNode( 乘 vals[0]); 写入 auto *root
    std::queue<TreeNode *> q;            // std::队列 小于 TreeNode 乘 超过 节点;
    q.push(root);                        // 把 根节点 压入栈/数组尾部
    size_t i = 1;                        // 把 1; 写入 size_t i
    while (!q.empty() &&
           i < vals.size()) { // 循环，直到不满足「取反 节点 是否为空 且 下标 i 小于 vals.大小(」
        TreeNode *node = q.front();                  // 把 节点.front(); 写入 TreeNode *node
        q.pop();                                     // 弹出栈顶元素
        if (i < vals.size()) {                       // 若 下标 i 小于 vals.大小(
            if (vals[i].has_value()) {               // 若 vals[下标 i].has_value(
                node->left = new TreeNode(*vals[i]); // 把 new TreeNode( 乘 vals[下标 i]); 写入 node->left
                q.push(node->left);                  // 把 节点 减 超过 左边界 压入栈/数组尾部
            }
            ++i; // 加一 下标 i;
        }
        if (i < vals.size()) {                        // 若 下标 i 小于 vals.大小(
            if (vals[i].has_value()) {                // 若 vals[下标 i].has_value(
                node->right = new TreeNode(*vals[i]); // 把 new TreeNode( 乘 vals[下标 i]); 写入 node->right
                q.push(node->right); // 把 节点 减 超过 右边界 压入栈/数组尾部
            }
            ++i; // 加一 下标 i;
        }
    }
    return root; // 返回 根节点
}

static void free_tree(TreeNode *n) { // 定义函数/方法 free_tree
    if (!n)
        return;          // 若 取反 元素个数) return;
    free_tree(n->left);  // free_tree(元素个数 减 超过 左边界);
    free_tree(n->right); // free_tree(元素个数 减 超过 右边界);
    delete n;            // delete 元素个数;
}

struct NNode {                        // 定义类型
    int val;                          // int 值;
    std::vector<NNode *> children;    // std::vector 小于 NNode 乘 超过 children;
    explicit NNode(int v) : val(v) {} // explicit NNode(int 值) : 值(值) {}
};
static std::vector<std::vector<int>> levelOrder(NNode *root) {
    std::vector<std::vector<int>> res; // std::vector 小于 std::vector 小于 int 超过 超过 结果;
    if (!root)
        return res;                            // 若 取反 根节点，直接返回 结果
    std::queue<NNode *> q;                     // std::队列 小于 NNode 乘 超过 节点;
    q.push(root);                              // 把 根节点 压入栈/数组尾部
    while (!q.empty()) {                       // 循环，直到不满足「取反 节点.empty(」
        int size = static_cast<int>(q.size()); // 把 static_cast 小于 int 超过 (节点.大小()) 存入 大小
        std::vector<int> level;                // std::vector 小于 int 超过 level;
        for (int i = 0; i < size; ++i) { // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
            auto *n = q.front();         // 把 节点.front(); 写入 auto *n
            q.pop();                     // 弹出栈顶元素
            level.push_back(n->val);     // level 追加 元素个数 减 超过 值);
            for (auto *c : n->children)
                q.push(c); // 把 字符 压入栈/数组尾部
        }
        res.push_back(std::move(level)); // 结果 追加 std::move(level));
    }
    return res; // 返回 结果
}
int main() {                                     // 程序入口：跑内嵌自测用例
    auto *root = new NNode(1);                   // 把 new NNode(1); 写入 auto *root
    auto *c3 = new NNode(3);                     // 把 new NNode(3); 写入 auto *c3
    c3->children = {new NNode(5), new NNode(6)}; // 把 {new NNode(5), new NNode(6)}; 写入 c3->children
    root->children = {c3, new NNode(2),
                      new NNode(4)}; // 把 {c3, new NNode(2), new NNode(4)}; 写入 root->children
    assert((levelOrder(root) == std::vector<std::vector<int>>{{1}, {3, 2, 4}, {5, 6}})); // 断言校验
    assert(levelOrder(nullptr).empty());                                                 // 断言校验
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
```

### R 实现（2 种方案）

R 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：双重循环枚举

**思路与代码分析**：核心是「双重循环枚举」。R 版用向量化思维与 1 起始下标，注意 1:n 的降序陷阱。**走读**：方案 1 · 双重循环枚举：开始 → 更新 new.env(parent → 处理 e$val ＜- val → 处理 e$left ＜- left → 处理 e$right ＜- right → 调用 class(e) ＜- TreeNode → 处理 e → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 双重循环枚举：开始"]
    N1["更新 new.env(parent"]
    N2["处理 e$val ＜- val"]
    N3["处理 e$left ＜- left"]
    N4["处理 e$right ＜- right"]
    N5["调用 class(e) ＜- TreeNode"]
    N6["处理 e"]
    N7["返回结果"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,N2,N3,N4,N5,N6 n;
    class N7 tm;
```

```r
# 版（方案1） 树节点：R 必须 environment 引用语义（list 是值语义） 定义函数 TreeNode（参数：值, 左边界 赋值为
# NULL, 右边界 赋值为 NULL）
TreeNode <- function(val, left = NULL, right = NULL) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$val <- val
    e$left <- left
    e$right <- right  # 把 值; e$左边界 小于 减 左边界; e$右边界 小于 减 右边界 存入 e$val
    class(e) <- "TreeNode"  # 把 「TreeNode」 存入 class(e)
    e
}
build_tree <- function(vals) {
    # 定义函数 build_tree（参数：vals）
    if (length(vals) == 0 || is.na(vals[[1]]))
        return(NULL)  # 若 长度(vals) 等于 0 或 is.na(vals[[1]])) return(NULL
    root <- TreeNode(vals[[1]])  # 把 TreeNode(vals[[1]]) 存入 根节点
    queue <- list(root)  # 把 列表(根节点) 存入 队列
    head <- 1L  # 把 1L 存入 头节点
    i <- 2L  # 把 2L 存入 下标 i
    while (head <= length(queue) && i <= length(vals)) {
        # 循环，直到不满足「头节点 不超过 长度(队列) 且 下标 i 不超过 长度(vals」
        node <- queue[[head]]  # 把 队列[[头节点]] 存入 节点
        head <- head + 1L  # 把 头节点 加 1L 存入 头节点
        if (i <= length(vals)) {
            # 若 下标 i 不超过 长度(vals 若 取反 is.na(vals[[下标 i]]
            if (!is.na(vals[[i]])) {
                node$left <- TreeNode(vals[[i]])  # 把 TreeNode(vals[[下标 i]]) 存入 node$left
                queue[[length(queue) + 1L]] <- node$left  # 队列[[长度(队列) 加 1L]] 小于 减 节点$左边界
            }
            i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
        }
        if (i <= length(vals)) {
            # 若 下标 i 不超过 长度(vals 若 取反 is.na(vals[[下标 i]]
            if (!is.na(vals[[i]])) {
                node$right <- TreeNode(vals[[i]])  # 把 TreeNode(vals[[下标 i]]) 存入 node$right
                queue[[length(queue) + 1L]] <- node$right  # 队列[[长度(队列) 加 1L]] 小于 减 节点$右边界
            }
            i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
        }
    }
    root  # 根节点
}
# 层序转列表（用于断言输出） 定义函数 tree_to_levels（参数：根节点）
tree_to_levels <- function(root) {
    if (is.null(root))
        return(list())  # 若 is.null(根节点)) return(列表(
    res <- list()  # 把 列表() 存入 结果
    level <- list(root)  # 把 列表(根节点) 存入 level
    while (length(level) > 0) {
        # 循环，直到不满足「长度(level) 超过 0」
        vals <- list()
        nxt <- list()  # 把 列表(); nxt 小于 减 列表() 存入 vals
        for (nd in level) {
            # for (nd in level) {
            vals[[length(vals) + 1L]] <- nd$val  # vals[[长度(vals) 加 1L]] 小于 减 nd$值
            if (!is.null(nd$left))
                nxt[[length(nxt) + 1L]] <- nd$left  # 若 取反 is.null(nd$左边界)) nxt[[长度(nxt) 加 1L]] 小于 减 nd$左边界
            if (!is.null(nd$right))
                nxt[[length(nxt) + 1L]] <- nd$right  # 若 取反 is.null(nd$右边界)) nxt[[长度(nxt) 加 1L]] 小于 减 nd$右边界
        }
        res[[length(res) + 1L]] <- unlist(vals)  # 结果[[长度(结果) 加 1L]] 小于 减 unlist(vals)
        level <- nxt  # 把 nxt 存入 level
    }
    res  # 结果
}
new_node <- function(v) {
    e <- new.env(parent = emptyenv())
    e$val <- v
    e$children <- list()
    class(e) <- "NNode"
    e
}  # 定义函数 new_node（参数：值）
level_order <- function(root) {
    # 定义函数 level_order（参数：根节点）
    if (is.null(root))
        return(list())  # 若 is.null(根节点)) return(列表(
    res <- list()  # 把 列表() 存入 结果
    q <- list(root)  # 把 列表(根节点) 存入 节点
    while (length(q) > 0) {
        # 循环，直到不满足「长度(节点) 超过 0」
        level <- integer(0)
        nxt <- list()  # 把 integer(0); nxt 小于 减 列表() 存入 level
        for (n in q) {
            # for (元素个数 in 节点) {
            level[[length(level) + 1L]] <- n$val  # level[[长度(level) 加 1L]] 小于 减 元素个数$值
            for (c in n$children) nxt[[length(nxt) + 1L]] <- c  # for (字符 in 元素个数$children) nxt[[长度(nxt) 加 1L]] 小于 减 字符
        }
        res[[length(res) + 1L]] <- level  # 结果[[长度(结果) 加 1L]] 小于 减 level
        q <- nxt  # 把 nxt 存入 节点
    }
    res  # 结果
}
root <- new_node(1L)  # 把 new_node(1L) 存入 根节点
c3 <- new_node(3L)  # 把 new_node(3L) 存入 c3
c3$children <- list(new_node(5L), new_node(6L))  # 把 列表(new_node(5L), new_node(6L)) 存入 c3$children
root$children <- list(c3, new_node(2L), new_node(4L))  # 把 列表(c3, new_node(2L), new_node(4L)) 存入 root$children
got <- level_order(root)  # 把 level_order(根节点) 存入 got
stopifnot(identical(got, list(1L, c(3L, 2L, 4L), c(5L, 6L))))  # 断言校验
stopifnot(length(level_order(NULL)) == 0L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
```

#### 方案 2：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。R 版用向量化思维与 1 起始下标，注意 1:n 的降序陷阱。**走读**：方案 2 · 迭代指针处理：开始 → 更新 new.env(parent → 处理 e$val ＜- val → 处理 e$left ＜- left → 处理 e$right ＜- right → 调用 class(e) ＜- TreeNode → 处理 e → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 迭代指针处理：开始"]
    N1["更新 new.env(parent"]
    N2["处理 e$val ＜- val"]
    N3["处理 e$left ＜- left"]
    N4["处理 e$right ＜- right"]
    N5["调用 class(e) ＜- TreeNode"]
    N6["处理 e"]
    N7["返回结果"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,N2,N3,N4,N5,N6 n;
    class N7 tm;
```

```r
# 版（方案2） 树节点：R 必须 environment 引用语义（list 是值语义） 定义函数 TreeNode（参数：值, 左边界 赋值为
# NULL, 右边界 赋值为 NULL）
TreeNode <- function(val, left = NULL, right = NULL) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$val <- val
    e$left <- left
    e$right <- right  # 把 值; e$左边界 小于 减 左边界; e$右边界 小于 减 右边界 存入 e$val
    class(e) <- "TreeNode"  # 把 「TreeNode」 存入 class(e)
    e
}
build_tree <- function(vals) {
    # 定义函数 build_tree（参数：vals）
    if (length(vals) == 0 || is.na(vals[[1]]))
        return(NULL)  # 若 长度(vals) 等于 0 或 is.na(vals[[1]])) return(NULL
    root <- TreeNode(vals[[1]])  # 把 TreeNode(vals[[1]]) 存入 根节点
    queue <- list(root)  # 把 列表(根节点) 存入 队列
    head <- 1L  # 把 1L 存入 头节点
    i <- 2L  # 把 2L 存入 下标 i
    while (head <= length(queue) && i <= length(vals)) {
        # 循环，直到不满足「头节点 不超过 长度(队列) 且 下标 i 不超过 长度(vals」
        node <- queue[[head]]  # 把 队列[[头节点]] 存入 节点
        head <- head + 1L  # 把 头节点 加 1L 存入 头节点
        if (i <= length(vals)) {
            # 若 下标 i 不超过 长度(vals 若 取反 is.na(vals[[下标 i]]
            if (!is.na(vals[[i]])) {
                node$left <- TreeNode(vals[[i]])  # 把 TreeNode(vals[[下标 i]]) 存入 node$left
                queue[[length(queue) + 1L]] <- node$left  # 队列[[长度(队列) 加 1L]] 小于 减 节点$左边界
            }
            i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
        }
        if (i <= length(vals)) {
            # 若 下标 i 不超过 长度(vals 若 取反 is.na(vals[[下标 i]]
            if (!is.na(vals[[i]])) {
                node$right <- TreeNode(vals[[i]])  # 把 TreeNode(vals[[下标 i]]) 存入 node$right
                queue[[length(queue) + 1L]] <- node$right  # 队列[[长度(队列) 加 1L]] 小于 减 节点$右边界
            }
            i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
        }
    }
    root  # 根节点
}
# 层序转列表（用于断言输出） 定义函数 tree_to_levels（参数：根节点）
tree_to_levels <- function(root) {
    if (is.null(root))
        return(list())  # 若 is.null(根节点)) return(列表(
    res <- list()  # 把 列表() 存入 结果
    level <- list(root)  # 把 列表(根节点) 存入 level
    while (length(level) > 0) {
        # 循环，直到不满足「长度(level) 超过 0」
        vals <- list()
        nxt <- list()  # 把 列表(); nxt 小于 减 列表() 存入 vals
        for (nd in level) {
            # for (nd in level) {
            vals[[length(vals) + 1L]] <- nd$val  # vals[[长度(vals) 加 1L]] 小于 减 nd$值
            if (!is.null(nd$left))
                nxt[[length(nxt) + 1L]] <- nd$left  # 若 取反 is.null(nd$左边界)) nxt[[长度(nxt) 加 1L]] 小于 减 nd$左边界
            if (!is.null(nd$right))
                nxt[[length(nxt) + 1L]] <- nd$right  # 若 取反 is.null(nd$右边界)) nxt[[长度(nxt) 加 1L]] 小于 减 nd$右边界
        }
        res[[length(res) + 1L]] <- unlist(vals)  # 结果[[长度(结果) 加 1L]] 小于 减 unlist(vals)
        level <- nxt  # 把 nxt 存入 level
    }
    res  # 结果
}
new_node <- function(v) {
    e <- new.env(parent = emptyenv())
    e$val <- v
    e$children <- list()
    class(e) <- "NNode"
    e
}  # 定义函数 new_node（参数：值）
level_order <- function(root) {
    # 定义函数 level_order（参数：根节点）
    if (is.null(root))
        return(list())  # 若 is.null(根节点)) return(列表(
    res <- list()  # 把 列表() 存入 结果
    q <- list(root)  # 把 列表(根节点) 存入 节点
    while (length(q) > 0) {
        # 循环，直到不满足「长度(节点) 超过 0」
        level <- integer(0)
        nxt <- list()  # 把 integer(0); nxt 小于 减 列表() 存入 level
        for (n in q) {
            # for (元素个数 in 节点) {
            level[[length(level) + 1L]] <- n$val  # level[[长度(level) 加 1L]] 小于 减 元素个数$值
            for (c in n$children) nxt[[length(nxt) + 1L]] <- c  # for (字符 in 元素个数$children) nxt[[长度(nxt) 加 1L]] 小于 减 字符
        }
        res[[length(res) + 1L]] <- level  # 结果[[长度(结果) 加 1L]] 小于 减 level
        q <- nxt  # 把 nxt 存入 节点
    }
    res  # 结果
}
root <- new_node(1L)  # 把 new_node(1L) 存入 根节点
c3 <- new_node(3L)  # 把 new_node(3L) 存入 c3
c3$children <- list(new_node(5L), new_node(6L))  # 把 列表(new_node(5L), new_node(6L)) 存入 c3$children
root$children <- list(c3, new_node(2L), new_node(4L))  # 把 列表(c3, new_node(2L), new_node(4L)) 存入 root$children
got <- level_order(root)  # 把 level_order(根节点) 存入 got
stopifnot(identical(got, list(1L, c(3L, 2L, 4L), c(5L, 6L))))  # 断言校验
stopifnot(length(level_order(NULL)) == 0L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
```

### Zig 实现（2 种方案）

Zig 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：双重循环枚举

**思路与代码分析**：核心是「双重循环枚举」。Zig 版显式分配与清零，整型边界处理严格。**走读**：方案 1 · 双重循环枚举：开始 → 计算 n → 更新 n.* → 返回 n。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 双重循环枚举：开始"]
    N1["计算 n"]
    N2["更新 n.*"]
    N3["返回 n"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,N2 n;
    class N3 tm;
```

```zig
// LeetCode 429. N叉树的层序遍历 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std

const TreeNode = struct { // 把 struct { 存入 TreeNode
    val: i32,
    left: ?*TreeNode,
    right: ?*TreeNode,
};

fn buildTree(allocator: std.mem.Allocator, vals: []const i32) !?*TreeNode { // 定义函数/方法 buildTree
    if (vals.len == 0 or vals[0] == -1) return null; // 若 vals.长度 等于 0 or vals[0] 等于 减 1，直接返回 null
    const root = try allocator.create(TreeNode); // 把 try allocator.create(TreeNode) 存入 根节点
    root.* = .{ .val = vals[0], .left = null, .right = null };
    var queue = std.ArrayList(*TreeNode).init(allocator); // 把 std.ArrayList( 乘 TreeNode).init(allocator) 存入 队列
    defer queue.deinit(); // defer 队列.deinit();
    try queue.append(root); // 把 根节点 追加到列表尾部
    var head: usize = 0; // 把 0; 写入 var head: usize
    var i: usize = 1; // 把 1; 写入 var i: usize
    while (head < queue.items.len and i < vals.len) { // 循环，直到不满足「头节点 小于 队列.items.长度 and 下标 i 小于 vals.长度」
        const node = queue.items[head]; // 把 队列.items[头节点] 存入 节点
        head += 1; // 头节点累加 1
        if (i < vals.len) { // 若 下标 i 小于 vals.长度
            if (vals[i] != -1) { // 若 vals[下标 i] 不等于 减 1
                const child = try allocator.create(TreeNode); // 把 try allocator.create(TreeNode) 存入 子节点
                child.* = .{ .val = vals[i], .left = null, .right = null };
                node.left = child; // 把 子节点; 写入 左边界
                try queue.append(child); // 把 子节点 追加到列表尾部
            }
            i += 1; // 下标 i累加 1
        }
        if (i < vals.len) { // 若 下标 i 小于 vals.长度
            if (vals[i] != -1) { // 若 vals[下标 i] 不等于 减 1
                const child = try allocator.create(TreeNode); // 把 try allocator.create(TreeNode) 存入 子节点
                child.* = .{ .val = vals[i], .left = null, .right = null };
                node.right = child; // 把 子节点; 写入 右边界
                try queue.append(child); // 把 子节点 追加到列表尾部
            }
            i += 1; // 下标 i累加 1
        }
    }
    return root; // 返回 根节点
}

const NNode = struct { val: i32, children: std.ArrayList(*NNode) };
fn nnew(v: i32, alloc: std.mem.Allocator) *NNode { // 定义函数/方法 nnew
    const n = alloc.create(NNode) catch unreachable; // 把 alloc.create(NNode) catch unreachable 存入 元素个数
    n.* = .{ .val = v, .children = std.ArrayList(*NNode).init(alloc) };
    return n; // 返回 元素个数
}
fn levelOrder(root: ?*NNode, alloc: std.mem.Allocator) std.ArrayList(std.ArrayList(i32)) { // 定义函数/方法 levelOrder
    var res = std.ArrayList(std.ArrayList(i32)).init(alloc); // 把 std.ArrayList(std.ArrayList(i32)).init(alloc) 存入 结果
    const r = root orelse return res; // 把 根节点 orelse return 结果 存入 右指针
    var q = std.ArrayList(*NNode).init(alloc); // 把 std.ArrayList( 乘 NNode).init(alloc) 存入 节点
    q.append(r) catch unreachable; // 把 右指针 追加到列表尾部
    var head: usize = 0; // 把 0; 写入 var head: usize
    while (head < q.items.len) { // 循环，直到不满足「头节点 小于 节点.items.长度」
        const size = q.items.len - head; // 把 节点.items.长度 减 头节点 存入 大小
        var level = std.ArrayList(i32).init(alloc); // 把 std.ArrayList(i32).init(alloc) 存入 level
        for (0..size) |_| { // 让 _ 从 0 走到 大小 减一
            const n = q.items[head]; // 把 节点.items[头节点] 存入 元素个数
            head += 1; // 头节点累加 1
            level.append(n.val) catch unreachable; // 把 元素个数.值 追加到列表尾部
            for (n.children.items) |c| q.append(c) catch unreachable; // 逐个取出 元素个数.children.items 的元素（字符）
        }
        res.append(level) catch unreachable; // 把 level 追加到列表尾部
    }
    return res; // 返回 结果
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const root = nnew(1, alloc); // 把 nnew(1, alloc) 存入 根节点
    const c3 = nnew(3, alloc); // 把 nnew(3, alloc) 存入 c3
    c3.children.append(nnew(5, alloc)) catch unreachable; // 把 nnew(5, alloc 追加到列表尾部
    c3.children.append(nnew(6, alloc)) catch unreachable; // 把 nnew(6, alloc 追加到列表尾部
    root.children.append(c3) catch unreachable; // 把 c3 追加到列表尾部
    root.children.append(nnew(2, alloc)) catch unreachable; // 把 nnew(2, alloc 追加到列表尾部
    root.children.append(nnew(4, alloc)) catch unreachable; // 把 nnew(4, alloc 追加到列表尾部
    const res = levelOrder(root, alloc); // 把 levelOrder(根节点, alloc) 存入 结果
    if (res.items.len != 3) return error.TestFailed; // 若 结果.items.长度 不等于 3，直接返回 error.TestFailed
    if (res.items[0].items[0] != 1) return error.TestFailed; // 若 结果.items[0].items[0] 不等于 1，直接返回 error.TestFailed
    if (res.items[1].items[0] != 3 or res.items[1].items[1] != 2 or res.items[1].items[2] != 4) return error.TestFailed;
    if (res.items[2].items[0] != 5 or res.items[2].items[1] != 6) return error.TestFailed;
    if (levelOrder(null, alloc).items.len != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
```

#### 方案 2：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Zig 版显式分配与清零，整型边界处理严格。**走读**：方案 2 · 迭代指针处理：开始 → 计算 n → 更新 n.* → 返回 n。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 迭代指针处理：开始"]
    N1["计算 n"]
    N2["更新 n.*"]
    N3["返回 n"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N1,N2 n;
    class N3 tm;
```

```zig
// LeetCode 429. N叉树的层序遍历 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std

const TreeNode = struct { // 把 struct { 存入 TreeNode
    val: i32,
    left: ?*TreeNode,
    right: ?*TreeNode,
};

fn buildTree(allocator: std.mem.Allocator, vals: []const i32) !?*TreeNode { // 定义函数/方法 buildTree
    if (vals.len == 0 or vals[0] == -1) return null; // 若 vals.长度 等于 0 or vals[0] 等于 减 1，直接返回 null
    const root = try allocator.create(TreeNode); // 把 try allocator.create(TreeNode) 存入 根节点
    root.* = .{ .val = vals[0], .left = null, .right = null };
    var queue = std.ArrayList(*TreeNode).init(allocator); // 把 std.ArrayList( 乘 TreeNode).init(allocator) 存入 队列
    defer queue.deinit(); // defer 队列.deinit();
    try queue.append(root); // 把 根节点 追加到列表尾部
    var head: usize = 0; // 把 0; 写入 var head: usize
    var i: usize = 1; // 把 1; 写入 var i: usize
    while (head < queue.items.len and i < vals.len) { // 循环，直到不满足「头节点 小于 队列.items.长度 and 下标 i 小于 vals.长度」
        const node = queue.items[head]; // 把 队列.items[头节点] 存入 节点
        head += 1; // 头节点累加 1
        if (i < vals.len) { // 若 下标 i 小于 vals.长度
            if (vals[i] != -1) { // 若 vals[下标 i] 不等于 减 1
                const child = try allocator.create(TreeNode); // 把 try allocator.create(TreeNode) 存入 子节点
                child.* = .{ .val = vals[i], .left = null, .right = null };
                node.left = child; // 把 子节点; 写入 左边界
                try queue.append(child); // 把 子节点 追加到列表尾部
            }
            i += 1; // 下标 i累加 1
        }
        if (i < vals.len) { // 若 下标 i 小于 vals.长度
            if (vals[i] != -1) { // 若 vals[下标 i] 不等于 减 1
                const child = try allocator.create(TreeNode); // 把 try allocator.create(TreeNode) 存入 子节点
                child.* = .{ .val = vals[i], .left = null, .right = null };
                node.right = child; // 把 子节点; 写入 右边界
                try queue.append(child); // 把 子节点 追加到列表尾部
            }
            i += 1; // 下标 i累加 1
        }
    }
    return root; // 返回 根节点
}

const NNode = struct { val: i32, children: std.ArrayList(*NNode) };
fn nnew(v: i32, alloc: std.mem.Allocator) *NNode { // 定义函数/方法 nnew
    const n = alloc.create(NNode) catch unreachable; // 把 alloc.create(NNode) catch unreachable 存入 元素个数
    n.* = .{ .val = v, .children = std.ArrayList(*NNode).init(alloc) };
    return n; // 返回 元素个数
}
fn levelOrder(root: ?*NNode, alloc: std.mem.Allocator) std.ArrayList(std.ArrayList(i32)) { // 定义函数/方法 levelOrder
    var res = std.ArrayList(std.ArrayList(i32)).init(alloc); // 把 std.ArrayList(std.ArrayList(i32)).init(alloc) 存入 结果
    const r = root orelse return res; // 把 根节点 orelse return 结果 存入 右指针
    var q = std.ArrayList(*NNode).init(alloc); // 把 std.ArrayList( 乘 NNode).init(alloc) 存入 节点
    q.append(r) catch unreachable; // 把 右指针 追加到列表尾部
    var head: usize = 0; // 把 0; 写入 var head: usize
    while (head < q.items.len) { // 循环，直到不满足「头节点 小于 节点.items.长度」
        const size = q.items.len - head; // 把 节点.items.长度 减 头节点 存入 大小
        var level = std.ArrayList(i32).init(alloc); // 把 std.ArrayList(i32).init(alloc) 存入 level
        for (0..size) |_| { // 让 _ 从 0 走到 大小 减一
            const n = q.items[head]; // 把 节点.items[头节点] 存入 元素个数
            head += 1; // 头节点累加 1
            level.append(n.val) catch unreachable; // 把 元素个数.值 追加到列表尾部
            for (n.children.items) |c| q.append(c) catch unreachable; // 逐个取出 元素个数.children.items 的元素（字符）
        }
        res.append(level) catch unreachable; // 把 level 追加到列表尾部
    }
    return res; // 返回 结果
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const root = nnew(1, alloc); // 把 nnew(1, alloc) 存入 根节点
    const c3 = nnew(3, alloc); // 把 nnew(3, alloc) 存入 c3
    c3.children.append(nnew(5, alloc)) catch unreachable; // 把 nnew(5, alloc 追加到列表尾部
    c3.children.append(nnew(6, alloc)) catch unreachable; // 把 nnew(6, alloc 追加到列表尾部
    root.children.append(c3) catch unreachable; // 把 c3 追加到列表尾部
    root.children.append(nnew(2, alloc)) catch unreachable; // 把 nnew(2, alloc 追加到列表尾部
    root.children.append(nnew(4, alloc)) catch unreachable; // 把 nnew(4, alloc 追加到列表尾部
    const res = levelOrder(root, alloc); // 把 levelOrder(根节点, alloc) 存入 结果
    if (res.items.len != 3) return error.TestFailed; // 若 结果.items.长度 不等于 3，直接返回 error.TestFailed
    if (res.items[0].items[0] != 1) return error.TestFailed; // 若 结果.items[0].items[0] 不等于 1，直接返回 error.TestFailed
    if (res.items[1].items[0] != 3 or res.items[1].items[1] != 2 or res.items[1].items[2] != 4) return error.TestFailed;
    if (res.items[2].items[0] != 5 or res.items[2].items[1] != 6) return error.TestFailed;
    if (levelOrder(null, alloc).items.len != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
```

### Dart 实现（2 种方案）

Dart 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：双重循环枚举

**思路与代码分析**：核心是「双重循环枚举」。Dart 版用可空类型标注与集合方法，注意空安全。代码里依次做这些事：单循环线性扫描。**走读**：方案 1 · 双重循环枚举：开始 → 命中条件，直接返回 → 更新 res → 计算 q → 当 (q.isNotEmpty) 时反复执行 → 更新 level → 更新 nxt → 遍历循环 → 调用 level.add(n.val) → 调用 nxt.addAll(n.children) → 调用 res.add(level) → 更新 q → 返回 res。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 双重循环枚举：开始"]
    N1{"root == null ？"}
    N2["命中条件，直接返回"]
    N3["更新 res"]
    N4["计算 q"]
    N5["当 (q.isNotEmpty) 时反复执行"]
    N6["更新 level"]
    N7["更新 nxt"]
    N8["遍历循环"]
    N9["调用 level.add(n.val)"]
    N10["调用 nxt.addAll(n.children)"]
    N11["调用 res.add(level)"]
    N12["更新 q"]
    N13["返回 res"]
    N0 --> N1
    N1 -- 是 --> N2
    N1 -- 否 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    N9 --> N10
    N10 -- 下一轮 --> N8
    N8 --> N11
    N11 --> N12
    N12 -- 下一轮 --> N5
    N5 --> N13
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N3,N4,N6,N7,N9,N10,N11,N12 n;
    class N5,N8 lp;
    class N1 dc;
    class N2,N13 tm;
```

```dart
// LeetCode 429. N叉树的层序遍历 — Dart 版（方案1）
class TreeNode {
  // 定义类型
  int val; // int 值;
  TreeNode? left; // TreeNode? 左边界;
  TreeNode? right; // TreeNode? 右边界;
  TreeNode(this.val); // TreeNode(this.值);
}

TreeNode? buildTree(List<int?> vals) {
  // TreeNode? buildTree(List 小于 int? 超过 vals) {
  if (vals.isEmpty || vals[0] == null)
    return null; // 若 vals.isEmpty 或 vals[0] 等于 null，直接返回 null
  final root = TreeNode(vals[0]!); // 把 TreeNode(vals[0]取反 ) 存入 根节点
  final queue = <TreeNode>[root]; // 把 小于 TreeNode 超过 [根节点] 存入 队列
  var head = 0; // 把 0 存入 头节点
  var i = 1; // 把 1 存入 下标 i
  while (head < queue.length && i < vals.length) {
    // 循环，直到不满足「头节点 小于 队列.长度 且 下标 i 小于 vals.长度」
    final node = queue[head++]; // 把 队列[头节点 加一 ] 存入 节点
    if (i < vals.length) {
      // 若 下标 i 小于 vals.长度
      if (vals[i] != null) {
        // 若 vals[下标 i] 不等于 null
        node.left = TreeNode(vals[i]!); // 把 TreeNode(vals[下标 i]取反 ); 写入 左边界
        queue.add(node.left!); // 队列 追加 节点.左边界取反 );
      }
      i++; // 下标 i 加一
    }
    if (i < vals.length) {
      // 若 下标 i 小于 vals.长度
      if (vals[i] != null) {
        // 若 vals[下标 i] 不等于 null
        node.right = TreeNode(vals[i]!); // 把 TreeNode(vals[下标 i]取反 ); 写入 右边界
        queue.add(node.right!); // 队列 追加 节点.右边界取反 );
      }
      i++; // 下标 i 加一
    }
  }
  return root; // 返回 根节点
}

List<List<int>> treeToLevels(TreeNode? root) {
  // 定义函数/方法 treeToLevels
  if (root == null) return []; // 若 根节点 等于 null，直接返回 []
  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  var level = <TreeNode>[root]; // 把 小于 TreeNode 超过 [根节点] 存入 level
  while (level.isNotEmpty) {
    // 循环，直到不满足「level.isNotEmpty」
    final vals = <int>[]; // 把 小于 int 超过 [] 存入 vals
    final nxt = <TreeNode>[]; // 把 小于 TreeNode 超过 [] 存入 nxt
    for (final n in level) {
      // for (final 元素个数 in level) {
      vals.add(n.val); // vals 追加 元素个数.值);
      if (n.left != null)
        nxt.add(n.left!); // 若 元素个数.左边界 不等于 null) nxt 追加 元素个数.左边界取反 );
      if (n.right != null)
        nxt.add(n.right!); // 若 元素个数.右边界 不等于 null) nxt 追加 元素个数.右边界取反 );
    }
    res.add(vals); // 结果 追加 vals);
    level = nxt; // 把 nxt 存入 level
  }
  return res; // 返回 结果
}

class NNode {
  // 定义类型
  final int val; // final int 值;
  final List<NNode> children = []; // 把 []; 写入 final List<NNode> children
  NNode(this.val); // NNode(this.值);
}

List<List<int>> levelOrder(NNode? root) {
  // 定义函数/方法 levelOrder
  if (root == null) return []; // 若 根节点 等于 null，直接返回 []
  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  var q = <NNode>[root]; // 把 小于 NNode 超过 [根节点] 存入 节点
  while (q.isNotEmpty) {
    // 循环，直到不满足「节点.isNotEmpty」
    final level = <int>[]; // 把 小于 int 超过 [] 存入 level
    final nxt = <NNode>[]; // 把 小于 NNode 超过 [] 存入 nxt
    for (final n in q) {
      // for (final 元素个数 in 节点) {
      level.add(n.val); // level 追加 元素个数.值);
      nxt.addAll(n.children); // nxt.addAll(元素个数.children);
    }
    res.add(level); // 结果 追加 level);
    q = nxt; // 把 nxt 存入 节点
  }
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  final root = NNode(1); // 把 NNode(1) 存入 根节点
  final c3 = NNode(3); // 把 NNode(3) 存入 c3
  c3.children.addAll([
    NNode(5),
    NNode(6),
  ]); // c3.children.addAll([NNode(5), NNode(6)]);
  root.children.addAll([
    c3,
    NNode(2),
    NNode(4),
  ]); // 根节点.children.addAll([c3, NNode(2), NNode(4)]);
  final a = levelOrder(root); // 把 levelOrder(根节点) 存入 数组
  if (a.length != 3 || a[0][0] != 1)
    throw StateError(
      'c1',
    ); // 若 数组.长度 不等于 3 或 数组[0][0] 不等于 1) throw StateError('c1');
  if (a[1].length != 3 || a[1][0] != 3 || a[1][1] != 2 || a[1][2] != 4)
    throw StateError('c2');
  if (a[2].length != 2 || a[2][0] != 5 || a[2][1] != 6) throw StateError('c3');
  if (levelOrder(null).isNotEmpty)
    throw StateError(
      'c4',
    ); // 若 levelOrder(null).isNotEmpty) throw StateError('c4');
  print('PASS'); // 全部用例通过，输出 PASS
}
```

#### 方案 2：迭代指针处理

**思路与代码分析**：核心是「迭代指针处理」。Dart 版用可空类型标注与集合方法，注意空安全。代码里依次做这些事：单循环线性扫描。**走读**：方案 2 · 迭代指针处理：开始 → 命中条件，直接返回 → 更新 res → 计算 q → 当 (q.isNotEmpty) 时反复执行 → 更新 level → 更新 nxt → 遍历循环 → 调用 level.add(n.val) → 调用 nxt.addAll(n.children) → 调用 res.add(level) → 更新 q → 返回 res。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 迭代指针处理：开始"]
    N1{"root == null ？"}
    N2["命中条件，直接返回"]
    N3["更新 res"]
    N4["计算 q"]
    N5["当 (q.isNotEmpty) 时反复执行"]
    N6["更新 level"]
    N7["更新 nxt"]
    N8["遍历循环"]
    N9["调用 level.add(n.val)"]
    N10["调用 nxt.addAll(n.children)"]
    N11["调用 res.add(level)"]
    N12["更新 q"]
    N13["返回 res"]
    N0 --> N1
    N1 -- 是 --> N2
    N1 -- 否 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    N9 --> N10
    N10 -- 下一轮 --> N8
    N8 --> N11
    N11 --> N12
    N12 -- 下一轮 --> N5
    N5 --> N13
    classDef n fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    classDef lp fill:#dcfce7,stroke:#15803d,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#eff6ff,stroke:#3b82f6,color:#1e293b;
    class N0,N3,N4,N6,N7,N9,N10,N11,N12 n;
    class N5,N8 lp;
    class N1 dc;
    class N2,N13 tm;
```

```dart
// LeetCode 429. N叉树的层序遍历 — Dart 版（方案2）
class TreeNode {
  // 定义类型
  int val; // int 值;
  TreeNode? left; // TreeNode? 左边界;
  TreeNode? right; // TreeNode? 右边界;
  TreeNode(this.val); // TreeNode(this.值);
}

TreeNode? buildTree(List<int?> vals) {
  // TreeNode? buildTree(List 小于 int? 超过 vals) {
  if (vals.isEmpty || vals[0] == null)
    return null; // 若 vals.isEmpty 或 vals[0] 等于 null，直接返回 null
  final root = TreeNode(vals[0]!); // 把 TreeNode(vals[0]取反 ) 存入 根节点
  final queue = <TreeNode>[root]; // 把 小于 TreeNode 超过 [根节点] 存入 队列
  var head = 0; // 把 0 存入 头节点
  var i = 1; // 把 1 存入 下标 i
  while (head < queue.length && i < vals.length) {
    // 循环，直到不满足「头节点 小于 队列.长度 且 下标 i 小于 vals.长度」
    final node = queue[head++]; // 把 队列[头节点 加一 ] 存入 节点
    if (i < vals.length) {
      // 若 下标 i 小于 vals.长度
      if (vals[i] != null) {
        // 若 vals[下标 i] 不等于 null
        node.left = TreeNode(vals[i]!); // 把 TreeNode(vals[下标 i]取反 ); 写入 左边界
        queue.add(node.left!); // 队列 追加 节点.左边界取反 );
      }
      i++; // 下标 i 加一
    }
    if (i < vals.length) {
      // 若 下标 i 小于 vals.长度
      if (vals[i] != null) {
        // 若 vals[下标 i] 不等于 null
        node.right = TreeNode(vals[i]!); // 把 TreeNode(vals[下标 i]取反 ); 写入 右边界
        queue.add(node.right!); // 队列 追加 节点.右边界取反 );
      }
      i++; // 下标 i 加一
    }
  }
  return root; // 返回 根节点
}

List<List<int>> treeToLevels(TreeNode? root) {
  // 定义函数/方法 treeToLevels
  if (root == null) return []; // 若 根节点 等于 null，直接返回 []
  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  var level = <TreeNode>[root]; // 把 小于 TreeNode 超过 [根节点] 存入 level
  while (level.isNotEmpty) {
    // 循环，直到不满足「level.isNotEmpty」
    final vals = <int>[]; // 把 小于 int 超过 [] 存入 vals
    final nxt = <TreeNode>[]; // 把 小于 TreeNode 超过 [] 存入 nxt
    for (final n in level) {
      // for (final 元素个数 in level) {
      vals.add(n.val); // vals 追加 元素个数.值);
      if (n.left != null)
        nxt.add(n.left!); // 若 元素个数.左边界 不等于 null) nxt 追加 元素个数.左边界取反 );
      if (n.right != null)
        nxt.add(n.right!); // 若 元素个数.右边界 不等于 null) nxt 追加 元素个数.右边界取反 );
    }
    res.add(vals); // 结果 追加 vals);
    level = nxt; // 把 nxt 存入 level
  }
  return res; // 返回 结果
}

class NNode {
  // 定义类型
  final int val; // final int 值;
  final List<NNode> children = []; // 把 []; 写入 final List<NNode> children
  NNode(this.val); // NNode(this.值);
}

List<List<int>> levelOrder(NNode? root) {
  // 定义函数/方法 levelOrder
  if (root == null) return []; // 若 根节点 等于 null，直接返回 []
  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  var q = <NNode>[root]; // 把 小于 NNode 超过 [根节点] 存入 节点
  while (q.isNotEmpty) {
    // 循环，直到不满足「节点.isNotEmpty」
    final level = <int>[]; // 把 小于 int 超过 [] 存入 level
    final nxt = <NNode>[]; // 把 小于 NNode 超过 [] 存入 nxt
    for (final n in q) {
      // for (final 元素个数 in 节点) {
      level.add(n.val); // level 追加 元素个数.值);
      nxt.addAll(n.children); // nxt.addAll(元素个数.children);
    }
    res.add(level); // 结果 追加 level);
    q = nxt; // 把 nxt 存入 节点
  }
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  final root = NNode(1); // 把 NNode(1) 存入 根节点
  final c3 = NNode(3); // 把 NNode(3) 存入 c3
  c3.children.addAll([
    NNode(5),
    NNode(6),
  ]); // c3.children.addAll([NNode(5), NNode(6)]);
  root.children.addAll([
    c3,
    NNode(2),
    NNode(4),
  ]); // 根节点.children.addAll([c3, NNode(2), NNode(4)]);
  final a = levelOrder(root); // 把 levelOrder(根节点) 存入 数组
  if (a.length != 3 || a[0][0] != 1)
    throw StateError(
      'c1',
    ); // 若 数组.长度 不等于 3 或 数组[0][0] 不等于 1) throw StateError('c1');
  if (a[1].length != 3 || a[1][0] != 3 || a[1][1] != 2 || a[1][2] != 4)
    throw StateError('c2');
  if (a[2].length != 2 || a[2][0] != 5 || a[2][1] != 6) throw StateError('c3');
  if (levelOrder(null).isNotEmpty)
    throw StateError(
      'c4',
    ); // 若 levelOrder(null).isNotEmpty) throw StateError('c4');
  print('PASS'); // 全部用例通过，输出 PASS
}
```

---

## 内容总结

- **n 叉树的层序遍历**（二叉树 · Medium）：共 2 个方案，主线思路「双重循环枚举」；时间 O(n²)（两层嵌套扫描）；动画演示DFS 点亮过程，附录给出 11 种语言 × 全部方案的可运行实现。
- 来源博客：[https://blog.csdn.net/tyro_java/article/details/145088458](https://blog.csdn.net/tyro_java/article/details/145088458)
- 导航：[📋 总目录](../) ｜ [← 130 左叶子之和](../130_左叶子之和/) ｜ [132 找树左下角的值 →](../132_找树左下角的值/)
