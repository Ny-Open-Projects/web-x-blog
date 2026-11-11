# Python Stub 补全指南（DSA 多语言仓库）

## 背景
仓库 `/Users/Wang/Code/webfault-ai/dsa` 把 CSDN 博客的 DSA 题解（原作者的 TS）转成了 4 语言（go/java/python/ts）。
`python/<topic>/<problem_dir>/solution_*.py` 中仍有大量**空 stub**（内容如 `def solve(): pass` + 末尾 `if __name__ == '__main__': print(...)`），需要补全为**正确、可运行的 Python 实现**。

## 你的任务
补全分配给你的 chunk 里每一个 stub。

## 单文件操作流程
1. **先 Read 目标 .py**（Write/Edit 前必须 Read）。
2. 读它的 TS 参考：`ts/<topic>/<problem_dir>/<同名>.ts`（`.py`→`.ts`）。它提示**目标解法变体/思路**。
3. **关键**：TS 是自动转换生成的，**常常坏掉**（会见到 `// BROKEN`、`<` 被吞、循环边界错、逻辑错）。**绝不要照抄 TS**。理解算法后写**正确的标准 LeetCode 解法**。
4. 拿不准时读博客原文：chunk 条目里的 `blog` 字段（存在则有）。`notes` 类题目博客里通常有正确 Python，可直接改写。
5. **禁止 TS-isms**（写纯正 Python）：
   - `Map` → `dict`；`Set` → `set`
   - `arr.slice(a, b)` → `arr[a:b]`；`arr.push(x)` → `arr.append(x)`
   - `m.has(x)` → `x in m`；`m.get(k)` → `m.get(k)`；`m.set(k,v)` → `m[k]=v`
   - `===`/`!==` → `==`/`!=`；`let`/`const` → 普通变量；模板字符串 → f-string 或普通拼接
   - `.length` → `len(x)`；`x++` → `x += 1`
6. **树/链表题**：当函数操作节点时，在文件顶部内联定义 `TreeNode` / `ListNode`，使文件自洽可跑。
7. **函数名**：若 stub 是泛化 `def solve(): pass`，从 TS 函数名或题目推断正确名（如 `fib`、`firstMissingPositive`、`canPlaceFlowers`）并改掉 demo 调用；若 stub 已有正确名（如 `def reverseWords3(s):`）则保留。
8. 文件末尾必须有 `if __name__ == '__main__':`，用**示例输入**调用函数并打印结果，确保能无错运行。
9. **校验每个写出的文件**：用 managed python 运行
   `/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3 <file>` —— 不能崩，崩了就修。
10. **跳过**已经是非 stub 的真实实现（写前再确认）。已经有 16 个示例文件做完，别重做。
11. **只改分配给你 chunk 里的文件**，别动别的。

## 风格样例（Read 这 4 个对齐 house style）
- `python/dp/lc_509_斐波那契数/solution_5___5.py`  —— 干净翻译，正确函数名
- `python/sort/lc_41_缺失的第一个正数/solution_15___15.py`  —— 坏 TS → 正确算法，泛化 solve→真名
- `python/tree/lc_654_最大二叉树/solution_2_2_____2____.py`  —— 树题，内联 TreeNode
- `python/heap/lc_451_根据字符出现频率排序/solution_5_1____1_map____.py`  —— Map→dict

## concurrency 类（JS Promise/async）
JS `Promise`/`async-await` 题翻译成 Python `asyncio`：`async def` + `asyncio.wait_for(fn(), timeout=t/1000)` 实现超时拒绝（参考已完成的 `python/concurrency/lc_2637_有时间限制的_promise_对象/solution_1___1.py`）。

## 工作流
- 读 `_tools/chunks.json`：结构为数组，每项 `{index, items:[{py,ts,blog}, ...]}`。处理你被分配的 `index` 对应的 `items`。
- 逐条：Read py（若已是真实现则跳过）→ Read ts（+blog 若非空）→ 写完整 py → 运行校验。
- 分批做，边做边校验。

## 修复模式（fix_chunks.json —— 已破损但非 stub 的文件）
`_tools/fix_chunks.json` 里的文件**不是空 stub**，而是早先转译时带进了 TS 残留（典型：`Map`/`Set`/`Infinity`/`Array`/`undefined`/`.includes`/`.slice` 未转换、`__init__` 缺失、`str` 不可赋值、`guess` 未定义、循环边界错），导致 `python3 <file>` 运行时崩溃（NameError/TypeError/AttributeError）。
- **流程与 stub 模式一致**，差别只在起点：
  1. Read 该 .py，先 `python3 <file>` 复现崩溃，定位根因（看最后一行 traceback）。
  2. **保留题目标题与解法变体的意图**，但重写为纯正、可运行的正确 Python——不要照抄坏 TS。
  3. 判题逻辑必须正确（参考 TS 思路 + LeetCode 标准解法；`notes` 类有博客原文可改）。
  4. 树/链表题内联 `TreeNode`/`ListNode`；设计类题（`_design_*`、LFU/LRU/Trie/循环队列）要能实例化并跑通示例。
  5. 末尾 `if __name__ == '__main__':` 用示例输入输出，确保 `returncode==0` 且 stderr 为空。
- 校验同 stub 模式：managed python 逐文件运行，崩了就修。
- 只动你 chunk 里的文件；已完成/已正确的别重做。

## 结束汇报（简洁）
completed 数 / skipped 数 / 列未能 confidently 完成的文件（路径+原因）/ 发现的系统性问题。
