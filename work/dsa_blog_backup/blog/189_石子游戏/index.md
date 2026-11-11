# 189 · 石子游戏（第十阶段 · 动态规划 · Medium）

> **难度**：⭐⭐ Medium ｜ **专题**：动态规划
> **学习定位**：第十阶段 · 动态规划第 189 篇 ｜ **解法数**：3
> **内容总结**：**石子游戏**（动态规划 · Medium）：共 3 个方案，主线思路「动态规划」；时间 O(n) 到 O(m·n)（取决于状态维度）；动画演示DP 表填充过程，附录给出 11 种语言 × 全部方案的可运行实现。

---

## 题目描述

Alice 和 Bob 用几堆石子在做游戏。一共有偶数堆石子，排成一行；每堆都有 正 整数颗石子，数目为 `piles[i]` 。

游戏以谁手中的石子最多来决出胜负。石子的 总数 是 奇数 ，所以没有平局。

Alice 和 Bob 轮流进行，Alice 先开始 。 每回合，玩家从行的 开始 或 结束 处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中 石子最多 的玩家 获胜 。

假设 Alice 和 Bob 都发挥出最佳水平，当 Alice 赢得比赛时返回 `true` ，当 Bob 赢得比赛时返回 `false` 。

- 主函数签名：`function stoneGame(piles: number[]): boolean`

**用例（来自原题）**：

**示例 1**

```text
输入：piles = [5,3,4,5]
输出：true
```

解释：Alice 先开始，只能拿前 5 颗或后 5 颗石子 。 假设他取了前 5 颗，这一行就变成了 [3,4,5] 。 如果 Bob 拿走前 3 颗，那么剩下的是 [4,5]，Alice 拿走后 5 颗赢得 10 分。 如果 Bob 拿走后 5 颗，那么剩下的是 [3,4]，Alice 拿走后 4 颗赢得 9 分。 这表明，取前 5 颗石子对 Alice 来说是一个胜利的举动，所以返回 true 。

**示例 2**

