---
title: 07 堆与 TopK · 经典算法 20 题
date: 2026-11-24
categories: [经典算法]
tags: [前端面试, 笔试题, C, 堆]
type: 笔试题
---

# 07 堆与 TopK（C-121 ~ C-140）

> 「第 K 大 / 前 K 个 / 数据流 / 调度」是大厂笔试里最稳定的送分题，几乎每场线上笔试题都有一道。**识别特征**：看到「第 K 大」「最近的 K 个」「合并 K 个有序序列」「按频次或优先级取最优」，就要立刻想到**用大小顶堆把 O(n log n) 压到 O(n log k)**；看到「第 K 小」又要求 O(1) 空间或近似线性，就要想到**快速选择或值域二分**。求第 K 大用小顶堆、求第 K 小用大顶堆——原因是"要淘汰的那个元素必须待在堆顶"。

## 题型速查

| 子类型 | 核心手法 | 代表题 |
|---|---|---|
| 第 K 大/小（静态） | 容量 K 的堆 / 快速选择 | C-121、C-133 |
| 数据流 TopK | 常驻堆，add 即维护 | C-122 |
| 距离 TopK | 只比平方和，反向堆淘汰 | C-123 |
| 矩阵/多路取第 K | 值域二分 + 行列单调计数 / K 路归并 | C-124、C-125 |
| 多路归并 + 序列生成 | 三指针 DP / 小顶堆 | C-126、C-132 |
| 区间与调度 | 按开始排序 + 结束时间堆 | C-127、C-128 |
| 频次类 | 计数 + 桶 / 隔位贪心 | C-129、C-130 |
| 贪心 + 堆联合 | 一个堆"解锁"、一个堆"选优" | C-132、C-134、C-135 |
| 排序即贪心 | 自定义比较器 / 双指针田忌赛马 | C-139、C-140 |

> 本章所有堆题代码都自带一份精简 `MinHeap`（支持自定义比较器，`new MinHeap((a, b) => b - a)` 即大顶堆），复制即可运行，不依赖任何第三方库。

---

### C-121 数组中的第 K 个最大元素 · 中等 · 字节/美团

**题干**：给定整数数组 `nums` 和整数 `k`，返回数组中第 `k` 个最大的元素。注意是排序后的第 `k` 个最大元素，而不是第 `k` 个**不同**的元素。约定 `1 <= k <= nums.length <= 10^5`，元素范围 `[-10^4, 10^4]`。

**示例**：`输入: nums = [3,2,1,5,6,4], k = 2` → `输出: 5`；`nums = [3,2,3,1,2,4,5,5,6], k = 4` → `输出: 4`

**思路**：
- 排序：降序后取下标 `k-1`，一行搞定，O(n log n)。面试里只能当 baseline，说出它表示你知道但不够。
- 小顶堆：维护一个**大小恰好为 k** 的堆，堆顶是这 k 个元素里最小的那个，恰好就是"当前的"第 k 大。新元素只和堆顶比较：比堆顶大就把堆顶挤掉，否则直接丢弃。**为什么求第 K 大用小顶堆**——要淘汰的是"离答案最远"的元素，它必须待在堆顶才能 O(1) 找到；求第 K 小则反过来用大顶堆。
- 快速选择：借用快排的 partition，每次只递归包含目标下标的那一侧，平均 O(n)；但会打乱原数组，最坏 O(n²)，随机化 pivot 才把期望降到 O(n)。
- 取舍：数据量小、允许改数组 → 快选；要稳定 O(n log k) 且只读 → 堆；要求结果有序 → 排序。

**代码**：
```javascript
class MinHeap {
  constructor(cmp = (a, b) => a - b) { this.a = []; this.cmp = cmp; }
  get size() { return this.a.length; }
  peek() { return this.a[0]; }
  push(x) {
    const a = this.a, c = this.cmp;
    a.push(x);
    for (let i = a.length - 1; i > 0;) {
      const p = (i - 1) >> 1;
      if (c(a[p], a[i]) <= 0) break;
      [a[p], a[i]] = [a[i], a[p]];
      i = p;
    }
  }
  pop() {
    const a = this.a, c = this.cmp, top = a[0], last = a.pop();
    if (!a.length) return top;
    a[0] = last;
    for (let i = 0; ;) {
      const l = 2 * i + 1, r = l + 1;
      let m = i;
      if (l < a.length && c(a[l], a[m]) < 0) m = l;
      if (r < a.length && c(a[r], a[m]) < 0) m = r;
      if (m === i) break;
      [a[m], a[i]] = [a[i], a[m]];
      i = m;
    }
    return top;
  }
}

function findKthLargest(nums, k) {
  const heap = new MinHeap();
  for (const x of nums) {
    heap.push(x);
    if (heap.size > k) heap.pop(); // 堆顶是当前第 k 大，多出来的最小值出局
  }
  return heap.peek();
}
```

**复杂度**：时间 O(n log k)／空间 O(k)（堆内最多 k 个元素）

**易错点**：
- `k = 1` 或 `k = nums.length` 的边界，堆版本天然正确，快选版本容易越界。
- 重复元素**不能去重**："第 k 大"按排序位置计数，`[3,3,3], k = 2` 答案是 3。
- 快选的 partition 若用 `<=` 把相等元素全分到一边，递归区间不收缩会死循环。
- `pop()` 在弹出后堆为空时必须直接返回，否则 `a[0] = undefined` 污染堆。

**变体与追问**：
- 改求第 k 个最小 → 换成大顶堆（`cmp = (a, b) => b - a`）。
- 数据流版本见 C-122；TopK 高频词则是「Map 计数 + 小顶堆」。
- 追问"必须 O(n) 且不许改数组"：只能堆（O(n log k)）或计数排序（值域小的场合）。

---

### C-122 数据流中的第 K 大元素 · 简单 · 字节

**题干**：设计一个类 `KthLargest` 求数据流中第 `k` 大的元素。构造函数 `KthLargest(k, nums)` 用整数 `k` 和初始数字流 `nums` 初始化；方法 `add(val)` 把 `val` 插入数据流，并返回当前数据流中第 `k` 大的元素。约定每次调用 `add` 时，流中元素不少于 `k` 个。

**示例**：`k = 3, nums = [4,5,8,2]`，依次 `add(3)→4`、`add(5)→5`、`add(10)→5`、`add(9)→8`、`add(4)→8`

**思路**：
- 维护一个**大小恒为 k 的小顶堆**，堆顶就是第 k 大，查询 O(1)。
- `add` 的写法有讲究：先无脑 `push`，再判断 `size > k` 就 `pop`。如果新值比原堆顶还小，它会被立刻弹出，等价于"没进来"，于是不必另写 `if (val > peek)` 分支，只有一条路径，天然覆盖"堆未满"和"堆已满"两种情况。
- 构造函数里逐个调用 `add` 而不是一次性建堆，是为了复用同一套不变式；初始 `nums` 可能少于 k 个，此时堆还不满，题目保证第一次 `add` 之后数量够 k。
- 为什么不用有序数组：插入要搬元素 O(n)；也不用平衡树，堆更轻、常数更小。

**代码**：
```javascript
class MinHeap {
  constructor(cmp = (a, b) => a - b) { this.a = []; this.cmp = cmp; }
  get size() { return this.a.length; }
  peek() { return this.a[0]; }
  push(x) {
    const a = this.a, c = this.cmp;
    a.push(x);
    for (let i = a.length - 1; i > 0;) {
      const p = (i - 1) >> 1;
      if (c(a[p], a[i]) <= 0) break;
      [a[p], a[i]] = [a[i], a[p]];
      i = p;
    }
  }
  pop() {
    const a = this.a, c = this.cmp, top = a[0], last = a.pop();
    if (!a.length) return top;
    a[0] = last;
    for (let i = 0; ;) {
      const l = 2 * i + 1, r = l + 1;
      let m = i;
      if (l < a.length && c(a[l], a[m]) < 0) m = l;
      if (r < a.length && c(a[r], a[m]) < 0) m = r;
      if (m === i) break;
      [a[m], a[i]] = [a[i], a[m]];
      i = m;
    }
    return top;
  }
}

class KthLargest {
  constructor(k, nums) {
    this.k = k;
    this.heap = new MinHeap();
    for (const x of nums) this.add(x);
  }
  add(val) {
    this.heap.push(val);
    if (this.heap.size > this.k) this.heap.pop();
    return this.heap.peek();
  }
}
```

**复杂度**：构造 O(n log k)，每次 `add` 时间 O(log k)，空间 O(k)

**易错点**：
- 构造时不能 `nums.slice(0, k)`，那取的是**前** k 个而不是最大的 k 个。
- `this` 丢失：把方法单独赋值再调用（`const f = obj.add; f(1)`）会抛错，面试官爱考这个。
- 初始长度小于 k 时堆不满，`peek()` 返回 `undefined`，要确认题目是否保证。
- 返回值是堆顶，**不要**写成 `pop()`，否则堆被破坏后续全错。

