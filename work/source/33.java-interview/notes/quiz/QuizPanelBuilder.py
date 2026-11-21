# -*- coding: utf-8 -*-
"""交互刷题面板构建器：从 11 域 quiz-bank.md 抽取客观题（单选正向/反向 + 判断），
生成单文件 HTML（notes/quiz/exams/interactive-quiz.html），离线可用。
功能：域/题型过滤、顺序/随机刷题、点击判分、解析即时展开、错题标记与统计、进度保存（localStorage）。
用法: python QuizPanelBuilder.py
"""
import re, os, json

DOMAINS = ['java-basics','concurrency','jvm','spring','mysql','redis','mongodb','mq','distributed','ai','algorithm','java-ai','agent-dev']
DOM_NAME = {'java-basics':'Java 基础','concurrency':'并发','jvm':'JVM','spring':'Spring','mysql':'MySQL',
            'redis':'Redis','mongodb':'MongoDB','mq':'MQ','distributed':'分布式','ai':'AI/Agent','algorithm':'算法','java-ai':'Java AI 框架','agent-dev':'Agent 开发'}
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, 'exams', 'interactive-quiz.html')

HEAD_RE = re.compile(r'^\*\*Q[\w\-]+（(单选·正向|单选·反向|场景单选|判断|场景判断)·([^）]+）)\*\* ?(.*)$')

def parse_bank(path):
    """返回题目列表: {id,dom,topic,kind,stem,opts,ans,why}"""
    text = open(path, encoding='utf-8').read()
    blocks = re.split(r'\n(?=\*\*Q[\w\-]+（)', text)
    dom = os.path.basename(path).split(os.sep)[0] if os.sep in path else None
    qs = []
    for b in blocks:
        if not b.startswith('**Q'):
            continue
        lines = b.strip().split('\n')
        m = HEAD_RE.match(lines[0])
        if not m:
            continue
        kind, dim, tail = m.group(1), m.group(2), m.group(3).strip()
        qid = re.match(r'^\*\*(Q[\w\-]+)（', lines[0]).group(1)
        # 来源 id
        src = ''
        for l in lines:
            if l.startswith('**来源：**'):
                src = l.replace('**来源：**', '').strip()
                break
        why_lines = []
        ans_letter = None
        opts = []
        for l in lines[1:]:
            mo = re.match(r'^- ([A-D])\. (.*)$', l)
            if mo:
                opts.append(mo.group(2))
                continue
            ma = re.match(r'^\*\*答案：([A-D])\*\*$', l)
            if ma:
                ans_letter = ma.group(1)
                continue
            if l.startswith('**解析：**'):
                why_lines.append(l)
                continue
            if l.startswith('**来源：**'):
                continue
            if why_lines:
                why_lines.append(l)
        if '单选' in kind:
            if ans_letter is None or len(opts) < 4:
                continue
            ans = ord(ans_letter) - ord('A')
            if not (0 <= ans < len(opts)):
                continue
            stem = tail
            qs.append({'id': qid, 'kind': '单选', 'reverse': kind == '单选·反向',
                       'stem': stem, 'opts': opts, 'ans': ans,
                       'why': ' '.join(x.replace('**解析：**', '').strip() for x in why_lines if x.replace('**解析：**','').strip())})
        else:  # 判断
            ans_line = next((l for l in lines if l.startswith('**答案：')), None)
            if ans_line is None:
                continue
            truth = ans_line.startswith('**答案：对')
            qs.append({'id': qid, 'kind': '判断', 'reverse': False,
                       'stem': tail, 'opts': [], 'ans': 0 if truth else 1,
                       'why': ans_line.replace('**答案：对。**', '').replace('**答案：错。**', '').strip()})
    return qs

all_q = []
for d in DOMAINS:
    path = os.path.join(BASE, 'out', d, 'quiz-bank.md')
    for q in parse_bank(path):
        q['dom'] = d
        q['domName'] = DOM_NAME[d]
        all_q.append(q)
