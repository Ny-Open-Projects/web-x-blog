---
title: 11 回溯与 DFS · 经典算法 20 题
date: 2026-11-24
categories: [经典算法]
tags: [前端面试, 笔试题, C, 回溯]
type: 笔试题
---

# 11 回溯与 DFS（C-201 ~ C-220）

> 笔试里唯一"代码只有 20 行、写错一个字符就零分"的板块。面试官不看你跑通没跑通，只看你会不会画决策树、敢不敢写剪枝。**识别特征**：题干出现"所有方案 / 所有组合 / 能否恰好凑成 / 棋盘填满"，且数据规模 ≤ 20（因为解空间是指数级），就该想到回溯。

## 题型速查

| 子类型 | 核心手法 | 代表题 |
|---|---|---|
| 排列（顺序有关） | `used[]` 标记 + 每层全遍历 | C-201 |
| 组合 / 子集（顺序无关） | `start` 索引，下一层从 `i+1` 或 `i` 开始 | C-203、C-207 |
| 含重复元素去重 | 先排序，同层跳过 `i>start && a[i]===a[i-1]` | C-202、C-205、C-208 |
| 切割型 | 枚举"下一刀"位置，判断子串合法性 | C-212、C-213 |
| 棋盘型 | 逐格试放 + 冲突集合（列/对角线/宫） | C-214、C-215 |
| 划分型 | 把元素往 k 个桶里放，桶和相等才放 | C-218、C-219 |
| 方案计数（顺序有关） | 回溯必超时，转一维 DP | C-216 |
| 记忆化 DFS | 两个分支 + `Map` 缓存 `(下标, 状态)` | C-220 |

**三条铁律**：① 做选择 → 递归 → 撤销选择，三步缺一不可；② 收集答案必须深/浅拷贝；③ 去重靠"排序 + 同层判断"，不是靠 Set 事后去重。

---

### C-201 全排列 · 中等 · 字节/阿里/腾讯

**题干**：给定一个**不含重复数字**的数组 `nums`，返回其所有可能的全排列，顺序不限。约定 `1 <= nums.length <= 6`，`-10 <= nums[i] <= 10` 且互不相同。

