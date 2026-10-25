# 网锋量化 QuantSite

量化投资子站：**真实行情决策看板 + 量化课程 + 模拟盘**。Next.js 15 + React 19 + TypeScript，纯 CSS 深色主题。

## 模块
- **数据看板 `/`**：大盘环境 + 自选 ETF 全览 + 逐一深度分析（今日数据 / MA·MACD·RSI / 明日·下周·下月 / 支撑压力 / 情景概率 / 条件式操作）。数据来自**东方财富公开接口（实时）**，接口不可用时自动降级为模拟数据并标注。
- **量化课程 `/course`**：两大主线——量化基础（指标·分类·系统·JQData，源自课程文档）+ 数字货币量化实战（wyy0008）。
- **模拟盘 `/sim`**：虚拟资金 ¥1,000,000，按实时价撮合买卖、持仓与盈亏，localStorage 持久化，不接真实资金。

## 本地开发
```bash
cd work/quant-site
npm install
npm run dev      # http://localhost:3000
```

## 生产部署
```bash
npm run build && npm start           # 本机 node 18+ 
# 或 Docker：
docker build -t quant-site:0.1.0 .
docker run -d --name quant-site -p 8093:3000 quant-site:0.1.0
```

## 作为 web-x-blog 子站
- 子域：`quant.webfault.com` → 反代到 `http://127.0.0.1:8093`
- 子路径：主站 Nginx `location /quant/ { proxy_pass http://127.0.0.1:8093/; }`

## 目录
```
app/            页面与 API（看板 / 课程 / 模拟盘 / api/board）
components/      Board(看板) / SimTrading(模拟盘) / Markdown / Nav
lib/             market.ts(行情+指标+综合) / content.ts(课程加载)
content/         课程 Markdown（basics 基础 + quant 实战）
```

## 数据与风控
- 换标的/加自选：改 `lib/market.ts` 的 `WATCH` / `INDICES`。
- 决策为**规则化指标综合**（MA/MACD/RSI/动量打分），仅供参考，非投资建议。
- 合规：不承诺收益、不自动下单、仅模拟盘、全链路风险披露。
