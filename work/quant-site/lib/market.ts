// 真实行情数据层：腾讯财经（qt.gtimg 实时报价 + ifzq 前复权日K + m5 分钟线）+ 指标 + 规则化五维综合
// 报价 GBK；报价批量一次拉取。网络失败抛错，由 API 层降级模拟数据。

const TX_QUOTE = "https://qt.gtimg.cn/q=";
const TX_KLINE = "https://web.ifzq.gtimg.cn/appstock/app/fqkline/get";
const TX_MIN = "https://web.ifzq.gtimg.cn/appstock/app/minute/query";

export type Kline = { date: string; open: number; close: number; high: number; low: number; volume: number; pct: number };
export type Period = "day" | "week" | "month";
export const PERIOD_NAME: Record<Period, string> = { day: "日K", week: "周K", month: "月K" };
export type Indicators = { ma5: number; ma10: number; ma20: number; dif: number; dea: number; rsi6: number; hi20: number; lo20: number };
export type Decision = {
  code: string; name: string; price: number; change: number; changePct: number; open: number; high: number; low: number; prevClose: number;
  volume: number; amount: number; turnover: number; updated: string;
  volRatio: number; outerVol: number; innerVol: number; power: string; powerPct: number;
  ind: Indicators; verdict: "偏多" | "中性" | "偏空"; score: number;
  prob: [number, number, number]; support: number; resistance: number;
  tf: { next: [string, string, string]; week: [string, string, string]; month: [string, string, string] };
  action: string; afternoon: string; kline: Kline[];
};
export type Board = {
  live: boolean; updated: string; source: string; period: Period;
  market: { rating: string; reason: string; indices: { name: string; val: number; chg: number; amt: string }[] };
  portfolio: Decision[];
};

function txCode(code: string): string {
  if (code.startsWith("sh") || code.startsWith("sz")) return code;
  return /^(5|6|9)/.test(code) ? "sh" + code : "sz" + code;
}

async function getText(url: string, timeout = 8000): Promise<string> {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), timeout);
  try {
    const r = await fetch(url, { signal: ctrl.signal, headers: { "User-Agent": "Mozilla/5.0", "Referer": "https://gu.qq.com/" } });
    if (!r.ok) throw new Error("HTTP " + r.status);
    return new TextDecoder("gbk").decode(await r.arrayBuffer());
  } finally { clearTimeout(t); }
}
async function getJSON(url: string, timeout = 8000): Promise<any> {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), timeout);
  try {
    const r = await fetch(url, { signal: ctrl.signal, headers: { "User-Agent": "Mozilla/5.0", "Referer": "https://gu.qq.com/" } });
    if (!r.ok) throw new Error("HTTP " + r.status);
    return await r.json();
  } finally { clearTimeout(t); }
}

async function fetchQuotes(codes: string[]): Promise<Record<string, any>> {
  const txt = await getText(TX_QUOTE + codes.map(txCode).join(","));
  const out: Record<string, any> = {};
  const re = /v_([a-z0-9]+)="([^"]*)"/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(txt))) {
    const f = m[2].split("~");
    if (f.length < 38) continue;
    out[m[1]] = {
      code: f[2], name: f[1], price: +f[3], prevClose: +f[4], open: +f[5],
      volume: +f[6], change: +f[31], changePct: +f[32], high: +f[33], low: +f[34],
      amount: (+f[37] || 0) * 1e4, turnover: +f[38] || 0, updated: f[30] || "",
      outerVol: +f[7] || 0,   // 外盘：主动买入量（手）
      innerVol: +f[8] || 0,   // 内盘：主动卖出量（手）
      volRatio: +f[49] || 0,  // 量比：当日每分钟均量 / 过去5日每分钟均量
    };
  }
  return out;
}

export async function fetchKline(code: string, limit = 90, period: Period = "day"): Promise<Kline[]> {
  const tc = txCode(code);
  const j = await getJSON(`${TX_KLINE}?param=${tc},${period},,,${limit},qfq`);
  const arr: string[][] = j?.data?.[tc]?.[`qfq${period}`] || j?.data?.[tc]?.[period] || [];
  const out = arr.map((r) => ({ date: r[0], open: +r[1], close: +r[2], high: +r[3], low: +r[4], volume: +r[5], pct: 0 }));
  for (let i = 0; i < out.length; i++) { const p = out[i - 1]?.close; out[i].pct = p ? (out[i].close - p) / p * 100 : 0; }
  return out;
}

