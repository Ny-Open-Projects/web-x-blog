---
title: 20 Trie、并查集与高级结构 · 经典算法 20 题
date: 2026-11-24
categories: [经典算法]
tags: [前端面试, 笔试题, C, Trie, 并查集]
type: 笔试题
---

# 20 Trie、并查集与高级结构（C-381 ~ C-400）

> 这一组是笔试里的"分水岭"：**Trie + 回溯**决定你能不能进终面，**并查集**是连通性问题的唯一正解，**线段树 / 树状数组 / 扫描线**则是"这题我会做，但写不出来"的重灾区。它们共同的特点是**模板固定、变体很少**——只要把模板背到能默写，几乎全是送分题。**识别特征**：看到"前缀/单词/自动补全"想到 Trie；看到"连通、合并、是否同属一组、成环"想到并查集（DSU）；看到"单点修改 + 区间查询"想到树状数组或线段树；看到"区间整体加 + 区间求和"想到线段树懒标记；看到"矩形/区间的最值轮廓"想到扫描线。

## 题型速查

| 子类型 | 核心手法 | 代表题 |
|---|---|---|
| Trie + 棋盘回溯 | 字典树剪枝 DFS，命中即删标记 | C-381 |
| Trie 多键索引 | 前缀 + 后缀双索引、倒序插树 | C-382、C-383 |
| Trie 有序检索 | 排序后二分 / 前缀节点下取 Top K | C-384、C-385 |
| 并查集模板 | 路径压缩 + 按秩合并，两行核心 | C-386 |
| 并查集判连通 | 合并成功则连通分量 -1 | C-387、C-392、C-395 |
| 并查集判环 | `union` 返回 false 即成环 | C-388、C-389 |
| 并查集 + 逻辑约束 | 先处理等号，再校验不等号 | C-390 |
| 并查集聚合输出 | 按根归组，组内排序 | C-391 |
| 并查集建图技巧 | 元素与因子 / 行列编号连边 | C-393、C-394 |
| 线段树 | `build` / `query` / `update` + 懒标记下推 | C-396、C-399 |
| 树状数组 | `lowbit` 跳跃，前缀和差分成区间和 | C-397、C-398 |
| 扫描线 + 堆 | 事件排序 + 惰性删除堆顶 | C-400 |

---

### C-381 单词搜索 II · 困难 · 字节/阿里

**题干**：给定一个 `m x n` 二维字符网格 `board` 和一个单词（字符串）列表 `words`，返回**所有**同时在二维网格和字典中出现的单词。单词必须按照字母顺序，通过**相邻的单元格**内的字母构成，其中"相邻"单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在**一个单词内**不允许被重复使用。

**示例**：
```
board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
输出：["eat","oath"]
```

**思路**：
- 如果对每个单词单独做一次 DFS，复杂度是 `O(W · m · n · 4^L)`，单词一多就超时。瓶颈在于**同一批前缀被反复搜索**：`oath` 和 `oat` 共享前缀 `oa`。
- 把 `words` 建成 **Trie**，然后在棋盘上只做**一次** DFS：每走一步就看当前字符能否在 Trie 中匹配下去，匹配不上立即剪枝。这样"共享前缀"的代价只付一次，复杂度降到 `O(m · n · 4^L)`，与单词数量无关。这就是 Trie 在这里的唯一价值。
- 命中单词后要**把 `isEnd` 置空（记录单词后删除标记）**，防止同一个单词从棋盘不同位置被匹配到两次，天然去重，比用 `Set` 再去重更省。
- 回溯时用 `'#'` 原地标记已访问，四个方向递归完再恢复——比额外开 `visited` 数组省空间，也不容易忘记恢复。

**代码**：
```javascript
function findWords(board, words) {
  const root = {};
  for (const w of words) {           // 建 Trie（对象比 Map 更快）
    let p = root;
    for (const ch of w) p = p[ch] || (p[ch] = {});
    p.word = w;                      // 词尾直接存单词，省去拼接
  }
  const m = board.length, n = board[0].length, res = [];
  const dfs = (i, j, node) => {
    if (i < 0 || i >= m || j < 0 || j >= n) return;
    const ch = board[i][j];
    if (ch === '#' || !node[ch]) return;      // 已访问 or Trie 无此分支：剪枝
    const next = node[ch];
    if (next.word) { res.push(next.word); next.word = null; } // 命中后置空防重复
    board[i][j] = '#';                        // 标记
    dfs(i + 1, j, next); dfs(i - 1, j, next);
    dfs(i, j + 1, next); dfs(i, j - 1, next);
    board[i][j] = ch;                         // 回溯还原
  };
  for (let i = 0; i < m; i++)
    for (let j = 0; j < n; j++) dfs(i, j, root);
  return res;
}
```

**复杂度**：时间 O(m·n·3^L)，L 为最长单词长度（第一步之后每步最多 3 个方向，因为不能回头）；空间 O(W·L) 的 Trie + O(L) 递归栈。

**易错点**：
- 忘记在命中后删掉 `word` 标记，同一单词会被不同起点重复收集。
- 回溯时漏掉 `board[i][j] = ch`，后续搜索全部被 `'#'` 挡住。
- Trie 用 `p[ch]` 判断存在时，若字符是 `"constructor"`、`"__proto__"` 这类原型链上的键，普通对象会误判为存在；工程上应用 `Map` 或 `Object.create(null)`。
- 单格单词（如 `"a"`）也要正确处理：入口就该检查 `node[ch].word`，所以命中判断必须放在"进入子节点之后"。

**变体与追问**：
- 追问"棋盘很大、单词很少怎么办"：反过来，用单词首字母做索引，只从首字母格出发，减少无效 DFS。
- 追问"允许对角线相邻"：方向数组从 4 个扩到 8 个。
- 追问"如何返回最长单词"：命中时比较长度即可，不需要额外结构（对应 C-385 的 Trie 解法）。

---

### C-382 前缀和后缀搜索 · 困难 · 字节/阿里

**题干**：设计一个包含一些单词的特殊词典，并找出与给定前缀和后缀匹配的**权重最大**的单词下标。实现 `WordFilter` 类：`WordFilter(String[] words)` 使用词典中的单词初始化；`int f(String pref, String suff)` 返回词典中具有前缀 `pref` 和后缀 `suff` 的单词的**下标**（下标从 0 开始）；如果不存在这样的单词，返回 `-1`；若有多个满足条件的单词，返回**下标最大**的那个。

**示例**：
```
WordFilter w = new WordFilter(["apple"]);
w.f("a", "e"); // 0，apple 前缀 a、后缀 e
```

**思路**：
- 暴力是每次 `f` 扫全表、对每个词做 `startsWith` + `endsWith`，O(N·L) 一次查询，查询多了就超时。
- 关键洞察：**把"前缀 + 后缀"这个二维条件压成一维字符串键**。对每个单词 `w`，枚举它的所有前缀 `p` 和所有后缀 `s`，把 `p + '#' + s` 作为 key 存入哈希表，value 存该单词的下标。`'#'` 是分隔符，保证不会把前缀和后缀串起来误匹配。
- 预处理的代价是 O(N·L²)（每个词 L+1 个前缀 × L+1 个后缀），查询降到 **O(L)**（一次哈希 + 一次字符串拼接）。这是典型的"用空间和预处理换查询速度"。
- 因为按下标从小到大遍历、后写覆盖先写，**同一个 key 自然保留最大下标**，不需要额外比较。这一点必须在答题时说清，否则面试官会怀疑你没处理"取最大下标"的要求。
- 更省空间的解法是**双 Trie**（前缀树 + 倒序后缀树，取交集）或"后缀树节点存下标列表"，但代码量大得多，笔试用 `p#s` 哈希最稳。

**代码**：
```javascript
class WordFilter {
  constructor(words) {
    this.map = new Map();      // "前缀#后缀" -> 单词下标
    for (let i = 0; i < words.length; i++) {
      const w = words[i];
      for (let p = 0; p <= w.length; p++) {
        const prefix = w.slice(0, p);
        for (let s = 0; s <= w.length; s++) {
          // 后写入的 i 更大，直接覆盖 => 天然保留最大下标
          this.map.set(prefix + '#' + w.slice(s), i);
        }
      }
    }
  }
  f(pref, suff) {
    const idx = this.map.get(pref + '#' + suff);
    return idx === undefined ? -1 : idx;
  }
}

const wf = new WordFilter(["apple", "app"]);
console.log(wf.f("a", "e")); // 0（"apple" 下标最大者优先，此处只有它匹配）
console.log(wf.f("a", "p")); // 1
```

**复杂度**：初始化 O(N·L²) 时间与空间；查询 O(L)（拼接字符串的代价）。

**易错点**：
- 分隔符必须是不出现在单词里的字符（`'#'`），否则 `"a"+"b"` 和 `"ab"+""` 会撞 key。
- 循环边界是 `p <= w.length`、`s <= w.length`（含空串），漏掉空前缀/空后缀会少存一批 key。
- 用 `i` 从小到大覆盖写入，**不能**用 `if (!map.has(key))` 再赋值，那样留下的是最小下标。
- 内存是 O(N·L²)，单词 15000 × 长度 7 时约 100 万条，可接受；长度 20 以上就要换双 Trie。

**变体与追问**：
- 追问"如何降空间"：前缀 Trie + 后缀 Trie，在节点上存下标集合，取交集的最大值；或用 AC 自动机。
- 追问"如果是模糊匹配（中间含通配）"：就退化成 C-375 的 DFS 枚举。
- 工程映射：搜索引擎的"前缀 + 属性"联合索引、Elasticsearch 的 edge_ngram。

---

### C-383 回文对 · 困难 · 阿里/字节

**题干**：给定一组**互不相同**的单词，找出所有不同的索引对 `(i, j)`，使得列表中的两个单词 `words[i] + words[j]` 拼接起来是回文字符串。

