---
title: 12 BFS 与图 · 经典算法 20 题
date: 2026-11-24
categories: [经典算法]
tags: [前端面试, 笔试题, C, 图]
type: 笔试题
---

# 12 BFS 与图（C-221 ~ C-240）

> 大厂笔试里"看起来是业务题、其实是图论"的重灾区：地图扩散、依赖安装、状态流转，全靠这一套模板。**识别特征**：出现"最短步数 / 最少次数 / 同时扩散 / 依赖先后 / 连通块个数"，网格图先想 BFS/DFS，有向依赖先想拓扑排序，求"任意两点最短路"先想 Dijkstra。

## 题型速查

| 子类型 | 核心手法 | 代表题 |
|---|---|---|
| 网格连通块 | DFS 洪水填充，原地改值代替 visited | C-221、C-222、C-237 |
| 边界反向标记 | 从边界灌水，剩下的才是内部 | C-224、C-237 |
| 多源 BFS | 所有源点一次性入队，层数即最短距离 | C-225、C-226、C-235 |
| 状态 BFS | 状态是"字符串/位掩码"，邻居靠枚举变换 | C-227、C-228、C-234 |
| 拓扑排序 | 入度表 + 队列，出队数不足即有环 | C-229、C-230、C-232 |
| 最短路 | Dijkstra（非负权）/ 边权相同用 BFS | C-233 |
| 并查集 / 连通分量 | 合并相邻块，统计根节点个数 | C-236 |
| 记忆化 DFS | 有向无环的网格图，缓存每格最优值 | C-239 |
| 状态压缩 BFS | `(节点, 已访问集合)` 作为状态 | C-240 |

**三条铁律**：① BFS 必须在**入队时**标记 visited，出队时标记会导致同一节点被重复入队、复杂度爆炸；② 多源 BFS 的答案是"最后一层"而不是"第一个到达的源"；③ 拓扑排序判环看的是"入队节点数是否等于总数"，不是队列是否为空。

---

### C-221 岛屿数量 · 中等 · 字节/阿里/腾讯

**题干**：给定由 `'1'`（陆地）和 `'0'`（水）组成的二维网格 `grid`，计算岛屿的数量。岛屿由水平或垂直方向相邻的陆地连接而成，四周被水包围，可以认为网格的四条边外都是水。`1 <= m, n <= 300`。

**示例**：`输入: grid = [["1","1","0","0"],["1","1","0","0"],["0","0","1","0"],["0","0","0","1"]]` → `输出: 3`

**思路**：
- 本质是求**连通块个数**：外层双循环每遇到一个没访问过的 `'1'`，计数器加一，然后从这个点洪水填充，把整块岛"淹掉"。
- 用**原地改值**（`'1' → '0'`）代替 `visited` 数组：省 O(mn) 空间，也不会漏标记。面试里若不允许改入参，再显式开 `visited`。
- 为什么用 DFS 而不是 BFS：连通块只关心"是否连通"，不关心距离，DFS 写起来最短。但网格 300×300 时递归深度可达 9 万，某些引擎会栈溢出，工程上更稳的是 BFS 或显式栈——这是高频追问。
- 复杂度 O(mn)：每个格子最多被访问常数次（一次外层判断 + 一次填充）。

**代码**：
```javascript
function numIslands(grid) {
  const m = grid.length;
  const n = grid[0].length;
  let count = 0;

  const dfs = (i, j) => {
    if (i < 0 || i >= m || j < 0 || j >= n) return;
    if (grid[i][j] !== '1') return;

    grid[i][j] = '0';            // 淹掉，等价于标记 visited
    dfs(i + 1, j);
    dfs(i - 1, j);
    dfs(i, j + 1);
    dfs(i, j - 1);
  };

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === '1') {
        count++;                 // 发现新岛屿
        dfs(i, j);               // 淹掉整块
      }
    }
  }
  return count;
}
```

**复杂度**：时间 O(m·n)，每格进出各一次；空间 O(m·n) 最坏递归深度（全陆地蛇形分布）。

**易错点**：
- 先 `count++` 再判断 `grid[i][j]`，把水也数进去。
- 忘记四个方向都要检查越界，`i >= m` 写成 `i > m`。
- 用 `'1'` 与 `1` 混判（字符/数字类型不一致），整张图被当成全水。
- 递归不淹岛只标记 visited，深层网格栈溢出。

**变体与追问**：
- 求最大岛屿面积 → C-222；求岛屿周长 → C-223。
- 若允许把 0 变 1，求最大连通块（LeetCode 827）→ C-238，需要给岛屿编号。
- 网格特别大时改用并查集：每个陆地与上、左邻居合并，最后统计根的数量。

---

### C-222 岛屿的最大面积 · 中等 · 字节/美团

**题干**：给定 `m x n` 的二进制矩阵 `grid`（`0` 水、`1` 陆地），返回岛屿的最大面积。岛屿面积是岛上 `1` 的个数，没有岛屿时返回 `0`。`1 <= m, n <= 50`。

**示例**：`输入: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]` → `输出: 6`

**思路**：
- 与 C-221 同构，把"计数 +1"换成"返回面积并取最大值"。
- `dfs` 的返回值定义为"以 `(i,j)` 为起点能扩展到的陆地格数"，递归时把四个方向的返回值累加，再 `+1` 计自己。
- 依然用原地置 0 标记，保证每格只被计入一次，否则同一块岛会被重复遍历、面积翻倍。
- 外层取 `Math.max`，注意全 0 网格要返回 0，所以初值设 0 而不是 1。
- 与 C-221 的唯一差别是"计数方式"：C-221 用外部计数器累加 1，本题把计数变成**函数返回值**逐层汇总。后者天然支持"每个起点算出自己的面积"，不需要任何额外状态，这也是判断该用哪种写法的依据。

**代码**：
```javascript
function maxAreaOfIsland(grid) {
  const m = grid.length;
  const n = grid[0].length;
  let best = 0;

  const dfs = (i, j) => {
    if (i < 0 || i >= m || j < 0 || j >= n) return 0;
    if (grid[i][j] !== 1) return 0;

    grid[i][j] = 0;                                   // 标记已访问
    return 1 +
      dfs(i + 1, j) + dfs(i - 1, j) +
      dfs(i, j + 1) + dfs(i, j - 1);                  // 自身 + 四个方向
  };

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 1) {
        best = Math.max(best, dfs(i, j));
      }
    }
  }
  return best;
}
```

**复杂度**：时间 O(m·n)；空间 O(m·n) 最坏递归深度。

**易错点**：
- `dfs` 里返回 `1 + ...` 漏掉自身，结果永远少 1。
- 标记与判断顺序颠倒，先置 0 再判断 `!== 1`，永远返回 0。
- 外层没有跳过已访问格子，同一块岛被重复统计（虽然置 0 后不会，但用 visited 数组时容易犯）。
- 用全局 `area` 变量累加却忘记在每块岛开始前清零。

**变体与追问**：
- 求岛屿数量 → C-221（不需要返回值）。
- 求周长 → C-223（数边界边）。
- 求"最多改一个 0 为 1"后的最大面积 → C-238。

---

### C-223 岛屿的周长 · 简单 · 腾讯/快手

**题干**：给定 `m x n` 的二进制矩阵 `grid`，其中 `1` 表示陆地、`0` 表示水域。岛屿内部没有湖（即所有 `1` 连通且不包围水）。求岛屿的周长。`1 <= m, n <= 100`。