// 今日分钟线 → 午后(13:00-15:00)方向（周末/休市取最近交易日）
async function fetchAfternoon(code: string): Promise<string> {
  try {
    const tc = txCode(code);
    const j = await getJSON(`${TX_MIN}?code=${tc}`);
    const rows: string[] = j?.data?.[tc]?.data?.data || [];
    if (rows.length < 5) return "—";
    const pm = rows.map((r) => r.split(" ")).filter((p) => p[0] >= "1300" && p[0] <= "1500" && p[1]);
    if (pm.length < 2) return "—";
    const px = pm.map((p) => +p[1]);
    const first = px[0], last = px[px.length - 1];
    const chg = ((last - first) / first) * 100;
    const hi = Math.max(...px), lo = Math.min(...px);
    const pos = hi > lo ? (last - lo) / (hi - lo) : 0.5;
    if (chg > 0.3 && pos > 0.6) return "上攻";
    if (chg > 0.3) return "探底回升";
    if (chg < -0.3 && pos < 0.4) return "冲高回落";
    return "震荡";
  } catch { return "—"; }
}

export function computeIndicators(k: Kline[]): Indicators {
  const close = k.map((x) => x.close);
  const ma = (n: number) => (close.length >= n ? close.slice(-n).reduce((a, b) => a + b, 0) / n : close[close.length - 1] || 0);
  const difSeries: number[] = []; let e12 = close[0] || 0, e26 = close[0] || 0;
  for (let i = 0; i < close.length; i++) {
    e12 = i === 0 ? close[0] : close[i] / 13 + e12 * 12 / 13;
    e26 = i === 0 ? close[0] : close[i] / 27 + e26 * 26 / 27;
    difSeries.push(e12 - e26);
  }
  const dif = difSeries[difSeries.length - 1] || 0;
  let dea = difSeries[0] || 0; const a = 1 / 10;
  for (let i = 1; i < difSeries.length; i++) dea = difSeries[i] * a + dea * (1 - a);
  const rsi = (n: number) => {
    if (close.length < n + 1) return 50;
    let up = 0, dn = 0;
    for (let i = close.length - n; i < close.length; i++) { const d = close[i] - close[i - 1]; d >= 0 ? (up += d) : (dn -= d); }
    return up + dn === 0 ? 50 : (up / (up + dn)) * 100;
  };
  const hi20 = k.length ? Math.max(...k.slice(-20).map((x) => x.high)) : 0;
  const lo20 = k.length ? Math.min(...k.slice(-20).map((x) => x.low)) : 0;
  return { ma5: ma(5), ma10: ma(10), ma20: ma(20), dif, dea, rsi6: rsi(6), hi20, lo20 };
}

