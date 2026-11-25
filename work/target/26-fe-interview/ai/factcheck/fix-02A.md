# 修复记录：02A（8 条）

> 主会话于 2026-11-24 直接执行修复（修复 agent 被限流打断，改动已落盘并验证）。

## 已修
| 文件 | 改了哪一行（改后原文 ≤30 字） | 说明 |
|---|---|---|
| 02-框架与业务/FRP-170-React-18-的-selective-hyd.md | `let capturedEvents = [];` | const 声明后又重新赋值，运行即抛 Assignment to constant variable |
| 02-框架与业务/FRP-029-为什么-Hooks-不能写在条件语句或循环里.md | 「条件移进 hook 回调内部 `useEffect(() => { if (ready) ... })`」 | 原「`if (ready) useEffect(...)`」本身就是条件化调用 Hook，正是本题要禁止的写法 |
| 02-框架与业务/V3-501-长任务与Vue更新-时间切片边界.md | 「一次 patch 在单个微任务内完成」 | Vue 调度器 `Promise.then(flushJobs)` 派发，patch 在微任务里跑；原文写宏任务与同卡下文矛盾 |
| 02-框架与业务/FRP-178-React-Compiler-的自动-memoi.md | 产物形态改为「`const $ = _c(n)` 取槽 + 内联 `Object.is` 比对」 | `_c` 是 `useMemoCache` 别名，签名 `_c(n)`，不存在 `_c(deps, fn)` 形态 |
| 02-框架与业务/FRP-178-React-Compiler-的自动-memoi.md | `new Array(size).empty` → `new Array(size)` | Array 无 `empty` 属性，槽位恒 undefined，`$[0]` 即报错 |
| 02-框架与业务/FRP-111-流式-SSR-与选择性-hydration-是什.md | 「（18 的选择性 hydration 特性）」 | React 18 没有 selectNav 这个 API，属虚构名 |
| 02-框架与业务/FRP-109-HMR-在框架层是怎么实现的reactrefre.md | 「注入 `$RefreshReg$(type, id)` 与签名函数」 | react-refresh 运行时无 `registerSignature`，实际是 `$RefreshReg$`/`$RefreshSig$` |
| 02-框架与业务/V3-285-上传组件设计-分片-断点续传-直传凭证.md | 补 `let uploadedCount = 0;` | 变量全篇未声明，严格模式下 `++uploadedCount` 直接 ReferenceError |

## 驳回
| 文件 | 报告说的片段 | 为什么其实没错 |
|---|---|---|
| — | 无 | 8 条需修均复核属实并修复 |

校验：被改卡片的 js 代码块已通过 `node --check`（FRP-029 的 JSX 片段豁免）。
