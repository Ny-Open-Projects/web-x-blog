# 18-日志收集-lua-resty-kafka安装和使用讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那么刚才我们说过

要想实现这个日子收集

我们得能向我们的卡夫卡生产房屋的一个日子信息

这个时候我们需要依赖Lua Recipe Kafka

那这个Lua Recipe Kafka

它的一个库在这里

我们可以去下载一下

好

我们打开这个库

进入到这里之后

这里有这个下载

大家可以点击下载

下载之后呢

就会有一个压缩包

这个压缩包我们需要解压一下

解压之后

下面这里有一个使用说明

你要添加Lua Package Pass

需要把刚才那个解压的Lua的一些库文件给加载进来

好

我们看一下

在我这里呢

已经提前

已经提前下载了

好

我先把上面这个注释掉

等会儿我们用的时候再打开

我们这个时候呢

在这一块需要下载

刚才那个Lua库

我已经下载下来了

叫Lua Recipe Kafka Master.zip

我们现在需要解压这个文件

on.zip

Lua-Recipe-Kafka

好

解压了

解压了之后呢

注意一下

这里有个目录了

-Recipe Kafka

有这个目录了

它里面有一个lib目录

cdlib

cdlib

这里还有个reslib目录

大家可以看到里面就是一些库文件了

它这里呢

我们进去看一下cd Kafka

这里有一些相关的Lua库

这个是broker

这个是client

这个是produce

produce很明显就是消息生产者

client很明显就是消息消费者

这是我们这一块的一个配置讲解

接着

我们要把这个

主件也就是咱们这个库用到咱们这里来

怎么用呢

注意看一下这个路径

我们需要告诉我们nginx

在这里有一个库文件是你需要去加载的

对吧

那怎么办呢

就把我们的nginx打开看一下

这个我先退出空气的词义

刚才没有反应

我先进入到我们的nginx

我们先进入到我们的nginx

进入到我们的nginx那里去

usr local openresd

nginx configure

vi-nginx configure

在这里添加一下我们Lua库的地址

刚才是哪个地方呢

所以刚才是usr local openresd

luaresd-kafka-master

下面的lib下面的

所有的Lua脚本

lib下面的所有的Lua脚本

所有的Lua脚本

所有的Lua脚本

就是咱们这一块

就是咱们这一块

它会包含它下面的子目录

它会包含它下面的子目录

配置了之后

那么这个时候这个库就可以正式去使用了

这是咱们这一块Luaresd-kafka的一个安装和配置说明

配置好了之后

我们就可以开始用它去实现我们kafka的一个操作了

关于kafka的一个操作

在下面这一块有相关的一个使用说明

这个使用说明呢

我们来讲解一下

第一个这个地方要引入要依赖我们的Luaresd-kafka-client

Luaresd-kafka-producer

其实我们只需要依赖下面这个就行了

因为上面这个是消费者

而我们目前这里只做生产者

好

接着还有一个local broker list

这就是我们一会儿要向哪个kafka去发消息

那个kafka的IP和端口

这里还有个key

可以写可不写

还有个叫做message

就是你要向kafka发的一个消息

好

我们看一下这一块

这一块呢

大家看一下有一个client-6

broker list

表示创建一个消息消费者

那么消费谁消费这个kafka地址

里面对应的一些对联

好

这里有一个client-fetch-metadata

好

这里有一个client-fetch-metadata

这个其实就是消费test对立的数据

如果消费到了

这个时候就把它给输出

没有消费到

我们这里也输出一段话

上面这个是消息消费

而下面这个是消息生产

生产这一块produce

冒号6创建一个消息生产者对象

broker list创建这一个kafka

它对应的一个消息生产者对象

它对应的一个消息生产者对象

它对应的一个消息生产者对象

接着有个p冒号剩的

表示我们去发送我们的发送我们的消息

也就是做消息生产

发送给谁

发送给test

这是对立的名字

