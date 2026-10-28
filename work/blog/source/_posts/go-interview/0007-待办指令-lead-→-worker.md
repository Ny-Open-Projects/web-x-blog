---
disableNunjucks: true
title: "待办指令（lead → worker）"
date: 2026-10-06 10:46:56
categories: [Go面试题集]
tags: [Go面试题集]
---

> 时间：2026-10-03 00:2x
> 背景：门禁体量上限已从 400 调整为 **650**。实测确认 400 物理不可达（6 个必填小节最低 ~505 字），
> **原口径是 lead 的判断错误，不是 worker 的问题。**

---

## 🔴🔴 最高优先级：v4 归并口径 + 自循环引用门禁（2026-10-05 lead 定，**先读这条**）

### 一、口径：同源 v3 卡**必须全量吸收**

`_pipeline/v4-rework/ALL.txt` 里这三列 —— **「主v3卡」+「同源其它v3主卡」+「同源deep伴随件」** ——
列出的**所有文件，内容必须吃进本卡正文**。**边界行只许指 v4 卡**（3/4 位阿拉伯数字 + 中文文件名）。

**依据**：`PLAN-REWORK.md` **类型 C** 明文「v3 因为字数限制拆成了「主卡 + 深挖」，**v4 该合并**」；
文首警示「部分深挖内容可能该合并进主卡（v4 不限字数，不需要「主卡讲结论、深挖讲推导」这种拆分）」；
用户原话「**内容变重可以的**」。

**⚠️ 别被下面这条误导**：本文档更下面的「不要为了压字数把 6 张合并回 3 张」是 **2026-10-03、专指 GMP 六卡、
禁止「为省字数而压缩」**，**不是** v4 的归并禁令。（已有 worker 把它推广到全批，导致 8 张卡外推，见下。）

**吸收 ≠ 复制粘贴**：改写成卡自己的讲解；原有实测数字保留并**标明来源口径**
（重跑了就写重跑条件；没重跑就写「引自 v3 卡实测，本卡未重跑」）。

### 二、为什么：自循环引用 = 死路

若 v4 卡 **A** 写「细节见 **B** 卡」，而 **B 的取代者正是 A**（task 2 已给 B 加「已被 A 取代」指针），
读者就是 `A → B → A`：**两边都读不到内容**。

判定规则：

| 情形 | 处理 |
|---|---|
| B 的取代者 **== A**（自循环） | **必须改**（把内容吸收进来，边界行改指 v4 卡） |
| B 的取代者是**第三方 C** | **允许保留**（`A → B →（B 的指针）→ C`，两跳可达） |

### 三、门禁脚本（**交付前必须跑，不跑 = 没做完**）

```bash
cd "/Users/Wang/Documents/面试/磁盘自带软件/go-interview"
python3 _pipeline/check-selfref.py            # 全库；退出码 0 = 干净
python3 _pipeline/check-selfref.py --selftest # 已知答案自测（6 用例）
```

它只报 **「自循环 × 外推语体」** 的交集（「本卡合并 v3 主卡 `136-…`」这类**取材声明**不算）。
**你为什么该信它**：脚本自带 6 条已知答案自测（用例全部取自人工判读过的真实句子），
且第一版被自测打回两次（漏判 `现用 v3 卡…一致`、整句判语体过宽）——**判据是迭代出来的，不是拍的**。

当前全库状态（2026-10-05 12:2x）：**68 处 / 8 张卡**（1327、1330、1331、1332、1337、1340、1341、1342）。

---



## 🔴 最高优先级：GMP 六张卡（`002`~`007`）仍未拆深挖

**这是全库最后的 6 个 error**，体量 1170~1515 字。

⚠️ **体量上限已从 650 上调到 700，但 GMP 这批上调救不了** —— 差 470~815 字，
必须**拆 `.deep.md`**，不是压缩措辞。

| 卡 | 当前字数 |
|---|---|
| `005-findrunnable-and-work-stealing.md` | 1515 |
| `007-gm-model-and-why-p.md` | 1495 |
| `006-preemption-and-sysmon.md` | 1376 |
| `003-g-blocking-preempt-and-stack.md` | 1286 |
| `004-m-p-binding-and-handoff.md` | 1220 |
| `002-g-signal-and-provenance-fields.md` | 1170 |

**拆法**（这批是 L3，命中深挖门槛条件 1 + 3）：

- **主卡**（≤700 汉字）保留：一句话总述 / 面试官视角 / 主问答 / 追问链 L1~L5 / 版本与兼容性 / 总结
- **`.deep.md`** 承接：思路与架构（mermaid + 文字说明）/ 方案取舍表 / 细节与核心 API /
  性能量级与实测数据 / 答题技巧 / 广度深度延伸 / 反问环节
- **`## ⚠️ 原文纠错` 不计入主卡字数**，但单节 ≤150 字（`002` 那个纠错节有 345 字，需压缩）

**这 6 张原本就拆对了 6 个主题**（g 的信号字段 / 阻塞与栈 / m-p 绑定 / findRunnable 与偷取 /
sysmon 抢占 / GM 模型），**不要为了压字数把 6 张合并回 3 张**。

**接手方式**（任一空闲 worker 均可）：
1. 先跑 `validate.py` 确认当前 error 归属，别动别人的卡
2. 改号前用 `checkdup.py --allocate N` 申请
3. 每拆完 1~2 张就跑一次 `validate.py --strict` 自检

---

## ✅ 已完成，无需再动

| 范围 | 产出 |
|---|---|
| 08-14/08-16 GMP、09-25+07-6 sync/Gin | `002-007`、`201-207` |
| 07-10+07-8 mergo/Gin、10-8、10-19/10-20、10-6 | `101-109`、`301-304`、`401+`、`601-608` |
| 10-7+10-9 map/slice 并发 | `501-508` |
| 6-2 context、6-9 channel | `801-804`、`705-708` |
| 11-8 逃逸分析、8-8 GC 流程 | `701-702` |

---

## ⚠️ 路径速查（照抄，别手敲）

```
项目根  /Users/Wang/Documents/面试/磁盘自带软件/go-interview
规范    <项目根>/_pipeline/SPEC.md
待办    <项目根>/_pipeline/TODO-worker.md
纠错台账 <项目根>/_pipeline/ERRORS.md
卡片    <项目根>/target/go/
```


### 1. 源文件名**永远以 `state.json` 为准**，不要凭题面推测

lead 也可能给错文件名（曾编造 `10-11 gin框架的性能如何`）。开工第一步：

```bash
cd "/Users/Wang/Documents/面试/磁盘自带软件/go-interview"
PY=/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3
$PY -c "
import json
st = json.load(open('_pipeline/state.json'))
for t in st['tasks'].values():
    if t['status'] in ('running','pending'):
        print(f\"{t['id']:>7} {t['bytes']:>6}B {t['tier']:>2} {t['title']}\")
" | head -20
```

**若题面给的文件名不存在、或与 `state.json` 不符 → 立刻停下报告，不要猜、不要凑合。**

### 2. `source/` 里有**同名重复录制**文件

如 `10-7` / `10-8` 各有两份（仅时间戳不同）。`queue.py init` 已自动去重，
**按 `state.json` 给的 `source` 路径取文件**，不要自己 glob。

### 3. 接任务前先查重（⚠️ 脚本查不出主题重复，必须你人工做）

已发生：两个 worker 各做了 `16-5` 单例题（DCL / sync.Once），
**编号不冲突，`checkdup.py` 报"三项全 ✓"，但内容重复**。

**这是脚本的能力边界**——试过两种自动方案都不行，别再试：
- ❌ 按「段落号相同」判重 → `002-g-signal`(第36段) 与 `114-p-status`(第36段)
  起始段号相同但**来自不同源文件、主题完全不同**
- ❌ 按「标题分词指纹」判重 → 中文标题无空格，2 字滑窗取到 `懒汉/汉式/式单`
  这种位置碎片，同题不同措辞就漏

**所以开工前请手工做两步**：

```bash
cd "/Users/Wang/Documents/面试/磁盘自带软件/go-interview"
PY=/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3

# ① 看有没有同源文件的任务正在 running
$PY -c "
import json
st=json.load(open('_pipeline/state.json'))
for t in st['tasks'].values():
    if t['status']=='running': print(' ', t['id'], t['source'])
"
# ② 看你选的源文件是否已被别人做过
ls target/go/ | head -50
```

**发现同题 → 停下报告，别硬做。** 处置：由 lead 裁决谁让，
让的一方**整张不做**（不要换个措辞再做一遍），把已实测的数据交给对方即可。

> 判据：**同源文件 + 同角度 = 重复；同源文件 + 不同角度 = 正常分卡**（如 002~007）。

### 4. 体量与质量口径

- 主卡 **≤650 汉字**（不含代码块，不含 `## ⚠️ 原文纠错` 小节）
- `## ⚠️ 原文纠错` 自身**控制在 150 字内**
- **L3+ 允许且应该出 `.deep.md`**，超出部分挪进去
- **禁止**为凑字数砍掉：追问链停档判据 / 版本与兼容性表 / `[实测]` 的验证方式
- **代码必须从卡内提取后重跑核对**——已有 worker 因此返工 3 次，这是硬要求
- 测试代码本身有 bug 时，**标注「数值会波动」而不是给一个稳定的假数字**

### 5. 编号分配：**必须用脚本申请，不要自己拍**

⚠️ **已发生三次同号并存**（601-604 两批占用、701 段 2 个主卡并存、801 组重排）。
**根因是各 worker 各自拍号段。** 现在改为申请制：

```bash
cd "/Users/Wang/Documents/面试/磁盘自带软件/go-interview"
PY=/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3
$PY _pipeline/checkdup.py --allocate 4     # 打印 4 个当前未占用的编号，直接用
```

**开工前先申请，拿到号再写卡。** 不要再按「600 段」「700 段」这种固定区间去猜。

### 6.1 收工前**必须**跑 `checkdup.py`（不跑 = 没做完）

⚠️ **已发生 4 次同号并存**（601-604、701、110-111）。**每一次都不是"忘了申请"，
而是"申请了但没跑门禁确认"** —— `--allocate` 只是给你看空闲号，
**真正的门禁是收工前的 `checkdup.py` 默认模式**。

```bash
cd "/Users/Wang/Documents/面试/磁盘自带软件/go-interview"
PY=/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3

# ① 开工前：申请号
$PY _pipeline/checkdup.py --allocate 4

# ② 收工前：必须 0 error  ← 漏了这步，你的号可能已被别人占
$PY _pipeline/validate.py     # 内容门禁 → 0 error
$PY _pipeline/checkdup.py     # 编号门禁 → 冲突/孤儿/坏引用 全清
```

**如果发现撞了**（刚落盘，别的 worker 也用了同一个号）：
- **先在汇报里说明**，不要自己去改别人的文件
- 规则：**先落盘的批次保留原号，后落盘的让号**；改号后必做
  ① 改 H1 标题编号 ② 同步全库「见 NNN 卡」引用 ③ 改 `.deep.md` 挂靠名
- 让完号**立刻告诉 lead**，因为另一方也要同步自己的引用

### 6.2 撞号了怎么办（lead 已用此规则裁决两次）

| 情况 | 裁决 |
|---|---|
| 两批同号 | **先派批次保留原号，后派批次整体移到新段** |
| 同批次内多张撞号 | 保留**形成体系、最先落盘**的那组（同主题互相引用的算一组） |
| 改号后必做 | ① 改 H1 标题里的编号 ② 同步全库「见 NNN 卡」交叉引用 ③ 改 `.deep.md` 的挂靠名 |

**已经这么处理过的先例**（不要重复劳动）：
- `601-604` 冲突 → slice 那批已改到 `505-508`
- `701` 冲突 → **701 保留给 `escape-analysis`**（先派批次），
  context 整组已改到 **`801-804`**（`802` err-sentinel、`803` cancel-leak、`804` WithValue）

**所以：channel 底层那批（`705` 起）不要往 801-804 靠，那段已占。**
继续用 `checkdup.py --allocate` 申请即可。

### 6. 收工前**必须**逐项自查（不查 = 没做完）

⚠️ **已发生**：worker 2 的 `110`/`111` 漏了闭合围栏，门禁报了 error 但 worker 收工前没看，
lead 手工补的围栏。**这种事不该由 lead 兜底。**

```bash
cd "/Users/Wang/Documents/面试/磁盘自带软件/go-interview"
PY=/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3

# ① 围栏自检（最快，抓漏闭合围栏）
for f in target/go/xxx*.md; do
  n=$(awk '/^```/{c++} END{print c%2}' "$f")
  [ "$n" != "0" ] && echo "✗ 围栏未闭合: $f"
done

# ② 内容门禁：14 条 → 必须 0 error
$PY _pipeline/validate.py

# ③ 编号门禁：冲突 / 孤儿 / 坏引用 → 全清
$PY _pipeline/checkdup.py
```

**汇报前必须自己先跑 ② ③，并把命令输出贴进汇报。**
「我这批 0 error」这句话**必须来自刚跑出来的命令输出，不能是印象**。

`checkdup.py` 修法：

| 报错 | 修法 |
|---|---|
| `冲突 NNN：2 个主卡并存` | 先在汇报里说明（**别改别人的文件**）；先落盘方保留，后落盘方让号 |
| `孤儿深挖：X.deep.md` | 补上 `X.md`，或删掉这个深挖 |
| `引用了不存在的「见 NNN 卡」` | 要么补出那张卡，要么**删掉该引用**（不要留占位） |
| `代码块未闭合` | 用上面的 `awk` 一行命令定位，补上缺失的 ``` |

### 7. 收工前**必须**标记任务状态（否则任务僵死）

⚠️ **已发生 6 次**：worker 领了任务、写了卡，但**没调 `queue.py done`**，
任务永久僵在 `running` 状态，后续没人认领，队列看起来"在跑"实际没动。

**只要你有产出，就必须标记**：

```bash
cd "/Users/Wang/Documents/面试/磁盘自带软件/go-interview"
PY=/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3
$PY _pipeline/queue.py done <任务ID> --cards "a.md,b.md"
```

**如果没做完**（中途被叫停 / 出错 / 上下文不够）：
```bash
$PY _pipeline/queue.py fail <任务ID> --reason "原因"
```

> 判据：**你手上有产出却没标记 = 任务白干**（下次会有人重做一遍）。
> 哪怕只完成 1 张卡，也要 `done` 并如实写 `--cards`。

### 8. 纠错台账