**变体与追问**：
- 第 k 小 → 改大顶堆。
- 数据流中位数（LC 295）：大顶堆存较小的一半、小顶堆存较大的一半，保持两堆大小差 ≤ 1，插入 O(log n)、查询 O(1)。
- 若还要求支持删除，需要惰性删除（延迟弹出）或可索引堆。

---

### C-123 最接近原点的 K 个点 · 中等 · 快手/美团

**题干**：给定平面上的点集 `points`，其中 `points[i] = [xi, yi]`，以及整数 `k`，返回离原点 `(0,0)` 最近的 `k` 个点。距离为欧氏距离，答案顺序不限，题目保证答案唯一（不存在因距离并列导致的多解）。

**示例**：`输入: points = [[1,3],[-2,2]], k = 1` → `输出: [[-2,2]]`；`points = [[3,3],[5,-1],[-2,4]], k = 2` → `[[3,3],[-2,4]]`

**思路**：
- 距离比较**只用平方和** `x*x + y*y`，不开根号：开方是单调变换，不影响大小关系，却能免掉浮点误差和一次 `Math.sqrt`。
- 大顶堆：维护 k 个"当前最近的候选"，堆顶是这 k 个里**最远**的。新点比堆顶近就替换堆顶。**为什么求最近 k 个反而用大顶堆**——要淘汰的是最远的那个，淘汰对象必须在堆顶。
- 排序全排 O(n log n)，n 大 k 小时浪费；快速选择按距离 partition，平均 O(n)，但会改数组且最坏 O(n²)。
- 面试按"排序 → 堆 → 快选"递进作答，并说明各自代价，体现取舍意识。

**代码**：
```javascript
class MinHeap {
  constructor(cmp = (a, b) => a - b) { this.a = []; this.cmp = cmp; }
  get size() { return this.a.length; }
  peek() { return this.a[0]; }
  push(x) {
    const a = this.a, c = this.cmp;
    a.push(x);
    for (let i = a.length - 1; i > 0;) {
      const p = (i - 1) >> 1;
      if (c(a[p], a[i]) <= 0) break;
      [a[p], a[i]] = [a[i], a[p]];
      i = p;
    }
  }
  pop() {
    const a = this.a, c = this.cmp, top = a[0], last = a.pop();
    if (!a.length) return top;
    a[0] = last;
    for (let i = 0; ;) {
      const l = 2 * i + 1, r = l + 1;
      let m = i;
      if (l < a.length && c(a[l], a[m]) < 0) m = l;
      if (r < a.length && c(a[r], a[m]) < 0) m = r;
      if (m === i) break;
      [a[m], a[i]] = [a[i], a[m]];
      i = m;
    }
    return top;
  }
}

const kClosest = (points, k) => {
  const d = ([x, y]) => x * x + y * y;
  // 比较器反向写 => 大顶堆，堆顶是当前 k 个里最远的
  const heap = new MinHeap((a, b) => d(b) - d(a));
  for (const p of points) {
    heap.push(p);
    if (heap.size > k) heap.pop(); // 淘汰最远的
  }
  return heap.a.slice(); // 堆内即答案，顺序任意
};
```

**复杂度**：时间 O(n log k)／空间 O(k)

**易错点**：
- 用 `Math.hypot` 或 `Math.sqrt` 比较，极大数据下可能出现 `a < b` 与 `a² < b²` 不一致的误判。
- `k === points.length` 时全体入堆、一次都不弹，代码要能自然成立。
- 返回的是**点坐标**而不是距离；顺序不限，但不要漏点、不要重复。
- 返回内部数组前要 `slice()` 拷贝，避免调用方拿到堆的私有状态。

**变体与追问**：
- 求最远的 k 个点 → 换成小顶堆。
- 曼哈顿距离（`|x|+|y|`）或切比雪夫距离，只需换距离函数。
- KNN 分类：正是"维护 K 个最近邻 + 多数投票"，工业界同款思路。

---

### C-124 有序矩阵中第 K 小的元素 · 中等 · 字节/阿里

**题干**：给定一个 `n x n` 矩阵 `matrix`，其中每行、每列元素都按升序排列，找出矩阵中第 `k` 小的元素。注意是排序后的第 `k` 小元素，不是第 `k` 个**不同**元素。约定 `1 <= k <= n²`，元素可重复、可为负数。

**示例**：`matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8` → `输出: 13`（排序后为 1,5,9,10,11,12,13,13,15）

**思路**：
- 值域二分（最优）：答案必落在 `[左上角, 右下角]` 内。关键子问题是"统计 ≤ mid 的元素个数"：**从左下角出发**，若 `matrix[i][j] <= mid`，则这一列上方的 `i+1` 个元素都 ≤ mid，直接 `cnt += i+1` 并向右走；否则向上走。整个统计 O(n)。
- **为什么能二分**：`count(≤x)` 关于 `x` 单调不减，要找的是"最小的 x 使 count(≤x) ≥ k"，正是 `lower_bound` 的形状，因此 `while (lo < hi)` 能唯一收缩到答案。
- **为什么从左下角**：它是"当前列最大、当前行最小"，一步就能排除一整列或一整行，这是利用行列双重单调的标准姿势；从左上角出发无法判断该往哪走。
- 备选：从 `(0,0)` 出发的小顶堆，弹出后把右、下邻居入堆，第 k 次弹出即答案，O(k log k)；k 接近 n² 时退化为 O(n² log n)。

**代码**：
```javascript
function kthSmallest(matrix, k) {
  const n = matrix.length;

  // 统计矩阵中 <= x 的元素个数，O(n)
  const countLE = (x) => {
    let i = n - 1, j = 0, cnt = 0; // 从左下角出发
    while (i >= 0 && j < n) {
      if (matrix[i][j] <= x) {
        cnt += i + 1;  // 该列第 0..i 行都 <= x
        j++;           // 整列算完，向右
      } else {
        i--;           // 当前元素太大，向上找更小的
      }
    }
    return cnt;
  };

  let lo = matrix[0][0], hi = matrix[n - 1][n - 1];
  while (lo < hi) {
    const mid = lo + ((hi - lo) >> 1);
    if (countLE(mid) >= k) hi = mid; // mid 可能就是答案，保留
    else lo = mid + 1;
  }
  return lo; // 一定是矩阵中真实存在的元素
}
```

**复杂度**：时间 O(n·log(max−min))／空间 O(1)；堆解法 O(k log k)／O(k)

**易错点**：
- 计数起点写成左上角、往右下走，既会漏算又判不出方向，必须左下或右上。
- 二分写成 `lo <= hi` 或 `hi = mid - 1`，容易漏掉"答案就是 mid"的情况。
- 返回 `mid` 而不是 `lo`：循环结束时 `mid` 已不在区间内，`lo` 才是答案。
- 重复元素要按个数计入，不能先去重；`k` 是 1 基。
- `(lo + hi) >> 1` 在负数区间向负无穷取整，建议写 `lo + ((hi - lo) >> 1)`。

**变体与追问**：
- 求第 k 大 → 统计 `≥ mid` 的个数，或改从右上角走。
- 矩阵是 m×n 非方阵：`i` 初值换成 `m-1`，其余不变。
- 求中位数：`k = (m*n+1) >> 1`；若要求输出所有 ≤ 第 k 小的元素，需再扫描一趟。

---

### C-125 查找和最小的 K 对数字 · 中等 · 美团

**题干**：给定两个以**升序**排列的整数数组 `nums1`、`nums2`，以及整数 `k`，定义一对值 `(u, v)`（第一个来自 `nums1`，第二个来自 `nums2`），返回**和最小**的 `k` 对数字。结果以 `[u, v]` 列表返回，顺序不限，允许数值对重复（只要下标对不同）。

**示例**：`nums1 = [1,7,11], nums2 = [2,4,6], k = 3` → `输出: [[1,2],[1,4],[1,6]]`；`nums1 = [1,1,2], nums2 = [1,2,3], k = 2` → `[[1,1],[1,1]]`

**思路**：
- 把问题看成 **k 路归并**：固定 `nums1[i]`，序列 `nums1[i]+nums2[0], nums1[i]+nums2[1], ...` 递增，一共 `m` 条这样的有序链。在 m 条链里取全局最小的 k 个，标准做法就是小顶堆归并。
- 初始化只放每条链的头：`(nums1[i]+nums2[0], i, 0)`，共 `min(m, k)` 个。每弹出 `(sum, i, j)`，就把同一条链的下一个 `(nums1[i]+nums2[j+1], i, j+1)` 入堆。
- **为什么正确**：堆里始终持有"每条链当前未消费的最小值"，全局最小必在堆顶；弹出后立刻补位，等价于归并排序的 merge 过程，因此前 k 次弹出就是前 k 小。
- 为什么不用暴力 `m*n` 全算再排序：O(mn log(mn))，m、n 上千就爆；堆版本只与 k 有关。
- 元组里带 `i, j` 而不是只存和，是为了还原 `[u, v]` 并推进指针。

