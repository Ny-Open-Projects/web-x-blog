---
title: [NODE-305] 流式深水区：零拷贝 sendfile 与性能边界？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-305：流式深水区：零拷贝 sendfile 与性能边界？
**答**:
- sendfile 系统调用：文件→socket 直接内核态拷贝，绕过用户态——大文件静态服务吞吐关键；Node 内部在 http 静态响应路径自动使用（fs.createReadStream 满足条件时）。
- 边界：需要 transform（gzip/加密）时无法 sendfile（要过用户态）；Range 请求部分支持。
- 应用侧做法：静态大文件直接 Node 响应流（让框架判定 sendfile）；需要加密/水印的场景接受用户态拷贝成本。
- 对比 nginx：专业静态服务做 sendfile+open_file_cache 更成熟——动态服务里的静态文件用 Node 流，大规模静态资产交给 CDN/Nginx。

```javascript
// Node 内部判定（心智模型）
// res 上直接 pipe 文件流 + 未压缩 → libuv 用 uv_fs_sendfile（零拷贝）
app.get('/video/:id', async (req, res) => {
  const f = await repo.getVideo(req.params.id);
  res.writeHead(200, { 'Content-Length': f.size, 'Content-Type': 'video/mp4' });
  createReadStream(f.path).pipe(res);      // 大文件：sendfile 路径（可观测：strace 看 sendfile 调用）
});
// 静态资产策略：小而多 → Node/框架静态中间件；大而热 → CDN（边缘 sendfile）
```
