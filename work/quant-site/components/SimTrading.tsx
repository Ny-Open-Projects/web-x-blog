"use client";
import { useEffect, useState } from "react";
import type { Board } from "@/lib/market";
import { getWatch } from "@/lib/watch";

type Pos = { qty: number; cost: number };
type Sim = { cash: number; positions: Record<string, Pos> };
const KEY = "quantsite-sim-v1";
const INIT: Sim = { cash: 1000000, positions: {} };

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
    fetch("/api/board?codes=" + getWatch().join(",")).then((r) => r.json()).then(setBoard).catch(() => {});
    const t = setInterval(() => fetch("/api/board?codes=" + getWatch().join(",")).then((r) => r.json()).then(setBoard).catch(() => {}), 30000);
    return () => clearInterval(t);
  }, []);
  useEffect(() => { localStorage.setItem(KEY, JSON.stringify(sim)); }, [sim]);

  const priceOf = (c: string) => board?.portfolio.find((d) => d.code === c)?.price ?? 0;
  const nameOf = (c: string) => board?.portfolio.find((d) => d.code === c)?.name ?? c;
  const codes = board?.portfolio.map((d) => d.code) ?? ["510300", "510500", "515030", "512000", "588000"];

  const posValue = Object.entries(sim.positions).reduce((s, [c, p]) => s + p.qty * priceOf(c), 0);
  const posCost = Object.entries(sim.positions).reduce((s, [, p]) => s + p.qty * p.cost, 0);
  const total = sim.cash + posValue;
  const pnl = total - INIT.cash;

  const trade = (side: "buy" | "sell") => {
    const px = priceOf(code); const q = Math.floor(qty);
    if (!px) return setMsg("暂无行情价，无法交易");
    if (q <= 0) return setMsg("数量需为正整数");
    if (side === "buy") {
      const cost = px * q;
      if (cost > sim.cash) return setMsg(`现金不足：需 ¥${cost.toFixed(0)}，可用 ¥${sim.cash.toFixed(0)}`);
      const old = sim.positions[code] || { qty: 0, cost: 0 };
      const nq = old.qty + q; const nc = (old.qty * old.cost + cost) / nq;
      setSim({ cash: sim.cash - cost, positions: { ...sim.positions, [code]: { qty: nq, cost: nc } } });
      setMsg(`买入 ${nameOf(code)} ${q} 手 @ ${px.toFixed(3)}，花费 ¥${cost.toFixed(0)}`);
    } else {
      const old = sim.positions[code];
      if (!old || old.qty < q) return setMsg(`持仓不足：当前 ${old?.qty ?? 0} 手`);
      const gain = px * q;
      const nq = old.qty - q;
      const positions = { ...sim.positions };
      if (nq === 0) delete positions[code]; else positions[code] = { qty: nq, cost: old.cost };
      setSim({ cash: sim.cash + gain, positions });
      setMsg(`卖出 ${nameOf(code)} ${q} 手 @ ${px.toFixed(3)}，回笼 ¥${gain.toFixed(0)}（盈亏 ¥${(gain - q * old.cost).toFixed(0)}）`);
    }
  };

  const reset = () => { if (confirm("确认重置模拟盘？将清空持仓与记录。")) { setSim(INIT); setMsg("已重置"); } };

  return (
    <div>
      <div className="index-grid" style={{ marginBottom: 16 }}>
        <div className="card"><div className="idx-name">总资产</div><div className="idx-val">¥{total.toFixed(0)}</div><div className="idx-sub">初始 ¥1,000,000</div></div>
        <div className="card"><div className="idx-name">可用现金</div><div className="idx-val">¥{sim.cash.toFixed(0)}</div><div className="idx-sub">用于买入</div></div>
        <div className="card"><div className="idx-name">持仓市值</div><div className="idx-val">¥{posValue.toFixed(0)}</div><div className="idx-sub">成本 ¥{posCost.toFixed(0)}</div></div>
        <div className="card"><div className="idx-name">总盈亏</div><div className={`idx-val ${pnl >= 0 ? "up" : "down"}`}>{pnl >= 0 ? "+" : ""}¥{pnl.toFixed(0)}</div><div className="idx-sub">{((pnl / INIT.cash) * 100).toFixed(2)}%</div></div>
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
      </div>

      <div className="tbl-wrap">
        <table>
          <thead><tr><th>标的</th><th>持仓(手)</th><th>成本价</th><th>现价</th><th>市值</th><th>盈亏</th><th>盈亏%</th></tr></thead>
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
    </div>
  );
}
