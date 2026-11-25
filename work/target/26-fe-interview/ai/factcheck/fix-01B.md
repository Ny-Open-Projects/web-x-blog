# 修复记录：01B（6 条）

> 主会话于 2026-11-24 直接执行修复（修复 agent 被限流打断，改动已落盘并验证）。

## 已修
| 文件 | 改了哪一行（改后原文 ≤30 字） | 说明 |
|---|---|---|
| 01-语言与基础/JS-384-并发原语组合模式-限流加重试加熔断.md | `if (++fails >= threshold) openedAt = ...` | `===` 只在恰好等于阈值时刷新 openedAt，冷却后再失败永不续期、熔断永不重开 |
| 01-语言与基础/JS-295-笔试-手写-深拷贝补充函数字段.md | 补 `if (!('value' in d)) { defineProperty(out, k, d); continue; }` | 访问器属性展开后带 `value: undefined`，defineProperty 抛 TypeError；访问器原样复制 |
| 01-语言与基础/JS-401-笔试-手写串行执行队列锁.md | 补 `const next = this.#pending[0]; if (next !== task) return;` | shift 返回值被丢弃，clear 后被清任务仍执行，与「clear 清空未执行任务」矛盾 |
| 01-语言与基础/WEB-596-笔试-手写进程崩溃检测的心跳探针.md | `start()` 先 `_checkCrash()` 再写心跳起定时器 | 原顺序先写新心跳再检测，gap≈0 永不触发崩溃判定 |
| 01-语言与基础/WEB-633-笔试-手写SIMD特性分发加载器.md | 探测字节 `252,12` → `253,12`（v128.const = 0xFD 0x0C） | 0xFC 是 misc 前缀，字节非法，`WebAssembly.validate` 恒 false，SIMD 版永不加载（Node 实测修复后 validate=true） |
| 01-语言与基础/WEB-636-笔试-手写WASM模块缓存管理器.md | `const final = p.finally(() => this.inflight.delete(key));` | 失败路径 inflight 不清理，rejected promise 永久占据 key，模块被无限期熔断 |

## 驳回
| 文件 | 报告说的片段 | 为什么其实没错 |
|---|---|---|
| — | 无 | 6 条需修均复核属实并修复 |

校验：被改卡片的 js 代码块已通过 `node --check`。
