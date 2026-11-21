---
title: [NODE-364] Node 服务的文件与路径安全（穿越/软链/临时文件）如何防？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-364：文件与路径安全
**答**:
- 路径穿越：用户输入拼路径（../）读任意文件——防线：ID 映射（不直接用文件名，用 DB 记录 id → 存储路径）、path.resolve 后校验前缀（必须以 baseDir 开头）、文件名白名单字符集。
- 上传文件名：原始文件名只做展示元数据，存储名服务端生成（UUID/哈希）；解压 zip 检查条目路径（zip slip：压缩包内 ../ 条目写到包外）与解压炸弹（解压后总大小上限）。
- 临时文件：写系统临时目录 + 随机名（防碰撞竞争）、用完即删（finally 清理）、上传目录禁执行权限。
- 符号链接：下载/读取入口 resolve 后校验真实路径（fs.realpath）防软链逃逸。
- 权限与隔离：文件服务进程最小权限（只读写指定目录）、容器文件系统只读 + 显式挂载可写卷。
```javascript
function safePath(baseDir, userPath) {
  const full = path.resolve(baseDir, userPath);
  if (!full.startsWith(path.resolve(baseDir) + path.sep)) throw new Error('路径越界'); // 穿越防护
  return fs.realpathSync(full);                                  // 防软链逃逸
}
// zip 解压：entry.name 必须无 ../ 且 resolve 后在目标目录内；总解压大小上限
```
