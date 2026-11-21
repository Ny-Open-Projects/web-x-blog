# 06-热点数据隔离-代码实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们实现热点数据隔离

那热点数据隔离呢

我们介绍一下它的一个操作流程

刚才我们实现了热点数据的实时发现

实时发现之后

我们应该要调用我们的商品微服务

商品微服务在这一块实现热点数据隔离

怎么隔离

它要把这个商品先从数据库中进行锁定

锁定的目的是

这个时候不要让别人抢购这个商品

因为如果别人抢购这个商品

你同时又再把它进行隔离

会导致数据库数据库存数量不清楚问题

所以这个时候一定要把它在数据库中进行锁定

锁定了之后呢

就开始把这个商品进行隔离

怎么隔离

把它存到ready的缓存区

存到ready的缓存呢

大概的格式

刚才我们已经讲了这种格式

一个key

key里面有对应的数据

number是表示当前这个商品的一个库存数量

好

我们按照这个想法

来实现一下这个隔离

把我们的商品微服务打开

在这一块

写一个方法

叫做隔离方法isolation

我们把这一块打开

商品隔离

是热点商品隔离

我们写个oid

quote isolation

每次记得把商品的ID给我

好

接着我们来实现一下这边的操作

那这边该怎么做呢

很容易的

热点商品隔离

隔离怎么隔离

第一个你要明白

隔离的话

首先你要把数据库进行锁定

对不对

数据库锁定怎么锁定呢

我们来介绍一下

数据库锁定把这里打开

故事里面

找到我们的SKU

在SKU这里

大家看

有一个列是锁定列

叫做e-Slock

一是未锁定

二是锁定

只要用户来抢个个锁定列

锁定一个商品的时候

商品只要是变成了锁定状态

那么此时这个商品将不再允许用户抢购

好

我们看一下这一块

要把这个改成二锁定

对吧

所以第一个步骤要记住是

数据库该商品进行锁定操作

锁定之后

要注意

锁定成功

则把商品

存入到redis缓存进行隔离

这是这一块

总共就只有这两个步骤

锁定成功了就隔离

好我们来实现一下锁定

锁定呢

sku

等于6个sku

sku.set islock

换成2锁定

好锁定有个前提条件

如果之前有人把它锁定了

那我这里还锁不锁呢

有人把它锁定了

我这里就不锁了

所以我要有一个条件的

一个example

一个example

我们选这个

留一个example

sku.class

好一个example

create criteria

creature.and equal

这里写谁呢

注意是锁定的这个

它必须是没有锁定的

如果已经有人锁了

我再锁它干嘛呢

对不对

还有一个是商品的ID

必须是

上面这个ID

好了

这个作为条件

条件有了

紧接着我们开始锁定

那开始锁定

怎么锁定呢

sku.map.updateBy

example.selective

example给它

如果锁定成功

那么此时count会大于0

这个是执行锁定

好我们看一下count是不是大于0

如果此时count大于0

那就没事

大于0的话

那么现在就开始把商品

存入到我们ready的缓存进行隔离了

那么怎么隔离的

注意一下key等于

我们key写个固定潜序sku

对吧

再加上商品ID

这是我们的key

存怎么存呢

大伙要注意一下

存的话存两点数据进去

一个是商品的数量

一个是商品的信息

我们先存数量再存信息

好

存储商品数量

第二个是存储商品信息

其实商品信息存不存都没所谓

只是有时候价格可能会发生变更

价格发生变更的时候

这个价格要跟着变

就这一块

好我们来开始操作

这一块叫redis.bond

我们写下

bond哈希类型

key给它点increment number

这一块给个number

好给个number

紧接着我们要把这个商品的数量给它

我先写个1

这是这一块

那1明显是不正确的

因为当前商品是不是要查出来

所以我上面还要把它查出来

叫db.current.sku

等于skumap.select

byprimarkey

ID给它

上面查出来了数量就知道了对不对

.get叫

sku number

数量有了

紧接着我们存储商品信息

商品信息的我们不要把整个对象都存了

我们只存一部分数据

比如说商品价格商品名称

这两个

还有一些别的东西我们可以存可以不存

我们看一下

来我们写一个对象叫map

string object

叫说info

luhashmap

写string

object

往里面存一下相关的信息就可以了

哪些信息呢

第一个可以给它ID

ID给它

除了ID还可以给它价格

price

叫current.get

skuprice

还有什么呢

还有它的一个

注意名字也给它

current.get

name