**代码**：
```javascript
class MinHeap {
  constructor(cmp = (a, b) => a - b) { this.a = []; this.cmp = cmp; }
  get size() { return this.a.length; }
  peek() { return this.a[0]; }
  push(x) {
    const a = this.a, c = this.cmp;
    a.push(x);
    for (let i = a.length - 1; i > 0;) {
      const p = (i - 1) >> 1;
      if (c(a[p], a[i]) <= 0) break;
      [a[p], a[i]] = [a[i], a[p]];
      i = p;
    }
  }
  pop() {
    const a = this.a, c = this.cmp, top = a[0], last = a.pop();
    if (!a.length) return top;
    a[0] = last;
    for (let i = 0; ;) {
      const l = 2 * i + 1, r = l + 1;
      let m = i;
      if (l < a.length && c(a[l], a[m]) < 0) m = l;
      if (r < a.length && c(a[r], a[m]) < 0) m = r;
      if (m === i) break;
      [a[m], a[i]] = [a[i], a[m]];
      i = m;
    }
    return top;
  }
}

function kSmallestPairs(nums1, nums2, k) {
  if (!nums1.length || !nums2.length || k <= 0) return [];
  const heap = new MinHeap((x, y) => x[0] - y[0]);
  const m = Math.min(nums1.length, k); // 只有前 k 行可能产生答案
  for (let i = 0; i < m; i++) heap.push([nums1[i] + nums2[0], i, 0]);

  const res = [];
  while (res.length < k && heap.size) {
    const [, i, j] = heap.pop();
    res.push([nums1[i], nums2[j]]);
    if (j + 1 < nums2.length) {
      heap.push([nums1[i] + nums2[j + 1], i, j + 1]); // 同一条链往后走
    }
  }
  return res;
}
```

**复杂度**：时间 O(k log k)／空间 O(k)（堆内最多 k 个元素）

**易错点**：
- `k` 可能大于 `m*n`，循环条件必须带 `heap.size`，否则弹出 `undefined` 崩溃。
- `j+1` 越界要判，否则访问得到 `undefined`，和变成 `NaN` 污染堆序。
- 初始化放 `min(m, k)` 行而不是全部 m 行，k 小时能省内存；但 `nums2` 为空要提前返回。
- 同一对不会重复：每条链只按 `j → j+1` 前进一次。
- 若为省堆空间交换 `nums1`/`nums2`，输出里 `[u,v]` 的语义会变，讲清楚再写。

**变体与追问**：
- 和最大的 k 对 → 两条链都从尾部走，用大顶堆。
- 第 k 小的**乘积**：负数让单调性反转，要分正负段处理，是本类高频追问。
- 两个有序数组第 k 小（LC 4 退化版）：二分可把 O(k log k) 降到 O(log(min(m,n)))。
- 若两数组本身无序，先各自排序，复杂度 O(n log n + k log k)。

---

### C-126 丑数 II · 中等 · 字节/腾讯

**题干**：丑数是只包含质因子 `2`、`3`、`5` 的正整数，`1` 被视为丑数。给定整数 `n`，返回第 `n` 个丑数。约定 `1 <= n <= 1690`，答案保证在 32 位有符号整数范围内。

**示例**：`输入: n = 10` → `输出: 12`（序列 1,2,3,4,5,6,8,9,10,12）

**思路**：
- 暴力逐个判断每个数是否丑数，O(n·log) 且要扫过大量非丑数，n 大时不可行。
- 三指针 DP：任何丑数都能写成 `某丑数 × 2/3/5`。于是把丑数序列看成三条有序链 `dp[p2]*2`、`dp[p3]*3`、`dp[p5]*5` 的**归并**，每次取三个候选的最小值填进 `dp[i]`，然后让产生这个值的指针前进一格。这就是"多路归并 + 去重"的 DP 形式。
- **为什么三处相等要同时前进**：`6 = 2×3 = 3×2`，两个指针都会产出 6，只前进一个的话下一轮还会产出 6，序列就重复了。所以三个 `if` 必须各自独立判断，而不是 `if / else if`。
- 堆解法：小顶堆 + `Set` 去重，每次弹最小、乘 2/3/5 入堆，第 n 次弹出即答案，O(n log n) 且需要 O(n) 的 Set；DP 是 O(n) 且常数更小，是标准解。

**代码**：
```javascript
function nthUglyNumber(n) {
  const dp = new Array(n).fill(1);
  let p2 = 0, p3 = 0, p5 = 0; // 三个"乘数指针"
  for (let i = 1; i < n; i++) {
    const a = dp[p2] * 2, b = dp[p3] * 3, c = dp[p5] * 5;
    dp[i] = Math.min(a, b, c);
    // 三个 if 独立，相等时一起前进，避免重复
    if (dp[i] === a) p2++;
    if (dp[i] === b) p3++;
    if (dp[i] === c) p5++;
  }
  return dp[n - 1];
}
```

**复杂度**：时间 O(n)／空间 O(n)（堆解法为 O(n log n)／O(n)）

**易错点**：
- 用 `if / else if` 链判断相等，`6` 这类公共倍数会重复入列，序列整体错位。
- `n = 1` 要返回 1，`dp` 初值必须是 1 而不是 0。
- 堆解法务必配 `Set` 去重，否则堆内会塞进大量重复值。
- 数值上界：n = 1690 时答案约 2×10⁹，在 JS 安全整数内，但换成 `n` 更大就要考虑 BigInt。

**变体与追问**：
- 超级丑数（LC 313）：质因子由数组 `primes` 给出，指针数量变成 `primes.length`，其余完全一致。
- 判断是否为丑数（LC 263）：反复除以 2/3/5，最后看是否剩 1。
- 求前 n 个丑数（返回数组）：DP 原地返回即可。

---

### C-127 会议室 II · 中等 · 阿里/快手

**题干**：给定一个会议时间安排的数组 `intervals`，其中 `intervals[i] = [starti, endi]` 表示会议 `i` 从 `starti` 开始、到 `endi` 结束，区间为**左闭右开**。求最少需要多少间会议室才能容纳所有会议（不能有两个会议同时在同一间会议室进行）。

**示例**：`输入: intervals = [[0,30],[5,10],[15,20]]` → `输出: 2`；`intervals = [[7,10],[2,4]]` → `输出: 1`

**思路**：
- 问题本质是求**最大重叠区间数**。最直观的扫描线：把 `start` 记 +1、`end` 记 −1，排序后求前缀和最大值，O(n log n)。
- 堆解法（面试首选）：按开始时间排序，维护一个**存结束时间的小顶堆**，堆的大小就是当前占用的会议室数。处理每个会议时，若堆顶（最早结束的那场）已经 ≤ 当前 `start`，说明房间空出来了，可以复用，于是先 `pop` 再 `push`。
- **为什么堆顶判断就够**：只需要知道"有没有任意一间空了"，而最早结束的那间最可能空，其余必然更晚结束，所以只看堆顶即可；堆的大小自然就是历史峰值。
- **为什么是 `<=` 不是 `<`**：区间左闭右开，上一场 10 点结束、下一场 10 点开始可以无缝复用，用 `<` 会多算一间。

**代码**：
```javascript
class MinHeap {
  constructor(cmp = (a, b) => a - b) { this.a = []; this.cmp = cmp; }
  get size() { return this.a.length; }
  peek() { return this.a[0]; }
  push(x) {
    const a = this.a, c = this.cmp;
    a.push(x);
    for (let i = a.length - 1; i > 0;) {
      const p = (i - 1) >> 1;
      if (c(a[p], a[i]) <= 0) break;
      [a[p], a[i]] = [a[i], a[p]];
      i = p;
    }
  }
  pop() {
    const a = this.a, c = this.cmp, top = a[0], last = a.pop();
    if (!a.length) return top;
    a[0] = last;
    for (let i = 0; ;) {
      const l = 2 * i + 1, r = l + 1;
      let m = i;
      if (l < a.length && c(a[l], a[m]) < 0) m = l;
      if (r < a.length && c(a[r], a[m]) < 0) m = r;
      if (m === i) break;
      [a[m], a[i]] = [a[i], a[m]];
      i = m;
    }
    return top;
  }
}

function minMeetingRooms(intervals) {
  if (!intervals.length) return 0;
  intervals.sort((a, b) => a[0] - b[0]); // 按开始时间排序
  const heap = new MinHeap();            // 小顶堆，存占用中的会议结束时间
  for (const [s, e] of intervals) {
    if (heap.size && heap.peek() <= s) heap.pop(); // 最早结束的已空出，复用
    heap.push(e);
  }
  return heap.size; // 峰值即所需房间数
}
```

**复杂度**：时间 O(n log n)／空间 O(n)

**易错点**：
- 用 `<` 判断让出房间，边界相接的会议会被多算一间，必须 `<=`。
- 按 `end` 排序是错的，必须按 `start` 排序（我们是在"时间推进"中做决策）。
- 空数组返回 0；单会议返回 1。
- 有人误以为答案是"最大同时进行数"用双层循环统计，O(n²) 会超时。

**变体与追问**：
- 合并区间（LC 56）：排序后比较 `cur.end >= next.start` 则合并。
- 判断能否只用一个会议室（LC 252）：等价于所有区间两两不重叠。
- 求"最多有几个会议同时进行的那一刻"：扫描线 + 事件排序，注意同一时刻先处理 −1 再处理 +1。

