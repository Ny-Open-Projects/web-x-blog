# 18-常见组件与中台化-常用组件服务介绍（通用权 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么刚才呢在咱们这个应用的这个地方呢出现了一个问题对吧

就是我们刚才这个数据呢其实是加载不出来的

这个是因为什么呢我刚才排查了一下

是因为我们这三个服务也就是PD Auth Server还有PD GOODS Server还有PD Gateway呢

刚才是不在同一个分组里边

导致什么呢我们这个网关处理完之后啊

它是不是想路由到我们这个商品服务

结果呢找不到商品服务因为他们不在同一个分组

现在呢我已经改过来了

大家只要在这个什么呢这个地方给它加一个group

对吧在我们这个服务的这个注册中心这个地方

给它写上这个品达TMS

因为我们当前这个什么权限服务还有这个网关服务呢都在这个分组里边

而我们刚才呢这个是没有写

没有写的话它其实是在那个默认分组里边

导致什么呢它在进行路由的时候呢找不到咱们这个商品服务

现在呢我们就在这个中心里面

你看我改过来之后呢它其实就没有问题了

你看我们正常查询的什么的这些操作都是没有问题的

比如说我删除一个数据对吧点确定

好这样呢就把它删掉了

好这是对我们刚才这个问题啊一个修复

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告：

---

### 1) 视频摘要

本视频片段主要演示了一个基于 **Nacos** 服务发现与配置中心的微服务架构。核心内容包括：
- **Nacos 控制台**：展示服务注册与发现的管理界面，确认 `pd-auth-server`、`pd-goods-server` 和 `pdd-gateway` 三个服务均已成功注册到 Nacos 服务列表中。
- **业务系统界面**：展示一个名为“易达物流”的商品管理后台，用于演示服务调用的业务场景。
- **代码配置**：通过 IDE（IntelliJ IDEA）展示 Spring Cloud 项目中 `bootstrap.yml` 配置文件，说明如何通过 Nacos 注册服务、配置命名空间、分组和元数据。
- **问题排查**：演示了当服务因健康检查失败而无法被调用时，前端页面会弹出提示框，提示用户“当前数据可能被永久删除，是否继续？”。

整个视频旨在说明 Nacos 在微服务架构中的核心作用，即服务注册、配置管理，以及在服务异常时的前端交互处理。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的画面没有明确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:05**：展示 Nacos 服务管理界面，列出已注册的服务（`pd-auth-server`, `pd-goods-server`, `pdd-gateway`），并强调其分组为 `pinda-tms`。
- **00:06 - 00:10**：切换到商品管理后台，展示商品列表数据，用于演示服务调用的业务场景。
- **00:11 - 00:15**：回到 Nacos 界面，再次确认服务列表，强调服务健康状态。
- **00:16 - 00:20**：切换到 IntelliJ IDEA，展示 `bootstrap.yml` 配置文件，重点讲解 `nacos`、`discovery` 和 `logging` 等配置项。
- **00:21 - 00:25**：再次回到商品管理后台，展示商品列表。
- **00:26 - 00:30**：在商品列表页面点击“删除”按钮，触发弹窗提示“当前数据可能被永久删除，是否继续？”。
- **00:31 - 00:35**：弹窗提示框出现，用户可选择“取消”或“确定”。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### 代码关键内容（来自 `bootstrap.yml`）

```yaml
nacos:
  username: tms
  password: itheima123
  config:
    server-addr: ${pinda.nacos.ip}:${pinda.nacos.port}
    file-extension: yaml
    namespace: ${pinda.yaml.namespace}
    shared-dataids: common.yml,redis.yml,mysql.yml
    refreshable-dataids: common.yml
    enabled: true

discovery:
  server-addr: ${pinda.nacos.ip}:${pinda.nacos.port}
  namespace: ${pinda.nacos.namespace}
  metadata:
    management.context-path: ${server.servlet.context-path}:${spring.mvc.servlet.path}
  group: pinda-tms

logging:
  file:
    path: /data/projects/logs
    name: ${logging.file.path}/${spring.application.name}/root.log
```

#### 关键配置说明

- **Nacos 配置**：
  - `username` 和 `password`：用于 Nacos 的认证。
  - `config.server-addr`：Nacos 配置中心的地址。
  - `namespace` 和 `group`：用于区分不同环境或业务线的服务和配置。
  - `shared-dataids` 和 `refreshable-dataids`：定义了共享和可刷新的配置文件。

- **服务发现配置**：
  - `discovery.server-addr`：服务发现的地址。
  - `discovery.group`：服务分组，用于服务注册和发现。

- **日志配置**：
  - `logging.file.path` 和 `logging.file.name`：定义了日志文件的存储路径和名称。

---

### 4) 关键场景与演示描述

#### 场景一：服务注册与发现

- **演示描述**：视频首先展示了 Nacos 控制台的服务列表，其中包含三个服务：`pd-auth-server`、`pd-goods-server` 和 `pdd-gateway`。它们的分组均为 `pinda-tms`，且健康状态均为 `false`，表明服务可能未完全启动或健康检查失败。这演示了 Nacos 作为服务注册中心的功能。

#### 场景二：业务系统调用

- **演示描述**：视频切换到商品管理后台，展示了商品列表数据。这表明前端应用（如 `pdd-gateway`）能够通过 Nacos 发现并调用后端服务（如 `pd-goods-server`）来获取数据。

#### 场景三：配置文件详解

- **演示描述**：视频展示了 `bootstrap.yml` 文件，详细讲解了 Nacos 的配置项和服务发现配置。这说明了如何在 Spring Cloud 应用中集成 Nacos，实现配置中心和注册中心的功能。

#### 场景四：异常处理与前端交互

- **演示描述**：在商品管理后台，用户点击“删除”按钮后，弹出提示框：“当前数据可能被永久删除，是否继续？”。这演示了在服务异常或数据删除时，前端如何与用户交互，确保数据安全。

---

以上是根据视频画面进行的结构化技术分析报告。