**示例**：
```
输入：words = ["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]]
解释："dcbaabcd"、"abcddcba"、"slls"、"llssssll" 都是回文串
```

**思路**：
- 暴力是两两拼接再判回文，O(N²·L)。要加速必须**从"回文"的结构入手**：`A + B` 是回文，说明 `A` 可以拆成 `A1 + A2`，其中 `A2` 与 `B` 互为反转、`A1` 自身是回文（或对称的另一半）。
- 于是枚举"切分点"：对每个单词 `w`，在每个位置 `cut` 处切成 `left` 和 `right`。若 `left` 是回文且 `reverse(right)` 存在于词典中（且不是自己），则 `reverse(right) + w` 是回文；若 `right` 是回文且 `reverse(left)` 存在，则 `w + reverse(left)` 是回文。
- 数据结构只需要一个 **`Map<单词, 下标>`** 做 O(1) 的存在性查询——这就是本题"结构选型"的全部内容：回文对本质是**字符串查找问题**，哈希表足够，Trie 只是可选优化（省掉 `reverse` 的 O(L)）。
- 去重靠"切分点范围"控制：第二种情况限定 `cut < w.length`，**排除 `right` 为空串**。否则 `w` 的 `cut = L` 与 `reverse(w)` 的 `cut = 0` 会把同一对答案各产出一遍，这是本题最隐蔽的重复来源。

**代码**：
```javascript
function palindromePairs(words) {
  const index = new Map();
  words.forEach((w, i) => index.set(w, i));
  const isPal = (s) => {
    let i = 0, j = s.length - 1;
    while (i < j) if (s[i++] !== s[j--]) return false;
    return true;
  };
  const reverse = (s) => s.split('').reverse().join('');
  const res = [];
  for (let i = 0; i < words.length; i++) {
    const w = words[i];
    for (let cut = 0; cut <= w.length; cut++) {
      const left = w.slice(0, cut), right = w.slice(cut);
      // 情况一：left 是回文，把 reverse(right) 拼在前面
      if (isPal(left)) {
        const rev = reverse(right);
        if (index.has(rev) && index.get(rev) !== i) res.push([index.get(rev), i]);
      }
      // 情况二：right 是回文，把 reverse(left) 拼在后面（排除 right 为空，避免重复）
      if (cut < w.length && isPal(right)) {
        const rev = reverse(left);
        if (index.has(rev) && index.get(rev) !== i) res.push([i, index.get(rev)]);
      }
    }
  }
  return res;
}
```

**复杂度**：时间 O(N·L²)（每个切分点判回文 O(L)）；空间 O(N·L)（哈希表）。

**易错点**：
- **重复答案**：情况二必须 `cut < w.length`。若写成 `cut <= w.length`，`w` 在 `cut = L`（right 为空串）产出的 `[i, j]` 会和 `words[j]` 在 `cut = 0` 产出的同一对完全重复。
- 必须排除"自己和自己配对"（`index.get(rev) !== i`），除非题目允许同一个单词用两次（本题不允许）。
- 空串单词 `""` 是合法输入，`"" + "aba"` 是回文，靠 `cut = 0` 且 `left=""` 为回文的逻辑能正确处理。
- `isPal` 的循环条件用 `i < j`，用 `i <= j` 也对但多做一次无意义比较；用 `i < j` 更清晰。

**变体与追问**：
- 追问"如何把判回文降到 O(1)"：预处理 `Manacher` 或字符串哈希，把 O(L) 的比较变成 O(1)，总体 O(N·L)。
- 追问"用 Trie 怎么做"：把单词**倒序**插入 Trie，枚举切分点时沿树走，走到词尾就检查剩余部分是否回文。
- 追问"允许重复单词"：索引要从 `单词 -> 下标` 改成 `单词 -> 下标列表`，答案规模可能爆炸。

---

### C-384 搜索推荐系统 · 中等 · 美团/腾讯

**题干**：给你一个产品数组 `products` 和一个字符串 `searchWord`，`products` 中每个产品都是一个字符串。请你设计一个推荐系统，在依次输入单词 `searchWord` 的每一个字母后，推荐 `products` 数组中**前缀与已输入部分相同**的最多**三个**产品。请返回一个二维列表，第 `i` 个列表是输入 `searchWord` 前 `i` 个字母后推荐的产品，且推荐产品需按**字典序升序**排列。

**示例**：
```
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
输出：[["mobile","moneypot","monitor"],
      ["mobile","moneypot","monitor"],
      ["mouse","mousepad"],
      ["mouse","mousepad"],
      ["mouse","mousepad"]]
```

**思路**：
- 每一轮的本质是"在当前前缀匹配的所有产品里，取字典序最小的 3 个"。所以第一件事是**把 `products` 按字典序排好**——排好之后，同一个前缀的匹配结果在数组中一定是**连续的一段**，且段首就是字典序最小的那个。
- 最直接的实现：每输入一个字符，就从头扫一遍 `products`，用 `startsWith` 过滤，凑满 3 个就 `break`。因为是全局有序的，**第一个命中的就是最小的**，不需要排序。复杂度 O(L · N · L)，在本题数据范围内足够。
- 更优的写法是**二分收紧区间**：前缀是单调变长的，所以上一次的匹配区间 `[lo, hi)` 是下一次的子区间，用两次 `lowerBound` 就能把区间收窄，最优解可做到 O(N log N + L log N)。
- 也可以**建 Trie**，在每个节点上预存"该前缀下字典序最小的 3 个产品"，查询 O(L)。这是"预处理换查询"的典型思路，也解释了为什么 Trie 在推荐系统里常见。

**代码**：
```javascript
function suggestedProducts(products, searchWord) {
  products.sort();                 // 全局字典序，保证命中顺序即答案顺序
  const res = [];
  let prefix = '';
  for (const ch of searchWord) {
    prefix += ch;
    const hits = [];
    for (const p of products) {
      if (p.startsWith(prefix)) {
        hits.push(p);
        if (hits.length === 3) break; // 有序，前 3 个就是最小的 3 个
      }
    }
    res.push(hits);
  }
  return res;
}

console.log(suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mou"));
// [[ 'mobile', 'moneypot', 'monitor' ], [ 'mobile', 'moneypot', 'monitor' ], [ 'mouse', 'mousepad' ]]
```

**复杂度**：排序 O(N log N)，每轮 O(N·L)，总 O(N log N + L·N·L)；空间 O(1) 额外（不含返回值）。

**易错点**：
- **忘记排序**，直接从原数组过滤，返回的三个产品不是字典序最小的。
- 每轮必须**新建** `hits` 数组，把同一个数组推进 `res` 会让所有轮次指向同一份数据。
- `startsWith` 的前缀要**累积**（`prefix += ch`），用 `searchWord[i]` 单字符匹配会错。
- 不足 3 个时返回实际数量，不要补空字符串。

**变体与追问**：
- 追问"N = 10⁶ 怎么办"：二分 + 区间收缩，或 Trie 节点预存 Top 3，把单次查询降到 O(L)。
- 追问"如何按热度而非字典序"：把 `products.sort()` 换成按热度排序，逻辑不变。
- 工程映射：搜索框的 suggest 服务、IDE 的代码补全（本质是 Trie + Top K）。

---

### C-385 最长单词 · 中等 · 腾讯/快手

**题干**：给你一个字符串数组 `words`，找出 `words` 中**最长**的一个单词，该单词是由 `words` 中**其他单词**逐步添加**一个字母**组成的。若其中有多个可行的答案，则返回答案中**字典序最小**的单词。若无答案，返回空字符串。单词只能由 `words` 中其他单词逐步添加一个字母组成（即它的**每个前缀都必须是 `words` 中的单词**）。

**示例**：
```
输入：words = ["w","wo","wor","worl","world"]
输出："world"
解释："world" 可由 "w" 逐步加字母得到，且每个中间词都在 words 中
输入：words = ["a","banana","app","appl","ap","apply","apple"]
输出："apple"
解释："apply" 和 "apple" 都能构成，但 "apple" 字典序更小
```

**思路**：
- 题目条件"每个中间词都必须在 `words` 中"等价于：**该单词的所有前缀都必须是 `words` 中的单词**。所以判断一个词合不合法，只需要从长度 1 到 L 枚举前缀，逐个到集合里查。
- 数据结构选 **`Set<string>`**：判断"某个前缀是不是单词"是纯粹的成员查询，哈希表 O(1)；不需要 Trie，因为查询的前缀是**从短到长的固定序列**，没有分支裁剪的价值（Trie 在这里反而更慢）。
- 一次遍历即可：对每个词检查所有前缀，合法就与当前最优比较。比较规则是"**长度更大优先，长度相同则字典序更小**"，两段条件必须都写全。
- 复杂度 O(N·L²)：外层 N 个词、内层 L 个前缀、每次 `slice` 是 O(L)。可以优化成"按长度排序后从长到短找第一个合法的"，但要注意同长度要字典序最小，排序比较器要写对。

**代码**：
```javascript
function longestWord(words) {
  // Set 让"某前缀是否也是单词"变成 O(1) 成员查询
  const set = new Set(words);
  let best = '';
  for (const w of words) {
    let valid = true;
    for (let i = 1; i <= w.length; i++) {
      if (!set.has(w.slice(0, i))) { valid = false; break; } // 任一前缀缺失就不合法
    }
    if (!valid) continue;
    // 更长优先；等长时字典序更小优先
    if (w.length > best.length || (w.length === best.length && w < best)) best = w;
  }
  return best;
}

console.log(longestWord(["w", "wo", "wor", "worl", "world"])); // world
console.log(longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])); // apple
console.log(longestWord(["abc", "bc", "c"])); // c（单字母词自身即合法）
```

**复杂度**：时间 O(N·L²)，空间 O(N·L)（Set）。

