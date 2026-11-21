---
title: [PER-322] 离线包占满用户磁盘怎么办？离线资源库的配额治理设计（版本淘汰 + 用量上报）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-322：离线包占满用户磁盘怎么办？离线资源库的配额治理设计（版本淘汰 + 用量上报）

**答**：
- 离线包（PWA 资源库/视频预载）是大头：一个业务离线包几十 MB，多版本堆积很快写爆配额。治理核心：**版本化分库 + 强制淘汰 + 用量自账**。
- 设计：每个离线包版本一个独立 Cache/IDB 库（`cache-v12/`），元数据表记录版本、大小、最后使用时间；下载新版本时删除旧版本（双版本窗口策略：最多保留当前 + 上一个，供回滚）；LRU 按业务优先级淘汰（核心包保护标记）。
- 用量自账：写入时按字节数记账（含 Blob size），预算制——离线库总预算（如 200MB）写满即停新增并提示；定期对账（estimate usage 与自账差异 > 20% 说明有泄漏，全量重建元数据）。
- 上报：每设备离线库用量/配额占比进 RUM，配额压力用户占比 > 5% 说明预算定太大；降级开关（服务端下发预算上限）。

```javascript
class OfflineStore {
  constructor({ budgetMB = 200, keepVersions = 2 }) {
    this.budget = budgetMB * 1048576; this.keep = keepVersions;
    this.meta = new Map();      // pkg -> [{version, bytes, lastUse}]
  }
  async install(pkg, version, download) {
    const used = [...this.meta.values()].flat().reduce((s, v) => s + v.bytes, 0);
    if (used + download.size > this.budget) {
      await this.#evict(download.size);         // 淘汰腾位
    }
    const cache = await caches.open(`pkg-${pkg}-v${version}`);
    await cache.put(`/${pkg}`, download);
    this.meta.get(pkg)?.push({ version, bytes: download.size, lastUse: Date.now() });
    await this.#dropOld(pkg);                   // 只留 keepVersions 个版本
  }
  async #dropOld(pkg) {
    const list = (this.meta.get(pkg) || []).sort((a, b) => b.version - a.version);
    for (const v of list.slice(this.keep)) { await caches.delete(`pkg-${pkg}-v${v.version}`); }
    this.meta.set(pkg, list.slice(0, this.keep));
  }
  async #evict(needBytes) { /* 按 lastUse 升序删非保护包，直到腾出 needBytes */ }
}
```
