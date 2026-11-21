# 21-热点商品抢单-Redis集群操作工具测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们接下来把这个工具类给测试一下

这个工具类如果说可以用

那咱们就用它

那我们做这么一个事情

我们一会儿测试

获取一下这里面指定数据的一个RAMP值

看能否拿到数据

好 我们来编写一下相关的代码

在这一块我们直接去操作我们的Nginx了

好 找到Nginx Config

在这里我们就配置一个

写到这里

行

这个

拉给一下

这个刚才是不是格式乱的呀

好 我们再来

把刚才这个给拷贝一份

这一块主要是测试我们的一个脚本的

测试脚本

这个是redis-cluster.lua脚本

好 怎么测试呢

我写一下

写个叫test

斜杠

redis

就可以了

那这个怎么测试呢

我们就直接用那个脚本就行了

这里我就写一下叫做content-by-lua

好 我写一下

这里面我们来写一下相关的实现了

这个就简单写就行了

就不写那么复杂了

那这一块我整这么一个事情

首先我要设置编码

来 设置编码叫做

ngx.

head.content-type

等于 我们写一下

application-json

charset-utf8

我就在这里写个案例就行了

就不搞那么复杂了

那我现在要用到刚才那个文件

那这里我要引入依赖

那引入依赖呢

来写一下local叫lredis-cluster.lua

等于requiry

这个requiry咱写一下这里

还是在这里写比较好

这里写轻松一点

行 require

把这个文件给写过来

文件叫redis-cluster

还有一个依赖

就是我们cjson的依赖

也得引入进来

好 写到这里

cjson

那前面这里也得写个cjson

行

这里总的来说呢

我们就开始去调用了

去调用一下

调用谁呢

调用它里面的方法

哪个方法呢

我们看一下

调用这一个方法叫hget

这个hget

别的我就不去测试了

我只测试这一个就行了

hget

给几个key它呢

给两个key

好 两个key我们看一下

第一个key是最外层的key

这个 对吧

最外层的key

写到这里

第二个key呢是number

这个key

我们看一下这一块能否拿到数据

好

好

拿到数据之后呢

我们定一个对象存一下local result等于

我们再将result输出ngx.say cjson.encode result

好 我们看这一块能否正常运行

好 我们看这一块能否正常运行

资讯是-s Reload

那现在我们就直接去访问了

就不做别的事情了

好 这一块就換一下

换成我们的test

redis回车一下

那这一块就报了500

我们看为什么会报500

log

好

cat

log

下面有个arrow

我们看这里为啥报500呢

它说当前这一块有一个对象无效

我们看是哪个对象无效

207行有个对象无效

对不对

config对象无效

咱们这里config对象配置可能有点问题

好我们看一下

89行

我们看这里89行

它说这一块我们看一下

70行对不对

hmget无效

我们看这哪里写错了

70行我们找到70行

这一块无效

这里不对

这里要用冒号

注意这个地方要用冒号才行

那么这里要用冒号

其他的地方也是一样

都要换成冒号才行

不能写点号

不能像咱家玩一样

好就这个给换一下

OK了

可以了

暂时看不到点了

就可以了

行

我们再来重新执行一次

ngs-s reload

再来重新请求一下

看效果

刷新一次

可以了

行

这是我们这个

工具的一个测试

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是一个关于如何在 Nginx 中使用 Lua（通过 OpenResty）与 Redis 集群进行交互的实战教程。主要内容包括：
- **核心目标**：实现一个基于 Lua 的 Nginx 服务，用于处理 HTTP 请求，并将数据写入 Redis 集群。
- **技术栈**：Nginx + OpenResty + Lua + Redis Cluster。
- **关键操作**：演示了如何在 Lua 中使用 `redis-cluster` 库初始化连接、执行 `HSET` 和 `HINCRBY` 命令，并通过 Nginx 的 `location` 块进行路由配置。
- **问题排查**：视频中展示了在执行 Lua 脚本时遇到的错误（如 `attempt to concatenate a nil value`），并分析了错误原因。
- **环境展示**：视频中展示了开发环境，包括代码编辑器（如 VS Code）、Nginx 配置文件、Redis 集群管理工具（如 Redis Desktop Manager）以及浏览器用于测试接口。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中每个画面对应的时间点，以下章节是根据画面内容和逻辑顺序进行的划分：