**易错点**：
- 只检查"去掉最后一个字母"的前缀是不够的，必须**每个长度**都检查（`w.slice(0, i)` 从 1 到 L）。
- 单字符单词（如 `"w"`）的前缀就是它自己，`set.has("w")` 为真，合法——不要特判成长度必须 ≥ 2。
- 等长时容易漏掉字典序比较，直接返回了先遇到的；`w < best` 是字符串比较，不要用长度或数值。
- 若用"排序后取第一个"的写法，排序比较器必须是 `a.length - b.length || (a > b ? -1 : 1)` 这种"长度降序 + 字典序升序"，写错就选错。

**变体与追问**：
- 追问"用 Trie 怎么做"：把所有词插入 Trie，再从根 DFS，只走 `isEnd` 为真的路径，记录最深的叶子，天然满足"每个前缀都是单词"。
- 追问"如果允许任意顺序加字母（不要求前缀）"：问题变成"单词链"，要按长度排序后做 DP 或哈希。
- 追问"数据量大时如何优化"：按长度分组 + 记忆化，或 Trie 上一次 DFS 替代 N 次前缀检查，降到 O(总字符数)。

### C-386 并查集模板（路径压缩 + 按秩合并） · 中等 · 字节/阿里/腾讯

**题干**：实现一个并查集（Disjoint Set Union），支持三个操作：`find(x)` 返回元素 `x` 所在集合的**代表元**；`union(a, b)` 合并 `a`、`b` 所在的两个集合，若本来同属一个集合则返回 `false`；`connected(a, b)` 判断两元素是否属于同一集合。另需维护 `count` 表示当前连通分量个数。要求 `find` 与 `union` 的**均摊**时间复杂度为 O(α(n))，α 为反阿克曼函数，可视作常数。

**示例**：
```
const uf = new UnionFind(5);
uf.union(0, 1);            // true
uf.connected(0, 1);        // true
uf.union(1, 2);            // true
uf.count;                  // 3（{0,1,2}、{3}、{4}）
uf.union(0, 2);            // false，已在同一集合
```

**思路**：
- 并查集的本质是**用树表示集合**：每个节点指向父节点，根节点指向自己，根就是集合的代表元。`find` 就是一路向上找根。朴素写法下树可能退化成链，`find` 变 O(n)。
- 优化一 **路径压缩**：`find` 时把沿途节点的父指针直接挂到根上（`parent[x] = find(parent[x])`），树高被压到近似 2，后续查询几乎 O(1)。写成一行递归即可。
- 优化二 **按秩合并**：合并时把"矮树"挂到"高树"下（`rank` 记录树高上界），避免长链。两个优化叠加后，均摊复杂度降到 O(α(n))，这就是"为什么必须两个都写"的标准答案。
- `count` 字段让"连通分量个数"变成 O(1) 读取：初始为 n，每次**成功合并**减 1。很多题（省份数量、岛屿数量 II）的答案直接就是它，这是并查集在笔试里最好用的一点。

**代码**：
```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i); // 初始各自为根
    this.rank = new Array(n).fill(1);                    // 树高上界
    this.count = n;                                      // 连通分量个数
  }
  find(x) {
    // 路径压缩：沿途节点全部直连根，摊还近似 O(1)
    if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
    return this.parent[x];
  }
  union(a, b) {
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;                  // 已连通，合并失败
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra]; // 矮树挂高树
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;    // 等高时树高 +1
    this.count--;                                 // 分量数减一
    return true;
  }
  connected(a, b) { return this.find(a) === this.find(b); }
}
```

**复杂度**：`find`/`union` 均摊 O(α(n))；`connected` O(α(n))；空间 O(n)。

**易错点**：
- **只写路径压缩、不写按秩合并**也能过大部分题，但最坏仍有 O(log n)；反过来只写按秩合并不压缩，链式查询会退化。两者都要有。
- `find` 的递归写法在 n 极大（10⁶+）时可能爆栈，改成迭代 + 两趟（先找根、再压缩）更稳。
- `rank` 是"上界"不是精确高度，所以等高时 `++`、不等时不动，别写成每次合并都 `++`。
- `count` 只能在 `union` **真正合并**时减，`ra === rb` 提前 return 的那个分支不能减。

**变体与追问**：
- 追问"如何支持删除元素"：并查集不支持删除，需要"懒删除"——为每个元素建新节点（版本化），旧节点留在树里作废。
- 追问"如何支持带权并查集"：额外维护 `weight[x]` 表示 x 到根的权值，`find` 时同步累加，用于"等式/倍数关系"的题（如除法求值 399）。
- 追问"并查集 vs DFS/BFS"：静态连通性问题二者等价；但并查集支持**动态加边**，DFS 每次加边都要重跑，这是它的不可替代性。

---

### C-387 省份数量 · 中等 · 腾讯/美团

**题干**：有 `n` 个城市，其中一些彼此相连，另一些没有相连。如果城市 `a` 与城市 `b` 直接相连，且城市 `b` 与城市 `c` 直接相连，那么城市 `a` 与城市 `c` 间接相连。**省份**是一组直接或间接相连的城市，组内不含其他没有相连的城市。给你一个 `n x n` 的矩阵 `isConnected`，其中 `isConnected[i][j] = 1` 表示第 `i` 个城市和第 `j` 个城市直接相连，而 `0` 表示不相连。返回矩阵中**省份的数量**。

**示例**：
```
输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
解释：城市 0 和 1 相连构成一个省份，城市 2 单独构成一个省份
```

**思路**：
- "间接相连"就是**传递闭包**，本质是求无向图的连通分量个数。三种做法：DFS/BFS 染色、并查集、Floyd（不必要）。笔试里最优选是并查集，因为它**代码最短且不需要建邻接表**。
- 矩阵是对称的，只需要遍历**上三角**（`j > i`）：`isConnected[i][j] === 1` 就 `union(i, j)`。下三角重复遍历不会错，但多做一半无用功。
- 答案直接读 `uf.count`：初始化 n 个孤立点，每次成功合并减 1，最后剩下的就是省份数。这就是 `count` 字段存在的意义——不用再扫描统计根的数量。
- 复杂度 O(n²·α(n))，瓶颈在遍历矩阵本身，这已经是最优（必须读完输入）。

**代码**：
```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(1);
    this.count = n;
  }
  find(x) {
    if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
    return this.parent[x];
  }
  union(a, b) {
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
    this.count--;
    return true;
  }
}
function findCircleNum(isConnected) {
  const n = isConnected.length;
  const uf = new UnionFind(n);
  for (let i = 0; i < n; i++)
    for (let j = i + 1; j < n; j++)          // 只扫上三角
      if (isConnected[i][j] === 1) uf.union(i, j);
  return uf.count;                            // 剩余分量数即省份数
}
```

**复杂度**：时间 O(n²·α(n))，空间 O(n)。

**易错点**：
- 自己和自己 `isConnected[i][i]` 恒为 1，若不从 `j = i + 1` 开始，会做大量无效 `union`（虽然 `union` 会返回 false，不影响正确性）。
- 返回 `uf.count` 而不是"根的个数统计"；如果额外写统计逻辑，容易漏掉被压缩后 `parent[x] === x` 的判定条件。
- 矩阵是**对称**的，只处理一半即可；如果只处理 `j > i` 却写成了 `isConnected[j][i]`，逻辑上没错但读起来容易混。
- 输入可能是 `n = 1`，此时答案 1，`count` 初值直接返回即可，不要特判成 0。

**变体与追问**：
- 追问"如果城市是动态加入的"：并查集天然支持，DFS 每次都要重建；这正是并查集的优势场景（对应 C-392 岛屿数量 II）。
- 追问"如何求最大的那个省份"：合并时维护每个根的成员数，取最大值。
- 追问"如果给的是边列表而不是矩阵"：直接遍历边 `union(u, v)`，复杂度降到 O(E·α(n))。

---

### C-388 冗余连接 · 中等 · 字节/阿里

**题干**：树可以看成是一个连通且**无环**的无向图。给定往一棵 `n` 个节点（节点值 1～n）的树中添加一条边后的图，边的两端点为 `1` 到 `n` 之间的整数。该图由一个长度为 `n` 的数组 `edges` 表示，其中 `edges[i] = [ai, bi]` 表示图中节点 `ai` 和 `bi` 之间存在一条边。请找出一条可以删去的边，删除后可使剩余图成为一棵有 `n` 个节点的树。**如果有多个答案，返回数组中最后出现的那个**。

**示例**：
```
输入：edges = [[1,2],[1,3],[2,3]]
输出：[2,3]
解释：删掉 [2,3] 后剩下 1-2、1-3，是一棵树
```

**思路**：
- 一棵有 n 个节点的树恰好有 n−1 条边且无环；现在有 n 条边，说明**恰好多出一条形成环的边**。所以要找的就是"加入时使图首次成环的那条边"。
- 并查集的判定极其优雅：**按顺序遍历每条边，若两端点已经属于同一集合，说明这条边会闭合一个环，它就是答案**。因为题目要求"返回最后出现的"，正序遍历时**最后一条**造成失败的边即为答案——所以不能提前 return，也可以理解为"造成失败的最后一条"。
- 为什么正序遍历能保证"最后出现"？设有多条边都能删，那些边在原图中都处于同一个环上；按顺序加入时，只有**最后加入**的那条才会造成"两端已连通"，前面的加入时还没连通。所以遇到 `union` 返回 false 时的边，就是最后出现的那条。
- 追问"为什么不用拓扑排序"：无向图没法用入度拓扑；DFS 判环也可以，但需要建邻接表 + 记录父节点，代码量是并查集的三倍。

**代码**：
```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(1);
  }
  find(x) {
    if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
    return this.parent[x];
  }
  union(a, b) {                       // 返回 false 表示已连通（会成环）
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
    return true;
  }
}
function findRedundantConnection(edges) {
  const uf = new UnionFind(edges.length + 1); // 节点编号 1..n，多开一位
  for (const [u, v] of edges) {
    if (!uf.union(u, v)) return [u, v];       // 首次合并失败即成环边
  }
  return [];
}
```

