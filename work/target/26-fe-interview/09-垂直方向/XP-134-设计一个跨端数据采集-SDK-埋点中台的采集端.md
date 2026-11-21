---
title: [XP-134] 设计一个跨端数据采集 SDK（埋点中台的采集端）？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-134：设计一个跨端数据采集 SDK（埋点中台的采集端）？
**答**：
- 架构分层：**采集器（事件源：点击/曝光/PV/自定义/性能）→ 处理管线（校验、补全、采样、脱敏）→ 队列缓冲（内存环形 + 落盘持久）→ 上报器（批量压缩、多通道、退避重试）**；插件化管线便于扩展（XP-058 采集适配的架构升级版）。
- 数据质量优先：事件 schema 校验（坏数据丢弃+计数，不静默污染）、公共属性自动补全（XP-111 日志同款公共字段）、时间戳统一 UTC + 单调时钟序号防端上改表乱序。
- 上传策略：批量（50 条/5s 触发）+ gzip、场景分级（error 即时、行为攒批、性能定时）、退避重试与磁盘上限（超限丢弃低优先级）、网络分型（蜂窝降采样）。
- 可靠性语义：至少一次（落盘重发）+ messageId 幂等去重（服务端）；关键事件（转化）与普通事件分级保障。
- 性能与合规红线：主线程零阻塞（采集入队 O(1)、序列化在后台）、初始化 defer（XP-077 启动纪律）、隐私合规（脱敏白名单、用户可关闭采集开关、GDPR 删除权接口）。

```typescript
// packages/track/sdk —— 插件化管线：采集 → 处理 → 缓冲 → 上报
interface PipelinePlugin { name: string; process(e: TrackEvent): TrackEvent | null; }

export class TrackSDK {
  #queue = new RingBuffer<TrackEvent>(2000);      // 内存环形缓冲
  constructor(private plugins: PipelinePlugin[], private transport: Transport) {}

  track(name: string, props: Props, level: 'normal' | 'critical' = 'normal') {
    let e: TrackEvent = { name, props, tsUtc: new Date().toISOString(), seq: monotonicSeq() };
    for (const p of this.plugins) {               // 管线：校验→补全→采样→脱敏
      const out = p.process(e);
      if (!out) return;                           // 坏数据/被采样剔除：丢弃+计数，不污染
      e = out;
    }
    this.#queue.push(e);
    if (level === 'critical' || this.#queue.size >= 50) this.#flush();
    else scheduleFlush(5_000);                    // 5s 攒批
  }

  async #flush() {
    const batch = this.#queue.drain(50);
    if (!batch.length) return;
    const body = gzip(JSON.stringify(batch));     // 批量压缩
    try { await this.transport.send(body); }
    catch {
      await this.#persist(batch);                 // 失败落盘，退避重发（至少一次）
      backoff(() => this.#flush());
      if (diskUsage() > LIMIT) this.#queue.dropLowPriority();  // 磁盘上限保护
    }
  }
}
// 内置插件：schemaValidator / enrich(公共字段自动补全) / sampler(蜂窝降采样) / mask(脱敏)
// 红线：入队 O(1) 零主线程阻塞；初始化走 defer（XP-077）；用户可关闭采集+删除权接口
```
