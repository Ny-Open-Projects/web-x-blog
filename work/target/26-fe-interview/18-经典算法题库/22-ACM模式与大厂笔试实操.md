---
title: 22 ACM 模式与大厂笔试实操 · 经典算法 15 题
date: 2026-11-24
categories: [经典算法]
tags: [前端面试, 笔试题, C, ACM模式]
type: 笔试题
---

# 22 ACM 模式与大厂笔试实操（C-416 ~ C-430）

> 前端笔试最大的冤枉分不是不会算法，而是**读不懂输入、跑不出样例、输出格式不对**。字节、腾讯、美团、快手的机考几乎都是 ACM 模式：没有函数签名，只有 stdin / stdout；本地 IDE 跑通不算数，要能在网页代码框里零调试一次过。这一组不是纯算法题，而是**考前 10 分钟能看完的救命卡片**——模板先背熟，输入输出先写对，再谈优化。**识别特征**：题干出现「第一行一个整数 T」就是多组输入；出现「保留两位小数」就先写 `toFixed(2)`；出现 n ≤ 20 就条件反射想到状压 DP。

## 题型速查

| 场景 | 核心模板 | 复杂度 | 代表题 |
|---|---|---|---|
| stdin 读取 | `fs.readFileSync(0)` 一次读全 | O(输入) | C-416 |
| 多组输入 | 先读 T 循环，或读到 EOF | O(输入) | C-417 |
| 大数运算 | 字符串模拟竖式，从低位加 | O(len) | C-418 |
| 混排解析 | 正则把空白/逗号统一成一种分隔符 | O(输入) | C-419 |
| 输出优化 | 收集到数组，最后 `join('\n')` 一次输出 | O(输出) | C-420 |
| 二分答案 | 单调可行性 + 二分边界 | O(n log V) | C-421 |
| 前缀和 / 差分 | 区间查询 O(1)、区间加 O(1) | O(n+q) | C-422 |
| 单调队列 DP | 滑动窗口最值优化转移 | O(n) | C-423 |
| 状压 DP | 集合状态压缩成二进制 | O(2ⁿ·n²) | C-424 |
| 树形 DP | 父子两状态转移 | O(n) | C-425 |
| 换根 DP | 先求子树、再二次扫描换根 | O(n) | C-426 |
| 区间 DP | 枚举分割点合并区间 | O(n³) | C-427 |
| 数位 DP | 逐位填数 + tight 标记 | O(位数·状态) | C-428 |
| 复杂度估算 | 由 n 反推可接受的算法档位 | — | C-429 |
| 部分分策略 | 暴力保底 + 对拍验证 | — | C-430 |

---

### C-416 Node.js 读取 stdin 的三种方式 · 模板 · 字节/腾讯

**题干**（场景）：大厂机考只给一个代码框，输入通过**标准输入**给出，答案打印到**标准输出**。请写出 Node.js 读取 stdin 的三种方式：① 一次性读全；② `readline` 按行读；③ 监听 `data` 事件流式读。并说明各自适合什么场景、有什么坑。

**示例**：`输入: 3` 换行 `1 2 3` → 三种方式都应能读到 3 个 token。

**思路**：
- **方式一 `fs.readFileSync(0)`**：把 fd 0（stdin）整个读成字符串，再 `split`。代码最短、最不容易出错，是笔试首选；输入在几十 MB 以内都没问题。
- **方式二 `readline`**：适合「每行一组数据」的语义，按行回调、`close` 时统一处理。坑是异步：所有逻辑必须写在 `close` 回调里，不能写在 `createInterface` 之后。
- **方式三 `process.stdin.on('data')`**：适合超大输入流式处理，但 chunk 边界可能把一行/一个数字截断，必须自己维护缓冲区，在 `end` 时再解析。除非内存吃紧，否则不推荐。
- 三种方式都建议先 `trim()` 再去掉末尾空行，避免 `split` 出空 token。如果输入含中文，务必显式 `setEncoding('utf-8')` 或传 `'utf-8'`，否则 Buffer 按字节切分会把一个汉字拆成三个乱码。

**代码**：
```javascript
// 方式一（推荐）：一次性读入全部标准输入
const fs = require('fs');
const raw = fs.readFileSync(0, 'utf-8').trim();
const tokens = raw.split(/\s+/);        // 按任意空白切分
console.log('token 数:', tokens.length);

/* 方式二：readline 按行读取（适合“每行一组数据”）
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin });
const lines = [];
rl.on('line', (line) => lines.push(line.trim()));
rl.on('close', () => {
  // 所有逻辑写在这里，lines 已经收集完毕
  console.log(lines.length);
});
*/

/* 方式三：data 事件流式读取（超大输入）
let buf = '';
process.stdin.setEncoding('utf-8');
process.stdin.on('data', (chunk) => { buf += chunk; });
process.stdin.on('end', () => {
  const arr = buf.trim().split(/\s+/);
  console.log(arr.length);
});
*/
```

**复杂度**：时间 O(输入规模)，空间 O(输入规模)。

**易错点**：
- 用 `readFileSync(0)` 时忘了 `'utf-8'`，拿到的是 `Buffer`，`split` 会报错。
- `readline` 是异步的，写在 `rl.on('line')` 外面的 `console.log(lines)` 一定拿到空数组。
- `data` 事件的 chunk 不保证按行边界切分，直接 `chunk.split('\n')` 会把数字切成两半。
- Windows 换行是 `\r\n`，只用 `split('\n')` 会残留 `\r`，`Number('3\r')` 虽然能转但比较字符串时会出错。

**变体与追问**：
- 输入只有一个数：`Number(fs.readFileSync(0, 'utf-8').trim())` 一行搞定。
- 需要按行保留空格语义（比如统计每行单词数）：必须用 `readline`，不能用 `split(/\s+/)`。
- 输出量大时用 `process.stdout.write`，并在最后手动补 `\n`。

---

### C-417 多组输入的处理模板 · 模板 · 美团/快手

**题干**（场景）：机考最常见的输入格式有两种：① 第一行是组数 `T`，接下来 `T` 组数据；② 没有 `T`，一直读到文件结束（EOF）。请写出两套**可直接套用**的模板：每组第一行是 `n`，第二行是 `n` 个整数，要求输出每组的总和，每组一行。

**示例**：`输入: 2` / `3` / `1 2 3` / `2` / `10 20` → `输出: 6` 换行 `30`

**思路**：
- 无论哪种格式，先把整个输入按空白切成 `tokens`，再用一个指针 `ptr` 顺序消费，这是 ACM 模式最稳的写法——不用关心换行，数字和行号自然对齐。
- 有 `T` 的版本：先 `T = Number(tokens[ptr++])`，然后循环 `T` 次；每次先读 `n`，再读 `n` 个数。
- 读到 EOF 的版本：`while (ptr < tokens.length)`，每轮读 `n` 和 `n` 个数。注意最后一组后面可能没有换行，`trim` 后不会多出空 token。
- 输出统一收集到 `out` 数组，最后 `out.join('\n')`，避免每组都 `console.log` 导致大量 I/O。另外要小心 n=0 的组：此时不读任何数，但这一组仍要输出一个 0 或空行，按题目要求处理。