**示例**：`输入: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]` → `输出: 16`

**思路**：
- 不要用 DFS 逐格数边界（容易重复计数），用**贡献法**：每块陆地初始贡献 4 条边，每与一个相邻陆地共边，就减去 2 条（双方各少一条）。
- 只需检查**上、左**两个方向：因为"下、右"的相邻关系会在对方的"上、左"检查中被覆盖，重复检查会多减。
- 这就是本题的全部：`perimeter = 4 * 陆地数 - 2 * 相邻陆地对数`。
- 相比 DFS，这个写法 O(mn) 且无需递归、无标记、可并行，是最优解。

**代码**：
```javascript
function islandPerimeter(grid) {
  const m = grid.length;
  const n = grid[0].length;
  let perimeter = 0;

  // 贡献法：每块陆地先给 4 条边，每有一条公共边就减去 2
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] !== 1) continue;

      perimeter += 4;                                  // 先假设四面环水
      if (i > 0 && grid[i - 1][j] === 1) perimeter -= 2;  // 上方有邻居
      if (j > 0 && grid[i][j - 1] === 1) perimeter -= 2;  // 左方有邻居
    }
  }
  return perimeter;
}
```

**复杂度**：时间 O(m·n)；空间 O(1)。

**易错点**：
- 四个方向都检查，每条公共边被减两次（-4），周长偏小。
- 忘记 `i > 0` 判断，第一行访问 `grid[-1]` 得到 `undefined`，条件恒 false 但隐藏风险。
- 把陆地判断写成 `grid[i][j] === '1'`，与数字输入类型不符导致全 0。
- 试图用 DFS 累加"出界次数"，但忘了标记 visited，环状岛屿会死循环。
- 全 0 网格返回 0，本写法天然正确（循环里没有陆地就加不了 4）；若改用 DFS，则要额外处理"无陆地"的情况避免返回 -1。

**变体与追问**：
- 若岛屿内部有湖（周长包含湖岸线），则公共边规则不再成立，必须 DFS 数每条边。
- 若有多座岛，求周长总和：本算法天然支持，无需改。
- 三维版本（投影面积）：换成立方体表面积公式。

---

### C-224 被围绕的区域 · 中等 · 字节/阿里

**题干**：给定 `m x n` 的矩阵 `board`，包含 `'X'` 和 `'O'`。找到所有**被 `'X'` 围绕**的 `'O'` 区域，并将其中所有 `'O'` 替换为 `'X'`。任何在边界上的 `'O'` 都不会被完全围绕，与其连通的 `'O'` 同理。要求原地修改。`1 <= m, n <= 200`。

**示例**：`输入: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]` → `输出: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]`

**思路**：
- 正向思路"判断每个 O 是否被围"需要看它能否逃到边界，每个点都要搜一次，代价高。
- **反向思维**：从四条边界上的每个 `'O'` 出发洪水填充，能到达的 `'O'` 一定与外界连通，先临时标记成 `'#'`（既区别于 `'O'` 又不会被二次访问）。
- 一趟扫描后：仍是 `'O'` 的就是被围住的，改成 `'X'`；`'#'` 是逃出去的，还原成 `'O'`。
- 为什么必须用第三个符号而不是直接改成 `'X'`：否则还原阶段无法区分"原本是 X"和"逃出去的 O"。

**代码**：
```javascript
function solve(board) {
  const m = board.length;
  const n = board[0].length;

  const dfs = (i, j) => {
    if (i < 0 || i >= m || j < 0 || j >= n) return;
    if (board[i][j] !== 'O') return;
    board[i][j] = '#';                  // 标记为"与边界连通"
    dfs(i + 1, j); dfs(i - 1, j);
    dfs(i, j + 1); dfs(i, j - 1);
  };

  // 从四条边界灌水
  for (let i = 0; i < m; i++) { dfs(i, 0); dfs(i, n - 1); }
  for (let j = 0; j < n; j++) { dfs(0, j); dfs(m - 1, j); }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 'O') board[i][j] = 'X';       // 被围住
      else if (board[i][j] === '#') board[i][j] = 'O';  // 还原
    }
  }
}
```

**复杂度**：时间 O(m·n)，每个格子最多被 DFS 访问一次；空间 O(m·n) 递归栈。

**易错点**：
- 只从四个角灌水，漏掉边界中间位置的 `'O'`（必须遍历整条边）。
- 标记成 `'X'` 后无法还原，边界连通的 O 被误吃。
- 最后扫描时把 `'#'` 也当成 `'O'` 处理，所有逃出的 O 又被改成 X。
- 边界循环写成 `dfs(i, 0)` 但忘了 `dfs(i, n - 1)`。

**变体与追问**：
- 若要求返回被围区域的个数：在最后扫描时对每块 `'O'` 计数并填充。
- 若允许斜向连通：方向数组扩成 8 个，但"围绕"的语义会变。
- 若矩阵极大：用并查集把边界 O 合并到一个虚拟根，最后一趟判断根。

---

### C-225 腐烂的橘子 · 中等 · 字节/腾讯/美团

**题干**：给定 `m x n` 网格，`0` 空、`1` 新鲜橘子、`2` 腐烂橘子。每分钟，腐烂橘子会让**上下左右**相邻的新鲜橘子腐烂。返回直到没有新鲜橘子为止所经过的分钟数；若不可能全部腐烂，返回 `-1`。`1 <= m, n <= 10`。

**示例**：`输入: grid = [[2,1,1],[1,1,0],[0,1,1]]` → `输出: 4`

**思路**：
- 这是**多源 BFS** 的标准模型：所有腐烂橘子是同一层的源点，一起向外扩散，扩散的层数就是分钟数。
- 为什么不能用单源 BFS 跑多次取最小：多源同时扩散与"分别 BFS 取最小值"结果相同，但前者一趟 O(mn)，后者 O(mn·源点数)。
- 关键细节：**入队时立刻把格子改成 2**，而不是出队时。否则同一格会被多个邻居重复入队，队列膨胀到 O((mn)²)，直接超时。
- 循环条件写 `while (queue.length && fresh > 0)`：没有新鲜橘子时提前结束，避免多算一分钟。
- 最后 `fresh === 0 ? minutes : -1`：还有剩的就说明被隔离了。

**代码**：
```javascript
function orangesRotting(grid) {
  const m = grid.length;
  const n = grid[0].length;
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  const queue = [];
  let fresh = 0;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 2) queue.push([i, j]);   // 多源：全量入队
      else if (grid[i][j] === 1) fresh++;
    }
  }

  let minutes = 0;
  let head = 0;
  while (head < queue.length && fresh > 0) {
    const size = queue.length - head;             // 当前层节点数
    for (let k = 0; k < size; k++) {
      const [i, j] = queue[head++];
      for (const [di, dj] of dirs) {
        const x = i + di;
        const y = j + dj;
        if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] !== 1) continue;
        grid[x][y] = 2;                           // 入队即标记，防止重复入队
        fresh--;
        queue.push([x, y]);
      }
    }
    minutes++;
  }

  return fresh === 0 ? minutes : -1;
}
```

**复杂度**：时间 O(m·n)，每格最多入队一次；空间 O(m·n) 队列。

**易错点**：
- 在出队时才标记 `grid[x][y] = 2`，同一格被四个邻居各推一次，队列爆炸。
- 用 `while (queue.length)` 不判 `fresh`，最后一轮空转导致分钟数 +1。
- `minutes++` 写在 `for` 层循环内部，变成按"节点"计数而不是按"分钟"计数，答案远大于正确值。
- 初始就没有新鲜橘子时，若把 `minutes++` 提到 `while` 之外，会返回 1 而不是 0。

