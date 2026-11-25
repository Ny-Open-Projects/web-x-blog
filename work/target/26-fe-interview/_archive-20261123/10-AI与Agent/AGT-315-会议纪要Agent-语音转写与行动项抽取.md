---
title: [AGT-315] 会议纪要 Agent——转写、区分发言人到行动项的管线？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-315：会议纪要 Agent（转写→纪要→行动项）怎么设计？

**答**:
- 管线三段：语音转写（ASR+说话人分离 diarization，多说话人场景必须分离否则纪要无归属）、结构化纪要（按议题分段：讨论要点/分歧/结论，引用说话人）、行动项抽取（谁/做什么/何时——三要素齐全才入行动项，缺要素标"待确认"，AGT-426 纪要规范的 AI 化）。
- 降噪与纠错：口语噪音处理（语气词/重复/跑题段过滤）、术语纠错（团队词表修正 ASR 术语错误）、指代消解（"那个方案"→具体名）——纠错词表可由用户维护。
- 隐私与留存：会议内容高敏——默认参会人可见、明确告知录音与 AI 处理、敏感会议（薪酬/绩效）建议不入库；留存期与删除权合规。
- 准确性兜底：数字/日期/人名在纪要中强制回听校验（锚到音频时间戳，可点击回放原话）——纪要错误的代价是执行错误，锚点回放是信任机制。

```javascript
async function meetingNotes(audio, roster) {
  const { segments, speakers } = await asr(audio,
    { diarization: true, vocab: teamVocab });
  const notes = await llm(`按议题分段：讨论/分歧/结论；
    行动项必须含谁/做什么/何时，缺则标待确认。
    术语表:${teamVocab}`, mapSpeakers(segments, speakers));
  return notes.map(anchorTimestamps);   // 每段锚音频时间戳
}
// 敏感词段（薪酬）→ 标记不入库。
```
