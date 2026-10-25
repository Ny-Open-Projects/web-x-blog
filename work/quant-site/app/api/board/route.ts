import { NextResponse } from "next/server";
import { getBoard, type Board, type Decision, type Period } from "@/lib/market";

export const dynamic = "force-dynamic";
export const revalidate = 60;

function mockDecision(code: string, name: string, price: number, changePct: number, score: number): Decision {
  const verdict = score >= 1 ? "偏多" : score <= -1 ? "偏空" : "中性";
  const ind = { ma5: price * 0.99, ma10: price * 0.98, ma20: price * 0.97, dif: 0.02, dea: 0.01, rsi6: 55, hi20: price * 1.03, lo20: price * 0.96 };
  const pu = Math.round(50 + score * 14);
  return {
    code, name, price, change: +(price * changePct / 100).toFixed(3), changePct,
    open: price * 0.999, high: price * 1.01, low: price * 0.99, prevClose: +(price / (1 + changePct / 100)).toFixed(3),
    volume: 100000, amount: 1.2e8, turnover: 0.8, updated: "模拟",
    volRatio: 1, outerVol: 52000, innerVol: 48000, power: "多空均衡", powerPct: 52,
    ind, verdict, score, prob: [pu, Math.round((100 - pu) * 0.45), 100 - pu - Math.round((100 - pu) * 0.45)],
    support: +(price * 0.96).toFixed(3), resistance: +(price * 1.03).toFixed(3),
    tf: { next: [verdict, "+0.6~1.5%", "中"], week: [verdict, "+1.5~3%", "中"], month: [verdict, "+3~6%", "中"] },
    action: verdict === "偏多" ? `模拟：回踩 ${(price * 0.96).toFixed(3)} 不破可低吸，跌破止损，上方 ${(price * 1.03).toFixed(3)} 兑现。` : verdict === "偏空" ? `模拟：宜观望/减仓，反抽 ${(price * 1.03).toFixed(3)} 无量降仓。` : `模拟：区间观望，突破/跌破关键位再动作。`,
    afternoon: "—", kline: [],
  };
}

function mockBoard(): Board {
  return {
    live: false, updated: new Date().toLocaleString("zh-CN", { hour12: false }), source: "模拟数据（行情接口暂不可用）", period: "day",
    market: {
      rating: "中性", reason: "模拟：主要指数窄幅整理，短线环境中性。",
      indices: [
        { name: "上证指数", val: 3228.46, chg: 0.42, amt: "成交额 3821 亿" },
        { name: "深证成指", val: 10412.73, chg: 0.31, amt: "成交额 4689 亿" },
        { name: "沪深300", val: 3876.33, chg: 0.31, amt: "成交额 4689 亿" },
        { name: "创业板指", val: 2154.08, chg: -0.27, amt: "成交额 1975 亿" },
      ],
    },
    portfolio: [
      mockDecision("510300", "沪深300ETF", 3.942, 0.86, 1.4),
      mockDecision("510500", "中证500ETF", 6.105, 0.23, 0.2),
      mockDecision("515030", "新能源车ETF", 2.138, 1.94, 1.8),
      mockDecision("512000", "证券ETF", 0.968, -0.82, -1.2),
      mockDecision("588000", "科创50ETF", 1.024, 1.18, 1.1),
    ],
  };
}

export async function GET(req: Request) {
  const sp = new URL(req.url).searchParams;
  const codes = sp.get("codes")?.split(",").map((s) => s.trim()).filter(Boolean);
  const p = sp.get("period");
  const period: Period = p === "week" || p === "month" ? p : "day";
  try {
    const board = await getBoard(codes && codes.length ? codes : undefined, period);
    return NextResponse.json(board);
  } catch (e) {
    return NextResponse.json({ ...mockBoard(), live: false, period });
  }
}
