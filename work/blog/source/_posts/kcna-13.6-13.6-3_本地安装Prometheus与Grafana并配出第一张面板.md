---
title: "Kubernetes 认证考点: 本地装起 Prometheus 与 Grafana 并配出第一张面板"
date: 2026-10-02 20:52:00
categories: [kcna, Kubernetes, 监控]
tags: [Prometheus, Grafana, brew, datasource, panel, go_goroutines, prometheus_sdk]
disableNunjucks: true

---

# Kubernetes 认证考点: 本地装起 Prometheus 与 Grafana 并配出第一张面板

前面几节把 Prometheus 的架构、SDK 接入都讲完了，这一节把它真正跑起来看一遍。

结论：**本地安装总共三步 —— ①装 Prometheus；②装 Grafana；③分别登录两个后台做初始化配置。mac 上一条 `brew install` 就能把两个装齐，然后各执行一行启动命令；Grafana 首次登录用默认账号 `admin` / 密码 `admin`，进来必须先改密码；最后在 Grafana 里把 Prometheus 配成数据源，就能建面板画图。**

## 纲要

- 三步走总览
- 本机目录与配置文件
- 端口分工：9090 与 8080
- 启动 Prometheus 与 Grafana
- Grafana 首次登录与改密
- 配置 Prometheus 数据源
- 新建面板：三条曲线
- 面板保存的一个小坑

## 三步走

```mermaid
flowchart LR
    A["① brew install<br/>prometheus grafana"] --> B["② 改配置<br/>/opt/homebrew/etc/prometheus.yml"]
    B --> C["③ 启动服务<br/>brew services start"]
    C --> D["④ 登录 Prometheus 后台<br/>localhost:9090 验证指标"]
    D --> E["⑤ 启动 Grafana<br/>localhost:3000"]
    E --> F["⑥ 登录 Grafana<br/>admin / admin → 改密"]
    F --> G["⑦ 配数据源 datasource<br/>只填 Prometheus 地址"]
    G --> H["⑧ 建 panel 画图"]
```

## 目录准备

切到 `observability` 目录，里面有一份文档（readme），**里面既有 mac 环境的安装说明，也有 linux 环境的安装说明**，按自己的系统挑一节看。

因为后面要基于镜像来部署，linux 那部分的安装过程也会留在文件里。本机是 mac 环境，所以看 mac 这一条 —— **装 Prometheus 和 Grafana 在 mac 上都非常简单，一条 `brew install` 命令就能把两个软件都装上**。

```text
observability/                      # 可观测性工作目录
├── README.md                       # mac / linux 两种安装说明
├── prometheus.yml                  # Prometheus 配置（代码库中同样保留一份）
├── grafana/
│   ├── provisioning/
│   │   └── datasources/
│   │       └── datasource.yml      # 数据源自动 provisioning（可选）
│   └── grafana.ini
└── Dockerfile                      # 后面做镜像用
```

装完之后，**它们的配置文件在 homebrew 的 `etc` 目录下，就是 `prometheus.yml`**，代码库里也有一份简版，需要补一些基本配置。

```bash
# 安装（mac）
brew install prometheus grafana

# 配置文件位置
/opt/homebrew/etc/prometheus.yml
/opt/homebrew/etc/grafana/grafana.ini
```

> 注意 Intel 芯片的 mac 路径前缀是 `/usr/local/etc`，Apple 芯片才是 `/opt/homebrew/etc`，`brew --prefix` 可以确认。

## 端口分工

| 端口 | 是谁 | 用途 |
| --- | --- | --- |
| 9090 | Prometheus 自己 | Prometheus 的 Web UI + 查询 API，也能暴露自己的指标 |
| 3000 | Grafana | Grafana 默认后台端口 |
| 8080 | 业务服务 | 用 gin 框架开发的 web 服务端口 |

**9090 是 Prometheus 自己的端口**，打开它就能看到内置的自监控指标；**8080 是服务的端口**，这个服务前面已经集成了 Prometheus 的 SDK，**所以它的业务指标一样能被抓起来**。

```yaml
# prometheus.yml：抓本地 8080 这个服务
scrape_configs:
  - job_name: "gin-server"
    scrape_interval: 15s
    static_configs:
      - targets: ["localhost:8080"]
```

