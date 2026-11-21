---
title: [AGT-333] 实时视频流 Agent——直播/监控场景怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-333：对实时视频流（直播/监控）做理解的 Agent 怎么设计？

**答**:
- 成本与采样：全帧 VLM 调用成本不可接受——分层采样：轻量检测模型（专用小模型/规则：运动检测/人脸/物体检测）做 24/7 低成本扫描，触发条件（异常事件）才唤起 VLM 深度分析——"便宜哨兵+昂贵专家"两级架构。
- 事件理解：触发后的 VLM 分析输出结构化事件（时间戳/描述/置信度/截图证据），事件流进下游（告警/审核/摘要）；时间维度的连续理解靠关键帧序列而非逐帧。
- 实时性权衡：告警类场景延迟敏感（秒级）用小模型+规则快判，深度分析异步补充（先告警后细化）；摘要类场景（直播高光）可批处理。
- 评测与误报治理：小模型哨兵的召回率/误报率持续监控（误报多则 VLM 调用成本失控），阈值动态调；事件准确率用抽检标注评估。

```javascript
function videoPipeline(stream) {
  stream.pipe(detectCheap);                 // 24/7 廉价扫描
  detectCheap.on('event', async ev => {     // 触发式深析
    const frames = pickKeyFrames(ev, 5);
    const analysis = await vlm(frames,
      { schema: EVENT_SCHEMA });            // 结构化事件
    emit({ ...analysis, evidence: frames });
  });
}
// 误报率监控 → 哨兵阈值动态调；
// 告警快判（小模型）+ 深析异步（VLM）。
```
