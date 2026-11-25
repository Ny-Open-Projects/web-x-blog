# 34.java-suite 断点状态（✅ 已收官 2026-11-20）

> 本课程已全部完成并入站构建。终验记录见 `_reports/delivery.md`，课程登记见 `work/COURSES.md` 34 号行。
> 本文件转为归档参考；若需增量修改（如 M2 逐篇精修、演示口径脱敏），改 target 后跑 `python3 ai/scripts/ingest_java_suite.py sync` + hexo（node 22）即可。

## 终态
- M1 257 篇 ✅ / M2 12 篇 ✅ / M3 1629 篇 ✅ / M4 214 单元重写 ✅（QC 214/214 PASS）
- `_posts/java-suite` 2112 篇 + images 188 + demos 8；hexo 全量 14302 files 通过
- 导航页（courses/index.md + 根 index.md）34 号卡已补；COURSES.md 34 号行 + 计数基线 + 变更记录已登
- git: commit 1ac2faf5（含全站风格审计修复）已在远端；2026-11-21 二次 push a028994d 连带课程24/11收尾提交上远端——**任务 done**
- 保活 cron automation-e817b99e 使命完成（已删）

## 过程要点（复盘索引）
- 归档两坑：rsync 目标已存在会嵌套、先 chmod 只读会挡后续 mkdir → 脚本 v2 先拷后锁
- hexo 必须用 node 22（`export PATH="$HOME/.nvm/versions/node/v22.13.1/bin:$PATH"`）
- 子 agent 并发上限 1；死 agent 直接重派勿 SendMessage；34.java-suite 点号误写已写进 m4_mark_done.py 自愈（recover_stray）
- M4 QC 分级字数门槛（<40KB 单元 1200）；title 必须双引号；重名 video_id 23 条见 _dup_report.json
- 双会话并发推进以 _m4_state.json 为唯一事实源，尾部认领防撞车