**变体与追问**：
- 若腐烂速度不同（有权扩散）：变成多源 Dijkstra。
- 若求"所有橘子腐烂的最短时间"且允许放置一个新腐烂橘子：枚举放置点 + BFS，规模大时用最短路预处理。
- 单向扩散改成双向（同时从新鲜侧收缩）：双向 BFS，常用于单词接龙类题目。

---
### C-226 01 矩阵 · 中等 · 字节/阿里

**题干**：给定 `m x n` 的二进制矩阵 `mat`，返回一个同样大小的矩阵 `dist`，其中 `dist[i][j]` 是 `(i, j)` 到最近的 `0` 的曼哈顿距离。相邻格子距离为 1。`1 <= m, n <= 10^4`，`m·n` 不超过 10^4。

**示例**：`输入: mat = [[0,0,0],[0,1,0],[1,1,1]]` → `输出: [[0,0,0],[0,1,0],[1,2,1]]`

**思路**：
- 若对每个 1 各跑一次 BFS，复杂度 O((mn)²)，必超时。正确做法是**多源 BFS**：把全部 0 当作第 0 层一起入队，向外扩散，第一次到达某格时的层数就是它的最短距离。
- 为什么多源 BFS 等价于"对每个 1 找最近 0"：BFS 按层扩展保证"先到达即最近"，而多个源同时扩散时，某格被谁先到达，就等于谁离它最近——取了个天然的 min。
- 距离数组同时充当 visited：初始化为 `-1`，表示未访问；等于 `-1` 才可入队，于是天然去重。
- 不需要额外的 `level` 变量，直接用 `dist[i][j] + 1` 递推即可。

**代码**：
```javascript
function updateMatrix(mat) {
  const m = mat.length;
  const n = mat[0].length;
  const dist = Array.from({ length: m }, () => new Array(n).fill(-1));
  const queue = [];

  // 所有 0 同时入队，构成第 0 层
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (mat[i][j] === 0) {
        dist[i][j] = 0;
        queue.push([i, j]);
      }
    }
  }

  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  let head = 0;
  while (head < queue.length) {
    const [i, j] = queue[head++];
    for (const [di, dj] of dirs) {
      const x = i + di;
      const y = j + dj;
      if (x < 0 || x >= m || y < 0 || y >= n) continue;
      if (dist[x][y] !== -1) continue;        // 已访问，跳过（兼顾去重）
      dist[x][y] = dist[i][j] + 1;            // 由上一层推出
      queue.push([x, y]);
    }
  }
  return dist;
}
```

**复杂度**：时间 O(m·n)，每格入队一次；空间 O(m·n) 队列与结果。

**易错点**：
- 用 `mat[x][y] === 0` 判断是否访问，导致 0 被反复入队。
- 每个 1 单独 BFS，`10^4` 个格子时超时。
- 距离写成 `dist[i][j]++`（自增源点），没有传播性。
- 外层队列用 `shift()`，虽然是 O(n) 但 10^4 规模下仍可通过；更规范用 `head` 指针。

**变体与追问**：
- 若求"到最近的 1"：把 0 和 1 的角色互换即可。
- 若允许斜向移动：方向数组扩成 8 个，距离变成切比雪夫距离。
- 若要求欧氏距离：不能 BFS，需几何方法或多源 Dijkstra 近似。

---

### C-227 单词接龙 · 困难 · 字节/阿里/腾讯

**题干**：给定 `beginWord`、`endWord` 和词典 `wordList`，求从 `beginWord` 到 `endWord` 的**最短转换序列长度**。每次只能改变一个字母，且中间单词必须在词典中。不存在则返回 0。`1 <= beginWord.length <= 10`，`wordList` 长度 ≤ 5000，所有单词等长且只含小写字母。

**示例**：`输入: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]` → `输出: 5`（hit → hot → dot → dog → cog）

**思路**：
- 建模成无权图：词是节点，相差一个字母的两词之间连边。求最短路径 → BFS。
- 暴力建图是 O(N²·L)：两两比对。更优做法是**通配模式哈希**：把每个词的每一位替换成 `*` 作为 key（`hot` → `*ot`、`h*t`、`ho*`），同一个 key 下的词互为邻居。建表 O(N·L²)（切片开销），查邻居 O(1) 平均。
- BFS 从 `beginWord` 出发，每层对应"转换一次"，层数即序列长度（起点算 1 层）。
- 必须**入队时标记 visited**：否则同一个词会被同层多个邻居重复加入，队列规模指数膨胀。

**代码**：
```javascript
function ladderLength(beginWord, endWord, wordList) {
  const dict = new Set(wordList);
  if (!dict.has(endWord)) return 0;          // 终点不在词典，必然无解

  const L = beginWord.length;
  const patterns = new Map();                // 通配模式 -> 单词列表
  for (const w of [beginWord, ...dict]) {
    for (let i = 0; i < L; i++) {
      const key = w.slice(0, i) + '*' + w.slice(i + 1);
      if (!patterns.has(key)) patterns.set(key, []);
      patterns.get(key).push(w);
    }
  }

  const visited = new Set([beginWord]);
  let queue = [beginWord];
  let steps = 1;                             // 起点本身算一层

  while (queue.length) {
    const next = [];
    for (const w of queue) {
      if (w === endWord) return steps;
      for (let i = 0; i < L; i++) {
        const key = w.slice(0, i) + '*' + w.slice(i + 1);
        for (const nb of patterns.get(key) || []) {
          if (visited.has(nb)) continue;      // 入队即判重
          visited.add(nb);
          next.push(nb);
        }
      }
    }
    queue = next;
    steps++;
  }
  return 0;
}
```

**复杂度**：时间 O(N·L²)，建表与 BFS 均为该量级；空间 O(N·L) 存模式表。

**易错点**：
- 只判 `dict.has(endWord)` 却没把 `beginWord` 加入模式表，起点找不到邻居直接返回 1。
- 出队时才标记 visited，同层重复入队，5000 词时内存爆炸。
- `steps` 从 0 开始，答案少 1（路径长度按节点数计）。
- 每次生成邻居都遍历整张 wordList（O(N) 判断差一字符），整体退化为 O(N²·L)，大数据超时。

**变体与追问**：
- 求所有最短路径（LeetCode 126）：BFS 建层 + DFS 回溯，或用"记录前驱"的反向图。
- 双向 BFS：从两端同时扩散，搜索空间从 b^d 降到 2·b^(d/2)，是"能否再快"的标准答案。
- 若词典很大但单词短：模式表比暴力建图更划算，反之则相反。

---

### C-228 打开转盘锁 · 中等 · 字节/腾讯

**题干**：转盘锁有 4 个圆形拨轮，每个有 `0-9` 十个数字，可向上或向下拨动（`0` 向下变 `9`）。初始为 `"0000"`。给定死亡数字列表 `deadends` 和目标 `target`，求最少拨动次数；无法解锁返回 `-1`。`1 <= deadends.length <= 500`。

**示例**：`输入: deadends = ["0201","0101","0102","1212","2002"], target = "0202"` → `输出: 6`

