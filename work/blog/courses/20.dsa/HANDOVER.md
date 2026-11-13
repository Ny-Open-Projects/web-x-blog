# DSA 项目交接文档

**交接时间：2026-11-11 23:52（CST）**
**当前状态：✅ 出版就绪（254 篇博客全部验证通过，详见 `_meta/ACCEPTANCE_REPORT.md` §30）**

---

## 1. 项目是什么

LeetCode 数据结构与算法题解语料库：**254 篇博客**（`blog_v2/`），每篇包含：

- LeetCode 官方题面 / 示例 / 数据范围 / 提示
- TypeScript 主讲解（1–6 种解法，逐步走读 + mermaid 控制流图 + 算法 GIF/SVG 动画）
- **11 语言附录**：Python / Go / Java / Rust / Lua / C / C++ / R / Zig / Dart（每种解法都有对应实现，自带测试用例，运行打印 PASS）
- 新手（🐣）/ 大佬（🦅）双阅读路线；API 速查表（4 列：参数/返回/复杂度/坑点）

```
dsa/
├── blog_v2/            # ★ 最终交付物：254 篇博客 + README.md 索引（102M，直接以此目录交付，不打包）
├── ts/ go/ python/ java/ rust/ lua/ c/ cpp/ r/ zig/ dart/   # 11 语言源码（每题 solution_N.lang，11,019 个文件）
├── _tools/             # 生成与验证工具链（见 §4）
├── _meta/              # 上游数据 + 验证报告（见 §5）
└── HANDOVER.md         # 本文档
```

---

## 2. 最终绿基线（2026-11-11 全量重跑，串行、未引用旧结论）

| 验证项 | 结果 |
|---|---|
| 11 语言代码本地运行 | 11,019 个 solution 文件全部 PASS |
| LeetCode 官方用例验证 | 123 ok / 0 fail / 79 skip（交互类/设计类无法本地注入） |
| blog_qa（8 维 P0/P1/P2） | 254 篇全部 0 问题 |
| code_review（存根/套套逻辑/空捕获等） | 0 真实问题 |
| expert_scan（16 规则 R1–R19） | 92 个残留项均已逐条 triage 为可接受 |
| publish_scan（出版规范 P1–P8） | 3 项为已文档化保留项 |
| omission_scan（原文遗漏） | 13 项为章节粒度残差，思路已回填 |
| mermaid 语法 | 11,068 块全部严格合规 |
| GIF 动画 | 1,254 个，0 异常 |

完整审计轨迹：`_meta/ACCEPTANCE_REPORT.md`（30 轮整改记录，§30 为出版就绪评估）。

---

## 3. ⚠️ 接手必读的既定约束（用户明确要求）

1. **串行执行，不并发**（"串行做，慢慢做"）。批量跑代码/扫描一律串行。
2. **`verify_new.sh` 绝不用于 java/ts/go/python**（它只服务 rust/lua/c/cpp/r/zig/dart 小语种）。java/ts/go/python 用 `verify_all.sh`。
3. **排版铁律：千万不能对现有代码格式换行等导致混乱的操作**。只允许真正的 AST 格式化工具（prettier/black/gofmt/rustfmt/clang-format/google-java-format/dart format/zig fmt/stylua/formatR），改完必须全量重跑验证。
4. 质量标准 >99/100。
5. 官方验证采用"两阶段候选扫描"：先在代表文件上探测候选注入形态，取通过官方用例的第一种，再全量套用（见 `verify_official.py` 的 split_named/_top_split，含无名输入 `输入：[7,1,5,3,6,4]` 的位置回退）。

---

## 4. 工具链（`_tools/`，清理后仅保留核心件）

| 工具 | 用途 | 用法 |
|---|---|---|
| `gen_blog.py` | 博客生成器 v6（真题面/真实方案名/mermaid 控制流） | `python3 gen_blog.py --force 253 0`（全量重生成 253 篇） |
| `annotate.py` / `langlib.py` / `svg_anim.py` / `svg_anim_extra.py` | gen_blog 依赖的注解与动画模块 | — |
| `extract_problem.py` / `fetch_official.py` | LeetCode GraphQL 抓题面 → `_meta/official_*` | — |
| `verify_official.py` | 官方用例注入验证（11 语言） | `python3 verify_official.py` → `_meta/official_verify.json` |
| `verify_all.sh` | 全语言本地运行验证（含 java/ts/go/python） | 逐语言执行，输出 `_meta/verify_report_*.txt` |
| `verify_new.sh` | 小语种验证（**勿用于 java/ts/go/python**） | — |
| `blog_qa.py` | 博客 8 维质量扫描 | → `_meta/blog_qa` 输出 |
| `code_review.py` | 结构化代码评审（存根/空捕获/危险 API） | → `_meta/code_review.json` |
| `expert_scan.py` | 数据结构专家语义扫描（R1–R19） | → `_meta/expert_scan.json` |
| `publish_scan.py` | 出版规范扫描（GB/T 标点/异形词/术语一致性） | → `_meta/publish_scan.json` |
| `omission_scan.py` | 爬取原文 vs 博客遗漏比对 | → `_meta/omission_scan.json` |

