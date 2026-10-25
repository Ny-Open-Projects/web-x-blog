"use client";
import { useEffect, useState } from "react";
import dynamic from "next/dynamic";
import type { Board } from "@/lib/market";
import { PERIOD_NAME, type Period } from "@/lib/market";
import { getWatch, saveWatch, validCode } from "@/lib/watch";

const KLineChart = dynamic(() => import("./KLineChart"), {
  ssr: false,
  loading: () => <div style={{ height: 340, display: "grid", placeItems: "center", color: "var(--faint)" }}>图表加载中…</div>,
});

const dirCls = (v: string) => (v === "偏多" || v === "上攻" || v === "探底回升" || v === "震荡上行" ? "up" : v === "偏空" || v === "冲高回落" || v === "震荡下行" ? "down" : "flat");
const opTag = (v: string) => (v === "偏多" ? '<span class="tag buy">低吸/持</span>' : v === "偏空" ? '<span class="tag trim">减仓</span>' : '<span class="tag hold">观望</span>');
const sign = (n: number) => (n >= 0 ? "+" : "") + n.toFixed(2);

export default function Board({ initial }: { initial: Board | null }) {
  const [board, setBoard] = useState<Board | null>(initial);
  const [loading, setLoading] = useState(!initial);
  const [refreshing, setRefreshing] = useState(false);
  const [watch, setWatch] = useState<string[]>([]);
  const [newCode, setNewCode] = useState("");
  const [sel, setSel] = useState("");
  const [period, setPeriod] = useState<Period>("day");

  useEffect(() => {
    const w = getWatch();
    setWatch(w);
    load(w);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const load = async (codes: string[], isRefresh = false, p: Period = period) => {
    if (!codes.length) return;
    isRefresh ? setRefreshing(true) : setLoading(true);
    try {
      const r = await fetch("/api/board?codes=" + codes.join(",") + "&period=" + p);
      const b: Board = await r.json();
      setBoard(b);
      if (b.portfolio?.length) setSel((cur) => (cur && b.portfolio.some((d) => d.code === cur) ? cur : b.portfolio[0].code));
    } finally { setLoading(false); setRefreshing(false); }
  };

  const addCode = () => {
    const c = newCode.trim();
    if (!validCode(c)) { alert("请输入 6 位股票/ETF 代码，如 510300"); return; }
    if (watch.includes(c)) { alert("该代码已在自选中"); return; }
    const w = [...watch, c]; setWatch(w); saveWatch(w); load(w); setNewCode("");
  };
  const removeCode = (c: string) => {
    const w = watch.filter((x) => x !== c);
    const nw = w.length ? w : getWatch();
    setWatch(nw); saveWatch(nw); load(nw);
  };

  if (loading || !board) {
    return <main className="wrap"><div className="banner live"><span className="spin"></span>正在拉取真实行情…</div></main>;
  }

  const selStock = board.portfolio.find((d) => d.code === sel) || board.portfolio[0];

  return (
    <main className="wrap">
      <div className={`banner ${board.live ? "live" : "sim"}`}>
        {board.live ? "📡 实时行情" : "⚠️ 模拟数据"} ｜ 数据源：{board.source} ｜ 更新：{board.updated}
        <button className="btn" style={{ marginLeft: "auto" }} onClick={() => load(watch, true)} disabled={refreshing}>
          {refreshing ? "刷新中…" : "刷新"}
        </button>
      </div>

      <section className="hero">
        <h1>量化决策看板</h1>
        <p>短线择时 · 多时间维度 · 可解释信号 ｜ 基于真实日线指标规则化综合，仅供参考</p>
      </section>

      <section className="section">
        <div className="section-title"><span className="bar"></span>我的自选<span className="sub">本地保存，可增删</span></div>
        <div className="card" style={{ display: "flex", gap: 10, flexWrap: "wrap", alignItems: "center" }}>
          {watch.map((c) => {
            const d = board.portfolio.find((x) => x.code === c);
            return (
              <span key={c} className="tf" style={{ alignItems: "center" }}>
                <span className="t" style={{ cursor: "pointer" }} onClick={() => setSel(c)}>{d ? d.name : c} {d ? <b className={d.changePct >= 0 ? "up" : "down"}>{sign(d.changePct)}%</b> : ""}</span>
                <button className="btn" style={{ padding: "2px 8px" }} onClick={() => removeCode(c)} title="移除">×</button>
              </span>
            );
          })}
          <input className="btn" style={{ width: 110 }} placeholder="代码 510300" value={newCode} maxLength={6} onChange={(e) => setNewCode(e.target.value.replace(/\D/g, ""))} onKeyDown={(e) => e.key === "Enter" && addCode()} />
          <button className="btn primary" onClick={addCode}>+ 添加</button>
        </div>
      </section>

      <section className="section">
        <div className="section-title"><span className="bar"></span>今日大盘环境<span className="sub">大盘评级作为个股决策前置过滤</span></div>
        <div className="index-grid">
          {board.market.indices.map((i) => (
            <div className="card" key={i.name}>
              <div className="idx-name">{i.name}</div>
              <div className={`idx-val ${i.chg >= 0 ? "up" : "down"}`}>{i.val ? i.val.toFixed(2) : "—"}</div>
              <div className={`idx-chg ${i.chg >= 0 ? "up" : "down"}`}>{sign(i.chg)}%</div>
              <div className="idx-sub">{i.amt}</div>
            </div>
          ))}
        </div>
        <div className="mkt-rating">
          <span className="label">大盘短线环境</span>
          <span className={`verdict ${dirCls(board.market.rating)}`}>{board.market.rating}</span>
          <span className="reason">{board.market.reason}</span>
        </div>
      </section>

      {selStock && (
        <section className="section">
          <div className="section-title"><span className="bar"></span>K 线图<span className="sub">日/周/月 + 成交量，指标固定日线</span>
            <span style={{ marginLeft: "auto", display: "flex", gap: 6 }}>
              {(["day", "week", "month"] as Period[]).map((p) => (
                <button key={p} className={`btn${period === p ? " primary" : ""}`} style={{ padding: "3px 12px" }}
                  onClick={() => { setPeriod(p); load(watch, true, p); }}>{PERIOD_NAME[p]}</button>
              ))}
            </span>
          </div>
          <div className="card"><KLineChart kline={selStock.kline} name={`${selStock.name}（${selStock.code}）`} period={period} /></div>
        </section>
      )}

      <section className="section">
        <div className="section-title"><span className="bar"></span>标的组合全览<span className="sub">自选 ETF / 个股</span></div>
        <div className="tbl-wrap">
          <table>
            <thead><tr><th>标的</th><th>最新价</th><th>涨跌幅</th><th>成交额</th><th>换手率</th><th>午后</th><th>短线方向</th><th>操作</th></tr></thead>
            <tbody>
              {board.portfolio.map((d) => (
                <tr key={d.code} style={{ cursor: "pointer" }} onClick={() => setSel(d.code)}>
                  <td><b>{d.name}</b> <span style={{ color: "var(--faint)" }}>{d.code}</span></td>
                  <td className={d.changePct >= 0 ? "up" : "down"}>{d.price.toFixed(3)}</td>
                  <td className={d.changePct >= 0 ? "up" : "down"}>{sign(d.changePct)}%</td>
                  <td>{(d.amount / 1e8).toFixed(2)}亿</td>
                  <td>{d.turnover ? d.turnover.toFixed(2) + "%" : "—"}</td>
                  <td className={`dir-${dirCls(d.afternoon)}`}>{d.afternoon}</td>
                  <td className={`dir-${dirCls(d.verdict)}`}>{d.verdict}</td>
                  <td dangerouslySetInnerHTML={{ __html: opTag(d.verdict) }} />
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="section">
        <div className="section-title"><span className="bar"></span>逐一深度分析<span className="sub">今日数据 / 技术指标 / 多周期 / 支撑压力 / 情景概率 / 条件式操作</span></div>
        <div className="stock-grid">
          {board.portfolio.map((d) => (
            <div className="stock-card" key={d.code}>
              <div className="sc-head">
                <div><div className="name">{d.name}</div><div className="code">{d.code}</div></div>
                <div className="px"><div className={`p ${d.changePct >= 0 ? "up" : "down"}`}>{d.price.toFixed(3)}</div><div className={`c ${d.changePct >= 0 ? "up" : "down"}`}>{sign(d.changePct)}%</div></div>
              </div>
              <div className="kv">
                <div><div className="k">成交量</div><div className="v">{(d.volume / 1e4).toFixed(1)}万手</div></div>
                <div><div className="k">换手率</div><div className="v">{d.turnover ? d.turnover.toFixed(2) + "%" : "—"}</div></div>
                <div><div className="k">成交额</div><div className="v">{(d.amount / 1e8).toFixed(2)}亿</div></div>
                <div><div className="k">量比</div><div className="v">{d.volRatio ? d.volRatio.toFixed(2) : "—"}</div></div>
              </div>
              <div className="block"><div className="bt">午后方向（分钟线）</div>
                <div className="tf"><span className={`t dir-${dirCls(d.afternoon)}`}>{d.afternoon}</span></div></div>
              <div className="block"><div className="bt">多空量能（外盘 / 内盘）</div>
                <div className="tf">
                  <span className="t">外盘 <b className="up">{d.outerVol ? (d.outerVol / 1e4).toFixed(0) + "万手" : "—"}</b></span>
                  <span className="t">内盘 <b className="down">{d.innerVol ? (d.innerVol / 1e4).toFixed(0) + "万手" : "—"}</b></span>
                  <span className="t">主动买占比 <b className={d.powerPct >= 55 ? "up" : d.powerPct <= 45 ? "down" : ""}>{d.powerPct}%</b></span>
                  <span className="t">量能 <b className={d.power === "买方主导" ? "up" : d.power === "卖方主导" ? "down" : ""}>{d.power}</b></span>
                </div></div>
              <div className="block"><div className="bt">技术指标（MA / MACD / RSI）</div>
                <div className="tf">
                  <span className="t">MA5 <b>{d.ind.ma5.toFixed(3)}</b></span>
                  <span className="t">MA20 <b>{d.ind.ma20.toFixed(3)}</b></span>
                  <span className="t">MACD <b className={d.ind.dif > d.ind.dea ? "up" : "down"}>{d.ind.dif > d.ind.dea ? "金叉" : "死叉"}</b></span>
                  <span className="t">RSI6 <b>{d.ind.rsi6.toFixed(0)}</b></span>
                </div></div>
              <div className="block"><div className="bt">多时间维度趋势（方向 / 幅度 / 置信度）</div>
                <div className="tf">
                  <span className="t">明日 <b className={dirCls(d.tf.next[0])}>{d.tf.next[0]}</b> {d.tf.next[1]} · {d.tf.next[2]}</span>
                  <span className="t">下周 <b className={dirCls(d.tf.week[0])}>{d.tf.week[0]}</b> {d.tf.week[1]} · {d.tf.week[2]}</span>
                  <span className="t">下月 <b className={dirCls(d.tf.month[0])}>{d.tf.month[0]}</b> {d.tf.month[1]} · {d.tf.month[2]}</span>
                </div></div>
              <div className="block"><div className="bt">支撑 / 压力（近20日）</div>
                <div className="sp"><span>支撑 <b className="down">{d.support.toFixed(3)}</b></span><span>压力 <b className="up">{d.resistance.toFixed(3)}</b></span>
                  <span style={{ marginLeft: "auto", color: "var(--muted)" }}>综合 <b className={dirCls(d.verdict)}>{d.verdict}</b> · 评分 {d.score}</span></div></div>
              <div className="block"><div className="bt">情景概率（多 / 空 / 震荡）</div>
                <div className="prob"><span className="pu" style={{ width: d.prob[0] + "%" }}></span><span className="pd" style={{ width: d.prob[1] + "%" }}></span><span className="pf" style={{ width: d.prob[2] + "%" }}></span></div>
                <div className="prob-legend"><span className="up">多 {d.prob[0]}%</span><span className="down">空 {d.prob[1]}%</span><span>震荡 {d.prob[2]}%</span></div></div>
              <div className="action">{d.action}</div>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}