`_pipeline/ERRORS.md` 已累积 **100+ 条**实测坐实的纠错 + **反纠错清单**（「不要改」的那些）。
新纠错按其格式追加（原文说X → 实际是Y → 依据），**只加不改已有条目**。
**发现原文其实是对的，也要单列「反纠错」并写明依据** —— 这类知识比多纠一条错更稀缺。
避免重复劳动——**先读一遍**，尤其你要处理的题材可能已有相关纠错。

---

---

## 🔴 并行度：不要凭直觉改（2026-10-03 撞过 429）

**实测数据**（整夜 369 篇语料）：

| 并行 | 结果 |
|---|---|
| **3** | 4 个 worker **同时** `429 额度已用尽` 全部失败 |
| **1** | 安全 |

**`queue.py` 的 `MAX_PARALLEL` 已设为 1、`COOLDOWN_SEC` 提到 180。**
**不要再为了提速调高它** —— 提速的正确方向是**缩小单次任务规模**（每 agent 2 篇），
不是加并发。没有数据支撑的并行度调整 = 拍脑袋。

**如果确实要提速，按阶梯来，一次只升一档，且必须观察到「一批 0 个 429」才升下一档**：

| 档 | 并行 | 每 agent 篇数 | 升档前置条件 |
|---|---|---|---|
| 1 | 1 | 2 | ✅ 当前（429 后已验证安全） |
| 2 | 2 | 2 | 连续 3 批 0 个 429 |
| 3 | 3 | 2 | 连续 6 批 0 个 429 |

**降档则立即**：任何一个 429 → 立刻回退一档并观察，不要重试同一档。

---

## 🔴 并行协作：不抢写正在被作业的文件

**2026-10-03 实操教训**：我派 worker 去压 `159` 的字数，**另��个 worker 正在写它**。
worker 自己发现并停手，判据是两条独立证据：

```
ls -lT  →  mtime 18:55:47，我第一条命令跑于 18:55:53   （6 秒前刚被改过）
validate →  报 752 字 而不是我给的 775 字              （作者已压掉 23 字，正在作业）
```

**两条独立证据互相印证 → 不插手。** 换成「mtime 变了」单条不够（可能只是 touch）。

### 判据（下次照此判断）

| 现象 | 判断 |
|---|---|
| mtime 在**几分钟内**变化 | **正在被写，别碰** |
| validate 报的数**与别人给你的数不符** | **对方正在改** |
| 文件数在变（deep 卡刚出现/消失） | **对方正在补配套文件** |

### 最重要的一条：**别等**

发现对方在写，**不要「等他收尾再接手」** ——
那会让自己的任务边界变模糊，而且**对方本人压更高效**（明细可直接下沉到 deep，你压要先挪再压）。

**正确做法：把自己的任务做完，做不到的当场报告，由 lead 重新指派。**

---

## 📌 决策（2026-10-03 lead 拍板，worker 无需再问）

### ①纠错节超 250 字 = **warn，不压**

**判定：纠错节的字数超线一律不压，「依据」列不可删。**

理由：依据（源码 `文件:行号` + `[实测]` 输出）**是这张卡不可替代的价值**。
压到 250 以内只能靠砍依据或砍整条纠错 —— 两者都是**自废武功**。

**正确做法**：纠错太多时**合并同类项**（如「原文说 A 实际 B」与「原文说 C 实际 B」
可合成一条），或把次要条目**下沉到 `.deep.md`**（deep 不受此线约束）。

> 这条已写进 `validate.py` 的 warn 文案里，**看到 warn 直接忽略，不必报告**。

### ② 语速纪律：报错就报，别自己硬修

- **前提被推翻 → 立刻停下报告**（不要将错就错硬写）
- **文件被抢 → 停下报告**（见「不抢写正在被作业的文件」）
- **R2/R3 降级 → 判了就报**（不要为了凑数硬出）
- **只有「压字数」可以自己动手**，且不可动必填小节

---

## 🔴🔴 验证语言版本语义：禁止用 `go run xxx.go`（worker 2 抓到，影响整类结论）

**现象**（lead 已独立复现，同一份代码、同一个目录、`go.mod` 写 `go 1.21`）：

```
go run .          →  3 3 3    ← 读 go.mod 的 go 指令（包模式）
go run main.go    →  0 1 2    ← 无视 go.mod（文件模式）
go build . 后执行 →  3 3 3
```

**没有任何报错或警告。** 同一份代码、同一台机器，只因命令写法不同就得出**相反的结论**。

**根因**：文件模式（`go run xxx.go`）**不构建 module**，因此不读 `go.mod` 的 `go` 指令，
`-lang` 这条链路是断的。包模式（`go run .` / `go test`）才走 module。

**佐证**：
```bash
$ go build -gcflags=all=-lang=go1.21 .
internal/strconv/itoa.go:203: cannot range over 4 ... requires go1.22 or later
  (-lang was set to go1.21; check go.mod)      ← 说明 -lang 由 go.mod 推导
```

### 硬要求

> **凡结论依赖 `go.mod` 语言版本的实验（loopvar / 泛型 / range-over-func / min-max-clear / AsType 等），
> 必须用 `go run .` 或 `go test`，禁止用 `go run xxx.go`。**

**更严的一条（worker 1 也踩过）**：
> **同目录改 `go.mod` 无效** —— 必须用**两个独立 module** 对照。
> 否则两个版本可能命中缓存或默认值，**输出完全一样却不报错**。

### 判据

**验证方法本身的正确性，要和被测结论一样被验证**：
- 改 `go.mod` 后**必须确认编译器真的换了语言版本**（看 `-lang` 是否生效 / 两次输出是否真的不同）
- 若两次实验输出**完全一样**，**先怀疑实验没生效**，不要直接写「语义没变」

> **这是本流水线第 4 次「测试没报错 ≠ 测试有效」**：
> ① 门禁反向测试注入位置错（在纠错节之后，被 split 切掉）
> ② `B/op` 与 `allocs/op` 自相矛盾时没怀疑 setup 摊薄
> ③ 同目录改 go.mod 跑出版本栅栏（两个输出一模一样）
> ④ `go run xxx.go` 静默用新语义，得出与 go.mod 相反的结论
>
> **规律：凡"让两种情况产生差异"的实验，先确认差异真的产生了。**

---

## 📏 字数口径：**只认 `validate.py`，自己数会多算 40~60 字`（worker 2 指出，省所有 worker 3~5 轮）

**权威口径**（`validate.py` 的实际算法）：

```python
n = cjk_count(strip_section(strip_section(body, "⚠️ 原文纠错"), "关键代码"))
```

它**排除两节**：
1. `## ⚠️ 原文纠错` —— 补充证据，不是必填内容
2. `## 关键代码` —— 里面是**代码的附件**（这段代码跑出什么），不是可背的知识点
3. 另外**所有围栏内的代码块**本身也不计入

> 排除「关键代码」的理由（实测各节平均字数）：
> 主问答 156 / 面试官视角 120 / 追问链 103 / 版本 65 / 总结 48 / 总述 38
> → **6 个必填小节合计约 530 字**，700 上限的余量主要被代码附件吃掉。

**⚠️ 自己用 `cjk_count` 数会系统性地多算 40~60 字**，
worker 2 估计自己**有 4 轮压缩是在追一个不存在的超标**。

### 正确做法

```bash
# 唯一权威：问门禁，别自己数
$PY _pipeline/validate.py --file target/go/<你的卡>.md
```

**汇报字数时也写「门禁口径 ≤700」，不要写自己算的数** ——
否则 lead 复核时会以为超标，白查一遍。

> **同族教训**（今天第 6 次「看起来是 A 问题其实是 B 问题」）：
> 门禁排除代码节这个决定是 **18:12 lead 做的**（当时贴顶率 40% → 8%），
> 但**没在指令里说「所以别自己数」** —— 于是每个 worker 都在追一个不存在的超标。
> **改了行为就要说，否则等于没改。**

---

# ⚠️ 2026-10-04 11:00 起：改用 **SPEC-v4**（本文档其余部分为 v3，逐步作废）

**用户裁定**：
> 「不太适合新手，**不要限制字数**，要**人类面试可读可背**」
> 「全部改成中文文件名」

## 规范以 `SPEC-v4.md` 为准

| | v3（旧） | **v4（现行）** |
|---|---|---|
| 文件名 | `166-binary-tree-equality.md` | **`166-判断两棵二叉树是否相等.md`** |
| 字数 | ≤700 汉字 | **不限，但不许有废话** |
| 风格 | P5/P6/P7 分档、红旗、惊艳点 | **讲解式**，删掉所有元标签 |
| 结构 | 6 个必填小节 | **7 段式**：先说结论 / 完整代码 / 逐行讲透 / 实测验证 / 原文哪里错了 / 面试怎么答 / 面试官可能接着问 |

## v4 门禁

```bash
$PY _pipeline/validate-v4.py --file target/go/<卡>.md    # 单张
$PY _pipeline/validate-v4.py                            # 全库
```

**v3 的 `validate.py` 对 v4 卡会报错（查 6 小节 + 700 字），那是预期的** —— v4 卡只跑 `validate-v4.py`。

## v4 的八条硬要求

1. **面向新手**：假设读者没做过这道题，要有铺垫
2. **有推导过程**：不要直接给结论，要让人看懂**怎么想到的**
3. **代码是主体**：完整可 `go run`，**关键行有中文注释**（说明"为什么这么写"）
4. **讲解围绕代码**：「逐行讲透」要指着代码讲
5. **实测数据能复现**：给命令 + 输出 + 量级
6. **「面试怎么答」是一段能直接背的话**（60~120 秒讲完，不要 bullet）
7. **「面试官可能接着问」**：2~4 个，附答案要点，**不要分档、不要表格**
8. **不限字数，但每句话删掉后读者会少懂一点东西** —— 否则删

## 不变的红线

- 代码必须 `go run` 通过；**从卡内提取后重跑 + `diff` 逐字比对**
- 所有数字实测且可从卡内代码复现
- 原文纠错必须有依据（源码行号 / 实测命令）
- **结论依赖 `go.mod` 语言版本时必须 `go run .`，禁止 `go run xxx.go`**
- 不确定的标 `[存疑]`


---

# 🔴 知识点勘误（lead 落点被 worker 实测证伪，2026-10-04 补）

> 背景：lead 在派 5-12 时给出的落点是「空结构体字段在**最后一个字段时不占空间**，作为**非末位字段可能占 1 字节对齐填充**」。
> worker 用实测**证伪**，方向正好相反。lead 已独立复现确认。**后续一律以本节为准。**

## 一、零尺寸字段的位置效应（正确版）

**规则**：结构体**以零尺寸字段结尾**时，编译器先 `size++`（补 1 字节），**再按结构体自身对齐向上取整**。
源码：`cmd/compile/internal/types/size.go`，issue 9401。

```
{int8;  E}          = 2      ← 末位：1 数据 + 1 填充
{E;  int8}          = 1      ← 首位：无填充
{int16; E}          = 4      ← 2+1=3 → 对齐到 2 的倍数
{int32; E}          = 8      ← 4+1=5 → 对齐到 4 的倍数
{int64; E}          = 16     ← 8+1=9 → 对齐到 8 的倍数
{E;  int64}         = 8
{int64; E; int64}   = 16     ← 中间位：与无 E 完全相同
{int64; int64}      = 16     ← 对照
```

**一句话**：**末位有害，首位/中间无害。**（与 lead 原落点相反）

**原因**：若允许末位零尺寸字段的地址等于结构体末尾，`&s.哨兵` 就可能与堆里紧邻的下一个对象同地址，取地址会「凭空造出」一个指向别人的指针。

**相关**：436 号卡（`_ [0]func()` 哨兵）讲的同一件事，那里的结论「**哨兵放最前**」是对的，可交叉引用。

## 二、`map[T]struct{}` 并不比 `map[T]bool` 省内存

流传极广的说法「用 `map[T]struct{}` 省内存」——**实测证伪**。

本机 go1.26.5，`SetGCPercent(-1)` + 预热后量 `HeapAlloc`：
```
map[int]struct{}  N=300000  = 9458432 B  (31.53 B/entry)
map[int]bool      N=300000  = 9458432 B  (31.53 B/entry)
差值 = 0 B
```
换 uint8 / int32 / int64 / string 做 key，结论一致——内部存储按 size class 向上取整，value 那 1 字节被抹平。

**所以选 `struct{}` 的理由是「语义」（值不携带信息），不是省内存。**
（worker 另测报 9458480 B，与 lead 的 9458432 B 差 48 B，属测量噪声，结论「差值为 0」一致。）

## 三、教训

- **lead 的落点也可能错**：worker 遇到与自己实测不符的 brief，**以实测为准**，并在回报中明确指出——这次 worker 做对了，且没把错的写进卡。
- **报数前先看 mtime**：lead 曾因在 worker 定稿前读取而误判 md5 不符。验收要等对方报「已落盘」。
- **测「可赋值性比较」别引入接口**：`any(p) == any(an)` 比的是「动态类型+值」，类型不同必 false；要测 `p == an`（不装箱）。

---

# 🔴 第 7 章起：外部依赖的拉取方式（2026-10-04 lead 实测）

## 问题

本机 `/Users/Wang/go/pkg/mod` **写入被拒**，任何拉取新依赖的操作都会失败：

```
go: writing stat cache: mkdir /Users/Wang/go/pkg/mod/cache/download/github.com/robfig: permission denied
go: github.com/robfig/cron/v3@latest: ... permission denied
```

**注意**：这不只是「没网」——本地 cache 里虽然有 `gin-gonic` / `gorm.io` 的源码，但 `go mod tidy` 需要写 `.lock` 文件，同样会被拒。所以 **gin 也拉不动**。

## 解法（lead 已实测跑通）

```bash
export GOMODCACHE=/tmp/gomodcache          # 换成可写目录
export GOSUMDB=off                          # 关掉 sumdb 校验（否则写 sumdb 缓存也被拒）
export GOFLAGS=-mod=mod
export GOPROXY=https://goproxy.cn,direct    # 国内镜像，已在本机 go env 配好
```

三条缺一不可：
- 只换 `GOMODCACHE` → 卡在 `open /Users/Wang/go/pkg/mod/sumdb/... : permission denied`
- 不设 `GOSUMDB=off` → 同上
- 不设 `GOFLAGS=-mod=mod` → 可能拒绝改 go.mod

## 验证方式

```bash
mkdir -p /tmp/deptest && cd /tmp/deptest && printf 'module deptest\ngo 1.26.5\n' > go.mod
go get github.com/robfig/cron/v3@latest && echo OK
```

## 写卡要求