**代码**：
```javascript
const fs = require('fs');
const data = fs.readFileSync(0, 'utf-8').trim().split(/\s+/);
let ptr = 0;
const out = [];

// 版本 A：第一行是组数 T
const T = Number(data[ptr++]);
for (let t = 0; t < T; t++) {
  const n = Number(data[ptr++]);
  let sum = 0;
  for (let i = 0; i < n; i++) sum += Number(data[ptr++]);
  out.push(String(sum));
}
console.log(out.join('\n'));

/* 版本 B：没有 T，读到 EOF
while (ptr < data.length) {
  const n = Number(data[ptr++]);
  let sum = 0;
  for (let i = 0; i < n; i++) sum += Number(data[ptr++]);
  out.push(String(sum));
}
console.log(out.join('\n'));
*/
```

**复杂度**：时间 O(总输入规模)，空间 O(总输入规模)。

**易错点**：
- 用「按行读」时，如果某组数据跨多行或一行有多组，会直接错位；按 token 消费最稳。
- `ptr` 忘记自增、或在内层循环里重复自增，是最常见的越界原因。
- 读到 EOF 的版本不要用 `for (let t = 0; t < T; t++)`，此时根本没有 `T`。
- 如果题目要求「每组输出后跟一个空行」，要在 `join` 时用 `'\n\n'` 或在每组后手动加空串。

**变体与追问**：
- 每组第一行是 `n m`，接下来 `n` 行每行 `m` 个数：多套一层循环即可。
- 输入以 `0 0` 结束：在循环里判断 `if (n === 0 && m === 0) break;`。
- 组数很大（1e5 组）时，务必用 `join` 一次性输出，逐行 `console.log` 会超时。

---

### C-418 大数相加（ACM 模式） · 中等 · 字节/腾讯

**题干**：给定两个非负整数字符串 `a` 和 `b`（长度可达 1e5，远超 JS `Number` 的安全整数范围），请计算它们的和并以字符串形式输出。禁止使用 `BigInt`，要求模拟竖式加法。

**示例**：`输入: 12345678901234567890 98765432109876543210` → `输出: 111111111011111111100`

**思路**：
- JS 的 `Number` 只能精确表示 2⁵³−1 以内的整数，两个 1e5 位的数相加必然溢出，所以必须用字符串模拟。
- 竖式加法：两个指针分别指向 `a`、`b` 的末尾，从低位往高位逐位相加，用 `carry` 保存进位。每一位的结果是 `(x + y + carry) % 10`，新进位是 `(x + y + carry) / 10` 向下取整。
- 循环条件是 `i >= 0 || j >= 0 || carry > 0`，三个条件缺一不可：两个数都遍历完后，如果还有进位，必须再补一位。
- 结果是从低位往高位 push 的，最后要 `reverse()` 再 `join('')`。用 `charCodeAt(i) - 48` 比 `Number(a[i])` 快，适合长字符串。
- 如果允许 `BigInt`，`String(BigInt(a) + BigInt(b))` 一行就能过，但面试官常要求手写模拟，两种都要会。结果的位数最多是 `max(|a|, |b|) + 1`，所以结果数组按这个上界开即可，不会溢出。

**代码**：
```javascript
const fs = require('fs');
const [a, b] = fs.readFileSync(0, 'utf-8').trim().split(/\s+/);

function addBig(a, b) {
  let i = a.length - 1;
  let j = b.length - 1;
  let carry = 0;
  const res = [];

  while (i >= 0 || j >= 0 || carry > 0) {
    // 取当前位，越界补 0；charCodeAt - 48 比 Number 快
    const x = i >= 0 ? a.charCodeAt(i--) - 48 : 0;
    const y = j >= 0 ? b.charCodeAt(j--) - 48 : 0;
    const sum = x + y + carry;
    res.push(sum % 10);          // 当前位
    carry = (sum / 10) | 0;      // 新进位
  }

  return res.reverse().join('');
}

console.log(addBig(a, b));
```

**复杂度**：时间 O(max(|a|, |b|))，空间 O(max(|a|, |b|))。

**易错点**：
- 循环条件漏掉 `carry > 0`，`999 + 1` 会输出 `000` 而不是 `1000`。
- `carry = sum / 10` 不取整，`carry` 会变成小数，下一位计算全错。
- 两个数长度不同时，短的那个指针越界后要补 0，不能直接退出循环。
- 结果是低位在前，忘记 `reverse()` 会输出倒序。
- 输入可能有多余空格或空行，用 `trim().split(/\s+/)` 最稳。

**变体与追问**：
- 大数相减：需要先比较大小、处理借位，结果为负时加负号。
- 大数相乘：模拟竖式，`res[i+j+1] += a[i]*b[j]`，再做进位，O(nm)。
- 大数比较：先比长度，长度相同再从高位逐位比。
- 允许 `BigInt` 时：`String(BigInt(a) + BigInt(b))`，但注意 `BigInt` 不能和 `Number` 混算。

---

### C-419 输入解析（空格/逗号/换行混排） · 模板 · 美团/拼多多

**题干**（场景）：有些题目的输入既不是纯空格分隔，也不是纯换行，而是「第一行 `n`，第二行逗号分隔的数组，后面若干行 `key=value`」这种混排格式。请写一个**统一 token 化**的解析模板：把空格、换行、英文逗号、中文逗号、分号都视为分隔符，然后按顺序取数。

**示例**：`输入: 3` / `1, 2，3` → 解析出 `n = 3`，数组为 `[1, 2, 3]`

**思路**：
- 不要为每种分隔符写一套 `split`，而是**先归一化再切分**：把中文逗号 `，`、顿号 `、`、分号 `;` 全部替换成英文逗号，再用 `/[\s,]+/` 一次性切开，最后 `filter(Boolean)` 去掉空串。
- 切完之后得到一个扁平的 `tokens` 数组，用一个指针 `ptr` 顺序消费。这样无论原始输入怎么换行、怎么混用分隔符，解析逻辑都不变。
- 如果某些字段是 `key=value` 形式，先按空白切出每个 `pair`，再对每个 `pair` 用 `split('=')` 拆成键值，不要一上来就用逗号切，否则 `=` 会被误伤。
- 数字统一用 `Number()` 转，注意 `Number('')` 是 0，所以一定要先 `filter(Boolean)`。