---

### C-128 任务调度器 · 中等 · 字节/腾讯

**题干**：给你一个用字符数组 `tasks` 表示的 CPU 需要执行的任务列表，任务用大写字母 `A` 到 `Z` 表示。两个**相同**任务之间必须至少有长度为 `n` 的冷却时间，冷却期间 CPU 可以执行其他任务或处于待命状态。你需要计算完成所有任务所需要的**最少**时间单位数。

**示例**：`输入: tasks = ["A","A","A","B","B","B"], n = 2` → `输出: 8`（A B 待命 A B 待命 A B）

**思路**：
- 出现次数最多的任务决定了"骨架"。设最大频次为 `maxF`、达到 `maxF` 次的字符种数为 `cnt`，则骨架占 `(maxF - 1) * (n + 1) + cnt` 个时间单位：前 `maxF-1` 组每组是"任务 + n 个冷却位"，最后一组只放 `cnt` 个高频任务，尾部不需要冷却。
- **为什么还要和 `tasks.length` 取 max**：当任务种类足够多、冷却位被填满甚至溢出时，骨架公式给出的空位已经被别的任务占掉了，此时最短时间就是"一个接一个地做"，即 `tasks.length`。所以答案是 `max(tasks.length, 骨架长度)`。
- **为什么贪心正确**：任何调度方案中，最高频任务之间至少隔 n 个位置，这是下界；按频次降序逐层填充恰好能达到该下界，下界可达即最优。
- 题面是"至少间隔 n"而不是"恰好 n"，所以可以连续执行不同任务，这正是取 max 的另一个原因。

**代码**：
```javascript
function leastInterval(tasks, n) {
  const cnt = new Array(26).fill(0);
  for (const t of tasks) cnt[t.charCodeAt(0) - 65]++;

  const maxF = Math.max(...cnt);        // 最大频次（空数组时为 0）
  let numMax = 0;
  for (const c of cnt) if (c === maxF) numMax++;

  const skeleton = (maxF - 1) * (n + 1) + numMax;
  return Math.max(tasks.length, skeleton); // 冷却位被填满时取总任务数
}
```

**复杂度**：时间 O(n)（n 为任务数量，字符集固定 26）／空间 O(1)

**易错点**：
- 忘记与 `tasks.length` 取 max，`["A","A","B","C","D","E"], n = 2` 会算小。
- `n = 0` 时公式退化为 `tasks.length`，要能自然成立。
- 空数组时 `Math.max(...[])` 得 `-Infinity` 吗？这里传入的是长度 26 的数组，安全；但若改写成 `Math.max(...tasks)` 就会踩坑。
- 把"至少 n 个间隔"理解成"必须空 n 个位置"，多加冷却时间。

**变体与追问**：
- 输出具体的调度序列（用堆每轮取 n+1 个不同任务，或按频次排序后按列填充）。
- 冷却时间按任务类型不同：需要"每个任务各自的下次可用时间"表，用堆或贪心。
- 冷却为 1 时判断能否重排（LC 767）：最大频次是否超过 `(len+1)/2`。

---

### C-129 根据字符出现频率排序 · 中等 · 美团

**题干**：给定一个字符串 `s`，请将字符串里的字符按照出现的**频率降序**排列，返回排列后的字符串。频率相同的字符顺序任意。约定 `1 <= s.length <= 5*10^5`，`s` 由大小写英文字母和数字组成。

**示例**：`输入: s = "tree"` → `输出: "eert"`（e 出现 2 次，r 和 t 各 1 次，`"eetr"` 也正确）

**思路**：
- 频率范围只有 `1..n`，非常适合**桶排序**：先 `Map` 计数 O(n)，再建 `n+1` 个桶，桶的下标就是频次，桶里存该频次的字符，最后从高频桶往低频桶拼接。整体 O(n)。
- 对比排序：`sort` 需要 O(k log k)（k 为不同字符数），计数 + 排序也可行但常数更大；k 最坏 62，实际上也够快，桶排序是更"懂题"的答案。
- 堆解法：把字符按频次建成大顶堆，逐个弹出重复写入，O(k log k)，适合"只取前 K 个高频"的场景。
- **为什么不用对象 key 遍历**：`Object.keys` 中纯数字键会被引擎按数值升序重排，行为不可控；用 `Map` 保持插入顺序或显式桶排序才可靠。

**代码**：
```javascript
function frequencySort(s) {
  const cnt = new Map();
  for (const ch of s) cnt.set(ch, (cnt.get(ch) || 0) + 1);

  // 桶排序：下标 = 频次，值 = 该频次的字符列表
  const buckets = Array.from({ length: s.length + 1 }, () => []);
  for (const [ch, f] of cnt) buckets[f].push(ch);

  let res = "";
  for (let f = s.length; f >= 1; f--) {
    for (const ch of buckets[f]) res += ch.repeat(f);
  }
  return res;
}
```

**复杂度**：时间 O(n)／空间 O(n)（桶数组长度 n+1）

**易错点**：
- 大小写敏感、数字也算独立字符，不要 `toLowerCase`。
- 用 `res += ch` 逐字符拼接在 V8 里已是 rope，不会 O(n²)，但 `ch.repeat(f)` 才能放大频次。
- `Array.from({length: n+1}, () => [])` 的第二个参数必须是工厂函数，直接写 `[]` 会让所有桶共享同一个数组。
- 桶下标从 1 开始，遍历到 `f = 1` 为止；从 0 开始会多一次空转（无害但多余）。

**变体与追问**：
- 前 K 个高频元素（LC 347）：`Map` 计数 + 容量 K 的小顶堆，或桶排序后从高往低取。
- 频率相同按字典序：桶内再排一次序，或自定义比较器。
- 按频率**升序**：桶从 1 往 n 遍历即可。

---

### C-130 重构字符串 · 中等 · 字节

**题干**：给定一个字符串 `s`，重新排列其中的字符，使得任意两个相邻字符都**不相同**。若无法做到，返回空字符串 `""`；否则返回任意一个可行结果。约定 `1 <= s.length <= 500`，`s` 只含小写字母。

**示例**：`输入: s = "aab"` → `输出: "aba"`；`输入: s = "aaab"` → `输出: ""`

**思路**：
- 先做**可行性判定**（鸽巢原理）：出现次数最多的字符有 `maxF` 个，它必须被塞进 `maxF-1` 个"空档"之间，因此必须满足 `maxF <= ceil(n/2) = floor((n+1)/2)`，否则无论怎么排都会有相邻相同。
- 构造用**隔位填充**：先按频次从高到低，把出现最多的字符填到下标 `0, 2, 4, ...`，剩下的字符继续填剩余偶数位，偶数位填满后从下标 1 开始填奇数位。这样相同字符天然不相邻，因为它们在结果里至少隔着一位。
- **为什么先填偶数位**：偶数位有 `ceil(n/2)` 个，正好容纳最大频次字符，把它放在"更宽的那一半"才能保证不越界；先填奇数位会导致最高频字符溢出到相邻位置。
- 堆解法：每轮从大顶堆取两个**不同**字符放到结果末尾，再把剩余次数放回堆，最后若剩一个字符则补在末尾。思路更"模拟"，但常数更大。

**代码**：
```javascript
function reorganizeString(s) {
  const cnt = new Map();
  let maxF = 0, maxCh = "";
  for (const ch of s) {
    const c = (cnt.get(ch) || 0) + 1;
    cnt.set(ch, c);
    if (c > maxF) { maxF = c; maxCh = ch; }
  }
  if (maxF > Math.floor((s.length + 1) / 2)) return ""; // 鸽巢判定

  const res = new Array(s.length);
  let idx = 0;
  // 1) 最高频字符先占满偶数位
  while (cnt.get(maxCh) > 0) {
    res[idx] = maxCh;
    idx += 2;
    cnt.set(maxCh, cnt.get(maxCh) - 1);
  }
  // 2) 其余字符继续填：偶数位用完就回到下标 1 填奇数位
  for (const [ch, c] of cnt) {
    for (let k = 0; k < c; k++) {
      if (idx >= s.length) idx = 1;
      res[idx] = ch;
      idx += 2;
    }
  }
  return res.join("");
}
```

**复杂度**：时间 O(n)／空间 O(n)（结果数组 + 计数表，字符集常数）

**易错点**：
- 判定条件写成 `maxF > s.length / 2`：`"aaab"` 时 `3 > 1.5` 仍成立，但 `"aab"` 的 `2 > 1.5` 会误判，必须用 `floor((n+1)/2)`。
- 奇数长度与偶数长度都要测：`"aaabb"` 可行（`"ababa"`），`"aaa bb"` 不行。
- 填奇数位时忘记 `idx = 1` 重置，会数组越界写入 `undefined`。
- 单字符 `"a"` 应返回 `"a"`，别被判定逻辑误杀。

