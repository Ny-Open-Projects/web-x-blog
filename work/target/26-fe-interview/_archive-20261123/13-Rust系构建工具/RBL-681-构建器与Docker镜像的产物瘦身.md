---
title: [RBL-681] 构建器与容器化部署：产物镜像瘦身与多阶段构建的配合
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-681：构建器与容器化部署：产物镜像瘦身与多阶段构建的配合

**答**:
- 前端产物进容器的典型错误：把 node_modules 全量拷进镜像（构建依赖 1GB+，运行时只需要产物几 MB）——多阶段构建（builder 阶段装依赖构建 → runtime 阶段只 COPY dist）是标准答案，镜像从 1.5GB 降到 50MB。
- 构建器的配套输出：1) **产物清单**（manifest：dist 内全部文件列表）让 COPY 精确（`COPY --from=builder /app/dist ./dist`）；2) 依赖「运行时全量分析」（SSR bundle 的 external 依赖需要 node_modules 的生产子集——`--production` 安装或 pnpm deploy 生成最小 runtime 依赖集）；3) 静态资产与运行时代码分离（静态资产可直接走 CDN，镜像只留运行时——缓存分层优化）。
- 缓存友好的层序：Docker 层缓存与构建增量对齐——package.json/lockfile 先 COPY 再 install（依赖不变时命中层缓存）；源码 COPY 放最后——构建器无法控制 Dockerfile 但能输出「最佳层序建议」到迁移文档。
- 追问钩子：为什么 SSR 场景「镜像里只放 dist」不够？——external 依赖（RBL-604）在运行时按 node_modules 解析，镜像必须带生产依赖子集；这要求构建器精确输出 external 清单供 pnpm deploy/lockfile 裁剪，少了清单就会「容器里运行时找不到模块」。

```dockerfile
# 多阶段构建（构建器输出建议模板）
FROM node:20 AS builder
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack pnpm install --frozen-lockfile        # 依赖层先缓存
COPY . .
RUN corepack pnpm build                            # 构建器输出 dist + manifest

FROM node:20-slim
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/pruned/node_modules ./node_modules   # external 依赖子集
ENV NODE_ENV=production
CMD ["node", "dist/server.js"]
# 静态资产建议走 CDN：构建器在 manifest 里标注 static 角色，部署层分流
```

```javascript
// pnpm deploy 生成最小 runtime 依赖集（external 清单驱动）
// 构建器输出 external 清单
const externals = await build({ externalList: true });  // ['express', 'pg']
fs.writeFileSync('deploy-deps.json', JSON.stringify(externals));
// CI: pnpm deploy --filter=server --prod pruned/
// 校验：pruned/node_modules 覆盖全部 externals，缺失即 fail
for (const dep of externals)
  if (!fs.existsSync(`pruned/node_modules/${dep}`))
    fail(`镜像缺少运行时依赖: ${dep}`);
```