**代码**：
```javascript
const fs = require('fs');
const raw = fs.readFileSync(0, 'utf-8');

// 1) 归一化：中文标点统一成英文逗号
const normalized = raw.replace(/[，、;；]/g, ',');

// 2) 按「空白或逗号」切分，过滤空 token
const tokens = normalized.split(/[\s,]+/).filter(Boolean);

// 3) 顺序消费：第一段是 n，后面 n 个数
let ptr = 0;
const n = Number(tokens[ptr++]);
const arr = tokens.slice(ptr, ptr + n).map(Number);

console.log('n =', n);
console.log('arr =', JSON.stringify(arr));

// 4) 如果还有 key=value 段，继续从 ptr + n 开始读
const rest = tokens.slice(ptr + n);
const map = {};
for (const pair of rest) {
  const [k, v] = pair.split('=');
  if (k) map[k] = v;
}
console.log(map);
```

**复杂度**：时间 O(输入规模)，空间 O(输入规模)。

**易错点**：
- 只写 `split(',')` 会把换行和空格留在 token 里，`Number(' 2')` 虽然能转，但 `'2\n3'` 会变成 `NaN`。
- 中文逗号 `，` 和英文逗号 `,` 是不同的字符，必须显式替换。
- `filter(Boolean)` 不能省，否则末尾换行会产生空 token，`Number('') === 0` 会悄悄多出一个 0。
- `key=value` 里的 `value` 如果本身含逗号（比如 CSV），要先按行切再按逗号切，不能全局归一化。

**变体与追问**：
- 输入是 JSON 字符串：直接 `JSON.parse(raw)`，不要手写解析。
- 输入是 CSV 且字段带引号：需要状态机解析，不能简单 `split`。
- 输入含负数：`Number('-3')` 正常，但 `split(/[\s,]+/)` 不会把负号当分隔符，安全。

---

### C-420 输出格式化与大数组 join 性能 · 模板 · 字节/阿里

**题干**（场景）：题目要求输出 `n` 行结果（n 可达 1e5），很多人的写法是循环里 `console.log(ans)`，结果本地秒过、提交超时。请说明为什么，并给出正确的输出模板；同时说明浮点数保留两位小数、以及大数组拼接的注意事项。

**示例**：输出 1 到 100000，每行一个数。

**思路**：
- `console.log` 每次都会做格式化并触发一次写系统调用，10 万次调用的开销远大于算法本身；在 Node 里尤其明显，因为 stdout 在非 TTY 环境下也可能是同步/半同步的。
- 正确做法：先把每行结果转成字符串放进数组 `out`，最后 `process.stdout.write(out.join('\n') + '\n')` 一次性写出。这样只有一次 I/O。
- 提前 `String(x)` 而不是留给 `join` 隐式转换，可以避免 `join` 内部对每个元素做类型判断；对 1e6 级别有可感知的差别。
- 浮点数用 `x.toFixed(2)`，但它返回的是字符串，且采用「四舍六入五成双」以外的规则（实际是二进制浮点最近值），涉及金额时建议先转整数分再算。
- 如果输出量特别大（几十 MB），可以分块 `write`，避免一次拼接占满内存。

**代码**：
```javascript
// 反例：循环里 console.log，10 万行会非常慢
// for (let i = 1; i <= 100000; i++) console.log(i);

// 正例：先收集，再一次性 join 输出
const n = 100000;
const out = new Array(n);
for (let i = 0; i < n; i++) {
  out[i] = String(i + 1);          // 提前转字符串，join 更快
}
process.stdout.write(out.join('\n') + '\n');

// 浮点格式化：保留两位小数
const pi = 3.14159;
const money = 2.005;
console.log(pi.toFixed(2));        // "3.14"
console.log(money.toFixed(2));     // "2.00"（二进制浮点误差，注意）

// 金额建议先转整数分再算，最后除 100
const cents = Math.round(2.005 * 100);
console.log((cents / 100).toFixed(2)); // "2.01"
```

**复杂度**：时间 O(输出总长度)，空间 O(输出总长度)。

**易错点**：
- `console.log` 传数组会打印成 `[1, 2, 3]`，不是每行一个；必须 `join('\n')`。
- `join` 之后忘记补末尾换行，部分判题机对最后一行没有换行不敏感，但有的会 WA。
- `toFixed` 返回字符串，不要再 `Number()` 转回去，否则末尾的 0 会丢。
- `2.005.toFixed(2)` 在 JS 里是 `"2.00"`，不是 `"2.01"`，涉及金额要特别小心。
- 输出 1e6 行时，`out` 数组本身占内存，建议边算边写或分块。

**变体与追问**：
- 需要输出空格分隔：`out.join(' ')`。
- 需要输出矩阵：每行内部 `join(' ')`，行之间 `join('\n')`。
- 输出超长（>100MB）：用 `process.stdout.write` 分块，每 1e4 行写一次。

---
### C-421 二分答案实战（月度开销） · 中等 · 字节/美团

**题干**：给出 `n` 天的开销 `cost[i]`，需要把这 `n` 天划分成 `m` 段**连续**的区间，每一段的花费是该段开销之和。请设计一种划分，使**最大段和最小**，输出这个最小值。经典题源为 POJ 3273「Monthly Expense」。

**示例**：`输入: n = 7, m = 5, cost = [100,400,300,100,500,101,400]` → `输出: 500`

**思路**：
- 「最大段和最小」是典型的**二分答案**：直接求最优划分很难，但判断「给定上限 `limit`，能否用不超过 `m` 段装下所有开销」很容易——贪心地从左往右装，装不下就开新段，最后看段数是否 `<= m`。
- 这个判定关于 `limit` 单调：上限越大，需要的段数越少。因此可以二分 `limit`，下界是 `max(cost)`（至少要装下最大的一天），上界是 `sum(cost)`（全部装进一段）。
- 二分写法用 `while (lo < hi)` + `if (can(mid)) hi = mid; else lo = mid + 1;`，最后 `lo` 就是最小可行上限。注意这里求的是「最小可行值」，所以可行时收缩右边界。
- **为什么贪心判定是对的**：在固定上限下，每一段装得越满，剩余的天数越少，段数只会更少，不会更差，所以「能装就装」不会错过可行解。

**代码**：
```javascript
const fs = require('fs');
const data = fs.readFileSync(0, 'utf-8').trim().split(/\s+/).map(Number);
let p = 0;
const n = data[p++];
const m = data[p++];
const cost = data.slice(p, p + n);

function minMaxSegmentSum(cost, m) {
  let lo = Math.max(...cost);                       // 下界：最大单日开销
  let hi = cost.reduce((a, b) => a + b, 0);         // 上界：全部装一段

  // 给定上限 limit，最少需要多少段
  const can = (limit) => {
    let groups = 1;
    let sum = 0;
    for (const x of cost) {
      if (sum + x > limit) {                        // 装不下，开新段
        groups++;
        sum = x;
      } else {
        sum += x;
      }
    }
    return groups <= m;
  };

  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (can(mid)) hi = mid;                         // 可行，尝试更小
    else lo = mid + 1;                              // 不可行，放大
  }
  return lo;
}

console.log(minMaxSegmentSum(cost, m)); // 500
```