当然名字可给可不给

好就这一块

紧接着我们把它也存到reddit缓存区

这个存呢

点写个put

key用什么呢

这个key用info

info给它

于是这一块

我们就实现了热点数据的隔离了

那这一块写了之后我们控制层要调它的

所以我们需要在控制层这里也写一个

写个调用

热点商品隔离

那隔离这一块写个public

result

isolate

写个hot

isolation

行

写个return

好了这一块隔离我们就开始给它搞个映射地址

post mapping

value

直接写过来

一个叫做

hot叫

isolation

行了

那么这个时候我需要接受一个参数的

注意是要接受一个参数的

参数呢我们可以写个

我们可以这样写

写个叫requestParamore

那这一块我们写个list

ids

可以了

数据接到了之后紧接着我们就开始调用它

调用就行了

那么调用这一块呢

skusit进行调用

一定是for循环的调用

for each

skuservice.isolationid给它

那么这个时候就进行了一个

商品的一个

隔离

那隔离这一块注意一下我们要返回一个状态信息

去

statuscode.ok

接着不要忘了给个提示

叫

热点数据

隔离成功

OK了

行隔离就搞定了

我们接着要给它写个份接口

那份接口呢这个就比较简单

我们直接在这去

写一下就行了

把份接口

找到

这故事这里

在这一块我们去写一个对应的方法就OK了

把它给补充过来

行加个逗号

那么这一块这个热点数据隔离就搞定了

搞定了之后呢我们在

监控那一块要进行调用

把我们的

monitor监控打开

monitor监控

这一块

我们需要注入我们当前这个

份接口

在这里

privately

叫sku份

sku份

直接给注入进来

注入进来之后呢就直接给调用

就可以了

那么这一块就不用去循环了

循环一次吧

紧接着调用

hot isolation

把当前的ids给它

这个是热点数据隔离

行隔离就成功了

但是有一个问题

这个份接口我们这里

要给它开启份才行

Enable

FontClient

好我们写下

EnableFontClient

BasePackage

Comm.

我们把这个份接口的包给导过来

这个包给copy过来就OK了

行这一块就搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于“秒杀系统”中“热点数据隔离”技术实现的教学内容。讲师通过演示一个名为 `seckill-goods` 的 Spring Boot 项目，详细讲解了如何在高并发场景下，通过数据库行锁和 Redis 分布式锁的组合，实现对热点商品数据的隔离，从而避免数据库被大量并发请求打垮。核心流程包括：在数据库中对商品进行行锁，然后将商品信息（如库存数量）写入 Redis，以支持后续的高并发读取和扣减操作。视频中还展示了如何通过 Feign 客户端调用服务，以及如何在监控程序中模拟热点商品的访问。

---

### 2) 按时间顺序的章节（带时间点）

*   **0:00 - 0:30**: 视频开头，讲师展示课程大纲，定位到“第3章 热点商品+抢单实现”下的“1.2.2 实时热点数据隔离”章节，引出本节主题。
*   **0:30 - 1:00**: 讲师在 PPT 上展示系统架构图，说明热点数据隔离需要考虑的问题：首先在 MySQL 数据库中对商品进行锁定，然后将商品数据导入 Redis，整个过程需要支持事务操作。
*   **1:00 - 2:00**: 讲师切换到 IDE，展示 `SkuService` 服务类的代码，讲解 `hotIsolation` 方法的实现逻辑。
*   **2:00 - 3:00**: 讲师在代码中演示如何使用 MyBatis-Plus 的 `updateByExampleSelective` 方法对数据库进行行锁操作。
*   **3:00 - 4:00**: 讲师展示如何将锁定成功后的商品信息（如库存数量）写入 Redis，使用 `StringRedisTemplate` 的 `boundHashOps` 方法进行操作。
*   **4:00 - 5:00**: 讲师展示 `SkuController` 控制器，讲解如何通过 `@GetMapping` 注解提供查询商品总数和分页查询商品列表的接口。
*   **5:00 - 6:00**: 讲师展示 `SkuFeign` 接口，讲解如何通过 Feign 客户端调用 `SkuService` 中的 `count` 和 `findList` 方法。
*   **6:00 - 7:00**: 讲师展示 `MonitorApplication` 监控程序，讲解如何通过 `ShardingContext` 获取热点商品 ID 列表，并打印日志进行模拟访问。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 图表