**复杂度**：时间 O(n·α(n))，空间 O(n)。

**易错点**：
- 并查集大小要开 `n + 1`（节点是 1-based），开 `n` 会越界。
- 必须**按输入顺序**遍历，顺序变了答案就变了；不要先排序。
- `union` 返回值语义要统一：本实现返回"是否真的合并"，所以 `!union` 就是"成环"。
- 题目保证图是"树 + 一条边"，所以一定能找到答案，不要写多余的分支。

**变体与追问**：
- 追问"如果是**有向图**"：就变成 C-389 冗余连接 II，要额外处理"某个节点入度为 2"的情况，并查集只能处理无向图。
- 追问"如何找出所有可删的边"：先找出环上的所有边，再按输入顺序取最后一条。
- 追问"删掉后是否还连通"：本题条件下删掉环边必然仍连通，不需要额外校验。

---

### C-389 冗余连接 II · 困难 · 阿里/字节

**题干**：在本问题中，**有向图**是指满足以下条件的图：从单一节点出发，每条边都从 `ai` 指向 `bi`。给定的图原本是一棵有根树，但被添加了一条额外的有向边。返回一条可以删去的边，使得剩下的图是**有根树**。如果有多个答案，返回数组中最后出现的那个。

**示例**：
```
输入：edges = [[1,2],[1,3],[2,3]]
输出：[2,3]
输入：edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
输出：[4,1]
```

**思路**：
- 有向图比无向图多了一种破坏方式：**某个节点的入度变成 2**（两个父亲），此时必定有一条边要删；否则（入度全为 1）就是纯**环**，与无向图一样用并查集找环边。
- 第一步：扫描所有边，找入度为 2 的节点 `v`。它的两条入边记作 `cand1`（先出现的）和 `cand2`（后出现的）。
- 第二步（有 `cand2` 时）：**先试着删 `cand2`**，用并查集检查剩下的边是否还能成环。若无环 → 说明 `cand2` 就是多余的那条（它既是后出现的、又不构成环）；若仍有环 → 说明真正的元凶是 `cand1`（`cand2` 是树上的合法边，`cand1` 才是闭合环的那条）。
- 第三步（无入度 2 时）：整张图必然是一个环，直接并查集找**首次合并失败**的边。
- 这三步的顺序就是本题的全部难点：**"有双父亲"和"有环"可能同时出现**，必须用"删掉候选后是否还成环"来区分两种删除方案，这也是它被评为困难的原因。

**代码**：
```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(1);
  }
  find(x) { return this.parent[x] === x ? x : (this.parent[x] = this.find(this.parent[x])); }
  union(a, b) {
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
    return true;
  }
}
function findRedundantDirectedConnection(edges) {
  const n = edges.length;
  const parent = new Array(n + 1).fill(0);      // parent[v] = 指向 v 的节点
  const fromIdx = new Array(n + 1).fill(-1);    // 该入边的下标
  let cand1 = -1, cand2 = -1;
  for (let i = 0; i < n; i++) {
    const [u, v] = edges[i];
    if (parent[v] === 0) { parent[v] = u; fromIdx[v] = i; }
    else { cand1 = fromIdx[v]; cand2 = i; break; } // v 有两个父亲，记下两条入边
  }
  const hasCycle = (skipIdx) => {
    const uf = new UnionFind(n + 1);
    for (let i = 0; i < n; i++) {
      if (i === skipIdx) continue;               // 按下标试删一条候选边
      if (!uf.union(edges[i][0], edges[i][1])) return true; // 仍成环
    }
    return false;
  };
  if (cand2 !== -1) return hasCycle(cand2) ? edges[cand1] : edges[cand2];
  const uf = new UnionFind(n + 1);               // 入度全为 1：纯环
  for (const e of edges) if (!uf.union(e[0], e[1])) return e;
  return [];
}
```

**复杂度**：时间 O(n·α(n))，空间 O(n)。

**易错点**：
- "试删"必须按**下标**跳过（`i === skipIdx`），不能拿 `[u, v]` 新数组去和边列表里的对象比引用，那样永远不相等，`hasCycle` 会恒为真。
- 有入度 2 时，`hasCycle` 为真意味着**环仍然存在**，此时答案必须是 `cand1`——很多人直接返回 `cand2`，这是本题最常见的错误。
- 节点 1-based，并查集开 `n + 1`；`parent` 数组也用 0 表示"没有父亲"，所以节点编号不能从 0 开始。
- 无入度 2 时不要用 `hasCycle`（没有候选边可删），必须直接找环边。

**变体与追问**：
- 追问"为什么不能直接返回最后一条入边"：如果那条边在树上（不构成环），删掉会破坏连通性，得到的不是有根树。
- 追问"如何验证删完确实是树"：n 个节点 n−1 条边 + 无环 + 恰有一个入度为 0 的根，三条同时满足。
- 追问"如果是无向图"：退化成 C-388，不需要入度判断。

---

### C-390 等式方程的可满足性 · 中等 · 字节/腾讯

**题干**：给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 `equations[i]` 的长度为 4，并采用两种不同的形式之一：`"a==b"` 或 `"a!=b"`。在这里，`a` 和 `b` 是小写字母（不一定不同），表示单字母变量名。只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 `true`，否则返回 `false`。

**示例**：
```
输入：["a==b","b!=a"]
输出：false
解释：若 a == b，则不可能 a != b
输入：["b==a","a==b"]
输出：true
```

**思路**：
- `==` 具有**传递性**（a==b、b==c 推出 a==c），这正是**等价关系**，也正是并查集的适用条件。把每个变量看作一个节点，`==` 就是"合并两个集合"。
- 关键在**处理顺序**：必须**先处理所有 `==`，把所有等价类合并完**，再回来检查所有 `!=`。如果一边遍历一边判断 `!=`，此时等价类还没建全，会漏判（例如先遇到 `a!=c`，后遇到 `a==b`、`b==c`）。
- 变量只有 26 个小写字母，并查集大小固定为 26，`charCodeAt(0) - 97` 做映射即可，不需要哈希表。
- 校验阶段：对每条 `!=`，若两端 `find` 相同，说明被 `==` 强制相等了，直接返回 false；全部通过则 true。复杂度 O(n·α(26))，实际是 O(n)。

**代码**：
```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(1);
  }
  find(x) { return this.parent[x] === x ? x : (this.parent[x] = this.find(this.parent[x])); }
  union(a, b) {
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
    return true;
  }
}
function equationsPossible(equations) {
  const uf = new UnionFind(26);
  const id = (ch) => ch.charCodeAt(0) - 97;   // 'a' -> 0
  for (const eq of equations) {
    if (eq[1] === '=') uf.union(id(eq[0]), id(eq[3])); // 第一轮：只合并相等
  }
  for (const eq of equations) {
    if (eq[1] === '!' && uf.find(id(eq[0])) === uf.find(id(eq[3]))) return false;
  }
  return true;
}
```

**复杂度**：时间 O(n·α(26)) ≈ O(n)，空间 O(26)。

**易错点**：
- **必须两轮**：先合并全部 `==`，再校验 `!=`；一轮遍历是本题最经典的错误。
- 方程格式固定为 `"a==b"` / `"a!=b"`，操作符在**下标 1**，变量在下标 0 和 3；用 `eq[2]` 判断会错。
- `"a!=a"` 一定无解（同一变量不可能不等于自己），逻辑上会被 `find` 相同捕获，但如果 `a` 从未出现在 `==` 中也要判出来。
- 变量可能是同一个字母，`union(a, a)` 返回 false 是正常的，不影响结果。

**变体与追问**：
- 追问"如果关系是 `a > b` 这种偏序"：等价关系用并查集，偏序要用**拓扑排序**，两者不能混。
- 追问"如何输出一组可行解"：给每个等价类分配一个编号作为变量值，`!=` 的类之间编号必须不同，需要图着色。
- 追问"如果变量是字符串而非单字母"：并查集下标改成哈希表映射，`Map<string, string>` 实现动态并查集。

### C-391 账户合并 · 中等 · 字节/阿里

**题干**：给定一个列表 `accounts`，每个元素 `accounts[i]` 是一个字符串数组，第一个元素是账户**名称**，其余元素是**邮箱**。现在我们需要合并这些账户。两个账户如果有**任何共同邮箱**，那么它们必定属于同一个人（即使名称不同）。合并后的账户名称可以是任意一个被合并账户的名称，邮箱需按**字典序升序**排列。返回合并后的账户列表，顺序不限。

**示例**：
```
输入：accounts = [["John","johnsmith@mail.com","john00@mail.com"],
                 ["John","johnnybravo@mail.com"],
                 ["John","johnsmith@mail.com","john_newyork@mail.com"],
                 ["Mary","mary@mail.com"]]
输出：[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
      ["John","johnnybravo@mail.com"],["Mary","mary@mail.com"]]
```

**思路**：
- 问题的本质是**对邮箱做连通分量划分**：同一个账户里的邮箱互相连通，不同账户通过相同邮箱连通。合并完成后，同一个连通分量里的所有邮箱属于同一个人。这就是并查集的教科书场景。
- 难点是"并查集的元素是什么"。**必须给每个邮箱编号**（而不是给账户编号），因为合并的触发条件是"同一个邮箱出现在两个账户里"。所以先做一次全量扫描建 `email -> id` 映射，id 从 0 连续递增。
- 建图：对每个账户，把它的**第一个邮箱**作为锚点，与其余邮箱逐个 `union`。用第一个邮箱连所有其他邮箱，等价于把这些邮箱两两连通，但只需 O(k) 次合并而不是 O(k²)。
- 输出阶段：`根 id -> [邮箱列表]`，再按根把邮箱排序、拼上名字。名字取该组**任意一个**邮箱对应的账户名即可（同组必然同名，因为题目保证同一人的账户名一致；若不一致取任意一个）。
- **为什么不用哈希表暴力合并**：每次合并要把两个集合的邮箱列表做并集，反复合并会退化成 O(n²)；并查集把"合并"变成指针操作，最后统一归组，复杂度线性。