**思路**：
- 状态是一串 4 位数字，共 10^4 = 10000 个状态；每个状态有 4×2 = 8 个邻居。求最少步数 → BFS。
- 用 `Set` 存 visited 与 dead，均 O(1) 查询；`deadends` 里含 `"0000"` 时直接返回 -1（起点就死了）。
- 邻居生成技巧：`(digit + 1) % 10` 与 `(digit + 9) % 10` 统一了"加一/减一"，避免写两段带 if 的代码，也就不会漏掉 0↔9 的环绕。
- BFS 的层数就是转动次数；用"当前层整体出队"的方式推进，而不是给每个状态存 step，可以省一份数据。
- 为什么不能 DFS：题目问"最少拨动次数"，DFS 必须枚举所有路径再取最小，状态数 10^4、每状态 8 邻居时基本跑不完；BFS 按层扩展保证首次到达即最优。

**代码**：
```javascript
function openLock(deadends, target) {
  const dead = new Set(deadends);
  if (dead.has('0000')) return -1;

  const visited = new Set(['0000']);
  let queue = ['0000'];
  let steps = 0;

  while (queue.length) {
    const next = [];
    for (const cur of queue) {
      if (cur === target) return steps;
      for (let i = 0; i < 4; i++) {
        for (const delta of [1, 9]) {           // +1 或 -1（mod 10）
          const d = (Number(cur[i]) + delta) % 10;
          const nb = cur.slice(0, i) + d + cur.slice(i + 1);
          if (visited.has(nb) || dead.has(nb)) continue;
          visited.add(nb);                      // 入队即标记
          next.push(nb);
        }
      }
    }
    queue = next;
    steps++;
  }
  return -1;
}
```

**复杂度**：时间 O(10^4 × 4 × 2) = O(1)（状态数固定，可视为常数）；空间 O(10^4)。

**易错点**：
- 忘记 `dead.has('0000')` 判断，起点死亡时仍返回 0。
- `-1` 用 `(d - 1) % 10`，JS 里 `0 - 1 = -1`，得到 `"-1"` 非法状态。
- 在出队时才加入 visited，同一状态被反复入队。
- `steps` 在循环内按节点自增而非按层自增。

**变体与追问**：
- 双向 BFS：从 `"0000"` 和 `target` 同时搜，状态空间 10^4 时提升明显。
- 若拨轮数为 n：状态数 10^n，BFS 仍可用但内存增长快，需要 A* 或 IDA*。
- 若要输出最短路径本身：BFS 记录 `parent` 映射，最后回溯。

---

### C-229 课程表 · 中等 · 字节/阿里/美团

**题干**：共 `numCourses` 门课，编号 `0..numCourses-1`。`prerequisites[i] = [a, b]` 表示修课程 `a` 之前必须先修 `b`。判断是否可能完成所有课程。`1 <= numCourses <= 2000`，`0 <= prerequisites.length <= 5000`。

**示例**：`输入: numCourses = 2, prerequisites = [[1,0]]` → `输出: true`；`输入: numCourses = 2, prerequisites = [[1,0],[0,1]]` → `输出: false`

**思路**：
- "能否修完"等价于"这张有向图是否**无环**"。有环说明存在互相依赖的课，永远修不完。
- Kahn 算法（BFS 拓扑排序）：统计每个节点的入度，入度为 0 的（没有前置课）先入队，出队时把它的所有后继入度减 1，减到 0 就入队。
- 为什么"出队数量 < 总数"就说明有环：环上的每个节点入度永远不会降到 0（环内互相提供入度），于是永远进不了队列，一定有节点被剩下。
- 必须先把整张图的入度算完再初始化队列，不能边建图边入队。

**代码**：
```javascript
function canFinish(numCourses, prerequisites) {
  const adj = Array.from({ length: numCourses }, () => []);
  const indegree = new Array(numCourses).fill(0);

  for (const [a, b] of prerequisites) {
    adj[b].push(a);          // 先修 b -> 后修 a
    indegree[a]++;           // a 多了一个前置
  }

  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (indegree[i] === 0) queue.push(i);   // 无前置的课先修
  }

  let head = 0;
  let finished = 0;
  while (head < queue.length) {
    const cur = queue[head++];
    finished++;
    for (const next of adj[cur]) {
      if (--indegree[next] === 0) queue.push(next);  // 前置全部修完
    }
  }

  return finished === numCourses;   // 有环时必有节点未出队
}
```

**复杂度**：时间 O(V + E)，每个节点与每条边各处理一次；空间 O(V + E) 邻接表。

**易错点**：
- 边方向建反（`adj[a].push(b)`），入度也加在 `b` 上，逻辑变成"a 是 b 的前置"，答案相反。
- 用 `queue.shift()` 导致 O(V²)，2000 节点虽能过，但面试官会指出。
- 判断条件写成 `queue.length === numCourses`（队列已清空，永远为 0）。
- 只检查入度为 0 的节点是否存在，不统计出队总数，无法发现局部环。

**变体与追问**：
- 要输出修课顺序 → C-230。
- 用 DFS 染色（0 未访问 / 1 访问中 / 2 已完成）判环：遇到"访问中"的节点即有环，代码更短但需要显式栈。
- 若要求"每学期最多修 k 门"：拓扑排序 + 分层，或用优先队列按截止时间调度。

---

### C-230 课程表 II · 中等 · 字节/腾讯

**题干**：同 C-229 的课程依赖关系，返回**任意一种**可行的修课顺序；若不可能完成所有课程，返回空数组。`1 <= numCourses <= 2000`。

**示例**：`输入: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]` → `输出: [0,2,1,3]`（或 `[0,1,2,3]`）

**思路**：
- 与 C-229 完全同构，只是把"计数"换成"收集出队顺序"。Kahn 算法出队的顺序天然就是一个合法拓扑序。
- 为什么出队序一定合法：一个节点只有在其全部前置都已出队（入度降为 0）时才入队，因此它永远排在后继之前。
- 若结果长度小于 `numCourses`，说明有环，按题意返回 `[]`。
- 也可以 DFS 后序遍历再反转，但 Kahn 更直观，且能顺带判环，是大厂默认答案。

**代码**：
```javascript
function findOrder(numCourses, prerequisites) {
  const adj = Array.from({ length: numCourses }, () => []);
  const indegree = new Array(numCourses).fill(0);

  for (const [a, b] of prerequisites) {
    adj[b].push(a);
    indegree[a]++;
  }

  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (indegree[i] === 0) queue.push(i);
  }

  const order = [];
  let head = 0;
  while (head < queue.length) {
    const cur = queue[head++];
    order.push(cur);                       // 出队即入结果
    for (const next of adj[cur]) {
      if (--indegree[next] === 0) queue.push(next);
    }
  }

  return order.length === numCourses ? order : [];
}
```

**复杂度**：时间 O(V + E)；空间 O(V + E)。

**易错点**：
- 有环时返回 `order`（部分序列）而不是 `[]`。
- 结果长度判断写成 `order.length > 0`，只要修了一门就返回，掩盖环。
- 忘记 `--indegree[next]` 的副作用，写成 `indegree[next] - 1` 比较，入度永不减少。
- 依赖对的方向读反（`[a,b]` 是 a 依赖 b），拓扑序整体颠倒。
- `order.push(cur)` 如果挪到"后继入队时"执行，输出顺序会整体错位（后继还没修完就被记录）；必须严格"出队即入结果"。

**变体与追问**：
- 若要求字典序最小的拓扑序：把队列换成最小堆，O((V+E) log V)。
- 若同时存在多组依赖且要求"同一学期可并行修"：BFS 分层，每层即一个学期。
- 若图不连通：Kahn 天然处理，多个入度 0 的起点都会入队。