**示例**：`输入: nums = [1,2,3]` → `输出: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

**思路**：
- 决策树：第 `i` 层决定"结果的第 `i` 位放哪个数"，因此每层要扫描全部元素，只跳过已经被祖先层用掉的。
- 为什么用 `used[]` 而不是 `path.includes(x)`：`includes` 每次 O(n)，把总复杂度从 O(n·n!) 抬到 O(n²·n!)；也不要用 `splice` 删元素，那会破坏入参且每次拷贝数组。
- 收集答案必须写 `res.push([...path])`。若直接 `push(path)`，存进去的是同一个引用，回溯时 `pop()` 会把所有结果一起清空，最后得到一堆空数组——这是本题第一大挂科点。
- `path.pop()` 与 `used[i] = false` 必须成对且放在递归返回之后，无论递归内部是否 return 都要执行。

**代码**：
```javascript
function permute(nums) {
  const res = [];
  const path = [];
  const used = new Array(nums.length).fill(false);

  const dfs = () => {
    if (path.length === nums.length) {
      res.push([...path]);            // 必须拷贝，否则被后续回溯改写
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;          // 已经在路径里
      used[i] = true;                 // 做选择
      path.push(nums[i]);
      dfs();                          // 递归
      path.pop();                     // 撤销选择
      used[i] = false;
    }
  };

  dfs();
  return res;
}
```

**复杂度**：时间 O(n·n!)，共 n! 个叶子、每个叶子拷贝长度 n；空间 O(n)，递归栈与 `used` 均为 n 量级（不计结果集）。

**易错点**：
- `res.push(path)` 少写展开运算符，结果全空。
- 撤销时只 `path.pop()` 忘了 `used[i] = false`，导致后续分支可用元素越来越少。
- 在 `for` 循环里用 `path.includes(nums[i])` 判重，复杂度悄悄超时。
- 递归深度等于 n，本题 n ≤ 6 无虞；若换成 n = 12 的变体，要注意 JS 引擎的调用栈上限。

**变体与追问**：
- 含重复数字 → C-202，加一行"同层跳过"。
- 只要第 k 个排列（LeetCode 60）：用康托展开或逐位确定，别真的生成全部。
- 字符串排列（剑指 Offer 38）：把 `nums` 换成 `[...str]` 即可，注意裁剪重复字符。

---

### C-202 全排列 II · 中等 · 字节/美团

**题干**：给定一个**可能包含重复数字**的序列 `nums`，返回所有**不重复**的全排列。`1 <= nums.length <= 8`。

**示例**：`输入: nums = [1,1,2]` → `输出: [[1,1,2],[1,2,1],[2,1,1]]`

**思路**：
- 只加 `used[]` 是不够的：两个 `1` 互换位置会产生两条一模一样的路径，结果重复且数量翻倍。
- 解法是**先排序**，让相同数字相邻，然后在同一层做剪枝：`i > 0 && nums[i] === nums[i-1] && !used[i-1]` 就 `continue`。
- 为什么要 `!used[i-1]`：这表示"前一个相同数字在这一层没被选"，说明当前分支是重复分支。若 `used[i-1]` 为 true，说明前一个相同数字在**祖先层**已被使用，此时必须允许选当前这个，否则 `[1,1,2]` 这种合法排列会被误杀。
- 记忆口诀：**"同层去重，同枝保留"**。剪枝条件判的是"同一层里相同值的第二个及以后"。

**代码**：
```javascript
function permuteUnique(nums) {
  nums.sort((a, b) => a - b);         // 排序让相同元素相邻
  const res = [];
  const path = [];
  const used = new Array(nums.length).fill(false);

  const dfs = () => {
    if (path.length === nums.length) {
      res.push([...path]);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      // 同一层出现相同值，且前一个没被用过 → 重复分支，跳过
      if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue;

      used[i] = true;
      path.push(nums[i]);
      dfs();
      path.pop();
      used[i] = false;
    }
  };

  dfs();
  return res;
}
```

**复杂度**：时间 O(n·n!)，最坏仍是全排列量级（去重只减少常数与重复枝）；空间 O(n)。

**易错点**：
- 漏写 `!used[i-1]`，结果从"重复"变成"缺解"，`[1,1,2]` 只剩 `[1,2,1]` 之类。
- 把条件写成 `used[i-1]`（没取反），逻辑正好相反。
- 忘了排序，`nums[i] === nums[i-1]` 根本不相邻，去重完全失效。
- 用 `JSON.stringify` 塞进 Set 事后去重：能过但复杂度爆炸，面试会被追问。

**变体与追问**：
- 字符串有重复字符的全排列（剪枝写法完全一致，排序对象换成字符数组）。
- 若要求按字典序输出，则不能简单排序后 DFS，需要按字符集顺序逐位构造。

---

### C-203 组合 · 中等 · 阿里/快手

**题干**：给定两个整数 `n` 和 `k`，返回 `1..n` 中所有可能的 `k` 个数的组合，顺序不限。`1 <= n <= 20`，`1 <= k <= n`。

**示例**：`输入: n = 4, k = 2` → `输出: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`

**思路**：
- 与排列的根本差别：组合不关心顺序，`[1,2]` 与 `[2,1]` 是同一个解。所以引入 `start`，下一层只能从 `i+1` 往后选，天然保证结果递增、不重复。
- 这也是为什么组合类问题**不需要 `used[]`**：`start` 已经承担了"哪些还能选"的信息。
- 剪枝：当 `i` 太大、剩余元素数量不足以填满还需的位数时，直接不进循环。上界是 `n - (k - path.length) + 1`，能砍掉大量无效叶子。
- 递归出口只有一个：`path.length === k` 时收集并返回，不需要再判 `start`。
- 自测信号：结果个数必须恰好等于 `C(n,k)`。若偏多，说明 `start` 传错（多乘了阶乘）；若偏少，多半是剪枝上界写小了一格。

**代码**：
```javascript
function combine(n, k) {
  const res = [];
  const path = [];

  const dfs = (start) => {
    if (path.length === k) {
      res.push([...path]);
      return;
    }
    // 还需要 need 个，i 最多只能到 n - need + 1
    const need = k - path.length;
    for (let i = start; i <= n - need + 1; i++) {
      path.push(i);        // 做选择
      dfs(i + 1);          // 下一层只能选更大的，避免重复组合
      path.pop();          // 撤销
    }
  };

  dfs(1);
  return res;
}
```

**复杂度**：时间 O(k·C(n,k))，共 C(n,k) 个解、每个解拷贝 k 个元素；空间 O(k) 递归栈。

**易错点**：
- `dfs(i)` 写成 `dfs(i + 1)` 的反面（即传 `i` 而非 `i+1`），组合会变成"可重复选"，结果集错误膨胀。
- 剪枝上界写成 `n - need`，会少一个合法分支（差一错误）。
- `start` 从 0 开始传，导致 `0` 被选进结果。
- `k > n` 时无解，虽然循环条件 `i <= n - need + 1` 会让它自然返回 `[]`，但入口显式判一下更易读。

**变体与追问**：
- 组合总和 I/II/III（C-204/205/206）：在组合骨架上加"和"的约束。
- 子集（C-207）：把"收集时机"从叶子提到每个节点。
- 求组合数而不枚举：直接算 `C(n,k)`，别 DFS。

---

### C-204 组合总和 · 中等 · 字节/腾讯/美团

**题干**：给定**无重复元素**的数组 `candidates` 和目标数 `target`，找出所有和为 `target` 的组合。同一个数字**可以被无限制重复选取**。解集不能包含重复组合。`1 <= candidates.length <= 30`，`2 <= candidates[i] <= 40`。

**示例**：`输入: candidates = [2,3,6,7], target = 7` → `输出: [[2,2,3],[7]]`

**思路**：
- 组合骨架 + 求和约束：递归参数从"还剩几位"变成"还剩多少和"（`rest`），`rest === 0` 即收集。
- **允许重复选自己**的关键就是把 `dfs(i + 1)` 改成 `dfs(i)`：下一层仍可从当前元素开始，于是 `2` 可以被选多次。
- 为什么必须排序：排序后 `candidates[i] > rest` 时可以直接 `break`——后面的元素只会更大，整条右半边分支都不可能凑出 `rest`。这个剪枝把指数级搜索砍掉一大半。
- 不需要 `used`、不需要同层去重：因为 `i >= start` 已经保证每个组合按非递减下标生成，`[2,3]` 和 `[3,2]` 只会出现前者。

**代码**：
```javascript
function combinationSum(candidates, target) {
  candidates.sort((a, b) => a - b);     // 排序是剪枝前提
  const res = [];
  const path = [];

  const dfs = (start, rest) => {
    if (rest === 0) {
      res.push([...path]);
      return;
    }
    for (let i = start; i < candidates.length; i++) {
      if (candidates[i] > rest) break;  // 后面只会更大，直接剪掉
      path.push(candidates[i]);         // 做选择
      dfs(i, rest - candidates[i]);     // 传 i：允许重复选当前元素
      path.pop();                       // 撤销
    }
  };

  dfs(0, target);
  return res;
}
```

**复杂度**：时间 O(S)，S 为所有解的节点总数（最坏指数级，约 O(n^(target/min))），有排序后剪枝远小于上界；空间 O(target/min) 递归深度。

**易错点**：
- 把 `dfs(i)` 写成 `dfs(i + 1)`，退化成"每个数只能用一次"，漏解。
- 忘记排序却写了 `break`：遇到乱序数组会提前终止，直接漏解（要么排序，要么改 `continue`）。
- 用 `rest < 0` 做出口而不是 `break`，多跑大量无效递归，面试官会问复杂度为什么退化。

**变体与追问**：
- 元素有重复且只能用一次 → C-205，需要"排序 + 同层跳过"。
- 只能用 1~9 且限定个数 → C-206。
- 求方案**数量**（元素顺序不同算不同方案）→ C-216，回溯会超时，必须转 DP。

---

### C-205 组合总和 II · 中等 · 字节/阿里

**题干**：给定**可能含重复元素**的数组 `candidates` 和目标数 `target`，每个数字**只能使用一次**，找出所有和为 `target` 的不重复组合。`1 <= candidates.length <= 100`，`1 <= candidates[i] <= 50`。

**示例**：`输入: candidates = [10,1,2,7,6,1,5], target = 8` → `输出: [[1,1,6],[1,2,5],[1,7],[2,6]]`

**思路**：
- 在 C-204 上改两点：`dfs(i + 1)`（每个数只用一次）+ 去重。
- 去重条件与全排列 II 同源但**判的是 `i > start` 而不是 `i > 0`**：组合的每一层候选区间是 `[start, n)`，同层重复只可能发生在该区间内相邻的相同值上。写成 `i > 0` 会把"跨层使用相同值"也剪掉，导致 `[1,1,6]` 这类解丢失。
- 直观理解：这一层已经用值 `v` 开过分支了，再遇到 `v` 必然生成完全相同的子树，直接跳过。
- 复杂度名义上是 O(2^n)，但 `candidates[i] > rest` 的 break 会把大量右子树整段砍掉，实际远小于上界，`n = 100` 的极端用例也能过。
- `break` 条件仍是 `candidates[i] > rest`（排序前提下）。

**代码**：
```javascript
function combinationSum2(candidates, target) {
  candidates.sort((a, b) => a - b);
  const res = [];
  const path = [];

  const dfs = (start, rest) => {
    if (rest === 0) {
      res.push([...path]);
      return;
    }
    for (let i = start; i < candidates.length; i++) {
      if (candidates[i] > rest) break;                 // 排序剪枝
      // 同一层里相同值只用第一个，i > start 是组合题的正确边界
      if (i > start && candidates[i] === candidates[i - 1]) continue;

      path.push(candidates[i]);                        // 做选择
      dfs(i + 1, rest - candidates[i]);                // 每个数只能用一次
      path.pop();                                      // 撤销
    }
  };

  dfs(0, target);
  return res;
}
```

**复杂度**：时间 O(2^n) 上界（每个元素选或不选），带剪枝实际远小；空间 O(n)。

**易错点**：
- 去重条件写成 `i > 0`：跨层误剪，`[1,1,6]` 丢失。
- 忘了 `sort`，重复元素不相邻，去重失效。
- 写成 `dfs(i, ...)`（可重复选），与"每个数只能用一次"的题意冲突。
- 用 `Set` 存 `path.join()` 事后去重：能过但既慢又体现不出剪枝思维。

**变体与追问**：
- 若允许每个数用无限次但数组有重复（LeetCode 变体）：需同时处理"用自己"和"同层去重"，`dfs(i)` + `i > start` 跳过。
- 求方案数而非方案列表：直接 DP（0-1 背包计数），注意外层循环顺序。

---
### C-206 组合总和 III · 中等 · 阿里/腾讯

**题干**：找出所有相加之和为 `n` 的 `k` 个数的组合，只使用数字 `1..9`，每个数字最多使用一次，解集不能重复。`2 <= k <= 9`，`1 <= n <= 60`。

**示例**：`输入: k = 3, n = 7` → `输出: [[1,2,4]]`；`输入: k = 3, n = 9` → `输出: [[1,2,6],[1,3,5],[2,3,4]]`

**思路**：
- 这是 C-203（限定个数）与 C-204（限定和）的交集：递归同时带"已选个数"和"剩余和"两个约束。
- 出口要**先判个数再判和**：`path.length === k` 时无论和是否为 0 都必须 return，否则会在凑够 k 个后继续往下选，产生长度超标的解。
- 剪枝有两层：`i > rest` 时 `break`（排序天然成立，因为候选就是递增的 1..9）；以及剩余数字不够填满 `k` 位时也可以提前退出。只写第一层也能过，但面试官常追问第二层。
- 因为候选集合固定为 1..9 且严格递增，本题不需要 `used`，也不需要去重逻辑。

**代码**：
```javascript
function combinationSum3(k, n) {
  const res = [];
  const path = [];

  const dfs = (start, rest) => {
    if (path.length === k) {
      if (rest === 0) res.push([...path]);  // 个数够了才判和
      return;
    }
    // 还需要 need 个数字，至少要 need 个不同的数
    const need = k - path.length;
    for (let i = start; i <= 9 - need + 1; i++) {
      if (i > rest) break;                 // 再选只会更大
      path.push(i);                        // 做选择
      dfs(i + 1, rest - i);                // 每个数字只能用一次
      path.pop();                          // 撤销
    }
  };

  dfs(1, n);
  return res;
}
```

**复杂度**：时间 O(C(9,k)·k)，最多 9 选 k 的枚举量；空间 O(k)。

**易错点**：
- 出口只判 `rest === 0` 不判个数：`k=3, n=3` 时会把 `[3]` 也收进结果；只判个数不判和，又会收入一堆和不对的解。两个条件必须同时成立。
- 忘记 `need` 剪枝，`k=9, n=45` 时也要跑满整棵树。
- `start` 从 0 开始，把 `0` 选进去，答案出现非法数字。
- `n` 小于 `1+2+...+k` 时必然无解，剪枝能兜住，但显式判断能让思路更完整。

**变体与追问**：
- 不限定个数只限定和 → C-204。
- 候选不是 1..9 而是任意数组 → 变成"限定个数 + 限定和"的通用模板，需排序去重。

---

### C-207 子集 · 中等 · 字节/腾讯/拼多多

**题干**：给定**互不相同**的整数数组 `nums`，返回其所有可能的子集（幂集），解集不能包含重复子集，顺序不限。`1 <= nums.length <= 10`。

**示例**：`输入: nums = [1,2,3]` → `输出: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`

**思路**：
- 子集 = 组合的"所有长度"版本。因此**收集时机从叶子提前到每个节点**：进入 `dfs` 的第一件事就是把当前 `path` 收进结果。
- 为什么这样能覆盖全部 2^n 个解：每个元素在每一层只有"选 / 不选"两种命运，`for` 循环枚举了"下一个选谁"，`start` 保证下标递增，于是每条从根到任意节点的路径恰好对应一个子集。
- 与 C-203 的差别只在出口：组合题在 `path.length === k` 时收集，子集题在函数入口收集且永不 return（循环自然结束）。
- 复杂度上界 2^n 个解，每个解平均长度 n/2，所以是 O(n·2^n)。
- 递归树长这样：根是 `[]`，第一层是 n 个单元素子集，深度最多 n，**每个节点都对应一个合法解**，节点总数正好 2^n。这也解释了为什么收集动作要放在函数入口而不是叶子。

**代码**：
```javascript
function subsets(nums) {
  const res = [];
  const path = [];

  const dfs = (start) => {
    res.push([...path]);          // 每个节点都是一个合法子集
    for (let i = start; i < nums.length; i++) {
      path.push(nums[i]);         // 做选择
      dfs(i + 1);                 // 下一层从 i+1 开始，保证不重复
      path.pop();                 // 撤销
    }
  };

  dfs(0);
  return res;
}

