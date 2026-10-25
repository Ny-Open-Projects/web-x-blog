import type { Metadata } from "next";
import SimTrading from "@/components/SimTrading";

export const metadata = { title: "模拟盘", description: "用自选标的做买入卖出模拟，演练仓位与止损纪律，不接入真实资金" };

export default function Page() {
  return (
    <main className="wrap">
      <section className="hero">
        <h1>模拟盘</h1>
        <p>虚拟资金 ¥1,000,000，按看板实时价撮合；用于验证决策、练习仓位与止损，<b>不接真实资金</b>。</p>
      </section>
      <div className="banner sim">🧪 模拟交易：所有盈亏为虚拟演示，仅用于学习方法与风控，不构成投资建议。</div>
      <SimTrading />
    </main>
  );
}
