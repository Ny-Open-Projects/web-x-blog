# 26-热点商品抢单-测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,这里还有个小问题,就是我们这一块这个商品数量递减的时候,如果这个数量为0了,没有了,那我们需要把它同步到数据库去。

这一块呢,我们来写一下,如果此时我们的number横等于0,那么这个时候我们要同步一下,sku分点,有个方法zero,这个方法会把那个商品库存数量换成0,这是这一块。

好,我们开始来测试一下这个整体的,还有一个问题,就是咱这里这个数量呢,我们是默认是1的,但是我们没有给它值,这里我们给个值,点set,total number等于1,我们这里只允许去购买一个商品,所以这里是1哈。

行,我们开始启动我们的各大微服务,开始进行测试,这一块呢,我们把这三个一起启动。

启动之后,我们就找一下。

我们就找一个商品进行测试,这一块是排过队的,把这个排队给干掉,不要了。

把这个商品的ID给复制过去,对这个商品进行抢购,那么抢购呢,一会儿我们要看一下相关的参数哈,好,把它换掉。

那么我们一会儿要看什么参数呢,我们先简单介绍一下。

等会儿抢购的时候,这个数量要减少,这个数量要减少,另外一个数据库里面应当是要生成的。

好,我们等它启动,之后我们来测试。

行,服务已经启动了,服务全部都已经启动了,接着我们开始抢单测试了。

来,测试一次。

排队成功了,看数据库数据,增加了一条订单。

数量应该要减少999,并且它的排队的标识清理了。

好,这里应该还会有一个它24小时不能购买的标识。

在这里。

正确。

OK,这是我们这个秒杀抢单总体的一个测试操作。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Cloud 微服务架构的秒杀系统（seckill-order）的订单创建与库存扣减核心逻辑。开发者在 IntelliJ IDEA 中调试 `OrderServiceImpl` 服务，该服务负责处理用户下单请求。核心流程包括：首先检查 Redis 中的库存数量 `num`，若为 0 则直接返回；否则，调用 `skuFeign` 服务获取商品详情，创建订单对象并填充数据，最后将订单写入数据库，并在 Redis 中将库存数量减 1。视频中还展示了如何通过 Redis Desktop Manager 查看和操作 Redis 数据，以及如何使用 Postman 发起 HTTP 请求来模拟用户下单。整个过程体现了分布式系统中服务间调用、数据库操作和缓存管理的协同工作。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各帧的时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **00:00 - 00:03**: 展示 `OrderServiceImpl` 类的代码，重点是 `if (num == 0)` 的条件判断逻辑。
*   **00:03 - 00:06**: 代码执行到 `skuFeign.findById(id)`，调用远程服务获取商品信息。
*   **00:06 - 00:09**: 创建 `Order` 对象并设置其属性，如 `setTotalNum`, `setCreateTime` 等。
*   **00:09 - 00:12**: 将订单数据通过 `orderMapper.insertSelective(order)` 插入数据库。
*   **00:12 - 00:15**: 在 Redis 中执行 `num--` 操作，减少库存。
*   **00:15 - 00:18**: 展示 Redis Desktop Manager 中的 Redis 数据库，查看 `num` 键的值。
*   **00:18 - 00:21**: 使用 Postman 发起 HTTP 请求，模拟用户下单，请求地址为 `http://192.168.211.137:8081/...`。
*   **00:21 - 00:24**: 在 Postman 中查看请求返回的 JSON 数据，确认订单创建成功。
*   **00:24 - 00:27**: 再次展示 Redis Desktop Manager，确认库存数量已成功减 1。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 (Java)**:
    *   **订单创建与库存检查逻辑**:
        ```java
        if (num == 0) {
            return;
        }
        Result<Sku> skuResult = skuFeign.findById(id);
        Sku sku = skuResult.getData();
        // 创建Order
        Order order = new Order();
        order.setTotalNum(0);
        order.setCreateTime(new Date());
        order.setUpdateTime(order.getCreateTime());
        order.setId("No" + idWorker.nextId());
        order.setOrderStatus("0");
        order.setPayStatus("0");
        order.setConsignStatus("0");
        order.setSkuId(id);
        order.setUserName(sku.getName());
        order.setPrice(sku.getSeckillPrice() * order.getTotalNum());
        orderMapper.insertSelective(order);
        // Redis中对应的num递减
        num--;
        ```
    *   **Redis 操作代码**:
        ```java
        // 清理用户排队信息
        Map<String, Object> allMap = new HashMap<>();
        allMap.put(userKey, 0);
        allMap.put("num", num);
        redisTemplate.boundHashOps(key).putAll(allMap);
        // 记录用户购买该商品，24小时后过期
        redisTemplate.boundValueOps(userKey).set("");
        ```
    *   **Redis 数据结构**:
        *   键名: `sku:21254301271648944`
        *   值: `1` (初始库存)
        *   操作后值: `0` (库存减 1)

*   **图表/界面**:
    *   **IDEA 项目结构**: 展示了 `seckill-order` 项目的目录结构，包括 `config`, `controller`, `dao`, `impl` 等包。
    *   **Redis Desktop Manager**: 展示了 Redis 数据库的界面，包括连接、键值对、日志等。
    *   **Postman**: 展示了 HTTP 请求的设置和返回结果。

---

### 4) 关键场景与演示描述

*   **场景一：订单创建与库存检查**
    *   **描述**: 开发者在 `OrderServiceImpl` 中编写了核心逻辑。当用户请求下单时，系统首先检查 Redis 中的库存数量 `num`。如果 `num` 为 0，系统直接返回，不创建订单。否则，系统会调用 `skuFeign` 服务获取商品详情，创建一个 `Order` 对象，并设置其属性，如订单状态、价格、用户信息等。
    *   **技术要点**: 该场景展示了分布式系统中如何通过 Redis 进行库存预扣，避免超卖。`skuFeign` 是一个远程调用服务，用于获取商品信息。

*   **场景二：订单写入数据库**
    *   **描述**: 在创建订单对象后，系统调用 `orderMapper.insertSelective(order)` 方法，将订单数据写入数据库。这一步确保了订单信息的持久化。
    *   **技术要点**: `orderMapper` 是 MyBatis 的 Mapper 接口，`insertSelective` 方法用于插入订单数据，但只插入非空字段，提高了数据插入的灵活性。

*   **场景三：Redis 库存扣减**
    *   **描述**: 在订单写入数据库后，系统执行 `num--` 操作，将 Redis 中的库存数量减 1。这一步确保了库存的准确性。
    *   **技术要点**: 该操作是原子性的，确保了在高并发场景下库存不会被重复扣减。

*   **场景四：Redis 数据查看与操作**
    *   **描述**: 开发者使用 Redis Desktop Manager 工具连接到 Redis 服务器，并查看 `sku:21254301271648944` 键的值。初始值为 `1`，在订单创建后，值变为 `0`。
    *   **技术要点**: 该场景展示了如何通过工具查看和操作 Redis 数据，验证库存扣减是否成功。

*   **场景五：HTTP 请求模拟下单**
    *   **描述**: 开发者使用 Postman 工具向 `http://192.168.211.137:8081/...` 发起 HTTP 请求，模拟用户下单。请求成功后，返回的 JSON 数据中包含 `message` 和 `code` 字段。
    *   **技术要点**: 该场景展示了如何通过 HTTP 请求模拟用户操作，验证服务的可用性。`code: 200` 表示请求成功。

---

以上是根据视频画面进行的结构化技术分析报告。
