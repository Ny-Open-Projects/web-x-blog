# 修复记录：07（4 条）+ 连带发现（1 条）

> 主会话于 2026-11-24 18:40 前后直接修复，全部通过 `node --check`。

## 已修
| 文件 | 改了哪一行（改后原文 ≤30 字） | 说明 |
|---|---|---|
| 07-架构与设计/DP-121-如何用-Suspense-模式重构loading.md | 「React 19 的 use() / 框架级 suspense 数据源已内置该机制」 | `use()` 是 React 19 才稳定的 API，原文写 React 18 且与同卡追问 3 冲突 |
| 07-架构与设计/DP-418-插件系统的模式组合.md | `on` 改为 `if (!has) set(...); get(hookName).push(fn)` | `Map.set()` 返回 Map 本身而非数组，首次注册钩子对 Map 调 `.push` 直接 TypeError |
| 07-架构与设计/DP-418-插件系统的模式组合.md | 补声明 `#facade()` 私有方法 | 修复时通读代码发现的连带问题：`use()` 里 `this.#facade()` 引用了未声明的方法 |
| 07-架构与设计/ARC-332-笔试题实现组件库的-Form-校验引擎.md | 删除 `startsWith('.')` filter | 拼接路径恒以 `.` 开头，filter 把校验结果全滤空，validate 从不校验任何字段 |
| 07-架构与设计/ARC-075-监控-SDK-的整体架构如何设计-采集-聚合-上.md | `if (!navigator.sendBeacon?.(...)) fetch(...)` | `??` 只对 null/undefined 回退，sendBeacon 失败返回 false，fetch+keepalive 兜底永不执行，卸载批次静默丢失 |

## 驳回
| 文件 | 报告说的片段 | 为什么其实没错 |
|---|---|---|
| — | 无 | 4 条需修均属实；第 5 条为修复时连带发现 |
