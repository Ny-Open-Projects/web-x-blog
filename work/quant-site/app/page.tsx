import { getBoard } from "@/lib/market";
import Board from "@/components/Board";

export const revalidate = 60;

export const metadata = {
  title: { absolute: "网锋量化 QuantSite · 短线决策看板" },
  description: "真实行情驱动的短线决策看板：大盘环境、多空量能、午后动能、支撑压力与条件式操作指引，含三轨量化课程与模拟盘。",
};

export default async function Page() {
  let initial = null;
  try { initial = await getBoard(); } catch { initial = null; }
  return <Board initial={initial} />;
}
