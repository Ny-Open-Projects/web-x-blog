---
title: [PER-669] 手写一个离线包差量更新校验器：bsdiff patch 应用前后的完整性校验与回滚
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-669：手写一个离线包差量更新校验器：bsdiff patch 应用前后的完整性校验与回滚

**答**：
- 差量流程：服务端下发 `oldVersion -> newVersion` 的 patch 文件，客户端校验 patch 签名 -> 应用 patch 生成新包 -> 全量 hash 校验 -> 原子切换；任一步失败回滚旧包并全量下载兜底。
- 要点：patch 校验三重——patch 自身签名、patch 的 base 版本匹配（本地版本号必须等于 patch.baseVersion）、结果包整体 hash 与 manifest 一致；失败计数（连续 3 次差量失败降级为只走全量）。
- 边界：磁盘空间校验（应用 patch 需要双份空间）；应用过程不阻塞页面（后台执行）。
- 评分点：base 版本匹配与差量失败降级。

```javascript

class DiffUpdater {
  constructor(bridge) { this.failCount = 0; this.bridge = bridge; }
  async update(route, patch) {
    if (this.failCount >= 3) return this.fullUpdate(route);     // 差量降级全量
    const localV = await this.bridge.getLocalVersion(route);
    if (patch.baseVersion !== localV.version)
      return this.fullUpdate(route);                            // base 不匹配，放弃差量
    const sigOk = await this.bridge.verifySignature(patch.url, patch.sig);
    if (!sigOk) throw new Error('patch 签名失败');
    const free = await this.bridge.freeDisk();
    if (free < patch.size * 3) return this.fullUpdate(route);   // 双份空间不够
    const newDir = await this.bridge.applyPatch(patch.url, localV.dir, route);  // 后台执行
    const hashOk = await this.verifyDir(newDir, patch.targetManifest);
    if (!hashOk) {
      await this.bridge.remove(newDir);                         // 回滚
      this.failCount++;
      return this.fullUpdate(route);
    }
    await this.bridge.switchVersion(route, newDir);             // 原子切换
    this.failCount = 0;
    return { ok: true, version: patch.targetVersion };
  }
  async fullUpdate(route) {
    const m = await fetch(`/offline/full/${route}`).then(r => r.json());
    await this.bridge.downloadAndExtract(m.url, route);
    return { ok: true, version: m.version, via: 'full' };
  }
}
```
