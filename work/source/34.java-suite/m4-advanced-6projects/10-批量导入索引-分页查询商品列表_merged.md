# 10-批量导入索引-分页查询商品列表 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们讲解商品索引数据的一个管理

那这一块呢

我们会先讲解批量导入商品数据到我们ES索引库中

然后讲解增量商品数据导入到ES索引库中

最后再讲解一下我们ES索引库中索引数据来实现商品的一个列表搜索

好

我们先来讲解这个批量导入这一块

先看一下它的实现流程是怎么做的

在我们做秒杀这一块啊

这个商品的数量呢

一般是非常庞大的

如果我们想要实现快速检索

可以去查询数据库

那这个时候去查询数据库呢

会给数据库造成非常大的压力

很有可能导致数据库崩溃

所以我们不建议采用数据库

并且数据库查询

它的效率也达不到我们的期望

那这个时候呢

我们可以做缓存

把数据存储到ready的缓存

但存到ready的缓存呢

也会有问题

因为你存到ready的缓存

它是占内存空间的

如果我们秒杀的商品数量庞大到PB级别

这个时候用缓存是解决不了问题的

所以我们不建议用数据库查询

也不建议用ready的缓存去存储海量的秒杀商品

那怎么办呢

我们做这么一块呢

我们做这么一块呢

我们做这么一个事情

把海量的秒杀商品数据

存储到我们全文收储引擎

Eletic社企中

那这个时候用Eletic社企来实现PB级别数据的一个

实时检索

实时更新的能力

而且我们Eletic社企

目前在市面上来说

使用的频率是非常广泛的

很多大厂都在用它

所以用它是比较合适的

好

那接着我们就实现一下

这个批量数据

批量导入

那批量导入这一块该怎么去做批量导入呢

首先第一个

我们批量导入一定是在搜索微服里面去做

因为搜索微服去直接管理我们的索引库

所以我们应该在搜索微服里面导入秒杀商品到索引库去

那这个导入该怎么导入呢

在这一块

他要去获取秒杀商品的列表

所以要用这个批量导入去做批量导入

用粪接口去调用我们的CQ故事去查询秒杀商品集合

然后导入到索引库去

但是秒杀商品是海量的

所以我们不建议一条一条逐条导入

我们建议分页查询

分页查询批量导入

你一次查十条一次查一百条一千条一万条

按照你这个数据的量去查询

然后导入到索引

这样子会快一些

也不建议一下全塞过去全塞过去

那这个时候批币级别数据

你根本就没有那么大的存储空间了

很有可能超时了

好

所以我们这一块这么子实现

首先在我们搜索微服里面去分页调用我们的

商品微服来查询秒杀商品

将分页查询到秒杀商品集合列表批量导入

到我们的索引库去按照这个流程实现

所以第一步这一块要准备一个分页查询秒杀商品集合

好

我们开始实现一下这个分页秒杀商品集合的查询

首先把我们的SQL故事微服打开

在这一块来编写相关的案例

在这里

还有个是SQL service

还有个是我们的控控球了

首先这里大家要注意

既然是分页查询

一定是要先查询总数量

然后是分页查询集合列表

我们把这两个方法给写一下

分页查询总数量返回数量integer

写个count

那查询集合列表了返回list

SKU

这一块要注意写个list

既然是分页查询

他应该是需要两个参数的

第一个参数当前页

第二个参数每页显示多少条

接着我们在他的实现内里去实现这个方法

这一块我们简单写一下

这个是查询总数

这个是分页列表查询

行

我们来开始写这个方法

再写这个

这个时候查询总数的话

一定要注意这么几个条件

第一你查询这个商品的话

这个商品他必须是秒杀的商品

对不对

这个状态必须等于二

还有一个你这个数量总得大于零

你不能说一个商品都没有

你就去把它给加载出来

这不合逻辑

还有一个就是秒杀时间

这一块

你都已经结束了

那这个商品还导入到索引库干嘛呢

对不对

这个时间不能是结束的时间

不能是已经结束的活动时间了

好

我们注意这三点就行了

来写一下

一个是商品状态

status等于二

还有一个是商品秒杀数量

是Q

number要大于零

还有一个是

是Q

and必须要大于当前时间

这是这三个条件

我们来写一下这三个条件

这三个条件呢

我们就封装一个example

example呢

是通用map里面的

大家去学习一下

这里我们就不去讲解了

好

这是这一块

写的叫sku.class

我们写一下

curter.rc

