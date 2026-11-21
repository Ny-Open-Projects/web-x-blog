# 18-非热点数据抢单-抢单测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们开始去测试一下这个抢单操作

那我们现在测试主要是非热点商品抢单

那么非热点商品抢单这一块呢

我们先来配置一下它的Nginx

它的Nginx这一块呢

我们就配两个

一个是我们Lua Order Addit

一个是我们的API这一块

好我们把Nginx打开

vi configure nginx.configure

把这一块给配置一下

用户抢单的时候

要先经过我们的Lua脚本

这一块我们写一个Lua脚本的控制

这个是抢单操作

好那么地址呢

我们也给一个地址就叫

lua-order-add

后面这个Lua脚本呢

就是我们刚才创建的那个脚本

这个脚本名称我们拷贝一下

好这是这一块

那上面这里呢

它只是做这么一个

事情只是用来判断当前商品是否是热点的

如果不是热点的

它就要走后端的微幅了

后端的微幅呢

我们就得配置一个微幅网关

那微幅网关这一块

我们来配置一下

这里面

prox下滑线pass http

这个要到我当前自己机器上来啊

因为我的项目是发布在我的机器上的

我的机器IP是192.168.0.102

哪个端口呢

8001端口

好那这一块注意写API就行了

这个是抢单操作

主要是微服务网关控制

可以了

咱们这里就搞定了

重新加载一下配置文件

那这里我们就搞定了

接着我们开始做另外一个事情

就是我们的程序测试了

那程序这一块呢

我们看一下在订单这里有一个地方有点小问题

咱们这里啊

没有给他设置抢购商品

给了整个默认的

我们不要让前端传过来

点set

total number

等于一个就行了

接着我们启动一下我们这个订单微服

好把订单微服重新启动一次

启动之后呢

我们就去进行一次测试

测试这一块呢

我们要把数据

给弄准确一点哈

好还有咱们这个热点数据发现系统的

我们也一起把它给起起来

全部给启动起来

启动起来做什么事情呢

实现热点数据的发现

那热点数据的发现

我们等会再做

来我们先执行一次抢单

那抢单地址是

lua-auto-add

加上商品ID等于

那商品ID等于多少呢?

我们先把这个订单表打开

这里所有的订单先清理掉

清理掉之后

紧接着我们来添加商品

把这个商品添加到咱们订单里面去

我们随意找一个商品吧

就这个这个商品

我们看一下好OK

我们就添加这个商品

大伙看一下哈

我点击一次提交

好提交一次

那么目前这里提升了多少呢?

我们看是否成功

这里刷新一下

看有没有订单

有订单OK

有订单了

但是还不够

我们做一个另外一个事情

再来抢购一次

大家看哈

再来抢购

又成功了

对不对

多次抢单都成功了

那说明哪里有问题了

就是这个程序里面控制部分是有问题的

但是不是我们这里解决

大家看一下哈

这一块为什么说有问题

你不是加了这个时间吗

但是你没有控制啊

不在这里控制

等会要在我们脚本中控制

所以现在这里看不到效果

但是你要看这边有没有添加对应的一个标记

刷新一次标记是有的

你看还过多少秒过期

26秒

26秒过期

二三秒

好

这是这一块

那我们这个商品如果库存不足了

我把它改一下

改成零个

改成零个

现在看还能不能下单

库存不足

对了吧

好

这是这个

那我们还做另外一个事情

让它变成热点数据

大家看哈

我让它变成热点数据

变成热点数据了

那这个时候抢单的话

咱得让他在中途休眠一会

让他在这里休眠一会

点sleep

休眠多少秒了

休眠

20秒

好了

这是这一块

休眠20秒钟

咱们输出一段话准备睡觉

后面就输出一段睡醒了

可以了

那么他一会来这里抢单的时候

就进来了

进来之进来来这里

那说明是一个非热点商品

对不对

因为我们这里也都是非热点商品啊

然后抢着抢着中途就让它变成热点的了

我们来测试一下

看这一块行不行

