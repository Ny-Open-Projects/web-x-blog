/* QuantSite — 模拟数据 + 看板渲染（Phase 0 打样，数据为演示用模拟值，非实时行情） */
(function(){
  "use strict";
  // ============ 模拟数据（MOCK，非实时；换真实数据时仅替换此两处） ============
  const MOCK_MARKET = {
    updated: "2026-10-23 15:00（模拟收盘）",
    rating: "中性偏多",
    ratingClass: "up",
    reason: "主要指数缩量整理、涨跌家数均衡，权重稳、题材活跃度中性，短线环境偏震荡略偏多。",
    indices: [
      { name:"上证指数", val:3228.46, chg:+0.42, amt:"成交额 3821 亿" },
      { name:"深证成指", val:10412.73, chg:+0.31, amt:"成交额 4689 亿" },
      { name:"沪深300",  val:3876.15, chg:+0.55, amt:"成交额 2410 亿" },
      { name:"创业板指", val:2154.08, chg:-0.27, amt:"成交额 1975 亿" }
    ]
  };

  const MOCK_PORTFOLIO = [
    {
      name:"沪深300ETF", code:"510300", price:3.942, chg:+0.86,
      vol:"128.6万手", volRatio:"1.12", turnover:"0.62%", cap:"主力净流入 +1.8亿",
      afternoon:"探底回升", verdict:"偏多", dir:"up", op:"buy",
      tf:{ next:["偏多","+0.6~1.2%","中"], week:["偏多","+1.5~3.0%","中高"], month:["偏多","+3~6%","中"] },
      support:"3.88", resistance:"4.02",
      prob:[58,22,20], conf:"中",
      action:"若回踩 3.88 一线缩量不破，则可低吸一笔；若放量跌破 3.85，则止损离场；否则持股观望，上方 4.02 附近减仓兑现。"
    },
    {
      name:"中证500ETF", code:"510500", price:6.105, chg:+0.23,
      vol:"42.3万手", volRatio:"0.95", turnover:"0.48%", cap:"主力净流入 +0.4亿",
      afternoon:"震荡", verdict:"中性", dir:"flat", op:"hold",
      tf:{ next:["中性","-0.5~+0.8%","中"], week:["中性","-1~+2%","中"], month:["偏多","+2~4%","中低"] },
      support:"6.02", resistance:"6.28",
      prob:[45,25,30], conf:"中",
      action:"震荡区间内观望为主；若放量突破 6.28 则顺势跟进，若跌破 6.02 则减仓，中间价位不追。"
    },
    {
      name:"新能源车ETF", code:"515030", price:2.138, chg:+1.94,
      vol:"96.7万手", volRatio:"1.86", turnover:"1.95%", cap:"主力净流入 +3.6亿",
      afternoon:"上攻", verdict:"偏多", dir:"up", op:"buy",
      tf:{ next:["偏多","+1~2.5%","中高"], week:["偏多","+3~6%","中"], month:["偏多","+5~10%","中"] },
      support:"2.05", resistance:"2.24",
      prob:[64,18,18], conf:"中高",
      action:"放量上攻、量价配合，可持股待涨；若冲高 2.24 附近滞涨缩量，则部分止盈；止损设 2.05 下方。"
    },
    {
      name:"券商ETF", code:"512000", price:0.968, chg:-0.82,
      vol:"158.2万手", volRatio:"1.43", turnover:"1.32%", cap:"主力净流出 -2.1亿",
      afternoon:"冲高回落", verdict:"偏空", dir:"down", op:"trim",
      tf:{ next:["偏空","-0.8~1.5%","中"], week:["中性","-1.5~+1%","中低"], month:["中性","-2~+3%","低"] },
      support:"0.95", resistance:"0.99",
      prob:[26,48,26], conf:"中",
      action:"冲高回落、主力流出，宜逢高减仓；若反抽 0.99 附近无量，则继续降低仓位；跌至 0.95 再看能否企稳。"
    },
    {
      name:"科创50ETF", code:"588000", price:1.024, chg:+1.18,
      vol:"88.4万手", volRatio:"1.31", turnover:"1.10%", cap:"主力净流入 +1.2亿",
      afternoon:"探底回升", verdict:"偏多", dir:"up", op:"buy",
      tf:{ next:["偏多","+0.8~1.8%","中"], week:["偏多","+2~5%","中"], month:["偏多","+4~8%","中"] },
      support:"1.00", resistance:"1.08",
      prob:[60,20,20], conf:"中",
      action:"缩量回踩 1.00 不破可低吸；若放量突破 1.08 则加仓跟进；止损 0.99，破位则离场观望。"
    }
  ];

  const COMBO_ACTION =
    "组合当前中性偏多：新能源车、科创50 量价配合可持可低吸；沪深300 回踩低吸；中证500 区间观望；券商冲高回落宜减仓。" +
    "总仓位建议 5~6 成，单票不超 2 成；任何标的放量破位（跌破所示支撑）即执行止损，不留恋。";

  // ============ 渲染 ============
  const $ = s => document.querySelector(s);
  const dirClass = d => d==="偏多"||d==="上攻"||d==="探底回升" ? "up" : (d==="偏空"||d==="冲高回落" ? "down" : "flat");
  const sign = n => (n>=0?"+":"") + n.toFixed(2);
  const opTag = op => op==="buy"?'<span class="tag buy">低吸/持</span>':op==="trim"?'<span class="tag trim">减仓</span>':'<span class="tag hold">观望</span>';

  function renderMarket(){
    $("#updated").textContent = MOCK_MARKET.updated;
    $("#indexGrid").innerHTML = MOCK_MARKET.indices.map(i=>{
      const c = i.chg>=0?"up":"down";
      return `<div class="card"><div class="idx-name">${i.name}</div>
        <div class="idx-val ${c}">${i.val.toFixed(2)}</div>
        <div class="idx-chg ${c}">${sign(i.chg)}%</div>
        <div class="idx-sub">${i.amt}</div></div>`;
    }).join("");
    $("#mktRating").innerHTML =
      `<span class="label">大盘短线环境</span>
       <span class="verdict ${MOCK_MARKET.ratingClass}">${MOCK_MARKET.rating}</span>
       <span class="reason">${MOCK_MARKET.reason}</span>`;
  }

  function renderOverview(){
    $("#overviewTable").innerHTML = MOCK_PORTFOLIO.map(s=>{
      const c = s.chg>=0?"up":"down";
      return `<tr>
        <td><b>${s.name}</b> <span style="color:var(--faint)">${s.code}</span></td>
        <td class="${c}">${s.price.toFixed(3)}</td>
        <td class="${c}">${sign(s.chg)}%</td>
        <td>${s.volRatio}</td><td>${s.turnover}</td>
        <td class="dir-${s.dir==='up'?'up':s.dir==='down'?'down':'flat'}">${s.afternoon}</td>
        <td class="dir-${s.dir==='up'?'up':s.dir==='down'?'down':'flat'}">${s.verdict}</td>
        <td>${opTag(s.op)}</td></tr>`;
    }).join("");
  }

  function renderStocks(){
    $("#stockGrid").innerHTML = MOCK_PORTFOLIO.map(s=>{
      const c = s.chg>=0?"up":"down";
      const [pu,pd,pf]=s.prob;
      return `<div class="stock-card">
        <div class="sc-head">
          <div><div class="name">${s.name}</div><div class="code">${s.code}</div></div>
          <div class="px"><div class="p ${c}">${s.price.toFixed(3)}</div><div class="c ${c}">${sign(s.chg)}%</div></div>
        </div>
        <div class="kv">
          <div><div class="k">成交量/量比</div><div class="v">${s.vol} · ${s.volRatio}</div></div>
          <div><div class="k">换手率</div><div class="v">${s.turnover}</div></div>
          <div><div class="k">多空量能</div><div class="v ${s.cap.includes('+')?'up':'down'}">${s.cap}</div></div>
        </div>
        <div class="block"><div class="bt">午后方向</div>
          <div class="tf"><span class="t dir-${dirClass(s.afternoon)}">${s.afternoon}</span></div></div>
        <div class="block"><div class="bt">多时间维度趋势（方向 / 幅度 / 置信度）</div>
          <div class="tf">
            <span class="t">明日 <b class="${dirClass(s.tf.next[0])}">${s.tf.next[0]}</b> ${s.tf.next[1]} · ${s.tf.next[2]}</span>
            <span class="t">下周 <b class="${dirClass(s.tf.week[0])}">${s.tf.week[0]}</b> ${s.tf.week[1]} · ${s.tf.week[2]}</span>
            <span class="t">下月 <b class="${dirClass(s.tf.month[0])}">${s.tf.month[0]}</b> ${s.tf.month[1]} · ${s.tf.month[2]}</span>
          </div></div>
        <div class="block"><div class="bt">支撑 / 压力</div>
          <div class="sp"><span>支撑 <b class="down">${s.support}</b></span><span>压力 <b class="up">${s.resistance}</b></span>
          <span style="margin-left:auto;color:var(--muted)">综合 <b class="${dirClass(s.verdict)}">${s.verdict}</b> · 置信度 ${s.conf}</span></div></div>
        <div class="block"><div class="bt">情景概率（多 / 空 / 震荡）</div>
          <div class="prob"><span class="pu" style="width:${pu}%"></span><span class="pd" style="width:${pd}%"></span><span class="pf" style="width:${pf}%"></span></div>
          <div class="prob-legend"><span class="up">多 ${pu}%</span><span class="down">空 ${pd}%</span><span>震荡 ${pf}%</span></div></div>
        <div class="action"><span class="if">操作指引（条件式）：</span>${s.action}</div>
      </div>`;
    }).join("");
    $("#comboAction").textContent = COMBO_ACTION;
  }

  document.addEventListener("DOMContentLoaded", ()=>{
    if($("#indexGrid")) renderMarket();
    if($("#overviewTable")) renderOverview();
    if($("#stockGrid")) renderStocks();
  });
})();
