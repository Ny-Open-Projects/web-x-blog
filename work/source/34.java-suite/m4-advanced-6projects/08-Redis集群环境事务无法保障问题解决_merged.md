# 08-Redis集群环境事务无法保障问题解决 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们讲解Redis集群环境中事物不生效的问题

那在我们Redis集群里面

事物是不支持的

单个Redis是支持事物的

所以我们在写的这个热点商品隔离的时候是存在问题的

我们看一下

这里分了两次保存

一次保存

两次保存

如果上面这里成功了

下面这里中途失败了

那上面这个数据是没法实现一个回滚的

那我们怎么保障这块数据没有问题呢

我们来提供一种思路

这里有三台Redis

第一台Redis

好

还有两台

三台Redis

在这一块我们怎么保障数据有效

数据的事物能够生效

用户这个时候保存数据

他往这里面添加

添加数据的时候

同时往这添加数据

同时再往这里添加数据

如果这个时候第一步成功了

第二步成功了

第三步失败了

那么第一步第二步的数据是没法回滚的

怎么办呢

能不能解决了

可以

把这两个Redis干掉不要

把这一次去操作的三个操作流程

合并成一个操作流程

一次保存进来

那就可以了

那像这样子有没有问题呢

有问题

咱们这一块做集群

是为了让数据的容量能够

保存进来

存更多数据

查找更快

那你这个时候把它直接给干掉了

那违背了我们那一个想法

对不对

怎么办呢

也不是说完全不能解决

单台Redis是支持事物的

我们只需要做到这个要求

第一是多次操作

合并成一次操作

第二个是多次数据操作

的数据操作

然后我们把这三个数据合并成一个数据

这样子就可以了

什么意思呢

比如说我这一块要操作Redis缓存

对吧

那我操作Redis缓存

要存三条数据

那么存三条数据呢

以前是一个存这里

一个存这里

一个存这里

那现在不要这样子了

现在只把它存到一个里面去

存到这来

存到这来是怎么存呢

做这么一回事呢

我们先做一个事情

把多次操作的流程合并成一次操作

那三次操作流程合并到一个里面去

合并成一次操作

多次操作的操作的数据呢

合并成一条数据

合并数据

这样子就可以了

那么它的key你可以给个key1

那如果是下次操作呢

下次操作没关系

下次操作操作第二个Redis就行

下次操作第二个Redis就行

也是按照这个流程合并就行了

合并数据也是合并就可以了

第三次也是一样

这样子就可以解决这个事物的一个问题

没有别的好办法啊

目前为止没有别的好办法

那我们这一块也可以遵循刚才的一个操作原则

来解决事物的问题

第一是合并操作合并

那还有个是数据合并

好我们先来做数据合并

数据合并怎么做呢

你这不是有两条数据吗

我把它合到一条数据里去

map可不可以呢

可以

object data map

reuhash map

好可以了

string object

然后把数据往里面存储一下

第一个是number

对应的数据在后面那里

我们也给存过来就行了

好存到这里

那下面这个呢

整体存一下就行了

整体存进来

datamap

点put一下

当前存的key是info

info对应的数据是这个数据

也就是这个数据

给塞进去就行了

好那上面这个呢

就可以注释了就不要了

这个也注释不要了

那存数据一次操作怎么一次操作呢

radius terminator

bound hash

key还是那个key

值呢

put all

那就可以把多次操作合并成一次了

OK

这样就可以解决

radius缓存集群环境下

