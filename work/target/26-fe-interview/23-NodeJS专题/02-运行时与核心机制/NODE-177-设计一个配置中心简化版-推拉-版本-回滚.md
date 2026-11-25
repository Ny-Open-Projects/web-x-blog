---
title: [NODE-177] 设计一个配置中心简化版（推拉/版本/回滚）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-177：设计一个配置中心简化版（推拉/版本/回滚）？
**答**：
- 与 NODE-150（协议与服务端核心）互补，本题补**客户端收敛与防呆**：本地 last-good 快照兜底、变更过 schema 校验才热更、配置本身支持灰度推送。
- 版本化：每次发布不可变快照 + 指针；回滚秒级（指回旧版本），全程审计留痕。
- 客户端姿态：启动拉全量 → 长轮询监听变更 → 内存热更 + 发本地事件（业务模块订阅）；配置中心不可用时用本地快照继续跑。
- 安全：敏感配置加密存储、客户端凭据鉴权、按环境物理隔离。

```javascript
// 客户端收敛实现
class ConfigClient {
  #listeners = new Map();
  async start() {
    this.snapshot = await fetch(`${CENTER}/configs/all`).then((r) => r.json())
      .catch(() => loadLocalSnapshot());           // 中心挂了用 last-good
    this.watchLoop();                               // 长轮询监听（NODE-150）
  }
  get(key) { return this.snapshot[key]; }
  onChange(key, fn) { this.#listeners.set(key, fn); }
  async #watchLoop() {
    while (true) {
      const r = await fetch(`${CENTER}/watch?version=${this.version}`)
        .then((r) => (r.ok ? r.json() : null)).catch(() => null);
      if (r) {
        const fresh = await fetch(`${CENTER}/configs/all`).then((r) => r.json());
        EnvShape.parse(fresh);                      // schema 校验（NODE-155）防呆
        const prev = this.snapshot;
        this.snapshot = fresh; saveLocalSnapshot(fresh);
        this.#listeners.forEach((fn, k) => fresh[k] !== prev[k] && fn(fresh[k]));
      }
    }
  }
}
```
