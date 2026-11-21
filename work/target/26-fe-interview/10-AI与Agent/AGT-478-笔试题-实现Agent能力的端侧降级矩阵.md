---
title: [AGT-478] 笔试题——实现端侧能力探测与降级矩阵（设备分档+能力协商）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-478：手写端侧降级矩阵：设备能力探测、模型分档、功能降级链

**需求与边界**：
- 输入：设备环境（WebGPU/内存/网络）；输出：可用能力集与降级方案。
- 边界要求：① 能力探测（WebGPU 可用性/显存估算/网络质量）；② 模型分档选择（端侧小模型按内存档位）；③ 功能降级链（本地推理→云端推理→预计算缓存→文本兜底）；④ 探测结果缓存与网络变化监听重协商。

**答**：
```javascript
async function capabilityMatrix(env) {
  const caps = {
    webgpu: !!env.gpu,
    vramMB: env.gpu ? await estimateVRAM(env.gpu) : 0,
    ramMB: env.deviceMemory * 1024,
    net: env.connection?.effectiveType ?? '4g',
    online: env.onLine,
  };
  // 模型分档：按显存/内存选端侧模型
  const model = caps.webgpu && caps.vramMB > 4000
    ? { tier: 'local-3b', where: 'local' }
    : caps.ramMB > 4000
      ? { tier: 'local-1b', where: 'local' }
      : { tier: null, where: 'cloud' };
  // 功能降级链
  const features = {
    chat: model.tier ? 'local' : caps.online ? 'cloud' : 'cache',
    imageDesc: caps.webgpu ? 'local' : caps.online
      ? 'cloud' : 'unavailable',
    realtimeVoice: caps.webgpu && caps.net !== 'slow-2g'
      ? 'enabled' : 'disabled',
  };
  const fallback = (feature) => ({                  // 降级链查询
    chat: ['local', 'cloud', 'cache', 'text_only'],
    imageDesc: ['local', 'cloud', 'unavailable'],
  }[feature] ?? []);
  return {
    caps, model, features, fallback,
    // 网络变化重协商
    watch: (onChange) => env.connection?.addEventListener(
      'change', () => onChange(capabilityMatrix(env))),
    // 探测缓存（会话内不重复探测）
    ttl: 3600e3,
  };
}
// 呈现：不可用功能说明原因（设备/网络），
// 降级模式明确标注（"离线模式，仅本地知识"）。
```

**评分点**:
- 能力探测多维（GPU/显存/内存/网络/在线）且分档选模型。
- 功能降级链逐级兜底（local→cloud→cache→text）。
- 网络变化监听重协商 + 探测缓存。
- 降级模式用户知情呈现（不可静默劣化）。
