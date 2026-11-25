---
title: [AGT-525] 一条回答里混排文本/表格/图表/公式/代码，渲染管线怎么组织（块解析→分发→增强）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-525：一条回答里混排文本/表格/图表/公式/代码，渲染管线怎么组织（块解析→分发→增强）

**答**：
- 三段管线：① 块解析（markdown 分块 + 块类型识别，流式下允许"未闭合块"挂起）；② 类型分发（text 走 markdown、mermaid 走图表引擎、表格走虚拟表格组件、代码走高亮+运行按钮）；③ 增强（完成后二次增强：代码加复制/运行、表格加排序导出、图表加交互）。
- 增强必须幂等且可撤销：流式先渲染基础形态，完整后再升级，避免重排闪跳。
- 每种块注册失败兜底：mermaid 语法错误降级为源码展示，不能整条回答白屏。

```javascript
const blockRenderers = {
  text: (b) => <Markdown src={b.raw} />,
  code: (b) => <CodeBlock {...b} onRun={() => runInSandbox(b)} />,
  mermaid: (b) => <Diagram src={b.raw} fallback={sourceView} />,
  table: (b) => <VirtualTable cols={b.cols} rows={b.rows} />,
};
function AnswerBlocks(stream) {
  const blocks = useBlockParser(stream);   // 流式块解析，末块可挂起
  return blocks.map(b => {
    const R = blockRenderers[b.type] ?? blockRenderers.text;  // 未知兜底
    return <R key={b.id} block={b} enhanced={b.complete} />;
  });
}
```

