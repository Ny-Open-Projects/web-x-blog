# -*- coding: utf-8 -*-
"""闪卡交互查看器构建器：11 域事实矩阵 → 单文件翻卡 HTML（exams/flashcards.html）。
功能：翻卡自测（正面→看背面→标会/不会）、域过滤、只看未掌握、进度 localStorage 持久、乱序。
用法: python FlashcardViewerBuilder.py
"""
import os, json

DOMAINS = ['java-basics','concurrency','jvm','spring','mysql','redis','mongodb','mq','distributed','ai','algorithm','java-ai','agent-dev']
DOM_NAME = {'java-basics':'Java 基础','concurrency':'并发','jvm':'JVM','spring':'Spring','mysql':'MySQL',
            'redis':'Redis','mongodb':'MongoDB','mq':'MQ','distributed':'分布式','ai':'AI/Agent','algorithm':'算法','java-ai':'Java AI 框架','agent-dev':'Agent 开发'}
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, 'exams', 'flashcards.html')

cards = []
for d in DOMAINS:
    for line in open(os.path.join(BASE, 'facts', f'{d}.txt'), encoding='utf-8'):
        t = line.strip()
        if not t or t.startswith('#') or len(t.split('|')) != 12:
            continue
        f = t.split('|')
        rid, topic, dim, term = f[0], f[2].strip(), f[3].strip(), f[4].strip()
        back = [f[5].strip(), '原理：' + f[6].strip()]
        if f[10].strip():
            back.append('用法：' + f[10].strip())
        if f[11].strip():
            back.append('锚点：' + f[11].strip())
        cards.append({'id': rid, 'dom': d, 'domName': DOM_NAME[d],
                      'front': f'{topic} · {term if term else dim}（{dim}）',
                      'back': chr(10).join(back)})
print(f'闪卡: {len(cards)} 张')

html = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>闪卡自测（##TOTAL## 张）</title>
<style>
:root{--bg:#0f1420;--card:#1a2130;--fg:#e8ecf3;--sub:#8b96a9;--acc:#4f8cff;--ok:#3fb96f;--bad:#e05b5b;--line:#2a3346}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--fg);font:15px/1.65 "Segoe UI",system-ui,"Microsoft YaHei",sans-serif;padding:24px}
.wrap{max-width:760px;margin:0 auto}
h1{font-size:20px;margin-bottom:4px}
.sub{color:var(--sub);font-size:13px;margin-bottom:14px}
.bar{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}
select,button{background:var(--card);color:var(--fg);border:1px solid var(--line);border-radius:8px;padding:7px 12px;font-size:14px;cursor:pointer}
.stat{color:var(--sub);font-size:13px;margin-bottom:12px}
.stat b{color:var(--fg)}
.flip{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:26px 24px;min-height:220px;margin-bottom:14px}
.tag{color:var(--sub);font-size:12px;margin-bottom:10px}
.tag b{color:var(--acc)}
.front{font-size:17px;font-weight:600}
.back{margin-top:14px;padding-top:14px;border-top:1px dashed var(--line);color:var(--sub);font-size:14px;white-space:pre-wrap}
.ops{display:flex;gap:10px;margin-bottom:14px}
.ops button{flex:1;padding:12px}
.yes{border-color:var(--ok)!important;color:var(--ok)!important}
.no{border-color:var(--bad)!important;color:var(--bad)!important}
</style>
</head>
<body>
<div class="wrap">
  <h1>闪卡自测</h1>
  <div class="sub">##TOTAL## 张（11 域矩阵生成）· 正面自问 → 看背面 → 标「会/不会」· 进度自动保存</div>
  <div class="bar">
    <select id="fDom"><option value="">全部域</option></select>
    <select id="fMode">
      <option value="all">全部卡片</option>
      <option value="unknown">只看不会的</option>
    </select>
    <button id="bShuffle">乱序</button>
    <button id="bReset">重置进度</button>
  </div>
  <div class="stat">当前 <b id="sPos">0</b>/<b id="sTotal">0</b> ｜ 已掌握 <b id="sOk">0</b> ｜ 未掌握 <b id="sBad">0</b></div>
  <div class="flip">
    <div class="tag"><b id="cDom"></b> · <span id="cId"></span></div>
    <div class="front" id="cFront"></div>
    <div class="back" id="cBack" style="display:none"></div>
  </div>
  <div class="ops">
    <button id="bFlip">看背面（空格）</button>
    <button id="bNo">不会（F）</button>
    <button id="bYes">会了（G）</button>
    <button id="bNext">下一张（N）</button>
  </div>
</div>
<script>
const C = ##DATA##;
const KEY = 'p10-flash-progress-v1';
let state = {order: C.map((_,i)=>i), idx: 0, known: {}};
try{ const s = JSON.parse(localStorage.getItem(KEY)); if(s && s.order) state = s; }catch(e){}
if(!Array.isArray(state.order) || !state.order.length) state.order = C.map((_,i)=>i);
if(!state.known) state.known = {};
function save(){ try{ localStorage.setItem(KEY, JSON.stringify(state)); }catch(e){} }
function visible(){
  const d = document.getElementById('fDom').value;
  const m = document.getElementById('fMode').value;
  return state.order.map(i=>C[i]).filter(c =>
    (!d || c.dom===d) && (m!=='unknown' || state.known[c.id]===false));
}
let cur = null;
function render(){
  const list = visible();
  document.getElementById('sTotal').textContent = list.length;
  const ok = list.filter(c=>state.known[c.id]===true).length;
  const bad = list.filter(c=>state.known[c.id]===false).length;
  document.getElementById('sOk').textContent = ok;
  document.getElementById('sBad').textContent = bad;
  if(!list.length){ document.getElementById('cFront').textContent='（该筛选下没有卡片，恭喜清空！）'; document.getElementById('cDom').textContent=''; document.getElementById('cId').textContent=''; document.getElementById('cBack').style.display='none'; cur=null; return; }
  if(state.idx >= list.length) state.idx = 0;
  cur = list[state.idx];
  document.getElementById('sPos').textContent = state.idx+1;
  document.getElementById('cDom').textContent = cur.domName;
  document.getElementById('cId').textContent = cur.id;
  document.getElementById('cFront').textContent = cur.front;
  document.getElementById('cBack').textContent = cur.back;
  document.getElementById('cBack').style.display = 'none';
  document.getElementById('bFlip').textContent = '看背面（空格）';
}
function flip(){ document.getElementById('cBack').style.display = document.getElementById('cBack').style.display==='none' ? 'block':'none'; document.getElementById('bFlip').textContent = '翻回正面（空格）'; }
function mark(known){
  if(!cur) return;
  state.known[cur.id] = known; save();
  document.getElementById('bNext').click();
}
document.getElementById('bFlip').onclick = flip;
document.getElementById('bYes').onclick = () => mark(true);
document.getElementById('bNo').onclick = () => mark(false);
document.getElementById('bNext').onclick = () => { state.idx++; const n=visible().length; if(n && state.idx>=n) state.idx=0; save(); render(); };
document.getElementById('bShuffle').onclick = () => { for(let i=state.order.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [state.order[i],state.order[j]]=[state.order[j],state.order[i]]; } state.idx=0; save(); render(); };
document.getElementById('bReset').onclick = () => { state.known={}; state.idx=0; save(); render(); };
document.getElementById('fDom').onchange = () => { state.idx=0; render(); };
document.getElementById('fMode').onchange = () => { state.idx=0; render(); };
document.addEventListener('keydown', e=>{
  if(e.target && (e.target.tagName==='SELECT' || e.target.tagName==='INPUT')) return;
  const k = e.key.toLowerCase();
  if(e.key===' ') { e.preventDefault(); flip(); }
  else if(k==='g') mark(true);
  else if(k==='f') mark(false);
  else if(e.key==='n') document.getElementById('bNext').click();
});
const fd = document.getElementById('fDom');
Object.entries(##DOMS##).forEach(([k,v])=>{ const o=document.createElement('option'); o.value=k; o.textContent=v; fd.appendChild(o); });
render();
</script>
</body>
</html>
"""
data = json.dumps(cards, ensure_ascii=False, separators=(',', ':'))
html = html.replace('##DATA##', data).replace('##DOMS##', json.dumps(DOM_NAME, ensure_ascii=False)).replace('##TOTAL##', str(len(cards)))
open(OUT, 'w', encoding='utf-8').write(html)
print(f'输出: {OUT}（{os.path.getsize(OUT)/1024:.0f} KB）')