*   **系统架构图**:
    *   **组件**: MySQL 数据库、Redis、数据隔离模块。
    *   **流程**: 数据隔离模块首先对 MySQL 数据库中的商品进行行锁，然后将商品数据导入 Redis。
    *   **关键说明**: “热点数据隔离，需要考虑很多问题，首先要将商品从数据库中进行锁定，然后将商品数据导入Redis，导入到Redis的时候，需要支持事务操作。”

#### 代码

*   **`SkuService.java` 中的 `hotIsolation` 方法**:
    ```java
    @Override
    public void hotIsolation(String id) {
        // 1. 数据库对该商品进行锁定操作
        Sku sku = new Sku();
        sku.setIslock(2); // 设置锁定状态

        Example example = new Example(Sku.class);
        Example.Criteria criteria = example.createCriteria();
        criteria.andEqualTo("islock", 2);
        criteria.andEqualTo("id", id);
        // 执行锁定
        int count = skuMapper.updateByExampleSelective(sku, example);

        // 2. 锁定成功了，则把商品存入到Redis缓存进行隔离
        if (count > 0) {
            String key = "SKU_" + id;
            Sku currentSku = skuMapper.selectById(id);
            // 存储商品数量
            redisTemplate.boundHashOps(key).increment("num", currentSku.getNum());
            // 存储商品信息
            Map<String, String> info = new HashMap<>();
            info.put("id", id);
            // ... (后续代码未完全展示)
        }
    }
    ```

*   **`SkuController.java` 中的 `count` 和 `findList` 方法**:
    ```java
    @GetMapping(value = "/count")
    public Integer count() {
        return skuService.count();
    }

    @GetMapping(value = "/sku/list/{page}/{size}")
    public Result<List<Sku>> findList(@PathVariable(value = "page") Integer page, @PathVariable(value = "size") Integer size) {
        return skuService.findList(page, size);
    }
    ```

*   **`SkuFeign.java` 接口**:
    ```java
    @FeignClient(value = "seckill-goods")
    public interface SkuFeign {
        @GetMapping(value = "/sku/count")
        Integer count();

        @GetMapping(value = "/sku/list/{page}/{size}")
        List<Sku> findList(@PathVariable(value = "page") Integer page, @PathVariable(value = "size") Integer size);
    }
    ```

*   **`MonitorApplication.java` 中的 `execute` 方法**:
    ```java
    @Override
    public void execute(ShardingContext shardingContext) {
        List<String> ids = monitorItemsAccess.loadData();
        for (String id : ids) {
            System.out.println("热点商品ID: " + id);
        }
    }
    ```

---

### 4) 关键场景与演示描述

1.  **场景一：系统架构讲解** (0:30 - 1:00)
    *   **描述**: 讲师在 PPT 上展示了一个包含 MySQL、Redis 和数据隔离模块的架构图。他解释了热点数据隔离的核心思想：先在数据库中锁定商品，再将数据导入 Redis，以支持高并发读取。他特别强调了“事务操作”的重要性。

2.  **场景二：数据库行锁实现** (1:00 - 2:00)
    *   **描述**: 讲师切换到 IDE，打开 `SkuService.java` 文件。他演示了如何在 `hotIsolation` 方法中，通过 `Example` 和 `Criteria` 对象构建查询条件，将商品的 `islock` 字段设置为 2（表示锁定状态），并使用 `updateByExampleSelective` 方法执行数据库更新操作，从而实现对商品的行锁。

3.  **场景三：Redis 缓存写入** (2:00 - 3:00)
    *   **描述**: 讲师在代码中添加了条件判断 `if (count > 0)`，确保只有在数据库锁定成功后，才将商品信息写入 Redis。他使用 `StringRedisTemplate` 的 `boundHashOps` 方法，将商品的 ID 作为 key，库存数量作为 value，写入 Redis 的哈希表中，以实现数据隔离。

4.  **场景四：Feign 客户端调用** (5:00 - 6:00)
    *   **描述**: 讲师展示了 `SkuFeign` 接口，该接口定义了 `count` 和 `findList` 两个方法，用于通过 Feign 客户端调用 `SkuService` 中的对应方法。这为后续的微服务调用和监控程序提供了接口支持。

5.  **场景五：监控程序模拟访问** (6:00 - 7:00)
    *   **描述**: 讲师展示了 `MonitorApplication` 监控程序。该程序通过 `ShardingContext` 获取热点商品 ID 列表，并使用 `System.out.println` 打印热点商品 ID，模拟对这些商品的访问。这为后续的性能测试和监控提供了基础。
