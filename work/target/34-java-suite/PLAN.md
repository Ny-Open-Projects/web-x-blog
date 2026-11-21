# 课程 34 · Java 后端全套四模块（面试专题 + 就业指导 + 十大中级项目 + 六大进阶项目）

> 生成时间：2026-11-18。素材源：外置盘 `/Volumes/SAMSUNG/ai-done/` 的 07/08/09/10 四个目录。
> 本文件是本课程的**方案与断点事实源**；每轮续跑先读这里，再看 STATE.md。

## 一、四模块映射（用户定调：一门课，四个模块，每模块润色深化）

| 模块 | 素材目录 | slug | 内容 | 原料成色 | 处理深度 |
|---|---|---|---|---|---|
| M1 | `07、阶段七 面试专题_20261025_002609/blog_interview` | `m1-interview` | 260 md（256 成稿按七章：基础57/并发43/框架45/虚拟机33/数据库23/缓存29/分布式26）+ INDEX + 术语白话注解 + 188 png（images/dayNN/） | ✅ 已是「先给结论」house style 深稿（上轮管线产物），无 front-matter | 机检 + 补漏 + front-matter + 图片落位（增量润色） |
| M2 | `08、阶段八 就业指导课+拓展学习_20261025_235658/blog_jobguide` | `m2-jobguide` | 12 成稿（工作/市场/简历×2/面试×2/试用期×2/拓展×4）+ 8 merged 原料 | ✅ 同款深稿 | 机检 + 逐篇精修（量小可逐篇过）+ front-matter |
| M3 | `09、赠送-JavaEE中级进修课【包含十大中级项目】/blog` | `m3-javaee-10projects` | 1629 成稿 × 10 阶段（微服务技术/SaaS-HRM/好客租房/Hadoop3/黑马头条/冷链监控/探花交友/智慧学成/闪聚支付/万信金融）+ raw 双线转写 5198 | ✅ 同款深稿（抽样质量高），已知缺陷：15 篇坏图引用 | 批量机检 + 坏图处置 + front-matter + 重命名防冲突 |
| M4 | `10、赠送精英进阶【包含六大进阶项目】_20261029_122215` | `m4-advanced-6projects` | 1671 个 `_merged.md`（声音线+画面线朴素合并稿，**ASR 口播原稿，未润色**，均 ~8-130KB）+ manifest | ❌ 原始口播稿 | **重写级润色深化**：按项目/章节聚合成语义单元 → house style 重写（本课最大工作量，夜班分批） |

六大项目（manifest 实证）：含 品达物流TMS（阶段二）、智牛股（阶段三）、亿可控物联网监控、Drools 规则引擎、文件服务、常见组件与中台化 等；聚合映射以 manifest.json 的 stage 字段为准。

## 二、落点规划（遵循三段式 + COURSES.md 编号规则）

- **source**：`work/source/34.java-suite/`（m1/m2/m3/m4 四子目录，只读锁，排除 wav/audio_line/vision_line/materials-code）
- **target**：`work/target/34-java-suite/`（agent 主工作目录，四模块各一子目录 + _reports + STATE.md）
- **blog**：`work/blog/source/_posts/java-suite/`（单目录平铺，front-matter `categories: [java-suite, 模块N-xxx]` 区分模块；图片进 `source/images/java-suite/`）
- **编号**：34（33 已被 java-interview 占用）。COURSES.md 更新由最后一轮统一做。

## 三、front-matter 约定

```yaml
---
title: <文章标题>
date: 2026-11-18
categories:
  - java-suite
  - M1 面试专题   # M2 就业指导 / M3 十大中级项目 / M4 六大进阶项目
  - <章/项目名>
tags:
  - Java
  - <主题 tag>
---
```

## 四、断点与批次

见 STATE.md。批次划分：
- M1：拷贝校验 → 机检 → front-matter+改名(加 `m1-` 序号前缀防冲突) → _posts → 导航页（1-2 轮）
- M2：同上，逐篇过（1 轮）
- M3：批量脚本（重命名 `s01-0001-…` 格式）→ 机检 → front-matter → _posts（2-3 轮）
- M4：**重写流水线**：①解析 manifest 聚合映射 → ②按项目×章聚合单元 → ③逐单元重写（每轮 cron 处理一批，断点记录）→ ④机检进站（多轮）
- 收尾：hexo generate + 构建验证 + COURSES.md 编号 34 + 导航卡片 + 交付报告

## 五、红线

- 外置盘原件不动；source 只读；质量优先于速度；不主动 git push；卡片过机检才进 _posts。
- M4 重写以 merged 为原料骨架，剔除 ASR 口播腔/重复口水，事实以 vision 线与代码为准，不得编造课程没讲的内容。