对立的名字key可以随便写

你可以写nil

key可以写nil不发

不指定对应的key

message就是对应的一个发送的消息

好

这一块如果发送成功了

我们就输出下面这一段话

如果发送失败了

我们就输出错误

还有一个下面这里也是一个消息发送

而下面这个消息发送用的是异步的方式

也首先用了一个produce对象

这后面这里写了个produce type

等于osin口异步

这里也是执行了消息发送

这个没有什么区别了

好

OK

这是我们当前这一个lua rest卡

好ok

我们现在来看一看

我们现在来看一个卡夫卡的一个安装和使用说明

等会我们就直接用它来实现

向我们的消息中间键

卡夫卡发送我们的消息了

实现我们消息生产了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程讲解了如何使用 Lua 语言在 Nginx 中实现日志收集，并将日志数据发送到 Apache Kafka 队列，最终由 Apache Druid 进行实时分析。核心内容包括：
*   **技术栈**：Nginx + Lua (OpenResty) + Kafka + Apache Druid。
*   **核心组件**：`lua-resty-kafka` 是一个关键的 Lua 库，用于在 Nginx 中与 Kafka 通信。
*   **工作流程**：用户访问 `/web/items/` 路径时，Nginx 会拦截请求，将日志信息（如请求路径、用户信息等）通过 Lua 脚本发送到 Kafka，然后 Kafka 将数据分发给 Druid 进行分析。
*   **操作步骤**：课程演示了如何下载、解压 `lua-resty-kafka` 库，并将其路径配置到 Nginx 的 `nginx.conf` 文件中，最后通过一个示例 Lua 脚本进行测试。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:30**：课程引言，介绍本节内容为“Lua 日志收集”，并展示课程大纲。
*   **00:30 - 01:00**：讲解日志收集的整体流程图，说明 Nginx、Kafka、Druid 三者之间的数据流向。
*   **01:00 - 01:30**：演示如何从 GitHub 下载 `lua-resty-kafka` 项目。
*   **01:30 - 02:00**：在本地服务器上解压下载的库文件。
*   **02:00 - 02:30**：修改 Nginx 配置文件 `nginx.conf`，添加 `lua_package_path` 指令，将 `lua-resty-kafka` 库的路径加入。
*   **02:30 - 03:00**：展示并讲解 `lua-resty-kafka` 库的源码，重点是 `resty.kafka.producer` 模块的使用方法。
*   **03:00 - 03:30**：演示如何在 Nginx 中创建一个 Lua 脚本，用于向 Kafka 发送日志消息。
*   **03:30 - 04:00**：总结本节内容，强调配置和代码的关键点。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 图表

*   **日志收集流程图** (00:30-01:00)：
    *   **流程**：用户请求 → Nginx → Kafka → Apache Druid。
    *   **关键路径**：
        *   `/web/items/` 路径的请求会被拦截。
        *   请求会被重定向到 `/items/` 路径，以实现文件访问。
        *   同时，请求信息会被 Lua 脚本捕获并发送到 Kafka。

#### 代码

*   **Nginx 配置文件 (`nginx.conf`) 关键片段** (02:00-02:30)：
    ```nginx
    lua_package_path "/usr/local/openresty/lua-resty-kafka-master/lib/?.lua;;";
    # 在 server 块中配置 location
    location / {
        # ... 其他配置 ...
    }
    location /web/items/ {
        # 拦截所有以/web/items/开始的请求
        # 并将请求重定向到另一个 location
        # 同时，通过 Lua 脚本向 Kafka 发送日志信息
        # 代码示例：lua_code_cache off;  # 可选，用于调试
        # lua_shared_dict log_cache 10m;  # 可选，用于共享内存缓存
        # 以下为示例 Lua 脚本的调用
        # set $log_message "user: $remote_user, request: $request_uri";
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code_cache off;
        # lua_shared_dict log_cache 10m;
        # lua_code
