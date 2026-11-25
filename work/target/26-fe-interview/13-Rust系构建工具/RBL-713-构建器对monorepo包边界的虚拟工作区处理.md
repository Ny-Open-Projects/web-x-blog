---
title: [RBL-713] 构建器的虚拟工作区：root 目录假设与多包同进程构建
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-713：构建器的虚拟工作区：root 目录假设与多包同进程构建

**答**:
- 构建器普遍假设「单 root」（一个 config 一个工作目录）——monorepo 多包同进程构建（一次跑 N 个包的构建任务）时，root 假设破裂：resolve 的 node_modules 上溯（从 /apps/web 找到 /node_modules）依赖目录结构、相对路径配置（./src）相对 root。解法是「虚拟工作区」：每个构建任务绑定显式 root（不用 cwd），文件系统操作全部相对 root 归一。
- 实现要点：1) root 注入一切路径 API（fs 适配层传入 base）；2) resolve 上下文按包隔离（每包独立的 tsconfig paths/aliases 作用域——包 A 的 alias 不影响包 B）；3) 产物输出路径校验（包 A 不许写包 B 的 dist——RBL-659 路径越界校验在包粒度）。
- 并发多包构建的共享面：跨包可共享的资源是「只读的」——node_modules 解析缓存、类型定义缓存；不可共享的是「包内状态」（模块图/插件实例）——共享边界搞错就是串包 bug（包 A 的模块出现在包 B 产物里）。
- 工程价值：多包同进程让 turbo 式编排器的「build 并发」成本下降（进程复用），也让「跨包增量」（ui 变 → web 增量）在同一会话里做（RBL-701 的失效传播）。
- 追问钩子：为什么 cwd 依赖是 monorepo 工具链的老 bug 源？——CI/本地/容器的工作目录不同，相对路径行为漂移；「显式 root + 相对归一」消灭一类「在我机器上能跑」问题——构建器 API 设计中 root 必须显式且不可变。

```javascript
// 虚拟工作区实现
function createWorkspace(root, { allowWrite = (p) => p.startsWith(root) } = {}) {
  return {
    root,
    resolve(p) { return path.isAbsolute(p) ? p : path.join(root, p); },  // 相对归一
    fs: {
      async read(p) { return fs.readFile(path.join(root, p)); },
      async write(p, data) {
        const full = path.join(root, p);
        if (!allowWrite(full)) throw new Error(`越界写入: ${p} 超出 ${root}`);   // 包隔离
        return fs.writeFile(full, data);
      },
    },
  };
}

// 多包同进程构建
async function buildAll(packages) {
  const shared = createSharedCache({ resolveCache: true });   // 只读共享
  return Promise.all(packages.map(pkg => {
    const ws = createWorkspace(pkg.dir);
    return builder.build({
      workspace: ws,
      resolveContext: { paths: pkg.tsconfigPaths, aliases: pkg.aliases },  // 包级作用域
      shared,                                                 // 只读共享，写隔离
    });
  }));
}
```
