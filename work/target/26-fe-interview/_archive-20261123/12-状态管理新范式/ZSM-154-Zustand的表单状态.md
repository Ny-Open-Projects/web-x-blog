---
title: [ZSM-154] 表单状态该放 Zustand 还是 react-hook-form？「全局表单」怎么处理才不乱？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-154：表单状态该放 Zustand 还是 react-hook-form？「全局表单」怎么处理才不乱？
**答**：
- 默认答案：表单值是瞬时局部状态，用 react-hook-form/useRef 非受控管理，每键入一个字符都写进全局 store 是性能与生命周期的双输。
- 真正需要全局的只有「表单的元信息」：跨步骤向导的已完成步骤、多表单共享的字典选项、提交后的服务端结果——值本体留在表单库。
- 多步骤表单模式：步骤切换单独 store 存「快照」（onNext 时 form.getValues() 写入），返回上一步再 reset 成快照；提交成功后快照与草稿一起清。
- 拆表单信号：一个巨型表单里不同区块由不同人维护、校验规则冲突时，按业务块拆成多个 form + 一个「步骤/草稿」协调 store。

```javascript
// 步骤快照模式：值在表单库，快照进 store
const useWizardStore = create((set) => ({
  step: 0, snapshots: {}, goto: (step, snap) =>
    set(s => ({ step, snapshots: { ...s.snapshots, [s.step]: snap } })),
}))

function StepOne() {
  const form = useForm()
  const { goto, step } = useWizardStore()
  const onNext = form.handleSubmit((values) => {
    goto(step + 1, values)               // 只存快照，不逐键同步
  })
  // 返回上一步时：form.reset(useWizardStore.getState().snapshots[0])
  return <Form form={form} onSubmit={onNext}/>
}
```