**复杂度**：时间 O(n log(sum))，空间 O(1)（不计输入）。

**易错点**：
- 下界必须是 `max(cost)`，写成 0 会让 `can(0)` 永远为 false，虽然二分仍能收敛，但会多跑很多轮。
- `groups` 初始为 1，不是 0；第一天一定属于第一段。
- 二分收缩方向别写反：求最小可行值用 `hi = mid`，求最大可行值才用 `lo = mid`。
- `Math.max(...cost)` 在 n 超过约 1e5 时可能栈溢出，改用 `cost.reduce((a,b)=>Math.max(a,b))`。
- 若某天开销大于 `limit`，贪心会把它单独成段但仍超限，此时 `can` 应返回 false；由于下界是最大值，这种情况不会出现在二分区间内。

**变体与追问**：
- 分割数组的最大值（LC 410）：完全一样的题，只是参数顺序不同。
- 切绳子 / 搬货物：判定函数换成「能切出多少段」。
- 要求输出具体划分方案：二分出 `limit` 后，再贪心走一遍记录切点。

---

### C-422 前缀和与差分实战 · 模板 · 美团/拼多多

**题干**（场景）：给一个长度为 `n` 的数组，需要支持两类操作：① 多次查询区间 `[l, r]` 的和；② 多次对区间 `[l, r]` 的每个元素加上 `v`，最后输出整个数组。请分别用**前缀和**和**差分**做到每次操作 O(1)。

**示例**：`a = [1,2,3,4,5]`，查询 `[1,3]` 的和为 `9`；对 `n=5` 执行 `[0,2]+10`、`[1,3]+5` 后数组为 `[10,15,15,5,0]`。

**思路**：
- **前缀和**：`pre[i+1] = pre[i] + a[i]`，则区间 `[l, r]`（0-based，闭区间）的和是 `pre[r+1] - pre[l]`。预处理 O(n)，每次查询 O(1)。适合「数组不变、大量查询」。
- **差分**：`diff[l] += v`、`diff[r+1] -= v`，表示「从 l 开始都加 v，从 r+1 开始撤销」。所有操作做完后，对 `diff` 求一次前缀和，就得到每个位置的真实增量。每次区间加 O(1)，最后还原 O(n)。适合「大量修改、最后统一查询」。
- 两者是互逆的：前缀和把「点值」变成「区间信息」，差分把「区间修改」变成「点修改」。
- 二维版本同理：二维前缀和用容斥 `pre[i][j] = ...`，二维差分四个角打标记。笔试输入通常是 1-based 下标，转成 0-based 时记得统一减 1，区间端点不要一个减一个不减。

**代码**：
```javascript
// ---------- 前缀和：区间查询 O(1) ----------
function buildPrefix(a) {
  const pre = new Array(a.length + 1).fill(0);
  for (let i = 0; i < a.length; i++) pre[i + 1] = pre[i] + a[i];
  return pre;
}
// 查询闭区间 [l, r] 的和（0-based）
function rangeSum(pre, l, r) {
  return pre[r + 1] - pre[l];
}

// ---------- 差分：区间加 O(1)，最后统一还原 ----------
function applyRangeAdd(n, ops) {
  const diff = new Array(n + 1).fill(0);
  for (const [l, r, v] of ops) {
    diff[l] += v;
    diff[r + 1] -= v;        // 多开一位，防止 r = n-1 越界
  }
  const res = new Array(n);
  let cur = 0;
  for (let i = 0; i < n; i++) {
    cur += diff[i];
    res[i] = cur;
  }
  return res;
}

const pre = buildPrefix([1, 2, 3, 4, 5]);
console.log(rangeSum(pre, 1, 3)); // 9
console.log(applyRangeAdd(5, [[0, 2, 10], [1, 3, 5]])); // [10,15,15,5,0]
```

**复杂度**：前缀和预处理 O(n)、查询 O(1)；差分每次修改 O(1)、还原 O(n)；空间 O(n)。

**易错点**：
- 前缀和数组长度是 `n+1`，`pre[0] = 0`；查询 `[l, r]` 用 `pre[r+1] - pre[l]`，不是 `pre[r] - pre[l]`。
- 差分的 `diff` 要开 `n+1`，因为 `r+1` 可能等于 `n`。
- 差分只能处理「先修改、后查询」；如果修改和查询交替，需要树状数组或线段树。
- 差分还原时 `cur` 是累加增量，不是直接赋值；若有初始数组，最后要加上 `a[i]`。

**变体与追问**：
- 二维前缀和：`pre[i+1][j+1] = a[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j]`。
- 区间修改 + 区间查询：用树状数组维护两个差分数组。
- 最大子段和：前缀和 + 维护最小前缀，O(n)。

---

### C-423 单调队列优化 DP 实战 · 困难 · 字节/快手

**题干**：给你一个下标从 0 开始的整数数组 `nums` 和一个整数 `k`。初始你在下标 0，每一步最多可以往前跳 `k` 步（即从 `i` 跳到 `i+1 ... i+k`），到达 `n-1` 结束。你的得分是路径上所有 `nums[i]` 之和。请返回你能得到的**最大得分**（LC 1696 Jump Game VI）。

**示例**：`输入: nums = [1,-1,-2,4,-7,3], k = 2` → `输出: 7`（路径 0 → 1 → 3 → 5，得分 1-1+4+3=7）

**思路**：
- 朴素 DP：`dp[i] = nums[i] + max(dp[j])`，其中 `j ∈ [i-k, i-1]`。如果每个 `i` 都扫一遍窗口，复杂度 O(nk)，k 大时退化到 O(n²)。
- 观察转移只需要「窗口内的最大值」，而窗口是固定长度、从左往右滑的，正是**单调队列**的用武之地：队列里存下标，对应的 `dp` 值从队头到队尾**单调递减**。
- 每次计算 `dp[i]` 前，先把队头滑出窗口的下标弹掉（`dq[head] < i - k`），此时队头就是窗口最大值的下标，直接转移。
- 计算完 `dp[i]` 后，从队尾把 `dp` 值 `<= dp[i]` 的下标全部弹出（它们不可能再成为最大值），再把 `i` 入队。
- **为什么是 O(n)**：每个下标最多入队一次、出队一次，均摊 O(1)；相比 O(nk) 的暴力，省掉了重复扫描窗口。