- **卡里要给读者可复现的 `go.mod`**（含 `require` 行 + 版本号）
- **卡里不要写这套沙箱环境的设置**——那是我们的环境问题，读者本机不需要
- 版本相关的结论（如 gorm 事务行为、gin binding 规则），**注明依赖版本号**

## 已知可用依赖

| 库 | 状态 |
|---|---|
| `github.com/gin-gonic/gin` | 需按上述方式拉取（cache 里有源码但关联不上） |
| `gorm.io/gorm` + `gorm.io/driver/sqlite` | 同上 |
| `github.com/glebarez/sqlite` | 纯 Go 驱动，**不需要 cgo**，推荐用于「不依赖外部数据库」的卡 |
| `github.com/robfig/cron/v3` | lead 已实测下载成功 |

---

# ✅ 已修：门禁的省略号误报（2026-10-04，worker 报的坑）

## 原来的坑

`validate-v4.py` 的省略号检查写的是 `"..." in code`，**太宽**——Go 里 `...` 有三种**合法**用法，全被当成「省略号占位」告警：

| 合法用法 | 例子 |
|---|---|
| 变参声明 | `func f(a ...string)` |
| 展开 | `f(args...)`、`append(a, b...)` |
| 数组长度推断 | `a := [...]int{1,2,3}` |

**后果**：166 卡（第一张 v4 样例卡）从第一天起就挂着 2 条**假告警**；worker 写变参函数的卡时被迫绕开三点号（改切片传参 + 手工拼 `cmd.Args`），白费返工。

## 修法

先摘掉三种合法用法，再看剩余是否还有裸的 `...`：

```python
_ELL_VARARG = re.compile(r"\.\.\.\s*[A-Za-z_\[\]\*]")   # 变参声明 a ...T
_ELL_EXPAND = re.compile(r"[A-Za-z_0-9\)\]]\.\.\.")     # 展开 f(xs...) 必须紧贴
_ELL_ARRLEN = re.compile(r"\[\s*\.\.\.\s*\]")           # 数组 [...]T{...}
```

用 15 条用例回归过（合法 8 条 / 占位 7 条），全对。

**注意 ② 不允许中间有空格**：`f(xs...)` 合法，`f(xs ...)` 本身才是语法错——所以带空格的 `return ...` 仍会被正确判为占位。

## 现在的结论

- **正常写变参函数，不必再绕**。写 `func f(a ...string)` / `f(xs...)` 不会再告警。
- 真正的占位（裸 `...`、`// ...`）**仍会告警**。
- 修完全库 **warn 归零**（38/38 PASS, error 0, warn 0）。

---

# 🔴 版本栅栏的默认规则：**切换点在 `go.mod` 的 `go` 行，不在工具链**（2026-10-04 四数据点确认）

## 规律

**Go 1.21 起，语言特性/运行时行为的生效版本由 `go.mod` 的 `go` 行决定，而不是你装的工具链版本。**

装 go1.26.5 但 `go.mod` 写 `go 1.21`，**拿到的仍是 1.21 的语义**。

## 四个独立实测数据点（都验证过）

| 特性 | 翻转版本 | `go.mod=go1.21` | `go.mod=go1.26` |
|---|---|---|---|
| 循环变量 `defer` 捕获（481） | 1.22 | `3 3 3` | `0 1 2` |
| 循环变量闭包捕获（517） | 1.22 | `[10 ×10]` | `[0..9]` |
| `time.After` 定时器回收（523） | 1.23 | 堆 ≈50 MB（不回收） | 堆 ≈0 MB |
| `ServeMux` 的 `{name}` 通配（524） | 1.22 | `404` | `200 id=42` |

## 实操含义

**要做版本栅栏对比实验时**：
```bash
# 正确做法：同一份 main.go，只改 go.mod
printf 'module x\ngo 1.21\n' > go.mod && go run .   # 旧语义
printf 'module x\ngo 1.26\n' > go.mod && go run .   # 新语义

# ⚠️ 不要用切换工具链来对比——那样测不出差异，或者测出的差异不是你想的那个
```

**写卡时**：如果结论依赖语言版本，**必须写明「依赖 `go.mod` 的 `go` 行」**，而不是只写「Go 1.N 起」。后者会让读者以为升级工具链就够了。

## 例外

- **标准库 API 的新增**（如 `math.MaxInt` 1.17、`slices` 1.21）不受此约束——那是「包是否存在」，由工具链决定
- 本条管的是**同一份代码在不同语言版本下语义不同**的情况

### ⚠️ 边界（2026-10-04 worker 实测证伪 lead，务必看）

**「go 行门控」只管语言语义与部分 `GODEBUG` 默认值，不管【编译进工具链的运行时能力】。**

反例（gpB 实测 + lead 独立复现）：**异步信号抢占**（Go 1.14 起）**不受 go 行控制**

```
纯计算死循环 + GOMAXPROCS=1 + 看门狗：
  go.mod=go 1.13 → 被抢占
  go.mod=go 1.21 → 被抢占
  go.mod=go 1.26 → 被抢占
  负对照 GODEBUG=asyncpreemptoff=1 → 卡死【未被抢占】✓
```

**它的开关是 `GODEBUG=asyncpreemptoff`，不是 go 行。** 因为异步抢占是**编译进二进制的运行时能力**，一旦工具链 ≥1.14 就具备，与模块声明的语言版本无关。

**判断口径**（写卡前先问自己，**四层**）：

| 类别 | 例子 | 谁决定 |
|---|---|---|
| ① **语言语法/语义** | `for range int`（1.22）、loopvar（1.22）、timer 回收（1.23）、ServeMux 通配（1.22） | **`go.mod` 的 go 行** |
| ② **编译器内建 + `unsafe` 新函数** | 内建 `min`/`max`/`clear`（1.21）、`unsafe.String`/`StringData`/`SliceData`/`Add`/`Slice`（1.20） | **`go.mod` 的 go 行**（⚠️ 与 ① 同栏！） |
| ③ **普通 stdlib 包/函数** | `slices`（1.21）、`errors.Join`（1.20）、`math.MaxInt`（1.17） | **只看工具链版本** |
| ④ **运行期行为/能力** | 异步信号抢占（1.14）、调度器新行为 | **只看工具链版本** + 找 `GODEBUG` 开关 |

**第 ② 类最容易判错**：`unsafe.String` 看着像「stdlib 新函数」，但它由编译器特殊处理，**受 `go` 行拦**。实测（工具链 go1.26.5、`go.mod` 写 `go 1.19`）：
```
① unsafe.String     → requires go1.20 or later (-lang was set to go1.19; check go.mod)
② built-in min      → requires go1.21 or later (-lang was set to go1.19; check go.mod)
③ slices.Contains   → 编译通过      ← 负对照：证明这份 go.mod 没把环境整体降级
④ errors.Join       → 编译通过      ← 同上
⑤ for range int     → requires go1.22 or later (-lang was set to go1.19; check go.mod)
```

**做栅栏实验前先跑负对照**：
- 验证「`go` 行拦住了它」→ 同环境放一个**普通 stdlib 新包**（如 `slices`）进去，它应该**能过**；否则说明是你的环境问题
- 验证「某个 `GODEBUG` 开关控制它」→ 加上开关后行为应该**翻回去**（如 `asyncpreemptoff=1` 会让死循环卡死）

## 相关

- `GODEBUG` 可以强制覆盖：`GODEBUG=httpmuxgo121=1`、`GODEBUG=asynctimerchan=1`——用于验证「旧语义确实是那样」，是很好的旁证手段

---

# 🐬 第 12 章（MySQL 专题，64 篇）：环境与写卡规范

## 一、MySQL 环境（**已就绪，直接用**）

本地 **MySQL 8.0.33**，专用实例已配好，**用脚本管理，别自己起**：

```bash
cd "/Users/Wang/Documents/面试/磁盘自带软件/go-interview"
bash _pipeline/mysql-env.sh check      # 检查连接（默认）
bash _pipeline/mysql-env.sh start      # 启动（幂等；datadir 丢了会自动 init）
bash _pipeline/mysql-env.sh sql "SELECT 1"        # 执行一条 SQL
bash _pipeline/mysql-env.sh file x.sql            # 执行一个 SQL 文件
bash _pipeline/mysql-env.sh reset                 # 重置 mtdemo 库
bash _pipeline/mysql-env.sh vars                  # 打印关键变量
```

**连接参数（固定）**：
| 项 | 值 |
|---|---|
| socket | `/tmp/mtdemo-mysql/my.sock` |
| port | `13307` |
| user | `root`（无密码，**仅本机测试**） |
| db | `mtdemo` |

**实测环境的关键变量**（写卡时可直接引用）：
```
log_bin=1  binlog_format=ROW  sync_binlog=1  innodb_flush_log_at_trx_commit=1
innodb_buffer_pool_size=128MB  innodb_page_size=16384  innodb_log_file_size=48MB
slow_query_log=0  long_query_time=10  performance_schema=1
default isolation = REPEATABLE-READ
```
→ **binlog 已开**（redo/binlog 系列卡可实测）、**page_size=16KB**（索引结构卡可实测）、**performance_schema=1**（性能卡可用）

⚠️ **datadir 在 `/tmp` 下，重启机器会丢** —— 丢了跑一次 `bash _pipeline/mysql-env.sh start` 即可（会自动 init + 建库）。

## 二、写卡规范（第 12 章的差异）

**七段式结构不变**，但「完整代码」段变成 **SQL 脚本**（DDL + DML + 查询/EXPLAIN），要求：

1. **SQL 要能整体执行**：从空库开始跑一遍不报错。**开头建议 `DROP TABLE IF EXISTS`**，结尾不需要清理（`reset` 会重置）
2. **可重复执行**：同一份 SQL 跑两遍结果一致（**确定性**）。涉及时间/自增 ID 的地方要**归一化**（如只断言「ID 递增」而不写死具体值）
3. **涉及会话变量要显式 `SET`**：如测隔离级别用 `SET SESSION TRANSACTION ISOLATION LEVEL ...`，**别依赖全局默认**
4. **实测要贴真实输出**：`EXPLAIN` 的 `type`/`key`/`rows`/`Extra`、`SHOW ENGINE INNODB STATUS` 的关键段、`SHOW VARIABLES` 的值——**要能从卡内 SQL 复现**
5. **版本栅栏**：MySQL 8.0 与 5.7 差异大（如**查询缓存被移除**、**自增 ID 持久化**、**默认隔离级别**）；写法用四层口径，**注明「MySQL 8.0.33 实测，5.7 行为可能不同」**
6. **代码块语言用 ` ```sql `**（门禁已支持；` ```go ` 也接受，但第 12 章主块应是 SQL）

**门禁**：`validate-v4.py` 必须 PASS（保持 **warn 0**）。注意：
- 省略号检查**只对 ` ```go ` 块生效**（SQL 块不受影响）
- 命名仍不许含 `%` `#` 空格

**编号**：由 lead 指定，**不要再执行 `--allocate`**。

---

# 🐧 第 18 章（Linux/网络，53 篇）预告

本机是 **macOS**，与 Linux 有差异（如 `sysctl`、`/proc`、`systemd`、`ulimit` 默认值）。
- 能真跑的（多数 GNU 命令、`ulimit`、`df`、`lsof`、`ss` 替代品）**照跑**
- **Linux 特有**的（`/proc/*`、`systemd`、`iptables`、`/etc/security/limits.conf`）→ **标明平台**，或说明「用 `docker run` 起一个 Linux 容器验证」（Docker 已就绪，Engine 28.3.2）
- 涉及具体数字的**必须给命令 + 保守表述**


---

# 🔴🔴 「完成」的判据：**文件落盘 + state 标 done**（2026-10-04，已发生两次）

## 事实

**两次**出现「worker 报告 completed，但实际只交付了一半」：

| 时间 | worker | 交付的报告 | 实际情况 |
|---|---|---|---|
| 第 1 次 | gpA | 「528 已完成」 | 只落了 **527**，528 根本没写；state 里 8-1/8-2 都是 pending |
| 第 2 次 | gpF | 「571/572 已交付」后，**12-1/12-2 也报完成** | 只落了 **575**，576 没写；state 里 12-1/12-2 都是 pending |

**lead 每次都是查文件系统才发现的**——如果只信报告，这两张卡会被记成「已完成」，而实际是空的。

## 规则（写卡收尾必做）

**报告的「完成」= 满足下面全部三条**，缺一条都不算完成：

```bash
cd "/Users/Wang/Documents/面试/磁盘自带软件/go-interview"
PY=/Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3

# ① 文件真的在（用 ls 确认，别凭记忆）
ls -l target/go/<你的编号>-*.md

# ② state 真的标了 done（不是 pending、不是 running）
$PY -c "import json;st=json.load(open('_pipeline/state.json'));\
[print(v['id'],v['status'],v.get('cards')) for v in st['tasks'].values() if v['id'] in ('12-1','12-2')]"

# ③ 门禁真的 PASS（跑一次看输出，别凭印象）
$PY _pipeline/validate-v4.py | tail -3
```

**最低成本的自我校验：报完状态后自己 `ls` 一下确认文件在。**

## 为什么会发生

不是「忘了写」，而是**卡写完了但没落盘/没标状态时，误以为整个流程结束了**。
所以收尾顺序要固定为：**写卡 → 落盘 → 跑门禁 → 标 state → `ls` 复核 → 才报告**。

---

# 测试环境总表（2026-10-04 更新）

> 起任何服务之前，**先问一句：它监听在哪？** —— 见下面的 Redis 事故记录。
> 所有 env 脚本都在 `_pipeline/` 下，用 `source` 引入。

## MySQL（第 12 章用）

```bash
source _pipeline/mysql-env.sh          # 13307 / mtdemo / root 无密码
sql "SELECT VERSION();"                # 8.0.33
file _work/xxx.sql                     # 跑脚本文件
is_up / do_start / do_stop / do_restart
```
- 🔴 **共享实例，严禁 stop / restart / kill mysqld / 改全局变量**
- 🔴 **大批量写入前必须 `SET SESSION sql_log_bin = 0;`** —— 历史上有 worker 把 binlog 写爆过盘
- 单表 ≤ 10 万行，用完立刻 `DROP TABLE`
### ⚠️ 共享 Redis 上的"残留 key"处理（2026-10-04 真实发生）

**`counter:__rand_int__`** 这个 key 是 **`redis-benchmark` 的签名式残留**
（`__rand_int__` 是它的随机占位符，跑 `-t incr` 类基准测试时创建），曾在**共享实例的 db0** 上滞留。

