# 16-非热点商品抢单-下单业务层代码实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

库存递减这里我们就搞定了

那接下来我们就开始实现下单了

下单这一块呢

由于商品在下单过程中可能会变成热点商品

那变成热点商品呢

那这一块我们就要开始去用到卡夫卡了

要往卡夫卡里面发送排队的信息

所以这个时候我们把这个订单系统打开

在这里添加上我们的卡夫卡配置信息

这一块就是卡夫卡的配置信息

把它给加过来

这一块呢

分别配置了我们的生产者和消费者这一块

好

那这里有一个地方大家要去改一下

就是当前生产者所对应的服务地址

卡夫卡server9092

还有消费者所对应的服务地址

卡夫卡server9092

这是这一块大家需要去改的地方

紧接着我们就去实现下单了

那下单的话就是添加订单

这几个地方是跑不掉的

业务层我们在这里写一个添加订单

int add

那你要把订单给我order

好了

接着写这一块的实现

这一块就是我们的添加订单

怎么做呢添加订单

添加订单要先递减库存

库存递减之后

那有可能递减成功啊

也有可能递减失败啊

递减成功

那这个时候就要下单了

下单的时候还要注意另外一个事情

不是下单就完成了

还要记录当前用户抢单的

抢单的时间点

也就是24小时内

不能抢购该商品

好这是这一块

那没准递减也有失败的可能性呢

那么递减失败

我们就要分析失败的原因

对不对

那失败的原因有哪些原因呢

第一是库存不足

第二是热点商品的

好还有一个

200呢

200是上面的

还有另外一种情况

0反过来是0

0怎么办呢

0这个时候就不处理了

服务器异常

其实一般是数据有问题

0我们就不管了

好这是这一块

或者你是0的商品

0的时候你提示给别人

数据异常

你也可能不能提数据异常

对吧

你只能说抢购人数多什么的

好这是这一块

我们来实现一下这个整体的操作流程

先把我们的SKU份注入进来

注入进来之后呢

再来实现库存递减

好库存递减decount

把当前这个商品的ID给他

还有一个是

用户抢购的个数也要给他

叫做total number

这是抢购的个数

紧接着我们看递减的一个情况

叫decount result

要写个SKU

注意返回的是SKU

那这里我们把它给加上去

写个SKU

因为递减成功是需要去查询数据的

所以我们这里要给他写一个SKU

把这一块打开加上去

好

我们看一下这一块

这里呢

给他整个SKU

行了

这里6的时候也要给他整个范形

SKU

OK了

这是我们这里

行

接着我们来看

这个数量是否大于0呢

抢购库存递减是否成功呢

我们就要判断一下了

如果此时decount.getcode

我们说过是code了

恒对200

那就是成功

status code.200

那这就是成功

成功了我们就要开始下单了

下单呢

我们还要记录当前这个商品用户买过了

二十四小时不能再买

对吧

否则就是我们的失败

失败这一块该怎么办呢

我们来看一下

先说说405吧

405失败

那就是失败了呗

库存不足

好还有个就是

商品变热点

还有个0

0呢是数据有问题

流程我们清楚了

接着我们按照流程来实现我们的操作

首先下单这一块

下单呢

我们就要看一下我们的订单表结构

把订单表打开

在这一块

订单表这里面我们看看有哪些列

第一个ID列

这就不用说了

主件ID

第二个total number抢购的数量

并不是说商品用户永远只能抢一个

秒杀的时候也有可能能抢两个的

这是这一块

接着后面的支付类型我就不管了

还有一个是订单创建时间订单修改时间

这个比较容易

一会要管这两个

好再往后面继续看

还有付款时间我们不管它

发货时间交易完成时间

交易关闭时间

收货人这个也不管

到后面这个

订单状态是要管的

支付状态也要管

这些是要管的

OK

后面还有几个

第一个是sku ID

就是商品ID

name呢

商品名称

price呢

当前你购买的商品的总价格

username这个订单是谁的

那像这些是要完善的

好

我们开始去创建一个订单对象

然后完善这些数据

在这一块6

order上面已经有对吧

我们只需要继续完善就行了

点set ID

那要把ID work给注入进来

private ID work

把它给注入进来就可以了

好了

首先第一个来实现一下ID的设置

no加上ID work

next id

还有什么呢

创建时间

修改时间

创建时间

修改时间

你时间给我传过来得了

好

另外还有这里是什么

这里是订单状态

状态我们写几了

肯定是未完成

写0就行了

除了状态

还有支付状态

也写0就完了

好

0是表示未支付

点set

还有发货状态

那肯定是不可能发货了吧

对吧

这是这一块

这个都写完了

