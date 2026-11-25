# 精讲 100 题核查结果

核查范围：`_prep/05-精讲100题.md` 全文 1960 行、100 篇（01-语言与基础 18 / 02-框架与业务 14 / 03-场景实战 7 / 04-工程化与构建 8 / 05-性能与安全 12 / 06-算法与手写 15 / 07-架构与设计 8 / 08-服务端与全栈 5 / 09-垂直方向 3 / 10-AI与Agent 3 / 11-软技能 5 / 12-状态管理 2，分篇数与表头一致）。
整体质量高：30 秒版与追问链结论一致，未发现自相矛盾；无「token 存 localStorage 称安全」「CSP 上 unsafe-inline 当最佳实践」这类危险误导；`Cache-Control: no-cache`（可缓存但须验证）、TCP 队头阻塞与 QUIC 多流、微任务清空才能渲染、`useEffect` 在 paint 后、`Object.defineProperty` vs `Proxy`（JS-295 只讲拷贝，未涉此对比）等关键结论均正确。

## 需修（置信度高）

| 题号 | 原文片段（≤30字，要能 grep 到） | 问题 | 精确改法 |
|---|---|---|---|
| ARC-124 | `monorepo 用 workspace 分项目避免复制` | **过时 API**。Vitest 官方文档明确：`workspace` 自 **3.2** 起已废弃（deprecated），由 `test.projects` 取代，`vitest.workspace.ts` 不再是推荐写法（CLI 亦为 `--project`）。2026 年照此答会被面试官纠正。 | 改为「monorepo 在根配置用 `test.projects: ['packages/*']` 分项目、避免复制配置；`workspace` 自 3.2 起已废弃，`--project` 过滤」。 |
| BLD-030 | `开 \`concatenatedModules\` 看合了谁` | **API 名错 + 用途错**。webpack 无 `concatenatedModules` 选项（未知键被静默忽略）；正确名是 `optimization.concatenateModules`（boolean/object，production 默认 true）。且它是「开启作用域提升」，不是「查看合并了谁」。 | 改为「配置项是 `optimization.concatenateModules`（production 默认开，5.109+ 支持 `{commonjs:false}` 只拼 ESM）；要看合并结果读 stats 的 `modules[].modules` 与 `optimizationBailout`」。 |
| BLD-082 | `降到 es5 以下它就不支持` | **事实说反**。esbuild 的降级管线只到 **ES2015**（官方 FAQ 描述该 pass 为 "ESNext-to-ES2015"），根本不支持 ES5 输出：`target: 'es5'` 遇到 class/箭头函数等会直接报 "Transforming … to the configured target environment (es5) is not supported"。原文让读者以为「ES5 可用、只是更低不行」，方向相反。 | 改为「esbuild 最低只降到 ES2015，连 `target: 'es5'` 都会直接报错；要兼容 ES5 只能换 Babel（或对产物再过一遍 Babel）」。 |
| BLD-081 | `API 三个：transform、build、serve` | **API 过时/名错**。esbuild 顶层 JS API 是 `build`、`transform`、`context`（另有 `initialize`）；`serve` 自 0.17 起已不是顶层函数，而是 context 的方法 `ctx.serve()`（`ctx.watch()` 同理）。 | 改为「三个入口：`transform`（字符串级转译）、`build`（打包写盘）、`context`（增量构建，`ctx.watch()` / `ctx.serve()` 挂在它上面）」。 |

## 存疑

| 题号 | 原文片段 | 疑点 |
|---|---|---|
| BLD-073 | `靠 HTTP/2 多路复用缓解` | Vite dev server 默认走 **HTTP/1.1**（只有配 `server.https` 才协商 h2）。默认配置下「海量小请求」靠的是浏览器每域约 6 个并发连接 + 预构建合并，而非 h2 多路复用；这句容易被追问「你开了 h2 吗」。建议改成「默认 HTTP/1.1 下靠预构建合并请求 + 浏览器并发上限，项目自建 https 时可上 h2」。 |
| PER-960 | `cls 取中位数` | Core Web Vitals 三个指标统一按 **p75** 口径（web-vitals 库上报的就是 p75），CLS 单独取中位数与业界口径不一致，跟同篇追问里「P75 是 CWV 常用口径」也略有张力。若确为周报自定义口径，需要在文中写明「本报表对 CLS 用中位数，与线上 CWV 的 p75 口径不同」。 |
| BLD-069 | `Vite 生产构建底座就是它` | Vite 正在向 Rolldown 迁移（rolldown-vite），「生产构建底座就是 Rollup」在 2026 年取决于具体大版本，建议按版本表述，避免被反问「Vite 8 不是换 Rolldown 了吗」。 |
| NODE-074 | `BullMQ 的 repeatable job` | BullMQ 5.16+ 已推出 Job Schedulers（`upsertJobScheduler`），`repeat` 选项标记为 deprecated。答 repeatable job 不算错但偏旧，可顺带提「新版本用 Job Schedulers 替代 repeat」。 |

## 覆盖确认

[H5-371] [H5-293] [H5-124] [JS-092] [WEB-102] [WEB-115] [JS-121] [JS-124] [JS-161] [CSS-189]
[WEB-266] [WEB-280] [JS-295] [JS-344] [JS-358] [WEB-566] [WEB-609] [WEB-636] [V3-250] [FRP-004]
[FRP-025] [FRP-046] [FRP-049] [FRP-097] [FRP-109] [FRP-111] [FRP-145] [FRP-152] [FRP-160] [FRP-292]
[FRP-303] [MP-375] [SCN-048] [SCN-209] [SCN-217] [SCN-277] [SCN-284] [SCN-520] [SCN-651] [BLD-030]
[BLD-069] [BLD-073] [BLD-081] [BLD-082] [BLD-086] [BLD-304] [BLD-312] [OPT-025] [OPT-060] [PER-101]
[PER-118] [PER-120] [OPT-139] [OPT-192] [PER-197] [PER-224] [PER-554] [PER-960] [PER-1243] [HW-073]
[HW-229] [HW-235] [HW-260] [HW-303] [HW-310] [ALG-318] [HW-321] [HW-353] [HW-367] [ALG-386]
[ALG-390] [HW-410] [ALG-520] [ALG-550] [DP-001] [ARC-043] [ARC-058] [ARC-124] [ARC-322] [ARC-325]
[ARC-432] [ARC-548] [NODE-052] [NODE-074] [NODE-088] [NODE-146] [NODE-731] [XP-016] [XP-055] [VIZ-324]
[AGT-198] [AGT-200] [AGT-451] [SOFT-004] [SOFT-006] [SOFT-076] [SOFT-085] [SOFT-100] [ZSM-750] [ZSM-805]
