---
title: [WEB-464] 大文件上传失败的排查 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-464：大文件上传失败的排查 SOP

**答**：
- 先定位失败层：请求根本没发（前端限制/size 校验）→ 网关 413（body 大小限制）→ 中途断（网络/超时）→ 服务端合并失败（分片序号/校验）
- 分层配置链核对：nginx client_max_body_size → 网关 SLB 限值 → 服务端 multipart 上限，任何一层都会 413，症状相似要逐层看错误来源
- 弱网问题：移动端上传大文件必须分片（5~10MB/片）+ 并发限流 + 失败重试 + 断点续传（已传分片列表持久化）
- MD5 校验的成本：全文件 hash 在主线程会卡死，用 Worker + 分片增量计算；只校验分片可接受时别算全量
- 观测：按片上报耗时与重试次数，区分「用户网络差」与「服务端真故障」

```javascript
async function uploadChunks(file, size = 5 * 1024 * 1024) {
  const chunks = Math.ceil(file.size / size);
  for (let i = 0; i < chunks; i += 3) { // 并发 3
    await Promise.all(
      Array.from({ length: 3 }, (_, k) => i + k).filter(i => i < chunks && !doneSet.has(i))
        .map(idx => retry(() => sendChunk(file.slice(idx * size, (idx + 1) * size), idx), 3))
    );
  }
}
```