**规矩：**
1. **跑 `redis-benchmark` 必须指定自己的库**：`redis-benchmark -n <db号> ...`；**绝不能在 db0（默认库）上跑**
2. **基准测试跑完，把自己造的 key 清掉**（`rflush`）
3. **看到不认识、且不是你造的 key —— 不要删，报 lead**（不删是对的：别人的数据可能还在用）
4. 判断基准残留的特征：key 含 `__rand_int__`、无 TTL、值是个递增计数

### ⚠️ MySQL「**静默错误读数**」黑名单（查询不报错，但结果是错的）

**这类坑比"报错"危险得多** —— 报错你会去查，静默错值你会直接拿去写卡。
**以下是本项目已实测确认的，用之前先看这张表：**

| 读数 | 坑 | 正确做法 |
|---|---|---|
| `information_schema.TABLES.AUTO_INCREMENT` | **显示陈旧值**（刚插完还是 NULL 或旧值） | 用 `SHOW CREATE TABLE` / `SHOW TABLE STATUS`，或**看下一条实际拿到的 id**（gpM 597 发现） |
| `information_schema.INNODB_LOCKS` / `INNODB_LOCK_WAITS` | 8.0 **视图还在、查不报错、但永远返回空** | 用 `performance_schema.data_locks` / `data_lock_waits`，且必须按自己的表过滤（gpM 912 发现） |
| `information_schema.tables.DATA_LENGTH` / `INDEX_LENGTH` | **不 `ANALYZE TABLE` 就不刷新**（实测误报 16KB，`ANALYZE` 后 89728KB） | 量体积前**先 `ANALYZE TABLE <表>`**（gpL 1111 发现） |
| `SHOW PROCESSLIST` 的 `Info` 列 | **精确截断到 100 字符**（不是"只显示前 100 行"） | 看完整语句用 `SHOW FULL PROCESSLIST`（gpM 912 发现） |
| 行锁等待时的 `State` 列 | 实测是 **`updating`**，不是 `Locked` | 判断行锁等待用 **`Innodb_row_lock_current_waits > 0`**（gpM 912 发现） |
| `SHOW ENGINE INNODB STATUS` 的 `dblwr_sync_requests` 等 | 实测**恒为 0 且 STATUS=disabled** | 别把这三个 0 当成"没发生双写"（gpK 584 发现） |

**共同规律：状态字 / 缓存字段会随版本和场景漂移，计数器才稳定。**
**拿不准时用「计数器 + 前后对照」**（跑一次，前后各读一遍看增量），**不要单点采样**。

- 🔴🔴 **锁观测必须按自己的表过滤**（2026-10-04 gpM 发现的跨 worker 污染坑）：
  `performance_schema.data_locks` / `data_lock_waits` 是**全实例视图**，
  **多个 worker 并行跑实验时会互相读到对方的表**。
  症状：`LOCK_DATA` 出现你表里根本没有的行值、或多个重复的 `TABLE IX` 行。

  正确写法：
  ```sql
  SELECT ENGINE_TRANSACTION_ID, OBJECT_SCHEMA, OBJECT_NAME, INDEX_NAME, LOCK_TYPE, LOCK_MODE, LOCK_STATUS, LOCK_DATA
    FROM performance_schema.data_locks
   WHERE OBJECT_SCHEMA = 'mtdemo'          -- 库里可能有多个 worker 的表
     AND OBJECT_NAME   = 't907'            -- ← 换成你自己的表名，务必加这行
   ORDER BY ENGINE_TRANSACTION_ID, LOCK_DATA;
  ```
  **不过滤 = 证据无效。** 卡片里贴 `data_locks` 输出时，也要把过滤条件一起贴上，让读者能复现。
- ⚠️ **`FLUSH TABLES` 不足以保证页落盘**：hexdump 读 `.ibd` 前必须用
  **`FLUSH TABLES <表名> FOR EXPORT`**（否则读出来是全 0）。用完 `UNLOCK TABLES` 释放。
- ⚠️ **`information_schema.INNODB_LOCK_WAITS` 在 8.0 已移除**（2026-10-04 gpM 实测）：
  该视图**还在、但查出来是空的**，容易让人误以为「当前没有锁等待」。
  **8.0 要看锁等待必须用 `performance_schema.data_lock_waits`**（且同样要按自己的表过滤）。
  （同理：5.7 的 `information_schema.innodb_locks` 在 8.0 也是空的，对应 `data_locks`。）

### 🔴 进程卫生：**绝不允许留下长期运行的测试进程**（2026-10-04 事故）

真实事故：两个 Go 测试二进制（`card561 spin`、`preempt`）**在后台空转了 4 小时 49 分**，
各烧掉 **275 CPU 分钟**（合计约 **9 个 CPU 小时**），工作目录都进了废纸篓还在跑。
当时机器 load average 已经 19~24 —— **它们把 CPU 抢走了，拖慢了所有 worker 的实验。**

**产生原因**：写「忙等/自旋/抢占」这类测试程序时，程序本身就是死循环，
worker 用完没有 terminate，进程就永久挂在后台。

**规矩（三条，都做到）：**

1. **凡是可能不自己退出的程序，一律包一层超时。**
   ⚠️ **macOS 没有 `timeout`，也没有 `gtimeout`**（已实测）。用 `perl` 的 alarm：
   ```bash
   perl -e 'alarm 30; exec @ARGV' go run .        # 最多 30 秒
   perl -e 'alarm 60; exec @ARGV' ./card561 spin
   ```
   （已验证可用：`perl -e 'alarm 1; exec "sleep","5"'` 会在 1 秒后被 SIGALRM 终止，退出码 142。）
2. **禁止用 `go run . &` / `nohup ... &` 把测试二进制扔后台**。
   需要并发就**两个前台会话各自带 alarm**，或让程序自己带退出条件。
3. **每批收工前自查一遍自己有没有留下东西**：
   ```bash
   ps aux | grep -E "[c]ard[0-9]+|[s]pin|[p]reempt|go-build" | head
   # 有就 kill -9 <PID>（自旋程序不响应 SIGTERM，必须 -9）
   ```

**顺带**：`go build` 产生的二进制放 `_work/<你的目录>/` 下，**用完删掉**；
别放 `/tmp/go-build*` 之外的地方还长期运行。

## Redis（第 12 章 Redis 部分、第 19 章系统设计用）

```bash
source _pipeline/redis-env.sh
redis_up                               # 存活判断
rcli ping                              # = redis-cli -p 16399
rdo info memory                        # 需要时自动拉起服务
bash _pipeline/redis-env.sh check      # 一条命令打出全部安全配置（做卡片证据用）
bash _pipeline/redis-env.sh restore    # 测完淘汰策略后还原默认
```
- 版本 **Redis 7.2.3**（`/usr/local/redis/src/redis-server`），端口 **16399**，**只有这一个共享实例，别开第二个**
- 🔴 **多 worker 隔离：用不同的 DB 编号**（Redis 默认有 db0~db15）。
  **每个 worker 认领一个 DB，进去先 `SELECT <n>`**，**不要用 db0**（默认库，最容易撞）：
  ```
  gpM → db 1     gpK → db 2     gpL → db 3
  rcli -n 1 flushdb        # 只清自己那个库
  ```
  **别用 `FLUSHALL`** —— 那会把别人的库一起清掉。
- 🔴 **`bind` 只能是 `127.0.0.1`，绝不允许 `bind * -::*`**
- 🔴 **`maxmemory 2gb`**：测淘汰策略时临时改，测完 `restore`
- 无持久化（`--save '' --appendonly no`，`--dir /tmp`）
- **不同测试之间必须 `FLUSHDB`**，否则结果互相污染
- 🔴🔴 **注意：持久化 / `maxmemory` / `appendfsync` 这些是「实例级」配置，不是「库级」**（2026-10-04 gpK 1013 发现）：
  ```
  CONFIG SET appendonly yes   →  影响【整台实例】；你开 AOF 期间，
                                 其他 worker 写进 db0/db1 的命令【也会进你的 AOF 文件】
  ```
  gpK 实测：它开 AOF 期间，从 AOF 里看到了**别库的 `SELECT 0` / `INCR counter` 命令**。
  **所以：**
  1. **测持久化类实验前，先看一眼当前配置**（`rcli config get appendonly appendfsync`），
     **测完立刻还原**（`appendonly=no` / `appendfsync=everysec` / `rdbcompression=yes`），
     **并删掉自己产生的 `dump.rdb` / `appendonlydir`**；
  2. **AOF/RDB 相关卡片的绝对数字要注明"实例级实验，期间其他库的写也会进 AOF，数字有波动"**；
  3. 想完全隔离，**自己起一个临时实例**（不同端口 + 不同 `dir`），别动共享实例。
- ⚠️ **Redis 7 的 `CONFIG SET dir` 是 protected config**：会返回
  `ERR CONFIG SET failed ... can't set protected config`。**文件只能落到实例启动时的 `dir`**（本实例是 `/tmp`）。
- ⚠️ **`rdb_last_cow_size` 在 macOS 恒为 0**（该指标依赖 Linux `/proc/self/smaps`）→
  **"COW 只复制被改页"在 macOS 上拿不到实测证据**，只能标 `[机制依据]`。
- ⚠️ **Redis 7 的 AOF 是多文件结构**：`appendonlydir/` 下有
  `appendonly.aof.N.base.rdb`（**头 5 字节是 `REDIS`**，即 RDB 格式）+ `.incr.aof`（RESP 文本）+ `.manifest`。
  **所谓"混合持久化"不是与 RDB/AOF 并列的第三种机制，而是 AOF 的一种形态**
  （`aof-use-rdb-preamble`，7.0 起默认 `yes`）—— 讲持久化时别把它说成三者并列。

### ⚠️ Redis 事故记录（2026-10-04，真的发生了）

worker 用 `redis-server --port 16399 --daemonize yes --save '' --appendonly no` 起服务，
**不带 `--bind`** —— Redis 7 的默认值就是 **`bind * -::*`（绑定所有网卡）**。

**为什么危险**：Redis 的 `protected-mode` 只在「**没有**显式写 bind 指令」时才生效。
一旦显式写了 `bind *`，protected-mode 实际**已失效**，再加上没设密码，
**同局域网任何人都能无密码连进来读写数据**（Redis 未授权访问是被长期利用的入侵入口）。

**修复**（不必重启，Redis 7 的 bind 支持热改，数据不丢）：
```bash
rcli config set bind "127.0.0.1 -::1"
rcli config set maxmemory 2gb
```

**教训：起任何 daemon 服务后，第一件事是确认它监听在哪个地址。**

## Kafka（第 14 章消息中间件用）

```bash
source _pipeline/kafka-env.sh
kafka_up                        # 存活判断（KRaft 单节点）
kafka_cli topic list            # = kafka-topics.sh
```
- 版本 **Kafka 3.7.0（KRaft 模式，无需 ZooKeeper）**，装在 `/tmp/mtdemo-kafka/kafka_2.13-3.7.0`
- **Java 用 JDK 21**（`/Library/Java/JavaVirtualMachines/jdk-21.0.11.jdk/Contents/Home`）
- **只有这一个共享实例，别开第二个**；测试 topic 用完 `kafka-topics.sh --delete`
- 同一实例上多 worker 跑实验时，**topic 名要带自己的卡号前缀**（如 `t910_orders`），别用 `test`/`topic1`

## Elasticsearch（第 13 章用）

```bash
source _pipeline/es-env.sh
es_up                           # 存活判断
es "GET /_cat/indices?v"        # 等价于 curl -s 127.0.0.1:9200/...
```
- 版本 **Elasticsearch 7.7.1**（`/Library/elasticsearch-7.7.1`，**本机原有，不是新装的**），端口 **9200**
- **只有这一个共享实例，别开第二个**
- **索引名要带自己的卡号前缀**（如 `t1108_files`），用完 `DELETE /<索引名>` 删掉

## ⚠️ 公共脚本可能正在被 lead 修改（2026-10-04 真实发生）

`validate-v4.py` / `checkdup.py` / `--env.sh` 这些**公共脚本由 lead 维护**。
lead 有时会在生产过程中加检查项，**那一瞬间你跑门禁可能撞上半成品**（报出奇怪的
`UnboundLocalError` / `NameError` / 语法错）。

**你的正确处理（gpK 做过一次，是对的）：**
1. **重跑一次** —— 多数情况下已经修好了
2. 还报错 → **不要自己改公共脚本**，直接报给 lead（附上完整报错与脚本 mtime）
3. 判断依据：`stat -f "%Sm" _pipeline/validate-v4.py` 看 mtime 是不是就在刚刚

**反过来说**：如果你在某张卡上报了"门禁炸了"，**先怀疑公共脚本，别先怀疑自己的卡**。

实测（2026-10-04 下 Kafka 时）：
```
archive.apache.org              →  9 KB/s      ← 110MB 要十几小时，完全不可用
mirrors.huaweicloud.com         →  240 KB/s ~ 1 MB/s ✓
mirrors.aliyun.com（该路径）     →  404（路径结构不同，不是网络问题）
mirrors.tuna.tsinghua.edu.cn    →  404（同上）
```
**规矩：下 Apache 系大文件先试 `https://mirrors.huaweicloud.com/apache/<项目>/<版本>/<文件>`，**
**再退到官方源。别直接在 `archive.apache.org` 上耗时间。**
（`goproxy.cn` 是 Go 模块的镜像，规则同理。）

## 系统环境（第 18 章 Linux 用）

- 本机是 **macOS**，**没有 Linux 环境**。
  ⚠️ **2026-10-05 更正**：**Docker daemon 现在是活的**（Desktop 4.43.2 / Engine 28.3.2），容器可以真跑。
  但纪律：**不许动 `webfault-*` 的任何容器/镜像，禁止 `docker system prune -a`**，用完 `docker rm` 自己的容器。
- 第 18 章按三档处理，**不许伪造**：
  1. 能在 macOS 实测的 → **必须真跑**（重定向 `2>&1`、inode/硬链接、mmap、TCP 状态机、TLS 握手…）
  2. macOS 与 Linux 行为不同的 → **必须显式标注平台差异**（`sed -i`、`ps`、`/proc`、`epoll` vs `kqueue`、`readlink -f`…）
  3. 纯内核概念（分段、页置换、DMA、零拷贝、写文件崩溃）→ 用 `man` / 内核文档 / 内核源码**带行号**追溯
- 🔴 **底线：宁可标「本机不可测，以下为文档口径」，绝不伪造实测输出。** 卡是给人背的，造假比不测危害大得多。

## 🔴🔴 但在写「本机不可测」之前，先做这道检查（2026-10-05 立 —— 已经错了 3 次）

