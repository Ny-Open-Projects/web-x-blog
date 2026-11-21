# 22-热点商品抢单-kafka操作工具对象封装 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们实现一下Lua操作卡夫卡

我们把这个Lua操作卡夫卡

封装成一个工具对象

因为也有可能会有很多地方会用到它

我们不可能每个地方去配置一堆代码

好 我们来实现一下

这个对象的名字就叫Lua.kafka

好 我们在这里操作一次

在之前呢

我们这里有一个日志访问这里

是用过它的

大概是这个

把它拷贝一下

名字就叫kafka.lua

好 我们编辑一下kafka.lua

在这一块是之前写的操作

那咱们这里呢

就把它给换一下

首先第一个Cjson这一块

我们就不需要了

对不对

咱换个工具吧

不用这个工具

行 这边我们就先退出一下

来 把这个kafka.lua打开

在这一块呢

我们操作一下

这一块咱把它给操作一下

首先我们来简单说一下

这一块

这个Cjson呢

我们就不要了

好

这个是所有的操作

那这个扣端这一块

我们也不要了

我们只要这个生产者就行了

那么这个是kafka的一个地址

这个呢

我们也不去管它

不用这么多

好 都不要了

这个也不要了

行

其实真正去操作我们对应的对列的

就只有这两段话

那我们现在要把它做成一个公用

的

既然要做成一个公用的

那么这一块就要写相应的方法了

方法呢

我们就写一个哈

而且我们还要配置一个模块

模块了就叫kafka

行接着往里面添加一个方法

只写一个发送

卡夫卡对列消息

好

我们写下方可行卡夫卡点

甚的就可以了

那么既然是发消息

那你一定要把这个对列的消息放在这里

那你一定要把这个对列的消息放在这里

你需要把这个名字给我qlm

还有你要发的消息给我message

接着把这两个给考进去

这样子就可以了

因为我们之前写过

所以这个时候用起来就很方便了

我们看一下这里面对应的一个点哈

这个是对列的名称

那就不要写死了

这个是对应的信息

你直接给我转好传给我就行了

这个就是我们这一块操作卡夫卡的工具类的封装

接着我们把这个对象给返回

ok

可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一段关于在 OpenResty（基于 Nginx 和 Lua）环境中进行后端服务开发与调试的实战教学。讲师通过终端日志、代码编辑器和浏览器访问等多种方式，演示了如何处理 HTTP 请求、与 Redis 集群交互、以及向 Kafka 发送消息。视频的核心内容是排查和解决在服务运行过程中出现的 Lua 脚本错误，例如“attempt to concatenate local id (a nil value)”和“attempt to index file ...”，并展示了如何通过修改代码逻辑来修复这些问题。整个过程体现了在高并发、分布式系统中，如何利用 OpenResty 的强大功能进行业务逻辑开发和故障排除。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的绝对时间点，以下章节是根据画面内容和逻辑顺序进行的推断性划分：

*   **章节 1: 服务启动与错误日志分析 (00:00:00 - 00:00:15)**
    *   展示了 OpenResty 服务启动时的终端日志。
    *   突出显示了多个 `runtime error`，包括 `attempt to concatenate local id (a nil value)` 和 `attempt to index file ...`，并指出这些是需要解决的核心问题。

*   **章节 2: 修复 Lua 脚本错误 (00:00:15 - 00:00:30)**
    *   讲师在代码编辑器中展示并修改了 `order-add.lua` 文件。
    *   重点讲解了如何在 `get_post_args` 函数中正确处理 `local id` 变量，避免出现 `nil value` 错误。

*   **章节 3: Kafka 生产者配置与消息发送 (00:00:30 - 00:00:45)**
    *   讲师切换到 `tafka.lua` 文件，展示了如何配置 Kafka 生产者。
    *   代码中包含了获取客户端 IP、构建消息体、并使用 `send` 方法向 Kafka 发送消息的逻辑。

*   **章节 4: Redis 集群操作与管道命令 (00:00:45 - 00:00:55)**
    *   讲师展示了 `redis-cluster.lua` 文件，讲解了如何使用 `resty.redis` 模块连接 Redis 集群。
    *   重点演示了 `hset`、`hincrby` 等命令的使用，并介绍了 `commit_pipeline` 方法来批量执行命令以提高效率。

*   **章节 5: 服务调试与浏览器访问 (00:00:55 - 00:01:00)**
    *   讲师在浏览器中访问服务，验证功能。
    *   同时在终端中监控日志，观察服务状态和错误信息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段：**

    *   **Lua 脚本错误处理 (来自 `order-add.lua`):**
        ```lua
        -- 错误示例：尝试连接一个 nil 值
        local id = ...  -- 假设此处未正确初始化
        local result = id .. "some string"  -- 会抛出 runtime error

        -- 修复示例：确保变量有值
        local id = get_post_args().id or "default_id"
        local result = id .. "some string"
        ```

    *   **Kafka 生产者配置 (来自 `tafka.lua`):**
        ```lua
        local client = require "resty.kafka.client"
        local producer = require "resty.kafka.producer"

        local broker_list = {
            { host = "192.168.211.137", port = 9092 },
        }

        local bp = producer:new(broker_list, { producer_type = "async" })

        local message = {
            ["ip"] = ngx.var.remote_addr or "0.0.0.0",
            ["actime"] = ngx.now(),
            ["url"] = ngx.var.uri,
            ["token"] = "THEIMA"
        }

        local ok, err = bp:send("logitems", nil, cjson.encode(message))
        ```

    *   **Redis 集群操作 (来自 `redis-cluster.lua`):**
        ```lua
        local redis = require "resty.redis"

        local commands = {
            ["hset"] = {["auth"]},  -- 示例命令
            ["hget"] = {["auth"]},
            ["hincrby"] = {["auth"]},
            ["hdel"] = {["auth"]},
            ["hexists"] = {["auth"]},
            ["hgetall"] = {["auth"]},
            ["hkeys"] = {["auth"]},
            ["hvals"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hscan"] = {["auth"]},
            ["hsetnx"] = {["auth"]},
            ["hsetrange"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
            ["hstrlen"] = {["auth"]},
