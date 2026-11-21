# 题库总览 —— 双 5000 题交付（P1-P10 全覆盖）

> 交付日期：2026-11-16 ｜ 本机实测校验通过（grep 计数）
> 架构：手写"知识点事实矩阵"（2550 条，每条 = 实证事实 + 3 个常见误认知 + 原理 + 用法 + 版本锚点）
> × 双生成器（固定随机种子确定性输出）= 笔试题库 + 面试题库

## 题量总账

| 域 | 知识点 | 笔试题 | 面试题 |
|----|--------|--------|--------|
| Java 基础 | 110 | 923 | 770 |
| 并发 | 110 | 983 | 770 |
| JVM | 110 | 981 | 770 |
| Spring | 110 | 973 | 770 |
| MySQL | 110 | 982 | 770 |
| Redis | 110 | 979 | 770 |
| MongoDB | 88 | 785 | 616 |
| MQ | 100 | 883 | 700 |
| 分布式 | 110 | 989 | 770 |
| AI/Agent | 88 | 794 | 616 |
| **Java AI 框架** ✅ 双 5000 达成 | 715 | 6287 | 5005 |
| **Agent 开发** ✅ 双 5000 达成 | 719 | 6448 | 5033 |
| 算法/数据结构 | 70 | 631 | 490 |
| **生成合计** | **2550** | **22638** | **17850** |
| **+ 手写存量**（24 册 156 题 / 笔试卷 283 题） | | **≈ 22921** | **≈ 18006** |

## 题型结构

**题号格式**：`Q<域名>-<序号>`（如 Qmysql-1514、Qredis-1250），跨域引用不歧义。

**笔试题**（FactQuestionGenerator，6 题型/知识点）：
单选·正向（3 干扰项=真实误认知）｜单选·反向（3 真 1 误）｜判断·真｜判断·假×2（纠正句带"原因"增强针对性）｜填空（术语挖空）｜简答（①事实②原理③要点 三段标准答案）

**面试题**（InterviewQuestionGenerator，5 题型/知识点，P 级全分层）：
概念考察｜误用纠错｜原理深挖｜工程落地｜版本演进｜边界追问｜追问链（7 题型/知识点）
每题含【面试官】问法 +【标准回答话术】+【评分点】

## 文件位置

```
notes/quiz/
├── facts/            # 11 个域的知识点矩阵（.txt，管道分隔 12 字段）
├── FactQuestionGenerator.java       # 笔试题生成器
├── InterviewQuestionGenerator.java  # 面试题生成器
└── out/<domain>/     # 每域 quiz-bank.md（笔试）+ interview-bank.md（面试）
```

## 重新生成

```bash
cd notes/quiz
javac -encoding UTF-8 FactQuestionGenerator.java InterviewQuestionGenerator.java
java FactQuestionGenerator facts/<domain>.txt out/<domain>       # 笔试
java InterviewQuestionGenerator facts/<domain>.txt out/<domain>  # 面试
```

确定性输出（固定随机种子），同输入同结果；改矩阵后重跑即更新题库。

## 质量机制

1. **每条事实可溯源**：矩阵行带版本锚点（JEP/JLS/官方文档），其中 30+ 条为本机 JDK 21.0.2 实测（树化语义/偏向锁移除/GC 日志格式/逃逸分析零 GC/滑动窗口语义等）
2. **干扰项=真实误认知**：单选干扰项与判断题素材来自工程实践常见错误，反向题 3 真 1 误
3. **质量守门**：干扰项不足 3 个不出单选；term 非 fact 子串不出填空
4. **官方文档核对零差异项已嵌入**：binlog ROW、HyperLogLog 12KB/0.81%、MongoDB 50/7、TTL 60s、KRaft 移除 ZK 等
5. **P 级覆盖**：面试题 P1-P10 无断档（按题型分层标注）
6. **结构审计（2026-11-16）**：全 1046 行自动审计——字段数错误 0（修复了 JB-079/JB-088 两行含未转义
   `|` 导致生成错位的问题，其中 JB-088 曾把"why"误混入干扰项列表）；填空守门剩余 270 条为 term 与
   fact 措辞不一致（设计上跳过不出题，无误题风险）；生成器填空匹配升级为空白容忍（"B+树"可匹配"B+ 树"）

## 笔试模拟卷（可自测）

10 套 100 分制试卷在 `notes/quiz/exams/`（ExamPaperBuilder.py 确定性抽样，seed=20261117）：
单选 20×2 + 判断 15×2 + 填空 5×2 + 简答 5×4 = 45 题/卷，题目在前、答案解析统一附卷尾。
做完按"来源域名"回 out/<域名>/quiz-bank.md 溯源。重跑 `python ExamPaperBuilder.py` 可重新抽卷。

## 面试模拟问答卷（口述自测）

10 套口述自测卷同样在 `notes/quiz/exams/`（InterviewPaperBuilder.py，seed=20261118）：
每卷 20 题（概念 6+纠错 4+原理 4+落地 3+版本 3，P1-P10 混合），面试官问法在前、
标准话术+评分点附卷尾，按评分点 0/1/2 自评，满分 40。

## 交互刷题面板（HTML，离线可用）

`notes/quiz/exams/interactive-quiz.html`（QuizPanelBuilder.py 生成）：4314 道客观题
（单选 1176 + 判断 3138，覆盖 11 域），双击即可用浏览器打开——点击判分、解析即时展开、
错题标记、域/题型过滤、"只刷错题"模式、进度 localStorage 自动保存、换序重刷，
以及**一键导出错题本**（Markdown，含正确答案标注与解析，方便打印复盘）。

## 面试话术检索手册（HTML，可搜索）

`notes/quiz/exams/interview-manual.html`（InterviewManualBuilder.py 生成）：**全库检索**——
面试题 5580 + 笔试主观题（填空/简答）共 7532 条单文件可搜索：关键词全文检索、按域/题型
过滤、P 级徽标、点击卡片展开答案（背诵模式：先默答再对照）。单选/判断在交互面板刷。

## 闪卡全量版（Anki 可导入）

`notes/quiz/flashcards.md`（Markdown 折叠卡）+ `notes/quiz/exams/anki-cards.csv`
（Tab 分隔带 BOM，Anki 直接导入）：1116 张闪卡由矩阵一键生成，正面「topic · term（维度）」，
背面四件套（事实/原理/用法/锚点）。重跑 `python FlashcardBuilder.py` 随矩阵更新。
HTML 交互版：`notes/quiz/exams/flashcards.html`（FlashcardViewerBuilder.py 生成）——翻卡自测、
标「会/不会」、"只看不会的"模式、进度保存，键盘：空格翻面 / G 会 / F 不会 / N 下一张。

## 使用建议

- 背诵路径：先 docs/ 第 1-11 册（体系）→ 面试题库按域刷（话术）→ 笔试题库自测（错题回矩阵行溯源）
- P10 冲刺：面试题库"工程落地"+"版本演进"两型 + docs/23 对话剧 + docs/24 笔试卷 G 组