**代码**：
```javascript
function maxResult(nums, k) {
  const n = nums.length;
  const dp = new Array(n).fill(0);
  const dq = new Array(n);          // 存下标，dp 值单调递减
  let head = 0;
  let tail = 0;

  dp[0] = nums[0];
  dq[tail++] = 0;

  for (let i = 1; i < n; i++) {
    // 1) 队头滑出窗口 [i-k, i-1]
    while (head < tail && dq[head] < i - k) head++;
    // 2) 队头即窗口内 dp 最大值
    dp[i] = dp[dq[head]] + nums[i];
    // 3) 维护单调性：比 dp[i] 小的队尾永远用不到了
    while (head < tail && dp[dq[tail - 1]] <= dp[i]) tail--;
    dq[tail++] = i;
  }
  return dp[n - 1];
}

console.log(maxResult([1, -1, -2, 4, -7, 3], 2)); // 7
console.log(maxResult([10, -10, -10, 10], 2));    // 10
```

**复杂度**：时间 O(n)，空间 O(n)。

**易错点**：
- 弹队头用 `while` 不用 `if`：可能一次滑出多个过期下标。
- 单调队列存的是**下标**，不是值；比较时用 `dp[dq[tail-1]]`。
- 维护单调性用 `<=` 还是 `<` 取决于是否允许重复值；这里用 `<=` 弹掉旧的等值下标，减少队列长度，不影响答案。
- 队列用数组 + `head/tail` 指针，不要用 `shift()`，`shift` 是 O(n) 会让整体退化。
- `k >= n` 时窗口不会滑出，答案等价于 `nums[0] + max(剩余正数)`，代码自然覆盖。

**变体与追问**：
- 滑动窗口最大值（LC 239）：单调队列的直接应用，不需要 DP。
- 最大子序和（LC 53）：可以用前缀和 + 单调队列求长度不超过 k 的最大子段和。
- 多重背包的单调队列优化：把「物品个数限制」转化为滑动窗口最值。

---

### C-424 状态压缩 DP 实战（旅行商） · 困难 · 字节/阿里

**题干**：给定 `n` 个城市（`n <= 18`）和 `n × n` 的距离矩阵 `dist`，从城市 0 出发，每个城市恰好访问一次，最后回到城市 0，求最短回路长度（TSP，旅行商问题）。

**示例**：`dist = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]` → `输出: 80`（路线 0→1→3→2→0，长度 10+25+30+15=80）

**思路**：
- 暴力枚举所有排列是 O(n!)，n=18 时是 6.4e15，完全不可行。
- 状压 DP 的核心是：我们只关心「**已经访问过哪些城市**」和「**当前停在哪个城市**」，不关心访问顺序。把「已访问集合」压缩成一个二进制数 `mask`，第 `i` 位为 1 表示城市 `i` 已访问。
- 定义 `dp[mask][i]`：从 0 出发，访问过的集合为 `mask`，最后停在 `i` 的最小花费。转移：从 `dp[mask][i]` 出发，枚举一个未访问的城市 `j`，`dp[mask | (1<<j)][j] = min(..., dp[mask][i] + dist[i][j])`。
- 初始 `dp[1][0] = 0`（只访问了城市 0，停在 0）。最终答案是 `min(dp[full][i] + dist[i][0])`，`full = (1<<n)-1`。
- **为什么能降复杂度**：状态数 `2ⁿ · n`，每个状态转移 `n` 次，总 O(2ⁿ·n²)。n=18 时约 8500 万，勉强可过；n=20 就要考虑剪枝或启发式。不能用贪心（每次走最近的城市）——TSP 的局部最优不等于全局最优，反例很容易构造。

**代码**：
```javascript
function tsp(dist) {
  const n = dist.length;
  const full = 1 << n;
  const INF = Infinity;

  // dp[mask][i]：访问集合 mask、最后停在 i 的最小花费
  const dp = Array.from({ length: full }, () => new Array(n).fill(INF));
  dp[1][0] = 0;                         // 只访问了 0，停在 0

  for (let mask = 1; mask < full; mask++) {
    for (let i = 0; i < n; i++) {
      if (!(mask & (1 << i)) || dp[mask][i] === INF) continue;
      for (let j = 0; j < n; j++) {
        if (mask & (1 << j)) continue;   // j 已访问，跳过
        const next = mask | (1 << j);
        const cost = dp[mask][i] + dist[i][j];
        if (cost < dp[next][j]) dp[next][j] = cost;
      }
    }
  }

  let ans = INF;
  for (let i = 1; i < n; i++) {
    ans = Math.min(ans, dp[full - 1][i] + dist[i][0]); // 回到起点
  }
  return ans;
}

const dist = [
  [0, 10, 15, 20],
  [10, 0, 35, 25],
  [15, 35, 0, 30],
  [20, 25, 30, 0],
];
console.log(tsp(dist)); // 80
```

**复杂度**：时间 O(2ⁿ·n²)，空间 O(2ⁿ·n)。

**易错点**：
- 初始状态是 `dp[1][0] = 0`，不是 `dp[0][0]`；至少要访问起点。
- 判断 `j` 是否已访问用 `mask & (1 << j)`，不要写成 `mask & j`。
- 最终要加上 `dist[i][0]` 回到起点，漏掉就变成「最短哈密顿路径」。
- n 超过 20 时 `2ⁿ·n` 的内存会爆（n=20 时约 2000 万个状态），必须换思路或剪枝。
- `1 << n` 在 n=31 时会溢出成负数，n 较大时用 `2 ** n` 或 BigInt（但 TSP 本身也跑不动）。

**变体与追问**：
- 最短哈密顿路径（不要求回到起点）：答案是 `min(dp[full-1][i])`。
- 每个城市有多个任务、有前置依赖：在 mask 上加约束，转移时检查前置集合是否为 mask 子集。
- 集合覆盖 / 状压枚举子集：`for (let sub = mask; sub; sub = (sub-1) & mask)`。

---

### C-425 树形 DP 实战（树上最大独立集） · 困难 · 字节/美团

**题干**：给定一棵 `n` 个节点的树，每个节点有一个权值 `w[i]`。请选出若干个节点，使得任意两个被选中的节点**不相邻**，且选中节点的权值之和最大。输出这个最大和（树的最大权独立集）。

**示例**：`n = 4`，`w = [1,2,3,4]`，边为 `1-2`、`1-3`、`2-4` → `输出: 7`（选节点 3 和 4）

**思路**：
- 树形 DP 的套路：任选一个根，把无根树变成有根树，然后定义「以 `u` 为根的子树」上的状态。
- 每个节点只有两种状态：**选**或**不选**。定义 `dp1[u]` 为「选 `u` 时子树的最大和」，`dp0[u]` 为「不选 `u` 时子树的最大和」。
- 转移：如果选了 `u`，所有子节点都不能选，所以 `dp1[u] = w[u] + Σ dp0[v]`；如果不选 `u`，子节点选不选都行，取较大值，所以 `dp0[u] = Σ max(dp0[v], dp1[v])`。
- 从根开始 DFS 后序计算，答案是 `max(dp0[root], dp1[root])`。
- **为什么正确**：每个子树的最优解只依赖根节点选/不选，子问题独立；枚举完两种状态就覆盖了所有合法方案，且不会重复计算。
- 注意：n 到 1e5 时递归可能爆栈，笔试里要么手动扩栈（Node 不好扩），要么写成迭代后序。

