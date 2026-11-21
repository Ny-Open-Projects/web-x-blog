---
title: 问卷统计前后端：动态表头、ECharts 与数据重组
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, ECharts, 统计]
---

## 问卷统计前后端：动态表头、ECharts 与数据重组

**后端三接口**：①获取问卷组件（TypeORM `In` 操作符一次查出 input/textarea/radio/checkbox 四种类型）作表头；②获取问卷内容（先校验页面存在 → 查 component_data → `Promise.all` 聚合异步查表结果）；③按 ID 查组件数据（`filter` 筛目标组件 → value 统一为数组（输入型字符串用 [] 包裹）→ `flat` 降维）。

**前端动态表头**：组件表重组为 antd Table 的 `{title, dataIndex, key}`（key/dataIndex=组件 id，title 取 options.title 带兜底）；二维数组重组为 dataSource；checkbox 数组 join 逗号串。坑：组件 id 当 key 会触发 React key 冲突警告；组件 ID vs 选项 ID 要区分。

**ECharts 图表**：`echarts-for-react` 只吃 option；数据 reduce 成 `{name,value}` 统计选项出现次数。饼图 `series[0].type='pie'` + radius + legend；**横向柱状图关键在 Y 轴**——`yAxis.type='category'` 放分类名、xAxis 放数值 + max=100、`showBackground:true` 铺灰底做对比、`grid.containLabel:true` 防长名被裁。

图表只对 radio/checkbox 出图，输入型组件生成填写者名单文本。

出处「课程25 · 21-2~21-5、22-4、22-5」