**变体与追问**：
- 间隔为 n 的最少时间（LC 621）：从"能否排"变成"最少多长"，答案是骨架公式。
- K 距离间隔重排（LC 358）：同类思想，用"等待队列"控制冷却。
- 要求字典序最小：变成每步贪心选"能放的最小字符"，需要额外判断剩余字符的可行性，难度上升一档。

---

### C-131 分割数组为连续子序列 · 中等 · 阿里/腾讯

**题干**：给你一个按**非递减**顺序排列的整数数组 `nums`（可能包含重复数字），请你判断能否将它分割成一个或多个长度**至少为 3** 的连续子序列。每个元素必须且只能属于一个子序列，子序列内部必须是连续递增的整数（如 `1,2,3`）。返回 `true` / `false`。

**示例**：`输入: nums = [1,2,3,3,4,5]` → `true`（1,2,3 和 3,4,5）；`[1,2,3,4,4,5]` → `false`；`[1,2,3,3,4,4,5,5]` → `true`

**思路**：
- 两个哈希表：`count[x]` 记录数字 `x` 还剩几个没用，`tail[x]` 记录"以 x 结尾的合法子序列"有几条。
- 遍历 `nums`，对每个 `x`（若 `count[x] == 0` 说明已被前面的序列消耗掉，跳过）：
  1. **优先接在已有序列后面**：若 `tail[x-1] > 0`，把 `x` 接到一条以 `x-1` 结尾的序列上，`tail[x-1]--`、`tail[x]++`。
  2. 否则**尝试新开**一条 `x, x+1, x+2`，要求三者 `count` 都 > 0，各扣 1，并令 `tail[x+2]++`。
  3. 两者都不行就返回 `false`。
- **为什么必须先接后开**：新开一条序列要一次性消耗 `x+1`、`x+2`，资源消耗是"接龙"的三倍。若先开新序列，后面的数字可能不够用；"能接就接"是本题贪心正确性的核心。
- 因为数组已非递减，处理到 `x` 时所有比它小的数字都已决策完毕，所以一次线性扫描就够。

**代码**：
```javascript
function isPossible(nums) {
  const count = new Map(), tail = new Map();
  for (const x of nums) count.set(x, (count.get(x) || 0) + 1);

  for (const x of nums) {
    if (!count.get(x)) continue;                 // 已被用掉

    if ((tail.get(x - 1) || 0) > 0) {            // 1) 能接就接
      tail.set(x - 1, tail.get(x - 1) - 1);
      tail.set(x, (tail.get(x) || 0) + 1);
      count.set(x, count.get(x) - 1);
    } else if ((count.get(x + 1) || 0) > 0 && (count.get(x + 2) || 0) > 0) {
      count.set(x, count.get(x) - 1);            // 2) 新开一条长度 3 的序列
      count.set(x + 1, count.get(x + 1) - 1);
      count.set(x + 2, count.get(x + 2) - 1);
      tail.set(x + 2, (tail.get(x + 2) || 0) + 1);
    } else {
      return false;                              // 3) 接不上也开不了
    }
  }
  return true;
}
```

**复杂度**：时间 O(n)／空间 O(n)

**易错点**：
- 三条分支顺序不能反，先新开后接龙会在 `[1,2,3,4,5,6]` 之外的用例上失败。
- 新开序列时只扣了 `count[x]`、忘了扣 `x+1`、`x+2`，后面会重复使用同一元素。
- `tail.get(x-1)` 未初始化时返回 `undefined`，与 0 比较为 `false`，虽然恰好正确，但建议显式 `|| 0`。
- 题目保证数组非递减，若未排序需先排序（并考虑这会改变"子序列"语义，实际题目不会这么出）。

**变体与追问**：
- 子序列长度**恰好**为 3：把"接龙"分支去掉，只允许新开，且最后 `count` 必须全空。
- 一手顺子（LC 846）：有分组大小限制且数组无序，需要先排序 + 分组。
- 问"最多能分出几条序列"：需要改成按段统计，贪心策略不变但计数方式不同。

---

### C-132 IPO · 困难 · 字节

**题干**：假设你正在创业，初始资本为 `w`。给定 `n` 个项目，第 `i` 个项目需要的最低资本为 `capital[i]`，完成后纯利润为 `profits[i]`。你最多可以完成 `k` 个**不同**的项目（每个项目只能做一次），且每次只能启动所需资本不超过当前资本 `w` 的项目。求最终能获得的最大资本。

**示例**：`输入: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]` → `输出: 4`（先做资本 0 的项目得 1，再做资本 1 的项目得 3）

**思路**：
- 把项目按 `capital` 升序排序，指针 `i` 指向"还没解锁"的第一个项目。每轮先做**解锁**：把所有 `capital <= w` 的项目推进利润大顶堆；再从堆里取利润最大的做掉，`w += profit`。
- **为什么需要两个结构**：资本门槛决定了"哪些项目现在能做"（按 capital 排序 + 指针即可，因为 w 单调不减，指针只前进不回退），而"做哪一个最划算"需要对当前可选集合取最大利润——这正是大顶堆的职责。一个负责"解锁"，一个负责"选优"。
- **为什么贪心正确**：项目的成本不随做过的项目变化，且利润是一次性入账、直接抬高资本。每轮选当前可做项目中利润最大的，能最大化下一轮的资本，从而解锁更多项目，这是典型的"无后效性 + 交换论证"贪心。

**代码**：
```javascript
class MaxHeap {
  constructor() { this.a = []; }
  get size() { return this.a.length; }
  push(x) {
    const a = this.a;
    a.push(x);
    for (let i = a.length - 1; i > 0;) {
      const p = (i - 1) >> 1;
      if (a[p] >= a[i]) break;
      [a[p], a[i]] = [a[i], a[p]];
      i = p;
    }
  }
  pop() {
    const a = this.a, top = a[0], last = a.pop();
    if (!a.length) return top;
    a[0] = last;
    for (let i = 0; ;) {
      const l = 2 * i + 1, r = l + 1;
      let m = i;
      if (l < a.length && a[l] > a[m]) m = l;
      if (r < a.length && a[r] > a[m]) m = r;
      if (m === i) break;
      [a[m], a[i]] = [a[i], a[m]];
      i = m;
    }
    return top;
  }
}

function findMaximizedCapital(k, w, profits, capital) {
  const n = profits.length;
  const projects = capital.map((c, i) => [c, profits[i]]).sort((a, b) => a[0] - b[0]);
  const heap = new MaxHeap();
  let i = 0;
  for (let round = 0; round < k; round++) {
    while (i < n && projects[i][0] <= w) heap.push(projects[i++][1]); // 解锁
    if (!heap.size) break;   // 没有可做的项目，提前结束
    w += heap.pop();         // 选利润最大的做掉
  }
  return w;
}
```

**复杂度**：时间 O(n log n + k log n)／空间 O(n)

**易错点**：
- `k` 可能远大于 `n`，循环里必须判 `heap.size === 0` 提前 `break`，否则白转。
- 每个项目只能做一次：出堆即消耗，不能放回；不要误写成"每次从头挑"。
- 每轮都要**重新解锁**（`w` 变大后门槛可能被跨过），不能只在第一轮解锁一次。
- 排序后要保存原利润，元组配对别搞错下标。

**变体与追问**：
- 项目可重复做：变成"每次都在可做集合中取最大利润"，堆不清空，可无限循环直到 k 次。
- 项目之间有依赖（做完 A 才能做 B）：变成带拓扑序的调度，需要用"入度 + 堆"。
- 求达到目标资本的最少项目数：改成计数，并在 w 不再增长时立即返回 -1。

---

### C-133 最小的 k 个数 · 简单 · 腾讯/美团

**题干**：输入整数数组 `arr`，找出其中最小的 `k` 个数。结果顺序不限。约定 `0 <= k <= arr.length <= 10^4`，`0 <= arr[i] <= 10^4`。

**示例**：`输入: arr = [3,2,1], k = 2` → `输出: [1,2]` 或 `[2,1]`；`arr = [0,1,2,1], k = 1` → `[0]`

**思路**：
- 大顶堆（推荐）：维护容量为 k 的大顶堆，堆顶是这 k 个里**最大**的。新元素比堆顶小就替换它。**为什么最小 k 个用大顶堆**——淘汰对象是"当前候选里最大的"，必须放堆顶才能 O(1) 定位。时间 O(n log k)，空间 O(k)，适合 n 很大、k 很小的数据流场景。
- 快速选择：基于 partition 把"下标 < k"的元素都变成不大于第 k 小的元素，平均 O(n)，但会修改原数组、最坏 O(n²)。
- 排序：O(n log n)，代码最短，面试里作为兜底。
- 三者对比是本题的标准追问点：面试官通常先要 O(n log k) 的堆解，再追问"能不能更快"，此时答快选并说明代价。