---
### C-231 克隆图 · 中等 · 字节/阿里

**题干**：给定无向连通图中一个节点的引用 `node`，返回该图的**深拷贝**（克隆）。每个节点包含 `val` 和 `neighbors` 列表。`1 <= 节点数 <= 100`，`1 <= node.val <= 100` 且唯一，图中可能有自环与重边。节点类定义与 LeetCode 一致（`val` + `neighbors`）。

**示例**：`输入: adjList = [[2,4],[1,3],[2,4],[1,3]]` → `输出: [[2,4],[1,3],[2,4],[1,3]]`（返回的是新图）

**思路**：
- 图有环，直接递归拷贝会在环上无限展开。必须用 `Map<原节点, 克隆节点>` 做**访问登记**。
- 顺序是本题灵魂：**先创建克隆并写进 map，再递归处理邻居**。如果先递归邻居再登记，遇到 A→B→A 时 A 还没登记，会再克隆一个 A，无限递归。
- 命中 `map` 直接返回已有克隆，这样同一个原节点在全图中只会有一个对应克隆，环也能正确闭合。
- 空图返回 `null`；连通图从一个节点出发即可覆盖全图，非连通则需外层遍历所有节点。

**代码**：
```javascript
// LeetCode 提供的节点类，这里显式给出以便本地运行
class GraphNode {
  constructor(val, neighbors = []) {
    this.val = val;
    this.neighbors = neighbors;
  }
}

function cloneGraph(node) {
  if (!node) return null;

  const map = new Map();          // 原节点 -> 克隆节点

  const dfs = (n) => {
    if (map.has(n)) return map.get(n);   // 已克隆，直接复用（处理环）

    const copy = new GraphNode(n.val);
    map.set(n, copy);                    // 先登记，再递归邻居

    for (const nb of n.neighbors) {
      copy.neighbors.push(dfs(nb));
    }
    return copy;
  };

  return dfs(node);
}
```

**复杂度**：时间 O(V + E)，每个节点与每条边访问一次；空间 O(V) 哈希表 + 递归栈。

**易错点**：
- 先递归邻居再 `map.set`，遇到环直接栈溢出。
- 克隆节点时把 `neighbors` 直接赋值（浅拷贝引用），新图与原图共享邻居。
- `map` 里存的是 `val` 而不是节点引用，遇到重复值（虽然本题 val 唯一）或同一值多节点时出错。
- 忘记处理 `null` 输入，LeetCode 有空图用例。

**变体与追问**：
- 非连通图：外层用 `visited` 遍历所有节点，逐个 `dfs`。
- 用 BFS 克隆：队列存原节点，出队时创建/填充克隆，效果相同且不怕深递归。
- 若要"深比较两张图是否同构"：同时 BFS 两图，边比对边标记。

---

### C-232 找到最终的安全状态 · 中等 · 字节/美团

**题干**：有向图中有 `n` 个节点，`graph[i]` 是节点 `i` 指向的节点列表。若从节点 `x` 出发的**所有**路径都能走到终端节点（出度为 0 的节点），则 `x` 是安全节点。返回所有安全节点，升序排列。`1 <= n <= 10^4`，边数 ≤ 3.2×10^4。

**示例**：`输入: graph = [[1,2],[2,3],[5],[0],[5],[],[]]` → `输出: [2,4,5,6]`

**思路**：
- 直白的 DFS 判断"是否所有路径都到达终端"需要三色标记，容易写错。更优雅的是**反向图 + 拓扑消元**。
- 观察：出度为 0 的节点一定是安全的。若一个节点的所有出边都指向已确认安全的节点，它也安全。这正是"从终端反向做拓扑排序"。
- 做法：建反图 `radj`，用 `outdeg` 记录原图出度；把出度 0 的节点入队；出队时标记安全，并把反图中指向它的前驱出度减 1，减到 0 就入队。
- 为什么这能排除环：环上的节点出度永远降不到 0（环内互相"消耗"），永远不会入队，自然被排除。

**代码**：
```javascript
function eventualSafeNodes(graph) {
  const n = graph.length;
  const radj = Array.from({ length: n }, () => []);   // 反向边
  const outdeg = new Array(n).fill(0);

  for (let u = 0; u < n; u++) {
    outdeg[u] = graph[u].length;
    for (const v of graph[u]) radj[v].push(u);        // v <- u
  }

  const queue = [];
  for (let i = 0; i < n; i++) {
    if (outdeg[i] === 0) queue.push(i);               // 终端节点
  }

  const safe = new Array(n).fill(false);
  let head = 0;
  while (head < queue.length) {
    const v = queue[head++];
    safe[v] = true;
    for (const u of radj[v]) {
      if (--outdeg[u] === 0) queue.push(u);           // u 的所有出边都安全
    }
  }

  const res = [];
  for (let i = 0; i < n; i++) if (safe[i]) res.push(i);
  return res;
}
```

**复杂度**：时间 O(V + E)；空间 O(V + E)。

**易错点**：
- 反图方向建反（`radj[u].push(v)`），拓扑方向错误，结果只剩终端节点。
- 用入度而不是出度：本题的"安全"依赖出边，用入度会得到完全相反的结论。
- 判断条件写成 `--outdeg[u] === 0` 但 `outdeg` 初始没设成原图出度。
- 结果忘记升序：按 `i` 从 0 到 n 扫描即为升序，若用 Set 后再展开需手动排序。

**变体与追问**：
- DFS 三色法：`0` 未访问、`1` 访问中、`2` 安全；遇到 `1` 说明成环，回溯时把路径标记为不安全。代码更短但难写对。
- 求"所有环上的节点"：拓扑消元后剩下的节点正好是环及指向环的节点，与安全节点互补。
- 若要求"最短安全路径"：在安全子图上 BFS。

---

### C-233 网络延迟时间 · 中等 · 字节/阿里/腾讯

**题干**：有 `n` 个网络节点，`times[i] = [u, v, w]` 表示信号从 `u` 到 `v` 需要 `w` 时间。从节点 `k` 发出信号，求使所有节点都收到信号所需的**最少时间**；有节点收不到则返回 `-1`。`1 <= k <= n <= 100`，`1 <= times.length <= 6000`。

**示例**：`输入: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2` → `输出: 2`

**思路**：
- 单源最短路：答案是 `max(dist[k][v])`——所有节点都收到信号的时间，取决于最远的那个。
- 边权非负且不相等，不能用普通 BFS，要用 **Dijkstra**。核心是"每次取出当前距离最小的未确定节点，用它松弛邻居"，这保证该节点距离已达最优。
- 本题 `n <= 100`，用 O(n²) 的朴素实现（每次线性扫描找最小）足够，代码也最短；堆优化是 O(E log V)，在大图上才必要。
- 若存在 `dist` 仍为 `Infinity` 的节点，说明图不连通，返回 -1。

**代码**：
```javascript
function networkDelayTime(times, n, k) {
  const INF = Infinity;
  // 邻接矩阵，重边取最小
  const w = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(INF));
  for (const [u, v, t] of times) w[u][v] = Math.min(w[u][v], t);

  const dist = new Array(n + 1).fill(INF);
  const done = new Array(n + 1).fill(false);
  dist[k] = 0;

  for (let round = 1; round <= n; round++) {
    let u = -1;
    for (let i = 1; i <= n; i++) {
      if (!done[i] && (u === -1 || dist[i] < dist[u])) u = i;  // 取最小未确定点
    }
    if (u === -1 || dist[u] === INF) break;    // 剩下的都不可达
    done[u] = true;

    for (let v = 1; v <= n; v++) {
      if (w[u][v] !== INF && dist[u] + w[u][v] < dist[v]) {
        dist[v] = dist[u] + w[u][v];           // 松弛
      }
    }
  }

  let ans = 0;
  for (let i = 1; i <= n; i++) {
    if (dist[i] === INF) return -1;
    ans = Math.max(ans, dist[i]);
  }
  return ans;
}
```