那还有一个是我们这里有skuid

name price username

这个怎么做呢

order.set username

我们从订单里面去获取就行了

它那边会传过来

所以我这里就不用管了

但是还有商品的信息呢

商品的信息

它这里的data正好是sku

sku等于dcount.getData

这是这一块

我们这个时候就可以给它把商品的信息填充进去了

第一个是商品的ID

点getID

好了

除了商品ID还有价格

点setname

点getname

这个搞错了

order

order.get.set

还有一个是price

getprice

price应该要乘以谁呢

要乘以你当前的价值呢

点这里抢购的数量

点gettotal number

那这一块这个就搞定了

搞定了之后我们就可以把它添加到我们数据库去了

好

让我们添加一下

order map.insertselective

order给它

那这一块这个抢单就搞定

紧接着还有

那用户抢单抢是抢了

那不能接着再抢吧

对不对

那于是我们就要开始定义一下这个项目

我们可以把这个项目定义一下

它抢单的标识了

抢单的标识怎么做呢

我们可以把它存储到我们ready的缓存去

让它在一段时间内自动消失就可以了

说白了就是给它添加到我们ready的缓存

设置一个过期时间呗

行

我们来整一下

在这里写一个key

key等于user id

这一块user是user id是id

我们把用户的users id是id

我们把用户的users id是id

我们把用户的users id是id

我们把用户的users id是id

我们先把用户给加上去

点getusername

id是商品it

order.getskuid

这是这一块

这个商品id在这里还不好总

在这里还不好总

在下面才有对不对

在下面才会有这个商品

像这是这一个

我写个user key

好了用户的key有了

key有了之后呢

紧接着把它存到redis缓存区就可以了

把redistemplate注入进来

注入进来之后呢

我们再来看

好注入进来之后呢

我们开始把它添加到我们redis里面去

我们就不写别的了

bond value吧

user key

随便给它一个数据

先给它一个数据

数据就给个空吧

只要有这个key存在就行了

有这个key存在那就没有问题

接着给它一个过期时间

过期时间呢

我们就给个一分钟

正常来说肯定不是一分钟

我们这里就给个一分钟

就可以了

因为我们是测试环境嘛

好这一块就搞定了

紧接着这个时候我们返回什么数据呢

我们要返回一个200

return

status code

点200哈

order ok 200

行了

这个是普通抢单的一个最基础流程

接着我们看下面这里库存递减失败的问题了

那库存递减失败这里事情就多了

首先第一个库存不足

那库存不足那就直接返回库存不足呗

status

code

.

库存不足返回405

就这一个

那热点商品这个怎么办呢

热点商品这个事情就多了

热点商品

哎我还没有写判断是吧

if

我们写一下判断哈

叫我们看一下

dcount

.getcode

横等于405

.405

那这就是库存不足

库存不足就直接把这个库存不足的

给返回过去就可以了

elseif

如果不是405怎么办呢

那有可能是205

205是商品变成热点商品了

对不对

那热点商品我们看一下

205

热点商品我们该干嘛呢

热点商品你就要去排队了

这个时候要去排队

排队这一块呢也简单哈

这一块好我们看一下

呃

这里面应该是已经有商品的ID

我们把它给挪出去得了

这个key挪到外面去

挪到外面去

因为一会也要用到它

好

挪到这里

来我们看这个成为热点商品

这个时候怎么办呢

热点商品的话

那它的信息一定会在这里存在的

在这儿存在

因为热点商品会跑到我们ready的缓存区

对不对

好

那它在这里我们该怎么办呢

我们首先看一下

用这个热点商品的话

我们首先看一下

用户有可能正好在这里抢这个商品呢

有可能有了

对不对

那这个时候怎么办呢

我们做这么一个事

用户在这里抢购这个商品

他如果正在排队

我给他一个key

给他一个key

就是刚才我说的user key

这个key给他

然后后面给他整一个值

那个值如果是1表示用户正在排队

如果这个时候大于1

表示用户已经排队了

已经在排队了

你就不要再排了

对不对

不要重复排队

好

我们来整一下

我先写一个key

key等于

为什么要写个key呢

因为我们操作的是它里面的数据

前面这个是不是个key

好

我写一下

sku-

加上order.get

sku id

这是这个key

紧接着我们看一下用户的数据

用户有没有在排队

readist.bondhc

key给他

点increment

这个user key

递增1

我们看一下递增之后的值

刚开始排队

如果没有排

你递增1

它的值返回给你是1

那就说明没有问题

那你这是第一次排队

但如果返回的值是大于1

那说明你这是第N次排队

这个商品第N次排队

那是不行的

好

所以这里我们要判断一下

