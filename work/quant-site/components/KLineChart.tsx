"use client";
import ReactECharts from "echarts-for-react";
import type { Kline } from "@/lib/market";
import { PERIOD_NAME, type Period } from "@/lib/market";

const UP = "#f04a4a", DOWN = "#1fb786"; // A股：涨红跌绿

export default function KLineChart({ kline, name, period = "day" }: { kline: Kline[]; name: string; period?: Period }) {
  if (!kline || kline.length < 2) {
    return <div style={{ height: 340, display: "grid", placeItems: "center", color: "var(--faint)" }}>暂无K线数据</div>;
  }
  const dates = kline.map((k) => k.date.slice(5)); // MM-DD
  const ohlc = kline.map((k) => [k.open, k.close, k.low, k.high]);
  const vols = kline.map((k) => ({ value: k.volume, itemStyle: { color: k.close >= k.open ? UP : DOWN } }));

  const option = {
    backgroundColor: "transparent",
    animation: false,
    tooltip: { trigger: "axis", axisPointer: { type: "cross" } },
    grid: [
      { left: 58, right: 16, top: 24, height: "52%" },
      { left: 58, right: 16, top: "70%", height: "18%" },
    ],
    xAxis: [
      { type: "category", data: dates, axisLine: { lineStyle: { color: "#3a4a63" } }, axisLabel: { color: "#8b98a9", fontSize: 11 } },
      { type: "category", gridIndex: 1, data: dates, axisLabel: { show: false }, axisTick: { show: false } },
    ],
    yAxis: [
      { scale: true, position: "left", axisLabel: { color: "#8b98a9", fontSize: 11 }, splitLine: { lineStyle: { color: "#1e2a3d" } } },
      { scale: true, gridIndex: 1, axisLabel: { color: "#8b98a9", fontSize: 11 }, splitLine: { show: false } },
    ],
    series: [
      { name: "K线", type: "candlestick", data: ohlc, itemStyle: { color: UP, color0: DOWN, borderColor: UP, borderColor0: DOWN } },
      { name: "成交量", type: "bar", xAxisIndex: 1, yAxisIndex: 1, data: vols, barWidth: "60%" },
    ],
  };

  return (
    <div>
      <div style={{ fontSize: 13, color: "var(--muted)", marginBottom: 4 }}>{name} · {PERIOD_NAME[period]}（前复权，近 {kline.length} 期）</div>
      <ReactECharts option={option} style={{ height: 340 }} notMerge={true} />
    </div>
  );
}