print(f'客观题抽取: {len(all_q)} 题（单选 {sum(1 for q in all_q if q["kind"]=="单选")} / 判断 {sum(1 for q in all_q if q["kind"]=="判断")}）')

html = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>Java P10 笔试刷题面板（OBJECTIVE ##TOTAL## 题）</title>
<style>
:root{--bg:#0f1420;--card:#1a2130;--fg:#e8ecf3;--sub:#8b96a9;--acc:#4f8cff;--ok:#3fb96f;--bad:#e05b5b;--line:#2a3346}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--fg);font:15px/1.65 "Segoe UI",system-ui,"Microsoft YaHei",sans-serif;padding:24px}
.wrap{max-width:860px;margin:0 auto}
h1{font-size:20px;margin-bottom:4px}
.sub{color:var(--sub);font-size:13px;margin-bottom:16px}
.bar{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px}
select,button{background:var(--card);color:var(--fg);border:1px solid var(--line);border-radius:8px;padding:7px 12px;font-size:14px;cursor:pointer}
button:hover{border-color:var(--acc)}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 20px;margin-bottom:14px}
.meta{color:var(--sub);font-size:12px;margin-bottom:8px}
.meta b{color:var(--acc);font-weight:600}
.stem{font-size:16px;margin-bottom:12px;white-space:pre-wrap}
.opt{display:block;width:100%;text-align:left;background:transparent;border:1px solid var(--line);border-radius:8px;padding:10px 14px;margin:8px 0;color:var(--fg);font-size:14px;cursor:pointer;transition:border-color .15s,background .15s}
.opt:hover{border-color:var(--acc)}
.opt.right{border-color:var(--ok);background:rgba(63,185,111,.12)}
.opt.wrong{border-color:var(--bad);background:rgba(224,91,91,.12)}
.opt:disabled{cursor:default;opacity:.9}
.tf{display:flex;gap:10px}
.tf .opt{flex:1;text-align:center}
.why{display:none;margin-top:12px;padding:12px 14px;background:rgba(79,140,255,.08);border-left:3px solid var(--acc);border-radius:6px;color:var(--sub);font-size:13px;white-space:pre-wrap}
.why.show{display:block}
.foot{display:flex;justify-content:space-between;align-items:center;margin-top:16px}
.stat{position:sticky;top:0;background:var(--bg);padding:10px 0;z-index:5;border-bottom:1px solid var(--line);margin-bottom:14px;color:var(--sub);font-size:13px;display:flex;gap:16px;flex-wrap:wrap}
.stat b{color:var(--fg)}
</style>
</head>
<body>
<div class="wrap">
  <h1>Java P10 笔试刷题面板</h1>
  <div class="sub">客观题集（单选 + 判断，来自 11 域知识点矩阵，点击判分）· 离线可用 · 进度自动保存 · 键盘：1-4 选答 / T 对 / F 错 / 回车下一题</div>
  <div class="bar">
    <select id="fDom"><option value="">全部域</option></select>
    <select id="fKind">
      <option value="">全部题型</option>
      <option value="单选">单选</option>
      <option value="判断">判断</option>
      <option value="wrong">只刷错题</option>
    </select>
    <button id="bShuffle">换序</button>
    <button id="bReset">重置进度</button>
    <button id="bExport">导出错题本</button>
    <button id="bDaily">每日 10 题</button>
  </div>
  <div class="stat">
    <span>进度 <b id="sPos">0</b>/<b id="sTotal">0</b></span>
    <span>正确 <b id="sOk">0</b></span>
    <span>错误 <b id="sBad">0</b></span>
    <span>正确率 <b id="sRate">—</b></span>
  </div>
  <div id="app"></div>
  <div class="foot"><button id="bNext">下一题 →</button></div>
</div>
<script>
const Q = ##DATA##;
const KEY = 'p10-quiz-progress-v1';
let state = {idx:0, order:[], answered:{}, stats:{ok:0,bad:0}};
try{ const saved = JSON.parse(localStorage.getItem(KEY)); if(saved && saved.state) state = saved.state; }catch(e){}
if(!Array.isArray(state.order) || state.order.length === 0){ state.order = Q.map((_,i)=>i); }
if(!state.answered) state.answered = {};
if(!state.stats) state.stats = {ok:0,bad:0};
let curQ = null;