**代码**：
```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(1);
  }
  find(x) { return this.parent[x] === x ? x : (this.parent[x] = this.find(this.parent[x])); }
  union(a, b) {
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
    return true;
  }
}
function accountsMerge(accounts) {
  const emailToId = new Map(), emailToName = new Map();
  let id = 0;
  for (const acc of accounts) {
    for (let i = 1; i < acc.length; i++) {          // 给每个邮箱编号
      if (!emailToId.has(acc[i])) emailToId.set(acc[i], id++);
      emailToName.set(acc[i], acc[0]);
    }
  }
  const uf = new UnionFind(id);
  for (const acc of accounts) {
    const first = emailToId.get(acc[1]);            // 用第一个邮箱当锚点
    for (let i = 2; i < acc.length; i++) uf.union(first, emailToId.get(acc[i]));
  }
  const groups = new Map();                         // 根 id -> 邮箱列表
  for (const [email, eid] of emailToId) {
    const root = uf.find(eid);
    if (!groups.has(root)) groups.set(root, []);
    groups.get(root).push(email);
  }
  const res = [];
  for (const list of groups.values()) {
    list.sort();                                    // 组内字典序
    res.push([emailToName.get(list[0]), ...list]);   // 名字 + 排序后的邮箱
  }
  return res;
}
```

**复杂度**：时间 O(E·α(E) + E log E)（E 为邮箱总数，排序占主导）；空间 O(E)。

**易错点**：
- 并查集元素必须是**邮箱**，不是账户下标；用账户下标会让"跨账户的同一邮箱"无处安放。
- 每个账户的名字只挂在邮箱上（`emailToName`），输出时用组内任一邮箱反查，不要用"根 id 直接取名字"（根 id 没有名字）。
- 输出顺序是"名字 + 邮箱"，**名字只出现一次**，不要把名字也塞进排序列表。
- 账户可能只有一个邮箱（没有可 union 的对象），要保证它自己也能成组——靠后面统一按 `find` 归组即可，不需要特判。

**变体与追问**：
- 追问"如果同一邮箱对应不同名字"：说明数据冲突，需要额外策略（取出现次数最多的名字 / 报错）。
- 追问"如何输出合并前后的变更明细"：在 union 时记录日志，或做两轮快照对比。
- 工程映射：用户身份归一（ID-Mapping），一个用户多个设备 ID/手机号/邮箱的打通。

---

### C-392 岛屿数量 II · 困难 · 阿里/字节

**题干**：给你一个大小为 `m x n` 的二进制网格 `grid`。网格表示**水域**和**陆地**，其中 `1` 表示陆地，`0` 表示水域。初始时网格全为水域。另给你一个数组 `positions`，其中 `positions[i] = [ri, ci]` 表示第 `i` 次操作在 `(ri, ci)` 位置**填海造陆**。请你返回每次操作后网格中**岛屿的数量**。岛屿总是被水域包围，并且每座岛屿只能由水平或垂直方向上相邻的陆地连接形成。

**示例**：
```
输入：m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
输出：[1,1,2,3]
解释：第 1 次造陆后 1 座岛；第 2 次后两格相连仍是 1 座；
     第 3 次独立成岛变 2；第 4 次独立成岛变 3
```

**思路**：
- 静态版"岛屿数量"用 DFS 染色，但本题是**动态加陆**：每加一格就要重算，DFS 会退化成 O(k·m·n)，k 次操作直接超时。
- 动态连通性的唯一正解是**并查集**：把每个格子编成 `r * n + c`，每填一格就看它的上下左右是否已经是陆地，是就 `union`。
- 关键在计数规则：**填一格先 `count++`（新岛）**，然后每**成功合并**一次相邻的岛，就 `count--`（两岛变一岛）。最终 `count` 就是当前岛屿数。这个"加一减一"的记账方式必须在答题时讲清楚，否则面试官会怀疑你是蒙的。
- 需要一个 `seen` 数组记录"哪些格子已经变成陆地"，因为并查集本身不存状态；同一位置重复填海要忽略（题目说不会重复，但防御性判断是加分项）。

**代码**：
```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(1);
    this.count = n;
  }
  find(x) { return this.parent[x] === x ? x : (this.parent[x] = this.find(this.parent[x])); }
  union(a, b) {
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
    return true;
  }
}
function numIslands2(m, n, positions) {
  const uf = new UnionFind(m * n);
  const land = new Array(m * n).fill(false);
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  const res = [];
  let count = 0;
  for (const [r, c] of positions) {
    const id = r * n + c;
    if (land[id]) { res.push(count); continue; }  // 重复填海：数量不变
    land[id] = true; count++;                     // 新格子先算作一座新岛
    for (const [dr, dc] of dirs) {
      const nr = r + dr, nc = c + dc;
      if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
      if (land[nr * n + nc] && uf.union(id, nr * n + nc)) count--; // 合并成功才减
    }
    res.push(count);
  }
  return res;
}
```

**复杂度**：时间 O(k·α(mn))，k 为操作次数；空间 O(mn)。

**易错点**：
- 减计数的条件是 `union` **返回 true**（真的合并了两个不同集合），写成 `if (land[邻居]) count--` 会把"同一个岛的两条边"重复减。
- 先 `count++` 再遍历四邻；顺序反了会让"自己和自己"的合并逻辑混乱。
- 格子映射是 `r * n + c`，**乘的是列数 n**，写反成 `r * m + c` 在非方阵时直接错乱。
- 重复填海（若出现）必须直接沿用旧答案，不能重复 `count++`。

**变体与追问**：
- 追问"如果还能**填水**（把陆地变回水）"：并查集不支持删除，要用"倒序处理"——从最终状态倒着删，删除变添加。
- 追问"如何求最大岛屿面积"：根上维护成员数，合并时相加，取最大值。
- 追问"网格很大但造陆很少"：用坐标哈希代替 `m*n` 数组，只给出现过的格子分配 id。

---

### C-393 移除最多的同行或同列石头 · 中等 · 腾讯/美团

**题干**：`n` 块石头放置在二维平面中的一些整数坐标点上，每个坐标点上**最多只能有一块**石头。如果一块石头的**同行或同列**中有其他石头存在，那么就可以移除这块石头。给你一个长度为 `n` 的数组 `stones`，其中 `stones[i] = [xi, yi]` 表示第 `i` 块石头的位置。返回可以移除石头的**最大数量**。

**示例**：
```
输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
输出：5
解释：可以移除 5 块，最后剩下 1 块
输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
输出：3
```

**思路**：
- 题意转译：同一行或同一列的石头之间可以"连锁移除"。**把"行"和"列"都当作图的节点**，每块石头就是一条连接"第 x 行"和"第 y 列"的边。这样一个连通分量内的所有石头最终只能剩下 1 块（删到最后必剩一个无法再删的孤立点）。
- 于是答案 = `石头总数 − 连通分量个数`。这是本题最漂亮的一步转化：**问题从"坐标"变成了"行/列编号的连通性"**，并查集直接可用。
- 编号技巧：行和列必须**分开编号**，否则"第 0 行"和"第 0 列"会被误认为同一个节点。常用做法是 `union(x, y + OFFSET)`，`OFFSET` 取 `10001`（坐标上限 10⁴）。
- 为什么这样建模能保证"最多"：每个连通分量是一棵"二分图生成树"式的结构，边数 = 点数 − 1 时可全删到只剩 1；边更多时也只需保留 1 块作为"根"，所以最大移除数恰好是 `边数 − 分量数`。

**代码**：
```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(1);
  }
  find(x) { return this.parent[x] === x ? x : (this.parent[x] = this.find(this.parent[x])); }
  union(a, b) {
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
    return true;
  }
}
function removeStones(stones) {
  const OFFSET = 10001;                    // 列编号整体右移，避免与行号撞车
  const uf = new UnionFind(20010);
  const nodes = new Set();                 // 只统计真正出现过的行/列
  for (const [x, y] of stones) {
    uf.union(x, y + OFFSET);               // 石头 = 行节点与列节点之间的一条边
    nodes.add(x); nodes.add(y + OFFSET);
  }
  const roots = new Set();
  for (const node of nodes) roots.add(uf.find(node));
  return stones.length - roots.size;       // 每个分量留 1 块，其余可删
}
```

**复杂度**：时间 O(n·α(n))，空间 O(n + 坐标范围)。

**易错点**：
- **行和列不加偏移**会让 `union(0, 0)` 变成自己连自己，第 0 行与第 0 列被错误合并。
- 连通分量个数要基于**出现过的节点集合**统计，不能对整个 `parent` 数组求根数目（未出现的行/列会各算一个分量）。
- 返回的是"可移除数量"而不是"剩余数量"，别把 `roots.size` 直接返回。
- 数组开多大取决于坐标上限，题目坐标 ≤ 10⁴，所以 `20010` 够用；若坐标范围不定，用哈希表动态分配 id。

**变体与追问**：
- 追问"如果石头可以斜着连"：图的边定义变了，但仍可用并查集，只是每块石头要连的节点更多。
- 追问"求最后剩下的石头坐标"：每个分量任选一块即可，但"任意"不代表唯一，题目通常只问数量。
- 工程映射：社交网络里的"共同群组"合并、图像连通区域标记（union-find 的经典工业应用）。

---

### C-394 按公因数计算最大组件大小 · 困难 · 字节/阿里

**题干**：给定一个由不同正整数的组成的数组 `nums`，考虑下面的图：有 `nums.length` 个节点，按从 `nums[0]` 到 `nums[nums.length - 1]` 标记；只有当 `nums[i]` 和 `nums[j]` **共用一个大于 1 的公因数**时，节点 `i` 和 `j` 之间才有一条边。返回图中**最大连通组件**的大小。