**采集间隔 15 秒** —— 进来之后能看到具体的指标，也能看到所有已经采集到的指标，但前提是把 8080 这个服务先启动起来，否则序列根本不存在，页面上什么都没有。

## 启动两个服务

本地已经装好了，所以**只是一行命令的事**，而且**两个软件的文件目录不一样，启动方法也有区别**。

```bash
# Prometheus（用 services 方式启动，后台常驻）
brew services start prometheus

# Grafana 另开一个窗口启动
brew services start grafana
```

```text
终端一：prometheus
  > brew services start prometheus
  ==> Successfully started `prometheus` (label: homebrew.mxcl.prometheus)
  ==> To restart prometheus after a upgrade:
     brew services restart prometheus
  输出一堆运行日志 ...

终端二：grafana
  > brew services start grafana
  ==> Successfully started `grafana` (label: homebrew.mxcl.grafana)
  ... 也起来了，还在跑
```

启动成功后分别访问两个地址，两个都起来了才谈得上后面的配置。

```bash
open http://localhost:9090   # Prometheus UI
open http://localhost:3000   # Grafana UI
```

## Grafana 首次登录

**第一次登录会提示默认的用户名和密码，两个都是 `admin`。**

**第一次登录之后需要改一下密码**，这里改成 `admin12345678`（示例密码，注意一定换成自己的强密码）。改完就进到后台了。

```text
Grafana 登录页
├── 用户名：admin            ← 默认
├── 密码：  admin           ← 默认，首次登录强制修改
└── 改密后 → /datasources / /d-dashboard 首页
```

进去之后能查到具体的指标，也能查看所有已经采集到的指标；**现在 8080 端口没有启动起来，所以这边还看不到它的数据 —— 需要把服务启动起来，才能采集到它的指标。**

## 配置数据源

打开文档里 Grafana 配置数据源那一步。**进入 datasource（数据源）页面，这里已经有两个了：一个是 alertmanager，一个是 prometheus；核心动作就是把 Prometheus 的地址配置进来。**

```text
Grafana → Connections / Data sources → + New data source
└── 选 Prometheus
    ├── Name:   Prometheus
    ├── URL:    http://localhost:9090     ← 只需要填这一个地址
    ├── Auth:   默认关闭（本地无鉴权）
    ├── Scrape interval: 15s             ← 保持默认即可
    └── Save & test  → 出现 "Data source is working" 即成功
```

**其他的都不需要设置，保持默认就可以，保存即可。数据源加进去之后，就能在这个页面看到它。**

## 新建面板：三条曲线

进到面板（dashboard）里，**我们这里已经建了一个报表"我的第一个报表"，先点进这个报表看一下**。报表里面的页面跟新建时是完全一样的。

上面有"新建面板"按钮，**点击它，一个新的面板就创建出来了** —— 先把已经建好的那条删掉，从零看一遍创建页面的每个表单项：

1. **设置数据源**：选中刚才配的 Prometheus；
2. **下面列出相应的指标**；
3. **曲线有两条，一条 A 一条 B**：这里设的是 `go_goroutines`，label 是 `job="prometheus"`；
4. **两种显示方式**：一种是原始的 `code`（raw query / 直接写 PromQL），一种是可视化的表单（builder，可以选指标、选指标的标签）；
5. **选一下操作方法**（聚合函数），最后汇总成这个 query；
6. **如果把这个原始的 query copy 进来会更快一些** —— 也就是直接把 PromQL 粘进 Code 模式，比在表单里点选快。

然后**下面还有选项可以设这条曲线的显示名字**；**legend（图例）也设置一下，它支持变量参数** —— 像 `hostname` 这种用两个花括号包起来 `{{hostname}}`，就可以把参数的值传进去，显示出来成为曲线的名字。

```text
Panel → Queries
├── A 曲线（绿）：go_goroutines   job="prometheus"  → {{hostname}}
├── B 曲线（黄）：go_...          job="prometheus"
└── C 曲线（蓝）：inv_request     ← 我们自己自定义的指标，走法一样
```

第三条曲线是 **`inv1_request`（自增请求数）—— 也就是前面集成 SDK 时自己定义并上报的那个自定义指标**，配置选项完全一样，选完指标就能出图。

这样就有三条 query 曲线：**绿色、黄色、蓝色三条**，鼠标移上去能看到这个点对应的具体数据 —— **一个基本的报表就配置出来了。**