**代码**：
```javascript
const fs = require('fs');
const data = fs.readFileSync(0, 'utf-8').trim().split(/\s+/).map(Number);
let p = 0;
const n = data[p++];
const w = data.slice(p, p + n);
p += n;

const g = Array.from({ length: n }, () => []);
for (let i = 0; i < n - 1; i++) {
  const u = data[p++] - 1;
  const v = data[p++] - 1;
  g[u].push(v);
  g[v].push(u);
}

const dp0 = new Array(n).fill(0);  // 不选 u
const dp1 = new Array(n).fill(0);  // 选 u

function dfs(u, parent) {
  dp1[u] = w[u];
  for (const v of g[u]) {
    if (v === parent) continue;
    dfs(v, u);
    dp1[u] += dp0[v];                       // 选 u，子节点必须不选
    dp0[u] += Math.max(dp0[v], dp1[v]);     // 不选 u，子节点随意
  }
}

dfs(0, -1);
console.log(Math.max(dp0[0], dp1[0])); // 7
```

**复杂度**：时间 O(n)，空间 O(n)。

**易错点**：
- 递归时一定要传 `parent`，否则在无向树上会走回父节点，无限递归。
- `dp1[u]` 初始化为 `w[u]`，不是 0；`dp0[u]` 初始化为 0。
- 选 `u` 时子节点只能不选（`dp0[v]`），不能取 `max`，这是与「不选 u」的唯一区别。
- 多棵树（森林）要遍历所有未访问节点，分别取 `max` 再相加。
- n 很大时递归深度可能到 1e5，Node 默认栈会溢出；可以手动用数组模拟栈做后序。

**变体与追问**：
- 没有上司的舞会（洛谷 P1352）：完全一样的模型，权值在节点上。
- 树上最小点覆盖：`min(dp0, dp1)` 的变形，或最大独立集 = 总点数 - 最小点覆盖（二分图）。
- 树上染色 / 相邻不能同色：把状态从 2 个扩展到 k 个。

---
### C-426 换根 DP 实战 · 困难 · 字节/阿里

**题干**：给定一棵 `n` 个节点的无向树，节点编号 `0 ~ n-1`。请返回数组 `ans`，其中 `ans[i]` 表示节点 `i` 到其余所有节点的**距离之和**（LC 834 Sum of Distances in Tree）。

**示例**：`n = 6`，`edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]` → `输出: [8,12,6,10,10,10]`

**思路**：
- 如果对每个节点都跑一次 BFS，复杂度 O(n²)，n 到 1e5 必超时。
- 换根 DP 分两遍 DFS：
  1. **第一遍（求子树信息）**：任选 0 为根，`size[u]` 是 `u` 的子树大小，`ans[u]` 是 `u` 到其子树内所有节点的距离和。转移：`ans[u] = Σ(ans[v] + size[v])`，因为 `v` 子树内每个节点到 `u` 的距离，都比到 `v` 多 1。
  2. **第二遍（换根传播）**：已知 `ans[u]`，把根从 `u` 移到相邻子节点 `v`。此时 `v` 子树内的 `size[v]` 个节点距离各减少 1，其余 `n - size[v]` 个节点距离各增加 1，所以 `ans[v] = ans[u] - size[v] + (n - size[v])`。
- **为什么 O(n)**：每个节点在第一遍、第二遍各访问一次，转移 O(1)。
- 这个「先求子树、再利用父子关系推全局」的套路是所有换根 DP 的模板，遇到「每个点作为根时的某个值」都可以往这上面套。

**代码**：
```javascript
const fs = require('fs');
const data = fs.readFileSync(0, 'utf-8').trim().split(/\s+/).map(Number);
let p = 0;
const n = data[p++];
const g = Array.from({ length: n }, () => []);
for (let i = 0; i < n - 1; i++) {
  const u = data[p++];
  const v = data[p++];
  g[u].push(v);
  g[v].push(u);
}

const size = new Array(n).fill(1);
const ans = new Array(n).fill(0);

// 第一遍：求子树大小 + 子树内距离和
function dfs1(u, parent) {
  for (const v of g[u]) {
    if (v === parent) continue;
    dfs1(v, u);
    size[u] += size[v];
    ans[u] += ans[v] + size[v];   // v 子树每个点都多走一条边
  }
}

// 第二遍：换根，由父推子
function dfs2(u, parent) {
  for (const v of g[u]) {
    if (v === parent) continue;
    // v 子树内 n 个点距离 -1，其余点距离 +1
    ans[v] = ans[u] - size[v] + (n - size[v]);
    dfs2(v, u);
  }
}

dfs1(0, -1);
dfs2(0, -1);
console.log(ans); // [8, 12, 6, 10, 10, 10]
```

**复杂度**：时间 O(n)，空间 O(n)。

**易错点**：
- 第一遍的 `ans[u]` 必须加上 `size[v]`，因为 `v` 子树内每个点到 `u` 都要多走 `u-v` 这条边。
- 换根公式是 `ans[u] - size[v] + (n - size[v])`，减的是 `size[v]`（子树内变近），加的是 `n - size[v]`（其余变远），不要写反。
- 第二遍 DFS 必须在第一遍全部完成后才能开始，否则 `size` 还没算好。
- 递归深度到 1e5 会爆栈，笔试里可以改成迭代后序（用栈记录访问顺序）。
- 多棵树（森林）要对每个根分别跑，答案不能直接拼接。

**变体与追问**：
- 换根求「每个点的最远距离」：需要同时维护子树内最大值和次大值。
- 换根求「每个点为根的子树权值和」：转移更简单，只加减子树和。
- 树上所有点对距离和：可以只跑第一遍，`Σ ans[i]` 再除以 2。

---

### C-427 区间 DP 实战（石子合并） · 困难 · 字节/美团

**题干**：有 `n` 堆石子排成一排，第 `i` 堆重量为 `stones[i]`。每次只能合并**相邻**的两堆，代价为两堆重量之和，合并后新堆的重量为两者之和。请把所有石子合并成一堆，求**最小总代价**。

**示例**：`输入: stones = [1,3,5,2]` → `输出: 22`（先合并 1+3=4，再合并 5+2=7，最后 4+7=11，总代价 4+7+11=22）

**思路**：
- 最后一次合并一定是把某个区间 `[i, j]` 分成 `[i, k]` 和 `[k+1, j]` 两堆再合并，代价是区间总和。于是可以枚举分割点 `k`。
- 定义 `dp[i][j]` 为把区间 `[i, j]` 合并成一堆的最小代价。转移：
  `dp[i][j] = min(dp[i][k] + dp[k+1][j]) + sum(i, j)`，`k ∈ [i, j-1]`。