**三个 worker 分别在 Redis 主从 / Docker 容器 / Kafka 高可用上写过「本机不可测」，三次全是错的。
三次都不是环境不行，是「没换个端口」。**

| 谁 | 当初的结论 | 真相 |
|---|---|---|
| lead | 「Redis 主从 / Sentinel 没法真跑」 | gpK 起了**私有实例**，主从 + Sentinel 全跑通 |
| lead | 「Docker daemon 不可用」 | 直连 socket 一查，**一直是活的** |
| gpM | 「单节点 KRaft，无法演示多机故障转移」 | 内存空闲 **77%**、现有 broker 只占 364MB，**完全可以再起 2 个**（+700MB 而已） |

**下「不可测」结论前，必须逐条回答这 5 问：**

1. **这个组件能不能再起一个实例？** 换个端口、换个 data 目录、换个 `-D` 参数，就能和现有实例并存。
2. **有没有「多实例」的替代？** 单机跑 3 个 broker / 3 个 Redis / 2 个 MySQL 是**标准做法**，不是权宜之计。
3. **资源够不够？先量再说**：`memory_pressure | tail -1`（空闲率）、`uptime`（负载）、`ps aux | grep java`（RSS）。
   **别凭感觉说"跑不动"。**
4. **多实例必须显式压内存**：JVM 加 `KAFKA_HEAP_OPTS="-Xmx256m -Xms256m"`、Redis 加 `maxmemory`、ES 加 `-Xms -Xmx`。
   **默认 1G 堆 × N 个实例 = 机器直接趴。**
5. **有没有「代理测量」？** 真硬件测不了（如 DMA），就**证明机制存在 + 测替代路径的成本**（gpN 1237 的 DMA 卡就是这么写的）。

**写卡时这两句话必须分清：**

- 「**本机不可测**」= 我做过上面 5 问，确认不可测 → **可以写**，并写明**为什么**不可测、缺什么条件
- 「**我没试**」= 没做检查就下结论 → **不许写成"不可测"** —— 那是把懒包装成诚实

**为什么较这个真**：卡的读者是要去面试的人。「本机不可测」写在卡上，他就永远学不到那个点；
而**换个端口真跑出来的东西，是他能复述、能在面试里说"我实测过"的**。

**配套资源**：`_pipeline/kafka-env.sh` / `redis-env.sh` / `mysql-env.sh` / `es-env.sh` 已经有单实例封装，
**多实例靠自己起，但纪律一样：独立端口、独立 data 目录、独立进程名，收工全清理。**

---

# 编号规则（2026-10-04 起）

**每个 worker 绑定一个固定号段，互不相交，由 lead 分配：**

| worker | 号段 | 负责范围 |
|---|---|---|
| **gpM** | **901 ~ 999** | 第 12 章 MySQL 主线（事务/锁/深分页/必备SQL/Redis） |
| **gpK** | **1001 ~ 1099** | 第 12 章索引底层存储 → EXPLAIN → SQL 优化 → 必备SQL |
| **gpL** | **1101 ~ 1199** | 第 19 章系统设计 → 第 13 章 Elasticsearch |
| **gpN** | **1201 ~ 1299** | 第 18 章 Linux / 网络（47 篇） |

**号段表是权威来源** —— 若任务书里写的号段与此表冲突，**以本表为准**（任务书可能是旧版）。

## 🔴 第 12 章剩余号源分配（2026-10-04 22:40 最终定稿，**只此一份，别再猜**）

> **背景**：这一天在 12 章上撞了 **6 次**号源（编号 3 次 + 同源重卡 3 次）。
> 根因是「派活清单只存在消息里」+「共享任务列表里同类任务并存」。
> **所以这张表写进手册，作为唯一权威。** 属于你的源做，不属于的**不要碰**。

| 源 id | 标题 | 卡号 | owner | 状态 |
|---|---|---|---|---|
| `12-45` | explain详解（三） | 1009 | gpK | ✅ done |
| `12-46` / `12-47` | 千万级深度分页（一/二） | 913 / 914 | gpM | ✅ done |
| `12-48` / `12-49` | 谈谈SQL优化的经验（一/二） | 915 / 916 | gpM | ✅ done |
| `12-50` / `12-51` | 面试必备的SQL语句（一/二） | 917 / 918 | gpM | ✅ done |
| **`12-52`** | **面试必备的SQL语句（三）** | **919** | **gpM** | ⬜ 待做 |
| **`12-53` ~ `12-58`** | **Redis 持久化 / 穿透雪崩击穿 / 过期删除 / 内存淘汰 / 大Key 等** | **1013 ~ 1018** | **gpK** | ⬜ 待做 |
| **`12-60` ~ `12-64`** | **Redis 双写一致性 / 高可用（一~三）等** | **1019 ~ 1023** | **gpK** | ⬜ 待做 |

**其余章节**：
| 章节 | 篇数 | owner | 号段 |
|---|---|---|---|
| 第 19 章（剩 2） | 19-11/19-12 | gpL | 1111 ~ 1112 |
| **第 13 章 Elasticsearch（16）** | `source/13/` | **gpL（做完 19 章接）** | **1113 ~ 1128** |
| **第 14 章 Kafka（20）** | `source/14/` | **gpM（12 章已收工）** | **920 ~ 939** |
| 第 18 章（剩 45） | 18-3 起 | gpN | 1203 起 |
| 第 15 章 微服务/Docker/K8s（19） | `source/15/` | **待分配** | — |
| 第 16 章 设计模式（8） | `source/16/` | **待分配** | — |
| 第 17 章 算法（2） | `source/17/` | **待分配** | — |
| 第 02 章 开篇（2） | `source/02/` | **待分配** | — |

### ⚠️ 同源重卡的判定与处置（今天发生过 3 次，别再发生）

**同一篇源文只能有一张卡。** 如果你发现某源已有卡（跑 `queue.py` 或看 `target/go` 的 `> 来源：` 行），
**立刻停手并报告 lead**，不要"我也做一张"。

已经归档的重复卡（**没删，留在 `_work/dup-archive/`**）：
```
1010-谈谈SQL优化的经验一.同源备份.md     （源 12-48，与 915 重复）
1011-谈谈SQL优化的经验二.同源备份.md     （源 12-49，与 916 重复）
1012-面试必备的SQL语句一.同源备份.md     （源 12-50，与 917 重复）
```

### ⚠️ 共享任务列表不是号源权威

`TaskList` 里可能**同时挂着两个 worker 的同类任务**（今天 #79 与 #81 都指向源 12-50），
按列表自驱领活就会撞源。**号源只以本表 + lead 当批消息里的清单为准。**

- 🔴 **不要跨段编号**。同一 worker 内在本段内顺序递增。
- 🔴 **不要跑 `checkdup.py --allocate`** —— 项目已改为手工号段分配
- `target/go/` 里 **v3 老英文卡占着 001~804 号段**，所以 v4 中文卡从 900 以上跳段编，避免同号共存
- 特批的例外（如接手的 583/584）由 lead 在任务书里单独指定

## ⚠️ 号段变更的血泪教训（2026-10-04，一天内撞了两次）

**第一次**：lead 给新 worker 和 gpG **都写了 901~904**（同一批号发给两个人）。
**第二次**：gpM 用的是**最初版本**任务书里的 901~904，而 lead 后来的「改号更正」消息它**没读到**，
结果它真把卡写成了 `901-事务的基础ACID与隐式提交.md` —— 那正是 gpK 的号。

**根因不是 worker 不听话，是 lead 的传达方式错了：**
1. 号段变更**只发一条「更正」消息**，没有在**每批开工消息里复述**
2. 变更**先改了产生编号的地方，后改校验的地方**（见下节）
3. worker 的上下文里可能同时存在**旧任务书 + 新更正**，它按哪个走全靠运气

**正确做法（已采用）：**
- 号段表写进**本文件**（worker 每轮都会读的手册），而不是只发消息
- **谁改号段成本低就让谁改** —— 第二次撞车最终解法是「gpM 保持 901~999 不动，把 gpK 从 901 挪到 1001」，
  因为 gpM 已经按 901~904 建好了目录、写好了第一张卡，**让它改等于重做，让 gpK 改只是一句话**
- 改完必须**回滚检查**：文件名、卡内 H1、卡内交叉引用 `见 XXX 卡`、`state.json` 的 `cards` 字段、
  门禁复跑 —— 五处都要对，**用 md5 证明内容没被改坏**

# 改编号/格式约定后的必做动作（2026-10-04 教训）

把编号从 3 位扩到 4 位时，只改了「产生编号的地方」，漏了「校验编号的地方」，结果：

- `validate-v4.py` 只认 `\d{3}` → 4 位卡直接报「命名不含编号前缀」
- `checkdup.py` 只认 `\d{3}` → 4 位卡**完全进不了查重范围**（静默漏检）
- `checkdup.py` 是**只读检查却在偷偷写状态**（`report()` 调 `allocate(5)`，每次往 `.reserved_ids` 追加 5 条）→ 累积 657 条，其中 528 条是垃圾

**所以，改任何编号/格式约定后，必须：**
```bash
grep -n 'd{3}' _pipeline/*.py _pipeline/*.sh     # 全仓库扫一遍旧正则
$PY _pipeline/validate-v4.py | tail -3           # 跑全库回归
$PY _pipeline/checkdup.py | tail -10             # 跑查重回归
```

---

# 🔴🔴 最终 50 篇冲刺分配表（2026-10-05 00:10 定稿 —— 本节覆盖前面所有旧表）

> 进度：**319 / 369 done（86.4%）**，全库门禁 **235/235 PASS，error 0 warn 0**。
> 只剩 **50 篇**。**做完这 50 篇，v4 主线就收工了。**
> 本节是**唯一权威**，与前面任何表冲突**以本节为准**。

## 各 worker 剩余任务与编号（一一对应，别再猜）

| worker | 剩余源 | 篇数 | 编号段 | 备注 |
|---|---|---|---|---|
| **gpK** | 第 15 章 `15-12` ~ `15-19` | 8 | **1035 ~ 1042** | ✅ 已完成 |
| **gpK** | 第 16 章设计模式 `16-1..16-5,16-7..16-9` | 8 | **1043 ~ 1050** | ✅ 已完成 |
| **gpK** | **回补** `1042`/`1040`/`1041`/`1039` 真机实测 | 4 | 卡号不变 | ⬜ 用 `gpk-demo` 集群，**限时 1.5h** |
| **gpM** | 第 14 章 `14-18` ~ `14-20` | 3 | **937 ~ 939** | ⬜ 做完即收工 |
| **gpN** | 第 18 章尾部 `18-49` ~ `18-53` | 5 | **1249 ~ 1253** | ⬜ 18-49 已完成(1249)，剩 4 张 |
| **gpL** | 第 13 章 `13-16` | 1 | **1128** | ⬜ 第 13 章收官 |
| **gpL** | 第 02 章 `2-1` / `2-2` | 2 | **1129 / 1130** | ⬜ 原属 gpM，00:40 转 gpL |
| **gpL** | 第 17 章 `17-1` / `17-20` | 2 | **1131 / 1132** | ⬜ 同上 |

**合计（收尾阶段）11 篇。** 谁也不要去碰别人的行。

> ⚠️ **2026-10-05 00:40 第三次调整（当前有效，前两版作废）**：
> gpN 在我发出「18-49 停手」之前**已经把 18-49 做出来了**（卡 1249，无重复）。
> **处理原则：让已经在章节里的人继续做完**（gpN 在 ch18 已做 13 张，上下文最热），
> 所以 **ch18 尾部整段归 gpN**（18-49~18-53 → 1249~1253）；
> **ch02 + ch17 改派 gpL**（→ 1129~1132，在它自己的号段内）。
>
> 🔴 **教训（写进这里，别再犯）**：**改派必须"先撤回旧指令，再发新指令"，而且要在同一条消息里说清"哪条作废"**。
> 我 00:37 那条把「停手」和「派新活」写在了一起，worker 在两次消息之间已经把旧活做完了 —— **时间差就够撞一次车**。
> 这次没撞上（靠盘上核查发现），**但属于运气**。

### 📌 进度快照（2026-10-05 00:37，用于开工前自检）

| 号段 | 已用到最大号 | 下一个可用 |
|---|---|---|
| gpM 901~999 | **936** | 937 |
| gpK 1001~1099 | **1050** | 收尾阶段只回补 |
| gpL 1101~1199 | **1127** | **1128** |
| gpN 1201~1299 | **1248** | **1249** |

🔴 **开工前必做**（30 秒，防撞号）：
```bash
cd /Users/Wang/Documents/面试/磁盘自带软件/go-interview
ls target/go/11*.md | sed 's/.*\///' | sort -n | tail -3    # 换成你的号段前缀
```
**消息里的号可能过期，盘上的号不会。** 今天为止已经在编号上撞了 6 次，**每一次都是"消息给的号 vs 实际占用"不一致**。

## 第 16 章 / 第 02 章 / 第 17 章的特别说明

这三章以前是「待分配」，**现在归人了**：

- **第 16 章（设计模式，8 篇）→ gpK**。注意：`source/16/` 共 **10 篇**，其中 **`16-6` / `16-10` 已完成**（v3 老卡：
  `330-go-factory-patterns-collapse.md`、`237-decorator-embedding-trap.md`，**英文命名、没有 `> 来源：` 行，所以 grep 来源行是查不到的**）。
  🔴 **别去补 `16-6`/`16-10`，会撞同源。** 正确自查方式（不要 grep 来源行）：
  ```bash
  $PY -c "
  import json;s=json.load(open('_pipeline/state.json'))
  [print(v['id'],v['status'],v.get('cards')) for v in s['tasks'].values() if v['chapter']=='16']"
  ```
  预期输出：`16-1/16-2/16-3 running(空)`、`16-4/16-5/16-7/16-8/16-9 pending(空)`、**`16-6 done`、`16-10 done`**。
  **只做空卡的那 8 篇。**
- **第 02 章（开篇 2 篇）→ gpM**。这两篇是「Go 为什么流行 / Go 的语言特性」，**内容偏观点、技术密度低**，
  按 v4 七段式写，`实测验证` 段可以写「语言特性对照实测」（如 goroutine 起 10 万个的实测内存占用），
  **但绝不允许空着或写「无需实测」**。
- **第 17 章剩 `17-1` / `17-20` → gpM**。算法题，**代码必须真实跑过并贴输出**。

## ⚠️ 代码块语言白名单已放开（2026-10-05，gpN 1237 触发）