function save(){ try{ localStorage.setItem(KEY, JSON.stringify(state)); }catch(e){} }
let mode = 'all';
let dailyIds = [];
function ensureDaily(){
  const today = new Date().toISOString().slice(0,10);
  try{ const s = JSON.parse(localStorage.getItem(KEY+'-daily')); if(s && s.date===today){ dailyIds=s.ids; return; } }catch(e){}
  let seed=0; for(const c of today) seed=(seed*31+c.charCodeAt(0))>>>0;
  const rnd=()=>{ seed=(seed*1664525+1013904223)>>>0; return seed/4294967296; };
  const arr=Q.map((_,i)=>i);
  for(let i=arr.length-1;i>0;i--){ const j=Math.floor(rnd()*(i+1)); [arr[i],arr[j]]=[arr[j],arr[i]]; }
  dailyIds=arr.slice(0,10).map(i=>Q[i].id);
  try{ localStorage.setItem(KEY+'-daily', JSON.stringify({date:today, ids:dailyIds})); }catch(e){}
}
function visible(){
  const d=document.getElementById('fDom').value, k=document.getElementById('fKind').value;
  const src = mode==='daily' ? dailyIds.map(id=>Q.find(q=>q.id===id)).filter(Boolean) : state.order.map(i=>Q[i]);
  let list = src.filter(q =>
    (!d || q.dom===d) && (!k || (k==='wrong' ? state.answered[q.id]===false : q.kind===k)));
  return list;
}
function render(){
  const list = visible();
  const app = document.getElementById('app');
  document.getElementById('sTotal').textContent = list.length;
  let ok=0, bad=0;
  list.forEach(q=>{ const a=state.answered[q.id]; if(a===true)ok++; if(a===false)bad++; });
  document.getElementById('sOk').textContent = ok;
  document.getElementById('sBad').textContent = bad;
  document.getElementById('sRate').textContent = (ok+bad)? Math.round(ok*100/(ok+bad))+'%':'—';
  if(!list.length){ app.innerHTML='<div class="card">该筛选下没有题目。</div>'; return; }
  if(state.idx >= list.length) state.idx = 0;
  const q = list[state.idx];
  document.getElementById('sPos').textContent = state.idx+1;
  const ans = state.answered[q.id];
  let html = `<div class="card"><div class="meta"><b>${q.domName}</b> · ${q.id} · ${q.kind}${q.reverse?'（选<b>错误</b>项）':''}</div>`;
  html += `<div class="stem">${q.stem.replace(/</g,'&lt;')}</div>`;
  if(q.kind==='单选'){
    q.opts.forEach((o,i)=>{
      const cls = ans===undefined||ans===null ? '' : (i===q.ans?'right':(i===ans?'wrong':''));
      html += `<button class="opt ${cls}" data-i="${i}" ${ans!==undefined&&ans!==null?'disabled':''}>${'ABCD'[i]}. ${o.replace(/</g,'&lt;')}</button>`;
    });
  } else {
    ['对','错'].forEach((t,i)=>{
      const cls = ans===undefined||ans===null ? '' : (i===q.ans?'right':(i===ans?'wrong':''));
      html += `<button class="opt ${cls}" data-i="${i}" ${ans!==undefined&&ans!==null?'disabled':''} style="flex:1;text-align:center">${t}</button>`;
    });
  }
  if(ans!==undefined&&ans!==null){
    html += `<div class="why show">${(q.why||'（无解析）').replace(/</g,'&lt;')}</div>`;
  } else {
    html += `<div class="why" id="whyBox"></div>`;
  }
  html += '</div>';
  app.innerHTML = html;
  app.querySelectorAll('.opt').forEach(btn=>{
    btn.onclick = ()=>{
      const pick = +btn.dataset.i;
      state.answered[q.id] = pick===q.ans;
      if(pick===q.ans) state.stats.ok++; else state.stats.bad++;
      save(); render();
    };
  });
  curQ = q;
}
document.getElementById('app').addEventListener('click', e=>{
  if(e.target.id==='bNext') return;
});
document.getElementById('bNext').onclick = ()=>{ state.idx++; const n=visible().length; if(state.idx>=n) state.idx=0; save(); render(); };
document.getElementById('bShuffle').onclick = ()=>{
  for(let i=Q.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [Q[i],Q[j]]=[Q[j],Q[i]]; }
  state.idx=0; render();
};
document.getElementById('bReset').onclick = ()=>{ state.answered={}; state.stats={ok:0,bad:0}; state.idx=0; save(); render(); };
document.addEventListener('keydown', e=>{
  if(e.target && (e.target.tagName==='SELECT' || e.target.tagName==='INPUT')) return;
  if(!curQ) return;
  const btns=[...document.querySelectorAll('#app button.opt')];
  if(!btns.length) return;
  const answered = state.answered[curQ.id] !== undefined && state.answered[curQ.id] !== null;
  if(answered){
    if(e.key==='Enter'||e.key===' '){ e.preventDefault(); document.getElementById('bNext').click(); }
    return;
  }
  let idx=-1;
  if(curQ.kind==='单选'){ if(e.key>='1'&&e.key<='4') idx=+e.key-1; }
  else { const k=e.key.toLowerCase(); if(e.key==='1'||k==='t') idx=0; if(e.key==='2'||k==='f') idx=1; }
  if(idx>=0 && btns[idx] && !btns[idx].disabled) btns[idx].click();
});
document.getElementById('bDaily').onclick = ()=>{
  if(mode==='daily'){ mode='all'; } else { ensureDaily(); mode='daily'; }
  document.getElementById('bDaily').textContent = mode==='daily' ? '返回全库' : '每日 10 题';
  state.idx=0; save(); render();
};
document.getElementById('fDom').onchange = ()=>{ state.idx=0; render(); };
document.getElementById('fKind').onchange = ()=>{ state.idx=0; render(); };
function wrongList(){
  return state.order.map(i=>Q[i]).filter(q=>state.answered[q.id]===false);
}
function exportWrong(){
  const list = wrongList();
  if(!list.length) return null;
  let md = '# 错题本（自动导出 ' + new Date().toLocaleString() + '）\n\n共 ' + list.length + ' 题\n\n';
  list.forEach((q,i)=>{
    md += '## ' + (i+1) + '. ' + q.id + '（' + q.domName + ' · ' + q.kind + '）\n\n';
    md += q.stem + '\n\n';
    if(q.kind==='单选'){
      q.opts.forEach((o,j)=>{ md += '- ' + 'ABCD'[j] + '. ' + o + (j===q.ans ? '  ✅正确' : '') + '\n'; });
    } else {
      md += '正确答案：' + (q.ans===0?'对':'错') + '\n';
    }
    md += '\n解析：' + (q.why||'（无）') + '\n\n---\n\n';
  });
  return md;
}
document.getElementById('bExport').onclick = ()=>{
  const md = exportWrong();
  if(md===null){ alert('当前没有错题记录'); return; }
  const blob = new Blob([md], {type:'text/markdown'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = '错题本-' + new Date().toISOString().slice(0,10) + '.md';
  a.click();
  URL.revokeObjectURL(a.href);
};
const fd = document.getElementById('fDom');
Object.entries(##DOMS##).forEach(([k,v])=>{ const o=document.createElement('option'); o.value=k; o.textContent=v; fd.appendChild(o); });
render();
</script>
</body>
</html>
"""

data = json.dumps(all_q, ensure_ascii=False, separators=(',', ':'))
doms = json.dumps(DOM_NAME, ensure_ascii=False)
html = html.replace('##DATA##', data).replace('##DOMS##', doms).replace('##TOTAL##', str(len(all_q)))
open(OUT, 'w', encoding='utf-8').write(html)
print(f'输出: {OUT}（{os.path.getsize(OUT)/1024:.0f} KB）')