// 位运算写法（n <= 20 时更快）：
// for (let mask = 0; mask < (1 << n); mask++) { ... }
```

**复杂度**：时间 O(n·2^n)；空间 O(n) 递归栈。

**易错点**：
- 把 `res.push` 写在 `path.length === n` 的出口里，只得到"全选"一个结果。
- `dfs(i)` 而不是 `dfs(i + 1)`，会生成无限递归（start 不前进）。
- 用 `path` 直接 push 未拷贝，结果全变成最后一次的 `[]`。

**变体与追问**：
- 含重复元素 → C-208。
- 只要大小为 k 的子集 → C-203。
- 要求按字典序、且 `[1,2]` 在 `[1,2,3]` 前：当前 DFS 顺序天然满足。

---

### C-208 子集 II · 中等 · 字节/美团

**题干**：给定**可能包含重复元素**的整数数组 `nums`，返回所有不重复的子集（幂集）。`1 <= nums.length <= 10`。

**示例**：`输入: nums = [1,2,2]` → `输出: [[],[1],[1,2],[1,2,2],[2],[2,2]]`

**思路**：
- 在 C-207 上加去重，写法与 C-205 完全一致：排序 + `i > start && nums[i] === nums[i-1]` 跳过。
- 为什么这样能去重：`[1,2]`（用第一个 2）和 `[1,2]`（用第二个 2）在结果上不可区分。强制"相同值只允许按从左到右的顺序被选"，即同层只用第一个，就能保证每个多元素组合只被生成一次。
- 与全排列 II 的 `!used[i-1]` 是同一思想的两种表达：排列题用 `used` 判"是否在同一层"，子集题用 `start` 判"是否是本层第一个相同值"。
- 边界：`[2,2]` 仍然合法——第二个 2 在 `i > start` 时被选，此时 `i === start` 分支先走完，深度下探后可以继续选第二个 2。
- 因此去重只发生在"同一层横向展开"时，纵向深入时相同值可以连用，这正是"同层去重、同枝保留"的含义。

**代码**：
```javascript
function subsetsWithDup(nums) {
  nums.sort((a, b) => a - b);        // 去重的前提
  const res = [];
  const path = [];

  const dfs = (start) => {
    res.push([...path]);
    for (let i = start; i < nums.length; i++) {
      // 同一层里相同值只用第一个分支
      if (i > start && nums[i] === nums[i - 1]) continue;

      path.push(nums[i]);            // 做选择
      dfs(i + 1);                    // 递归
      path.pop();                    // 撤销
    }
  };

  dfs(0);
  return res;
}
```

**复杂度**：时间 O(n·2^n)；空间 O(n)。

**易错点**：
- 条件写成 `i > 0`：跨层误剪，`[1,2,2]` 中的 `[2,2]` 会消失。
- 未排序 → 重复元素不相邻，去重完全失效。
- 把 `continue` 写成 `break`：相同值后面可能还跟着别的值（如 `[2,2,3]` 里的 3），`break` 会连带跳过，直接漏解。
- 用 Set 对 `path.join(',')` 去重：遇到 `[1,12]` 与 `[11,2]` 之类可拼接歧义（本题数字范围小一般不出错，但思路不严谨）。

**变体与追问**：
- 若数值范围有限（如 `-10..10`），可用 `usedValue` 数组代替排序，做到"同层不重复枚举同一值"。
- 与 C-202 对比记忆：排列靠 `used`，组合/子集靠 `start`。

---

### C-209 电话号码的字母组合 · 中等 · 腾讯/快手

**题干**：给定一个仅包含数字 `2-9` 的字符串 `digits`，返回它能表示的所有字母组合。数字到字母的映射与电话按键相同（2→abc，3→def，…，7→pqrs，8→tuv，9→wxyz）。`0 <= digits.length <= 4`。

**示例**：`输入: digits = "23"` → `输出: ["ad","ae","af","bd","be","bf","cd","ce","cf"]`；`输入: digits = ""` → `输出: []`

**思路**：
- 这是"多集合笛卡尔积"，决策树的层号就是 `digits` 的下标，每层从对应字母集合中选一个。
- 与前面题目的区别：候选集**由当前层决定**，不是全局数组，所以不需要 `start` 也不需要 `used`，只需要层号 `idx`。
- 出口是 `idx === digits.length`，此时 `path` 长度必然等于 `digits.length`，`join('')` 即为一个解。
- 空串必须单独返回 `[]` 而不是 `['']`——这是本题最常见的判空错误。
- 为什么不需要 `start`：每层候选完全由 `digits[idx]` 决定，层与层之间没有"已用"概念，同一个字母允许在不同位置重复出现（比如 `"22"` 能拼出 `"aa"`）。

**代码**：
```javascript
function letterCombinations(digits) {
  if (digits.length === 0) return [];       // 空输入返回空数组，不是 ['']
  const MAP = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'];
  const res = [];
  const path = [];

  const dfs = (idx) => {
    if (idx === digits.length) {
      res.push(path.join(''));
      return;
    }
    const letters = MAP[Number(digits[idx])];  // 本层可选字母
    for (const ch of letters) {
      path.push(ch);                            // 做选择
      dfs(idx + 1);                             // 进入下一层
      path.pop();                               // 撤销
    }
  };

  dfs(0);
  return res;
}
```

**复杂度**：时间 O(4^n·n)，n 为 `digits` 长度，每层最多 4 个分支，叶子处 `join` 为 O(n)；空间 O(n)。

**易错点**：
- 空串返回 `['']`：长度为 1，测试用例直接挂。
- 用 `MAP[digits[idx]]` 下标取数组，字符串下标得到 `undefined`（必须 `Number()` 转换）。
- 把 `path` 当字符串累加却漏了回溯（字符串不可变，用 `path + ch` 传参也可以，但要明确不可变语义）。

**变体与追问**：
- 若按键还包含 `0`、`1`（空格等），映射表要扩展。
- 要求按字典序输出：把每个字母集合本身有序即可，`abc/def` 天然有序。
- 求组合总数而不枚举：直接连乘各层字母数。

---

### C-210 括号生成 · 中等 · 字节/阿里/腾讯

**题干**：数字 `n` 代表生成括号的对数，请设计函数生成所有**有效**的括号组合。`1 <= n <= 8`。

**示例**：`输入: n = 3` → `输出: ["((()))","(()())","(())()","()(())","()()()"]`

**思路**：
- 不用先生成 2^(2n) 个串再校验（那是 O(2^2n·n) 的暴力），而是在构造过程中就保证前缀合法，只走"能走通"的枝。
- 合法前缀的两个不变量：① 已用左括号数 `open <= n`；② 任意前缀中右括号数不能超过左括号数，即 `close < open` 才能放 `)`。
- 这两个条件同时充当"可行性剪枝"和"合法性校验"，所以搜到的每个叶子都是答案，不需要事后验证。
- 解的数量是第 n 个卡特兰数 `C(2n,n)/(n+1)`，n=8 时 1430 个，规模可控。
- 两个 `if` 必须**并列**而不是 `else if`：当 `open < n` 与 `close < open` 同时成立时，两条分支都合法（既能放左也能放右），写成 `else` 会漏掉一半解。

**代码**：
```javascript
function generateParenthesis(n) {
  const res = [];
  const path = [];

  const dfs = (open, close) => {
    if (path.length === 2 * n) {
      res.push(path.join(''));
      return;
    }
    if (open < n) {                 // 左括号还有配额
      path.push('(');
      dfs(open + 1, close);
      path.pop();
    }
    if (close < open) {             // 右括号不能多于左括号
      path.push(')');
      dfs(open, close + 1);
      path.pop();
    }
  };

  dfs(0, 0);
  return res;
}
```

**复杂度**：时间 O(4^n/√n)（卡特兰数量级，每个解长度 2n）；空间 O(n) 递归深度。

**易错点**：
- 只写 `open < n` 忘了 `close < open`，会生成 `")("` 这类非法串。
- 把条件写成 `close < n`，同样产出非法解。
- 递归出口用 `open === n && close === n` 与 `path.length === 2n` 等价，但若只判 `open === n` 会提前截断。
- 用 Set 存结果去重：本题不会重复，纯属浪费。

**变体与追问**：
- 判断单个括号串是否有效（LeetCode 20）：栈，遇右括号弹栈。
- 求最少添加多少个括号使其有效（LeetCode 921）：贪心计未匹配数。
- 只要第 k 个括号串：按卡特兰数逐位计数（组合数学），不建议 DFS。

---
### C-211 单词搜索 · 中等 · 字节/腾讯/美团

**题干**：给定 `m x n` 的字符网格 `board` 和一个字符串 `word`，判断 `word` 是否存在于网格中。单词必须由**相邻格子**（水平或垂直，上下左右）的字母按顺序构成，**同一个格子不能重复使用**。`1 <= m, n <= 6`，`1 <= word.length <= 15`。

**示例**：`输入: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"` → `输出: true`