**代码**：
```javascript
class MaxHeap {
  constructor() { this.a = []; }
  get size() { return this.a.length; }
  peek() { return this.a[0]; }
  push(x) {
    const a = this.a;
    a.push(x);
    for (let i = a.length - 1; i > 0;) {
      const p = (i - 1) >> 1;
      if (a[p] >= a[i]) break;
      [a[p], a[i]] = [a[i], a[p]];
      i = p;
    }
  }
  pop() {
    const a = this.a, top = a[0], last = a.pop();
    if (!a.length) return top;
    a[0] = last;
    for (let i = 0; ;) {
      const l = 2 * i + 1, r = l + 1;
      let m = i;
      if (l < a.length && a[l] > a[m]) m = l;
      if (r < a.length && a[r] > a[m]) m = r;
      if (m === i) break;
      [a[m], a[i]] = [a[i], a[m]];
      i = m;
    }
    return top;
  }
}

function getLeastNumbers(arr, k) {
  if (k <= 0) return [];            // k = 0 要单独处理
  const heap = new MaxHeap();
  for (const x of arr) {
    heap.push(x);
    if (heap.size > k) heap.pop();  // 挤掉当前候选里最大的
  }
  return heap.a.slice();            // 顺序不限，直接返回堆内元素
}
```

**复杂度**：时间 O(n log k)／空间 O(k)

**易错点**：
- `k = 0` 时若不特判，最后返回的会是"最小的 0 个"却可能因逻辑走偏返回 `undefined`。
- `k >= arr.length` 时应当返回全部元素，堆版本天然正确，快选版本要防越界。
- 结果顺序不限，但**不能有重复缺失**：重复值要原样保留（`[1,1,2], k = 2` → `[1,1]`）。
- 快选必须随机化 pivot，否则有序输入退化为 O(n²)；且 partition 后要判断 `pivotIndex` 与 `k-1` 的关系。

**变体与追问**：
- 第 k 大的元素（C-121）：同一套堆思想，容量 k、方向相反。
- 数据流版本（C-122）：堆常驻，`add` 后返回堆顶。
- 要求结果升序：堆内元素再排一次，O(k log k)，总复杂度不变。
- n 极大且内存受限（如 10 亿个数取最小 100 个）：只能流式读取 + 堆，这正是堆解法的杀手锏场景。

---

### C-134 雇佣 K 名工人的最低成本 · 困难 · 阿里

**题干**：有 `n` 名工人，`quality[i]` 表示第 `i` 名工人的工作质量，`wage[i]` 表示其最低期望工资。现在要雇佣 `k` 名工人组成一个付费小组，必须按**同一单价** `price` 付薪：第 `i` 名工人的实付为 `price * quality[i]`，且不得低于 `wage[i]`。求雇佣 k 名工人的最低总成本（返回 double）。

**示例**：`输入: quality = [10,20,5], wage = [70,50,30], k = 2` → `输出: 105.00000`（雇第 0、2 名，price = 70/10 = 7，成本 7×10 + 7×5 = 105）

**思路**：
- 关键恒等式：若某工人被雇，则 `price >= wage[i] / quality[i]`。所以只要**枚举"谁决定了 price"**，整组的 price 就确定了。
- 把工人按 `wage/quality` **升序**排序。遍历到第 `i` 个工人时，假设他（也就是当前 ratio 最大者）就是"被满足得最紧"的那个，令 `price = ratio[i]`，前面的工人都满足 `ratio <= price`，全部可选。此时为了让总成本 `price * Σquality` 最小，应在前面所有人里挑 **k 个 quality 最小**的。
- 用一个**大顶堆**维护"当前已遍历工人中 quality 最小的 k 个"，同时维护它们的和 `sumQ`。堆超过 k 就弹掉 quality 最大的（它最费钱）。当堆恰好 k 个时，用 `ratio[i] * sumQ` 更新答案。
- **为什么贪心正确**：对固定 price，成本只与 quality 之和成正比，因此选 quality 最小的 k 人最优；而最优解的 price 一定等于某个工人的 ratio（否则可以下调 price 直到某个工人恰好被满足），枚举所有 ratio 即可覆盖最优解。

**代码**：
```javascript
class MaxHeap {
  constructor() { this.a = []; }
  get size() { return this.a.length; }
  push(x) {
    const a = this.a;
    a.push(x);
    for (let i = a.length - 1; i > 0;) {
      const p = (i - 1) >> 1;
      if (a[p] >= a[i]) break;
      [a[p], a[i]] = [a[i], a[p]];
      i = p;
    }
  }
  pop() {
    const a = this.a, top = a[0], last = a.pop();
    if (!a.length) return top;
    a[0] = last;
    for (let i = 0; ;) {
      const l = 2 * i + 1, r = l + 1;
      let m = i;
      if (l < a.length && a[l] > a[m]) m = l;
      if (r < a.length && a[r] > a[m]) m = r;
      if (m === i) break;
      [a[m], a[i]] = [a[i], a[m]];
      i = m;
    }
    return top;
  }
}

function mincostToHireWorkers(quality, wage, k) {
  const workers = quality.map((q, i) => [wage[i] / q, q]);
  workers.sort((a, b) => a[0] - b[0]); // 按 ratio 升序

  const heap = new MaxHeap(); // 维护 k 个最小 quality
  let sumQ = 0, ans = Infinity;
  for (const [ratio, q] of workers) {
    heap.push(q);
    sumQ += q;
    if (heap.size > k) sumQ -= heap.pop();      // 挤掉 quality 最大的
    if (heap.size === k) ans = Math.min(ans, ratio * sumQ);
  }
  return ans;
}
```

**复杂度**：时间 O(n log n + n log k)／空间 O(n)（排序）+ O(k)（堆）

**易错点**：
- 用 `wage[i] / quality[i]` 做浮点排序理论上可能有精度问题，稳妥做法是比较器里交叉相乘 `wage[a]*quality[b] - wage[b]*quality[a]`。
- 堆大小必须**恰好为 k** 时才更新答案，否则 `k = 3` 时前两轮会算出偏小的假答案。
- `k = 1` 时要返回 `min(wage[i])`，代码能覆盖，但别在循环外忘了初始化 `ans`。
- 返回 double，JS 直接返回 `number`，不要 `Math.round`。
- `sumQ` 是整数累加，n 大时也在安全范围内，但不要写成先乘后加的浮点形式。

**变体与追问**：
- 若要求每人工资**严格高于** `wage[i]`，判定改成 `>`，其余不变。
- 若质量与工资不成正比（不同工种单价不同），问题变成带权匹配，贪心失效。
- 若限制小组内必须来自不同部门，需要按部门分组后再选，退化为"分组背包"式问题。

---

### C-135 找到处理最多请求的服务器 · 困难 · 字节

**题干**：有 `k` 台服务器，编号 `0` 到 `k-1`。第 `i` 个请求在 `arrival[i]` 时刻到达、需要 `load[i]` 的处理时间。分配规则：优先分配给编号为 `i % k` 的服务器；若它正忙，则按编号**循环**找下一个空闲服务器（`i%k+1`, `i%k+2` …，超过 `k-1` 回到 0）；若全部忙则丢弃该请求。求处理请求数量最多的服务器编号，数量相同取编号最小者。

**示例**：`输入: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]` → `输出: 1`（服务器 0 处理 1 个、服务器 1 处理 2 个、服务器 2 处理 1 个）

**思路**：
- 需要两个结构：**忙碌堆**（小顶堆，按"空闲时刻"排序，存 `[freeAt, id]`）负责释放，**空闲集合**（按编号有序）负责"找 ≥ i%k 的最小空闲编号"。
- 每个请求到来时：先把 `freeAt <= arrival[i]` 的服务器**全部**弹回空闲集合（同一时刻可能有多个释放，必须一次性释放完，否则会误判为忙而丢弃）。
- 然后在空闲集合里用二分找到第一个编号 `>= i % k` 的服务器；若没有则回绕取最小（下标 0）。取走后从集合删除并压入忙碌堆。
- **为什么不能只用堆**：堆只能取全局最小，回答不了"≥ i%k 的最小值"，必须用**有序集合**（C++ `set`、Java `TreeSet`）；JS 无内置实现，用升序数组 + 二分模拟，或用 Fenwick 树维护前缀空闲计数。
- 复杂度见下：数组模拟有序集合时单次插入/删除为 O(k)，换平衡树或 Fenwick 树可降到 O(log k)。

