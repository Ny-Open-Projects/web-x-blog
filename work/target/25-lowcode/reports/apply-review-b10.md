# 批10（35 张知识卡）审核修正落地记录（2026-11-19）

来源：review-b10-cards.md（P1×24 / P2×22）。
- 机械批量：getCacheData→getCachedData（4 文件）、generatorComponent→generateComponent、/resource→/resources、request:code:→register:code:、isScan 布尔→'no'/'yes' 字符串（practice-03/04/09、interview-03、README）。
- 缓存口径族：principle-04/practice-09/interview-03 force 语义改「置空回写并非显式 del」+ TTL 600s + 「最终仓库注释态、线上走无缓存版」限定（面试保命句）。
- 事务/问卷族：principle-03 主流程改「保留 component_data」+ 按 account_id 查 + err 只进日志注；concept-08/05 四列口径 + 组件 id 在 props[].id + 孤儿行口径。
- 字段/契约：NodeContract 五字段（去 ports/execute 假字段）、端口 7 种、types/local.ts→share types/request/、15 组件清单 titleText/textArea、CORS 全开待补项、防枚举预先课口径、@Catch(HttpException)、mobx-shallow-undo 整 store 深拷贝取舍、微信回调注释态注、OSS IDOR 顺序隐患、upload_files、componentExport、键盘快捷键（去排序）、缓存压缩待补项、拖拽 distance:2 阈值口径。
- 同步：cards → blog/_posts/xiaodi-lowcode-cards `diff -rq` 校验一致（README 不进站）。