**思路**：
- 决策树：起点遍历全部格子，之后每层向四个方向扩展，层号 `k` 就是已匹配到 `word` 的第几个字符。
- "不能重复使用同一格"用**原地标记**实现：进入时把 `board[i][j]` 改成 `'#'` 之类不可能匹配的字符，四个方向递归后再改回来。这比额外 `visited[m][n]` 省空间，也避免每次递归拷贝。
- 剪枝顺序很重要：先判越界、再判字符不匹配，两个都不过就直接返回 false，避免无谓的标记/撤销。
- 只要存在一条路径就返回 true，所以四个方向用 `||` 短路，找到即可提前结束。

**代码**：
```javascript
function exist(board, word) {
  const m = board.length;
  const n = board[0].length;

  const dfs = (i, j, k) => {
    if (k === word.length) return true;                       // 全部匹配完
    if (i < 0 || i >= m || j < 0 || j >= n) return false;     // 越界
    if (board[i][j] !== word[k]) return false;                // 字符不符

    const ch = board[i][j];
    board[i][j] = '#';                                        // 标记已访问
    const ok =
      dfs(i + 1, j, k + 1) || dfs(i - 1, j, k + 1) ||
      dfs(i, j + 1, k + 1) || dfs(i, j - 1, k + 1);
    board[i][j] = ch;                                         // 回溯恢复

    return ok;
  };

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (dfs(i, j, 0)) return true;
    }
  }
  return false;
}
```