**示例**：
```
输入：nums = [4,6,15,35]
输出：4
解释：4-6（公因数 2）、6-15（公因数 3）、15-35（公因数 5）连成一片
输入：nums = [20,50,9,63]
输出：2
```

**思路**：
- 暴力两两求 gcd 建图是 O(n² log V)，n = 2×10⁴ 时可以过，但面试官显然想听更优解。
- 关键洞察：两个数有公因数，当且仅当它们**共享至少一个质因子**。所以不必两两连边，而是**把"质因子"也当作图节点**：每个数向它的每个质因子连一条边。这样边数是 O(n log V)，而连通性与原图完全等价。
- 于是并查集的大小取 `max(nums) + 1`：下标既表示数值本身，也表示质因子。对每个 `x`，先质因数分解，再 `union(x, p)`。
- 质因数分解必须用**线性筛 / 埃氏筛预处理最小质因数（SPF）**，否则每个数试除到 √x，总体是 O(n√V)，10⁴ × 10⁴ 会超时。筛法代价 O(V log log V)，之后每个数分解是 O(log x)。
- 最后统计每个根的成员数，注意**只统计 `nums` 里的数**（质因子节点不算组件大小），取最大值。

**代码**：
```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(1);
  }
  find(x) { return this.parent[x] === x ? x : (this.parent[x] = this.find(this.parent[x])); }
  union(a, b) {
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
    return true;
  }
}
function largestComponentSize(nums) {
  const max = Math.max(...nums);
  const spf = Array.from({ length: max + 1 }, (_, i) => i); // 最小质因数筛
  for (let i = 2; i * i <= max; i++) {
    if (spf[i] === i) {
      for (let j = i * i; j <= max; j += i) if (spf[j] === j) spf[j] = i;
    }
  }
  const uf = new UnionFind(max + 1);
  for (const x of nums) {
    let v = x;
    while (v > 1) {
      const p = spf[v];
      uf.union(x, p);              // 数值与它的质因子连边
      while (v % p === 0) v /= p;  // 去掉这个质因子的所有幂
    }
  }
  const size = new Map();          // 根 -> 组件内 nums 元素个数
  let best = 1;
  for (const x of nums) {
    const root = uf.find(x);
    const cur = (size.get(root) || 0) + 1;
    size.set(root, cur);
    best = Math.max(best, cur);
  }
  return best;
}
```

**复杂度**：筛法 O(V log log V)，建图 O(n log V)，统计 O(n)；空间 O(V)，V = max(nums)。

**易错点**：
- 统计组件大小时**只能数 `nums` 中的元素**，把质因子节点也数进去会得到错误的（偏大的）结果。
- 分解时去掉质因子的所有幂（`while (v % p === 0) v /= p`），否则会重复 union 同一个质因子。
- `spf[1] = 1`，`while (v > 1)` 保证 1 不会被当成质因子。
- `nums` 元素互不相同，所以不需要去重；但重复元素也不影响正确性（union 返回 false）。

**变体与追问**：
- 追问"不用筛法行不行"：可以，每个数试除到 √x 也能过 10⁴ 的数据，但复杂度差一个量级，答题时应提筛法。
- 追问"如果要求输出每个组的具体数字"：按根归组即可，和 C-391 的输出方式一致。
- 追问"gcd 建图 vs 质因子建图"：前者 O(n²)，后者 O(n log V)，且后者揭示了"连通性由质因子传递"的本质。

---

### C-395 相似字符串组 · 困难 · 阿里/字节

**题干**：如果交换字符串 `X` 中的两个不同位置的字母，使得它和字符串 `Y` 相等，那么称 `X` 和 `Y` 两个字符串**相似**。如果两个字符串本身相等也可以认为是相似的（不需要交换）。给你一个字符串数组 `strs`，其中每个字符串都是其他字符串的**字母异位词**（即长度相同、字符多重集相同）。返回 `strs` 中**相似字符串组**的数目。

**示例**：
```
输入：strs = ["tars","rats","arts","star"]
输出：2
解释：{"tars","rats","arts"} 互相相似，{"star"} 单独一组
输入：strs = ["omv","ovm"]
输出：1
```

**思路**：
- 相似关系具有**传递性**（题目保证所有字符串互为字母异位词，所以"恰好 2 处不同"这个关系在异位词条件下是可传递的），因此可以用并查集把相似的点合并成组，答案就是连通分量数。
- 判断两个字符串是否相似：逐位比较，统计不同位置的数量；**不同处超过 2 个就可以提前返回 false**。注意"相似"的定义是"交换两个字母后相等"，对于字母异位词，这等价于**恰好 0 处或恰好 2 处不同**（1 处不同不可能，因为字符多重集相同）。
- 朴素做法是 O(n²·L) 两两比较，n = 300 时完全够用。笔试写这个版本即可，但要能说出"这是最优吗"——本质上需要在 O(n²) 个点对里判断，除非做哈希分组优化。
- 优化方向：把每个字符串的**字符计数向量**作为 key 分组（异位词必然同组），组内再两两比较；或用"删除一个字符后的签名"做哈希加速。但注意不能只靠排序后的字符串判断相似，因为 `"tars"` 和 `"rats"` 排序后都是 `"arst"`，无法区分相似与不相似。

**代码**：
```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(1);
    this.count = n;
  }
  find(x) { return this.parent[x] === x ? x : (this.parent[x] = this.find(this.parent[x])); }
  union(a, b) {
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
    this.count--;
    return true;
  }
}
function numSimilarGroups(strs) {
  const n = strs.length;
  const uf = new UnionFind(n);
  const similar = (a, b) => {
    let diff = 0;
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i] && ++diff > 2) return false; // 超过 2 处直接否
    }
    return true;                                      // 0 处或 2 处不同
  };
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      // 已同组就不必再比，省一次 O(L)
      if (uf.find(i) !== uf.find(j) && similar(strs[i], strs[j])) uf.union(i, j);
    }
  }
  return uf.count;
}
```

**复杂度**：时间 O(n²·L)，空间 O(n)。

**易错点**：
- "相似"允许**完全相同**（0 处不同），所以 `similar` 在 `diff === 0` 时返回 true，不能要求必须恰好 2 处。
- 用 `++diff > 2` 提前退出，若写成 `diff++ > 2` 会在 `diff` 已经是 2 时继续累加，逻辑上多跑一轮但结果不变；写成 `diff > 2` 后置判断更容易读。
- 必须有"已同组就跳过"的剪枝，否则同一个组内的点对被反复比较，虽不影响正确性但浪费。
- 字符串长度相同是前提（互为异位词），若输入不满足，`similar` 的下标会越界。

**变体与追问**：
- 追问"如何更快"：按"删除第 k 个字符后的剩余串"做哈希，相似的两个串必然在某个 k 上哈希相同，可把候选对从 O(n²) 降到接近 O(n)。
- 追问"如果不保证是异位词"：相似关系不再可传递，答案不能简单用并查集求分量，需要求最大团（NP-hard），这是本题"保证异位词"这一条件的价值。
- 追问"如何输出每组的具体内容"：按根归组，和 C-391 一致。
### C-396 线段树模板（区间加 + 区间求和 · 懒标记） · 中等 · 字节/阿里

**题干**：给定一个长度为 `n` 的整数数组 `nums`，要求支持两种操作：`update(l, r, val)` 把下标区间 `[l, r]` 内的所有元素**同时加上** `val`；`query(l, r)` 返回下标区间 `[l, r]` 内所有元素的**和**。两种操作各调用 m 次，要求单次操作 O(log n)。数组下标从 0 开始。

**示例**：
```
const st = new SegmentTree([1, 2, 3, 4, 5]);
st.query(0, 4);      // 15
st.update(1, 3, 10); // 下标 1~3 各加 10 => [1,12,13,14,5]
st.query(1, 3);      // 39
st.query(0, 0);      // 1
```

**思路**：
- "区间修改 + 区间查询"如果每次暴力改，单次 O(n)，m 次就是 O(nm)。线段树把区间切成 O(log n) 个树节点，每个节点维护该区间的聚合值（这里是和），于是两种操作都降到 O(log n)。
- **树用数组存**：下标 `node` 的左右孩子是 `2*node` 和 `2*node+1`，`node` 覆盖区间 `[l, r]`，`mid = (l+r)>>1`。数组开 `4n` 一定够（满二叉树性质），这是最容易记错的常数。
- **懒标记（lazy）是本题唯一难点**：区间整体加时，不可能也不必要把区间内每个叶子都改一遍。做法是"在完全覆盖的节点上打标记 + 立刻更新该节点的 `tree` 值"，**把下推推迟到真正需要访问子节点时**。
- **下推时机只有一处：进入部分覆盖的分支之前**。`_pushDown` 把父亲的 `lazy` 分给两个孩子，并按"孩子区间长度 × lazy"更新孩子的 `tree` 值，然后清空父亲的标记。忘记下推或下推太晚，查询就会拿到旧值——这是线段树 bug 的第一来源。
- 为什么 `tree[node] += lazy * (r - l + 1)`：懒标记代表"这个区间每个元素都加了 `lazy`"，所以区间和增加 `lazy × 元素个数`。这一步的乘数是易错核心。

