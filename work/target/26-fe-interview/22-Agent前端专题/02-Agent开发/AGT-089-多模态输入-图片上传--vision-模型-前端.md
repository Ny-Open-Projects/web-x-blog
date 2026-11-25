---
title: [AGT-089] 多模态输入（图片上传 → vision 模型）前端怎么处理？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-089：多模态输入（图片上传 → vision 模型）前端怎么处理？
**答**：
- OpenAI 兼容接口用 content parts：数组形式混合 `{type:'text'}` 与 `{type:'image_url'}`；URL 或 base64 data URL 均可。
- 前端处理：Canvas 压缩（长边 ≤ 1568px、JPEG 0.85）后再传，大图 base64 会撑爆请求体，生产优先对象存储 URL。
- `detail: low/high` 控制视觉 token 消耗：缩略图/列表场景用 low 省钱，精读场景才用 high。
- 安全：图片是用户内容——图内文字可能携带注入指令，按 AGT-050 的「内容即数据」原则处理。

```typescript
import { z } from 'zod';

// 图片上传 → 压缩 → vision 模型
async function fileToDataURL(file: File, maxEdge = 1568): Promise<string> {
  const bitmap = await createImageBitmap(file);
  const scale = Math.min(1, maxEdge / Math.max(bitmap.width, bitmap.height));
  const canvas = new OffscreenCanvas(bitmap.width * scale, bitmap.height * scale);
  canvas.getContext('2d')!.drawImage(bitmap, 0, 0);
  const blob = await canvas.convertToBlob({ type: 'image/jpeg', quality: 0.85 });
  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result as string); // data:image/jpeg;base64,...
    reader.readAsDataURL(blob);
  });
}

export async function describeImage(file: File, question: string) {
  const dataUrl = await fileToDataURL(file);
  return chatOnce([{
    role: 'user',
    content: [ // 多模态 content：数组形式混合文本与图片
      { type: 'text', text: question },
      { type: 'image_url', image_url: { url: dataUrl, detail: 'low' } },
    ],
  }] as any) as Promise<string>;
}
```