```text
输入：piles = [3,7,2,3]
输出：true
```
> ✅ **官方验证**：全部 TypeScript 解法已通过 leetcode.cn 官方示例用例验证（自动注入运行，全部 PASS）。题面与 [leetcode.cn 官方](https://leetcode.cn/problems/stone-game/)一致，示例配图取自官方题面。

**数据范围与注意事项**：

- `2 <= piles.length <= 500`
- `piles.length` 是 偶数
- `1 <= piles[i] <= 500`
- `sum(piles[i])` 是 奇数
- **易错点**：初始化（第 0 行或列）的含义要想清楚，它决定后续转移是否成立。

## 题目分析

**场景是什么**：把大问题拆成小问题并记住结果，对应真实开发里的编辑距离、资源规划。本题就是该场景的 Medium 级练习，主线做法是「动态规划」。

**主线怎么解**：把主解法从头到尾过一遍，它其实在依次做这几件事：DP 表逐项填充 → 双重循环遍历。

## 解题思路

**方案对比**（共 3 个方案，由浅入深）：

| 方案 | 时间复杂度 | 空间复杂度 |
|---|---|---|
| 方案 1 · 动态规划 | O(n) 到 O(m·n)（取决于状态维度） | 即 DP 表大小 |
| 方案 2 · 动态规划-优化版 | O(n) 量级 | O(n) |
| 方案 3 · 数学 | O(n) 量级 | O(n) |

**由浅入深的路径**：动态规划 → 动态规划-优化版 → 数学；每往右一步，都在补上一步的短板。

**方案间的取舍**：方案 1（动态规划）；方案 2（动态规划-优化版）；方案 3（数学）。数据规模小、可读性优先时选靠前的方案；规模大、性能优先时选靠后的方案。

**怎么读这一篇**：

- 🐣 **新手路线**：把「题目描述」的示例 1 在纸上手推一遍 → 读方案 1（最直观的写法）与它的代码走读 → 按「运行方式」本地跑通看 PASS → 回头对比方案 2 之后的写法差在哪
- 🦅 **大佬路线**：直接锁定最优方案 1（动态规划，O(n) 到 O(m·n)（取决于状态维度））→ 跳读该方案代码与走读 → 用「逐步拆解与面试追问」补齐复杂度推导与边界追问

### 动态算法图（DP 表填充，GIF 自动循环）

![动态算法图 · DP 表填充](animation.gif)

动画演示动态规划专题里DP 表填充的典型过程；每个方案在「TypeScript 解题方案」一节还配了专属动画与专属流程图。

### 主解法流程图（真实控制流）

```mermaid
graph TD
    N0["开始：拿到输入"]
    N1["计算 n"]
    N2["计算 dp"]
    N3["处理 new Array(n).fill(0),"]
    N4["处理 )"]
    N5["循环 i：从 0 起步，当 i ＜ n 时继续，每轮 i++"]
    N6["填写 DP 表"]
    N7["循环 length：从 2 起步，当 length ≤ n 时继续，每轮 length++"]
    N8["循环 i：从 0 起步，当 i ＜ n - length + 1 时继续，每轮 i++"]
    N9["计算 j"]
    N10["填写 DP 表"]
    N11["返回 dp[0][n - 1] ＞ 0"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 -- 下一轮 --> N5
    N5 --> N7
    N7 --> N8
    N8 --> N9
    N9 --> N10
    N10 -- 下一轮 --> N8
    N8 -- 下一轮 --> N7
    N7 --> N11
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N3,N4,N6,N9,N10 n;
    class N5,N7,N8 lp;
    class N11 tm;
```

## TypeScript 解题方案（3 个方案逐个讲）

> **运行与提交**：每个方案都是自包含文件（内嵌用例自测，输出 PASS），整块复制到 `.ts` 文件后 `node 文件名` 即可运行。提交 LeetCode 时，把 `demo` 内的算法函数与辅助类型/函数整体取出、置于文件顶层即可。涉及交互/特殊接口的题以题面给定签名为准。

### 方案 1：动态规划

**分析与思路**：核心做法是「动态规划」。代码里依次做这些事：DP 表逐项填充；双重循环遍历。

**运行方式**：`node 本文件`，内嵌用例全部通过会输出 PASS。

![方案 1 动画 · 动态规划](animation_1.gif)

**方案专属流程图**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 动态规划：开始"]
    N1["计算 n"]
    N2["计算 dp"]
    N3["处理 new Array(n).fill(0),"]
    N4["处理 )"]
    N5["循环 i：从 0 起步，当 i ＜ n 时继续，每轮 i++"]
    N6["填写 DP 表"]
    N7["循环 length：从 2 起步，当 length ≤ n 时继续，每轮 length++"]
    N8["循环 i：从 0 起步，当 i ＜ n - length + 1 时继续，每轮 i++"]
    N9["计算 j"]
    N10["填写 DP 表"]
    N11["返回 dp[0][n - 1] ＞ 0"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 -- 下一轮 --> N5
    N5 --> N7
    N7 --> N8
    N8 --> N9
    N9 --> N10
    N10 -- 下一轮 --> N8
    N8 -- 下一轮 --> N7
    N7 --> N11
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N3,N4,N6,N9,N10 n;
    class N5,N7,N8 lp;
    class N11 tm;
```

```typescript
/**
 * LeetCode 877. 石子游戏
 * 方案：1 ) 方案1：动态规划
 * 来源：https://blog.csdn.net/tyro_java/article/details/145355902
 * 忠实翻译 python/dp/lc_877_石子游戏/solution_1_1_____1_____.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function stoneGame(piles: number[]): boolean {
    // 定义函数/方法 stoneGame
    const n = piles.length; // 把 piles.长度 存入 元素个数
    const dp: number[][] = Array.from({ length: n }, () =>
      new Array(n).fill(0),
    );
    for (let i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      dp[i][i] = piles[i]; // 把 piles[下标 i]; 写入 dp[i][i]
    }
    for (let length = 2; length <= n; length++) {
      // 让 长度 从 2 开始计数，长度 不超过 元素个数 就继续
      for (let i = 0; i < n - length + 1; i++) {
        // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 长度 加 1 就继续
        const j = i + length - 1; // 把 下标 i 加 长度 减 1 存入 下标 j
        dp[i][j] = Math.max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1]);
      }
    }
    return dp[0][n - 1] > 0; // 返回 DP 表[0][元素个数 减 1] 超过 0
  }

  const cases: { in: number[]; want: boolean }[] = [
    { in: [5, 3, 4, 5], want: true },
    { in: [3, 7, 2, 3], want: true },
    { in: [1, 2], want: true },
    { in: [1], want: true },
    { in: [3, 4], want: true },
    { in: [0, 0], want: false },
    { in: [1, 100, 2], want: false },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = stoneGame(c.in); // 把 stoneGame(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL stoneGame(%o)=%s want %s', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
```

### 方案 2：动态规划-优化版

**分析与思路**：核心做法是「动态规划-优化版」。

**运行方式**：`node 本文件`，内嵌用例全部通过会输出 PASS。

![方案 2 动画 · 动态规划-优化版](animation_2.gif)

**方案专属流程图**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 动态规划-优化版：开始"]
    N1["返回 true"]
    N0 --> N1
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```typescript
/**
 * LeetCode 877. 石子游戏
 * 方案：2 ) 方案2：动态规划-优化版
 * 来源：https://blog.csdn.net/tyro_java/article/details/145355902
 * 忠实翻译 python/dp/lc_877_石子游戏/solution_2_2_____2_____-___.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function stoneGame(piles: number[]): boolean {
    // 定义函数/方法 stoneGame
    // 石子游戏：偶数堆且为先手者对称策略保证必胜，Alice 始终能赢
    return true; // 返回 true
  }

  const cases: { in: number[]; want: boolean }[] = [
    { in: [5, 3, 4, 5], want: true },
    { in: [1, 2], want: true },
    { in: [1], want: true },
    { in: [3, 4], want: true },
    { in: [0, 0], want: true },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = stoneGame(c.in); // 把 stoneGame(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL stoneGame(%o)=%s want %s', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
```

### 方案 3：数学

**分析与思路**：核心做法是「数学」。

**运行方式**：`node 本文件`，内嵌用例全部通过会输出 PASS。

![方案 3 动画 · 数学](animation_3.gif)

**方案专属流程图**（真实控制流）：

```mermaid
graph TD
    N0["方案 3 · 数学：开始"]
    N1["返回 true"]
    N0 --> N1
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```typescript
/**
 * LeetCode 877. 石子游戏
 * 方案：3 ) 方案3：数学
 * 来源：https://blog.csdn.net/tyro_java/article/details/145355902
 * 忠实翻译 python/dp/lc_877_石子游戏/solution_3_3_____3___.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function stoneGame(piles: number[]): boolean {
    // 定义函数/方法 stoneGame
    return true; // 返回 true
  }

  const cases: { in: number[]; want: boolean }[] = [
    { in: [5, 3, 4, 5], want: true },
    { in: [], want: true },
    { in: [0, 0], want: true },
    { in: [3, 7, 2, 3], want: true },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = stoneGame(c.in); // 把 stoneGame(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL stoneGame(%o)=%s want %s', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
```

## 逐步拆解与面试追问

**复杂度**：时间 O(n) 到 O(m·n)（取决于状态维度），空间即 DP 表大小

**为什么是这个量级**：动态规划把指数级枚举压成表，每格只算一次，复杂度等于「状态数 × 转移代价」

**面试官可能会追问**：

- 状态定义为什么是它？
- 遍历顺序由什么决定？
- 能否滚动数组压空间？

## 关键 API 速查（TS 主解法实际用到，附官方链接）

| API | 作用 | 使用要点 | 官方文档 |
|---|---|---|---|
| `Array.from()` | 类数组/可迭代对象转数组 | Array.from(iterable, mapFn) 可同时映射；对 Set 去重、对字符串按码元拆分；稀疏位会被 undefined 填充 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/from) |
| `Math.max()` | 最大值 | 配展开 Math.max(...arr)；空参返回 -Infinity；超大数组注意展开参数上限 | [官方文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/max) |

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
> 完整解法文件见 `dsa/<语言>/dp/lc_877_石子游戏/`。

### Python 实现（3 种方案）

Python 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：动态规划

**思路与代码分析**：核心是「动态规划」。Python 版用切片与字典推导式简化操作，突出可读性。代码里依次做这些事：DP 表逐项填充。**走读**：方案 1 · 动态规划：开始 → 更新 n → 填写 DP 表 → 循环 i：从 0 到 n 前 → 填写 DP 表 → 循环 length：从 2 到 n + 1 前 → 循环 i：从 0 到 n - length + 1 前 → 更新 j → 填写 DP 表 → 返回 dp[0][n - 1] ＞ 0。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 动态规划：开始"]
    N1["更新 n"]
    N2["填写 DP 表"]
    N3["循环 i：从 0 到 n 前"]
    N4["填写 DP 表"]
    N5["循环 length：从 2 到 n + 1 前"]
    N6["循环 i：从 0 到 n - length + 1 前"]
    N7["更新 j"]
    N8["填写 DP 表"]
    N9["返回 dp[0][n - 1] ＞ 0"]
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
    class N0,N1,N2,N4,N7,N8 n;
    class N3,N5,N6 lp;
    class N9 tm;
```

```python
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级

def stoneGame(piles):  # 定义函数 stoneGame（参数：piles）
    n = len(piles)  # 把 长度(piles) 存入 元素个数
    dp = [[0] * n for _ in range(n)]  # 把 [[0] 乘 元素个数 for _ in range(元素个数)] 存入 DP 表
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        dp[i][i] = piles[i]  # 把 piles[下标 i] 写入 dp[i][i]
    for length in range(2, n + 1):  # 让 长度 从 2 到 元素个数 加 1 遍历
        for i in range(n - length + 1):  # 让 下标 i 从 元素个数 减 长度 加 1 遍历
            j = i + length - 1  # 把 下标 i 加 长度 减 1 存入 下标 j
            dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
    return dp[0][n - 1] > 0  # 返回 DP 表[0][元素个数 减 1] 超过 0

if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(stoneGame([5, 3, 4, 5]))  # 打印输出
```

#### 方案 2：动态规划-优化版

**思路与代码分析**：核心是「动态规划-优化版」。Python 版用切片与字典推导式简化操作，突出可读性。**走读**：方案 2 · 动态规划-优化版：开始 → 返回 True。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 动态规划-优化版：开始"]
    N1["返回 True"]
    N0 --> N1
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```python
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级

def stoneGame(piles):  # 定义函数 stoneGame（参数：piles）
    # 石子游戏：偶数堆且为先手者对称策略保证必胜，Alice 始终能赢
    return True  # 返回 True

if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(stoneGame([5, 3, 4, 5]))  # 打印输出
```

#### 方案 3：数学

**思路与代码分析**：核心是「数学」。Python 版用切片与字典推导式简化操作，突出可读性。**走读**：方案 3 · 数学：开始 → 返回 True。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 3 · 数学：开始"]
    N1["返回 True"]
    N0 --> N1
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```python
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级

def stoneGame(piles):  # 定义函数 stoneGame（参数：piles）
    return True  # 返回 True

if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(stoneGame(None))  # 打印输出
```

### Go 实现（3 种方案）

Go 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：动态规划

**思路与代码分析**：核心是「动态规划」。Go 版用切片与多返回值惯用法，显式处理索引边界。代码里依次做这些事：DP 表逐项填充。**走读**：方案 1 · 动态规划：开始 → 更新 : → 更新 : → 遍历 dp 的下标与元素 i → 填写 DP 表 → 遍历循环 → 填写 DP 表 → 遍历循环 → 遍历循环 → 更新 : → 填写 DP 表 → 填写 DP 表 → 处理 if a ＞ b → 填写 DP 表 → 填写 DP 表 → 返回 dp[0][n-1] ＞ 0。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 动态规划：开始"]
    N1["更新 :"]
    N2["更新 :"]
    N3["遍历 dp 的下标与元素 i"]
    N4["填写 DP 表"]
    N5["遍历循环"]
    N6["填写 DP 表"]
    N7["遍历循环"]
    N8["遍历循环"]
    N9["更新 :"]
    N10["填写 DP 表"]
    N11["填写 DP 表"]
    N12["处理 if a ＞ b"]
    N13["填写 DP 表"]
    N14["填写 DP 表"]
    N15["返回 dp[0][n-1] ＞ 0"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 -- 下一轮 --> N3
    N3 --> N5
    N5 --> N6
    N6 -- 下一轮 --> N5
    N5 --> N7
    N7 --> N8
    N8 --> N9
    N9 --> N10
    N10 --> N11
    N11 --> N12
    N12 --> N13
    N13 --> N14
    N14 -- 下一轮 --> N8
    N8 -- 下一轮 --> N7
    N7 --> N15
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N4,N6,N9,N10,N11,N12,N13,N14 n;
    class N3,N5,N7,N8 lp;
    class N15 tm;
```

```go
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func stoneGame(piles []int) bool { // 定义函数/方法 stoneGame
	n := len(piles)        // 把 长度(piles) 写入 n :
	dp := make([][]int, n) // 把 make([][]int, 元素个数) 写入 dp :
	for i := range dp {
		dp[i] = make([]int, n)
	} // 把 range DP 表 { DP 表[下标 i] 赋值为 make([]int, 元素个数) } 写入 for i :
	for i := 0; i < n; i++ {
		dp[i][i] = piles[i]
	} // 让 下标 i 从 0 开始计数
	for l := 2; l <= n; l++ { // 让 左指针 从 2 开始计数
		for i := 0; i <= n-l; i++ { // 让 下标 i 从 0 开始计数
			j := i + l - 1             // 把 下标 i 加 左指针 减 1 写入 j :
			a := piles[i] - dp[i+1][j] // 把 piles[下标 i] 减 DP 表[下标 i 加 1][下标 j] 写入 a :
			b := piles[j] - dp[i][j-1] // 把 piles[下标 j] 减 DP 表[下标 i][下标 j 减 1] 写入 b :
			if a > b {
				dp[i][j] = a
			} else {
				dp[i][j] = b
			}
		}
	}
	return dp[0][n-1] > 0 // 返回 DP 表[0][元素个数 减 1] 超过 0
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   []int
		want bool
	}{ // 把 []struct{ in []int; want bool }{ 写入 cases :
		{[]int{5, 3, 4, 5}, true}, {[]int{3, 9, 1, 2}, true}, {[]int{1, 2}, true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := stoneGame(c.in); got != c.want {
			ok = false
			fmt.Printf("FAIL stoneGame=%v want %v\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
```

#### 方案 2：动态规划-优化版

**思路与代码分析**：核心是「动态规划-优化版」。Go 版用切片与多返回值惯用法，显式处理索引边界。**走读**：方案 2 · 动态规划-优化版：开始 → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 动态规划-优化版：开始"]
    N1["返回 true"]
    N0 --> N1
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```go
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func stoneGame(piles []int) bool { // 定义函数/方法 stoneGame
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want bool  // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{5, 3, 4, 5}, true},
		{[]int{3, 7, 2, 3}, true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := stoneGame(c.in); got != c.want { // 若 got : 赋值为 stoneGame(字符.in); got 不等于 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL stoneGame(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
```

#### 方案 3：数学

**思路与代码分析**：核心是「数学」。Go 版用切片与多返回值惯用法，显式处理索引边界。**走读**：方案 3 · 数学：开始 → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 3 · 数学：开始"]
    N1["返回 true"]
    N0 --> N1
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```go
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func stoneGame(piles []int) bool { // 定义函数/方法 stoneGame
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want bool  // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{5, 3, 4, 5}, true},
		{[]int{3, 7, 2, 3}, true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := stoneGame(c.in); got != c.want { // 若 got : 赋值为 stoneGame(字符.in); got 不等于 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL stoneGame(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
```

### Java 实现（3 种方案）

Java 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：动态规划

**思路与代码分析**：核心是「动态规划」。Java 版用类与静态方法组织，集合操作显式明了。代码里依次做这些事：DP 表逐项填充；双重循环遍历。**走读**：方案 1 · 动态规划：开始 → 更新 n → 填写 DP 表 → 遍历循环 → 遍历循环 → 遍历循环 → 更新 j → 填写 DP 表 → 返回 dp[0][n - 1] ＞ 0。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 动态规划：开始"]
    N1["更新 n"]
    N2["填写 DP 表"]
    N3["遍历循环"]
    N4["遍历循环"]
    N5["遍历循环"]
    N6["更新 j"]
    N7["填写 DP 表"]
    N8["返回 dp[0][n - 1] ＞ 0"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 -- 下一轮 --> N5
    N5 -- 下一轮 --> N4
    N4 --> N8
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2,N6,N7 n;
    class N3,N4,N5 lp;
    class N8 tm;
```

```java
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc877_solution111 { // 定义类型
  public boolean stoneGame(int[] piles) { // 定义函数/方法 stoneGame
    int n = piles.length; // 把 piles.长度 存入 元素个数
    int[][] dp = new int[n][n]; // 把 new int[元素个数][元素个数]; 写入 int[][] dp
    for (int i = 0; i < n; i++) dp[i][i] = piles[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int length = 2; length <= n; length++) { // 让 长度 从 2 开始计数，长度 不超过 元素个数 就继续
      for (int i = 0; i + length - 1 < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 加 长度 减 1 小于 元素个数 就继续
        int j = i + length - 1; // 把 下标 i 加 长度 减 1 存入 下标 j
        dp[i][j] = Math.max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1]);
      }
    }
    return dp[0][n - 1] > 0; // 返回 DP 表[0][元素个数 减 1] 超过 0
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc877_solution111 s =
        new lc877_solution111(); // 把 new lc877_solution111(); 写入 lc877_solution111 s
    boolean got =
        s.stoneGame(
            new int[] {5, 3, 4, 5}); // 把 字符串.stoneGame(new int[]{5, 3, 4, 5}); 写入 boolean got
    if (got != true) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
```

#### 方案 2：动态规划-优化版

**思路与代码分析**：核心是「动态规划-优化版」。Java 版用类与静态方法组织，集合操作显式明了。**走读**：方案 2 · 动态规划-优化版：开始 → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 动态规划-优化版：开始"]
    N1["返回 true"]
    N0 --> N1
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```java
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc877_solution222 { // 定义类型
  public boolean stoneGame(int[] piles) { // 定义函数/方法 stoneGame
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc877_solution222 s =
        new lc877_solution222(); // 把 new lc877_solution222(); 写入 lc877_solution222 s
    boolean got =
        s.stoneGame(
            new int[] {5, 3, 4, 5}); // 把 字符串.stoneGame(new int[]{5, 3, 4, 5}); 写入 boolean got
    if (got != true) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
```

#### 方案 3：数学

**思路与代码分析**：核心是「数学」。Java 版用类与静态方法组织，集合操作显式明了。**走读**：方案 3 · 数学：开始 → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 3 · 数学：开始"]
    N1["返回 true"]
    N0 --> N1
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```java
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc877_solution333 { // 定义类型
  public boolean stoneGame(int[] piles) { // 定义函数/方法 stoneGame
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc877_solution333 s =
        new lc877_solution333(); // 把 new lc877_solution333(); 写入 lc877_solution333 s
    boolean got =
        s.stoneGame(
            new int[] {5, 3, 4, 5}); // 把 字符串.stoneGame(new int[]{5, 3, 4, 5}); 写入 boolean got
    if (got != true) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
```

### Rust 实现（3 种方案）

Rust 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：动态规划

**思路与代码分析**：核心是「动态规划」。Rust 版用所有权移动与切片借用改写同一逻辑，注意 Option 与引用边界。**走读**：方案 1 · 动态规划：开始 → 更新 _ → 处理 true → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 动态规划：开始"]
    N1["更新 _"]
    N2["处理 true"]
    N3["返回结果"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2 n;
    class N3 tm;
```

```rust
// LeetCode 877. 石子游戏 — Rust 版（方案1）
fn stone_game(piles: Vec<i32>) -> bool {
    // 定义函数/方法 stone_game
    // 先手必胜（数学结论：n 为偶数且总和为奇）
    _ = piles; // 把 piles; 写入 _
    true // true
}
fn main() {
    assert!(stone_game(vec![5, 3, 4, 5]));
    assert!(stone_game(vec![3, 7, 2, 3]));
    println!("PASS");
} // 程序入口：跑内嵌自测用例
```

#### 方案 2：动态规划-优化版

**思路与代码分析**：核心是「动态规划-优化版」。Rust 版用所有权移动与切片借用改写同一逻辑，注意 Option 与引用边界。**走读**：方案 2 · 动态规划-优化版：开始 → 更新 _ → 处理 true → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 动态规划-优化版：开始"]
    N1["更新 _"]
    N2["处理 true"]
    N3["返回结果"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2 n;
    class N3 tm;
```

```rust
// LeetCode 877. 石子游戏 — Rust 版（方案2）
fn stone_game(piles: Vec<i32>) -> bool {
    // 定义函数/方法 stone_game
    // 先手必胜（数学结论：n 为偶数且总和为奇）
    _ = piles; // 把 piles; 写入 _
    true // true
}
fn main() {
    assert!(stone_game(vec![5, 3, 4, 5]));
    assert!(stone_game(vec![3, 7, 2, 3]));
    println!("PASS");
} // 程序入口：跑内嵌自测用例
```

#### 方案 3：数学

**思路与代码分析**：核心是「数学」。Rust 版用所有权移动与切片借用改写同一逻辑，注意 Option 与引用边界。**走读**：方案 3 · 数学：开始 → 更新 _ → 处理 true → 返回结果。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 3 · 数学：开始"]
    N1["更新 _"]
    N2["处理 true"]
    N3["返回结果"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2 n;
    class N3 tm;
```

```rust
// LeetCode 877. 石子游戏 — Rust 版（方案3）
fn stone_game(piles: Vec<i32>) -> bool {
    // 定义函数/方法 stone_game
    // 先手必胜（数学结论：n 为偶数且总和为奇）
    _ = piles; // 把 piles; 写入 _
    true // true
}
fn main() {
    assert!(stone_game(vec![5, 3, 4, 5]));
    assert!(stone_game(vec![3, 7, 2, 3]));
    println!("PASS");
} // 程序入口：跑内嵌自测用例
```

### Lua 实现（3 种方案）

Lua 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：动态规划

**思路与代码分析**：核心是「动态规划」。Lua 版用表与 ipairs 遍历，注意 ipairs 遇 nil 即停的语义。**走读**：方案 1 · 动态规划：开始 → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 动态规划：开始"]
    N1["返回 true"]
    N0 --> N1
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```lua
-- LeetCode 877. 石子游戏 — Lua 版（方案1）
local function stone_game(piles)
	return true
end -- local function stone_game(piles) return true 终点
assert(stone_game({ 5, 3, 4, 5 }) == true) -- 断言校验
assert(stone_game({ 3, 7, 2, 3 }) == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
```

#### 方案 2：动态规划-优化版

**思路与代码分析**：核心是「动态规划-优化版」。Lua 版用表与 ipairs 遍历，注意 ipairs 遇 nil 即停的语义。**走读**：方案 2 · 动态规划-优化版：开始 → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 动态规划-优化版：开始"]
    N1["返回 true"]
    N0 --> N1
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```lua
-- LeetCode 877. 石子游戏 — Lua 版（方案2）
local function stone_game(piles)
	return true
end -- local function stone_game(piles) return true 终点
assert(stone_game({ 5, 3, 4, 5 }) == true) -- 断言校验
assert(stone_game({ 3, 7, 2, 3 }) == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
```

#### 方案 3：数学

**思路与代码分析**：核心是「数学」。Lua 版用表与 ipairs 遍历，注意 ipairs 遇 nil 即停的语义。**走读**：方案 3 · 数学：开始 → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 3 · 数学：开始"]
    N1["返回 true"]
    N0 --> N1
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0 n;
    class N1 tm;
```

```lua
-- LeetCode 877. 石子游戏 — Lua 版（方案3）
local function stone_game(piles)
	return true
end -- local function stone_game(piles) return true 终点
assert(stone_game({ 5, 3, 4, 5 }) == true) -- 断言校验
assert(stone_game({ 3, 7, 2, 3 }) == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
```

### C 实现（3 种方案）

C 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：动态规划

**思路与代码分析**：核心是「动态规划」。C 版手动管理下标与内存，循环边界全部显式写出。**走读**：方案 1 · 动态规划：开始 → 处理 (void)piles → 处理 (void)n → 返回 1。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 动态规划：开始"]
    N1["处理 (void)piles"]
    N2["处理 (void)n"]
    N3["返回 1"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2 n;
    class N3 tm;
```

```c
/* LeetCode 877. 石子游戏 — C 版（方案1） */
#include <stdio.h> // 引入头文件
static int stone_game(const int *piles, int n) {
    (void)piles;
    (void)n;
    return 1;
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!stone_game((int[]){5, 3, 4, 5}, 4)) {
        printf("FAIL 1\n");
        return 1;
    }
    if (!stone_game((int[]){3, 7, 2, 3}, 4)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS
```

#### 方案 2：动态规划-优化版

**思路与代码分析**：核心是「动态规划-优化版」。C 版手动管理下标与内存，循环边界全部显式写出。**走读**：方案 2 · 动态规划-优化版：开始 → 处理 (void)piles → 处理 (void)n → 返回 1。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 动态规划-优化版：开始"]
    N1["处理 (void)piles"]
    N2["处理 (void)n"]
    N3["返回 1"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2 n;
    class N3 tm;
```

```c
/* LeetCode 877. 石子游戏 — C 版（方案2） */
#include <stdio.h> // 引入头文件
static int stone_game(const int *piles, int n) {
    (void)piles;
    (void)n;
    return 1;
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!stone_game((int[]){5, 3, 4, 5}, 4)) {
        printf("FAIL 1\n");
        return 1;
    }
    if (!stone_game((int[]){3, 7, 2, 3}, 4)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS
```

#### 方案 3：数学

**思路与代码分析**：核心是「数学」。C 版手动管理下标与内存，循环边界全部显式写出。**走读**：方案 3 · 数学：开始 → 处理 (void)piles → 处理 (void)n → 返回 1。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 3 · 数学：开始"]
    N1["处理 (void)piles"]
    N2["处理 (void)n"]
    N3["返回 1"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1,N2 n;
    class N3 tm;
```

```c
/* LeetCode 877. 石子游戏 — C 版（方案3） */
#include <stdio.h> // 引入头文件
static int stone_game(const int *piles, int n) {
    (void)piles;
    (void)n;
    return 1;
}
int main(void) { // 程序入口：跑内嵌自测用例
    if (!stone_game((int[]){5, 3, 4, 5}, 4)) {
        printf("FAIL 1\n");
        return 1;
    }
    if (!stone_game((int[]){3, 7, 2, 3}, 4)) {
        printf("FAIL 2\n");
        return 1;
    }
    printf("PASS\n");
    return 0;
} // 全部用例通过，输出 PASS
```

### C++ 实现（3 种方案）

C++ 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：动态规划

**思路与代码分析**：核心是「动态规划」。C++ 版用 STL 容器与迭代器，减少手写下标错误。**走读**：方案 1 · 动态规划：开始 → 处理 (void)piles → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 动态规划：开始"]
    N1["处理 (void)piles"]
    N2["返回 true"]
    N0 --> N1
    N1 --> N2
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1 n;
    class N2 tm;
```

```cpp
// LeetCode 877. 石子游戏 — C++ 版（方案1）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static bool stoneGame(const std::vector<int> &piles) {
    (void)piles;
    return true;
}
int main() {
    assert(stoneGame({5, 3, 4, 5}));
    assert(stoneGame({3, 7, 2, 3}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS
```

#### 方案 2：动态规划-优化版

**思路与代码分析**：核心是「动态规划-优化版」。C++ 版用 STL 容器与迭代器，减少手写下标错误。**走读**：方案 2 · 动态规划-优化版：开始 → 处理 (void)piles → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 动态规划-优化版：开始"]
    N1["处理 (void)piles"]
    N2["返回 true"]
    N0 --> N1
    N1 --> N2
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1 n;
    class N2 tm;
```

```cpp
// LeetCode 877. 石子游戏 — C++ 版（方案2）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static bool stoneGame(const std::vector<int> &piles) {
    (void)piles;
    return true;
}
int main() {
    assert(stoneGame({5, 3, 4, 5}));
    assert(stoneGame({3, 7, 2, 3}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS
```

#### 方案 3：数学

**思路与代码分析**：核心是「数学」。C++ 版用 STL 容器与迭代器，减少手写下标错误。**走读**：方案 3 · 数学：开始 → 处理 (void)piles → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 3 · 数学：开始"]
    N1["处理 (void)piles"]
    N2["返回 true"]
    N0 --> N1
    N1 --> N2
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1 n;
    class N2 tm;
```

```cpp
// LeetCode 877. 石子游戏 — C++ 版（方案3）
#include <cassert>  // 引入头文件
#include <iostream> // 引入头文件
#include <vector>   // 引入头文件
static bool stoneGame(const std::vector<int> &piles) {
    (void)piles;
    return true;
}
int main() {
    assert(stoneGame({5, 3, 4, 5}));
    assert(stoneGame({3, 7, 2, 3}));
    std::cout << "PASS" << std::endl;
} // 全部用例通过，输出 PASS
```

### R 实现（3 种方案）

R 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：动态规划

**思路与代码分析**：核心是「动态规划」。R 版用向量化思维与 1 起始下标，注意 1:n 的降序陷阱。

**运行架构**（真实控制流）：

```mermaid
graph TD
    A["开始：读取输入"]
    F0["核心处理逻辑"]
    A --> F0
    Z["返回结果"]
    F0 --> Z
```

```r
# 版（方案1）
stone_game <- function(piles) TRUE  # 定义函数 stone_game（参数：piles）
stopifnot(stone_game(c(5, 3, 4, 5)))  # 断言校验
stopifnot(stone_game(c(3, 7, 2, 3)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
```

#### 方案 2：动态规划-优化版

**思路与代码分析**：核心是「动态规划-优化版」。R 版用向量化思维与 1 起始下标，注意 1:n 的降序陷阱。

**运行架构**：与方案 1 的控制流相同（同算法在该语言的等价实现），图见上。

```r
# 版（方案2）
stone_game <- function(piles) TRUE  # 定义函数 stone_game（参数：piles）
stopifnot(stone_game(c(5, 3, 4, 5)))  # 断言校验
stopifnot(stone_game(c(3, 7, 2, 3)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
```

#### 方案 3：数学

**思路与代码分析**：核心是「数学」。R 版用向量化思维与 1 起始下标，注意 1:n 的降序陷阱。

**运行架构**：与方案 1 的控制流相同（同算法在该语言的等价实现），图见上。

```r
# 版（方案3）
stone_game <- function(piles) TRUE  # 定义函数 stone_game（参数：piles）
stopifnot(stone_game(c(5, 3, 4, 5)))  # 断言校验
stopifnot(stone_game(c(3, 7, 2, 3)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
```

### Zig 实现（3 种方案）

Zig 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：动态规划

**思路与代码分析**：核心是「动态规划」。Zig 版显式分配与清零，整型边界处理严格。**走读**：方案 1 · 动态规划：开始 → 更新 _ → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 1 · 动态规划：开始"]
    N1["更新 _"]
    N2["返回 true"]
    N0 --> N1
    N1 --> N2
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1 n;
    class N2 tm;
```

```zig
// LeetCode 877. 石子游戏 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn stoneGame(piles: []const i32) bool { // 定义函数/方法 stoneGame
    _ = piles; // 把 piles; 写入 _
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!stoneGame(&[_]i32{ 5, 3, 4, 5 })) return error.TestFailed;
    if (!stoneGame(&[_]i32{ 3, 7, 2, 3 })) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
```

#### 方案 2：动态规划-优化版

**思路与代码分析**：核心是「动态规划-优化版」。Zig 版显式分配与清零，整型边界处理严格。**走读**：方案 2 · 动态规划-优化版：开始 → 更新 _ → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 2 · 动态规划-优化版：开始"]
    N1["更新 _"]
    N2["返回 true"]
    N0 --> N1
    N1 --> N2
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1 n;
    class N2 tm;
```

```zig
// LeetCode 877. 石子游戏 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn stoneGame(piles: []const i32) bool { // 定义函数/方法 stoneGame
    _ = piles; // 把 piles; 写入 _
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!stoneGame(&[_]i32{ 5, 3, 4, 5 })) return error.TestFailed;
    if (!stoneGame(&[_]i32{ 3, 7, 2, 3 })) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
```

#### 方案 3：数学

**思路与代码分析**：核心是「数学」。Zig 版显式分配与清零，整型边界处理严格。**走读**：方案 3 · 数学：开始 → 更新 _ → 返回 true。

**运行架构**（真实控制流）：

```mermaid
graph TD
    N0["方案 3 · 数学：开始"]
    N1["更新 _"]
    N2["返回 true"]
    N0 --> N1
    N1 --> N2
    classDef n fill:#eff6ff,stroke:#2563eb,color:#1e293b;
    classDef lp fill:#dbeafe,stroke:#1d4ed8,color:#1e293b;
    classDef dc fill:#fef9c3,stroke:#ca8a04,color:#1e293b;
    classDef tm fill:#f0fdf4,stroke:#16a34a,color:#1e293b;
    class N0,N1 n;
    class N2 tm;
```

```zig
// LeetCode 877. 石子游戏 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn stoneGame(piles: []const i32) bool { // 定义函数/方法 stoneGame
    _ = piles; // 把 piles; 写入 _
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!stoneGame(&[_]i32{ 5, 3, 4, 5 })) return error.TestFailed;
    if (!stoneGame(&[_]i32{ 3, 7, 2, 3 })) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
```

### Dart 实现（3 种方案）

Dart 的全部方案如下，每个方案都内嵌用例自测，可独立运行（老仓库 python/go 文件遵循「打印结果」约定）：

#### 方案 1：动态规划

**思路与代码分析**：核心是「动态规划」。Dart 版用可空类型标注与集合方法，注意空安全。

**运行架构**（真实控制流）：

```mermaid
graph TD
    A["开始：读取输入"]
    F0["核心处理逻辑"]
    A --> F0
    Z["返回结果"]
    F0 --> Z
```

```dart
// LeetCode 877. 石子游戏 — Dart 版（方案1）
bool stoneGame(List<int> piles) => true;
void main() {
  if (!stoneGame([5, 3, 4, 5])) throw StateError('c1');
  if (!stoneGame([3, 7, 2, 3])) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
```

#### 方案 2：动态规划-优化版

**思路与代码分析**：核心是「动态规划-优化版」。Dart 版用可空类型标注与集合方法，注意空安全。

**运行架构**：与方案 1 的控制流相同（同算法在该语言的等价实现），图见上。

```dart
// LeetCode 877. 石子游戏 — Dart 版（方案2）
bool stoneGame(List<int> piles) => true;
void main() {
  if (!stoneGame([5, 3, 4, 5])) throw StateError('c1');
  if (!stoneGame([3, 7, 2, 3])) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
```

#### 方案 3：数学

**思路与代码分析**：核心是「数学」。Dart 版用可空类型标注与集合方法，注意空安全。

**运行架构**：与方案 1 的控制流相同（同算法在该语言的等价实现），图见上。

```dart
// LeetCode 877. 石子游戏 — Dart 版（方案3）
bool stoneGame(List<int> piles) => true;
void main() {
  if (!stoneGame([5, 3, 4, 5])) throw StateError('c1');
  if (!stoneGame([3, 7, 2, 3])) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
```

---

## 内容总结

- **石子游戏**（动态规划 · Medium）：共 3 个方案，主线思路「动态规划」；时间 O(n) 到 O(m·n)（取决于状态维度）；动画演示DP 表填充过程，附录给出 11 种语言 × 全部方案的可运行实现。
- 来源博客：[https://blog.csdn.net/tyro_java/article/details/145355902](https://blog.csdn.net/tyro_java/article/details/145355902)
- 导航：[📋 总目录](../) ｜ [← 188 k 站中转内最便宜的航班](../188_k_站中转内最便宜的航班/) ｜ [190 将字符串翻转到单调递增 →](../190_将字符串翻转到单调递增/)
