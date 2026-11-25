---
title: [RBL-711] Watch 模式的生命周期：持续会话中图结构的热更新与重跑优化
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-711：Watch 模式的生命周期：持续会话中图结构的热更新与重跑优化

**答**:
- watch 模式是「长会话状态机」：idle → invalidating（文件变更）→ building → 输出。与一次性构建的差异在于**图结构复用**：模块图/resolve 缓存/插件状态跨轮保留——这也让 watch 出现特有 bug 类别：跨轮状态泄漏（插件累积计数、缓存失效遗漏）导致「watch 越跑越慢/越跑越错」。
- 快速重跑的关键路径优化：1) 失效裁剪（RBL-636 最小失效集）；2) 增量 hash（只重算变更链的级联 hash）；3) 插件状态分区（插件声明 per-module 状态由构建器管理生命周期，防泄漏）。
- 配置变更的处理：watch 到构建配置文件变化 → 等价于重启会话（插件集合变），但**缓存可迁移**（模块级缓存键不含插件配置部分的可保留）——区分「结构性变更」与「参数性变更」。
- 队列合并语义：watch 中连续保存（编辑风暴）→ 多次失效合并为一轮构建（去抖 RBL-567）；构建中到来的失效 → 标记 dirty，本轮结束立即再跑（不中断当前轮——中断的收益小于完成一半的产物）。
- 追问钩子：为什么「中断重跑」在 watch 模式反而不是最优？——编辑风暴下每轮都被打断 = 永远出不了产物；「完成当前轮 + 立即追跑」的延迟下界更好（用户最后停手后一定能拿到最新产物）。而 dev server 请求驱动的场景（RBL-639）才适合打断重跑——语义取决于「消费者是文件系统还是浏览器」。

```javascript
class WatchSession {
  #dirty = new Set(); #building = null;
  async onFileChange(file) {
    this.#dirty.add(file);                               // 队列合并
    if (this.#building) return;                          // 构建中：标记即可，本轮结束追跑
    while (this.#dirty.size) {
      const batch = [...this.#dirty]; this.#dirty.clear();
      this.#building = this.rebuild(batch);              // 增量：最小失效集
      const result = await this.#building;
      this.#building = null;
      if (this.#dirty.size) continue;                    // 追跑最新变更
      emit('watch:done', result);
    }
  }
  async rebuild(files) {
    const { retransform, rechunck } = invalidateBatch(files, this.graph);
    await this.pipeline(retransform, { reuse: true });   // 图/缓存复用
    if (rechunck) this.chunker.rebalance();
    return computeHashes(this.chunks);                   // 增量级联 hash
  }
}
```
