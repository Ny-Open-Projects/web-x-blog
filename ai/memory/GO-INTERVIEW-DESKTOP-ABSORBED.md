# 课程 11 · Desktop 原始工作区吸收完毕（2026-11-17）

> 事实：`~/Desktop/go-interview`（go 面试卡流水线原始工作区，2026-10-02~10-07）已按用户指令
> 三遍扫描确认吸收后删除——2026-11-17 23:40:47 `mv` 到 `~/.Trash/go-interview_20261117_234047`
>（7587 路径 / 451MB 含 .git；**未用 rm**；manifest 见 `/tmp/go_interview_delete_manifest.txt`）。
> 注意：macOS 可能自动清空废纸篓，恢复窗口有限；但内容已全部吸收，数据无独有损失。

## 吸收结论

- **渊源**：项目 `work/go-interview` 是该 Desktop 工作区的 fork 续跑版（10-06 起夜间批量 + v5 重编号）。
- **source**：两侧逐目录一致（21 章 / 398 文件）——无独有素材。
- **target**：材料 378 张卡（旧编号 001/141-939/1001-1405）与项目 1394 卡 **0 文件名重叠**；
  经标题模糊匹配 + 关键词核查 + 内容 4-gram 相似度三道比对，≈97% 已覆盖或超越。
- **真缺口（已补，target 1394→1405，blog 1402→1411）**：
  - ch20 求职 5 张：2001 录用条件三层拆解 / 2002 岗位画像与单源孤证 / 2003 谈薪与年包到手测算 / 2004 大小公司决策矩阵 / 2005 试用期法定红线（v5 格式重写，实测脚本内嵌，交叉引用 2001–2005）。
  - ch18 Linux 实操 2 张：1854 取 tmp 权限与打印偶数、1855 求和五法与权限三层扩展（BSD/GNU 差异实测）。
  - ch08 runtime 2 张：821 静态锁分级与 m 持锁上限（+deep）、822 调度延迟抽样 /sched/latencies（+deep）。
  - 815 卡「上限 10」[存疑] 已解除（locksHeld[10] 仅 GOEXPERIMENT=staticlockranking 下维护），指向 821；blog 1301-815 帖已同步。
- **未搬**：读物 3 册（精读/速览/学习路径）、背诵清单-全库/本批、复习路线——都是**旧 378 卡库上的生成产物**，
  卡号（1332/543 式）已过时，内容=卡片聚合。生成能力在 `work/go-interview/_pipeline/gen-reader.py / gen-recite-list.py / gen-study-path.py / gen-review-path.py`（后者本次补齐），
  但这四个脚本按 v4 卡格式 + `target/go/` 布局解析，对 v5 平铺布局**不能直接跑**，重生成前需先移植解析逻辑。
- **v3 归档**（go-v3-archive 219 张英文卡）：37 张 v4 未覆盖的孤儿卡里，唯二有价值的内容（115/121）已转 821/822；其余全部有 v4/v5 对应。
- **_work/ 311 项**：批处理草稿与实测脚本归档，实测脚本已内嵌进对应新卡（jd_match/job_profile/tax_after/decision_matrix/probation/perm-parity/sum100-perm）。
- **material 的 git 历史**：删除前 HEAD 为 `b22eaff`（项目从 Documents 迁移到 Desktop 并更新全部写死旧路径），工作区 clean；内容已全部被项目侧覆盖，无独有提交价值。

## 遗留（如需再做）

- 读物/背诵清单/复习路线若要为 1411 卡库重生成：先移植 4 个 gen-* 脚本的解析逻辑到 v5 卡格式（`一句话总述`/`面试官视角`/meta 行 `频率：`），TGT 路径改 `PROJ/"target"`。
- blog `_posts/go-interview` 的序号是**发布顺序**（0001–1411），与 target 卡号解耦；再次全量重跑 `_hexo_publish.py` 会重排序号、破坏链接——增量发帖请沿用手动 seq 追加。