约定文档：`BLOG_CONVENTIONS.md`、`NEWLANG_CONVENTIONS.md`、`TRANSLATION_GUIDE.md`。

---

## 5. `_meta/` 数据说明（gen_blog 的上游依赖，勿删）

**必须保留**：`curriculum.json`（254 篇清单）、`problem_meta.json`、`official_meta.json`、`official_parsed.json`（官方题面解析）、`official_cases.json`、`official_verify.json`、`article_notes.json`（lc_787/lc_63 作者原文要点，注入 solution-1）、`all_urls.tsv`、`lc_slugmap.json`、`inventory.json`、`lc_imgs/`（题面配图源，gen_blog 引用）、`ACCEPTANCE_REPORT.md`、6 个扫描器 JSON 输出、11 个 `verify_report_*.txt`。

**已压缩**：`articles.tar.gz`（9.0M）＝ 原 76M 的 `_meta/articles/`（246 个 CSDN 爬取 HTML 原文，omission_scan 的数据源）。需要重跑 omission_scan 时先解压回 `_meta/articles/`。

---

## 6. 本次清理记录（2026-11-11 23:49–23:52）

**已删除**（全部先归档，可恢复）：

- 根目录陈旧副本：`gen_blog.py`（v4 旧版，正式版在 `_tools/`）、`diagnose_report.json`、旧版博客目录 `blog/`（v1，已被 blog_v2 取代）
- `_tools/` 一次性脚本与中间产物约 270 项：Sep–Oct 的 fix_* / convert_* / fetch_* 系列、chunks/batches/resume_batches×6/remediation_tasks/url_backfill_bak（15M）、`format_all_crude_2020.bak.disabled`（**历史上损坏过缩进的危险脚本**，切勿恢复使用）、gen_blog v2/v3 备份、浏览器扩展 zip、旧状态报告（RESUME_STATUS_* 等）
- `_meta/`：page*.html 爬取中间页、8 个历史日志、blog_v2_pilot、python_solutions
- 全部 `.DS_Store`、`__pycache__`、`*.pyc`
- **安全归档**：`/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa_cleanup_archive_2026-11-11.tar.gz`（3.3M，6,048 个条目，位于项目外，需要时解压恢复）

**未动**：`opencode-free-models/`、`.workbuddy/`、`.zcode/`（非本项目产物，归属不明，留给用户决定）。

清理后项目体积：约 280M → 176M。曾生成过交付 zip，按用户要求已删除：**交付以 `blog_v2/` 目录原样为准，不做压缩包**。

---

## 7. 已知残留（均为可接受项，已 triage，无需处理除非用户要求）

1. **mermaid 浏览器全量重渲染**：上次全渲染 11,068/11,068 成功；之后新增的 26 个含花括号标签块仅做了语法级验证（同构形态已被那次渲染覆盖）。若 node_repl/浏览器工具可用，可再做一次全量渲染确认。
2. **9 篇单题爬取文章**未被博客直接关联，其有价值内容已在 13 项 omission triage 中回填。
3. **verify_official 79 skip**：交互题（LC 374）、设计接口题（146/460/1797/341/933/429）等无法本地注入官方用例，属预期。
4. **publish_scan 3 项保留**、**expert_scan 92 项 triage**：逐条理由见 `ACCEPTANCE_REPORT.md` 对应章节。

---

## 8. 接手 Agent 常见操作速查

```bash
# 全量重生成博客（改了 gen_blog.py 或上游数据后）
cd /Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/_tools && python3 gen_blog.py --force 253 0

# 重跑官方验证
python3 verify_official.py

# 重跑某语言本地验证（串行）
bash verify_all.sh   # 按 .sh 内注释选择语言段

# 重跑六大扫描
python3 blog_qa.py && python3 code_review.py && python3 expert_scan.py \
  && python3 publish_scan.py && python3 omission_scan.py   # omission 前先解压 _meta/articles.tar.gz
```

**发布**：参考 `blog_v2/CSDN发布指南.md`（如果后续从 blog_v2 移除，见 ACCEPTANCE_REPORT §29 引用）。

> 最后一轮全量验证 = 2026-11-10 ~ 11-11 的"从零马拉松"（阶段 0–7），全过程记录在 `_meta/ACCEPTANCE_REPORT.md`。在那之后除本清理与打包外未改动任何博客/代码文件，绿基线仍然有效。
