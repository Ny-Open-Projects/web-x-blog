---
title: [TST-143] 笔试：为 WebSocket 消息流（IM 场景）写测试
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-143：笔试：为 WebSocket 消息流（IM 场景）写测试
**答**：
- 场景：IM 页面连接 WebSocket，收消息追加到列表、发消息推送给服务器、断线自动重连。测试用 `mock-socket`（或手写 WebSocket stub）——可控地触发 open/message/close 事件并捕获 send。
- 断言层次：① 收到消息渲染（含 JSON 解析与排序）；② send 的 payload 结构正确；③ 断线重连（close 后重新 new WebSocket）；④ 重连指数退避（fake timers）。
- 手写 stub 要实现的关键面：addEventListener/onmessage 双风格、readyState 状态机、close() 触发组件清理。

```jsx
import WS from 'jest-websocket-mock'; // 或 mock-socket；此处展示通用思路
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Chat from './Chat';

test('收消息渲染 + 发消息 payload 正确', async () => {
  const wsServer = new WS('wss://im.example.com/socket');
  render(<Chat userId="u1" />);

  await wsServer.connected;                              // 等真实连接握手

  // 服务端推消息 → 渲染
  wsServer.send(JSON.stringify({ type: 'msg', from: 'u2', text: '在吗', ts: 1000 }));
  expect(await screen.findByText('在吗')).toBeInTheDocument();

  // 客户端发送 → 校验 payload
  const user = userEvent.setup();
  await user.type(screen.getByRole('textbox'), '在的');
  await user.keyboard('{Enter}');
  await expect(wsServer).toReceiveMessage(
    JSON.stringify({ type: 'msg', from: 'u1', text: '在的', ts: expect.any(Number) }),
  );

  wsServer.close();
});

test('断线后自动重连', async () => {
  const wsServer = new WS('wss://im.example.com/socket');
  render(<Chat userId="u1" />);
  await wsServer.connected;

  wsServer.close({ code: 1006, wasClean: false });       // 异常断线
  expect(await wsServer.nextMessage).toBeDefined?.();    // —
  await wsServer.connected;                              // 第二次 connected = 重连成功
  expect(screen.getByText('连接已恢复')).toBeInTheDocument();
  wsServer.close();
});
```

**评分点**：
1. 等 `connected` 握手后再操作（直接 send 必竞态）。
2. 双向断言：收消息渲染 + 发送 payload 结构校验。
3. 断线重连场景覆盖（code 1006 异常断线）。
4. 测试结束 close 清理，防止 mock server 泄漏影响下一用例。