我们写一下

and equal

注意是状态status必须等于二

还有一个是秒杀的一个数量点

注意是大于零

所以我们找一下这里面哪一个是大于

好

看上面这里

咱找这个大于还没找着

这个是大于

写它就行了

属性呢

我们看一下对应的属性是谁

这个是大于

叫做sku.lumbo

这个好大于零

所以我这里写个零就行了

还有一个时间这一块

curter.and大于

注意是大于

这里写一下

谁大于谁呢

我要写一下

结束时间在上面这里有一个end time

这个它要大于谁呢

注意要大于

这个它要大于谁呢

你写个new date

这是这一块

好了

接着我们再写一下这个查询就可以了

sku map select count by example

example给它

于是count这里就搞定了

接着我们再写下面这个分页列表查询

那么分页列表查询的条件是不会变的

所以这整个条件我们可以考过来

但是这一块是怎么做

第一个步骤要分页

第二个步骤要集合查询

我们按这两个步骤来做就行了

分页呢

我们将采用一个第三方插件

配给helper

这个呢

我也不去讲解了

直接带大家用就行了

写个配给helper.startpage

第一个当前页

第二个每页显示的条数

它一定要写到查询的前面

好

下面这里就是我们要查询的

那么查询怎么查询呢

一样的叫sku map.select by example了就行了

这一块就实现了一个分页查询

好

我们控制层要调用它

所以我需要在控制层这里写这个分页查询

分页查询

那第一个是查询总数量

第二个是分页查询集合列表

我们先写这个总数量查询

public.integer就写个count就可以了

return

那上面这一块呢

我就给个get mapping

地址呢

我就写个count就可以了

写个叫skuservice.count

好结束

下面这个是一个集合查询

public.integer

写一个list

sku

写个叫list

那么上面这个地址呢

我写个get mapping

value写个list

先给个分页

再给个每页显示的条数

先获取这个页码

好

然后获取每页显示的条数

直接给拷过来就行了

条数呢用这个size

行

方法搞清楚了

然后再调用我们的查询.list

配置给它

size给它

搞定

这两个写完之后

不要忘了把它写到份接口中

因为外部查询是需要调用的

等会儿我们批量导入的时候

需要调它

所以要在这个份接口中去编写一下

我们就把它写到这一块来就OK了

这个呢要注意一下

它是要去掉的

前面不要忘了加SKU

上面也是一样

当然SKU你可以加到上面去

好了

