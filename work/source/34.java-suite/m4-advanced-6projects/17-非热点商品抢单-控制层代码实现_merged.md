# 17-非热点商品抢单-控制层代码实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那接下来我们把这一块这个空置成这里给添加一下

好

这个是添加订单

我们写一个public result add

那你每次添加订单呢

你要给我把商品的一个ID给我传过来

你要抢单嘛

ID肯定要给我

对不对

好

写个叫password

value

那这一块我就写个get就行了

好

商品的ID给我

紧接着还有一个就是用户的一个身份识别

身份识别这一块

怎么识别呢

就是你每次要把你的请求头里面的命牌给我传过来

命牌也要给我

好

request head

这里写一个命牌

叫authorization

把它给拷过来

OK

命牌有了

接着身份识别

也就可以了

6 result

这是我们这一块

首先我们先说一下这里

你抢购这个商品

那这一块我得先识别你的身份

身份识别呢

我们可以去解析令牌就可以了

解析令牌

解析令牌之后呢

我们要封装一个order

好

我们先遛一个order

遛order

order.set

skuid

就是你抢购的商品

那么还有一些别的

比如说创建时间

credit time

new date

then set update time

等于order.get credit time

就是这一块

那解析令牌这一块怎么解析令牌呢

jwt token点

这里有一个地方是我们解析令牌的

pass token

authorization给它

行

令牌这一块

就解析了

解析了之后呢

我们写下tokenmap

可以从里面获取用户的信息

tokenmap.get

有一个叫username的

点图视镜

令牌我们就

就能从中获取到用户的名字

那接着把用户名给我们的

订单就行了

上面的username

这一块订单就搞定了

订单搞定了

紧接着我们就要去添加订单

那添加订单呢

这里也容易

直接调一下

就可以了

好

调了之后呢

那也不一定说添加订单就一定是成功的

这个是一个code的状态吗

为什么说不一定是添加订单成功呢

因为这里有很多种可能性

第一个首先这个订单这里

也有可能是真成功了

对不对

真成功了

所以说呢

其实我要判断一下

好判断一下我们当前这个code

如果是

status code

这个这就是真成功

好我们看一下啊

break

这个时候就是真正成功对不对

那我们直接

return

丢一个result

写个true

写个

200对吧

status code

写个200

20000吧

行了我们就把这个给响应出去

那这个是成功

接着

提示什么呢

提示下单成功

好了这个可以了

那也不需要break了对吧

那还有另外一种情况

万一不是下单成功了

下面这里就有失败的情况啊

如果是这个呢

这个就是库存不足了呀

对不对

库存不足怎么办

6 result

跟上面这一块

差不多的复制一下

把这个改成force

这个呢就不是ok了

这个是库存不足

库存不足了就是我们这里的405

好我们把这个给拷贝一下

405

这一块是什么呢

这一块是库存不足

行接着再往这里看

还有别的

除了库存不足之外

那这里还有一个

正在排队呢

如果是这个呢

接着写呗

接着写

是deduce code

这个是正在排队

正在排队呢并不表示出错了哈

好我们把它给写这里

这一块换成我们的

叫

order queue

正在排队

排队抢购中

行

那其他呢

default了

default了咱们就不管了

default我们给它想一个别的了

想要什么呢

这里想要force

这里

就来个

arrow

抢单发生异常

可以了

这一块就是我们这个控制层这里的一个

实现操作

行这个我们就讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Boot 的高并发订单系统中，`OrderController` 控制器如何处理“添加订单”请求。核心逻辑包括：从 HTTP 请求中提取用户身份（通过 JWT Token 解析），创建订单对象，调用服务层进行库存扣减和订单持久化，并根据业务状态返回不同的响应码和消息。视频重点演示了如何通过 `@PathVariable` 和 `@RequestHeader` 注解获取参数，如何使用 `JwtTokenUtil` 解析 JWT，以及如何在控制器中通过 `switch` 语句处理不同业务状态码（如 `ORDER_OK`, `DECOUNT_NUM`, `ORDER_QUEUE`），并返回自定义的 `Result` 对象。同时，视频也展示了服务层中如何与 Redis（用于库存和队列）和 Kafka（用于异步通知）进行交互，以实现高并发下的库存扣减和排队抢购功能。

---

### 2) 按时间顺序的章节（带时间点）