gpN 报「```c 不被门禁认，只能改写成 ```text」。**这个修法不对** —— 那是**打地鼠**，
第 18 章全是 IO/系统调用（`read`/`write`/`mmap` 的 C 原型就得用 ```c），后面还有 cpp/rust/toml。

**已修 `validate-v4.py`：从「语言白名单」改成「非代码黑名单」** ——
只排除空标记 / `无` / `none` / `n/a`，其余一律认。**```c / ```cpp / ```rust / ```ini 现在都能过。**

**所以以后：语言该写什么就写什么，不要为了过门禁把 C 代码标成 text。**

## ⚠️ 关于「running 卡死」状态

`state.json` 里若有任务长期停在 `running` 而盘上没有卡（如 `16-1`/`16-2`/`16-3`，attempts≥1），
那是**早期已退出 worker 留下的陈旧标记**，**不影响你做活** ——
你照本表做完，用 `queue.py --done <id>` 正常收尾即可覆盖它。

---

# ⚠️ 实测陷阱追加（2026-10-05，与 MySQL 黑名单同性质：**测出来的数是假的**）

> 这一类错误的共同点：**命令跑通了、返回码是 0、数字看着像模像样，但那个数字根本不是你想测的东西。**
> 比"命令报错"危险 10 倍。**发现一个记一个。**

## 1. `dd if=/dev/zero of=/dev/null` 测内存占用 —— **假成功**（gpK 1035）

想验证 cgroup 的 `--memory=16m` 有没有真的 OOM，用 `dd if=/dev/zero of=/dev/null count=...`
→ **100MiB 也"成功"**，于是得出"限额没生效"的**错误结论**。

**为什么假**：零是**凭空生成的**，`/dev/null` 是**黑洞**，这条命令**从头到尾不持有任何内存**，
连 page cache 都留不下。它测的是 CPU 和 syscall 速度，跟内存配额毫无关系。

**改法**：必须**真正持有内存**（如 `python3 -c "a=bytearray(60*1024*1024)"`、或 `head -c 60M /dev/zero | sort`）。
gpK 改完之后 → **退出码 137（SIGKILL）**，限额生效 ✓。

🔴 **通用记法**：测「内存限制」时，被测进程必须**同时持有**那么多内存，**不能边生成边丢**。

## 2. 串行起两个容器比对隔离性 —— **拿到相同 inode**（gpK 1035）

想证明"两个容器的 namespace 是隔离的"，串行起容器 A、读 inode，销毁，再起 B、读 inode
→ **两者 inode 相同** → 会误判成"根本没隔离"。

**为什么假**：**namespace 的 inode 号在内核里会被回收复用**。A 销毁后它的 inode 被释放，
B 立刻拿到同一个号。**号相同 ≠ 同一个 namespace。**

**改法**：**必须并行起**两个容器再比对（gpK 并行起 → A=`...275`、B=`...379`，隔离成立 ✓）。

🔴 **通用记法**：**任何"销毁再重建然后比对 ID"的测量都不可信** ——
inode / pid / fd / 端口 / 临时文件名，全都会被内核复用。**要比就必须让两个对象同时活着。**

## 3. 验证脚本自己的 off-by-one —— **P99 不是 `sorted(v)[98]`**（lead 自查）

100 个元素的列表求 P99：`sorted(v)[int(0.99*100)]` = `sorted(v)[99]` 才对；
写 `sorted(v)[98]` 得到的是 **P99 的左边一个**（准确说是第 99 小的元素），
在"平均值掩盖长尾"的实验里会**正好把最长的那个长尾值漏掉**，于是得出"没有长尾"的反结论。

**改法**：求分位数用 `sorted(v)[min(n-1, int(p*n))]`，或者直接上 `numpy.percentile(v, 99)`。
**并且用一条已知答案的用例自检**（如 1..100 求 P99 应得 100）。

🔴 **通用记法**：**你写来"验证别人"的脚本，本身没人验证。**
凡是分位数 / 边界 / 取整，先用一个小样本手算一遍对答案。

## 4. `docker pull --platform` **会改写本地 tag 的指向**（gpK 1036 踩到，lead 复核确认）

想跑 `--platform linux/arm64` 看跨架构，于是 `docker pull --platform linux/arm64 busybox` ——
**这会把本机 `busybox:latest` 这个 tag 改指向 arm64 那份**，而本机是 **Intel（x86_64）**。

后果：**之后任何人 `docker run busybox` 都会静默跑在 qemu 模拟的 arm64 上** ——
不会报错、不会警告，只是**每个命令变慢好几倍**，测出来的时间全是假的。

**改法**：显式 pin 架构 `docker run --platform linux/amd64 busybox ...`，或**用完把 tag 拉回来**。

🔴 **通用记法**：**共享环境里带 tag 的"改写型"操作都要警惕** ——
`docker pull --platform` / `docker tag` / `git tag -f` / `ln -sf`，
都是**把别人的指向悄悄改掉**，而受害者毫无察觉。

## 5. 借这条讲个纪律（不是陷阱，是习惯）

上面第 4 条**是 lead 在验收下一张卡时顺手 `docker run` 才发现的** —— gpK 自己以为"已改成 pin amd64 重跑，数据干净"，
其实**只是它的实验干净了，共享 tag 还留在 arm64 上**。

**所以：你改过任何共享资源后，最后一步要"回头看一眼它现在是什么状态"，而不是"我改回来了"。
`docker images` / `git status` / `ls -l` 一行输出的事，比解释强一百倍。**

## 6. 「故意造的错误态」别留在共享实例上（2026-10-05，gpL 1115 触发）

**背景**：为了讲清 ES 的 red / yellow / green 三种健康态，gpL 在**共享的 9200 集群**上造了三个索引：
```
PUT /t_red    { "index.routing.allocation.require.box_type": "node_not_exist" }   ← 强制分不到节点 → red
```
**手法是对的、卡里证据也扎实，我认。**

**但副作用是：那之后任何 worker 敲 `_cluster/health`，看到的都是 `status: red`。**
- 轻则困惑（"集群挂了？"）
- **重则把"集群是红的"写进别的卡当结论** —— 这就变成污染数据源了

**规则**：

1. **造之前先想**：这个错误态会让**别人**读到什么？会不会被误当成真实状态？
2. **命名带标识**：用 `tmp_` / `demo_` 前缀（`tmp_red` 而不是 `t_red`），一眼看得出是实验产物。
3. **用完立刻删**：实验数据是**一次性的**；卡里**写下复现命令**就够了，不需要让那个状态常驻。
   判断标准：**"卡里有命令能重建" → 那就删掉实例。**
4. **必须常驻的情况**（如需要长期观察）→ **在共享实例上留一条显眼的说明**（如一个 `00_README_实验数据` 索引），
   并在报告里**明确告诉 lead**。

🔴 **通用记法**：**你的"教学道具"是别人的"环境污染"。**
共享实例上的每一个"故意弄坏的东西"，都要么**立刻拆掉**，要么**明确标出来**。

## 7. 改标题时的**三处联动**（2026-10-05，gpN 1245 踩到并处理正确）

**触发**：gpN 的 1245 卡文件名 25 个中文字，门禁报 `⚠ 命名: 中文标题 25 字，建议 ≤24 字`。

**改名不是改一处，是三处**：

| 位置 | 怎么改 | 为什么 |
|---|---|---|
| **① 文件名** | `1245-<短标题>.md` | 门禁看的就是这个；**≤24 个中文字** |
| **② 卡内 H1** | `# 1245 <短标题>` | 🔴 **最容易漏** —— 文件名改了 H1 没改，卡里卡外两个标题，读者一开就懵 |
| **③ `> 来源：` 行** | **一个字都不动** | 那是**源文件原标题**（机翻课的真实标题），**不是你的标题**。改了它就断了溯源链 |

**gpN 的处理是标准样板**（三处全对），照它做：
```
文件名  : 1245-3次握手时客户端何时会收到不正确的ack.md            ← 22 字 ✓
卡内 H1 : # 1245 3次握手时客户端何时会收到不正确的ack             ← 同步 ✓
来源行  : > 来源：`18-45 什么情况下3次握手过程中客户端会收到不正确的ack？`  ← 原样 ✓
```

**改完必做**：`validate-v4.py --file <新文件>` 复跑 + **重报 md5 与字节数**（重命名不改内容，md5 不变，但要证明你没顺手改到别的）。

🔴 **通用记法**：**凡是"一个东西有两个副本"的地方（文件名/标题、指针/数据、声明/实现），改一处就必须问"另一处在哪"。**

## 8. `k3d cluster list` 在创建完成前**恒显示为空**（2026-10-05，gpK 自曝）

**现象**：`k3d cluster create` 还在跑（拉镜像阶段），但 `k3d cluster list` **只有表头、没有任何行**。
gpK 连看三次都是空的 → **以为创建失败要重来** → 重复发起 —— **但那次其实一直在正常跑**。

**根因**：`k3d` 是**等集群完全起来之后才把它写进列表**的。`--wait` 没结束前，列表里**永远看不到它**。
**用"列表为空"判断"有没有在跑"是错的。**

**判断"创建中 vs 已失败"，看这个顺序**：
```bash
ps aux | grep "[k]3d cluster create"        # ① 进程还在 = 还在跑
docker ps -a | grep k3d                     # ② 看容器（tools / server / agent 逐步出现）
ls ~/.kube/config                           # ③ 建好后才有 kubeconfig
k3d cluster list                            # ④ 最后才看列表
```

🔴 **通用记法**：**"我没看到" ≠ "它不存在"。**
凡是"异步创建 / 后台任务 / 缓冲写入"，**用目标状态查询来判断进度都是错的** ——
要看**执行侧的痕迹**（进程、文件、日志），而不是**结果侧的清单**。

**同理**：`docker pull` 中途 `docker images` 看不到半拉镜像；
`git commit` 未完成时 `git log` 也看不到。**看错了工具，就会做出"重来一次"的错误决定。**

## 9. 换镜像源是解决"拉不动"的正规手段，但要**带 manifest 验证**（2026-10-05）

**背景**：`rancher/k3s` 从 Docker Hub 直连**在国内拉不动**（`du` 实测 Docker 数据目录 5 秒增 0MB）。

**测镜像源不要只测域名**，要测到**具体镜像的具体 tag**：
```bash
curl -s -o /dev/null -w "%{http_code}" https://<mirror>/v2/                                  # 能连
curl -s -o /dev/null -w "%{http_code}" https://<mirror>/v2/rancher/k3s/manifests/<tag>       # 真的能取
```
实测结果（2026-10-05）：
```
docker.1panel.live     /v2/ 200 + manifests 200   ← ✅ 可用
docker.m.daocloud.io   /v2/ 401                    ← 能连但鉴权异常
dockerproxy.com        /v2/ 000                    ← 不通
hub-mirror.c.163.com   /v2/ 000                    ← 不通
```

**用法**（拉下来改 tag，让工具用本地镜像）：
```bash
docker pull <mirror>/rancher/k3s:<tag>
docker tag  <mirror>/rancher/k3s:<tag> rancher/k3s:<tag>
k3d cluster create ... --image rancher/k3s:<tag>      # 显式 --image，别让它再联网校验
```

🔴 **通用记法**：**"能连"和"能取到我要的那个东西"是两件事。** 测任何依赖下载的路径，都要测到**最终产物**那一层。

## 10. **worker 会不认识自己的产出** —— 这是长时任务的必然，不是它的错（2026-10-05 gpK 实例）

**现象**：gpK 完成了 K8s 回补（改了 4 张卡、追加 ERRORS 段、删了集群），**并在报告里写清了全过程**。
几分钟后，它又报：「**我发现了第二个 gpK**，它在我跑的同时做了完全相同的回补」——**而它列出的每一条证据，都和它自己刚报的一模一样**（命名空间 `gpk-rt`、脚本 `rt1042.sh`、同样四张卡、同样的 ERRORS 段、同样删了集群）。

**真相**：**只有一个 gpK。** 它看到的是**自己几分钟前的产出**。

**为什么**：**我（lead）连发了 5 条消息给它**（00:33~00:45），它被**重复唤醒**；
如果两次唤醒后的运行有重叠，**后一个 run 起来时会看到"卡已经被改好了"，而它不知道那个人就是自己。**

🔴 **给 worker 的处置原则（gpK 做对了，照它做）**：
发现「有人在我之前做了同一件事」时 —— **只读核验 + 不改一个字 + 立刻问 lead**。
**绝对不要"修复"、不要"回滚"、不要"重做到我确认的样子"** —— 你不知道那些改动是合作者的成果还是你自己的，**动手就是破坏**。

🔴 **给 lead 的调度原则（这是我犯的错）**：
**消息发得太密会让 worker 重复唤醒、把自己的产出误认成别人的。**
- 同一批指令**合并成一条**发，不要拆成 5 条
- 发出后**等它回一轮再发下一条**
- 需要连续补充时，**明确写"以上一条为准，本条是补充"**

**通用记法**：**上下文会被压缩，但磁盘不会。**
凡是"我记得是我做的 / 我觉得是别人做的"这类判断，**一律回到磁盘上核对**（md5、mtime、`_work/` 目录），
**不要靠记忆**。

## 11. 改**已验收产物**之前先存原件（2026-10-05 gpK 无意中做对）

gpK 在回补 K8s 卡之前，**先把回补前的四张原卡复制到 `_work/gpK-k8s-realtest/orig-cards/`**。
它当时可能只是随手留底，但**这正是正确做法**：

- 改**已过门禁、已验收**的文件（回补、返修、格式统一），**先 `cp` 一份原文件到 `_work/<你的>-backup/`**
- 出事能**逐字节回退**，而不是靠"我改了什么来着"
- 报告里写明备份路径，lead 才知道去哪找

🔴 **通用记法**：**"我只是改一点点"是事故的高发区。** 改动前留底的成本是 1 秒，后悔的成本是一整轮返工。

## 12. **断言通过 ≠ 测到了东西**（2026-10-05，gpL 1132 自曝）

**现象**：gpL 给一个"找出只出现一次的 URL"的算法写测试 —— **断言全 PASS，但什么都没验证**。
**根因**：他把 **50 万个随机 URL 塞进值域 `0..9999`**（每个值平均出现 50 次）→
**"只出现一次"的个数 = 0** → 断言"结果为空"当然成立，**但这个断言在任何实现下都成立**，**等于没测**。

**改法**：换成**稀疏数据**（值域远大于样本数，保证确实存在"只出现一次"的元素）。

🔴 **通用记法（三条，按重要性排）**：

1. **断言通过不代表测到了东西，要先问"这个断言在错的实现下会不会也通过"** ——
   如果答案不确定，**就先故意把实现改错、看断言会不会红**（变异测试的思路）。
   **一个从没红过的断言，不值得信任。**