**复杂度**：时间 O(m·n·4^L)，L 为单词长度，每个起点最多 4^L 条路径；空间 O(L) 递归栈。

**易错点**：
- 忘记恢复 `board[i][j] = ch`：一条路径失败后整块棋盘被永久污染，后续起点全部失效。
- 先标记再判字符（顺序颠倒），会把不匹配的格子也标记掉。
- 用 `visited` 数组但只在入参拷贝时重置，导致同一层不同分支互相污染。
- 递归出口写成 `k === word.length - 1`，最后一个字符没校验。

**变体与追问**：
- 需要返回**所有**单词（LeetCode 212 单词搜索 II）：把词典建 Trie，DFS 时沿 Trie 走，命中即收集并剪枝。
- 允许八个方向（含对角）时，方向数组扩成 8 个。
- 若网格可重复走，问题性质改变，通常需要用状态压缩 BFS。

---

### C-212 分割回文串 · 中等 · 字节/阿里/快手

**题干**：给定字符串 `s`，将 `s` 分割成若干**回文子串**，返回所有可能的分割方案。`1 <= s.length <= 16`。

**示例**：`输入: s = "aab"` → `输出: [["a","a","b"],["aa","b"]]`

**思路**：
- 这是典型的**切割型回溯**：决策不是"选哪个元素"，而是"这一刀切在哪里"。`start` 表示当前子串的起点，`for` 枚举终点 `end`，切出 `s[start..end]`。
- 只有当前子串是回文才继续递归，否则这一刀无效。这个约束天然完成剪枝：非回文前缀不会进入下一层。
- 出口是 `start === s.length`，说明切到了末尾，此时 `path` 就是一组合法分割。
- 为什么出口判 `start` 而不是最后一段的 `end`：`start` 表示"下一段从哪开始"，当它越过末尾就说明前面每一段都切完了；用 `end` 判断会漏掉"最后一段单独成解"的情形。
- 回文判断可以用双指针 O(len)，也可以预处理 `dp[i][j]` 表示区间是否回文，把整体从 O(n·2^n·n) 降到 O(n·2^n)。长度 ≤ 16 时双指针足够。

**代码**：
```javascript
function partition(s) {
  const res = [];
  const path = [];

  const isPalindrome = (l, r) => {
    while (l < r) {
      if (s[l++] !== s[r--]) return false;
    }
    return true;
  };

  const dfs = (start) => {
    if (start === s.length) {
      res.push([...path]);          // 切到末尾，记录方案
      return;
    }
    for (let end = start; end < s.length; end++) {
      if (!isPalindrome(start, end)) continue;   // 这一刀切出非回文，跳过
      path.push(s.slice(start, end + 1));        // 做选择
      dfs(end + 1);                              // 从下一段起点继续
      path.pop();                                // 撤销
    }
  };

  dfs(0);
  return res;
}
```

**复杂度**：时间 O(n·2^n)（2^(n-1) 种切法，每种校验 O(n)）；空间 O(n) 递归深度。

**易错点**：
- `dfs(end)` 写成 `dfs(end + 1)` 的反面（传 `end`），会切出重叠子串甚至死递归。
- 忘记 `slice(start, end + 1)` 的 `+1`，每段少一个字符。
- 出口写成 `start >= s.length` 之外的判断（如 `path.join('').length === s.length`），既慢又易错。
- 用全局变量缓存回文结果但未按 `(l, r)` 建键，导致误判。

**变体与追问**：
- 只求**最少切割次数**（LeetCode 132）：回溯必超时，必须 `dp[i] = min(dp[j] + 1)` 且预处理回文表。
- 分割成 k 段且每段回文：加一维"已切段数"。
- 允许最多删 k 个字符使整体回文：区间 DP。

---

### C-213 复原 IP 地址 · 中等 · 字节/腾讯

**题干**：给定一个只包含数字的字符串 `s`，返回所有可能的**有效 IP 地址**，形式上为四个 0~255 的整数用 `.` 分隔。每段**不允许前导零**（`"0"` 合法，`"01"` 非法）。`1 <= s.length <= 20`。

**示例**：`输入: s = "25525511135"` → `输出: ["255.255.11.135","255.255.111.35"]`

**思路**：
- 切割型回溯的变体：固定切 4 段，`segs` 记录已切出的段，`start` 是当前段起点。
- 三层约束同时生效：段数恰好 4、每段 1~3 位、数值 ≤ 255 且无前导零。
- 强剪枝：剩余字符数 `left` 必须落在 `[need, need*3]`，其中 `need = 4 - segs.length`。不加这条，长度 20 的串会枚举大量废枝。
- 前导零的处理：当 `end > start && s[start] === '0'` 时直接 `break`——以 0 开头的段只能是单个 "0"，再往后延必然非法。
- 数值累加用 `num * 10 + digit` 而不是每轮 `Number(s.slice(...))`：后者每次切片 O(len)，且无法在"刚超过 255"时立刻 `break`，剪枝会失效。

**代码**：
```javascript
function restoreIpAddresses(s) {
  const res = [];
  const segs = [];

  const dfs = (start) => {
    const need = 4 - segs.length;
    const left = s.length - start;
    if (left < need || left > need * 3) return;      // 剩余长度不可能切够
    if (segs.length === 4) {
      if (start === s.length) res.push(segs.join('.'));
      return;
    }

    let num = 0;
    for (let end = start; end < start + 3 && end < s.length; end++) {
      if (end > start && s[start] === '0') break;    // 前导零，本段非法
      num = num * 10 + Number(s[end]);
      if (num > 255) break;                          // 超过 255，再延只会更大

      segs.push(s.slice(start, end + 1));            // 做选择
      dfs(end + 1);                                  // 递归
      segs.pop();                                    // 撤销
    }
  };

  dfs(0);
  return res;
}
```

**复杂度**：时间 O(3^4·n) = O(n)，切法最多 3^4 种、每次拼接 O(n)；空间 O(1) 递归（深度固定 4）。

**易错点**：
- 漏掉前导零判断：`"010010"` 会切出 `"01.0.0.10"` 这类非法地址，答案多出一批错误项。
- `num > 255` 用 `continue` 而不是 `break`，多跑无意义分支（虽然结果不错）。
- 忘记 `left` 剪枝，`s` 很长时递归爆栈。
- 收集时 `res.push(segs)` 未 `join`，输出成了嵌套数组。
- 若要求输出按字典序，收集后 `res.sort()` 即可，因为每一段都是从左到右切出来的，天然不会重复。