这一块就搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个高并发秒杀系统（`seckill`）的开发教程，重点讲解了商品（SKU）数据的分页查询与条件筛选功能。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `SkuService` 服务层使用 MyBatis-Plus 的 `Example` 对象构建复杂的查询条件（如商品状态、秒杀数量、秒杀结束时间），并在 `SkuController` 控制器层实现分页接口。同时，视频也展示了如何通过 Feign 客户端调用远程服务，以及如何在 `Sku` 实体类中使用 `@TableId` 和 `@TableField` 注解进行数据库映射。整个过程旨在构建一个支持商品列表分页、条件筛选和活动商品查询的后端服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，展示课程大纲，当前章节为“3.1 批量导入”，并引出使用 Elasticsearch 进行海量数据索引管理的必要性。
*   **00:05 - 00:15**: 展示项目结构，进入 `SkuService` 服务层代码，开始讲解分页查询的实现。
*   **00:15 - 00:25**: 在 `SkuService` 中，演示如何使用 `Example` 对象构建查询条件，包括商品状态、秒杀数量和秒杀结束时间。
*   **00:25 - 00:35**: 展示 `Sku` 实体类的代码，讲解 `@TableId` 和 `@TableField` 注解的使用。
*   **00:35 - 00:45**: 在 `SkuService` 中，继续完善查询条件，使用 `Date` 类构造秒杀结束时间。
*   **00:45 - 00:55**: 展示 `SkuController` 中的 `count()` 方法，用于查询商品总数。
*   **00:55 - 01:05**: 展示 `SkuController` 中的 `list()` 方法，用于分页查询商品列表。
*   **01:05 - 01:15**: 展示 `SkuController` 中的 `actList()` 方法，用于查询指定活动下的秒杀商品。
*   **01:15 - 01:25**: 展示 `SkuFeign` 接口，用于定义 Feign 客户端调用远程服务的接口。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   **架构图**: 展示了 `seckill-search` 服务通过 Feign 调用 `seckill-goods` 服务的架构图，用于分页查询商品数据。
*   **代码**:
    *   **`SkuService.java`**:
        ```java
        @Override
        public Integer count() {
            Example example = new Example(Sku.class);
            Example.Criteria criteria = example.createCriteria();
            // 1. 商品状态 status=2
            criteria.andEqualTo("status", "2");
            // 2. 商品秒杀数量 seckillNum>0
            criteria.andGreaterThan("seckillNum", 0);
            // 3. seckillEnd>now()
            criteria.andGreaterThan("seckillEnd", new Date());
            return null;
        }
        ```
        ```java
        @Override
        public List<Sku> list(Integer page, Integer size) {
            // 2. 分页集合查询
            Example example = new Example(Sku.class);
            Example.Criteria criteria = example.createCriteria();
            // 1. 商品状态 status=2
            criteria.andEqualTo("status", "2");
            // 2. 商品秒杀数量 seckillNum>0
            criteria.andGreaterThan("seckillNum", 0);
            // 3. seckillEnd>now()
            criteria.andGreaterThan("seckillEnd", new Date());
            return null;
        }
        ```
    *   **`Sku.java`**:
        ```java
        @Table(name = "tb_sku")
        public class Sku implements Serializable {
            @Id
            @TableId(name = "id")
            private String id; // 商品id
            @TableField(name = "name")
            private String name; // SKU名称
            @TableField(name = "price")
            private Integer price; // 价格（分）
            @TableField(name = "seckill_price")
            private Integer seckillPrice; // 单位，分
            @TableField(name = "num")
            private Integer num; // 库存
        }
        ```
    *   **`SkuController.java`**:
        ```java
        @GetMapping(value = "/count")
        public Integer count() {
            return skuService.count();
        }
        ```
        ```java
        @GetMapping(value = "/list/{page}/{size}")
        public List<Sku> list(@PathVariable(value = "page") Integer page,
                             @PathVariable(value = "size") Integer size) {
            return skuService.list(page, size);
        }
        ```
        ```java
        @GetMapping(value = "/activity/{id}/{page}/{size}")
        public Result<PageInfo<Sku>> actList(@PathVariable(value = "id") String id,
                                            @PathVariable(value = "page") Integer page,
                                            @PathVariable(value = "size") Integer size) {
            PageInfo<Sku> pageInfo = skuService.findSkuByActivityId(id, page, size);
            return new Result<>(flag, true, StatusCode.OK, message, pageInfo);
        }
        ```
    *   **`SkuFeign.java`**:
        ```java
        @FeignClient(value = "seckill-goods")
        public interface SkuFeign {
            @GetMapping(value = "/count")
            public Integer count();
            @GetMapping(value = "/sku/list/{page}/{size}")
            List<Sku> list(@PathVariable(value = "page") Integer page,
                          @PathVariable(value = "size") Integer size);
            @GetMapping(value = "/sku/dcount/{id}/{count}")
            public Integer dcount(@PathVariable(value = "id") String id,
                                 @PathVariable(value = "count") Integer count);
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：分页查询条件构建** (00:15 - 00:25)
    *   讲师在 `SkuService` 中，通过 `Example` 对象创建查询条件。
    *   使用 `criteria.andEqualTo("status", "2")` 来筛选状态为“2”的商品。
    *   使用 `criteria.andGreaterThan("seckillNum", 0)` 来筛选秒杀数量大于0的商品。
    *   使用 `criteria.andGreaterThan("seckillEnd", new Date())` 来筛选秒杀结束时间大于当前时间的商品。
*   **场景二：实体类映射** (00:25 - 00:35)
    *   讲师展示了 `Sku` 实体类，其中使用 `@TableId` 注解标记主键 `id`，并使用 `@TableField` 注解标记其他字段，如 `name`、`price`、`seckill_price` 和 `num`。
*   **场景三：控制器层接口实现** (00:45 - 01:15)
    *   讲师在 `SkuController` 中定义了三个接口：
        *   `count()`：用于查询商品总数。
        *   `list()`：用于分页查询商品列表。
        *   `actList()`：用于查询指定活动下的秒杀商品。
    *   每个接口都调用了 `SkuService` 中对应的实现方法。
*   **场景四：Feign 客户端定义** (01:15 - 01:25)
    *   讲师展示了 `SkuFeign` 接口，用于定义 Feign 客户端调用远程服务的接口。
    *   接口定义了 `count()`、`list()` 和 `dcount()` 方法，用于调用远程服务的相应接口。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解该技术课程的内容。