- 区间长度从 2 开始枚举，保证计算 `dp[i][j]` 时所有更短的子区间已经算好。`sum(i,j)` 用前缀和 O(1) 求。
- **为什么是 O(n³)**：区间数 O(n²)，每个区间枚举 O(n) 个分割点。n ≤ 500 可过；n 到 3000 需要「四边形不等式」优化到 O(n²)。
- 如果石子**围成一圈**，把数组复制一份接在后面，对所有长度为 `n` 的窗口取最小值。

**代码**：
```javascript
const fs = require('fs');
const data = fs.readFileSync(0, 'utf-8').trim().split(/\s+/).map(Number);
let p = 0;
const n = data[p++];
const stones = data.slice(p, p + n);

function stoneMerge(stones) {
  const n = stones.length;
  const pre = new Array(n + 1).fill(0);
  for (let i = 0; i < n; i++) pre[i + 1] = pre[i] + stones[i];

  const dp = Array.from({ length: n }, () => new Array(n).fill(0));

  for (let len = 2; len <= n; len++) {          // 区间长度
    for (let i = 0; i + len - 1 < n; i++) {
      const j = i + len - 1;
      dp[i][j] = Infinity;
      const sum = pre[j + 1] - pre[i];          // 区间总和
      for (let k = i; k < j; k++) {             // 枚举分割点
        const cost = dp[i][k] + dp[k + 1][j] + sum;
        if (cost < dp[i][j]) dp[i][j] = cost;
      }
    }
  }
  return dp[0][n - 1];
}

console.log(stoneMerge(stones)); // 22
```

**复杂度**：时间 O(n³)，空间 O(n²)。

**易错点**：
- 区间长度从 2 开始，长度 1 的 `dp[i][i] = 0`（不用合并）。
- 内层 `i` 的边界是 `i + len - 1 < n`，写成 `i + len <= n` 也对，但 `j` 要相应调整。
- `dp[i][j]` 必须先置为 `Infinity` 再取 min，否则默认 0 会让答案永远是 0。
- 分割点 `k` 的范围是 `[i, j-1]`，取到 `j` 会出现空区间。
- 环形石子合并不能只复制数组，还要把 `dp` 开到 `2n`，最后在 `dp[i][i+n-1]` 中取最小。

**变体与追问**：
- 环形石子合并：数组翻倍，答案 `min(dp[i][i+n-1])`，i 从 0 到 n-1。
- 合并果子（每次合并任意两堆）：那是哈夫曼树，用优先队列，不是区间 DP。
- 矩阵链乘：转移同样是枚举分割点，代价换成矩阵乘法次数。
- 四边形不等式优化：当代价满足单调性时，分割点范围可以缩小，O(n²)。

---

### C-428 数位 DP 实战（不含连续 1 的数） · 困难 · 字节/快手

**题干**：给定一个非负整数 `n`，请统计 `[0, n]` 范围内，二进制表示中**不含连续两个 1** 的整数个数。例如 `3 = 11₂` 含连续 1，不合法；`5 = 101₂` 合法。

**示例**：`输入: n = 5` → `输出: 5`（合法的是 0、1、2、4、5）

**思路**：
- 直接枚举 `0 ~ n` 逐个检查，复杂度 O(n log n)，n 到 1e18 必爆。数位 DP 按**二进制位**逐位填数，复杂度只和位数有关。
- 把 `n` 转成二进制数组 `bits`。定义 `dfs(pos, prevOne, tight)`：
  - `pos`：当前填到第几位；
  - `prevOne`：上一位是否填了 1；
  - `tight`：之前填的位是否和 `n` 的前缀完全相同（贴着上界）。
- 当前位能填的上限是 `tight ? bits[pos] : 1`。如果 `prevOne && d === 1`，跳过（会出现连续 1）。递归下一位时，新的 `tight` 是 `tight && d === up`。
- 记忆化：`pos`、`prevOne`、`tight` 组成状态。`tight` 只有两种取值，直接一起存；也可以只在 `!tight` 时记忆化。
- **为什么正确**：`tight` 保证了不会枚举超过 `n` 的数；`prevOne` 保证不出现连续 1；每一位独立枚举，覆盖了所有合法数且不重不漏。相比暴力枚举，数位 DP 的复杂度只与 n 的二进制位数有关，n 到 1e18 也只有 60 位，非常适合大范围计数。

**代码**：
```javascript
function countNoConsecutiveOnes(n) {
  const bits = n.toString(2).split('').map(Number);
  const memo = new Map();

  // pos：当前位；prevOne：上一位是否为 1；tight：是否贴着上界
  function dfs(pos, prevOne, tight) {
    if (pos === bits.length) return 1;        // 填完，得到一个合法数
    const key = `${pos},${prevOne},${tight}`;
    if (memo.has(key)) return memo.get(key);

    const up = tight ? bits[pos] : 1;
    let res = 0;
    for (let d = 0; d <= up; d++) {
      if (prevOne === 1 && d === 1) continue; // 不能出现连续 1
      res += dfs(pos + 1, d, tight && d === up);
    }
    memo.set(key, res);
    return res;
  }

  return dfs(0, 0, true);                     // 统计包含 0
}

console.log(countNoConsecutiveOnes(5));  // 5
console.log(countNoConsecutiveOnes(3));  // 3（0,1,2）
console.log(countNoConsecutiveOnes(10)); // 8
```

**复杂度**：时间 O(位数 × 2 × 2)，空间 O(位数 × 2 × 2)，位数约为 log₂n。

**易错点**：
- `up = tight ? bits[pos] : 1`，不是恒为 1；`tight` 为真时不能超过 `n` 的当前位。
- 新的 `tight` 是 `tight && d === up`，不是 `d === bits[pos]`；当 `tight` 已经为 false 时，后续都自由。
- 结果是包含 0 的；如果题目要求正整数，返回前要 `-1`。
- `prevOne` 传的是当前填的 `d`，不是 `prevOne` 本身。
- `memo` 的 key 必须包含 `tight`，否则会把「贴上界」和「不贴上界」的状态混在一起。

**变体与追问**：
- 统计 `[a, b]` 区间：`f(b) - f(a-1)`。
- 不含连续相同数字（十进制）：把 `prevOne` 换成「上一位数字」，枚举 0~9。
- 数位之和 / 数字计数：在状态里增加「当前和」维度。

---

### C-429 时间空间复杂度的现场估算与取舍 · 模板 · 全公司通用

**题干**（场景）：机考没有实时反馈，写完代码才知道超时。请在动手前根据数据范围 `n` **反推**可接受的复杂度，并能在本机快速测出「1e8 次循环大概多久」，从而决定是写 O(n²) 暴力还是必须上 O(n log n)。

