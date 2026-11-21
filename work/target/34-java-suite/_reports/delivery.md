# 课程 34 · Java 后端进阶全套 · 交付报告

> 收官时间：2026-11-20。素材源：外置盘 `/Volumes/SAMSUNG/ai-done/` 的 07/08/09/10 四目录（原件未动）。
> 本报告是四模块新课的终验记录；断点细节见 `../STATE.md`，课程登记见 `work/COURSES.md` 34 号行。

## 一、成品总览

| 模块 | 内容 | 篇数 | 处理方式 | QC |
|---|---|---:|---|---|
| M1 面试专题 | 七章（基础/并发/框架/虚拟机/数据库/缓存/分布式）+ 术语速查卡 | 257 | 成品深稿 → front-matter + 图片/demos 路径改写 + 章名校验 | 0 问题 |
| M2 就业指导 | 工作/市场/简历/面试/试用期 + 拓展 4 篇 | 12 | 成品深稿 → front-matter + 主题 tag | 0 问题 |
| M3 十大中级项目 | 微服务技术/SaaS-HRM/好客租房/Hadoop3/黑马头条/冷链监控/探花交友/智慧学成/闪聚支付/万信金融 | 1629 | 成品深稿 → 批量 front-matter + 重命名防冲突 + 坏图剔除 | 12 处 TODO 为教学占位（豁免） |
| M4 六大进阶项目 | 品达物流TMS / 智牛股 / 秒杀专题 / 中台组件化 / 亿可控 / 立可得 | 214 | **口播原稿重写级深稿**（manifest 聚合单元 → agent 重写 → QC 门禁） | 214/214 PASS |

**进站落位**：`work/blog/source/_posts/java-suite/` 2112 篇（单目录，categories 分四模块）；
`source/images/java-suite/m1/` 188 png；`source/demos/java-suite/` 8 个交互 demo。
**构建**：hexo 全量 14302 files 通过（node 22.13.1；系统 node16 有 strip-ansi ESM 冲突）。
**导航**：`/courses/` 页与首页已补 34 号卡（26 门课 / 11574 篇）。

## 二、素材处置与红线遵守

- source 归档 `work/source/34.java-suite`（161M / 11726 md / 376 png），排除 19G wav、418M vision_line、1.1G materials-code，全部 chmod 只读锁；外置盘原件未动。
- M4 原料 1671 份 merged 双线合并稿；manifest 权威映射六大项目/章节；23 条跨章重名 video_id（同名「学习目标/本章内容介绍」）merged 按唯一文件归属首单元，`_dup_report.json` 留痕，不编造。
- 已知源缺陷处置：09 交接文档 INDEX「2085 篇」陈旧未采信（实盘 1629）；M1 INDEX 漏收 5 篇已补章名、2 篇管线元文档不发布；M3 15 篇坏图剔除、相对内链降级；「【一手：666java .com】」水印一律不进成稿。

## 三、流水线资产（可复用）

- `ai/scripts/ingest_java_suite_source.sh` — 素材归档（rsync 尾斜杠/只读锁时序两个坑已修）
- `ai/scripts/ingest_java_suite.py` — m1/m2/m3 机械处理 + sync（m4 只放行 QC PASS 稿）
- `ai/scripts/m4_build_units.py` / `m4_next_prompt.py` / `m4_mark_done.py`（含 34.java-suite 点号误写自愈）/ `m4_qc.py` — M4 夜班滚动四件套
- QC 口径：front-matter 四字段 + title 双引号 + CJK 分级门槛（<40KB 单元 1200，其余 1500）+ 口播腔 0 残留 + 围栏成对 + H1 唯一
- agent 协作口径：并发上限 1（实测 3 派 2 死 1 拒）；双会话分头推进时以 _m4_state.json 为唯一事实源，尾部认领避免撞车

## 四、全站风格审计（2026-11-20 补做）

对 2112 篇做了三类机械审计并修复，全部改动落 target 后 re-sync + hexo 重建（48 files）通过：
- **弯引号**：M4 有 3 篇（立可得 m4-163/164/197，并发会话产出）正文含 54 处弯引号 → 成对改「」，含 1 处 front-matter title 嵌套引号隐患（YAML 已验证解析正常）
- **整句加粗**：30 处（M1 8 / M2 10 / M3 10 / M4 2）→ 去粗保留文字
- **本文/本篇 自我指涉** 138 处：判定为中文技术博客自然用法，不改
- 复检：正文弯引号 0 / 整句加粗 0

## 五、遗留与建议

- 未 commit：本课程全部产出在工作区未提交，待用户裁定提交批次（建议按 source 归档 / target+脚本 / _posts 进站三笔分开）。
- 保活 cron automation-e817b99e 使命完成，可由用户停掉（或保留作巡检，每轮只会报告"无待续工作"）。
- M2 的 12 篇仅做了机械处理 + 抽检，未逐篇人工精修（原料已是成品深稿，边际收益低）；如需逐篇精修可在 target/34-java-suite/m2 上直接改后 re-sync。
- M4 深稿由 agent 依画面线修正 ASR 错字，个别演示口径（IP/端口/密码）按课程原样保留，发布前如需脱敏可全库 grep 处理。
