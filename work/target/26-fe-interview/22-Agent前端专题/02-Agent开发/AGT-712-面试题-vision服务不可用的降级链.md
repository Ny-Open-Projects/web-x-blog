---
title: [AGT-712] vision 模型限流/故障时，多模态问答的降级链怎么设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-712：vision 模型限流/故障时，多模态问答的降级链怎么设计

**答**：
- 降级三级：① 用已缓存的描述/提取结果（入库时缓存的 caption/dataJson 承担 80% 场景）；② OCR 兜底（纯文字提取代替完整理解，回答质量降但可用，UI 明示"降级模式"）；③ 拒答该部分并保留文字能力（"图片理解服务暂不可用，文字问题不受影响"）。
- 降级决策在网关层（健康检查+熔断），前端只感知降级标记并渲染提示；恢复后自动回主链路。
- 降级期间的请求要记账：降级率是 vision 容量规划的输入。

```javascript
async function visionWithFallback(img, task) {
  if (circuit.closed('vision')) {
    const cached = descCache.get(img.id);
    if (cached) return { ...cached, degraded: 'cache' };
    const ocr = await ocr(img);                    // OCR兜底
    return { text: ocr.text, degraded: 'ocr',
      note: '图片理解降级，仅提取文字' };
  }
  return vision(img, task);                        // 主链路
}
```