**代码**：
```javascript
class MinHeap {
  constructor(cmp = (a, b) => a - b) { this.a = []; this.cmp = cmp; }
  get size() { return this.a.length; }
  peek() { return this.a[0]; }
  push(x) {
    const a = this.a, c = this.cmp; a.push(x);
    for (let i = a.length - 1; i > 0;) {
      const p = (i - 1) >> 1;
      if (c(a[p], a[i]) <= 0) break;
      [a[p], a[i]] = [a[i], a[p]]; i = p;
    }
  }
  pop() {
    const a = this.a, c = this.cmp, top = a[0], last = a.pop();
    if (!a.length) return top;
    a[0] = last;
    for (let i = 0; ;) {
      const l = 2 * i + 1, r = l + 1; let m = i;
      if (l < a.length && c(a[l], a[m]) < 0) m = l;
      if (r < a.length && c(a[r], a[m]) < 0) m = r;
      if (m === i) break;
      [a[m], a[i]] = [a[i], a[m]]; i = m;
    }
    return top;
  }
}

function busiestServers(k, arrival, load) {
  const cnt = new Array(k).fill(0);
  const free = Array.from({ length: k }, (_, i) => i); // 升序空闲编号
  const busy = new MinHeap((a, b) => a[0] - b[0]);     // [freeAt, id]
  const lowerBound = (x) => {                          // 第一个 >= x 的下标
    let lo = 0, hi = free.length;
    while (lo < hi) {
      const m = (lo + hi) >> 1;
      if (free[m] < x) lo = m + 1; else hi = m;
    }
    return lo;
  };

  for (let i = 0; i < arrival.length; i++) {
    const t = arrival[i];
    while (busy.size && busy.peek()[0] <= t) {         // 一次性释放所有到期的
      const id = busy.pop()[1];
      free.splice(lowerBound(id), 0, id);
    }
    if (!free.length) continue;                        // 全忙，请求被丢弃
    let p = lowerBound(i % k);
    if (p === free.length) p = 0;                      // 回绕到最小编号
    const id = free.splice(p, 1)[0];
    cnt[id]++;
    busy.push([t + load[i], id]);
  }

  let best = 0;
  for (let i = 1; i < k; i++) if (cnt[i] > cnt[best]) best = i;
  return best;
}
```

**复杂度**：时间 O(n·k)（数组有序集合，`splice` 为 O(k)）；用平衡树/Fenwick 优化后 O(n log k)／空间 O(k)

**易错点**：
- 释放必须写成 `while` 循环一次性放完，若每轮只放一个，同一时刻多台空闲时会漏。
- 二分找不到 `>= i%k` 的编号时忘记回绕到 0，会误丢请求。
- `i % k` 用的是**请求下标**，不是时间；并列取编号最小，所以最后比较用 `>` 而非 `>=`。
- `k = 1` 时所有请求都打同一台，回绕逻辑要能处理 `p === free.length`。

**变体与追问**：
- 用 Fenwick 树实现 O(n log k)：`bit` 存"该编号是否空闲"，用二分 + 前缀和找第 `rank` 个空闲编号。
- 负载均衡场景：改成"最少连接数"或"最少负载"决策，注意力放到堆的比较键。

---

### C-136 吃苹果的最大数目 · 中等 · 快手

**题干**：有一棵特殊的苹果树，`apples[i]` 表示第 `i` 天长出的苹果数量，`days[i]` 表示这批苹果会在第 `i + days[i]` 天**腐烂**（即只能吃到第 `i + days[i] - 1` 天）。你每天最多吃一个苹果，也可以选择不吃。给你两个长度为 `n` 的数组，返回你最多能吃到的苹果数目。

**示例**：`输入: apples = [1,2,3,5,2], days = [3,2,1,4,2]` → `输出: 7`

**思路**：
- 每天都有"吃哪个"的决策，直觉是**先吃最快过期的**（贪心）：早熟的苹果放不久，晚熟的可以等等。这正好对应一个按**过期日**排序的小顶堆。
- 流程：第 `i` 天先把新长出的苹果 `[i + days[i], apples[i]]` 入堆；然后清理堆顶所有 `过期日 <= i` 的批次（已烂，丢掉）；若堆非空，吃掉堆顶一个（数量减 1 后若仍 > 0 就放回堆）。
- **为什么贪心正确**：任意时刻两个可选批次，若 A 比 B 先过期，则先吃 B 再吃 A 在 A 过期时可能已损失，而先吃 A 再吃 B 不会更差——交换论证成立。
- 优化：第 `n` 天之后不再有新增，但堆里可能还有苹果，循环条件应为 `i < n || heap.size`；若某天堆空且后续还有苹果，可以直接跳到下一个 `apples[i] > 0` 的日子，避免空转。
- 复杂度：天数上界约为 `n + max(days)`，每天最多一次入堆/出堆，O((n + maxDay) log n)。

**代码**：
```javascript
class MinHeap {
  constructor(cmp = (a, b) => a - b) { this.a = []; this.cmp = cmp; }
  get size() { return this.a.length; }
  peek() { return this.a[0]; }
  push(x) {
    const a = this.a, c = this.cmp; a.push(x);
    for (let i = a.length - 1; i > 0;) {
      const p = (i - 1) >> 1;
      if (c(a[p], a[i]) <= 0) break;
      [a[p], a[i]] = [a[i], a[p]]; i = p;
    }
  }
  pop() {
    const a = this.a, c = this.cmp, top = a[0], last = a.pop();
    if (!a.length) return top;
    a[0] = last;
    for (let i = 0; ;) {
      const l = 2 * i + 1, r = l + 1; let m = i;
      if (l < a.length && c(a[l], a[m]) < 0) m = l;
      if (r < a.length && c(a[r], a[m]) < 0) m = r;
      if (m === i) break;
      [a[m], a[i]] = [a[i], a[m]]; i = m;
    }
    return top;
  }
}

function eatenApples(apples, days) {
  const n = apples.length;
  const heap = new MinHeap((a, b) => a[0] - b[0]); // [过期日, 剩余数量]
  let eaten = 0, day = 0;

  while (day < n || heap.size) {
    if (day < n && apples[day] > 0) heap.push([day + days[day], apples[day]]);
    while (heap.size && heap.peek()[0] <= day) heap.pop(); // 已腐烂（当天就烂）
    if (heap.size) {
      const [expire, left] = heap.pop();
      eaten++;
      if (left > 1) heap.push([expire, left - 1]);
    }
    day++;
  }
  return eaten;
}
```

**复杂度**：时间 O((n + maxDay) log n)／空间 O(n)

**易错点**：
- 过期判定用 `<=`：`days[i] = 0` 的批次当天就烂，`<` 会把它当成能吃。
- 循环条件漏写 `|| heap.size`：第 n 天之后堆里还有苹果，会少算。
- 吃掉一个后要判断剩余数量是否 > 0 再放回，否则堆里塞满 0 导致死循环（虽然会被过期清理）。
- 若用「数组存每天苹果 + 每天扫描」会 O(n·maxDay) 超时。

**变体与追问**：
- 每天**必须**吃一个（吃不到就结束）：把"可以不吃"去掉，答案变成"连续能吃多少天"。
- 苹果有不同价值、优先吃价值高的：比较键从过期日换成"价值降序 + 过期日升序"。
- 每天可以吃多个（有上限 `m`）：每轮循环吃 `min(m, ...)` 个，或把"批次"拆成按天入堆。

---

### C-137 距离顺序排列矩阵单元格 · 简单 · 美团

**题干**：给定四个整数 `rows`、`cols`、`rCenter`、`cCenter`，矩阵为 `rows x cols`，`(rCenter, cCenter)` 是其中的一个单元格。返回矩阵中的所有单元格坐标 `[r, c]`，并按到 `(rCenter, cCenter)` 的**曼哈顿距离升序**排列；距离相同的单元格按**行优先**（先比 `r`，再比 `c`）排列。

**示例**：`输入: rows = 1, cols = 2, rCenter = 0, cCenter = 0` → `输出: [[0,0],[0,1]]`；`rows = 2, cols = 3, rCenter = 1, cCenter = 2` → `[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]`

**思路**：
- 最直接：把 `rows * cols` 个坐标全部生成，按 `(曼哈顿距离, r, c)` 三元组排序。O(rc log(rc))，代码三行，面试先给这个。
- 更优：从中心做 **BFS**（上下左右扩展），BFS 天然按"层"扩展，第 d 层就是距离为 d 的所有格子，因此**不需要排序**，O(rc)。注意入队顺序要保证同层内行优先，可在同一层内先收集再按 `(r, c)` 排序，或按固定方向顺序扩展。
- **为什么 BFS 有序**：每条边权为 1，BFS 的访问顺序就是最短距离的非降序，这是无权图 BFS 的基本性质。
- 复杂度对比：排序 O(rc log(rc)) vs BFS O(rc)，rc 上限 10⁴ 时两者都能过，但面试答出 BFS 更显功底。

**代码**：
```javascript
function allCellsDistOrder(rows, cols, rCenter, cCenter) {
  const dist = (r, c) => Math.abs(r - rCenter) + Math.abs(c - cCenter);
  const res = [];

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) res.push([r, c]);
  }

  // 主键：曼哈顿距离；次键：行；再次：列（保证同距行优先）
  res.sort((a, b) => {
    const d = dist(a[0], a[1]) - dist(b[0], b[1]);
    if (d !== 0) return d;
    if (a[0] !== b[0]) return a[0] - b[0];
    return a[1] - b[1];
  });

  return res;
}
```

**复杂度**：时间 O(rc log(rc))／空间 O(rc)（BFS 版本为 O(rc) 时间）

**易错点**：
- 只按距离排序，同距元素的顺序不确定，题目要求行优先，必须补次级比较键。
- `rCenter`/`cCenter` 是 0 基坐标，别和 `rows`/`cols` 搞混。
- 返回的是坐标数组的数组，不是扁平化的一维数组。
- 用 `sort` 的比较器必须返回数值，返回布尔值会导致排序结果不可预期。

