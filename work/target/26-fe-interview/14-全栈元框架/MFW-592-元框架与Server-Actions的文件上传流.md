---
title: [MFW-592] Server Actions 的文件上传：流式与大文件策略
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-592：Server Actions 的文件上传流

**答**:
- Action 上传文件的两形态：1) **formData 直接传**（file 字段 → action 收 File 对象——serverless 的 body 大小限制（Vercel 4.5MB——大文件不行）；2) **预签名直传**（action 只签发预签名 URL（S3 presigned）→ client 直传 S3 → 回调确认——「文件不过 server」绕开限制（大文件标准方案 RBL-840 分片的 S3 版））。
- 流式处理：小文件（formData 里 file.stream() 流式写——避免 buffer 全量内存）；「内存峰值」：File.arrayBuffer() = 全量内存（10MB 文件 = 10MB 内存峰值 × 并发）——流式是 serverless 内存预算的关键。
- 直传的完整性：client 直传 S3 的校验（预签名 URL 带 content-type/大小限制 + 上传后 server 校验 ETag/大小——「直传的信任边界」：S3 事件回调验证 RBL-592）。
- 追问钩子：为什么「大文件直传 S3」比「流过 server」更值得？——流过 server：上传时长占 serverless 函数时长（100MB × 慢网络 = 超时）+ 内存/带宽成本（server 侧双倍带宽：进+出）；直传：client → S3 一次（server 只签 URL 一次）——「server 的角色 = 授权者而非中转」——serverless 成本模型（RBL-855）下的必然选择：server 只做控制面、数据面走旁路。

```typescript
// Action：预签名直传（大文件标准方案）
'use server';
export async function getUploadUrl(fileName: string, size: number) {
  await requireAuth();                                   // 上传也要鉴权
  if (size > 100 * 1024 * 1024) throw new Error('too large');
  const key = `uploads/${crypto.randomUUID()}/${fileName}`;
  const url = await s3.presign(key, { expiresIn: 3600,
    conditions: [['content-length-range', 1, size]] });  // 预签名含大小限制
  return { url, key };
}
// 确认（S3 回调或 client 调）
'use server';
export async function confirmUpload(key: string, etag: string) {
  const meta = await s3.head(key);
  if (meta.etag !== etag) throw new Error('integrity');  // 完整性校验
  await db.files.create({ key, size: meta.size });
  revalidateTag('files');
}
// client
async function upload(file: File) {
  const { url, key } = await getUploadUrl(file.name, file.size);
  await fetch(url, { method: 'PUT', body: file });       // 直传 S3（不过 server）
  await confirmUpload(key, etagFromResponse);
}
```
