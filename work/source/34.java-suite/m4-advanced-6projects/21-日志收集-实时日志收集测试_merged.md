# 21-日志收集-实时日志收集测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们接着开始实现日子时事收集的测试

测试的时候我们一会儿只需要刷新页面

页面一刷新这个地址它会记录

然后我们这边会立刻看到访问的日子信息

我们先把Nginx的配置重新加载一下

Nginx-s reload加载一下

加载之后我们现在就来实现我们的一个请求

刷新一次页面是可以正常访问的了

这个不对咱得加个web对不对

web

这个时候是不会有日子输出的

因为没有经过第一个location

我们再来回车试一下

可以详情页是可以访问的

我们看日子输出没有

输出了日子已经输出了

这是这一块

我们这一块就已经实现了

用户请求详情页

访问详情页的一个日子实时收集了

好

这是这一块的一个知识点的讲解

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

该视频片段展示了一个技术演示，主要围绕如何使用 **Kafka** 和 **Nginx** 进行日志收集和数据流转，最终将数据发送到 **Apache Druid** 进行实时分析。演示者通过终端操作 Kafka 消费者来查看商品详情页的访问日志，并通过 Nginx 的 Lua 模块（OpenResty）来处理这些日志，将关键信息（如商品ID、访问时间、IP）结构化后发送到 Kafka。整个过程旨在说明一个完整的日志收集、处理和分析的流水线。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的画面是静态截图，无法精确判断时间点。但根据画面内容和逻辑顺序，可以推断出以下章节结构：

*   **00:00 - 00:02**: 展示前端页面，显示一个商品详情页，包含商品ID和“秒杀商品详情”字样。
*   **00:03 - 00:07**: 切换到终端，演示者执行 Kafka 消费者命令，准备消费名为 `logitems` 的主题。
*   **00:08 - 00:10**: Kafka 消费者成功消费到一条消息，内容为 JSON 格式，包含 `token`、`actime`、`ip` 和 `uri` 等字段。
*   **00:11 - 00:13**: 演示者切换到 Nginx 配置目录，准备修改配置文件。
*   **00:14 - 00:16**: 展示 Nginx 配置文件 `nginx.conf` 的结构，其中包含两个 `location` 块，分别用于处理 `/web/items` 和 `/items` 的请求。
*   **00:17 - 00:19**: 展示 `items-access.lua` 脚本内容，该脚本负责获取请求头、构建日志对象、发送消息到 Kafka，并重定向请求。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “3.3.3 Lua日志收集”。
    *   **流程图**: 一个 Nginx 与 Apache Druid 的数据流转图，显示了用户请求 -> Nginx -> Kafka -> Apache Druid 的路径。
    *   **代码片段**:
        *   **Kafka 消费者命令**:
            ```bash
            /kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic logitems --from-beginning
            ```
        *   **Lua 脚本 (items-access.lua)**:
            ```lua
            -- 配置Kafka的连接地址
            local broker_list = {
                { host = "192.168.211.137", port = 9092 }
            }
            -- 创建生产者
            local pro = producer:new(broker_list, { producer_type="async" })
            -- 获取IP
            local headers = ngx.req.get_headers()
            local ip = headers["X_REAL_IP"] or headers["X_FORWARDED_FOR"] or ngx.var.remote_addr or "0.0.0.0"
            -- 定义消息内容
            local logjson = {}
            logjson["uri"] = ngx.var.uri
            logjson["ip"] = ip
            logjson["token"] = "Bearer ETHMA"
            logjson["actime"] = os.date("%Y-%m-%d %H:%M:%S")
            -- 发送消息
            local offset, err = pro:send("itemaccess", nil, cjson.encode(logjson))
            -- 页面跳转
            local uri = ngx.var.uri
            uri = string.gsub(uri, "/web/", "")
            ngx.exec(uri)
            ```
        *   **Nginx 配置文件 (nginx.conf)**:
            ```nginx
            server {
                listen 80;
                server_name localhost;

                # /web开始的请求，做日志记录，然后跳转到下面的location
                location /web/items/ {
                    content_by_lua_file /usr/local/openresty/nginx/lua/items-access.lua;
                }

                # /items开始的请求，直接在详情页目录下找文件
                location /items/ {
                    root /usr/local/openresty/nginx/web/;
                }
            }
            ```

---

### 4) 关键场景与演示描述

*   **场景一：前端页面展示**
    *   **描述**: 视频开始时，展示了一个简单的商品详情页。页面上显示了商品ID `5125433012716489944` 和“秒杀商品详情”字样。这表明前端应用正在正常工作，并向后端发送请求。
*   **场景二：Kafka 消费者消费日志**
    *   **描述**: 演示者在终端中执行 Kafka 消费者命令，成功消费到一条日志消息。消息内容为 JSON 格式，包含 `token`、`actime`、`ip` 和 `uri` 等关键字段，这证明了日志数据已经成功从 Kafka 主题中读取。
*   **场景三：Nginx Lua 脚本处理日志**
    *   **描述**: 演示者展示了 `items-access.lua` 脚本。该脚本通过 `ngx.req.get_headers()` 获取客户端 IP，构建一个包含访问信息的 JSON 对象，并使用 `producer:send()` 方法将该对象发送到 Kafka。最后，它通过 `ngx.exec(uri)` 将请求重定向到目标页面。
*   **场景四：Nginx 配置文件结构**
    *   **描述**: 展示了 Nginx 配置文件 `nginx.conf` 的结构。配置文件中定义了两个 `location` 块，分别用于处理 `/web/items/` 和 `/items/` 的请求。前者调用 Lua 脚本进行日志处理，后者直接返回静态文件，实现了日志收集和页面服务的分离。

---