把这个重新启动一下

好

重新启动了

我们为当前这个商品做一个处理

把它添加成热点商品

就这个程序都启动了

接着我们再启动我们的监控系统

monitor监控

把监控系统也给启动

启动的话

这边的我们给他整一个静态页

静态页

我们看在哪个地方啊

静态页在

nosfile.locsever.yp下

items下

cp 1.html

Cp 1.html

咱儿看一下

Martineомина

咱不用这个了

换一个别的

这个正好是它换一个别的

这个

这个

等会儿我把它变成几了

éner

等会儿我要把它变成二

ayuda

er

Node

程序会自动去变

好

那这个时候我们再来操作一次

行

我们再来操作一次

cp1.html

html

好了

这是这个尾数52

尾数52

我们访问一下尾数52的页面

那么尾数52我们找一下

页面没有了

192.168

写个叫做web

137

web叫items

好

这个页面我们考一下

回车一次

一次

两次还不够

还构成不了热点商品

再来整一次

好

整之前呢

我们先去执行抢单

大家看

执行抢单

这个商品的ID不对

先执行抢单

这个时候抢

它并不是热点商品

对不对

我们抢

它会等待20秒

好

开始让它变成热点商品

好了

热点商品

我们看这一块这里是不是会

立刻有该商品了

52有了吧

好

看这里响应的是什么

它要睡20秒钟

我们看程序这里

有没有睡觉

准备睡觉

20秒睡醒了

睡醒了吧

睡醒了

我们看它干嘛了

这一块肯定是要发送我们的

对应的数据了

好

我们看

看这里有没有排队信息

这是当前用户

当前用户

我们看这里排队信息52

好

这一块

大家看一下

这一块做了个什么事情

刚才我们是不是在这里做了排队

我们总是在这里做了一个睡觉

睡觉之后到这里面去进行了一个地检

对不对

进行了个地检

我们打个断点

再来尝试一下

大家看一下

好

这个商品现在是到这来了

好

到这来了

刚才我们那一块响应的跟这有点不一样

对不对

我们看这里是怎么个操作流程

好

它一会会走这里面

走这里面

我们看一下这个商品

它这里

52是这一个

我们看它这里已经锁定了

对吧

锁定了

往这里走

好

地检

地检这一块

我们看地检的是成功还是失败

地检200

地检成功了

这个地检是成功了

地检怎么会成功呢

是不是有问题

说明我们的地检写的有问题

什么问题

这个商品它必须是没有锁定的

不然你这里写的是有不行的

商品必须是没有锁定

所以我们要更正这一个问题

在这里

DL里面

它的状态必须是没有锁定的

加个按的叫一只乐客

我们看一下这个锁定的状态

把这里打开

因为这里是比较复杂的

对不对

也是乐可变成假变成二

变成二

它必须得顶一才行

否则不让你地检锁定的是不能让你操作的

好

我们重启这个故事为服务

那么刚才这里呢

我们就不让他休眠这么多秒了

就不休眠了

因为现在这一块问题咱们是不是就知道了

热点商品

他这个时候会去发送我们对应的一个

对立信息

好

这是这一块

服务已经停了

服务停了

所以找不到这个服务了

行

咱们监控也就不要了

因为热点数据这一块

我们知道是怎么走的了吧

好

等他运行

这个服务就不管他了

因为服务已经起来了

那现在我们再来抢单

看现在会遇到什么样的情况

刚才这一块呢

是有问题的

为什么说是有问题的

因为这一块他抢单成功了

所以是有问题

而按照正常来说

他应该是抢单失败的

这个还有十几秒钟就过了

好

刷新一次

等咱们服务启动

服务人目前已经全部启动

我们接着开始再进行抢单

那么再进行抢单的时候

看一下这个数据是不是不一样了

好

这个数据应该还有几秒钟

没了

对吧

刷新一次

没了

好

开始进行抢单

抢单

抢单

哎

排队中吧

这个时候是在排队了吧

看这里

有没有数据

找不到数据了

找52这个

你看用户正在排队

