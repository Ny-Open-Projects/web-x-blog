---
title: [TST-082] 图表/地图等第三方渲染库在组件测试里怎么处理？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-082：图表/地图等第三方渲染库在组件测试里怎么处理？
**答**：
- 原则：不测库本身（echarts/antd 不归你测），测「你的接线」——传了什么数据、何时初始化/销毁、事件绑定是否正确。
- 三种处理：① vi.mock 整库，导出假渲染组件 + 断言 props（最常用）；② mock 容器 ref（jsdom 无 canvas，echarts init 会挂——mock echarts.init 返回带 setOption/dispose 的 stub）；③ 组件封装时留一层「可注入渲染器」props，测试注入假渲染器（DI 思路）。
- 断言面：mock 产物收到正确的 option（数据映射）、resize 监听注册、卸载时 dispose 被调用（内存泄漏防线）。
- 追问钩子：canvas/webgl 相关库在 jsdom 下大量 API 缺失，与其 polyfill 不如 mock——测试的目标是接线不是像素。

```jsx
// mock echarts：只验证接线
import { describe, it, expect, vi, afterEach } from 'vitest';

const setOption = vi.fn(), dispose = vi.fn();
vi.mock('echarts', () => ({
  default: { init: vi.fn(() => ({ setOption, dispose, resize: vi.fn() })) },
}));

import ChartPanel from './ChartPanel';

afterEach(() => { setOption.mockClear(); dispose.mockClear(); });

describe('ChartPanel', () => {
  it('把销量数据映射进 option 并在卸载时 dispose', () => {
    const { unmount } = render(<ChartPanel data={[{ day: '01', sales: 10 }]} />);
    expect(setOption).toHaveBeenCalledWith(expect.objectContaining({
      series: [expect.objectContaining({ data: [10] })],   // 数据映射正确
    }));
    unmount();
    expect(dispose).toHaveBeenCalledTimes(1);              // 泄漏防线
  });
});
```
