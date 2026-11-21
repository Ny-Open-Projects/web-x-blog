# scan1 · 拆题报告（2026-11-18）

- 总卡片：**2913**
- 层次：体系精讲 12 章 / 实战演练 9 类 / 背诵卡 13 域 2550 条

## 源缺陷与处置

- agent-dev: JA-033 前缀归一化为 AD-033（源笔误，AD-031/032/034 序列）

## 备注

- INDEX.md（源）统计为陈旧版 6145 题，实际 quiz 题库 20908 条，以 DELIVERY.md 为准；未按 INDEX 拆分。
- 源 notes/quiz/exams 两块 HTML 面板（interactive-quiz / interview-manual）为自测工具，不拆卡，留在 source。
- source 归档排除 maven target/ 构建产物与 ._* AppleDouble，160 文件 / 45.4M 与 live 逐字节 cmp 一致。

## 后记（2026-11-18 删除外置盘源）

- 用户指令删除交付素材（live 目录 + 3 个备份 zip）。删前将 live 的 maven target/（4 文件）补入
  归档，归档升为 164 文件全量超集，164/164 逐字节 cmp 一致。
- 三 zip 哈希审计证明其内容均为 live 子集（only-in-z14/z16/z17 = 0），无独有数据丢失。
- 删除方式：`mv` 进废纸篓 `~/.Trash/java-interview-win1_20261118_003256/`（未用 rm），
  移动后废纸篓副本再次 164/164 cmp 校验一致，3 zip 字节数与原件相同。
- 唯一留存：`work/source/33.java-interview`（164 文件 / 45.4M，只读锁定）。
