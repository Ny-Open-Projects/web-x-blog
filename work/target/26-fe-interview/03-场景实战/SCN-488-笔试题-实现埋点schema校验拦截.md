---
title: [SCN-488] 笔试题——实现埋点 schema 校验（未注册拦截/公共属性补全/漏埋检测）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-488：手写埋点校验：事件字典校验、公共属性自动补全、漏埋自动检测

**需求与边界**：
- 输入：埋点事件、事件字典；输出：上报决策与质量报告。
- 边界要求：① 未注册事件拦截（字典外事件不上报+计数告警）；② 公共属性自动补全（用户/设备/页面上下文——业务方少传）；③ 漏埋检测（关键路径跑批比对期望事件集）；④ 字段类型校验（数值型传字符串拦截）。

**答**：
```javascript
class TrackingValidator {
  constructor(dict, { commonProps }) {
    this.dict = dict;                          // 事件字典（注册制）
    this.commonProps = commonProps;            // 公共属性工厂
  }
  track(event) {
    const def = this.dict[event.name];
    if (!def) {                                // 未注册拦截
      warnCounter.inc(event.name);
      if (warnCounter.get(event.name) > 100)
        alert('未注册事件堆积', { top: event.name });
      return false;                            // 不上报
    }
    const check = def.schema.safeParse(event.props);
    if (!check.success) {                      // 字段类型校验
      warnCounter.inc(`${event.name}:bad_schema`);
      return false;
    }
    return { ...this.commonProps(), ...check.data };  // 公共属性补全
  }
  async coverageCheck(journey) {               // 漏埋检测
    await smokeRun(journey);                   // 冒烟跑关键路径
    const captured = capturedEvents(journey);
    const missing = journey.expectedEvents
      .filter(e => !captured.includes(e));
    return { missing, ok: missing.length === 0 };   // 漏埋清单
  }
}
// 字典门户：事件/属性/示例/负责人可查；
// CI：字典变更评审（SCN-399 治理复用）。
```

**评分点**:
- 未注册拦截+堆积告警（字典注册制的执行）。
- 公共属性工厂自动补全（业务方少传）。
- 漏埋检测：冒烟跑关键路径比对期望事件集。
- 字段 schema 校验（类型错误拦截）。