**多条曲线其实就靠四个动作：选数据源 → 设查询条件 → 选指标和标签 → 设曲线显示名。剩下的面板（Panel）分组、报表（Dashboard）分组、添加或编辑报表页面都是一样的。**

## 一个容易卡住的地方

**没有更新过是保存不了的。** 这个报表我们从头就没改过，直接点保存会报"没有变化"之类的提示。

```bash
# 保底做法：确认改动进了查询配置再保存
# 哪怕只是把 legend 从 A 改成 A-go_goroutines，保存按钮就亮了
```

所以操作时按这个例子走一遍：先随便动一下（改 legend、改曲线名），**看到保存按钮可用了再正式配**，这样就不会在"保存不了"上浪费时间。

## API 速览

| 路径 / 概念 | 位置 | 作用 |
| --- | --- | --- |
| `localhost:9090` | Prometheus | UI + PromQL 查询 API + 自监控 |
| `localhost:3000` | Grafana | 后台、数据源、面板管理 |
| `/graph`、`/targets` | Prometheus | 查指标、看抓取目标健康 |
| `/datasources` | Grafana | 数据源管理（alertmanager / prometheus） |
| `/d/<uid>` | Grafana | 面板（Dashboard）详情 |
| `code` 模式 | Panel query | 直接写 PromQL，配多曲线最快 |
| `builder` 模式 | Panel query | 表单化选指标 + 标签，新手友好 |
| `legend {{var}}` | Panel | 图例用变量取值当曲线名 |
| `scrape_interval` | prometheus.yml | 本地示例用 15s |

## Demo 示例

把上面这套本地流程落成一条可复现的命令清单，以及对应的最小配置。

```bash
# 1. 安装（mac，Intel 机器把 /opt/homebrew 换成 /usr/local）
brew install prometheus grafana

# 2. 编辑 /opt/homebrew/etc/prometheus.yml，加上 gin-server 这个 job
vim /opt/homebrew/etc/prometheus.yml

# 3. 启动
brew services start prometheus
brew services start grafana

# 4. 另开一个窗口把 8080 的 gin 服务也跑起来（否则抓不到它的指标）
go run ./cmd/server

# 5. 验证
open http://localhost:9090/targets     # 两个 target 都 UP
open http://localhost:3000             # admin / admin → 改密
```

对应的 Prometheus 抓取片段与一条多曲线查询：

```yaml
# /opt/homebrew/etc/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  # Prometheus 自己
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  # gin 业务服务（前面已集成 prometheus SDK）
  - job_name: "gin-server"
    static_configs:
      - targets: ["localhost:8080"]
```

```text
# Code 模式直接粘这三行就能出三条线
# 绿：go_goroutines
go_goroutines{job="gin-server"}
# 黄：Go 进程里的堆内存（换成你实际有的指标）
go_memstatsallocbytes_total{job="gin-server"}
# 蓝：自定义指标 inv_request
increase(inv1_request{job="gin-server"}[1m])
```

```bash
# 命令行验一下序列真的抓到了（比开浏览器快）
curl -s localhost:9090/api/v1/targets \
  | python3 -c "import sys,json;print([t['scrapePool']+':'+t['health'] for t in json.load(sys.stdin)['data']['activeTargets']])"
# ['gin-server:up', 'prometheus:up']
```

## 总结

本地跑通这条链路的价值，在于把前面几节的概念全部落到一次可点的界面上：**装 → 配 → 起 → 验 → 画图**。

1. **mac 上一条 `brew install` 搞定两个组件**，配置在 `/opt/homebrew/etc/prometheus.yml`，改动记得同步到代码库里的那份；
2. **9090 是 Prometheus，3000 是 Grafana，8080 是被监控的业务服务** —— 三个端口分不清，后面一定会踩"抓不到数据"的坑；
3. **Grafana 首次登录 `admin`/`admin`，进来第一件事是改密码**；
4. **配数据源只需要填 Prometheus 地址，其余全默认**；
5. **建面板最快的路径是 Code 模式直接粘 PromQL**，配多曲线就四步：数据源 → 查询条件 → 指标和标签 → 曲线显示名；`{{hostname}}` 这类变量能直接当图例名；
6. **自定义指标和内置指标的配置方式完全一样**，SDK 已经在服务里埋好点，这里选出来就能出图；
7. 最后注意**没改动过保存不了**，先动一下 legend 让保存按钮亮起来。

