# 55. Go APM 监控系统实战: 用 Grafana 绘制监控面板（二）——面板优化

## 纲要

- 优化一：**错误数面板要同时按 `method` 聚合**，否则只能看到错误码、看不到具体路由，不利于定位
- 优化二：**`rate` 的时间窗口改用 Grafana 内置变量 `$__rate_interval`**，让它随数据源抓取间隔自动取「间隔 × 4」
- 数据源的抓取间隔（默认 15s）决定了 `$__rate_interval` 的基准，官方建议 rate 窗口至少覆盖 4 个样本

## 正文

### 优化一：错误数按方法名聚合

第一版的黄金指标面板里，错误数只做了按 `status` 的过滤，但**没有按 `method` 聚合**，导致面板上只显示错误码、看不出是哪个接口出了问题，对定位毫无帮助。

正确做法是在 `sum by` 里把 `method` 也加进去：

```promql
sum by (method) (rate(server_handle_seconds_count{app="$app", host=~"$host", type="http", status!="200"}[5m]))
```

这样每条线对应一个具体接口，一眼就能看出是 `GET /order` 还是 `POST /pay` 在报错。

### 优化二：用 `$__rate_interval` 代替写死的窗口

第一版所有 `rate` 都写死了 `[5m]`。但 5-9 里我们已经把 `orderservice` 的抓取间隔配成了 5s，而数据源层面还有一个**默认抓取间隔 15s**（来自 `prometheus.yml` 的 `global.scrape_interval`）。

Grafana 读取数据源的抓取间隔后，提供一个内置变量 **`$__rate_interval`**，它等于「抓取间隔 × 4」。按官方建议，`rate` 的窗口至少要覆盖 4 个样本，否则曲线可能缺数据。`$__rate_interval` 会自动处理这件事：

```promql
sum by (method) (rate(server_handle_total{app="$app", host=~"$host", type="http"}[$__rate_interval]))
```

好处：

- 不用手动在 `5m` / `3m` 之间反复试；
- 抓得越频繁（间隔小），窗口自动变小、数据更灵敏；间隔大则窗口自动变大、保证有样本；
- 把其他面板的 `rate` 窗口也统一改成 `$__rate_interval` 即可。

> 说明：本项目 `orderservice` 配的是 5s 抓取，若要更精准也可显式写成 `[20s]`（5s × 4）。但线上通常不会把抓取频率拉到 5s 这么高，维持 15s 抓取、用 `$__rate_interval`（≈60s）是更通用的做法。

```mermaid
flowchart LR
    A[数据源抓取间隔 15s] --> B[Grafana $__rate_interval = 15s × 4]
    B --> C[rate 窗口自动取 60s]
    C --> D[曲线至少覆盖 4 个样本<br/>不会缺数据]
```

## 技术点总结

- 错误数面板必须 `sum by (method)`，否则只能看错误码看不到路由
- `$__rate_interval` = 数据源抓取间隔 × 4，是 `rate` 窗口的最佳实践值
- 把面板里的固定窗口（如 `[5m]`）统一替换为 `$__rate_interval`，可自适应抓取频率

