import type { Metadata, Viewport } from "next";
import "./globals.css";
import Nav from "@/components/Nav";

export const metadata: Metadata = {
  metadataBase: new URL("https://quant.webfault.com"),
  title: { default: "网锋量化 QuantSite", template: "%s · 网锋量化" },
  description: "量化投研 · 短线决策看板 · 模拟盘 · 三轨量化课程（量化基础 / 数字货币实战 / 数据分析）",
  keywords: ["量化交易", "量化投资", "ETF", "短线择时", "A/B 实验", "数据分析", "模拟盘", "回测"],
  icons: { icon: "/favicon.svg" },
  openGraph: { type: "website", locale: "zh_CN", siteName: "网锋量化 QuantSite" },
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh-CN">
      <body>
        <Nav />
        {children}
        <footer>
          <div className="wrap">
            <b>合规披露：</b>本站为量化方法学习与演示工具，<b>不构成任何投资建议</b>；行情数据来自公开接口（东方财富/腾讯），可能延迟；量化交易有风险，历史与模拟业绩不代表未来收益；本站不代客理财、不自动下单、不接入真实资金。投资决策请独立判断并自行承担风险。
          </div>
        </footer>
      </body>
    </html>
  );
}