第一次排队

对不对

你如果再点一次

他这里还是让你继续去排队的

大家看哈

只会排一次

不会排多次

好

无论你怎么整

他只排一次

不会排多次

这个数字在递增而已

这是这一块

我们看一下

这个数字在不停递增而已

行

这个是我们秒杀抢购的一个总体的测试

这是你的

就这样

这个

这

这个

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出：

---

### 1) 视频摘要

本视频课程聚焦于一个高并发抢购系统的实现，核心是通过 **Nginx + Lua + Redis + Spring Boot** 的技术栈来解决“秒杀”场景下的性能瓶颈和数据一致性问题。课程内容从系统架构设计开始，逐步深入到具体的代码实现，包括：

*   **Nginx 配置**：利用 `location` 指令将 `/api` 路由到后端服务，将 `/lua/order/add` 路由到 Lua 脚本，实现请求的分发和预处理。
*   **Lua 脚本**：在 Nginx 中编写 Lua 脚本 `seckill-order-add.lua`，用于处理用户请求，进行 JWT 验证、读取请求体、调用 Redis 进行库存扣减，并根据结果返回不同状态码。
*   **Redis 集群操作**：使用 `lua-resty-redis-cluster` 库操作 Redis 集群，实现分布式锁和库存减操作，确保高并发下的数据一致性。
*   **Java 服务层**：在 Spring Boot 服务中，通过 `OrderService` 实现订单创建和库存扣减逻辑，使用 `@Transactional` 确保事务一致性，并通过 `RedisTemplate` 记录用户抢购状态。
*   **数据库操作**：通过 MyBatis 的 `@Select` 和 `@Update` 注解，执行 SQL 查询和更新操作，如查询商品活动信息和更新商品库存。

整个课程通过代码演示和系统调试，展示了如何构建一个健壮、高性能的抢购系统。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:30**：课程介绍与系统架构概览，展示 Nginx 配置文件和 Lua 脚本的结构。
*   **00:30 - 01:00**：讲解 Nginx 配置，包括 `location /lua/order/add` 和 `location /api` 的路由设置。
*   **01:00 - 01:30**：演示 Lua 脚本 `seckill-order-add.lua` 的编写，包括 JWT 验证、读取请求体、调用 Redis。
*   **01:30 - 02:00**：展示 Spring Boot 服务中的 `OrderController` 和 `OrderService` 代码，实现订单创建和库存扣减。
*   **02:00 - 02:30**：演示 Redis 集群的连接和操作，使用 `lua-resty-redis-cluster` 库。
*   **02:30 - 03:00**：讲解 Java 服务中的库存扣减逻辑，包括 `@Transactional` 注解和 `RedisTemplate` 的使用。
*   **03:00 - 03:30**：展示数据库操作，通过 MyBatis 的 `@Select` 和 `@Update` 注解执行 SQL。
*   **03:30 - 04:00**：演示系统整体运行，包括 Nginx 路由、Lua 脚本执行、Java 服务处理和数据库更新。
*   **04:00 - 04:30**：总结课程内容，强调各组件的协同工作和系统性能优化。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **课程大纲**：
    *   1.2 实时热点数据分析
    *   2.1 Jwt令牌
    *   3.1 抢单分析
    *   3.2.2 Lua实现Redis操作
    *   3.3.4 下单实现

#### 代码关键内容

*   **Nginx 配置文件 (`nginx.conf`)**：
    ```nginx
    # 抢单路由
    location /lua/order/add {
        content_by_lua_file /usr/local/openresty/nginx/lua/seckill-order-add.lua;
    }

    # 服务网关
    location /api/ {
        proxy_pass http://192.168.1.5:8001;
    }
    ```

