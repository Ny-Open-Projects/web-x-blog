---
title: [AGT-730] 把多模态检索做成 Agent 工具（看图/读表工具）相比固定管线的优势与设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-730：把多模态检索做成 Agent 工具（看图/读表工具）相比固定管线的优势与设计

**答**：
- 做成工具让 Agent 决定「何时看图、看哪部分」：复杂问题（"对比图 2 和图 5 的架构差异"）需要多次定向看图（裁剪指定区域再看），固定管线一次塞原图做不到。
- 工具集设计：read_image(区域裁剪)、read_table(行列投影)、read_chart(数据提取)、watch_segment(视频段转写)；每个工具返回结构化结果+置信度，Agent 据此决定是否再看一次。
- 成本护栏：工具调用次数上限+每工具预算（防止 Agent 对一张图反复看 10 次），可观测里单独计量多模态工具成本。

```javascript
const MM_TOOLS = [
  { name: 'read_image', args: { assetId, region? }, budget: 3 },
  { name: 'read_table', args: { assetId, rows?, cols? } },
  { name: 'read_chart', args: { assetId } },
  { name: 'watch_segment', args: { videoId, t0, t1 } },
];
async function runTool(call) {
  const result = await tools[call.name](call.args);  // 区域裁剪/投影
  meter.count(`mm.tool.${call.name}`, { tokens: result.usage });
  if (meter.exceeded(call.name))                    // 预算护栏
    return { ...result, truncated: true,
      note: '查看次数已达上限，基于已有信息回答' };
  return result;
}
```

