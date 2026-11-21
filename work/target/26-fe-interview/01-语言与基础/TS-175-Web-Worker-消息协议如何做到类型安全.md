---
title: [TS-175] Web Worker 消息协议如何做到类型安全？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-175：Web Worker 消息协议如何做到类型安全？
**答**：
- 协议文件定义请求/响应两条可辨识联合，收发端 import 同一份定义。
- 主线程按 id 关联请求响应；worker 端 switch 穷尽处理，漏分支用 never 检查拦截。
- 进阶方向：请求/响应配对成映射类型，callWorker 返回类型按消息类型精确化。

```typescript
// protocol.ts —— 收发端共享
type WorkerRequest =
  | { id: number; type: "sum"; nums: number[] }
  | { id: number; type: "sort"; nums: number[] };

type WorkerResponse =
  | { id: number; type: "sum"; result: number }
  | { id: number; type: "sort"; result: number[] }
  | { id: number; type: "error"; message: string };

// worker.ts —— 穷尽处理，漏分支编译报错
worker.onmessage = (e: MessageEvent<WorkerRequest>) => {
  const req = e.data;
  switch (req.type) {
    case "sum":
      self.postMessage({ id: req.id, type: "sum", result: req.nums.reduce((a, b) => a + b, 0) });
      break;
    case "sort":
      self.postMessage({ id: req.id, type: "sort", result: [...req.nums].sort() });
      break;
    default: {
      const _exhaustive: never = req; // 新增请求类型未处理时这里报错
    }
  }
};

// main.ts —— Promise 化调用
function callWorker(worker: Worker, req: WorkerRequest): Promise<WorkerResponse> {
  return new Promise((resolve) => {
    worker.onmessage = (e: MessageEvent<WorkerResponse>) => {
      if (e.data.id === req.id) resolve(e.data);
    };
    worker.postMessage(req);
  });
}
```

## 第三十六章 TS 元编程进阶（TS-176 ~ TS-181）
