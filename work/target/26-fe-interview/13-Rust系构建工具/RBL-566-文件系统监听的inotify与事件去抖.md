---
title: [RBL-566] 构建工具的文件监听实现：inotify/FSEvents 差异与去抖策略
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-566：构建工具的文件监听实现：inotify/FSEvents 差异与去抖策略

**答**：
- 各平台原生机制不同：Linux inotify（每文件 fd，需处理 watch 上限 fs.inotify.max_user_watches）、macOS FSEvents（目录级粗粒度事件，递归免费但延迟较高且事件粒度是目录）、Windows ReadDirectoryChangesW（目录递归但缓冲区可能溢出）——notify crate 统一抽象，但语义差异要构建器自己抹平。
- 关键事件缺陷与对策：1) **编辑器写文件是多次事件**（vim/原子保存产生 create+rename+write）→ 去抖合并（150~300ms 窗口）后按路径去重；2) rename 无法区分移动目标 → 用「消失+出现」配对启发；3) 目录树大变更（git checkout 切分支）产生事件风暴 → 批量失效 + 单次重建。
- 粒度策略：watch 粒度从「所有源文件」到「模块图依赖闭包内的文件」——构建器只需监听已解析模块 + 动态 import 候选目录；node_modules 默认不 watch（预构建产物除外，vite 的 optimizeDeps 失效检测另走 hash）。
- 事件→失效映射：路径 → 模块 id → 依赖反向边失效传播（参见 RBL-526 一轮）——watcher 只是传感器，失效传播在图上做。
- 追问钩子：FSEvents 目录事件如何映射回具体文件？——对比事件前后目录快照（mtime/size 缓存）或直接全量 hash 该目录下模块；这也是 macOS 上 HMR 略慢于 Linux 的原因之一。

```javascript
// watcher 去抖与失效映射（概念实现）
class DebouncedWatcher {
  #pending = new Map(); #timer = null;
  onRaw(ev) {
    const key = ev.path;                       // 同路径多次事件合并
    const prev = this.#pending.get(key);
    this.#pending.set(key, { kind: mergeKind(prev?.kind, ev.kind), at: Date.now() });
    clearTimeout(this.#timer);
    this.#timer = setTimeout(() => this.flush(), 200); // 去抖窗口
  }
  flush() {
    const batch = [...this.#pending.entries()]; this.#pending.clear();
    const ids = batch.map(([p]) => this.graph.pathToModule(p)).filter(Boolean);
    // 事件风暴保护：>50 个模块失效 -> 走全量重建而非逐个 HMR
    if (ids.length > 50) this.builder.rebuildAll();
    else ids.forEach(id => this.builder.invalidate(id));
  }
}
const mergeKind = (a, b) => (a && b && a !== b ? 'change' : (a || b)); // create+write -> change
```
