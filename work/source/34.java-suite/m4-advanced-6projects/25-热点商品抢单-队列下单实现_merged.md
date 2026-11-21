# 25-热点商品抢单-队列下单实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那这一块我们已经实现了热点商品抢单

但是热点商品抢单之后呢

我们还要给它下单才行

所以我们这一块紧接着就要开始去实现下单了

那下单这里我们在这儿新建一个消费对象

Kafka

Order

Listener

这一块呢给它加一个Completing

然后在里面我们可以写一个消费的方法

叫GetMessage

那每次要把消息给消费过来

这上面加上一个KafkaListener注解

这里面把对应的一个对列给写上去

对列呢我们叫New Order对列

好这个是消费

这个是订单消费

消费之后呢

我们要把这个商品对应的一个订单给下单了

好这个是

这个是下单信息

我们把它转成

一个Map

String

Object

好这个我们可以写成String

String得了

这个叫

OrderMap

等于我们json.passObject

我们把它解析成一个Map对象

Map.class

行

这个对象有了

那么它里面呢

我们之前说过有ID有UserName对不对

那我们接着开始做另外一个事

就是下单操作了

那么下单操作呢

我们在这里写一个叫热点商品下单

那怎么下单呢

写个int hot add

那你要把刚才那个数据给我传过来

String Automap

好我们来开始实现热点商品下单了

那么这一块热点商品下单呢

应该是比较简单的了

下单这一块该怎么下单

我们来简单说一下哈

好

好

,那首先第一个我们要确定

一会要操作Redis缓存的Key有哪些

我们先把这个Key给准备一下

sku-

加上ID对不对

还有一个是UserKey

这些Key是一定会操作的

UserKey这里的是UserID

好我们开始获取对应的数据

先说说第一个用户的名字

UserName等于OrderMap

点Get

UserName

除了这个之外还有一个是商品的ID

ID这里面也就是ID

这个是这一块的获取数据

ID正好加过来

于是Key就有了

UserName也正好加过来

好再加上ID

那么现在这里操作缓存的两个Key就有了

Redis中对应的Key

好Key有了之后

我们就开始去下单

前提是当前这个商品在我们的Redis缓存

我们来判断一下

如果Key在Redis缓存

则表示商品信息在Redis中进行操作

那进行操作怎么操作呢

如果在里面的话

那我第一个步骤是不是要创建订单呢

对吧

Order创建了

紧接着做什么事呢

我们创建下一个步骤

我们就要开始去做另外一个事情

要让我们的Redis中对应的Number递减

这个是一方面

它要递减之后还有别的事情也要操作

除了递减之外

我还要记录你当前用户购买过该商品

记录用户购买过该商品

该商品大概多久了

24小时后过期对不对

这是这一个

除了24小时过期

这里还要做另外一个事

清理用户排队信息

因为当前用户在该商品抢购过程中排过队了

这个时候要把它清理

好

我们按照这几个流程来实现就可以了

行

来开始操作

if RedisTemplate.

.redisTemplate.

.redisTemplate.

.redisTemplate.

如果有这个key

我们就按照这些来操作就OK了

创建订单

New

大套

这一块东西很多

下面这里有一部分

我们就直接按这个来参考一下就可以了

参考一下这一部分

商品ID的那一块有

用户的名称

好

这是这个价格

对吧

对吧

那当前这个商品

我们是不是得查出来

把它查出来

SKU

等于SKU map

好我们这里没有它

那我们这里

行这个是价格这一块

那咱们这里要用到

这个商品的信息

所以我们得把它查出来

SKU份

等于SKU份.fundbyid

ID给它当前这个商品

就查询到了

那这一块咱们得用另外一个

叫做result

里面是SKU

行

这一个

接着我们可以获取SKU

等于SKU result

getData

好那接着这里面的数据就OK了

商品名称.getName

价格都有了

对不对

这些都有了

好除了这些

还有时间这一块

我们要创建一下

auto.sql

creditTime

multi

order.set

updateTime

点get

creditTime

好这里就基本上就完成了

基本上完成了之后呢

我们接着看下面这里

要ready中对应的numbr要递减

对不对

那么这个numbr我们现在还没有获取

我们获取一次

在这里获取一下商品的数量

怎么做呢

我们写一下

ready是template

bond哈希

我们写一下

ready是template

bond哈希

我们写一下

bond哈希

我们写一下

bond哈希

