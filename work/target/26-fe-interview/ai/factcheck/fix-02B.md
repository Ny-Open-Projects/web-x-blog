# 修复记录：02B（6 条）

> 修复 agent 于限流前完成，主会话核验落盘。

## 已修
| 文件 | 改了哪一行（改后原文 ≤30 字） | 说明 |
|---|---|---|
| 02-框架与业务/FRP-381-笔试-手写createRoot通用挂载器.md | 三元分支改 IIFE `(() => { throw ... })()` | throw 是语句不能进三元分支，整段无法解析 |
| 02-框架与业务/FRP-386-笔试-手写hook链表执行器.md | `let currentFiber = null, hookIndex = 0;` | 原声明的是 currentIndex，`currentFiber = fiber` 直接 ReferenceError；并把赋值挪进循环体开头保证 StrictMode 双跑可用 |
| 02-框架与业务/FRP-376-笔试-手写toRaw与依赖图遍历.md | `Array.isArray(raw) ? raw.slice() : { ...raw }` | 数组分支建空数组后按自有键遍历恒为空，toRaw 对数组恒返回 `[]` |
| 02-框架与业务/R19-434-笔试-手写useMediaQuery与useEventListener.md | 初值固定 `useState(false)`，真实值由 useEffect 校正 | 惰性初值在水合首帧读 matchMedia 与服务端 false 不一致 → 水合不匹配 |
| 02-框架与业务/MP-399-笔试-手写分层mock用例.md | `mockWxMethod` 移到 tap 之前 | mock 注册在支付调用之后，mock 不生效、用例必挂 |

## 驳回
| 文件 | 报告说的片段 | 为什么其实没错 |
|---|---|---|
| — | 无 | 6 条需修均复核属实并修复 |

校验：被改卡片的 js 代码块已通过 `node --check`。