**代码**：
```javascript
class SegmentTree {
  constructor(nums) {
    this.n = nums.length;
    this.tree = new Array(4 * this.n).fill(0); // 区间和
    this.lazy = new Array(4 * this.n).fill(0); // 待下推的加法标记
    this._build(1, 0, this.n - 1, nums);
  }
  _build(node, l, r, nums) {
    if (l === r) { this.tree[node] = nums[l]; return; }
    const mid = (l + r) >> 1;
    this._build(node * 2, l, mid, nums);
    this._build(node * 2 + 1, mid + 1, r, nums);
    this.tree[node] = this.tree[node * 2] + this.tree[node * 2 + 1];
  }
  _pushDown(node, l, r) {                 // 只在"部分覆盖"前调用
    if (this.lazy[node] === 0) return;
    const mid = (l + r) >> 1, L = node * 2, R = L + 1, v = this.lazy[node];
    this.tree[L] += v * (mid - l + 1);    // 左孩子区间长度
    this.lazy[L] += v;
    this.tree[R] += v * (r - mid);        // 右孩子区间长度
    this.lazy[R] += v;
    this.lazy[node] = 0;                  // 标记已下推，清空
  }
  update(ql, qr, val) { this._update(1, 0, this.n - 1, ql, qr, val); }
  _update(node, l, r, ql, qr, val) {
    if (ql <= l && r <= qr) {             // 完全覆盖：打标记即返回
      this.tree[node] += val * (r - l + 1);
      this.lazy[node] += val;
      return;
    }
    this._pushDown(node, l, r);           // 必须在下钻前下推
    const mid = (l + r) >> 1;
    if (ql <= mid) this._update(node * 2, l, mid, ql, qr, val);
    if (qr > mid) this._update(node * 2 + 1, mid + 1, r, ql, qr, val);
    this.tree[node] = this.tree[node * 2] + this.tree[node * 2 + 1];
  }
  query(ql, qr) { return this._query(1, 0, this.n - 1, ql, qr); }
  _query(node, l, r, ql, qr) {
    if (ql <= l && r <= qr) return this.tree[node];
    this._pushDown(node, l, r);           // 查询同样要下推，否则值不新
    const mid = (l + r) >> 1;
    let sum = 0;
    if (ql <= mid) sum += this._query(node * 2, l, mid, ql, qr);
    if (qr > mid) sum += this._query(node * 2 + 1, mid + 1, r, ql, qr);
    return sum;
  }
}
```

**复杂度**：建树 O(n)；`update`/`query` O(log n)；空间 O(n)。

**易错点**：
- **查询也要下推**，很多人只在 `update` 里写了 `_pushDown`，导致查询区间只覆盖了部分子节点时读到未更新的值。
- `tree` 数组必须开 `4 * n`，开 `2 * n` 在非满二叉树时会越界（`undefined + 数字 = NaN`）。
- 下推时孩子区间的长度分别是 `mid - l + 1` 和 `r - mid`，写反或用同一个长度，长区间求和必错。
- 完全覆盖的判定是 `ql <= l && r <= qr`，写成 `l <= ql && qr <= r` 就把条件方向搞反了。

**变体与追问**：
- 追问"区间赋值（不是加）怎么办"：懒标记改成"赋值标记 + 是否有标记"的布尔位，下推时直接覆盖孩子的值。
- 追问"区间加 + 区间求最大值"：`tree` 存 `max`，下推时孩子 `max += lazy`（不加长度乘数），说明"乘长度"只适用于求和类聚合。
- 追问"动态开点"：值域很大（如 10⁹）时不能开 `4n` 数组，改成按需创建节点（`left/right` 用 Map 或对象），空间 O(m log V)。

---

### C-397 树状数组模板（Fenwick Tree） · 中等 · 阿里/腾讯

**题干**：实现一个树状数组（Binary Indexed Tree），支持：`add(i, delta)` 把第 `i` 个元素（**1-based**）增加 `delta`；`prefixSum(i)` 返回前 `i` 个元素之和；`rangeSum(l, r)` 返回区间 `[l, r]` 的元素之和。三个操作都要求 O(log n)，空间 O(n)。

**示例**：
```
const fw = new Fenwick([1, 3, 5, 7, 9]);
fw.prefixSum(3);    // 1+3+5 = 9
fw.rangeSum(2, 4);  // 3+5+7 = 15
fw.add(2, 10);      // 第 2 个元素 3 -> 13
fw.prefixSum(3);    // 1+13+5 = 19
```

**思路**：
- 线段树能做的事树状数组大多能做，但**代码量只有三分之一**、常数更小，代价是只支持"可减"的聚合（和、异或），不支持最大值。
- 核心是 `lowbit(i) = i & (-i)`，它取出 `i` 的二进制最低位的 1。`tree[i]` 维护的是"以 `i` 结尾、长度为 `lowbit(i)` 的区间和"，这就是树状数组"树"的形状来源。
- 两个方向的操作互为镜像：**更新往上传**（`i += lowbit(i)`），**查询往下跳**（`i -= lowbit(i)`）。记住这两行，模板就不会忘。
- 建树可以直接 O(n)：先把 `nums` 拷进 `tree`（1-based），再对每个 `i` 把 `tree[i]` 加到 `tree[i + lowbit(i)]` 上。比逐个 `add` 的 O(n log n) 更快，也更能体现你懂 `lowbit` 的含义。
- 区间和用**前缀和相减**：`rangeSum(l, r) = prefixSum(r) - prefixSum(l - 1)`。这就是"可减性"的体现，也是它不能求最大值的原因。

**代码**：
```javascript
class Fenwick {
  constructor(nums) {
    this.n = nums.length;
    this.tree = new Array(this.n + 1).fill(0);   // 1-based
    for (let i = 1; i <= this.n; i++) {
      this.tree[i] += nums[i - 1];
      const j = i + (i & -i);                    // O(n) 建树：把贡献推给父节点
      if (j <= this.n) this.tree[j] += this.tree[i];
    }
  }
  add(i, delta) {
    for (; i <= this.n; i += i & -i) this.tree[i] += delta; // 向上更新所有祖先
  }
  prefixSum(i) {
    let sum = 0;
    for (; i > 0; i -= i & -i) sum += this.tree[i];         // 向下跳，拼出前缀
    return sum;
  }
  rangeSum(l, r) { return this.prefixSum(r) - this.prefixSum(l - 1); }
}
```

**复杂度**：建树 O(n)；`add`/`prefixSum`/`rangeSum` O(log n)；空间 O(n)。

**易错点**：
- 树状数组是 **1-based**，`add(0, x)` 会死循环（`0 & -0 === 0`，`i += 0` 永远不动），这是最经典的死循环 bug。
- `rangeSum(l, r)` 里是 `prefixSum(l - 1)`，少了减 1 会把 `l` 也算进去。
- `lowbit` 用 `i & -i`，JS 的位运算是 32 位有符号的，`n` 超过 2³¹ 会溢出；一般题目不会这么大，但要知道。
- O(n) 建树时 `tree[i] += nums[i-1]` 用的是 `+=` 而不是 `=`，因为此时 `tree[i]` 可能已被更小的节点累加过。

**变体与追问**：
- 追问"为什么树状数组不能求区间最大值"：最大值不可减，`max(l, r) ≠ max(0, r) - max(0, l-1)`。求最值只能用线段树或 ST 表。
- 追问"如何支持区间加、单点查"：用**差分**——`add(l, v)`、`add(r+1, -v)`，单点查就是 `prefixSum(i)`。
- 追问"如何支持区间加、区间和"：维护两个树状数组（分别存 `d[i]` 和 `i*d[i]`），是树状数组的高阶用法。

---

### C-398 区域和检索 · 数组可修改 · 中等 · 字节/美团

**题干**：给你一个数组 `nums`，请你完成两类查询：其中一类查询要求**更新**数组 `nums` 对应的下标处的值；另一类查询要求返回数组 `nums` 中索引 `left` 和索引 `right` 之间的子数组的**和**，包含 `left` 和 `right` 两端点。实现 `NumArray` 类：`NumArray(int[] nums)` 初始化；`void update(int index, int val)` 将 `nums[index]` 更新为 `val`；`int sumRange(int left, int right)` 返回区间和。

**示例**：
```
NumArray a = new NumArray([1, 3, 5]);
a.sumRange(0, 2);   // 9
a.update(1, 2);     // [1,2,5]
a.sumRange(1, 2);   // 7
```

**思路**：
- 如果只有查询，**前缀和**就能 O(1) 出答案；但一旦有 `update`，前缀和数组后续所有元素都要改，O(n)。反过来，用裸数组查询是 O(n)。两种朴素结构各占一头，这正是需要树状数组的场景。
- 树状数组给"单点修改"和"前缀和查询"都做到 O(log n)，而区间和 = 两个前缀和相减，所以三种操作都是 O(log n)。**这就是本题的结构选型理由**：修改与查询的频率相当、且聚合可减。
- `update` 要算**增量** `val - nums[index]` 再 `add`，不能直接把 `tree` 里的值改成 `val`——树状数组存的是区间和，不是单点值。更新完记得同步 `nums[index]`，否则下一次 `update` 的增量会算错。
- 下标转换是本题唯一的"工程细节"：`nums` 是 0-based、树状数组是 1-based，`index + 1` 和 `right + 1` 两个 `+1` 不能漏。

**代码**：
```javascript
class NumArray {
  constructor(nums) {
    this.nums = nums.slice();
    this.n = nums.length;
    this.tree = new Array(this.n + 1).fill(0);
    for (let i = 1; i <= this.n; i++) {
      this.tree[i] += nums[i - 1];
      const j = i + (i & -i);
      if (j <= this.n) this.tree[j] += this.tree[i];  // O(n) 建树
    }
  }
  _add(i, delta) {
    for (; i <= this.n; i += i & -i) this.tree[i] += delta;
  }
  _prefix(i) {
    let sum = 0;
    for (; i > 0; i -= i & -i) sum += this.tree[i];
    return sum;
  }
  update(index, val) {
    this._add(index + 1, val - this.nums[index]); // 只能加增量
    this.nums[index] = val;                       // 同步原数组
  }
  sumRange(left, right) {
    return this._prefix(right + 1) - this._prefix(left);
  }
}
```

**复杂度**：初始化 O(n)；`update`/`sumRange` O(log n)；空间 O(n)。

