---
title: [PER-516] 手写一个 Lighthouse 自定义审计：检测页面是否存在超过 200KB 的未压缩 JS 资源
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-516：手写一个 Lighthouse 自定义审计：检测页面是否存在超过 200KB 的未压缩 JS 资源

**答**：
- Lighthouse 自定义审计继承 `Audit` 类，实现 `static get meta()`（id、标题、评分模式）与 `static audit(artifacts)`。
- 要点：从 `devtoolsLogs` 网络工件里过滤 script 资源，比较 transferSize 与 resourceSize 推断压缩率；评分模式用 `numericValue` 生成 0-1 分。
- 边界：transferSize 为 0（缓存或跨域无 TAO）的样本要跳过，避免误判。
- 评分点：meta 三要素是否完整、scoring 是否用正确的 gatherer 工件。

```javascript

const { Audit } = require('lighthouse');
const NetworkRecords = require('lighthouse/core/audits/audit.js');

class BigJsAudit extends Audit {
  static get meta() {
    return {
      id: 'big-uncompressed-js',
      title: '未压缩的超大 JS',
      failureTitle: '存在超过 200KB 的未压缩 JS',
      description: '检测 transferSize/resourceSize 比值异常的脚本资源',
      requiredArtifacts: ['devtoolsLog', 'networkRequest'],  // 声明依赖工件
      scoringMode: Audit.SCORING_MODES.NUMERIC,
    };
  }
  static audit(artifacts, context) {
    const LIMIT = 200 * 1024;
    const offenders = artifacts.networkRequest.filter(req =>
      req.resourceType === 'Script' &&
      req.transferSize > 0 &&                                // 缓存/无 TAO 的样本跳过
      req.resourceSize > LIMIT &&
      req.transferSize / req.resourceSize > 0.7              // 压缩率 < 30% 视为未压缩
    ).map(r => ({ url: r.url, size: +(r.resourceSize / 1024).toFixed(0) + 'KB' }));
    return {
      numericValue: offenders.length,
      score: offenders.length === 0 ? 1 : Math.max(0, 1 - offenders.length * 0.2),
      displayValue: offenders.length ? `${offenders.length} 个超大未压缩脚本` : '',
      details: BigJsAudit.makeTableDetails([{ key: 'url' }, { key: 'size' }], offenders),
    };
  }
}
module.exports = BigJsAudit;
```
