# -*- coding: utf-8 -*-
"""全库检索手册构建器：11 域 interview-bank.md（5580 面试题）+ quiz-bank.md 的填空/简答（笔试主观题）
→ 单文件可搜索 HTML。
功能：关键词全文检索、域/题型过滤、背诵模式（点击展开答案）、分页浏览。
用法: python InterviewManualBuilder.py
"""
import re, os, json

DOMAINS = ['java-basics','concurrency','jvm','spring','mysql','redis','mongodb','mq','distributed','ai','algorithm','java-ai','agent-dev']
DOM_NAME = {'java-basics':'Java 基础','concurrency':'并发','jvm':'JVM','spring':'Spring','mysql':'MySQL',
            'redis':'Redis','mongodb':'MongoDB','mq':'MQ','distributed':'分布式','ai':'AI/Agent','algorithm':'算法','java-ai':'Java AI 框架','agent-dev':'Agent 开发'}
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, 'exams', 'interview-manual.html')

HEAD_RE = re.compile(r'^\*\*Q[\w\-]+（(概念考察|误用纠错|原理深挖|工程落地|版本演进|结论依据|边界追问|追问链)·(P[\d\-P]+)）\*\*')
QUIZ_RE = re.compile(r'^\*\*Q([\w\-]+)（(填空|简答)·([^）]+）)\*\* ?(.*)')

def parse_bank(path):
    """面试题（五题型+结论依据）"""
    qs = []
    text = open(path, encoding='utf-8').read()
    for b in re.split(r'\n(?=\*\*Q[\w\-]+（)', text):
        if not b.startswith('**Q'):
            continue
        first, *rest = b.strip().split('\n')
        m = HEAD_RE.match(first)
        if not m:
            continue
        qid = re.match(r'^\*\*(Q[\w\-]+)（', first).group(1)
        q = a = pts = ''
        for l in rest:
            if l.startswith('【面试官】'):
                q = l[len('【面试官】'):].strip()
            elif l.startswith('【标准回答话术】'):
                a = l[len('【标准回答话术】'):].strip()
            elif l.startswith('【评分点】'):
                pts = l[len('【评分点】'):].strip()
        if q and a:
            qs.append({'id': qid, 'kind': m.group(1), 'p': m.group(2), 'q': q, 'a': a, 'pts': pts})
    return qs

def parse_quiz_bank(path):
    """填空/简答（笔试主观题；单选/判断已在交互面板，不重复收录）"""
    qs = []
    text = open(path, encoding='utf-8').read()
    for b in re.split(r'\n(?=\*\*Q[\w\-]+（)', text):
        if not b.startswith('**Q'):
            continue
        lines = b.strip().split('\n')
        m = QUIZ_RE.match(lines[0])
        if not m:
            continue
        qid, kind, tail = m.group(1), m.group(2), m.group(4).strip()
        cut = None
        for i, l in enumerate(lines):
            if l.startswith('**答案：') or l.startswith('**要点（标准答案）**'):
                cut = i
                break
        if cut is None:
            continue
        ans = ' '.join(l.strip() for l in lines[cut:] if not l.startswith('**来源：'))
        qs.append({'id': qid, 'kind': kind, 'p': 'P1-P10', 'q': tail, 'a': ans, 'pts': ''})
    return qs

all_q = []
for d in DOMAINS:
    for item in parse_bank(os.path.join(BASE, 'out', d, 'interview-bank.md')):
        item['dom'] = d
        item['domName'] = DOM_NAME[d]
        all_q.append(item)
print(f'面试题: {len(all_q)}')
for d in DOMAINS:
    for item in parse_quiz_bank(os.path.join(BASE, 'out', d, 'quiz-bank.md')):
        item['dom'] = d
        item['domName'] = DOM_NAME[d]
        all_q.append(item)
print(f'总计: {len(all_q)} 条（面试 + 填空/简答）')

html = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>全库检索手册（##TOTAL## 条）</title>
<style>
:root{--bg:#0f1420;--card:#1a2130;--fg:#e8ecf3;--sub:#8b96a9;--acc:#4f8cff;--line:#2a3346}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--fg);font:15px/1.65 "Segoe UI",system-ui,"Microsoft YaHei",sans-serif;padding:24px}
.wrap{max-width:900px;margin:0 auto}
h1{font-size:20px;margin-bottom:4px}
.sub{color:var(--sub);font-size:13px;margin-bottom:14px}
.bar{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}
input,select{background:var(--card);color:var(--fg);border:1px solid var(--line);border-radius:8px;padding:8px 12px;font-size:14px}
input{flex:1;min-width:220px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin-bottom:12px;cursor:pointer}
.card:hover{border-color:var(--acc)}
.badge{display:inline-block;font-size:11px;padding:2px 8px;border-radius:10px;background:rgba(79,140,255,.15);color:var(--acc);margin-right:6px}
.q{font-size:15px;margin-top:6px;white-space:pre-wrap}
.a{display:none;margin-top:10px;padding:12px 14px;background:rgba(79,140,255,.07);border-left:3px solid var(--acc);border-radius:6px;color:var(--sub);font-size:13px;white-space:pre-wrap}
.card.open .a{display:block}
.pager{display:flex;gap:10px;justify-content:center;align-items:center;margin:18px 0;color:var(--sub)}
.pager button{background:var(--card);color:var(--fg);border:1px solid var(--line);border-radius:8px;padding:6px 14px;cursor:pointer}
.stat{color:var(--sub);font-size:13px;margin-bottom:10px}
</style>
</head>
<body>
<div class="wrap">
  <h1>全库检索手册</h1>
  <div class="sub">面试题 5580 + 笔试主观题（填空/简答）· 点卡片展开答案 · 关键词全文检索</div>
  <div class="bar">
    <input id="kw" placeholder="关键词检索（如：三级缓存 / watchdog / SLO / 脏读）">
    <select id="fDom"><option value="">全部域</option></select>
    <select id="fKind">
      <option value="">全部题型</option>
      <option>概念考察</option><option>误用纠错</option><option>原理深挖</option>
      <option>工程落地</option><option>版本演进</option><option>结论依据</option>
      <option>边界追问</option><option>追问链</option>
      <option>填空</option><option>简答</option>
    </select>
  </div>
  <div class="stat">命中 <b id="cnt">0</b> 条（背诵：先自己默答 → 点卡片对照答案）</div>
  <div id="app"></div>
  <div class="pager"><button id="pgPrev">← 上一页</button><span id="pgInfo"></span><button id="pgNext">下一页 →</button></div>
</div>
<script>
const Q = ##DATA##;
let page = 0;
const PAGE = 50;
function filtered(){
  const kw = document.getElementById('kw').value.trim().toLowerCase();
  const d = document.getElementById('fDom').value;
  const k = document.getElementById('fKind').value;
  return Q.filter(q =>
    (!d || q.dom===d) && (!k || q.kind===k) &&
    (!kw || (q.q+' '+q.a+' '+q.pts).toLowerCase().includes(kw)));
}
function esc(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;'); }
function render(){
  const list = filtered();
  document.getElementById('cnt').textContent = list.length;
  const pages = Math.max(1, Math.ceil(list.length/PAGE));
  if(page >= pages) page = pages-1;
  if(page < 0) page = 0;
  const slice = list.slice(page*PAGE, page*PAGE+PAGE);
  const app = document.getElementById('app');
  app.innerHTML = slice.map(q =>
    `<div class="card" data-id="${q.id}">` +
    `<span class="badge">${q.domName}</span><span class="badge">${q.kind}</span>` +
    (q.p && q.p !== 'P1-P10' ? `<span class="badge">${q.p}</span>` : '') +
    `<span style="color:var(--sub);font-size:11px">${q.id}</span>` +
    `<div class="q">${esc(q.q)}</div>` +
    `<div class="a">${esc(q.a)}${q.pts ? '\n【评分点】' + esc(q.pts) : ''}</div></div>`).join('')
    || '<div class="card">无命中结果。</div>';
  app.querySelectorAll('.card').forEach(c => c.onclick = () => c.classList.toggle('open'));
  document.getElementById('pgInfo').textContent = `第 ${page+1}/${pages} 页`;
}
document.getElementById('kw').oninput = () => { page = 0; render(); };
document.getElementById('fDom').onchange = () => { page = 0; render(); };
document.getElementById('fKind').onchange = () => { page = 0; render(); };
document.getElementById('pgPrev').onclick = () => { page--; render(); };
document.getElementById('pgNext').onclick = () => { page++; render(); };
const fd = document.getElementById('fDom');
Object.entries(##DOMS##).forEach(([k,v])=>{ const o=document.createElement('option'); o.value=k; o.textContent=v; fd.appendChild(o); });
render();
</script>
</body>
</html>
"""
data = json.dumps(all_q, ensure_ascii=False, separators=(',', ':'))
html = html.replace('##DATA##', data).replace('##DOMS##', json.dumps(DOM_NAME, ensure_ascii=False)).replace('##TOTAL##', str(len(all_q)))
open(OUT, 'w', encoding='utf-8').write(html)
print(f'输出: {OUT}（{os.path.getsize(OUT)/1024:.0f} KB）')