如果此时排队的很等于1

那说明可以排队

那说明可以排队

你现在就可以抢够这个商品了

那就执行排队了

好

这是这一块

否则呢

否则没关系

你也在排队

对不对

否则没关系

你仍然在排队

所以没事

这一块

我给它加一个状态

订单状态

这里还有个202

这个是抢够商品正在排队

那是Statues Code.

正在排队

好了

紧接着我们来做这个事情

就是执行排队的操作

那么执行排队的操作

用到一个对象

叫卡夫卡

template

用到它了

注入进来

注入进来之后

用它去实现

消息的发送就行了

来消息发送

是什么

第一个是topic

第二个是消息

topic叫new order

消息也很简单

消息就是你抢单的消息

我给个map

string

叫qmap

new hash map

好

给个string

给个string

接着往里面添加数据就行了

put一下

key给什么

首先我给个

你当前抢单这一块

我给个用户的名字username

username

order.getusername

我还可以给他一个ID

就是你抢的商品ID

因为我要根据你这里来执行下单的

所以你要把数据给我给全了

对吧

好

再把map给塞进去

json.

转成json.zfchuan

接上字符串了

好了

OK

这个消息就发送成功了

并且注意

消息发送成功了

并且我们上面这里已经给他记录了排队标识

对不对

但是还有另外一个现象

还有另外一个问题

就是他这里商品没有抢购成功

所以说像上面这里有一个标识记录

我们这里暂时就不用了

OK

好

如果这个时候这里大家看

如果这里抢单是成功

走这个

如果抢单没有成功

走下面这里

如果这里走了

这里走了

这里走了

都没有执行

怎么办

就返回个0得了

返回个0

或者返回你这里对应的一个状态码都可以

点get code

好

这是这一块

这整个就是我们的一个抢单操作流程

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个高并发抢购系统（秒杀系统）的开发教学。核心内容是演示如何在订单服务中，通过调用商品服务的 Feign 客户端来实现库存扣减，并在扣减失败时，利用 Redis 的分布式锁和消息队列（Kafka）来处理“热点商品”和“库存不足”的场景，以保证数据一致性并提升系统吞吐量。视频主要展示了 `OrderService` 中 `add` 方法的完整实现逻辑，包括库存扣减、订单创建、Redis 分布式锁、以及失败后的队列处理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示 `SkuFeign` 接口，定义了两个核心方法：`dcount` 用于库存递减，`hotIsolation` 用于热点商品隔离。
*   **00:06 - 00:10**: 展示 `OrderService` 接口，定义了 `findPage` 方法，用于分页查询订单。
*   **00:11 - 00:15**: 展示 `OrderService` 的实现类 `OrderServiceImpl`，重点是 `add` 方法的开始部分，用于处理下单逻辑。
*   **00:16 - 00:20**: 展示 `OrderServiceImpl` 中的 `add` 方法，调用 `skuFeign.dcount` 进行库存扣减，并根据返回结果进行分支处理。
*   **00:21 - 00:25**: 展示 `OrderServiceImpl` 中的 `add` 方法，成功扣减后，创建订单对象并调用 `orderMapper.insertSelective` 插入数据库。
*   **00:26 - 00:30**: 展示 `OrderServiceImpl` 中的 `add` 方法，创建订单后，设置订单状态、用户信息，并使用 `redisTemplate.boundValueOps` 设置 Redis 分布式锁。
*   **00:31 - 00:35**: 展示 `OrderServiceImpl` 中的 `add` 方法，失败时（库存不足或商品是热点），使用 `redisTemplate.boundHashOps` 执行队列操作。
*   **00:36 - 00:40**: 展示 `OrderServiceImpl` 中的 `add` 方法，失败时，将订单信息放入队列，并返回相应的状态码。
*   **00:41 - 00:45**: 展示 `StatusCodes` 类，定义了各种状态码，如 `DECOUNT_OK`、`DECOUNT_HOT`、`DECOUNT_NUM` 等。
*   **00:46 - 00:50**: 展示 `OrderServiceImpl` 中的 `add` 方法，处理失败情况时，使用 `queueMap` 进行队列操作。
*   **00:51 - 00:55**: 展示 `OrderServiceImpl` 中的 `add` 方法，最终返回 0，表示操作完成。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   未在画面中展示 PPT 或图表。
*   **公式**:
    *   未在画面中展示数学公式。