**思路**：
- 经验值（JS / Node，1 秒时限）：简单循环约 `1e8` 次；带函数调用 / 对象访问约 `1e7` 次；`Map`/`Set` 操作约 `1e6~1e7` 次。保守按 `1e7` 估算。
- 常用对照表：
  - `n ≤ 10`：O(n!) 全排列；
  - `n ≤ 20`：O(2ⁿ·n) 状压 DP；
  - `n ≤ 100`：O(n⁴) 勉强；
  - `n ≤ 500`：O(n³)；
  - `n ≤ 5000`：O(n²)；
  - `n ≤ 1e5`：O(n log n)；
  - `n ≤ 1e6`：O(n)；
  - `n ≤ 1e8`：O(log n) 或 O(1)。
- 空间：判题机通常给 256MB，JS 的 `Array<Array>` 开销大，`1e7` 个 `Number` 约 80MB，二维 `dp[n][n]` 在 n=5000 时约 200MB，已经危险。
- 取舍原则：**先保证不超时，再考虑空间**；能用一维滚动数组就不要开二维；能用 `Int32Array` 就不要用普通数组。
- 现场测速：用 `process.hrtime.bigint()` 包一段循环，估算本机每秒操作数，按比例折算到题目数据量。

**代码**：
```javascript
// 数据范围 -> 可接受复杂度（JS，1s 时限，保守估计）
const GUIDE = [
  [10, 'O(n!) 全排列'],
  [20, 'O(2^n · n) 状压 DP'],
  [100, 'O(n^4) 勉强'],
  [500, 'O(n^3) 区间 DP'],
  [5000, 'O(n^2) 普通 DP'],
  [100000, 'O(n log n) 排序/二分'],
  [1000000, 'O(n) 线性扫描'],
];
for (const [n, algo] of GUIDE) {
  console.log(`n <= ${n}: ${algo}`);
}

// 本机测速：1e8 次加法大约多少毫秒
const t0 = process.hrtime.bigint();
let sum = 0;
for (let i = 0; i < 1e8; i++) sum += i;
const ms = Number(process.hrtime.bigint() - t0) / 1e6;
console.log(`1e8 次加法: ${ms.toFixed(0)} ms, sum=${sum}`);

// 空间估算：n=5000 的二维 dp 约 25e6 个元素
const n = 5000;
console.log(`dp[${n}][${n}] 元素数: ${(n * n / 1e6).toFixed(1)}M`);
```

**复杂度**：测速代码本身 O(1e8)，只是本地估算，不会出现在提交代码里。

**易错点**：
- 不要用「我在 M1 上跑得很快」来判断判题机，判题机可能是共享 CPU，慢 3~5 倍很正常。
- `console.log` 在循环里会严重拖慢测速，测速时不要打印。
- 二维 `dp` 在 n=5000 时仅数字就 25e6 个，V8 的普通数组每个元素还有额外开销，很容易超 256MB。
- 递归深度超过 1e4 就可能爆栈，和复杂度无关，是独立的坑。
- 复杂度估算要算**常数**：同样是 O(n log n)，快排比 `Array.sort` 带比较器慢很多。

**变体与追问**：
- 用 `Int32Array` / `Float64Array` 替代普通数组，内存和速度都更好。
- 用 `node --max-old-space-size=512` 临时扩内存（本地可以，判题机不行）。
- 时间复杂度相同但常数差 10 倍时，优先选常数小的写法（如迭代代替递归、手写堆代替 `sort`）。

---

### C-430 笔试策略：部分分怎么拿与暴力怎么交 · 模板 · 全公司通用

**题干**（场景）：大厂机考按**测试点**给分，一道 100 分的题，暴力往往能拿到 30~50 分。请给出一个「暴力保底 + 优化冲满分 + 对拍验证」的实操模板，并说明时间不够时应该怎么交。

**思路**：
- **第一步：先写暴力**。不管最优解会不会，先把能过小数据的 O(n²) / O(2ⁿ) 版本写出来，保证有分。很多题 30% 的测试点 n ≤ 100，暴力足够。
- **第二步：再写优化**。用暴力当「标准答案」，随机生成小数据对拍，验证优化版本是否正确。对拍通过再提交优化版，避免「优化写挂得 0 分」。
- **第三步：分支提交**。如果优化只对部分情况有效，可以按数据范围分支：小数据走暴力（稳），大数据走优化（赌）。例如 `if (n <= 2000) return brute(a); return fast(a);`。
- **时间不够时**：直接交暴力，不要交一个没验证过的「半成品优化」；机考不看代码优雅，只看测试点通过数。
- 常见部分分特征：n ≤ 20 状压、n ≤ 1000 O(n²)、所有数非负、图是一条链、询问只有一次——这些特殊性质都可以单独写分支骗分。

**代码**：
```javascript
// 以「最大子段和」为例：暴力 O(n^2) 保底，Kadane O(n) 冲满分
function brute(a) {
  let best = -Infinity;
  for (let i = 0; i < a.length; i++) {
    let sum = 0;
    for (let j = i; j < a.length; j++) {
      sum += a[j];
      if (sum > best) best = sum;
    }
  }
  return best;
}

function fast(a) {
  let best = -Infinity;
  let cur = 0;
  for (const x of a) {
    cur = Math.max(x, cur + x);   // 以当前元素结尾的最大和
    best = Math.max(best, cur);
  }
  return best;
}

// 对拍：随机小数据比较暴力与优化
for (let t = 0; t < 2000; t++) {
  const n = 1 + Math.floor(Math.random() * 10);
  const a = Array.from({ length: n }, () => Math.floor(Math.random() * 21) - 10);
  if (brute(a) !== fast(a)) {
    console.log('WA', a, brute(a), fast(a));
    process.exit(1);
  }
}
console.log('对拍通过');

// 按数据范围分支：小数据暴力保底，大数据优化
function solve(a) {
  return a.length <= 2000 ? brute(a) : fast(a);
}
console.log(solve([-2, 1, -3, 4, -1, 2, 1, -5, 4])); // 6
```

**复杂度**：暴力 O(n²)，优化 O(n)；对拍 2000 组小数据在本机秒级完成。

**易错点**：
- 暴力也要处理边界：全负数时 `best` 初始为 `-Infinity`，不能初始为 0。
- 对拍数据要覆盖负数、0、单元素、全相同、极端值，否则测不出问题。
- 分支阈值不要拍脑袋写 `1e5`，要按暴力复杂度算：O(n²) 在 1e8 操作内，n 约 1e4 就到顶。
- 时间不够时优先交暴力，不要为了「看起来更优」交一个没跑过样例的版本。
- 多组输入时，暴力/优化的选择要对**每组**单独判断，不能只看第一组。

**变体与追问**：
- 对拍模板可以复用到所有题：改 `brute` 和 `fast` 两个函数即可。
- 如果暴力也写不出，先写「输出 0 / -1 / 空」的骗分版本，有些测试点会给边界分。
- 提交前用题目样例 + 自造边界（n=1、全 0、全负）各跑一遍，比盲目提交稳。

---
