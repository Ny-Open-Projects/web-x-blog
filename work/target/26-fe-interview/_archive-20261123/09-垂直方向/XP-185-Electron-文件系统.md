---
title: [XP-185] Electron 文件系统：安全读写与路径校验
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-185：Electron 文件系统：安全读写与路径校验

**答**：
- 题目：Electron 文件操作安全——路径白名单（防目录穿越）、文件类型校验（魔数）、大文件流式处理。
- 思路：路径解析后必须落在白名单目录内（path.resolve + startsWith 校验）；魔数校验（HW-AV-305 复用）；大文件流（createReadStream 而非 readFileSync）。
- 评分点：目录穿越防御；魔数校验；流式处理。

```javascript
const ALLOWED_DIRS = [path.join(app.getPath('userData'), 'files')];
function assertSafePath(userPath) {                            // 目录穿越防御
  const resolved = path.resolve(userPath);                     // 解析真实路径
  const allowed = ALLOWED_DIRS.some(dir => resolved.startsWith(dir + path.sep));
  if (!allowed) throw new Error(`path-escape: ${userPath}`);     // 拒绝越界
  return resolved;
}
ipcMain.handle('fs:read', async (e, userPath) => {
  const safe = assertSafePath(userPath);                        // 校验后读
  const stat = await fs.promises.stat(safe);
  if (stat.size > 100 * 1024 * 1024)                            // >100MB 走流
    return createStreamResponse(safe);
  return fs.promises.readFile(safe);
});
```