我们写一下

bond哈希

我们写一下

bond哈希

bond哈希

p给它点

p给它点

这一块我们写get

这一块我们写get

get谁呢

get谁呢

numbr

点图是g

点图是g

点图是g

然后不要忘了把它转成int类型

然后不要忘了把它转成int类型

可以了

这个是我们的数量

这个是我们的数量

等于

等于

数量有了

紧接着这个数量要递减

紧接着这个数量要递减

我们递减一次

我们递减一次

在这里开始递减

在这里开始递减

numbr

减减

减了之后呢

用户的一个信息

我们先清理一下

用户在这里

用户在这里

它有一个排队的信息

它有一个排队的信息

大家看一下

在这里有个排队的信息

在这里有个排队的信息

要把后面这个值换成0

要把后面这个值换成0

好

我们把它这个值换成0

好

我们把它这个值换成0

map

map

存储到一个map里面去

map存储到一个map里面去

object

object

object

叫

allmap

allmap

allmap

luhashmap

luhash map

luhash map

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

string object

接着我们还要做另外一个事情,

就是用户购买的记录要给它设置一下,

用户购买的记录,

ready is time的点,

bound value,

当前对应的user key,

点,set,

随便给个值,

这一块我们需要让它在指定时间内要过期,

好,

指定时间内我们需要它过期的,

多久呢,

我们写个一分钟,

写个一分钟,

行,

这一块就搞定了,

这个整个逻辑就是这样子实现,

那这一块我们来说一下,

这里我们应该还要判断一下,

number大于0的时候,

只有它大于0的时候才会执行相关的操作,

好,

这个地方我们就不返回参数了,

这个就不返回int了,

wait,

这个最后这个可以去掉了,

那么它的接口里面也可以去掉了,

写个wait,

OK了,

到目前为止,

这一块全都搞定,

搞定了之后呢,

这边只用去调用一下就行了,

把它注入进来,

叫做autoservice,

直接给注入进来,

注入进来之后,

我们开始去调用一次,

下单操作,

点add,

下面这个automap给它,

行,

这一块我们就整体搞定,

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段为一个关于“秒杀系统”开发的技术教程，主要使用 IntelliJ IDEA 作为开发环境，演示了如何在订单服务中实现基于 Redis 的库存扣减和订单创建功能。核心内容包括：
- **技术栈**：Java、Spring Boot、Redis、Kafka、MyBatis。
- **核心功能**：实现一个“热点商品下单”接口，该接口会先检查 Redis 中的库存数量，如果库存不足则直接返回，否则创建订单并更新库存。
- **关键流程**：`hotAdd` 方法 -> 检查 Redis 库存 -> 创建订单 -> 更新 Redis 库存。
- **技术亮点**：展示了如何使用 `RedisTemplate` 进行 Redis 操作，如何通过 `@KafkaListener` 消费 Kafka 消息并调用服务方法，以及如何使用 `@Autowired` 注入服务。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节根据画面内容和逻辑顺序进行划分：

- **00:00 - 00:05**：视频开场，展示 IntelliJ IDEA 的主界面，项目结构为 `seckill-order`，并提示用户可以使用 `Ctrl+Shift+N` 快捷键查找文件。
- **00:05 - 00:15**：进入 `KafkaOrderListener.java` 文件，展示如何使用 `@KafkaListener` 注解监听 Kafka 主题 `neworder`，并调用 `orderService.add` 方法。
- **00:15 - 00:25**：切换到 `OrderServiceImpl.java` 文件，展示 `hotAdd` 方法的实现，该方法用于处理热点商品的下单请求。
- **00:25 - 00:35**：在 `hotAdd` 方法中，首先从传入的 `orderMap` 中获取用户名和商品 ID，并构造 Redis 的 key。
- **00:35 - 00:45**：检查 Redis 中是否存在该 key，如果存在，则获取库存数量。
- **00:45 - 00:55**：如果库存数量为 0，则直接返回 0，表示库存不足。
- **00:55 - 01:05**：如果库存大于 0，则创建一个 `Order` 对象，并设置其属性。
- **01:05 - 01:15**：调用 `orderMapper.insertSelective(order)` 将订单插入数据库。
- **01:15 - 01:25**：更新 Redis 中的库存数量，使用 `redisTemplate.boundHashOps(key).putAll(allMap)`。
- **01:25 - 01:35**：记录用户购买商品的过期时间，使用 `redisTemplate.boundHashOps(userKey).put("expire", System.currentTimeMillis() + 24 * 60 * 60 * 1000)`。
- **01:35 - 01:45**：返回 0，表示操作成功。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### 代码关键内容

