---
title: [SCN-081] 本地开发与联调阶段，如何优雅切换 mock 与真实接口，并支持抓包调试？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-081：本地开发与联调阶段，如何优雅切换 mock 与真实接口，并支持抓包调试？
**答**：
- 两层开关：环境变量决定默认走 mock 还是代理；请求层维护"单接口 mock 集合"，只 mock 正在开发的接口，其余照常联调。
- mock 与 TypeScript 类型同源（同一 schema 生成），防止 mock 与真实结构漂移；mock 加 300ms 延迟，暴露 loading 态问题。
- 抓包：devServer proxy 转发联调环境（changeOrigin + secure:false 处理自签证书），需要改包时把 target 指向本机 whistle/Charles 端口。

```javascript
// vite.config.js：代理配置 + 抓包切换
export default defineConfig(({ mode }) => ({
  server: {
    proxy: {
      '/api': {
        target: 'https://test-env.example.com',
        changeOrigin: true,      // 修改 Host 头，绕过对方域名校验
        secure: false,           // 联调环境自签证书不校验
        // 抓包调试：把 target 换成 'http://127.0.0.1:8899'（Charles/whistle 端口）
        configure: (proxy) => {
          proxy.on('proxyReq', (req) => {
            req.setHeader('X-Debug-User', 'wang');   // 联调环境区分流量来源
          });
        },
      },
    },
  },
}));
```

```typescript
// 请求层 mock 开关：全局 + 单接口覆盖，类型同源防漂移
import type { OrderDetail } from './types';
import mockOrder from './mocks/order.mock';

const MOCK_OVERRIDES = new Set(['/api/order/detail']);   // 只 mock 正在开发的接口
const MOCK_ALL = import.meta.env.VITE_USE_MOCK === 'true';

export async function get<T>(url: string): Promise<T> {
  if (MOCK_ALL || MOCK_OVERRIDES.has(url)) {
    console.warn('[mock]', url);
    await new Promise((r) => setTimeout(r, 300));   // 模拟延迟，暴露 loading 逻辑问题
    return mockOrder as T;                          // mock 与 OrderDetail 类型同源
  }
  return http.get<T>(url).then((r) => r.data);
}
```