**变体与追问**：
- 若允许 5 段（IPv6 风格）则不适用本题，但模板只需改 `need` 常量。
- 判断给定字符串是否是合法 IPv4（LeetCode 468）：直接按 `.` 切并逐段校验。
- 求方案数而不列举：DP 统计 `f[i][k]`。

---

### C-214 N 皇后 · 困难 · 字节/阿里/腾讯

**题干**：将 `n` 个皇后放在 `n x n` 棋盘上，使任意两个皇后不在同一行、同一列、同一斜线上。返回所有不同的解法，用 `Q` 和 `.` 表示棋盘。`1 <= n <= 9`。

**示例**：`输入: n = 4` → `输出: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]`

**思路**：
- 关键建模：**按行放置**。一行只放一个皇后，于是"行冲突"被结构性消除，每层只需决定"这一行的皇后放哪一列"。
- 冲突用三个集合 O(1) 判断：列 `col`、主对角线 `row - col`（同一条上该值恒定）、副对角线 `row + col`（同理）。为什么是这两个式子：主对角线方向 `(r,c)` 满足 `r-c` 相同，副对角线满足 `r+c` 相同，用 Set 就免去了扫描。
- 试探 → 递归 → 撤销，三个集合的增删必须与棋盘的落子/撤销严格配对。
- 剪枝就是"冲突即跳过"，因此搜索树被压到很小，n=9 也能秒出。

**代码**：
```javascript
function solveNQueens(n) {
  const res = [];
  const cols = new Set();
  const diag1 = new Set();   // 主对角线：row - col
  const diag2 = new Set();   // 副对角线：row + col
  const board = Array.from({ length: n }, () => new Array(n).fill('.'));

  const dfs = (row) => {
    if (row === n) {
      res.push(board.map((r) => r.join('')));   // 深拷贝成字符串数组
      return;
    }
    for (let col = 0; col < n; col++) {
      if (cols.has(col) || diag1.has(row - col) || diag2.has(row + col)) continue;

      cols.add(col); diag1.add(row - col); diag2.add(row + col);
      board[row][col] = 'Q';                    // 做选择
      dfs(row + 1);                             // 递归下一行
      board[row][col] = '.';                    // 撤销选择
      cols.delete(col); diag1.delete(row - col); diag2.delete(row + col);
    }
  };

  dfs(0);
  return res;
}
```

**复杂度**：时间 O(n!)，第 i 行最多 n-i 个可用列；空间 O(n) 递归栈 + O(n) 集合。

**易错点**：
- 只撤销 `board` 不撤销三个 Set，后续行全部被误判冲突。
- 对角线写成 `row + col` 与 `row - col + n` 混用（后者是数组下标写法，用 Set 时不能加偏移，否则主副对角线键空间混乱）。
- `res.push(board)` 存引用，最终所有解都变成同一块棋盘。
- 忘记"按行放"的前提，试图枚举行列组合，复杂度爆炸。

**变体与追问**：
- 只求方案数（LeetCode 52）：去掉棋盘构造，直接计数即可，n=9 也能过。
- 用位运算优化：`cols | (ld >> 1) | (rd << 1)` 表示可用列，速度提升 3~5 倍，是大厂"能否再快"的常见追问。
- 输出第一种解即可（LeetCode 51 变体）：找到即 return true 逐层上浮。

---

### C-215 解数独 · 困难 · 字节/阿里

**题干**：编写程序，填充 `9 x 9` 数独空格使其满足：每行、每列、每个 `3 x 3` 宫内数字 `1-9` 各出现一次。输入保证唯一解，空格用 `'.'` 表示。要求**原地修改** `board`。

**示例**：`输入: board = [["5","3",".",...],...]`（标准题面）→ `输出: board 被填充为合法数独`

**思路**：
- 枚举单位是"格子"：把 81 个位置线性编号 `pos`，每层填一个格子，填满即成功。
- 冲突检测用三组 Set：`rows[r]`、`cols[c]`、`boxes[3*(r/3)+c/3]`。初始化时把已给的数字全部登记，之后每次试填 O(1) 判冲突。
- 与 N 皇后最大的不同：本题只要**一个解**，所以递归函数返回 boolean，`if (dfs(pos+1)) return true;` 逐层短路上浮，找到即整体退出，不再撤销。
- 撤销时必须三处同步删除，否则后续分支会误判"数字已被占用"。

**代码**：
```javascript
function solveSudoku(board) {
  const rows = Array.from({ length: 9 }, () => new Set());
  const cols = Array.from({ length: 9 }, () => new Set());
  const boxes = Array.from({ length: 9 }, () => new Set());
  const boxId = (r, c) => Math.floor(r / 3) * 3 + Math.floor(c / 3);

  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      const v = board[r][c];
      if (v === '.') continue;
      rows[r].add(v); cols[c].add(v); boxes[boxId(r, c)].add(v);
    }
  }

  const dfs = (pos) => {
    if (pos === 81) return true;                 // 全部填完
    const r = Math.floor(pos / 9), c = pos % 9;
    if (board[r][c] !== '.') return dfs(pos + 1); // 预填格直接跳过

    const b = boxId(r, c);
    for (let d = 1; d <= 9; d++) {
      const v = String(d);
      if (rows[r].has(v) || cols[c].has(v) || boxes[b].has(v)) continue;

      board[r][c] = v; rows[r].add(v); cols[c].add(v); boxes[b].add(v);
      if (dfs(pos + 1)) return true;             // 找到一个解就上浮
      board[r][c] = '.'; rows[r].delete(v); cols[c].delete(v); boxes[b].delete(v);
    }
    return false;                                // 1-9 都试过，此路不通
  };

  dfs(0);
}
```

**复杂度**：时间 O(9^(空格数)) 上界，实际因冲突剪枝远小于此；空间 O(81) 递归栈 + O(81) 集合。

**易错点**：
- 找到解后仍继续搜索并撤销，最终棋盘被还原成初始状态。
- 只删 `rows` 忘了 `cols/boxes`，后续格子误判冲突，出现无解回溯。
- 预填格也进入 `for` 循环试填，覆盖了题目给定的数字。
- `boxId` 写成 `Math.floor(r/3) + Math.floor(c/3)*3`，行列颠倒仍能跑但语义错，调试时极易迷失。

**变体与追问**：
- 判断当前数独是否合法（LeetCode 36）：只校验不求解，一遍扫描即可。
- 求解数量：把返回值改成计数，且不短路。
- 优化：先填"候选数最少"的格子（MRV 启发式），可把最坏用例从秒级降到毫秒级。

---
### C-216 组合总和 IV · 中等 · 字节/美团

**题干**：给定**互不相同**的正整数数组 `nums` 和目标整数 `target`，求有多少种**排列**（顺序不同算不同方案）的元素之和等于 `target`。`1 <= nums.length <= 200`，`1 <= target <= 1000`，答案保证在 32 位整数范围内。