**复杂度**：时间 O(n² + E)；空间 O(n²)。

**易错点**：
- 用 BFS 求最短路：边权不为 1，BFS 得不到正确结果。
- 重边不做 `Math.min`，保留了较大的权值，答案偏大。
- 忘记 `done` 数组，节点被反复选中松弛，可能死循环（负权时更明显）。
- 只返回 `dist` 的最大值而不判 `Infinity`，不连通时返回 `Infinity` 而不是 -1。
- 矩阵开成 `(n+1) x (n+1)` 是为了直接使用 1-based 的节点编号；若改用 0-based，`times` 里的 `u`、`v` 都要统一减 1。

**变体与追问**：
- 堆优化 Dijkstra：适合 `n` 大、边稀疏（如 10^5 节点），复杂度 O(E log V)。
- 边权有负数：Dijkstra 失效，改 Bellman-Ford / SPFA。
- 求"任意两点最短路"：Floyd O(n³)，n ≤ 400 时可用。
- 求"最多允许 k 次中转"：加一维状态 `dist[v][hop]`。

---

### C-234 最小基因变化 · 中等 · 字节/腾讯

**题干**：基因序列由 `'A','C','G','T'` 组成，长度为 8。给定起始基因 `startGene`、目标基因 `endGene` 和基因库 `bank`，每次只能改变一个字符，且结果必须在 `bank` 中。求最少变化次数，不可能则返回 `-1`。`0 <= bank.length <= 10`。

**示例**：`输入: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]` → `输出: 1`

**思路**：
- 与 C-227 单词接龙同构，只是"邻居"的生成方式不同：单词接龙靠通配模式预建索引，本题字母表固定为 4 个字符、长度固定为 8，直接**枚举 8×4 种变换**更简单（每个状态最多 32 个候选）。
- 与 BFS 的配合：每层代表一次基因变化，第一次到达 `endGene` 的层数就是答案。
- `bank` 必须转成 `Set`：既用于 O(1) 判断合法性，也顺手作为"存在性"检查——`endGene` 不在 bank 中直接返回 -1。
- visited 必须包含 `startGene`，否则起点会被邻居再次入队。

**代码**：
```javascript
function minMutation(startGene, endGene, bank) {
  const valid = new Set(bank);
  if (!valid.has(endGene)) return -1;           // 目标不在库中，不可达

  const CHARS = ['A', 'C', 'G', 'T'];
  const visited = new Set([startGene]);
  let queue = [startGene];
  let steps = 0;

  while (queue.length) {
    const next = [];
    for (const gene of queue) {
      if (gene === endGene) return steps;
      for (let i = 0; i < gene.length; i++) {
        for (const c of CHARS) {
          if (gene[i] === c) continue;              // 没变化，跳过
          const nb = gene.slice(0, i) + c + gene.slice(i + 1);
          if (!valid.has(nb) || visited.has(nb)) continue;
          visited.add(nb);                          // 入队即标记
          next.push(nb);
        }
      }
    }
    queue = next;
    steps++;
  }
  return -1;
}
```

**复杂度**：时间 O(N·L·4)，N 为 bank 大小、L=8，每个状态扩展 32 个候选；空间 O(N)。

**易错点**：
- 忘记 `valid.has(endGene)`，目标不在库中时会白白搜完整张图再返回 -1。
- 漏掉 `gene[i] === c` 的跳过，生成与自身相同的"邻居"，虽然被 visited 挡住但浪费。
- `visited` 未初始化为含起点，起点被重新入队。
- `steps` 从 1 开始计数，答案偏大。

**变体与追问**：
- 若 `bank` 很大（10^5）：枚举 32 个候选仍可接受（O(32N)），比建图 O(N²) 好得多。
- 若要输出变化路径：BFS 记录 `parent`。
- 若变化规则变成"任意两个字符可同时改"：状态空间不变，但邻居生成需要组合枚举。

---

### C-235 地图分析 · 中等 · 字节/美团

**题干**：给定 `n x n` 的网格 `grid`，`1` 表示陆地、`0` 表示海洋。求**海洋格子**到最近陆地的曼哈顿距离的最大值（即"离陆地最远的海"）；若全是陆地或全是海洋，返回 `-1`。`1 <= n <= 100`。

**示例**：`输入: grid = [[1,0,1],[0,0,0],[1,0,1]]` → `输出: 2`

**思路**：
- 与 C-226 的 01 矩阵几乎是同一题，只是返回值从"整张距离表"变成"最大距离"。
- 多源 BFS：所有陆地作为第 0 层一起入队，逐层向外扩散，每一层对应距离 +1。最后一个被访问到的海洋格的距离就是答案。
- 边界条件必须单独处理：`n*n` 个格子全是陆地时没有海洋，全是海洋时没有源点，两种情况都返回 -1。
- 原地把访问过的 0 改成 1，省一个 visited 数组；因为之后不再需要原始值。

**代码**：
```javascript
function maxDistance(grid) {
  const n = grid.length;
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  const queue = [];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 1) queue.push([i, j]);   // 所有陆地同时入队
    }
  }
  if (queue.length === 0 || queue.length === n * n) return -1;

  let dist = -1;
  let head = 0;
  while (head < queue.length) {
    dist++;                                        // 进入下一层
    const size = queue.length - head;              // 本层节点数
    for (let k = 0; k < size; k++) {
      const [i, j] = queue[head++];
      for (const [di, dj] of dirs) {
        const x = i + di;
        const y = j + dj;
        if (x < 0 || x >= n || y < 0 || y >= n || grid[x][y] !== 0) continue;
        grid[x][y] = 1;                            // 标记已访问
        queue.push([x, y]);
      }
    }
  }
  return dist;
}
```

**复杂度**：时间 O(n²)；空间 O(n²) 队列。

**易错点**：
- 忘记全陆地/全海洋的边界，全陆地时 `dist` 会是 0 而非 -1。
- `dist` 从 0 开始，答案比正确值小 1（第 0 层是陆地本身，海洋从第 1 层算起）。
- 层内循环用 `while (queue.length)` 边出边入，导致层数统计错乱。
- 用 `grid[x][y] === 1` 判重，但初始陆地也是 1，海洋格第一次被访问后改成 1 才能去重——顺序不能反。

**变体与追问**：
- 若求"每块海洋到最近陆地的距离"：C-226 的 01 矩阵。
- 若距离定义为欧氏距离：多源 BFS 不再适用，需要计算几何。
- 若网格是矩形 `m x n`：把 `n` 的边界判断拆成 `m` 与 `n` 两个变量即可。

---
### C-236 由斜杠划分区域 · 中等 · 字节/快手

**题干**：用 `n x n` 的网格表示一个正方形，每个格子是 `' '`、`'/'` 或 `'\\'`，分别表示空格、从右上到左下的斜线、从左上到右下的斜线。斜线把正方形分割成若干区域，返回区域个数。`1 <= n <= 30`。