**易错点**：
- `update` 直接用 `_add(index + 1, val)` 是错的，等于在原值上又加了一次；必须是**差值**。
- 忘记同步 `this.nums[index] = val`，第二次 `update` 同一个位置时增量算错。
- `sumRange` 的右端是 `right + 1`、左端是 `left`（不是 `left + 1`），因为要算 `[left, right]` 对应 1-based 的 `[left+1, right+1]`，相减后是 `prefix(right+1) - prefix(left)`。
- `constructor` 里 `this.nums = nums` 直接引用会让外部修改数组时内部状态不一致，要 `slice()` 拷贝。

**变体与追问**：
- 追问"如果还要区间加"：改成两个树状数组（差分 + 加权差分），或直接上带懒标记的线段树。
- 追问"如果还要区间最大值"：树状数组做不到，必须用线段树（C-399）。
- 追问"数据量 10⁵、操作 10⁵，两种方案谁快"：树状数组常数更小，实测比线段树快 2～3 倍。

---

### C-399 维护区间最大值的线段树（单点修改 + 区间查询） · 中等 · 阿里/字节

**题干**：实现一个数据结构，支持对一个长度为 `n` 的整数数组做两种操作：`update(pos, val)` 把下标 `pos` 的值修改为 `val`；`query(l, r)` 返回下标区间 `[l, r]` 内的**最大值**。单次操作要求 O(log n)。

**示例**：
```
const st = new MaxSegmentTree([5, 1, 9, 3, 7]);
st.query(0, 4);   // 9
st.query(1, 3);   // 9
st.update(2, 2);  // [5,1,2,3,7]
st.query(0, 4);   // 7
st.query(0, 1);   // 5
```

**思路**：
- 结构骨架与 C-396 完全一致，唯一区别是**聚合函数从"和"换成"max"**，因此**不需要懒标记**——单点修改只会影响一条从根到叶的路径，沿途重算 `max` 即可。
- 这正说明"要不要懒标记"取决于**修改的粒度**：区间修改才需要懒标记把"整段一起改"的操作推迟；单点修改只要一路回溯更新，O(log n) 自然满足。
- 查询用**区间不相交就返回单位元**的写法：`-Infinity` 是 max 的单位元（`max(-Infinity, x) === x`）。这和求和的单位元 `0` 是同一个套路，必须理解"为什么需要单位元"——因为递归会走到与查询区间无关的分支，需要一个"不影响结果"的返回值。
- 也可以写成"如果完全覆盖就返回，否则只往有交集的一侧递归"，省掉单位元判断，但边界条件更多，容易漏 `ql > r || qr < l` 的剪枝。

**代码**：
```javascript
class MaxSegmentTree {
  constructor(nums) {
    this.n = nums.length;
    this.tree = new Array(4 * this.n).fill(-Infinity); // 单位元：不影响 max
    this._build(1, 0, this.n - 1, nums);
  }
  _build(node, l, r, nums) {
    if (l === r) { this.tree[node] = nums[l]; return; }
    const mid = (l + r) >> 1;
    this._build(node * 2, l, mid, nums);
    this._build(node * 2 + 1, mid + 1, r, nums);
    this.tree[node] = Math.max(this.tree[node * 2], this.tree[node * 2 + 1]);
  }
  update(pos, val) { this._update(1, 0, this.n - 1, pos, val); }
  _update(node, l, r, pos, val) {
    if (l === r) { this.tree[node] = val; return; }   // 叶子直接改
    const mid = (l + r) >> 1;
    if (pos <= mid) this._update(node * 2, l, mid, pos, val);
    else this._update(node * 2 + 1, mid + 1, r, pos, val);
    this.tree[node] = Math.max(this.tree[node * 2], this.tree[node * 2 + 1]); // 回溯重算
  }
  query(ql, qr) { return this._query(1, 0, this.n - 1, ql, qr); }
  _query(node, l, r, ql, qr) {
    if (qr < l || r < ql) return -Infinity;           // 不相交：返回单位元
    if (ql <= l && r <= qr) return this.tree[node];   // 完全覆盖
    const mid = (l + r) >> 1;
    return Math.max(this._query(node * 2, l, mid, ql, qr),
                    this._query(node * 2 + 1, mid + 1, r, ql, qr));
  }
}
```

**复杂度**：建树 O(n)；`update`/`query` O(log n)；空间 O(n)。

**易错点**：
- 单位元必须是 `-Infinity` 而不是 `0`：数组全是负数时返回 0 就错了。
- `_query` 里"不相交"的判断要在"完全覆盖"**之前**，否则区间反向时会漏判。
- 单点修改不需要懒标记，硬加懒标记反而容易出错；要能说清"为什么这里不用"。
- `4 * n` 的数组开小会越界，这是所有数组版线段树的通病。
- 递归写法的调用栈深度是 O(log n)，不会爆栈；但如果用"递归建树 + n = 10⁷"就要注意内存。

**变体与追问**：
- 追问"区间加 + 区间最大值"：这时**必须**加懒标记，下推时 `tree[child] += lazy`（不加长度），且需要额外维护"次大值/严格次大值"才能做区间取 min（Segment Tree Beats），属于超纲但能加分。
- 追问"静态数组、只查询不修改"：用 **ST 表**，O(n log n) 预处理、O(1) 查询，比线段树更快。
- 追问"二维区间最大值"：二维线段树或树套树，复杂度 O(log² n)。

---

### C-400 天际线问题 · 困难 · 字节/阿里

**题干**：城市的**天际线**是从远处看城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，返回由这些建筑物形成的天际线。每个建筑物由三元组 `[left, right, height]` 表示，左边界 `left`、右边界 `right`（右边界不包含在建筑内）、高度 `height`。天际线应由若干**关键点**表示：每个关键点是 `[x, y]`，表示高度 `y` 从横坐标 `x` 开始；最后一个关键点的 `y` 坐标总是 0，仅用于标记天际线的最右端。

**示例**：
```
输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
```

**思路**：
- 天际线的本质是"每个横坐标 x 处的**最大高度**"，而高度只在**建筑的左右边界**处可能变化。所以先做**离散化**：把所有边界 x 收集起来排序，问题变成"在若干个 x 位置上求当前覆盖的最大高度"——这就是**扫描线**。
- 从左往右扫，维护一个"当前所有覆盖该 x 的建筑高度"的集合，答案是集合最大值。需要支持"插入高度、删除高度、取最大值"，**大顶堆 + 惰性删除**最合适：删除时不真的从堆里挖，而是在取堆顶时若"该建筑的右边界 ≤ 当前 x"就弹掉。
- 事件顺序是本题最大的坑：同一个 x 上，**先加左边界、后处理右边界**（或者说先加入新建筑再清理过期建筑），否则"建筑在 x 结束、另一个建筑在 x 开始"的衔接点会算错（会多输出一个高度为 0 的点，或漏掉新建筑）。
- 相邻两个 x 若最大高度相同，**不能重复输出关键点**，所以每次算出 `curMax` 后与上一次输出的高度比较，只有变化时才 push。这就是"关键点"的定义。

**代码**：
```javascript
function getSkyline(buildings) {
  const events = [];                       // [x, -height, right]，用负高度做"高者优先"
  for (const [l, r, h] of buildings) {
    events.push([l, -h, r]);               // 左边界：加入
    events.push([r, 0, 0]);                // 右边界：清理
  }
  // x 升序；同一 x 上高度大的（-h 小）先处理，右边界(0)最后
  events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  const res = [];
  const heap = [[0, Infinity]];            // 哨兵 [负高度, 右边界]，保证堆非空
  const push = (item) => {
    heap.push(item);
    let i = heap.length - 1;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (heap[p][0] <= heap[i][0]) break;
      [heap[p], heap[i]] = [heap[i], heap[p]];
      i = p;
    }
  };
  const pop = () => {
    const top = heap[0], last = heap.pop();
    if (heap.length) {
      heap[0] = last;
      let i = 0;
      for (;;) {
        const l = i * 2 + 1, r = l + 1;
        let m = i;
        if (l < heap.length && heap[l][0] < heap[m][0]) m = l;
        if (r < heap.length && heap[r][0] < heap[m][0]) m = r;
        if (m === i) break;
        [heap[m], heap[i]] = [heap[i], heap[m]];
        i = m;
      }
    }
    return top;
  };
  for (const [x, negH, r] of events) {
    while (heap[0][1] <= x) pop();         // 惰性删除：右边界已过的建筑
    if (negH !== 0) push([negH, r]);       // 左边界：加入当前建筑
    const curMax = -heap[0][0];
    if (!res.length || res[res.length - 1][1] !== curMax) res.push([x, curMax]);
  }
  return res;
}
```

**复杂度**：时间 O(n log n)（排序 + 每次事件 O(log n)）；空间 O(n)。

**易错点**：
- 事件排序必须保证"同一 x 上左边界先于右边界"（`a[1] - b[1]`，因为左边界是负高度，天然排在 0 前面）；顺序错了会在交界处多一个 `[x, 0]`。
- 惰性删除在**每次处理事件前**做（`while (heap[0][1] <= x) pop()`），只在右边界事件时清理会漏掉"堆顶过期但不是当前事件"的情况。
- 输出前必须与上一个关键点的高度比较，否则同一高度会连续输出多个点。
- 堆必须留哨兵（高度 0、右边界 `Infinity`），否则空堆时 `heap[0]` 为 `undefined`，取最大值直接崩。
- 负高度技巧是为了把"大顶堆"复用成"小顶堆"；如果在 JS 里写比较器，注意 `-0` 与 `0` 在排序中的表现。

**变体与追问**：
- 追问"能不能不用堆"：可以，用**有序多重集**（`TreeMap<高度, 出现次数>`）或线段树维护"高度轴上的覆盖计数"，取最大高度是 O(log n)。
- 追问"如何求天际线的总长度/面积"：面积 = 相邻关键点之间 `宽 × 高` 累加，这正是"天际线"在图形学里的用法。
- 工程映射：地图渲染的等高线、柱状图叠加、区间覆盖类问题的通用扫描线框架。
