---
title: [MFW-740] 笔试：手写 Nuxt 文件路由解析器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-740：笔试：手写 Nuxt 文件路由解析

**答**：实现 `parseServerRoutes(files)`。files: 文件路径数组（如 `server/api/user.get.ts`、`server/api/products/[id].delete.ts`、`server/routes/sitemap.xml.get.ts`）。规则：1) 解析文件名 → `{ path, method, handler }`：`user.get.ts` → GET /api/user；`[id].delete.ts` → DELETE /api/products/:id（动态段 `[id]` → `:id`）；2) **方法提取**：文件名的最后一个 `.方法` 段（get/post/put/delete/patch）；3) 无方法后缀（`middleware.ts`）→ 中间件（非路由）；4) 路径前缀：server/api → /api；server/routes → /（无前缀）；5) 返回 `{ routes: Array<{ path, method, file }>, middlewares: string[] }`。边界：空 files；无方法后缀的非 middleware 文件（警告）；多级动态段。

```javascript
const HTTP_METHODS = ['get', 'post', 'put', 'delete', 'patch', 'head', 'options'];

function parseServerRoutes(files = []) {
  const routes = [], middlewares = [];
  for (const file of files) {
    const parts = file.split('/');
    // 方法后缀提取
    const baseName = parts.at(-1).replace(/\.ts$/, '');
    const lastDot = baseName.lastIndexOf('.');
    const method = lastDot !== -1 ? baseName.slice(lastDot + 1).toLowerCase() : null;
    const routeName = lastDot !== -1 ? baseName.slice(0, lastDot) : baseName;

    if (routeName === 'middleware' || parts.includes('middleware')) {
      middlewares.push(file); continue;
    }
    if (!method || !HTTP_METHODS.includes(method)) {
      console.warn(`无有效方法后缀: ${file}`);
      continue;
    }
    // 路径前缀
    const isApi = file.includes('server/api/');
    const isRoutes = file.includes('server/routes/');
    let path;
    if (isApi) path = '/api/' + routeName;
    else if (isRoutes) path = '/' + routeName;
    else continue;
    // 动态段
    path = path.replace(/\[(\w+)\]/g, ':$1');
    routes.push({ path, method: method.toUpperCase(), file });
  }
  return { routes, middlewares };
}

// 自测
const files = [
  'server/api/user.get.ts',
  'server/api/user.post.ts',
  'server/api/products/[id].delete.ts',
  'server/api/products/[id]/reviews.get.ts',
  'server/routes/sitemap.xml.get.ts',
  'server/middleware/auth.ts',
];
let r = parseServerRoutes(files);
console.log(r.routes.length === 5);
console.log(r.middlewares.length === 1);

const userGet = r.routes.find(x => x.path === '/api/user');
console.log(userGet.method === 'GET');

const prodDelete = r.routes.find(x => x.method === 'DELETE');
console.log(prodDelete.path === '/api/products/:id');

const reviews = r.routes.find(x => x.path === '/api/products/:id/reviews');
console.log(reviews.method === 'GET');

const sitemap = r.routes.find(x => x.path === '/sitemap.xml');
console.log(sitemap.method === 'GET');                   // server/routes 无 /api 前缀

// 无方法后缀
r = parseServerRoutes(['server/api/helper.ts']);
console.log(r.routes.length === 0);                      // 警告但不崩

// 空
console.log(parseServerRoutes([]).routes.length === 0);
```

**评分点**：
- 文件名解析正确（方法后缀提取 + 动态段 → :id 转换）；双前缀（/api 与 / 无前缀）
- middleware 识别（middleware.ts → 中间件清单）；无效后缀警告不崩
- 边界（空 files/无方法/多级动态段）；对比 Next 的 route.ts 多导出
- 能说清「文件名 = HTTP 方法的显式性：user.get.ts 看名即知方法——与 Next 的导出式各有取舍」属于加分
