---
title: [AGT-539] 手写草稿 parts 模型：mention 校验、资产登记、序列化、长度预算？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-539：手写草稿 parts 模型：mention 校验、资产登记、序列化、长度预算

**需求与边界**：
- 输入：parts 数组（text/mention/image/file），mentions 与 assets 需登记校验；输出：协议字符串与预算检查。
- 边界要求：① mention 必须引用已校验对象（未选完的输入态拒绝发送）；② 图片需先上传拿 assetId（未上传完成阻塞发送并显示进度）；③ 总预算（文本字符 + 附件隐含 token）超限提示；④ 序列化转义正文中的伪标记（防用户文本里写 @kb: 被误解析）。

**答**：
```javascript
function serializeParts(parts, { maxChars = 20000 } = {}) {
  const out = []; let chars = 0; const assets = [];
  for (const p of parts) {
    if (p.type === 'text') {
      const t = p.value.replace(/@(kb|agent):/g, '@\$1:');  // 转义伪标记
      chars += t.length; out.push(t);
    } else if (p.type === 'mention') {
      if (!p.ref?.id) throw new Error('mention 未选完');       // 输入态校验
      out.push(`@${p.ref.kind}:${p.ref.id}`); chars += 8;
    } else if (p.type === 'image' || p.type === 'file') {
      if (!p.assetId) throw new Error('附件上传中');            // 阻塞发送
      assets.push(p.assetId);
      out.push(`[asset:${p.assetId}]`); chars += 500;           // 附件隐含预算
    }
  }
  const text = out.join('');
  if (chars > maxChars)
    throw new Error(`超出预算 ${chars}/${maxChars}，请精简或拆分提问`);
  return { text, assets, chars };
}
```

**评分点**:
- 发送前置校验完整：mention 未选完、附件未上传均阻塞并给出明确错误。
- 用户正文中的伪标记被转义（防注入解析错位）。
- 预算计入附件隐含 token，超限给出量化提示而非静默截断。