**变体与追问**：
- 只要第 k 近的格子：仍可 BFS，数到第 k 个即停。
- 带障碍物的最短距离：BFS 仍然适用，距离排序改为"按 BFS 序输出可达格子"。
- 欧氏距离排序：距离函数换成平方和，但"同距行优先"的次级键规则要重新约定。

---

### C-138 卡车上的最大单元数 · 简单 · 拼多多

**题干**：有 `n` 种箱子，`boxTypes[i] = [numberOfBoxes_i, numberOfUnitsPerBox_i]` 分别表示第 `i` 种箱子的数量和每箱能装的单元数。卡车最多能装 `truckSize` 个箱子，可以只装某种箱子的一部分。返回卡车能装下的**最大单元总数**。

**示例**：`输入: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4` → `输出: 8`（拿 1 箱 3 单元 + 2 箱 2 单元 + 1 箱 1 单元）

**思路**：
- 每种箱子的"单位价值"是固定的，箱子可**按个拆分**装入，这就是分数背包的退化形式：单位价值恒定 + 可分割 ⇒ 贪心最优，按单元数**降序**装，装到容量用完为止。
- 实现：按 `numberOfUnitsPerBox` 降序排序，依次取 `min(剩余容量, 该种箱数)` 个，累加 `个数 × 单元数`。
- **为什么贪心正确**（交换论证）：若方案里有单价低的箱子，而还有单价高的箱子没装满，把低单价换成高单价，总单元数只会增加，故最优解必然"先装满高单价"。
- **为什么不用堆**：这是静态集合、全量可排序，排序 O(n log n) 已经最优；堆适合"动态取最大"的场景，这里没必要。
- 与 0/1 背包的区别：0/1 背包每件不可分割，贪心会错；本题可按箱取部分，所以贪心成立——这是最容易被追问的点。

**代码**：
```javascript
function maximumUnits(boxTypes, truckSize) {
  // 按每箱单元数降序，优先装"性价比"最高的
  boxTypes.sort((a, b) => b[1] - a[1]);

  let total = 0;
  for (const [count, units] of boxTypes) {
    const take = Math.min(count, truckSize); // 容量不够时只取一部分
    total += take * units;
    truckSize -= take;
    if (truckSize === 0) break;              // 装满提前退出
  }
  return total;
}
```

**复杂度**：时间 O(n log n)／空间 O(1)（原地排序，不计输入）

**易错点**：
- 容量不足时忘记只取 `truckSize` 个，直接 `total += count * units` 会超装。
- `truckSize` 大于所有箱子总数时，循环自然结束，结果应等于全部单元之和。
- 排序键搞错成"数量降序"，会得到错误答案（题目比的是单位价值）。
- 比较器写 `b[1] - a[1]` 而非 `a[1] - b[1]`，方向反了会先装最差的。

**变体与追问**：
- 每箱不可拆分（只能整箱装）：变成 0/1 背包，n 小可用 DP，贪心失效。
- 箱子有体积和重量双约束：二维背包，DP。
- 允许多辆卡车、每辆容量不同：先按单位价值排序，再按容量顺序贪心装（若卡车之间无差别仍成立）。

---

### C-139 最大数 · 中等 · 腾讯/字节

**题干**：给定一组非负整数 `nums`，重新排列每个数的顺序（每个数不可拆分），使拼接结果组成一个**最大的整数**。由于结果可能非常大，返回**字符串**而不是整数。约定 `1 <= nums.length <= 100`，`0 <= nums[i] <= 10^9`。

**示例**：`输入: nums = [10,2]` → `输出: "210"`；`nums = [3,30,34,5,9]` → `"9534330"`；`nums = [0,0]` → `"0"`

**思路**：
- 这不是按数值大小排序：`9` 显然应在 `34` 前，但 `30` 又该在 `3` 后。正确做法是把数转成字符串，用**自定义比较器**：若 `a + b > b + a`，则 `a` 应排在 `b` 前面。
- **为什么这个比较器有效**：`a+b > b+a` 定义了"拼接后更优"的偏序关系。可以证明它满足**传递性**（把每个串看成以自身重复拼接为极限的无穷串，比较即比较字典序），因此可以用 `sort` 得到全序，贪心拼接就是全局最优。
- **为什么不能按长度/字典序**：`"30" vs "3"` 字典序 `"3" > "30"`，但 `"330" > "303"` 才是对的；只看长度同样会错。
- 前导零处理：若排序后第一个串是 `"0"`，说明所有数都是 0，直接返回 `"0"`，否则会输出 `"000"`。
- 复杂度：排序 O(n log n) 次比较，每次比较拼接两个长度至多 10 的串，可视为 O(n log n)。

**代码**：
```javascript
function largestNumber(nums) {
  const strs = nums.map(String);

  strs.sort((a, b) => {
    const ab = a + b, ba = b + a;
    if (ab > ba) return -1; // a 拼前面更大 => a 在前
    if (ab < ba) return 1;
    return 0;
  });

  if (strs[0] === "0") return "0"; // 全 0 的情况
  return strs.join("");
}
```

**复杂度**：时间 O(n log n · L)（L 为数字位数，比较是字符串比较）／空间 O(n)

**易错点**：
- 用 `(b + a) - (a + b)` 把字符串转数值比较，长度超过 15 位会精度丢失，必须用字符串比较。
- 比较器返回布尔值（如 `a + b > b + a`）会被 `sort` 转成 1/0，永不返回 -1，排序结果错乱。
- 忘记前导零特判，`[0,0]` 输出 `"000"`。
- 认为 `[0]` 也需特判——其实 `strs[0] === "0"` 已覆盖。

**变体与追问**：
- 拼成**最小**数：比较器反向，同时要处理前导零（结果 `"0"` 也要特判）。
- 拼成能被 k 整除的最小数：需要 DP 记录余数，难度陡增。
- 两两拼接最大（LC 周赛变体）：只需比较每对，O(n²) 但 n 小。

---

### C-140 优势洗牌 · 中等 · 阿里/快手

**题干**：给定两个长度相等的数组 `nums1` 和 `nums2`，`nums1` 相对于 `nums2` 的**优势**定义为满足 `nums1[i] > nums2[i]` 的下标 `i` 的数目。请重排 `nums1`，使得优势最大化，返回重排后的 `nums1`。约定长度不超过 10⁵，元素范围 `[0, 10^9]`。

**示例**：`输入: nums1 = [2,7,11,15], nums2 = [1,10,4,11]` → `输出: [2,11,7,15]`（优势 4）；`nums1 = [12,24,8,32], nums2 = [13,25,32,11]` → `[24,32,8,12]`

**思路**：
- 这是"田忌赛马"：把 `nums1` 升序排好，`nums2` 按**值降序**处理（同时记住原下标，因为最终要放回原位置）。
- 双指针 `l` 指向 `nums1` 最小值、`r` 指向最大值。对 `nums2` 当前最大的那个位置：
  - 若 `nums1[r] > nums2[i]`，就用最大值去赢它（**能赢的最大值留着专打硬仗**），`r--`；
  - 否则说明连最大值都赢不了，这个位置必输，用**最小值**去"送"（牺牲最小代价），`l++`。
- **为什么正确**：`nums2` 的最大值最难对付，若 `nums1` 的最大值能赢它，用它去赢绝不劣于用更小的值（小的留着可以赢更多弱对手）；若赢不了，这个位置无论如何都输，用最小值送掉能保留大值去对付其他位置。这是标准的交换论证。
- 为什么必须按 `nums2` 降序：从最难的位置开始决策，保证"必输位"用最小代价填，避免大材小用。

**代码**：
```javascript
function advantageCount(nums1, nums2) {
  const sorted = [...nums1].sort((a, b) => a - b);
  // 按 nums2 的值降序拿下标，值相同则按下标升序（保证稳定）
  const order = nums2
    .map((_, i) => i)
    .sort((i, j) => nums2[j] - nums2[i] || i - j);

  const res = new Array(nums1.length);
  let l = 0, r = sorted.length - 1;

  for (const i of order) {
    if (sorted[r] > nums2[i]) res[i] = sorted[r--]; // 最大能赢，就正面刚
    else res[i] = sorted[l++];                      // 赢不了，用最小去送
  }
  return res;
}
```

**复杂度**：时间 O(n log n)／空间 O(n)

**易错点**：
- 直接对 `nums2.sort()` 排序会丢失原下标，结果位置全错——必须排"下标数组"。
- 判定用 `>` 而不是 `>=`：题目定义优势是**严格大于**，相等不算赢。
- `nums1` 的每个元素都要用掉且只用一次，双指针 `l`/`r` 不能越界（循环次数恰为 n，天然安全）。
- 平局时选择"送"最小值而不是最大值，否则会浪费能赢其他位置的大值。

**变体与追问**：
- 求最大优势的**数目**而不是重排结果：同算法，最后统计 `res[i] > nums2[i]` 的个数。
- 相等也算赢（`>=`）：判定改符号即可，贪心结构不变。
- 要求输出**字典序最小**的最优解：需要额外维护可选集合，用有序多重集 + 二分，复杂度升到 O(n log n) 但常数更大。

---

