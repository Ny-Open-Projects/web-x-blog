# 网锋量化 QuantSite

量化投资子站：**真实行情决策看板 + 三轨量化课程 + 模拟盘**。Next.js 15 + React 19 + TypeScript，纯 CSS 深色主题。

线上：`https://quant.webfault.com`（本机 Docker :8098，nginx 子域反代，通配符证书）

## 模块

- **决策看板 `/`**：大盘环境评级 + 自选标的全览 + 逐一深度分析（量价 / 多空量能 / 午后动能 / MA·MACD·RSI / 明日·下周·下月 / 支撑压力 / 情景概率 / 条件式操作）。
- **K 线图**：ECharts 蜡烛图 + 成交量，**日 / 周 / 月**周期切换（涨红跌绿，A 股惯例）。
- **量化课程 `/course`**：三轨 **26 模块**——量化基础 5 + 数字货币量化实战 11 + 数据分析（量化基石）10。
- **模拟盘 `/sim`**：虚拟资金 ¥1,000,000，按实时价撮合买卖、持仓与盈亏，localStorage 持久化，不接真实资金。

数据来自**腾讯财经公开接口**（qt.gtimg 实时报价 + ifzq 前复权 K 线 + minute/query 分钟线），接口不可用时自动降级为模拟数据并在页首标注。

## 指标口径

- **趋势**：MA5 / MA20 位置、MACD 金叉死叉、RSI6 超买超卖、5 日动量
- **量能**：换手率、**量比**、**外盘（主动买）vs 内盘（主动卖）占比** → 判买方/卖方主导
- **午后**：分钟线取 13:00–15:00，按涨跌与收盘位置判「上攻 / 探底回升 / 冲高回落 / 震荡」
- **综合**：十维加权得 ±3 分 → 偏多 / 中性 / 偏空；情景概率由分数量化；趋势按明日 / 下周 / 下月输出方向 + 幅度 + 置信度

## 本地开发

```bash
cd work/quant-site
npm install
npm run dev      # http://localhost:3000
```

课程内容是 `content/{basics,quant,data}/*.md`，front-matter 只需 `title / track / order / summary`，新增文件自动进导航与 sitemap。

## 生产部署

见 [DEPLOY.md](./DEPLOY.md)。要点：

```bash
docker build -t quant-site:0.3.0 .
docker run -d --name quant-site --network webfault-net --restart unless-stopped -p 8098:3000 quant-site:0.3.0
docker exec webfault-nginx nginx -s reload
```

⚠️ 容器须加入 `webfault-net`（nginx upstream 走容器名 `quant-site:3000` 解析）；端口用 **8098**（8093 已被 search-web 占用）；镜像须含 `public/` 目录。

无人值守脚本 `deploy/autodeploy.sh`：等 Docker daemon 就绪 → 构建 → 起容器 → reload nginx → 自验。

## 目录

```
app/            页面与 API（看板 / 课程 / 课程详情 / 模拟盘 / api/board / sitemap / robots）
components/     Board(看板) / KLineChart(蜡烛图) / SimTrading(模拟盘) / Markdown / Nav
lib/            market.ts(行情+指标+综合) / content.ts(课程) / watch.ts(自选持久化)
content/        课程 Markdown（basics 基础 + quant 实战 + data 数据分析）
deploy/         nginx vhost 配置 + 自动部署脚本
```

## 数据与风控

- 换标的/加自选：改 `lib/market.ts` 的 `WATCH` / `INDICES`；前端自选存 localStorage。
- 决策为**规则化指标综合**，仅供参考，非投资建议。
- 合规：不承诺收益、不自动下单、仅模拟盘、全链路风险披露。