*   **0:00 - 0:15**: 开场，展示 `OrderController` 类的初始代码结构，包括 `@RestController`、`@RequestMapping` 和 `@CrossOrigin` 注解。
*   **0:16 - 0:30**: 编写 `@GetMapping` 注解的 `add` 方法，定义路径参数 `id` 和请求头参数 `Authorization`。
*   **0:31 - 0:45**: 使用 `JwtTokenUtil.parseToken(authorization)` 解析 JWT，提取用户名，并创建 `Order` 对象。
*   **0:46 - 1:00**: 调用 `orderService.add(order)` 方法，并根据返回的 `code` 值，使用 `switch` 语句判断业务状态。
*   **1:01 - 1:15**: 展示 `switch` 语句中不同 `case` 分支的处理逻辑，包括成功、库存不足、排队抢购等场景。
*   **1:16 - 1:30**: 展示服务层 `OrderServiceImpl` 的代码，重点是库存扣减逻辑（`skuFeign.count`）、Redis 操作（`boundValueOps`）和 Kafka 消息发送（`kafkaTemplate.send`）。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **控制器层 (`OrderController.java`)**:
        ```java
        @GetMapping(value = "/{id}")
        public Result add(@PathVariable(value = "id") String id, @RequestHeader(value = "Authorization") String authorization) {
            // 解析令牌
            Map<String, Object> tokenMap = JwtTokenUtil.parseToken(authorization);
            String username = tokenMap.get("username").toString();
            // 封装订单
            Order order = new Order();
            order.setSkuid(id);
            order.setCreateTime(new Date());
            order.setUpdateTime(order.getCreateTime());
            order.setUsername(username);
            // 添加订单
            int code = orderService.add(order);
            // 返回结果
            switch (code) {
                case StatusCode.ORDER_OK:
                    return new Result(true, StatusCode.ORDER_OK, "下单成功！");
                case StatusCode.DECOUNT_NUM:
                    return new Result(false, StatusCode.DECOUNT_NUM, "库存不足！");
                case StatusCode.ORDER_QUEUE:
                    return new Result(true, StatusCode.ORDER_QUEUE, "排队抢购中！");
                default:
                    return new Result(false, StatusCode.ERROR, "抢单发生异常！");
            }
        }
        ```
    *   **服务层 (`OrderServiceImpl.java`)**:
        ```java
        // 1. 递减库存
        Result<Sku> count = skuFeign.count(order.getSkuid(), order.getMemberId());
        if (count.getCode() == StatusCode.DECOUNT_OK) {
            // 2. 下单
            order.setOrderId("No" + idWorker.nextId());
            order.setOrderStatus("0");
            order.setPayStatus("0");
            order.setConsignStatus("0");
            order.setSkuid(order.getSkuid());
            order.setSkuName(order.getSkuName());
            order.setPrice(order.getPrice());
            orderMapper.insertSelective(order);
            // 3. 记录当前用户抢购的时间点，24小时内不能再次抢购
            redisTemplate.boundValueOps(userKey).set("order", order.getCreateTime(), 24, TimeUnit.HOURS);
            redisTemplate.boundValueOps(userKey).expire(timeout, TimeUnit.SECONDS);
            return StatusCode.ORDER_OK;
        } else {
            // 3. 递减失败
            if (count.getCode() == StatusCode.DECOUNT_NUM) {
                return StatusCode.DECOUNT_NUM;
            } else if (count.getCode() == StatusCode.DECOUNT_OK) {
                // 2/5商品热点
                String key = "SKU_" + order.getSkuid();
                Long increment = redisTemplate.boundListOps(key).rightPush(order.getSkuid());
                if (increment == 1) {
                    // 执行排队
                    Map<String, String> queueMap = new HashMap<>();
                    queueMap.put("id", order.getSkuid());
                    kafkaTemplate.send(topic, order.getSkuid());
                    return StatusCode.ORDER_QUEUE;
                }
            }
        }
        ```

*   **关键注解**:
    *   `@RestController`: 将控制器方法的返回值直接作为 HTTP 响应体。
    *   `@RequestMapping`: 定义控制器的请求路径。
    *   `@GetMapping`: 用于处理 HTTP GET 请求。
    *   `@PathVariable`: 从 URL 路径中提取参数。
    *   `@RequestHeader`: 从 HTTP 请求头中提取参数。
    *   `@Autowired`: 自动注入依赖的 Bean。

---

### 4) 关键场景与演示描述

*   **场景一：控制器方法创建与参数绑定**
    *   **描述**: 讲师在 `OrderController` 中创建了一个 `@GetMapping` 方法，用于处理 `/order/{id}` 路径的请求。通过 `@PathVariable` 注解绑定 URL 中的 `{id}` 参数，并通过 `@RequestHeader` 注解绑定 `Authorization` 请求头。
    *   **演示**: 屏幕上显示了注解的完整代码，并通过 IDE 的自动补全功能展示了可用的注解。

*   **场景二：JWT Token 解析与订单封装**
    *   **描述**: 讲师在方法体内使用 `JwtTokenUtil.parseToken(authorization)` 解析 JWT，提取出用户名。然后创建一个 `Order` 对象，并设置其 `id`、`createTime`、`updateTime` 和 `username` 属性。
    *   **演示**: 代码逐行展示，IDE 的自动补全功能帮助选择 `JwtTokenUtil` 类和 `Order` 类。

*   **场景三：服务层调用与状态处理**
    *   **描述**: 讲师调用 `orderService.add(order)` 方法，并根据返回的 `code` 值，使用 `switch` 语句判断业务状态。根据不同的状态码，返回不同的 `Result` 对象，包含成功、失败或排队等信息。
    *   **演示**: 代码中 `switch` 语句的 `case` 分支被高亮显示，展示了不同状态码对应的返回信息。

*   **场景四：服务层库存扣减与队列处理**
    *   **描述**: 讲师展示了服务层的代码，其中首先通过 `skuFeign.count` 调用远程服务进行库存扣减。如果库存充足，则创建订单并写入数据库。如果库存不足，则返回相应的状态码。如果库存充足但商品是热点商品，则将其加入 Redis 队列，并通过 Kafka 发送消息，实现排队抢购。
    *   **演示**: 屏幕上显示了 `skuFeign.count` 的调用、Redis 的 `boundValueOps` 操作和 Kafka 的 `send` 方法。

---

以上是根据视频画面进行的结构化分析，旨在提供清晰、准确的技术理解。