*   **Lua 脚本 (`seckill-order-add.lua`)**：
    ```lua
    local json = require "cjson"
    local jwtoken = require "token"
    local auth_header = ngx.var.http_authorization

    local result = jwtoken.check(auth_header)
    if result == false then
        ngx.say(json.encode({message = "token校验失败"}))
        ngx.exit(401)
    end

    local body = ngx.req.read_body()
    local data = json.decode(body)
    local id = data.id
    local count = data.count

    local redis = ngx.redis:new()
    redis:connect("192.168.1.5", 6379)
    local res = redis:eval(
        [[
            local key = KEYS[1]
            local value = redis.call('HGET', key, 'stock')
            if value == nil or value <= 0 then
                return "库存不足"
            else
                redis.call('HSET', key, 'stock', value - 1)
                return "抢购成功"
            end
        ]],
        1,
        "seckill:stock:" .. id
    )
    redis:close()

    ngx.say(json.encode({message = res}))
    ngx.exit(200)
    ```

*   **Java 服务代码 (`OrderService.java`)**：
    ```java
    @Transactional
    public Result add(@PathVariable(value = "id") String id, @RequestHeader(value = "Authorization") String authorization) {
        // 解析令牌
        String userKey = "USER" + order.getUsername() + id;
        Result<Sku> count = skuFeign.dcount(order.getSkuId(), order.getTotalNum());
        if (count.getCode() == StatusCode.DECOUNT_OK) {
            Sku sku = count.getData();
            order.setId("No" + idWorker.nextId());
            order.setOrderStatus("0");
            order.setPayStatus("0");
            order.setConsignStatus("0");
            order.setSkuId(sku.getId());
            order.setName(sku.getName());
            order.setPrice(sku.getPrice() * order.getTotalNum());
            orderMapper.insertSelective(order);
            redisTemplate.boundValueOps(userKey).set("抢购成功", 1, TimeUnit.MINUTES);
            return StatusCode.ORDER_OK;
        } else {
            return StatusCode.ORDER_FAIL;
        }
    }
    ```

*   **数据库操作 (`Skumapper.java`)**：
    ```java
    @Select("SELECT s.id, s.name, s.price, s.seckill_price seckillPrice, s.num FROM tb_sku_act sa LEFT JOIN tb_sku s ON sa.sku_id = s.id WHERE sa.id = #{id} AND sa.islock = 1")
    List<Sku> findSkuActivityId(String id);

    @Update("update tb_sku set seckill_num = seckill_num - #{count} where id = #{id} and seckill_num >= #{count} and islock = 1")
    int updateSkuStock(String id, Integer count);
    ```

---

### 4) 关键场景与演示描述

*   **场景一：Nginx 配置演示**
    *   **描述**：讲师在 Nginx 配置文件中添加了两个 `location` 块，一个用于处理 `/lua/order/add` 路径的 Lua 脚本，另一个用于处理 `/api/` 路径的后端服务。通过 `proxy_pass` 将请求转发到后端服务。

*   **场景二：Lua 脚本执行演示**
    *   **描述**：讲师在 Nginx 中编写并运行了 `seckill-order-add.lua` 脚本。脚本首先读取请求头中的 JWT 令牌，验证其有效性。然后，读取请求体中的商品 ID 和数量，调用 Redis 集群进行库存扣减操作，并根据结果返回相应的 JSON 响应。

*   **场景三：Java 服务处理演示**
    *   **描述**：讲师在 Spring Boot 服务中演示了 `OrderService` 的 `add` 方法。该方法首先调用 `skuFeign.dcount` 获取库存信息，然后根据库存情况决定是否创建订单。如果库存充足，创建订单并更新数据库，同时在 Redis 中记录用户抢购状态。

*   **场景四：Redis 集群操作演示**
    *   **描述**：讲师使用 `lua-resty-redis-cluster` 库连接 Redis 集群，并执行 `HGET` 和 `HSET` 操作来查询和更新商品库存。通过 Lua 脚本实现原子操作，确保在高并发下的数据一致性。

*   **场景五：数据库操作演示**
    *   **描述**：讲师通过 MyBatis 的 `@Select` 和 `@Update` 注解，执行 SQL 查询和更新操作。查询商品活动信息，更新商品库存数量，并记录用户抢购状态。

*   **场景六：系统整体运行