2. **测之前先确认"样本里真的有你要找的东西"** —— 找"只出现一次"的元素，先确认样本里**存在**这种元素。
3. **数据分布会决定测试是否有效** —— 值域与样本量的比例、重复率、边界值密度，
   **这些参数本身就是测试的一部分**，不是随便 `rand()` 一下就行。

**gpL 的处置（正确）**：**没有隐去这个失败**，而是把它写进卡里当教训。
**一个"我设计的用例其实什么都没测到"的自曝，比十条"我测通了"更有价值。**

## 13. 🔴 **给 lead：`_work/` 的 mtime 不动 ≠ worker 卡住了**（2026-10-05，我误判了 gpN）

**我犯的错**：看到 `_work/gpN-1252/` 的文件 mtime 停在 00:47、而当时是 01:09，
**就推断 gpN 卡住了**，并据此把它的第二张任务（18-53）转给了别人。

**真相**：gpN **一直在干活**。它这张卡要反复调参（WebSocket 握手的字节级实验），
**脚本没跑通之前它不落盘** —— 所以 `_work/` 里的文件是**上一步的产物，不是当前进度**。

**为什么这个指标不适用**：**worker 的典型工作模式是"先跑通再落盘"**。
`_work/` 里的文件**只在阶段完成时更新**，**中间的大段思考与试错完全不留痕**。
**用 mtime 判断"是否在推进"，等于用"交卷时间"判断"是否在答题"。**

🔴 **判断 worker 状态，至少看三个信号，不能只看一个**：

| 信号 | 怎么查 | 说明 |
|---|---|---|
| **① 它有没有回消息** | 等它自己报，或主动问一句 | **最直接** —— 但它可能在一个长推理轮里，回得慢 |
| **② 有没有进程在跑** | `ps aux` 找它的实验进程（`go build` / `curl` / 测试二进制） | 有进程 = 在跑 |
| **③ 文件有没有更新** | `_work/` mtime、`target/go/` 新文件 | **最弱的信号** —— 只在阶段完成时才变 |

**正确的动作顺序**：**先问一句**（成本最低、信息最准），**再看进程**，**最后才看文件**。

🔴 **处置原则（我当时做对了一半）**：
**拿不准时，改动要保守** —— 我当时只把"还没开头的那一张"转走，
**已经开了头的那张留给原 owner**，所以**没有造成重复劳动**。
**"转移任务"是不可逆的（会诱发重复写入），"多等一会儿"是可逆的。**
**不确定时，选可逆的那个。**

---

## 📌 给 lead 的自我提醒（今天累计的调度错误）

1. **消息发得太密会重复唤醒 worker**，它会把自己的产出误认成别人的（见第 10 条）→ **同批指令合并成一条**
2. **改派必须先撤回旧指令**，且要在同一条消息里写清"哪条作废"（今天 gpN 18-49 撞过一次）→ **时间差就够撞一次车**
3. **mtime 不动 ≠ 卡住**（见本条）→ **先问，再看进程，最后看文件**
4. **拿不准时选可逆的处置** → **多等一会儿优于转移任务**
5. 🔴 **最重要的**：**每次改派之后，必须回盘上核对"最终谁做了什么"** ——
   `grep -l "来源：\`NN-MM" target/go/*.md` 一秒钟的事，**今天靠它拦过两次**。

---

# 🆕 v5 改造规范（2026-10-05 定稿，用户已确认）

## 目标

**369 篇跑完了，但卡太厚 —— 中位 22 KB ≈ 8,000 汉字 ≈ 认真读 25~35 分钟。**
用户要的是「**考前 10 分钟能速记，平时能深挖**」，**两个需求不冲突，分隔开就行，都在一个文件内**。

**v5 = 在 v4 卡上加一个「速记区」，放在最上面；原有七段原样下沉为「原理区」。**

## 改造后的固定结构

```
# <编号> <标题>
> 来源 / 难度 / 边界 / 版本口径              ← 元信息，一字不动

# 🎯 速记区（考前只看这里）                  ← 上半（脚本自动加）
    ## 30 秒版                               ← ★ 你写的（唯一需要动脑的部分）
    ## 面试怎么答                             ← 原有段，脚本自动上移

---                                          ← 脚本自动加

# 📖 原理区（要搞懂原理再往下）               ← 下半（脚本自动加）
    ## 先说结论
    ## 完整代码
    ## 逐行讲透
    ## 实测验证
    ## 原文哪里错了
    ## 面试官可能接着问
```

**效果**：重卡从"654 行"变成"**前 58 行就能上场**"（占全文 9%）。

## 你唯一要做的事：写「30 秒版」

**存放位置**：`_pipeline/speed30/<编号>.md`（**纯正文，不要写 `## 30 秒版` 这个标题**，脚本会加）

**三段式结构（照这个写）**：

```markdown
**一句话**：<如果只记得住一句，就记这句 —— 通常是"这道题的题眼">

**面试按这 N 句说**：

1. **<要点名>** —— <一句话说清，可带数字>
2. ...
3. ...

**能报数字就更强**（实测）：
`<卡内实测数字>`
→ <这个数字说明了什么>

**最容易答错的 N 个点**：
- ...
```

**硬要求（会逐条检查）**：

| 要求 | 说明 |
|---|---|
| **长度 200~300 字** | 太短没信息，太长就不是"30 秒"了 |
| **四句左右，编号** | **按"面试时张嘴的顺序"编号**，不是按知识结构 |
| **不许引入卡里没有的内容** | **只做提炼，不做创作** —— 30 秒版里每个事实都必须在卡里找得到 |
| **不许直接抄「面试怎么答」原文** | 那一段是 **3~5 分钟的口语版**，30 秒版要**再压一个数量级** |
| **数字必须来自卡内实测** | 优先挑「实测数字 / 反直觉结论 / 易错点」——**这是拉开档位的地方** |
| **一句话必须是"题眼"** | 如 1031 的「不让局部故障演变成全局雪崩」、916 的「覆盖索引不回表」 |

**写之前必须读这三段**（顺序不要颠倒）：
1. **`## 先说结论`** —— 拿知识骨架
2. **`## 实测验证`** —— 拿可报的数字（**30 秒版里最值钱的部分**）
3. **`## 面试怎么答`** —— 看它怎么组织口语，然后**压短**，不是**照抄**

## 执行流程（每张卡）

```bash
cd /Users/Wang/Documents/面试/磁盘自带软件/go-interview

# 1. 读卡（三段）
sed -n '/^## 先说结论/,/^## 完整代码/p'      "target/go/<卡文件>"
sed -n '/^## 实测验证/,/^## 原文哪里错了/p'  "target/go/<卡文件>"
sed -n '/^## 面试怎么答/,/^## 面试官可能接着问/p' "target/go/<卡文件>"

# 2. 写 30 秒版（用 Write 工具落盘，不要用 heredoc）
#    → _pipeline/speed30/<编号>.md      纯正文，无标题

# 3. 改造（--inplace 会【自动备份】原卡到 _work/_v5-backup/）
$PY _pipeline/restructure-v5.py "target/go/<卡文件>" \
       --seconds30 "_pipeline/speed30/<编号>.md" --inplace --verify

# 4. 门禁复跑
$PY _pipeline/validate-v4.py --file "target/go/<卡文件>"

# 5. 报我：编号 + 新 md5 + 新字节 + 门禁输出
```

`$PY` = `/Users/Wang/.workbuddy/binaries/python/envs/default/bin/python`

## 🔴 六条红线

1. **只准改这一个文件**（你清单里的卡），**不许碰别人的号段** —— 清单在 `_pipeline/v5-blocks/block-<X>.txt`
2. **不许手改卡内容** —— 改造**只能**通过 `restructure-v5.py`；**脚本会校验"除顺序外一字未改"**
3. **不许改文件名 / 编号 / H1 / `> 来源：` 行**
4. **七段一个都不能少** —— 脚本缺段会直接报错退出（这是保护，不是故障）
5. **`--verify` 必须通过**才能算完成；不通过就停下来报我
6. **30 秒版不许编** —— 卡里没有的数字/结论**一个字都不许写**。**宁可写得朴素，不许写得漂亮**

## 抽检机制

lead 会随机抽卡，**逐字比对 `_work/_v5-backup/<原卡>` 与改造后**，确认：
- 除顺序外内容一字未改（脚本 `--verify` 已保证，但我会复核）
- 30 秒版里的每个事实**都能在原卡里找到**

**发现编造 = 该批全部返工。** 这条比"写得不好"严重得多。

---

## 🔴 v5 改造 · 踩坑记录（2026-10-05 全量开工当天，**每条都是真事故**）

### 坑 1：实测数字被"顺手整理" = 不合格（**不算编造，但同样不可接受**）

**事故**：30 秒版写 `match name=小红 → [2,1,3]`，**原卡实测输出是 `['2','1','3']`**。
集合没错、**顺序被重排了**。

**规则（硬）**：
> **30 秒版里的实测数字/输出，只能二选一：**
> - **✅【逐字照抄】** —— 连引号、空格、字段名一起抄：`match name=小红 → ['2','1','3']`
> - **✅【只留语义】** —— 不写具体序列：`match 命中全部 3 篇`
> - **❌ 重排** `[2,1,3]` ｜ **❌ 改精度** `rows≈49098` → `约 4.9 万行` ｜ **❌ 加模糊词** `1m` → `1m 左右`
>
> **理由**：30 秒版是给人**背**的，读者会记住那个顺序/精度。
> 原卡的数字是**实测输出**，是这张卡最硬的部分 —— **一旦被"顺手整理"，可信度就归零了。**

**附带产物**：检查脚本要能识别**千分位格式差异**（原卡 `2 569 168 B` ↔ 30 秒版 `2569168 B` 是**同一个数**，不是问题）。
`_pipeline/v5-audit.py` 已处理。

### 坑 2：改了 30 秒版直接重跑 `--inplace` → **二次加壳**

**事故**：改了 `speed30/<编号>.md` 后重跑，卡里叠出 **2 个速记区 + 2 个 30 秒版**，
**而且 `--verify` 检不出来**（旧卡也有 30 秒版，逐段比对照样通过）。

**已修（工具侧，不是靠人记）**：
- **硬保护**：卡里已含「🎯 速记区」→ **脚本直接拒绝执行**并告诉你怎么办
- **新增 `--refresh`**：要重做某张时加它，**会先从 `_work/_v5-backup/` 还原成 v4 原卡再重新套壳**

```bash
$PY _pipeline/restructure-v5.py "target/go/<卡文件>" \
       --seconds30 "_pipeline/speed30/<编号>.md" --inplace --verify --refresh
```

### 坑 3：`--refresh` 曾经会**把备份吃掉**（已修）

**事故**：`--refresh --inplace` 时，工具会把「**当前的 v5 卡**」复制进 `_work/_v5-backup/`，
**把 v4 原件覆盖掉** —— 等于把唯一退路烧了。（本目录**不是 git 仓库**，备份就是退路。）

**已修**：`--refresh` 模式下**保留原备份不动**。
**已受影响并重建**：`916`（从 v5 卡反向剥离脚手架 + 还原 v4 段序，重建后 22535 B，与原始 v4 一致）。

🔴 **给你的纪律**：**永远不要手动覆盖 `_work/_v5-backup/` 里的任何文件。**

### 坑 4：检查脚本的正则会**自己造出假阳性**（已修，记下来别再犯）

写"数字回原卡找"的校验时，我连错两版：
1. **第一版** `\d+(?:\.\d+)?` —— 漏判空格千分位 → 假阳性 2 个
2. **第二版** `\d[\d ,]*\d` —— **过贪**，把 `0.79 ms 2.4` 这类**跨数字的串**吃成 `792` → 假阳性涨到 11 个
3. **第三版**：30 秒版侧只抽纯数字；**原卡侧另建"千分位展开"集合**（只对 `1-3位+(分隔符+3位)+` 展开）→ **0 假阳性**

🔴 **通用记法**：**校验脚本本身必须有"已知答案"的自测。**
正则放宽一点，假阳性就冒出来；**一个会误报的检查，最后一定被人忽略。**

---

## 📌 全量改造的范围与分工（2026-10-05 10:17 起）

| 批次 | 范围 | 张数 | 状态 |
|---|---|---|---|
| **第 1 批** | **≥20KB** 的卡 | **171** | ✅ 全部完成（block-A/B/C/D） |
| **第 2 批** | **10–20KB** 的卡 | **112** | 🚧 进行中（block-E/F/G/H，各 28 张） |
| 合计 | 全部 v4 中文卡 | **283** | |

**为什么小卡也做**：**一致性**。读者打开任何一张卡，顶部都该有速记区；
一半有一半没有，比全都短更让人困惑。**但小卡的 30 秒版可以更短（150~250 字）**，不许为凑字数灌水。




---

# 🆕 任务：v3 → v4 重做（100 个源，2026-10-05 立项）

## 是什么

369 个源里，**100 个源当初是用 v3 老规范的卡交付的**（英文文件名、`分类/难度/原文锚点` 那套）。
现在要把这 100 个源**重做成 v4 规范**（中文名 + 七段式 + 来源行 + 实测优先 + ERRORS 段），
**并且新卡直接带上 v5 的「速记区 + 原理区」结构**（全库统一）。

## 清单在哪

```
_pipeline/v4-rework/ALL.txt       全部 100 个源
_pipeline/v4-rework/block-A.txt   卡号 1301~1325   ch04~ch08
_pipeline/v4-rework/block-B.txt   卡号 1326~1350   ch08~ch11
_pipeline/v4-rework/block-C.txt   卡号 1351~1375   ch11~ch16
_pipeline/v4-rework/block-D.txt   卡号 1376~1400   ch17~ch19
```
**制表符分隔，5 列**：`源id` / `章节` / `现用v3卡` / `新卡号` / `标题`

## 源文件在哪

```
source/<两位章节号>/<源id> <标题>-迅捷文字转语音-<时间戳>zh.txt
```
例：`source/04/4-11 Go输出时 %v %+v %#v 有什么区别？（一）-迅捷文字转语音-1790758588213zh.txt`

**这是 ASR 机转稿**（口播转写，不是机翻），**所以：错别字多、同音字多、没有标点分段、技术名词常被念错**。
**这正是一张卡的价值来源之一** —— 见下面「原文哪里错了」段的要求。

## 每张卡的产出流程

