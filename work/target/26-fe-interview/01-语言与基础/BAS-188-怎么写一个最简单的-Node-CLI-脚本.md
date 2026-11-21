---
title: [BAS-188] 怎么写一个最简单的 Node CLI 脚本？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-188：怎么写一个最简单的 Node CLI 脚本？
**答**：
- 文件首行 shebang `#!/usr/bin/env node`，声明用 node 执行；chmod +x 赋执行权后可直接 `./mytool.js` 运行。
- 命令行参数从 process.argv.slice(2) 取（前两项是 node 路径和脚本路径）。
- 工程化分发：package.json 的 bin 字段登记命令名，npm link 本地模拟全局安装。

```javascript
#!/usr/bin/env node
// mytool.js —— shebang 指定用 node 执行
const args = process.argv.slice(2);  // 前两项是 node 与脚本路径
console.log('收到参数:', args);
// 用法：chmod +x mytool.js && ./mytool.js hello world
// 发布：package.json 里配 "bin": { "mytool": "./mytool.js" }，npm link 后全局可用
```

## 二十一、工具与规范速答