**示例**：`输入: nums = [1,2,3], target = 4` → `输出: 7`（`1111,112,121,13,211,22,31`）

**思路**：
- 注意与 C-204 的本质差异：本题求**方案数**且**顺序不同算不同方案**，解空间是排列级别，回溯在最坏情况（`nums=[1], target=1000`）会退化成指数级，必须转 DP。
- 定义 `dp[t]` = 凑出 `t` 的排列数，转移 `dp[t] = Σ dp[t - num]`。含义是"最后一个选的数是 `num`"，把排列按末位元素分类，天然不重不漏。
- **循环顺序是本题全部考点**：`target` 在外层、`nums` 在内层 → 排列数；反过来 `nums` 在外层 → 组合数。因为外层循环变量代表"阶段"，把 `nums` 放内层意味着每个阶段都可以重新挑任意元素，顺序就被计入了。
- `dp[0] = 1` 是空方案，作为递推基底，不能设成 0。

**代码**：
```javascript
function combinationSum4(nums, target) {
  // dp[t]：凑出和为 t 的排列方案数
  const dp = new Array(target + 1).fill(0);
  dp[0] = 1;                              // 空序列，一种方案

  // 循环顺序即语义：外层是"容量阶段"，内层是"最后一个数"
  // 若交换两层，含义变成组合数（顺序不再计入），答案会偏小
  for (let t = 1; t <= target; t++) {     // 外层枚举"容量"
    for (const num of nums) {             // 内层枚举"最后一个数"
      if (t >= num) {
        dp[t] += dp[t - num];             // 末位是 num，前序方案有 dp[t-num] 种
      }
    }
  }

  return dp[target];
}
```

**复杂度**：时间 O(target·n)；空间 O(target)。

**易错点**：
- 内外层循环写反，算成组合数，`nums=[1,2,3], target=4` 输出 4 而非 7。
- `dp[0]` 初始化为 0，整张表全 0。
- 认为"和 C-204 一样回溯就行"：`nums=[1,2], target=35` 时递归次数爆炸，直接超时。
- 用 `dp[t] += dp[t-num]` 但漏了 `t >= num` 判断，负下标取到 `undefined`，结果为 NaN。

**变体与追问**：
- 顺序不同算同一方案 → LeetCode 518 零钱兑换 II，只需交换两层循环。
- 求最少硬币数 → LeetCode 322，转移改成 `min(dp[t-num]) + 1`。
- 若元素可重复使用且要求输出所有方案 → 回到 C-204 的回溯。

---

### C-217 递增子序列 · 中等 · 字节/腾讯

**题干**：给定整数数组 `nums`，找出所有**不同的递增子序列**，长度至少为 2。`1 <= nums.length <= 15`，`-100 <= nums[i] <= 100`。

**示例**：`输入: nums = [4,6,7,7]` → `输出: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]`

**思路**：
- 与子集 II 长得像，但**绝不能排序**：子序列要求保持原数组下标顺序，排序会破坏"子序列"定义，产出非法答案。
- 不能排序就无法用 `nums[i] === nums[i-1]` 去重，改用**每层一个 `Set`**：记录本层已经作为"下一个元素"尝试过的值，同层重复值直接跳过。
- 为什么每层新建 Set 而不是全局一个：去重的语义是"同一层不重复枚举相同的值"，不同层的相同值（如 `[7,7]`）是合法解，必须允许。若用全局 Set，`[7,7]` 会被误杀。
- 递增约束用 `nums[i] >= path[path.length - 1]` 判断，等号允许，因为题目要求非递减。

**代码**：
```javascript
function findSubsequences(nums) {
  const res = [];
  const path = [];

  const dfs = (start) => {
    if (path.length >= 2) res.push([...path]);   // 长度达标即收集

    const used = new Set();                      // 本层去重，关键：每层新建
    for (let i = start; i < nums.length; i++) {
      if (used.has(nums[i])) continue;           // 本层已枚举过该值
      if (path.length > 0 && nums[i] < path[path.length - 1]) continue; // 非递增

      used.add(nums[i]);                         // 登记本层选择
      path.push(nums[i]);                        // 做选择
      dfs(i + 1);                                // 递归
      path.pop();                                // 撤销
    }
  };

  dfs(0);
  return res;
}
```

**复杂度**：时间 O(n·2^n)，最多 2^n 个子序列；空间 O(n) 递归栈，每层额外 O(n) 的 Set。

**易错点**：
- 习惯性 `nums.sort()`，直接破坏子序列语义，答案全错。
- 把 `used` 提到函数外做全局去重，`[7,7]` 这类跨层重复被误删。
- 递增判断写成 `>`，漏掉相等元素组成的合法解。
- 忘记 `used.add` 放在 `path.push` 之前/之后不一致，导致同层判断失效。

**变体与追问**：
- 只要最长递增子序列长度（LeetCode 300）：贪心 + 二分，O(n log n)，与本题完全不同的解法。
- 最长递增子序列的**个数**（LeetCode 673）：树状数组或 DP 计数。
- 若允许任意子序列（不要求递增）且去重：那就是去重子集问题，可排序。

---

### C-218 划分为 k 个相等的子集 · 中等 · 字节/快手

**题干**：给定整数数组 `nums` 和整数 `k`，判断能否把数组分成 `k` 个**非空子集**，使每个子集的元素和都相等。`1 <= k <= nums.length <= 16`，`0 <= nums[i] <= 10^4`。

**示例**：`输入: nums = [4,3,2,3,5,2,1], k = 4` → `输出: true`（`5 / 4,1 / 3,2 / 3,2`）

**思路**：
- 先做可行性判断：`sum % k !== 0` 直接 false，任一元大于 `target = sum/k` 也 false。
- 建模成"往 k 个桶里放球"：每个元素必须进某一个桶，桶内和不得超过 `target`，全部放完即成功。
- **降序排序**是核心优化：大元素先放，能更早暴露"放不下"的矛盾，剪掉大量分支。
- 三重剪枝（面试重点）：① 桶放不下就跳过；② `buckets[i] === buckets[i-1]` 时跳过——两个桶当前和相同，放哪个等价；③ 回溯后若该桶回到 0 仍失败，直接 `break`——说明这个元素必须独占一个空桶，其它空桶试了也一样。
- 注意：这里不是"每个元素选或不选"，而是"每个元素选一个桶"，所以复杂度是 O(k^n) 而不是 2^n。

**代码**：
```javascript
function canPartitionKSubsets(nums, k) {
  const total = nums.reduce((a, b) => a + b, 0);
  if (total % k !== 0) return false;
  const target = total / k;

  nums.sort((a, b) => b - a);          // 降序，先放大元素
  if (nums[0] > target) return false;

  const buckets = new Array(k).fill(0);

  const dfs = (idx) => {
    if (idx === nums.length) return true;      // 全部放完
    const v = nums[idx];

    for (let i = 0; i < k; i++) {
      if (buckets[i] + v > target) continue;   // 放不下
      if (i > 0 && buckets[i] === buckets[i - 1]) continue; // 等价桶去重

      buckets[i] += v;                         // 做选择
      if (dfs(idx + 1)) return true;           // 递归
      buckets[i] -= v;                         // 撤销

      if (buckets[i] === 0) break;             // 空桶都失败，换桶无意义
    }
    return false;
  };

  return dfs(0);
}
```