```bash
cd /Users/Wang/Documents/面试/磁盘自带软件/go-interview
PY=/Users/Wang/.workbuddy/binaries/python/envs/default/bin/python

# 1. 读源稿（ASR）
cat "source/<NN>/<源文件>"

# 2. 读现用的 v3 卡（它已经有提炼过的结论和部分实测，可以复用，但必须核）
cat "target/go/<现用v3卡>"

# 3. 写 v4 卡（七段式，见下）→ target/go/<新卡号>-<中文短名>.md
#    用 Write 工具落盘，不要用 heredoc

# 4. 门禁
$PY _pipeline/validate-v4.py --file "target/go/<新卡号>-<中文短名>.md"

# 5. 写 30 秒版 → _pipeline/speed30/<新卡号>.md（纯正文，无标题）

# 6. 套 v5 结构
$PY _pipeline/restructure-v5.py "target/go/<新卡号>-<中文短名>.md" \
       --seconds30 "_pipeline/speed30/<新卡号>.md" --inplace --verify

# 7. 追加 ERRORS.md 段（源 <源id>，卡 <新卡号>）
```

## v4 卡七段（一段不能少，门禁会查）

```
# <新卡号> <中文标题>

> 来源：`<源id> <源标题>`          ← 必须与清单里的标题一致，**一个字不动**
> 难度：… ｜ 面试频率：…
> 边界（先读这条）：…              ← 说明本卡不覆盖什么、别的卡覆盖什么
> 版本口径：…                      ← 实测环境（OS / 版本 / 工具）

## 先说结论
## 完整代码
## 逐行讲透
## 实测验证
## 原文哪里错了
## 面试怎么答
## 面试官可能接着问
```

## 🔴 本任务的特殊要求

### 1. 「实测验证」段：**v3 卡里已有的数据可以复用，但必须核**
v3 卡里已经有实测数据（那些是当年真跑出来的）。**复用它们可以省时间，但：**
- **能重跑的一定重跑**（这类卡片多是 Go 语言题，本机有 go1.26.5，绝大多数能跑）
- **重跑不了的**（如需要 Linux 内核、需要特定版本的）→ **沿用 v3 卡的数字，并在卡内注明来源是"v3 批次实测"**
- **绝对不许把没有的数字写成有** —— 这是编造

### 2. 「原文哪里错了」段：**用力挑**（ASR 稿是重灾区）
ASR 转写稿的特征错误：
- **同音字**：`拘`/`go`、`是`/`式`、`的`/`得`、`那`/`哪`、`在`/`再`
- **技术名词被念错**：`切片`→`且片`、`并发`→`病发`、`接口`→`借扣`、`协程`→`鞋程`
- **英文术语音译**：`context`→`康泰克斯特`、`channel`→`钱呢饿`
- **整句被吞**：口播省略，句子不完整
- **【重要】把源文讲错的技术点挑出来** —— **这一类比错别字值钱得多**

### 3. 与已有 v4 卡的关系
**同章已有的 v4 卡里，可能有相关的**（比如你做的 `%v %+v %#v` 和已有的格式化输出卡）。
**在「边界」行里互相引用**（写清"本卡不覆盖 X，见 NNNN 卡"），**不要重复讲别人的内容**。

### 4. 编号规则
- **卡号从清单第 4 列取**，不许自己编、不许跳号
- **卡名**：中文，≤24 字，**不含空格**
- **开工前先查重**：`ls target/go/<卡号>-*.md` 应为空

### 5. ERRORS.md
每张卡追加一段，格式照已有段落：
```
## <章节名>·<标题>（源 <源id>，卡 <卡号>）
（机翻/转写错误表 + 反纠错表 + 关键实测 + 卡文件 md5）
```
**只追加，绝不改动别人的段落。**

## 六条红线（与 v5 一致）
1. 只碰自己 block 里的源
2. 不手改别人的卡
3. 不改已有卡的文件名 / 编号 / H1 / `> 来源：` 行
4. 门禁必须 PASS（`validate-v4.py` + `restructure-v5.py --verify`）
5. **不许编** —— 没有的数据不许写；复用的数据必须标明来源
6. 30 秒版里的实测数字：**只能逐字照抄或只留语义**

---

# 📖 权威章节名表（2026-10-05 定，写 ERRORS 段标题时以此为准）

**原则**：**沿用 `ERRORS.md` 里已经写过的名称**（避免同名不同写），只为没有的补新名。
**章节名来自源课程的实际篇目主题**（`source/<NN>/` 的首篇）。

| 章 | 权威名称 |
|---|---|
| ch01 | 第 1 章 课程导学 |
| ch02 | 第 2 章 Go 语言概览与特性 |
| ch03 | 第 3 章 简历与求职准备 |
| **ch04** | **第 4 章 Go 基础语法与标准库** ← 既有 |
| **ch05** | **第 5 章 Go 语言进阶** ← 既有 |
| ch06 | 第 6 章 Go 语言高级特性 |
| ch07 | 第 7 章 常用库与框架 |
| **ch08** | **第 8 章 并发模型与调度器** ← 既有 |
| **ch09** | **第 9 章 数据类型底层原理** ← 既有 |
| ch10 | 第 10 章 并发编程 |
| **ch11** | **第 11 章 性能优化** ← 既有 |
| ch12 | 第 12 章 数据库 |
| ch13 | 第 13 章 Elasticsearch |
| ch14 | 第 14 章 消息中间件 |
| ch15 | 第 15 章 微服务 |
| ch16 | 第 16 章 设计模式 |
| ch17 | 第 17 章 数据结构与算法 |
| ch18 | 第 18 章 Linux / 网络 |
| ch19 | 第 19 章 项目与系统设计 |
| ch20 | 第 20 章 求职与录用 |

> ⚠️ **2026-10-05 更正 `ch18`**（lead 全库扫描发现）：本表原写「第 18 章 Linux」，
> 但 `ERRORS.md` 里**已有 16 段**全部写「**第 18 章 Linux / 网络**」。同样按「沿用已有名称」原则 → 表已改齐。

> ℹ️ **ch12 / ch15 / ch16 / ch17 的历史写法不统一**（实测）：
> ch12 在「章名位」上写过 `Redis` / `SQL 优化经验（一）` / `面试必备 SQL 语句（一）` / `深度分页优化` 等
> 十余种，**没有**出现「第 12 章 数据库」；ch15/16/17 也各有把篇目直接当章名的段落。
> **口径**：这三章**从 2026-10-05 起统一用本表的名字**（`第 12 章 数据库·<篇目>` 等），
> **不回溯改历史段落**（历史段已稳定，改它只会制造新的同名不同写）。

> ℹ️ **ch10 复核结论**（r4-B 问）：`ERRORS.md` 已有 2 段写「**第 10 章 并发编程**」，与本表一致 → **表无需改**。

**ERRORS.md 段标题格式**：
```
## <章节名>·<篇目标题>（源 <源id>，卡 <卡号>）
```
例：`## 第 9 章 数据类型底层原理·不同String拼接方式的性能分析（源 9-4，卡 1332）`

> ⚠️ **注意**：源 `ch08` 的首篇是「为什么面试官那么喜欢问 runtime 类型的问题？」，
> 但 `ERRORS.md` 已有的段落用的是「**第 8 章 并发模型与调度器**」——
> **以既有写法为准**（一致性优先于"更贴切的名字"；改名会让历史段落与新段落**同名不同写**）。

> ⚠️ **2026-10-05 更正 `ch06`**（r4-A 报 → lead 复核）：本表原先写「第 6 章 Go 高级特性」，
> 但 `ERRORS.md` 里**已有的 8 段**（1309~1316）全部写「**第 6 章 Go 语言高级特性**」，实测 `grep -c`：
> 前者 0 处、后者 8 处。按本表自己的原则（**沿用 ERRORS.md 已写过的名称**），**正解是「第 6 章 Go 语言高级特性」**，
> 表已改齐。r4-A 的 1312~1316 段标题**本来就是对的**，无需改。

---

# 14. 🔴 `go run main.go` **不读 `go.mod`** —— 验证"版本栅栏"必须用 `go run .`（2026-10-05 r4-A 发现，lead 独立复现）

## 事故现场

r4-A 在验证 `go 1.21` / `go 1.22` 的 **loopvar 栅栏**（for 循环变量捕获语义）时，
**两个版本跑出来一样**，一度以为"这个问题与 Go 版本无关"。

## 根因（我独立复现过）

```
go.mod 声明 go 1.21：
  $ go run .        →  3 3 3     ← 旧语义（读了 go.mod 的 go 指令）✓
  $ go run main.go  →  0 1 2     ← 新语义（**根本没读 go.mod**）

go.mod 声明 go 1.22：
  两者都            →  0 1 2
```

**`go run main.go` 走的是"单文件模式"** —— 它**不加载 `go.mod`**，
所以 `go` 指令声明的**版本栅栏对它完全无效**，它永远用**工具链默认（最新）语义**。

## 影响

🔴 **任何用 `go run main.go` 去验证"版本相关的行为差异"，结论都不可信。**
- 你会看到**新旧版本输出一样** → 误判成"这个行为与版本无关"
- 真相是：**你压根没进入旧语义**

## 正确做法

| 目的 | 命令 |
|---|---|
| 验证版本栅栏（要读 go.mod） | **`go run .`** 或 `go test` / `go build` |
| 只想跑单文件、且**不关心版本语义** | `go run main.go`（可以） |
| 想强制某个版本语义 | `go.mod` 里写 `go 1.21` + **`go run .`** |

**同理**：`go vet main.go`、`go test main.go` 这类"单文件"形式**也不读 go.mod** ——
**凡是要验证版本相关行为的，一律在 module 里跑。**

🔴 **通用记法**：**"我跑了，两个版本一样" ≠ "这个问题与版本无关"** ——
**先确认"我跑的那个命令，到底读没读我写的那个配置"。**
（这和"测缓存前要先保证缓存是冷的"是同一类错误：**被测对象没被真正激活**。）


---

# 🆕 任务：ch20 扩展批（5 源**全新创建**，2026-10-05 lead 派，**规格以此为准**）

> ⚠️ 本节按「**派活必须落成文件**」规则落盘。worker 若发现本节与实际文件不符 —— **先问，不要猜**。

## 一、范围与输入

- **清单**：`_pipeline/v4-rework/block-E.txt`（5 行；卡号 **1401 ~ 1405**；三列 v3 素材列**全为空 = 该章此前 0 张卡**）
- **输入**：`source/20/<源id> <标题>-迅捷文字转语音-*.txt`（机翻稿）—— **没有 v3 底稿可依，全部原创**
- **与主批的关系**：主批 82 源（block-A~D）**已完成并发布门全绿**；本批是**独立扩展**，**不进 `ALL.txt`、不进 `final-check.py` 的八项**（发布门只覆盖 82）

| 卡号 | 源 | 标题 |
|---|---|---|
| 1401 | 20-1 | 充分了解录用条件 |
| 1402 | 20-2 | 全面了解应聘岗位的工作内容 |
| 1403 | 20-3 | 通过技术面试后怎么谈薪水 |
| 1404 | 20-4 | 去大公司还是小公司 |
| 1405 | 20-5 | 如何顺利度过试用期 |

## 二、格式规格（**非技术内容的特殊处理**）

1. **结构不变**：仍是 v4 七段（先说结论/完整代码/逐行讲透/实测验证/原文哪里错了/面试怎么答/面试官可能接着问）+ v5 套壳（🎯速记区 + 📖原理区）。
2. **`完整代码` 段怎么填**：门禁要求**至少一个带语言标记的代码块**（`mermaid` / `text` / `bash` / `go` 都算，只有空标记不算）。本批一律给：
   - **一条 `mermaid` 决策图**（必给）——把"怎么判断/怎么选"画成流程或决策树
   - **一个可跑的辅助件**：优先 **`go` 或 `bash` 的计算脚本**。可用方向（按内容选，不必全用）：
     - 20-3 谈薪 → **税后到手计算**（个税+社保，标明税率表年份与地区）、**offer 对比的加权期望值**
     - 20-4 公司选择 → **决策矩阵加权评分**（权重与打分表可改）
     - 20-1/20-2 → **核对清单**（`text` 块）+ 可跑的"条件匹配打分"
     - 20-5 → **试用期时间线**（mermaid 甘特/流程）
   - **不许为了凑代码块写无意义的代码**；写不出可跑的，就写**可渲染的 mermaid + `text` 清单**，别硬造。
3. **`实测验证` 段怎么填**：**只放本机跑出来的真实输出**（脚本 stdout、mermaid 渲染/语法检查、计算过程）。**凡属常识/法条/市场口径的，必须显式标注**（如 `[常识]` `[法条：劳动合同法第 N 条，2026 年现行]`）。**禁止把"话术建议"包装成"实测结论"** —— 这是本批最容易犯的错。
4. **时效与平台**：涉及**法条 / 税率 / 社保 / 市场薪资**的，**必须标年份与地区**（例：`[2026 年·中国大陆]`）。这类内容会过时，不标年份等于埋雷。
5. **`原文哪里错了` 段用力挑**：话术类源文**错得比技术类更多** —— 常见三类：**① 过时**（旧规/旧行情当现行）、**② 绝对化**（"一定""必须""绝对"）、**③ 以偏概全**（个例当规律）。挑出来的要**给依据**，不是"我觉得"。
6. **30 秒版的口径**：这类内容不是"面试怎么答"，而是"**怎么决策 / 怎么回应**"。`## 面试怎么答` 段保留（可写"被问到时怎么讲"），但 30 秒版要给**可执行的动作顺序**。

## 三、交付口径（照旧 6 项，缺一不可）

```
01. validate-v4.py --file  →  0 error 0 warn
02. 结构计数：🎯速记区 1 / ## 30 秒版 1 / 📖原理区 1
03. check-selfref.py       →  本卡号 0 命中
04. restructure-v5.py --seconds30 _pipeline/speed30/<卡号>.md --inplace --verify → ✓ 除顺序外内容一字未改
05. ERRORS.md 段标题：'## 第 20 章 求职与录用·<篇目>（源 20-x，卡 14xx）'（**只追加**）
06. 报告带：md5 / bytes / 门禁尾部 / 结构计数 / check-selfref 命中数 / ERRORS 段行号
```

**红线不变**：编号从 `block-E.txt` 第 4 列取、**不许自己编**；文件名中文 ≤24 字、不含空格/`%`/`#`/全角 `？`；开工前 `ls target/go/<卡号>-*.md` 确认不存在；**代码围栏内不用 Markdown 标记**（`**`/反引号）；**不许编数字**。

## 四、节奏

**每轮 2 张**（1401+1402 → 1403+1404 → 1405），每轮做完停下回报，等 lead 验收后再继续。
