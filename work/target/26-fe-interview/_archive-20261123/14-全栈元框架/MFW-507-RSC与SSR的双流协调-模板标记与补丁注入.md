---
title: [MFW-507] RSC 与 SSR 的双流协调：模板标记、占位与补丁注入
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-507：RSC 与 SSR 双流协调：模板标记与补丁注入

**答**:
- 双流协议：SSR HTML 流用 `<!--$?--><template id="B:0"></template>` 标记「待完成的 Suspense 边界」——Flight payload 到达对应 chunk 时，客户端（或流内 inline script `$RC`) 把内容注入模板位置——「HTML 先占位、数据后填充」的协议。
- 注入的两条路径：1) **流内 script**（Flight chunk 跟在 HTML 后，内联 `$RC(...)` 函数立即执行——JS 禁用时依赖表单/降级）；2) **客户端水合时**（水合器读取 payload 补齐——JS 启用后统一由 React 接管）。
- 协调的关键不变量：HTML 的占位 id 与 Flight 的 chunk id **一一对应**（id 空间共享）——错配 = 内容注入到错误位置（静默 UI 错乱）；这是构建器一致性测试的目标（RBL-700 双产物对齐的 SSR 流版）。
- 流结束标记：`<!--/$-->` 闭合边界——嵌套边界的配对由 id 保证。
- 追问钩子：为什么占位用 `template` 元素而不是直接留空？——template 是 inert 的（内容不渲染不执行）——流式注入前页面布局稳定（占位高度可由 CSS 骨架控制）；且 template 作为「注入锚点」可被 `$RC` 精确替换——DOM 协议细节服务于「流式填充的原子性」：占位 → 到达 → 替换，中间无中间态闪烁。

```javascript
// 流内注入函数 $RC（React 内部实现的概念还原）
function $RC(boundaryId, contentId) {
  const tpl = document.getElementById('B:' + boundaryId);   // HTML 占位
  const frag = document.getElementById(contentId);          // Flight 附带的隐藏内容容器
  if (tpl && frag) {
    tpl.parentNode.replaceChild(frag.content ?? frag, tpl); // 原子替换
    // 同步 Flight 数据引用：让水合器知道该边界已完成
    window.__flightResolved?.(boundaryId);
  }
}
// 服务端输出形态
// <div><!--$?--><template id="B:0"></template><div class="skeleton">加载中</div><!--/$--></div>
// <div hidden id="S:0">异步内容 HTML</div>
// <script>$RC("0","S:0")</script>                         // 到达即注入
```