**示例**：`输入: grid = [" /","/ "]` → `输出: 2`；`输入: grid = ["/\\","\\/"]` → `输出: 5`

**思路**：
- 斜线是"无限细"的，直接按格子连通会判错。经典技巧是**把每格放大成 3×3**：小格足够细，斜线就能用一串小格近似，且不会出现"斜着穿过去"的歧义。
- 对 `/` 在 3×3 里堵住 `(0,2),(1,1),(2,0)`；对 `\\` 堵住 `(0,0),(1,1),(2,2)`。其余小格为空。
- 在 `3n x 3n` 的图上做**四方向**连通块计数（DFS 洪水填充），每个未被访问的空小格就是一个新区域的起点。
- 为什么四方向就够：被堵住的小格形成斜向链条，四连通无法穿过斜对角，正好把这颗"斜线"当作真实墙壁。

**代码**：
```javascript
function regionsBySlashes(grid) {
  const n = grid.length;
  const N = 3 * n;
  const g = Array.from({ length: N }, () => new Array(N).fill(0));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const ch = grid[i][j];
      const r = 3 * i;
      const c = 3 * j;
      if (ch === '/') {
        g[r][c + 2] = 1; g[r + 1][c + 1] = 1; g[r + 2][c] = 1;
      } else if (ch === '\\') {
        g[r][c] = 1; g[r + 1][c + 1] = 1; g[r + 2][c + 2] = 1;
      }
    }
  }

  const dfs = (i, j) => {
    if (i < 0 || i >= N || j < 0 || j >= N || g[i][j] !== 0) return;
    g[i][j] = 1;                       // 标记为墙，兼作 visited
    dfs(i + 1, j); dfs(i - 1, j);
    dfs(i, j + 1); dfs(i, j - 1);
  };

  let regions = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (g[i][j] === 0) { regions++; dfs(i, j); }
    }
  }
  return regions;
}
```

**复杂度**：时间 O(n²)，共 9n² 个小格；空间 O(n²) 网格 + 递归栈。

**易错点**：
- 放大倍数用 2×2：斜线在 2×2 里只能占对角两格，四连通下会把两侧误连（必须 3×3 才有中间格）。
- `/` 与 `\\` 的墙体坐标写反，导致区域数镜像错误（对称用例能过、非对称用例挂）。
- DFS 里把访问标记写成别的值却仍用 `!== 0` 判断，导致重复计数。
- 只用原始 n×n 网格做 BFS（不放大），斜线两侧直接连通。

**变体与追问**：
- 并查集写法：把 9n² 个小格与右、下邻居合并，最后统计根的数量；适合网格更大时避免递归。
- 若斜线可以交叉（`X` 形）：一格内堵两条对角线，放大后区域数 +1。
- 若只求"是否把正方形分成两块"：等价于判断斜线是否构成从一条边到另一条边的通路。

---

### C-237 统计封闭岛屿的数目 · 中等 · 字节/阿里

**题干**：给定 `m x n` 的矩阵 `grid`，`0` 表示陆地、`1` 表示水域。**封闭岛屿**是完全被水域包围的陆地（不能接触网格边界）。求封闭岛屿数量。`1 <= m, n <= 100`。

**示例**：`输入: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,0,1,0],[1,0,1,1,1,0,1,0],[1,0,1,0,1,0,1,0],[1,0,1,1,1,0,1,0],[1,0,0,0,0,0,1,0],[1,1,1,1,1,1,1,0]]` → `输出: 2`

**思路**：
- 与 C-221 岛屿数量的差别：贴着边界的陆地不算封闭岛，且与边界陆地连通的整块岛都不算。
- 沿用"反向灌水"：先对所有边界上的陆地做 DFS，把与外界连通的部分全部"淹掉"（置 1）。
- 剩下的陆地中，每一块都不与边界相连，必然是封闭岛屿。再扫一遍，每发现一个 0 就计数并淹掉整块。
- 注意本题 `0` 是陆地、`1` 是水，与 C-221 相反，写代码时最容易踩这个语义坑。

**代码**：
```javascript
function closedIsland(grid) {
  const m = grid.length;
  const n = grid[0].length;

  const dfs = (i, j) => {
    if (i < 0 || i >= m || j < 0 || j >= n) return;
    if (grid[i][j] !== 0) return;       // 注意：0 是陆地
    grid[i][j] = 1;                     // 淹掉
    dfs(i + 1, j); dfs(i - 1, j);
    dfs(i, j + 1); dfs(i, j - 1);
  };

  // 第一步：把与边界连通的陆地全部淹掉
  for (let i = 0; i < m; i++) { dfs(i, 0); dfs(i, n - 1); }
  for (let j = 0; j < n; j++) { dfs(0, j); dfs(m - 1, j); }

  // 第二步：剩下的每块陆地都是封闭岛
  let count = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 0) {
        count++;
        dfs(i, j);
      }
    }
  }
  return count;
}
```

**复杂度**：时间 O(m·n)；空间 O(m·n) 递归栈。

**易错点**：
- 把 `0` 当水、`1` 当陆地（惯性思维），结果完全错误。
- 只从四个角灌水，漏掉边界中段的陆地。
- 先统计再淹边界，边界岛屿被误计。
- 淹边界时误把 `1`（水）也改掉，导致后续判断失效（`dfs` 里只处理 0 才对）。
- 快速自测用例：只有一行或一列的网格，所有陆地都与边界相连，答案必须是 0。

**变体与追问**：
- 不要求"封闭"，直接数岛屿 → C-221。
- 若要求返回最大封闭岛屿面积：第二步改成返回面积取 max。
- 若允许斜向连通：封闭的定义会变，边界灌水需用 8 邻域，但"封闭"判定要用 4 邻域的对偶，需谨慎。

---

### C-238 最大人工岛 · 困难 · 字节/美团/拼多多

**题干**：给定 `n x n` 二进制矩阵 `grid`（`1` 陆地、`0` 海洋），最多只能将**一个** `0` 变成 `1`，求操作后岛上最大面积；没有陆地返回 0。`1 <= n <= 500`。

**示例**：`输入: grid = [[1,0],[0,1]]` → `输出: 3`

**思路**：
- 暴力枚举每个 0 变成 1 后重跑 DFS，复杂度 O(n⁴)，500×500 必超时。
- 正确做法分两趟：**第一趟给每块岛编号并记面积**（把 `1` 改成大于 1 的编号 id，`Map<id, area>` 存面积）；**第二趟枚举每个 0**，看它四个方向邻居属于哪些岛，把不同 id 的面积加起来再加 1。
- 为什么必须用 `Set` 去重 id：一个 0 的上下左右可能属于**同一块**岛（比如环绕型），不去重会把面积重复累加。
- 边界情况：整张图全是 1 时没有 0 可变，答案是全图面积，所以 `best` 要先从已有岛屿面积里取最大值。

**代码**：
```javascript
function largestIsland(grid) {
  const n = grid.length;
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  const area = new Map();          // 岛屿编号 -> 面积
  let id = 2;                      // 从 2 开始，避开 0/1

  const dfs = (i, j) => {
    if (i < 0 || i >= n || j < 0 || j >= n || grid[i][j] !== 1) return 0;
    grid[i][j] = id;               // 染色成编号
    let size = 1;
    for (const [di, dj] of dirs) size += dfs(i + di, j + dj);
    return size;
  };

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 1) { area.set(id, dfs(i, j)); id++; }
    }
  }

  let best = [...area.values()].reduce((m, a) => Math.max(m, a), 0);  // 全陆地时无 0 可填

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] !== 0) continue;
      const seen = new Set();
      let total = 1;               // 这个 0 变成的陆地
      for (const [di, dj] of dirs) {
        const x = i + di, y = j + dj;
        if (x < 0 || x >= n || y < 0 || y >= n) continue;
        if (grid[x][y] < 2 || seen.has(grid[x][y])) continue;  // 同一块岛只算一次
        seen.add(grid[x][y]);
        total += area.get(grid[x][y]);
      }
      best = Math.max(best, total);
    }
  }
  return best;
}
```

