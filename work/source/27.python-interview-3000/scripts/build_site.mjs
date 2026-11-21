#!/usr/bin/env node
/**
 * 构建静态网页版:docs/*.md + README.md -> site/
 *  - 每章一个 HTML,README 为 index.html
 *  - 侧边栏:全部章节 + 题目锚点;顶部搜索框按题号/标题过滤
 *  - mermaid 图用本地 vendor 的 mermaid.min.js 渲染(离线可用)
 * 用法: node scripts/build_site.mjs   (需先 npm i)
 */
import { readFileSync, writeFileSync, mkdirSync, copyFileSync, readdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import { marked } from "marked";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const DOCS = join(ROOT, "docs");
const SITE = join(ROOT, "site");
function walk(dir) {
  let out = [];
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const full = join(dir, e.name);
    if (e.isDirectory()) out = out.concat(walk(full));
    else if (e.name.endsWith(".md") && !/\s\d+\.md$/.test(e.name)) out.push(full); // 排除 macOS 副本
  }
  return out;
}
const chapters = walk(DOCS).sort();
// 题数由源文档实时统计,禁止硬编码 badge
const TOTAL_Q = chapters.reduce((n, f) => n + (readFileSync(f, "utf8").match(/^### Q\d+ · /gm) || []).length, 0);

marked.setOptions({ gfm: true, breaks: false });

/** 把代码块包上语言 class,并给 # file: 行加徽标 */
const renderer = {
  code(code, infostring) {
    const lang = (infostring || "").split(/\s+/)[0];
    if (lang === "mermaid") {
      return `<div class="mermaid">${code}</div>`;
    }
    const m = code.match(/^# file: (code\/\S+)$/m);
    const fileBadge = m ? `<div class="codefile">${m[1]}</div>` : "";
    const cls = lang ? ` class="language-${lang}"` : "";
    return `${fileBadge}<pre><code${cls}>${escapeHtml(code)}</code></pre>`;
  },
};
marked.use({ renderer });

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

/** 从 md 提取题目列表 [{id,title}] */
function questionsOf(md) {
  return [...md.matchAll(/^### (Q\d+) · (.+)$/gm)].map((m) => ({ id: m[1], title: m[2] }));
}

const CSS = readFileSync(join(ROOT, "scripts", "site.css"), "utf8");
let mermaidReady = false;
try {
  copyFileSync(join(ROOT, "node_modules/mermaid/dist/mermaid.min.js"), join(SITE, "assets/mermaid.min.js"));
  mermaidReady = true;
} catch { /* 没装依赖时跳过 mermaid */ }
mkdirSync(join(SITE, "assets"), { recursive: true });
writeFileSync(join(SITE, "style.css"), CSS);

const navItems = [];
const qIndex = []; // 搜索索引
const pages = [];

for (const filePath of chapters) {
  const file = filePath.replace(DOCS + "/", "");
  const md = readFileSync(filePath, "utf8");
  const title = (md.match(/^# (.+)$/m) || [])[1] || file;
  const qs = questionsOf(md);
  const outName = file.replace(/\.md$/, ".html");
  const chapterId = outName.replace(".html", "");
  const category = file.includes("/") ? file.split("/")[0] : "";
  navItems.push({ outName, title, qs, chapterId, category });
  for (const q of qs) qIndex.push({ chapterId, outName, ...q });

  const body = marked.parse(md);
  const sidebar = renderSidebar(outName);
  pages.push({ outName, title, html: pageShell(title, sidebar, body, qListNav(qs)) });
}

// index: README
const readmeMd = readFileSync(join(ROOT, "README.md"), "utf8");
const readMeQs = questionsOf(readmeMd);
{
  const sidebar = renderSidebar("index.html");
  pages.unshift({
    outName: "index.html",
    title: "Python 面试知识库",
    html: pageShell("Python 面试知识库", sidebar, marked.parse(readmeMd), qListNav(readMeQs)),
  });
}
navItems.unshift({ outName: "index.html", title: "总览", qs: readMeQs, chapterId: "index" });

// 搜索索引 JSON
writeFileSync(join(SITE, "search.json"), JSON.stringify(qIndex));

function qListNav(qs) {
  if (!qs.length) return "";
  const lis = qs.map((q) => `<li><a href="#${q.id}">${q.id}</a></li>`).join("");
  return `<details class="qlist"><summary>本题 ${qs.length} 题(题号直达)</summary><ul>${lis}</ul></details>`;
}

function renderSidebar(active) {
  const cats = [];
  for (const it of navItems) {
    const c = it.category || "";
    let cat = cats.find((x) => x.name === c);
    if (!cat) { cat = { name: c, items: [] }; cats.push(cat); }
    cat.items.push(it);
  }
  const lis = cats
    .map((cat) => {
      const files = cat.items
        .map((it) => {
          const cls = it.outName === active ? ' class="active"' : "";
          return `<li${cls}><a href="${it.outName}">${it.title}</a>` +
            (it.qs.length
              ? `<details><summary>${it.qs.length} 题</summary><ul>` +
                it.qs.map((q) => `<li><a href="${it.outName}#${q.id}">${q.id}</a></li>`).join("") +
                `</ul></details>`
              : "") +
            `</li>`;
        })
        .join("");
      return `<li class="cat"><span>${cat.name || "其他"}</span><ul>${files}</ul></li>`;
    })
    .join("\n");
  return `<nav class="sidebar"><div class="brand"><a href="index.html">Python 面试知识库</a><span class="badge">${TOTAL_Q} 题</span></div><input id="search" placeholder="搜索题号或标题…" autocomplete="off"/><ul id="navlist">${lis}</ul></nav>`;
}

function pageShell(title, sidebar, body, qlist) {
  const mermaidScript = mermaidReady
    ? `<script src="assets/mermaid.min.js"></script><script>window.addEventListener('DOMContentLoaded',()=>{mermaid.initialize({startOnLoad:true,theme:'neutral'});});</script>`
    : "";
  const searchScript = `<script>
document.getElementById('search').addEventListener('input', function () {
  var kw = this.value.trim().toLowerCase();
  fetch('search.json').then(function (r) { return r.json(); }).then(function (idx) {
    if (!kw) { location.reload(); return; }
    var hits = idx.filter(function (q) {
      return q.id.toLowerCase().indexOf(kw) >= 0 || q.title.toLowerCase().indexOf(kw) >= 0;
    }).slice(0, 50);
    var html = '<ul>' + hits.map(function (q) {
      return '<li><a href="' + q.outName + '#' + q.id + '">' + q.id + ' · ' + q.title + '</a></li>';
    }).join('') + '</ul>';
    document.getElementById('navlist').innerHTML = html;
  });
});
</script>`;
  return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>${title} · Python 面试知识库</title>
<style>${CSS}</style>
</head>
<body>
${sidebar}
<main class="content">
${qlist}
${body}
</main>
${mermaidScript}
${searchScript}
</body>
</html>`;
}

for (const p of pages) {
  mkdirSync(dirname(join(SITE, p.outName)), { recursive: true });
  writeFileSync(join(SITE, p.outName), p.html);
  console.log("built", p.outName, `(${(p.html.length / 1024).toFixed(0)} KB)`);
}
console.log(`\nsite/ 完成:${pages.length} 个页面,${qIndex.length} 个题目索引,mermaid ${mermaidReady ? "已内置" : "未内置"}`);
