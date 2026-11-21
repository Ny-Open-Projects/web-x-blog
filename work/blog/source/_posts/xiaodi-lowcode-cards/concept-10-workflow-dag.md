---
title: 工作流引擎：节点契约与 DAG 编排
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 概念, 工作流, DAG]
---

## 工作流引擎：节点契约与 DAG 编排

页面 Schema 与工作流图 DSL 并列为低代码平台的两大契约。工作流侧的契约是**节点契约 `NodeContract {type, category, label, version, inputs, outputs}（契约与执行器分离，execute 在 NODE_REGISTRY）` + 图 DSL（nodes/edges 带端口）**，端口类型（data/schema/trigger）校验在连线时完成。

**本项目实例**（自研参考实现）：
- 7 类节点：`trigger.formSubmit`、`transform.map`（setField/pick/pickTo/concat）、`ui.composePage`（支持 `{{data.x}}` 模板注入生成 PageSchema）、`action.sendSms`、`action.ossUpload`、`script.eval`、`ai.llm`。
- 执行引擎 `engine/dag.ts`：Kahn 拓扑排序（按拓扑序**串行**执行，无并行调度）（检测环抛错）→ 按序执行 → 沿边注入下游输入端口 → 节点级 trace。纯函数无 HTTP 依赖，可单测。
- 副作用可替换：SmsProvider/OssProvider/FormStore 走 Provider 接口，默认 console/local/memory 实现，表单存储落库 wf_submission。
- 审计与追踪：wf_run/wf_run_node 记录节点级 inputMd/outputMd/durationMs。

注意出处区分：工作流/沙箱/AI 节点是自研参考实现，不是课程原始代码（课程版 B 无此模块），写作引用时要说清。

出处「scan3 §2-A」
