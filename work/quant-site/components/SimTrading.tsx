"use client";
import { useEffect, useState } from "react";
import type { Board } from "@/lib/market";
import { getWatch } from "@/lib/watch";

type Pos = { qty: number; cost: number };
type Trade = { t: string; side: "买入" | "卖出"; code: string; name: string; qty: number; price: number; amount: number; fee: number; pnl?: number };
type Sim = { cash: number; positions: Record<string, Pos>; trades: Trade[] };
const KEY = "quantsite-sim-v2";
const INIT: Sim = { cash: 1000000, positions: {}, trades: [] };
// 费率：ETF 交易免印花税，仅佣金万三、单笔最低 5 元（模拟用，与实际券商费率可能有差异）
const COMMISSION = 0.0003;
const MIN_FEE = 5;
const feeOf = (amount: number) => Math.max(amount * COMMISSION, MIN_FEE);

function load(): Sim {
  if (typeof window === "undefined") return INIT;
  try { const s = localStorage.getItem(KEY); return s ? { ...INIT, ...JSON.parse(s) } : INIT; } catch { return INIT; }
}

export default function SimTrading() {
  const [sim, setSim] = useState<Sim>(INIT);
  const [board, setBoard] = useState<Board | null>(null);
  const [code, setCode] = useState("510300");
  const [qty, setQty] = useState(100);
  const [msg, setMsg] = useState("");

  useEffect(() => { setSim(load()); }, []);
  useEffect(() => {
    const pull = () => fetch("/api/board?codes=" + getWatch().join(",")).then((r) => r.json()).then(setBoard).catch(() => {});
    pull();
    const t = setInterval(pull, 30000);
    return () => clearInterval(t);
  }, []);
  useEffect(() => { if (sim !== INIT) localStorage.setItem(KEY, JSON.stringify(sim)); }, [sim]);

  const priceOf = (c: string) => board?.portfolio.find((d) => d.code === c)?.price ?? 0;
  const nameOf = (c: string) => board?.portfolio.find((d) => d.code === c)?.name ?? c;
  const codes = board?.portfolio.map((d) => d.code) ?? ["510300", "510500", "515030", "512000", "588000"];

  const posValue = Object.entries(sim.positions).reduce((s, [c, p]) => s + p.qty * priceOf(c), 0);
  const posCost = Object.entries(sim.positions).reduce((s, [, p]) => s + p.qty * p.cost, 0);
  const total = sim.cash + posValue;
  const pnl = total - INIT.cash;
  const totalFee = sim.trades.reduce((s, t) => s + t.fee, 0);
  const realized = sim.trades.reduce((s, t) => s + (t.pnl || 0), 0);

  const trade = (side: "buy" | "sell") => {
    const px = priceOf(code); const q = Math.floor(qty);
    if (!px) return setMsg("暂无行情价，无法交易");
    if (q <= 0) return setMsg("数量需为正整数");
    const gross = px * q;
    const fee = feeOf(gross);
    const now = new Date().toLocaleString("zh-CN", { hour12: false });

    if (side === "buy") {
      const cost = gross + fee;
      if (cost > sim.cash) return setMsg(`现金不足：需 ¥${cost.toFixed(0)}（含手续费 ¥${fee.toFixed(2)}），可用 ¥${sim.cash.toFixed(0)}`);
      const old = sim.positions[code] || { qty: 0, cost: 0 };
      const nq = old.qty + q; const nc = (old.qty * old.cost + cost) / nq;
      setSim({ cash: sim.cash - cost, positions: { ...sim.positions, [code]: { qty: nq, cost: nc } }, trades: [{ t: now, side: "买入" as const, code, name: nameOf(code), qty: q, price: px, amount: cost, fee }, ...sim.trades].slice(0, 100) });
      setMsg(`买入 ${nameOf(code)} ${q} 手 @ ${px.toFixed(3)}，花费 ¥${cost.toFixed(0)}（含费 ¥${fee.toFixed(2)}）`);
    } else {
      const old = sim.positions[code];
      if (!old || old.qty < q) return setMsg(`持仓不足：当前 ${old?.qty ?? 0} 手`);
      const gain = gross - fee;
      const realizedPnl = (px - old.cost) * q - fee;
      const nq = old.qty - q;
      const positions = { ...sim.positions };
      if (nq === 0) delete positions[code]; else positions[code] = { qty: nq, cost: old.cost };
      setSim({ cash: sim.cash + gain, positions, trades: [{ t: now, side: "卖出" as const, code, name: nameOf(code), qty: q, price: px, amount: gain, fee, pnl: realizedPnl }, ...sim.trades].slice(0, 100) });
      setMsg(`卖出 ${nameOf(code)} ${q} 手 @ ${px.toFixed(3)}，回笼 ¥${gain.toFixed(0)}（已实现盈亏 ¥${realizedPnl.toFixed(0)}）`);
    }
  };

  const reset = () => { if (confirm("确认重置模拟盘？将清空持仓与交易记录。")) { setSim(INIT); setMsg("已重置"); } };

  return (
    <div>
      <div className="index-grid" style={{ marginBottom: 16 }}>
        <div className="card"><div className="idx-name">总资产</div><div className="idx-val">¥{total.toFixed(0)}</div><div className="idx-sub">初始 ¥1,000,000</div></div>
        <div className="card"><div className="idx-name">可用现金</div><div className="idx-val">¥{sim.cash.toFixed(0)}</div><div className="idx-sub">用于买入</div></div>
        <div className="card"><div className="idx-name">持仓市值</div><div className="idx-val">¥{posValue.toFixed(0)}</div><div className="idx-sub">成本 ¥{posCost.toFixed(0)}</div></div>
        <div className="card"><div className="idx-name">总盈亏</div><div className={`idx-val ${pnl >= 0 ? "up" : "down"}`}>{pnl >= 0 ? "+" : ""}¥{pnl.toFixed(0)}</div><div className="idx-sub">{((pnl / INIT.cash) * 100).toFixed(2)}%（已实现 ¥{realized.toFixed(0)}）</div></div>
      </div>

      <div className="card" style={{ marginBottom: 16 }}>
        <div style={{ display: "flex", gap: 12, alignItems: "end", flexWrap: "wrap" }}>
          <label style={{ fontSize: 13, color: "var(--muted)" }}>标的
            <select className="btn" style={{ marginLeft: 8 }} value={code} onChange={(e) => setCode(e.target.value)}>
              {codes.map((c) => <option key={c} value={c}>{nameOf(c)}（{c}）{priceOf(c) ? ` ¥${priceOf(c).toFixed(3)}` : ""}</option>)}
            </select>
          </label>
          <label style={{ fontSize: 13, color: "var(--muted)" }}>数量（手）
            <input className="btn" style={{ marginLeft: 8, width: 100 }} type="number" min={1} value={qty} onChange={(e) => setQty(+e.target.value)} />
          </label>
          <button className="btn primary" onClick={() => trade("buy")}>买入</button>
          <button className="btn danger" onClick={() => trade("sell")}>卖出</button>
          <button className="btn" style={{ marginLeft: "auto" }} onClick={reset}>重置</button>
        </div>
        {msg && <div style={{ marginTop: 10, fontSize: 13, color: "var(--accent)" }}>{msg}</div>}
        <div style={{ marginTop: 8, fontSize: 12, color: "var(--faint)" }}>费率：ETF 免印花税，佣金万三、单笔最低 ¥5（买卖双向），手续费计入持仓成本 / 卖出回笼，用于贴近真实交易摩擦。</div>
      </div>

      <div className="tbl-wrap" style={{ marginBottom: 16 }}>
        <table>
          <thead><tr><th>标的</th><th>持仓(手)</th><th>成本价</th><th>现价</th><th>市值</th><th>浮动盈亏</th><th>盈亏%</th></tr></thead>
          <tbody>
            {Object.keys(sim.positions).length === 0 ? (
              <tr><td colSpan={7} style={{ textAlign: "center", color: "var(--faint)", padding: 24 }}>暂无持仓，从上方买入开始模拟</td></tr>
            ) : (
              Object.entries(sim.positions).map(([c, p]) => {
                const px = priceOf(c); const mv = p.qty * px; const pl = (px - p.cost) * p.qty; const plp = p.cost ? (px - p.cost) / p.cost * 100 : 0;
                return (
                  <tr key={c}>
                    <td><b>{nameOf(c)}</b> <span style={{ color: "var(--faint)" }}>{c}</span></td>
                    <td>{p.qty}</td><td>{p.cost.toFixed(3)}</td>
                    <td className={px >= p.cost ? "up" : "down"}>{px.toFixed(3)}</td>
                    <td>¥{mv.toFixed(0)}</td>
                    <td className={pl >= 0 ? "up" : "down"}>{pl >= 0 ? "+" : ""}¥{pl.toFixed(0)}</td>
                    <td className={plp >= 0 ? "up" : "down"}>{plp >= 0 ? "+" : ""}{plp.toFixed(2)}%</td>
                  </tr>
                );
              })
            )}
          </tbody>
        </table>
      </div>

      <div className="section-title" style={{ margin: "18px 0 8px" }}><span className="bar"></span>交易流水<span className="sub">最近 {sim.trades.length} 笔 · 累计手续费 ¥{totalFee.toFixed(2)}</span></div>
      <div className="tbl-wrap">
        <table>
          <thead><tr><th>时间</th><th>方向</th><th>标的</th><th>数量(手)</th><th>成交价</th><th>金额</th><th>手续费</th><th>已实现盈亏</th></tr></thead>
          <tbody>
            {sim.trades.length === 0 ? (
              <tr><td colSpan={8} style={{ textAlign: "center", color: "var(--faint)", padding: 24 }}>暂无成交记录</td></tr>
            ) : (
              sim.trades.map((t, i) => (
                <tr key={i}>
                  <td style={{ color: "var(--faint)" }}>{t.t}</td>
                  <td><b className={t.side === "买入" ? "up" : "down"}>{t.side}</b></td>
                  <td>{t.name} <span style={{ color: "var(--faint)" }}>{t.code}</span></td>
                  <td>{t.qty}</td><td>{t.price.toFixed(3)}</td>
                  <td>¥{t.amount.toFixed(0)}</td>
                  <td style={{ color: "var(--faint)" }}>¥{t.fee.toFixed(2)}</td>
                  <td className={t.pnl == null ? "" : t.pnl >= 0 ? "up" : "down"}>{t.pnl == null ? "—" : `${t.pnl >= 0 ? "+" : ""}¥${t.pnl.toFixed(0)}`}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