*   **代码**:
    *   **`SkuFeign.java` 接口**:
        ```java
        @FeignClient(value = "seckill-goods")
        public interface SkuFeign {
            @PutMapping(value = "/dcount/{id}/{count}")
            Result dcount(@PathVariable(value = "id") String id, @PathVariable(value = "count") Integer count);

            @PostMapping(value = "/sku/hot/isolation")
            Result hotIsolation(@RequestParam List<String> ids);
        }
        ```
    *   **`OrderService.java` 接口**:
        ```java
        public interface OrderService {
            PageInfo<Order> findPage(Order order, int page, int size);
        }
        ```
    *   **`OrderServiceImpl.java` 实现类**:
        ```java
        @Override
        public int add(Order order) {
            // 1. 递减库存
            Result<Sku> dcount = skuFeign.dcount(order.getSkuId(), order.getTotalNum());
            // 2. 递减成功-->记录当前用户抢单的时间点，24小时内不能抢购该商品
            if (dcount.getCode() == StatusCode.DECOUNT_OK) {
                Sku sku = dcount.getData();
                // 下单
                order.setOrderId(IdWorker.nextId());
                order.setOrderStatus("0");
                order.setConsignStatus("0");
                order.setPayStatus("0");
                order.setSkuId(sku.getId());
                order.setSkuName(sku.getName());
                order.setPrice(sku.getPrice());
                orderMapper.insertSelective(order);
                // 记录当前用户抢单的时间点，24小时内不能抢购该商品
                String userKey = "USER" + order.getUsername() + "_" + order.getSkuId();
                redisTemplate.boundValueOps(userKey).expire(1, TimeUnit.MINUTES);
                return StatusCode.ORDER_OK;
            } else if (dcount.getCode() == StatusCode.DECOUNT_HOT) {
                // 205商品热点
                String key = "SKU_" + order.getSkuId();
                Long increment = redisTemplate.boundHashOps(key).increment(userKey, 1);
                if (increment == 1) {
                    // 执行排队
                    Map<String, String> queueMap = new HashMap<String, String>();
                    queueMap.put(String.valueOf(order.getId()), order.toString());
                    redisTemplate.boundHashOps(key).putAll(queueMap);
                    return 0;
                }
                return 0;
            } else if (dcount.getCode() == StatusCode.DECOUNT_NUM) {
                // 405库存不足
                return StatusCode.DECOUNT_NUM;
            } else {
                // 205商品热点
                String key = "SKU_" + order.getSkuId();
                Long increment = redisTemplate.boundHashOps(key).increment(userKey, 1);
                if (increment == 1) {
                    // 执行排队
                    Map<String, String> queueMap = new HashMap<String, String>();
                    queueMap.put(String.valueOf(order.getId()), order.toString());
                    redisTemplate.boundHashOps(key).putAll(queueMap);
                    return 0;
                }
                return 0;
            }
        }
        ```
    *   **`StatusCodes.java` 状态码类**:
        ```java
        public static final int ERROR = 20000; // 失败
        public static final int LOGINERROR = 20002; // 用户名或密码错误
        public static final int ACCESSERROR = 20003; // 权限不足
        public static final int REMOTEERROR = 20004; // 远程调用失败
        public static final int REPEERERROR = 20005; // 重复操作
        public static final int NOTFOUNDERROR = 20006; // 没有对应的抢购数据

        // 库存状态码
        public static final int DECOUNT_OK = 200; // 递减成功
        public static final int DECOUNT_NUM = 405; // 库存不足
        public static final int DECOUNT_HOT = 205; // 商品是热点商品
        public static final int DECOUNT_OK = 200; // 库存递减成功
        public static final int ORDER_QUEUE = 202; // 抢购商品正在排队
        public static final int ORDER_OK = 200; // 抢单成功
        ```

---

### 4) 关键场景与演示描述

*   **场景一：库存扣减与订单创建** (00:16 - 00:25)
    *   **演示**：在 `OrderServiceImpl` 的 `add` 方法中，首先调用 `skuFeign.dcount` 进行库存扣减。如果扣减成功（返回状态码 `DECOUNT_OK`），则创建一个 `Order` 对象，设置其 ID、状态、价格等属性，并调用 `orderMapper.insertSelective` 将订单插入数据库。
*   **场景二：Redis 分布式锁** (00:26 - 00:30)
    *   **演示**：在订单成功创建后，代码会生成一个用户-商品的唯一键（如 `USER_用户名_商品ID`），并使用 `redisTemplate.boundValueOps(userKey).expire(1, TimeUnit.MINUTES)` 设置一个 1 分钟的过期时间，以此来防止同一用户在 24 小时内重复抢购。
*   **场景三：热点商品处理** (00:31 - 00:35)
    *   **演示**：如果商品是热点商品（返回状态码 `DECOUNT_HOT`），系统会使用 `redisTemplate.boundHashOps(key).increment(userKey, 1)`
