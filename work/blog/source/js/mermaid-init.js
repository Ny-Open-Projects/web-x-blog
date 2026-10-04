// mermaid 代码块初始化。
//
// 需要兼容两种 HTML 结构（es 批和 k8s 批的代码块结构不一样）：
//   A. <pre><code class="language-mermaid">…</code></pre>            标准 markdown-it 输出
//   B. <figure class="highlight"><table><tr><td class="code">
//        <pre><span class="line">graph LR</span>…</pre>…            hexo 高亮器输出
// 结构 B 里语言 class 变成了 highlight.js 的 `plaintext`，只能靠内容特征判断是不是 mermaid。
(function () {
  // mermaid 的图类型声明，作为内容特征
  var DIAGRAM = /^\s*(graph\s+(LR|TD|TB|BT|RL)|flowchart\s+(LR|TD|TB|BT|RL)|sequenceDiagram|classDiagram|stateDiagram(?:-v2)?|erDiagram|gantt|pie|gitGraph|mindmap|timeline|quadrantChart|journey|C4Context|requirementDiagram|block-beta)\b/;

  function looksLikeMermaid(text) {
    return DIAGRAM.test(text);
  }

  function renderMermaid() {
    var host = document.querySelector('.post-body, #main, body');
    if (!host) return;
    if (!window.mermaid) return; // CDN 还没到，保留原样代码块

    var targets = [];
    var done = new Set();

    // A. 标准结构
    Array.prototype.forEach.call(host.querySelectorAll('pre > code.language-mermaid'), function (code) {
      var pre = code.parentElement;
      if (!done.has(pre)) { targets.push({ el: pre, text: code.textContent }); done.add(pre); }
    });

    // B. hexo 高亮器结构：先排除已被 mermaid 占用和明显不是 mermaid 的
    Array.prototype.forEach.call(
      host.querySelectorAll('figure.highlight pre, .highlight figure pre'),
      function (pre) {
        if (done.has(pre)) return;
        if (pre.closest('.mermaid')) return;
        var text = pre.textContent || '';
        if (!looksLikeMermaid(text)) return;
        targets.push({ el: pre, text: text });
        done.add(pre);
      }
    );

    if (!targets.length) return;

    window.mermaid.initialize({
      startOnLoad: false,
      theme: 'default',
      flowchart: { curve: 'basis', htmlLabels: true },
      gantt: { axisFormat: '%m-%d' }
    });

    targets.forEach(function (t) {
      // figure.highlight 的情况要连 figure 一起换掉，否则会留下空的表格边框
      var victim = t.el.closest('figure.highlight') || t.el;
      var block = document.createElement('div');
      block.className = 'mermaid';
      block.textContent = t.text;
      victim.parentNode.replaceChild(block, victim);
    });

    try {
      window.mermaid.run();
    } catch (e) {
      if (window.console) console.warn('[mermaid] render failed:', e);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderMermaid);
  } else {
    renderMermaid();
  }
  window.addEventListener('load', renderMermaid);
})();