**复杂度**：时间 O(n²)，每个格子常数次访问；空间 O(n²) 递归栈 + O(n²) 面积表。

**易错点**：
- 不加 `Set` 去重 id，四个邻居同属一块岛时面积翻倍。
- 岛屿编号从 0 或 1 开始，与"未访问/陆地"标记冲突。
- 忘记"全是陆地"的情况，`best` 保持 0，返回 0。
- 把 `grid[i][j] !== 0` 写成 `!== 1`，染色后（值 > 1）的陆地块被当作可填海点。

**变体与追问**：
- 若允许填 k 个格子：NP 难，通常退化为搜索 + 剪枝，或题目限定 k=1。
- 若允许上下左右斜 8 邻域：方向数组扩成 8 个，`Set` 去重逻辑不变。
- 若要求返回操作后最大岛的坐标：在累加时记录来源 id。

---

### C-239 矩阵中的最长递增路径 · 困难 · 字节/阿里/腾讯

**题干**：给定 `m x n` 整数矩阵 `matrix`，找出其中**最长递增路径**的长度。每个格子可向上下左右移动，不能沿对角线，也不能走出边界。`1 <= m, n <= 200`，`-2^31 <= matrix[i][j] <= 2^31 - 1`。

**示例**：`输入: matrix = [[9,9,4],[6,6,8],[2,1,1]]` → `输出: 4`（`1 → 2 → 6 → 9`）

**思路**：
- 朴素 DFS 从每个格子出发找最长路径，复杂度指数级。但这里有个关键性质：**递增约束让图变成有向无环图（DAG）**——沿严格递增方向走不可能回到原点。
- DAG 上同一子问题会被大量重复访问（同一个格子可以被多条路径经过），因此用 `memo[i][j]` 缓存"从该格出发的最长路径长度"，第二次访问 O(1)。
- 这本质是**记忆化搜索 / 拓扑序 DP**：`f(i,j) = 1 + max(f(邻居))`，其中邻居必须严格更大。
- 不需要 visited：严格递增保证不会绕回自己；缓存也保证不会无限递归。

**代码**：
```javascript
function longestIncreasingPath(matrix) {
  if (matrix.length === 0) return 0;
  const m = matrix.length;
  const n = matrix[0].length;
  const memo = Array.from({ length: m }, () => new Array(n).fill(0));
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

  const dfs = (i, j) => {
    if (memo[i][j] !== 0) return memo[i][j];   // 命中缓存

    let best = 1;
    for (const [di, dj] of dirs) {
      const x = i + di;
      const y = j + dj;
      if (x < 0 || x >= m || y < 0 || y >= n) continue;
      if (matrix[x][y] <= matrix[i][j]) continue;   // 必须严格递增
      best = Math.max(best, 1 + dfs(x, y));
    }
    memo[i][j] = best;
    return best;
  };

  let ans = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      ans = Math.max(ans, dfs(i, j));
    }
  }
  return ans;
}
```

**复杂度**：时间 O(m·n)，每格只计算一次、每条边松弛一次；空间 O(m·n) 缓存 + 递归栈。

**易错点**：
- 不加 memo，200×200 的蛇形矩阵直接超时（访问次数指数级）。
- memo 初值用 0 但答案可能为 1，判断写成 `if (memo[i][j])` 恰好可行，但若初值用 -1 则必须改判 `!== -1`。
- 递增条件写成 `matrix[x][y] < matrix[i][j]`（方向反了），求成递减路径。
- 用 visited 数组却没撤销，导致其他路径无法经过该格，答案偏小。

**变体与追问**：
- 若允许相等（非递减）：可能存在环，需要 SCC 缩点或特殊处理，问题难度陡增。
- 若求"最长递增子序列"（一维，可不连续）：LeetCode 300，贪心 + 二分 O(n log n)。
- 若要求输出路径本身：memo 改成记录"最优邻居坐标"，最后回溯。

---

### C-240 访问所有节点的最短路径 · 困难 · 字节/腾讯

**题干**：给定 `n` 个节点的**无向连通图**，`graph[i]` 是节点 `i` 的邻居列表（边权均为 1）。求访问所有节点的最短路径长度。可以从任意节点出发、在任意节点结束，节点和边都可以重复经过。`1 <= n <= 12`。

**示例**：`输入: graph = [[1,2,3],[0],[0],[0]]` → `输出: 4`（路径 `1 → 0 → 2 → 0 → 3`）

**思路**：
- 普通 BFS 的状态只有"当前节点"，但本题还需知道"已经访问过哪些节点"——否则无法判断是否完成。
- 状态定义为 `(当前节点, 已访问集合)`，用**位掩码**表示集合（n ≤ 12，`1 << 12 = 4096`）。总状态数 `n · 2^n`，可接受。
- 这是**状态空间 BFS**：从所有 `(i, 1<<i)` 同时出发（多源，因为起点任意），每走一步 `mask | (1 << v)`，第一次出现 `mask === (1<<n)-1` 时的层数就是答案。
- 访问标记必须针对 `(节点, 掩码)` 二元组，不能只标记节点——同一节点在不同掩码下是不同状态，只标节点会漏解。

**代码**：
```javascript
function shortestPathLength(graph) {
  const n = graph.length;
  const full = (1 << n) - 1;
  const visited = new Set();
  const queue = [];

  // 多源：任意节点都可以作为起点
  for (let i = 0; i < n; i++) {
    queue.push([i, 1 << i]);
    visited.add(i + ',' + (1 << i));
  }

  let steps = 0;
  let head = 0;
  while (head < queue.length) {
    const size = queue.length - head;
    for (let k = 0; k < size; k++) {
      const [u, mask] = queue[head++];
      if (mask === full) return steps;          // 所有节点都访问过

      for (const v of graph[u]) {
        const nextMask = mask | (1 << v);
        const key = v + ',' + nextMask;
        if (visited.has(key)) continue;
        visited.add(key);                       // 入队即标记
        queue.push([v, nextMask]);
      }
    }
    steps++;
  }
  return steps;
}
```

**复杂度**：时间 O(2^n · n²)，状态数 `n·2^n`，每个状态最多扩展 n 个邻居；空间 O(2^n · n)。

**易错点**：
- 只标记 `v` 而不标记 `(v, mask)`，同一节点在不同访问集合下被错误剪枝，答案偏大。
- 只用单源（从 0 出发），但题目允许任意起点，可能不是最优。
- `full` 算成 `1 << n`（多一位），永远达不到，死循环。
- 忘记"起点算已访问"，`mask` 初值写成 0，答案少 1。

**变体与追问**：
- 若边权不为 1：先 Floyd 求全源最短路，再做状态压缩 DP（TSP 型）`dp[mask][v]`。
- 若要求回到起点（哈密顿回路）：这是 TSP，NP 难，n ≤ 20 时用状压 DP。
- 若 n 更大（> 20）：位掩码不可行，需要启发式搜索（A*）或题目另行限制。

---