**复杂度**：时间 O(k^n) 上界，带三重剪枝后实际接近 O(n·k)；空间 O(n + k)。

**易错点**：
- 忘写 `total % k` 判断，`target` 出现小数，后续比较永不相等，静默返回 false。
- 不排序：同样能过但最坏用例超时，面试官会问"为什么降序"。
- `if (buckets[i] === 0) break;` 写成 `continue`，最坏情况退化成 O(k^n)。
- 等价桶去重条件写成 `buckets[i] === buckets[i+1]`，方向反了，去重无效。

**变体与追问**：
- 火柴拼正方形（C-219）：k 固定为 4，代码完全同构。
- 若要求输出具体分组：`buckets` 改成存元素下标的数组，回溯时 push/pop。
- 若 `nums[i]` 可达 10^4、n=16：需加状态压缩 DP `dp[mask]` 记录"前若干元素凑出的余数"，复杂度 O(2^n·n)。

---

### C-219 火柴拼正方形 · 中等 · 字节/阿里/拼多多

**题干**：给定整数数组 `matchsticks`，每个元素是一根火柴的长度。要用**全部**火柴拼成一个正方形，不能折断火柴，可以首尾相接，判断是否可行。`1 <= matchsticks.length <= 15`，`1 <= matchsticks[i] <= 10^8`。

**示例**：`输入: matchsticks = [1,1,2,2,2]` → `输出: true`（`1+1, 2, 2, 2`）

**思路**：
- 本质就是 C-218 取 `k = 4`，边长 `side = sum / 4`。差别只在题目包装，考点一致。
- 终止条件不是"桶数用完"而是"火柴用完"：把所有火柴分配到 4 条边，每条边和等于 `side`。
- 三条与 C-218 相同的剪枝：放不下跳过、等和边去重、空边试失败即 break。其中"空边失败即 break"在正方形场景特别好解释：如果一根火柴独占一条空边都不能成功，那换另一条空边结果必然相同。
- 必须先判 `sum % 4`，再用 `matchsticks[0] > side` 挡住超长火柴（降序后首个即最大值）。

**代码**：
```javascript
function makesquare(matchsticks) {
  const total = matchsticks.reduce((a, b) => a + b, 0);
  if (total % 4 !== 0) return false;
  const side = total / 4;

  matchsticks.sort((a, b) => b - a);
  if (matchsticks[0] > side) return false;

  const edges = new Array(4).fill(0);          // 四条边的当前长度

  const dfs = (idx) => {
    if (idx === matchsticks.length) return true;
    const v = matchsticks[idx];

    for (let i = 0; i < 4; i++) {
      if (edges[i] + v > side) continue;       // 这条边放不下
      if (i > 0 && edges[i] === edges[i - 1]) continue; // 等长边等价

      edges[i] += v;                           // 做选择
      if (dfs(idx + 1)) return true;           // 递归
      edges[i] -= v;                           // 撤销

      if (edges[i] === 0) break;               // 新边都失败，无需再试
    }
    return false;
  };

  return dfs(0);
}
```

**复杂度**：时间 O(4^n) 上界，剪枝后远小；空间 O(n)。

**易错点**：
- 只判了 `sum % 4`，没判单根火柴超长，导致后面白跑。
- 把"四条边"写成"四个桶但允许空桶"，题目要求用完所有火柴，空桶即失败，语义要清楚。
- `edges[i] -= v` 漏写，第一条分支失败后边长永久膨胀。
- 用贪心（每次放最长的边）直接返回结果：贪心会错，必须回溯。

**变体与追问**：
- 划分成 k 个等和子集（C-218）：把 4 换成 k 即可。
- 若允许折断火柴：问题退化为"能否凑出四段等长"，是纯数值问题。
- 状态压缩写法：`dp[mask]` 表示已用火柴集合下当前边的填充进度，复杂度 O(2^n)，n=15 时可过。

---

### C-220 目标和 · 中等 · 字节/腾讯/美团

**题干**：给定非负整数数组 `nums` 和整数 `target`，给每个数前添加 `+` 或 `-`，然后串联起来构造表达式，返回使表达式结果等于 `target` 的**不同表达式数目**。`1 <= nums.length <= 20`，`0 <= nums[i] <= 1000`。

**示例**：`输入: nums = [1,1,1,1,1], target = 3` → `输出: 5`

**思路**：
- 最直白的建模是二叉树：第 `i` 层决定第 `i` 个数取 `+` 还是 `-`，两个分支，叶子处判断和是否等于 `target`。纯回溯 O(2^n)，n=20 时约 100 万次，能过但面试官会继续追问优化。
- 用 `Map` 记忆化 `(下标, 当前和) → 方案数`：不同选择路径可能到达同一个 `(i, sum)` 状态，重复计算被消除，复杂度降到 O(n·S)，S 为和的取值范围（约 2 万）。
- 这里 `sum` 作为参数传值，天然"免撤销"——没有可变状态被修改，所以不需要显式的撤销步骤；但"两个分支 = 两次选择"的决策树结构仍然清晰。
- 另有更优雅的数学转化：设正数部分和为 `P`，负数部分绝对值和为 `N`，则 `P + N = sum`、`P - N = target`，解得 `P = (sum + target)/2`，问题变成**0-1 背包计数**。面试中能说出这一层会加分。

**代码**：
```javascript
function findTargetSumWays(nums, target) {
  const memo = new Map();

  // 返回：从下标 i 开始、当前累加和为 sum 时，能凑出 target 的方案数
  const dfs = (i, sum) => {
    if (i === nums.length) return sum === target ? 1 : 0;

    const key = i + ',' + sum;
    if (memo.has(key)) return memo.get(key);     // 命中缓存

    // 两个分支即两次"选择"：加号 / 减号
    const cnt =
      dfs(i + 1, sum + nums[i]) +                // 选 +
      dfs(i + 1, sum - nums[i]);                 // 选 -

    memo.set(key, cnt);
    return cnt;
  };

  return dfs(0, 0);
}

// 0-1 背包写法（更快）：
// const P = (sum + target) / 2; dp[0] = 1;
// for (const v of nums) for (let s = P; s >= v; s--) dp[s] += dp[s - v];
```

**复杂度**：时间 O(n·S)，S ≈ 2·sum(nums) 的状态空间；空间 O(n·S) 缓存。

**易错点**：
- 缓存 key 用 `i + sum` 字符串拼接，`(1, 23)` 与 `(12, 3)` 撞键；必须加分隔符。
- 忘记 `memo.has` 而直接 `memo.get(key)` 判空：方案数为 0 时被误当成"未计算"，退化为指数级。
- 背包写法里内层循环写成正序，`0-1` 退化成完全背包，答案偏大。
- `(sum + target)` 为奇数或为负时，背包写法应直接返回 0（数学上无解）。

**变体与追问**：
- 只问"是否存在"一种方案：LeetCode 416 分割等和子集，布尔 DP。
- 若 `nums` 含负数：背包转化失效，回到记忆化 DFS。
- 若 `target` 很大而 `n` 很小：记忆化 DFS 优于背包。

---