事物不能够生效的问题

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段展示了一个 Java 项目中 `SkuServiceImpl` 类的代码编写过程，核心内容是实现一个商品库存的“秒杀”功能。讲师通过 IntelliJ IDEA 编辑器，逐步演示了如何在数据库中查询商品锁定状态、在 Redis 中进行库存扣减和商品信息存储，并最终将数据合并后写入 Redis。整个过程体现了典型的“先查后锁，再操作”的分布式锁和缓存优化思路，旨在解决高并发下的库存超卖问题。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示 `SkuServiceImpl` 类中 `count()` 方法的初始代码，用于查询商品总数。
*   **00:05 - 00:10**: 讲师开始编写 `updateByExampleSelective` 方法，用于根据条件更新商品状态（锁定）。
*   **00:10 - 00:15**: 讲师在 `if(count>0)` 条件块内，开始编写将商品信息存入 Redis 的逻辑。
*   **00:15 - 00:20**: 讲师使用 `redisTemplate.boundHashOps(key).increment(...)` 方法，将商品的秒杀数量存入 Redis。
*   **00:20 - 00:25**: 讲师创建一个 `Map<String, Object> info`，用于存储商品的 ID、价格和名称。
*   **00:25 - 00:30**: 讲师将 `info` 映射中的数据写入 Redis，使用 `put("info", info)`。
*   **00:30 - 00:35**: 讲师决定将“库存数量”和“商品信息”合并到一个 `dataMap` 中，以减少 Redis 操作次数。
*   **00:35 - 00:40**: 讲师创建 `dataMap` 并将商品的秒杀数量放入其中。
*   **00:40 - 00:45**: 讲师创建 `info` 映射并填充商品信息。
*   **00:45 - 00:50**: 讲师将 `info` 映射的数据放入 `dataMap`。
*   **00:50 - 00:55**: 讲师使用 `redisTemplate.boundHashOps(key).put("info", info)` 将合并后的数据写入 Redis。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    ```java
    // 查询总数
    @Override
    public Integer count() {
        Example example = new Example(Sku.class);
        Example.Criteria criteria = example.createCriteria();
        criteria.andEqualTo(property: "isLock", value: 1);
        criteria.andEqualTo(property: "id", id);
        // 执行锁定
        int count = skuMapper.updateByExampleSelective(sku, example);
        // 2.锁定成功了，则把商品存入到Redis缓存进行隔离
        if(count>0) {
            String key = "SKU_"+id;
            Sku currentSku = skuMapper.selectByPrimaryKey(id);
            // 存储商品数量
            redisTemplate.boundHashOps(key).increment(key: "num", currentSku.getSeckillNum());
            // 存储商品信息
            Map<String, Object> info = new HashMap<String, Object>();
            info.put("id", id);
            info.put("price", currentSku.getSeckillPrice());
            info.put("name", currentSku.getName());
            redisTemplate.boundHashOps(key).put("info", info);
        }
    }
    ```

*   **关键操作**:
    *   **数据库查询**: 使用 `Example` 和 `Criteria` 查询商品是否被锁定。
    *   **数据库更新**: 使用 `updateByExampleSelective` 方法将商品状态更新为“锁定”。
    *   **Redis 操作**:
        *   `increment`：对商品的秒杀数量进行原子递增。
        *   `put`：将商品的 ID、价格、名称等信息存储为一个 Hash 结构。
    *   **数据合并**: 创建 `dataMap`，将商品数量和信息合并，以减少 Redis 的操作次数。

---

### 4) 关键场景与演示描述

*   **场景一：查询与锁定** (00:05 - 00:10)
    *   讲师在 `count()` 方法中，通过 `Example` 和 `Criteria` 查询数据库，筛选出 `isLock=1` 且 `id` 匹配的商品。
    *   使用 `updateByExampleSelective` 方法，将符合条件的商品的 `isLock` 字段更新为 1，实现“锁定”操作。

*   **场景二：Redis 存储** (00:10 - 00:25)
    *   讲师在 `if(count>0)` 条件块内，使用 `skuMapper.selectByPrimaryKey(id)` 查询商品的详细信息。
    *   使用 `redisTemplate.boundHashOps(key).increment(...)` 方法，将商品的秒杀数量存入 Redis。
    *   创建一个 `Map<String, Object> info`，并使用 `put` 方法将商品的 ID、价格和名称存入其中。
    *   使用 `redisTemplate.boundHashOps(key).put("info", info)` 将商品信息写入 Redis。

*   **场景三：数据合并优化** (00:30 - 00:50)
    *   讲师决定将“库存数量”和“商品信息”合并到一个 `dataMap` 中。
    *   创建 `dataMap`，并使用 `put` 方法将商品的秒杀数量放入其中。
    *   创建 `info` 映射，填充商品信息。
    *   将 `info` 映射的数据放入 `dataMap`。
    *   最终，使用 `redisTemplate.boundHashOps(key).put("info", info)` 将合并后的数据写入 Redis。

*   **场景四：IDEA 代码补全** (00:40 - 00:50)
    *   讲师在编写 `dataMap.put(...)` 时，IDEA 自动弹出 `Map` 的方法补全列表。
    *   讲师在编写 `redisTemplate.boundHashOps(key).put(...)` 时，IDEA 也弹出 `boundHashOps` 的方法补全列表，方便选择 `put` 方法。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解视频内容。