- **00:00 - 00:05**：开场，展示开发环境，包括 VS Code 编辑器中的 Lua 代码和 Nginx 配置文件。
- **00:05 - 00:15**：讲解 Nginx 配置文件，重点是 `location` 块的配置，用于将 `/lua/order/add` 路径的请求路由到 Lua 脚本。
- **00:15 - 00:25**：展示 Lua 脚本 `redis-cluster.lua` 的内容，包括初始化 Redis 集群连接、执行 `HSET` 和 `HINCRBY` 命令的代码。
- **00:25 - 00:35**：演示如何在 Nginx 中配置 `location /test/redis` 来测试 Lua 脚本。
- **00:35 - 00:45**：在浏览器中访问测试接口，展示返回结果。
- **00:45 - 00:55**：展示 Redis Desktop Manager 中的 Redis 集群数据，验证 Lua 脚本执行成功。
- **00:55 - 01:05**：在终端中执行 Lua 脚本，展示错误日志，分析错误原因。
- **01:05 - 01:15**：回到代码编辑器，对 Lua 脚本进行修改和调试。
- **01:15 - 01:25**：再次在浏览器中访问接口，展示修正后的结果。
- **01:25 - 01:35**：总结，强调 Lua 与 Redis 集群结合的优势和应用场景。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### 代码关键内容：

- **Lua 脚本 `redis-cluster.lua`**：
  ```lua
  -- Hash操作，增加数据，key1, key2
  function lredis.hset(key1, key2, value)
      -- 创建链接对象
      local red = redis_cluster:new(config)
      -- 初始化链接
      red:init_pipeline()
      -- 执行的命令编写
      red.hset(key1, key2, value)
      -- 执行命令
      local results = red:commit_pipeline()
      -- 关闭链接
      red:close()
      return lredis
  end

  -- Hash操作，if key1 里面key2值自增1
  function lredis.hincrby(key1, key2, value)
      -- 创建链接对象
      local red = redis_cluster:new(config)
      -- 初始化链接
      red:init_pipeline()
      -- 执行的命令编写
      red.hincrby(key1, key2, value)
      -- 执行命令
      local results = red:commit_pipeline()
      -- 关闭链接
      red:close()
      return lredis
  end
  ```

- **Nginx 配置文件关键部分**：
  ```nginx
  location /lua/order/add {
      content_by_lua_file /usr/local/openresty/nginx/lua/seckill-order-add.lua;
  }

  location /test/redis {
      content_by_lua_file /usr/local/openresty/nginx/lua/redis-cluster.lua;
  }
  ```

#### 错误日志：

- **错误信息**：
  ```
  runtime error: /usr/local/openresty/nginx/lua/seckill-order-add.lua:20: attempt to concatenate a nil value
  runtime error: /usr/local/openresty/nginx/lua/redis-cluster.lua:76: in function 'get'
  ```

---

### 4) 关键场景与演示描述

- **场景一：环境搭建与代码编写**
  - **描述**：视频开始时，展示了 VS Code 编辑器中的 Lua 代码，包括 `redis-cluster.lua` 脚本。代码中定义了 `hset` 和 `hincrby` 函数，用于向 Redis 集群写入数据。
  - **技术点**：使用 `redis_cluster:new(config)` 初始化连接，`init_pipeline()` 开启管道，`commit_pipeline()` 执行命令，`close()` 关闭连接。

- **场景二：Nginx 配置与路由**
  - **描述**：在终端中编辑 Nginx 配置文件，配置了 `location /lua/order/add` 和 `location /test/redis`，将请求路由到对应的 Lua 脚本。
  - **技术点**：使用 `content_by_lua_file` 指令指定 Lua 脚本文件。

- **场景三：接口测试与数据验证**
  - **描述**：在浏览器中访问 `http://192.168.211.137/test/redis` 接口，返回结果为 `11`，表示 `HINCRBY` 操作成功。
  - **技术点**：通过 HTTP 请求触发 Lua 脚本，验证 Redis 集群数据写入。

- **场景四：错误排查与调试**
  - **描述**：在终端中执行 Lua 脚本时，出现错误日志，提示 `attempt to concatenate a nil value`。视频中分析了错误原因，并对代码进行了修改。
  - **技术点**：错误日志分析，代码调试。

- **场景五：Redis 集群数据展示**
  - **描述**：使用 Redis Desktop Manager 工具连接 Redis 集群，查看 `HSET` 操作写入的数据。
  - **技术点**：Redis 集群管理，数据验证。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解视频内容。