- **`KafkaOrderListener.java`**：
  ```java
  @Component
  @KafkaListener(topics = "neworder")
  public class KafkaOrderListener {
      @Autowired
      private OrderService orderService;
      
      public void getMessage(String message) {
          // 解析消息
          Map<String, Object> orderMap = JSON.parseObject(message, Map.class);
          // 调用服务方法
          orderService.hotAdd(orderMap);
      }
  }
  ```

- **`OrderServiceImpl.java`**：
  ```java
  @Override
  public int hotAdd(Map<String, String> orderMap) {
      String username = orderMap.get("username");
      String id = orderMap.get("id");
      
      // Redis中对应的key
      String key = "SKU_" + id;
      String userKey = "USER_" + username + "_ID" + id;
      
      // 如果key在redis缓存, 则表示商品信息在Redis中进行操作
      if (redisTemplate.hasKey(key)) {
          // 获取商品数量
          Integer num = Integer.parseInt(redisTemplate.boundHashOps(key).get("num").toString());
          
          // 如果库存为0，直接返回
          if (num <= 0) {
              return 0;
          }
          
          // 创建订单
          Order order = new Order();
          order.setCreateTime(new Date());
          order.setUpdateTime(order.getCreateTime());
          order.setId("No" + idWorker.nextId());
          order.setOrderStatus("0");
          order.setPayStatus("0");
          order.setConsignStatus("0");
          order.setUserId(id);
          order.setSkuId(id);
          order.setSkuName(sku.getName());
          order.setPrice(sku.getPrice() * order.getTotalNum());
          orderMapper.insertSelective(order);
          
          // 更新Redis中的库存
          Map<String, Object> allMap = new HashMap<String, Object>();
          allMap.put("num", num - 1);
          redisTemplate.boundHashOps(key).putAll(allMap);
          
          // 记录用户购买商品，24小时后过期
          redisTemplate.boundHashOps(userKey).put("expire", System.currentTimeMillis() + 24 * 60 * 60 * 1000);
          
          return 0;
      }
      
      return 0;
  }
  ```

#### 公式与图表

- **无公式**：视频中未出现任何数学公式。
- **无图表**：视频中未出现任何图表或流程图。

---

### 4) 关键场景与演示描述

- **场景一：项目结构展示**（00:00 - 00:05）
  - **描述**：视频开始时，展示了 IntelliJ IDEA 的项目结构，`seckill-order` 项目包含 `main`、`test`、`resources` 等目录，以及 `pom.xml`、`bootstrap.yml` 等配置文件。
  - **技术点**：展示了项目的整体结构，为后续代码开发提供上下文。

- **场景二：Kafka 消费者实现**（00:05 - 00:15）
  - **描述**：切换到 `KafkaOrderListener.java` 文件，展示了如何使用 `@KafkaListener` 注解监听 Kafka 主题 `neworder`，并调用 `orderService.hotAdd` 方法。
  - **技术点**：演示了如何使用 Kafka 进行消息消费，以及如何将消息传递给服务层。

- **场景三：订单服务实现**（00:15 - 01:35）
  - **描述**：在 `OrderServiceImpl.java` 文件中，逐步演示了 `hotAdd` 方法的实现过程，包括检查 Redis 库存、创建订单、更新库存等步骤。
  - **技术点**：演示了如何使用 `RedisTemplate` 进行 Redis 操作，如何创建和设置 `Order` 对象，以及如何使用 MyBatis 的 `insertSelective` 方法插入数据库。

- **场景四：多窗口展示**（00:45 - 00:55）
  - **描述**：视频中出现了一个多窗口的展示，包括 IntelliJ IDEA、Postman、Redis Desktop Manager、Terraform 等工具的界面。
  - **技术点**：展示了开发过程中可能用到的多种工具，为读者提供更全面的开发环境参考。

- **场景五：代码调试与运行**（01:35 - 01:45）
  - **描述**：视频最后，展示了 `hotAdd` 方法的完整实现，并返回 0，表示操作成功。
  - **技术点**：演示了如何通过代码实现业务逻辑，并返回结果。

---

以上是根据视频画面进行的结构化技术分析报告。