export function synthesize(code: string, q: any, ind: Indicators, k: Kline[], kline: Kline[], afternoon: string): Decision {
  let score = 0;
  const c = q.price;
  if (c > ind.ma5) score += 0.6; else score -= 0.6;
  if (c > ind.ma20) score += 0.8; else score -= 0.8;
  if (ind.dif > ind.dea) score += 1; else score -= 1;
  if (ind.rsi6 > 70) score -= 0.6; else if (ind.rsi6 < 30) score += 0.6;
  const mom = k.length >= 6 ? (c - k[k.length - 6].close) / k[k.length - 6].close * 100 : 0;
  if (mom > 2) score += 0.6; else if (mom < -2) score -= 0.6;
  if (q.changePct > 0) score += 0.3; else score -= 0.3;
  // 午后动能（分钟线）：上攻/探底回升为正，冲高回落为负
  if (afternoon === "上攻") score += 0.6;
  else if (afternoon === "探底回升") score += 0.4;
  else if (afternoon === "冲高回落") score -= 0.6;
  // 换手确认：活跃放量顺势加成，明显缩量降权（turnover 缺失则不加，避免 ETF 系统性偏差）
  const tn = q.turnover || 0;
  if (tn >= 3) score += 0.3;
  else if (tn > 0 && tn < 1) score -= 0.2;

  // 多空量能：外盘(主动买) vs 内盘(主动卖) 占比
  const outV = q.outerVol || 0, inV = q.innerVol || 0;
  const tot = outV + inV;
  const powerPct = tot > 0 ? +(outV / tot * 100).toFixed(1) : 50;
  const power = tot === 0 ? "—" : powerPct >= 55 ? "买方主导" : powerPct <= 45 ? "卖方主导" : "多空均衡";
  if (tot > 0) { if (powerPct >= 55) score += 0.4; else if (powerPct <= 45) score -= 0.4; }
  // 量比确认：放量顺势加成，明显缩量降权
  const vr = q.volRatio || 0;
  if (vr >= 1.5) score += 0.3;
  else if (vr > 0 && vr < 0.7) score -= 0.3;
  score = Math.max(-3, Math.min(3, score));

  const verdict: Decision["verdict"] = score >= 1 ? "偏多" : score <= -1 ? "偏空" : "中性";
  const mag = Math.min(3, Math.abs(score));
  const conf = mag >= 2 ? "中高" : mag >= 1 ? "中" : "低";
  const pu = Math.round(50 + score * 14);
  const prob: [number, number, number] = [pu, Math.round((100 - pu) * 0.45), 100 - pu - Math.round((100 - pu) * 0.45)];

  const support = +ind.lo20.toFixed(3);
  const resistance = +ind.hi20.toFixed(3);
  const trend = (s: number): [string, string, string] => {
    const dir = s >= 0.6 ? "偏多" : s <= -0.6 ? "偏空" : "中性";
    const amp = s >= 0.6 ? `+${(1 + mag).toFixed(1)}~${(2.5 + mag).toFixed(1)}%` : s <= -0.6 ? `-${(1 + mag).toFixed(1)}~-${(2.5 + mag).toFixed(1)}%` : "-1~+1.5%";
    return [dir, amp, conf];
  };
  const tf = { next: trend(score), week: trend(score * 0.8), month: trend(score * 0.6) };

  const volTxt = `${tot > 0 ? `量能${power}（主动买占比 ${powerPct}%）` : "量能数据暂缺"}，${vr > 0 ? `量比 ${vr.toFixed(2)}` : "量比暂缺"}；据此判断多空主导方与量能是否配合。`;

  const action =
    verdict === "偏多"
      ? `技术面偏多（价格 ${c > ind.ma20 ? "站上" : "未站上"}20 日线、MACD ${ind.dif > ind.dea ? "金叉" : "待金叉"}、RSI6 ${ind.rsi6.toFixed(0)}）。若回踩 ${support} 缩量不破可低吸；放量跌破支撑则止损；上方 ${resistance} 附近注意兑现。`
      : verdict === "偏空"
      ? `技术面偏空（价格 ${c > ind.ma20 ? "仍在" : "跌破"}20 日线、MACD ${ind.dif > ind.dea ? "仍金叉" : "死叉"}、RSI6 ${ind.rsi6.toFixed(0)}）。宜观望或逢高减仓；反抽 ${resistance} 无量继续降仓；跌至 ${support} 再看能否企稳。`
      : `技术面中性（多空分歧、RSI6 ${ind.rsi6.toFixed(0)}）。区间 ${support}~${resistance} 内观望；放量突破 ${resistance} 顺势跟进，跌破 ${support} 减仓，中间价位不追。`;

  return {
    code: q.code || code, name: q.name || code, price: q.price, change: q.change, changePct: q.changePct,
    open: q.open, high: q.high, low: q.low, prevClose: q.prevClose, volume: q.volume, amount: q.amount, turnover: q.turnover, updated: q.updated,
    volRatio: +vr.toFixed(2), outerVol: outV, innerVol: inV, power, powerPct,
    ind, verdict, score: +score.toFixed(2), prob, support, resistance, tf, action: action + volTxt, afternoon, kline,
  };
}

const WATCH = ["510300", "510500", "515030", "512000", "588000"];
const INDICES = [
  { code: "sh000001", name: "上证指数" }, { code: "sz399001", name: "深证成指" },
  { code: "sh000300", name: "沪深300" }, { code: "sz399006", name: "创业板指" },
];

export async function getBoard(codes?: string[], period: Period = "day"): Promise<Board> {
  const watch = (codes && codes.length ? codes : WATCH).slice(0, 20);
  const idxCodes = INDICES.map((i) => i.code);
  const quotes = await fetchQuotes([...idxCodes, ...watch]);
  if (!Object.keys(quotes).length) throw new Error("empty quotes");

  const indices = INDICES.map((i) => {
    const q = quotes[txCode(i.code)];
    return { name: i.name, val: q ? q.price : 0, chg: q ? q.changePct : 0, amt: q ? `成交额 ${(q.amount / 1e8).toFixed(0)} 亿` : "—" };
  });
  const ups = indices.filter((i) => i.chg > 0).length;
  const avg = indices.reduce((a, b) => a + b.chg, 0) / (indices.length || 1);
  const rating = avg > 0.3 && ups >= 3 ? "偏多" : avg < -0.3 && ups <= 1 ? "偏空" : "中性";
  const reason = `${indices.length} 大指数均涨 ${avg.toFixed(2)}%、${ups} 涨 ${indices.length - ups} 跌，短线环境${rating}。`;

  const portfolio = await Promise.all(
    watch.map(async (code) => {
      const q = quotes[txCode(code)];
      if (!q) throw new Error("no quote " + code);
      const k = await fetchKline(code, 90, "day"); // 指标固定用日线，不受图表周期影响
      if (!k.length) throw new Error("no kline " + code);
      const afternoon = await fetchAfternoon(code);
      const chartK = period === "day" ? k.slice(-60) : await fetchKline(code, 60, period);
      return synthesize(code, q, computeIndicators(k), k, chartK.length ? chartK : k.slice(-60), afternoon);
    })
  );

  return { live: true, updated: new Date().toLocaleString("zh-CN", { hour12: false }), source: "腾讯财经(公开接口)", period, market: { rating, reason, indices }, portfolio };
}
