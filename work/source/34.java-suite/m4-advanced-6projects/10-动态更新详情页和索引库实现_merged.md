# 10-动态更新详情页和索引库实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着我们基于刚才的分析来实现一下这个操作

那首先我们在这一块

这里有一个添加我们的活动

在这里

这里做什么事情呢

添加活动的时候

我们就实现一个定时任务调度

将活动结束时间作为任务开始执行时间

好我们来调用一次

那我们要注入一下我们这个ElecticJobDynamicConfigure

把它给注入进来

注入进来之后

我们就调用一下那个活动

好我们看一下这几个参数

这几个参数呢

我们拷贝过来

拷贝到这里

这个是活动的名称

活动的名称呢

我们就把当前这个活动的

按钮

ID作为名称

免得后面重复了

点GetID

后面这个表达式呢

其实就是活动结束的时候开始执行

那这个我们就用ElecticJobDynamicConfigure

点DataToChrome这个方法

那把当前活动的结束时间传递过去

点GetEndTime

分片呢

我们就分一个

接着是这个任务的

这里还有一个ID

对吧

这个ID呢

注意我们传当前活动的ID过去

因为那边要接到ID

根据活动ID查询活动下的商品列表的

好

接着是最后一个执行的业务流程

6

DynamicTask

可以了

这个活动呢

活动结束

然后触发定时任务

这一块我们就解决了

紧接着我们就把这个任务调度给修改一下

这个任务调度这里怎么修改呢

这个ID此时是活动的ID了

对不对

那拿到了活动的ID

我们紧接着写下面一段代码Modify

把活动ID给我传过来

String ID

这里做什么事情呢?

我们来写一下

根据活动ID查询活动ID下拥有的秒杀商品集合

这是第一个步骤

查出来之后呢

做什么事情呢

查出来之后

我们就开始去修改参与活动的秒杀商品状态

将状态改成

分析状态

分析状态

分析状态

分析状态

分析状态

分析状态

分析状态

分析状态

分析状态

分析状态

分析状态

分析状态

分析状态

分析状态

分析状态

因为你这个活动已经结束了

那肯定不是秒杀商品了

对不对

那么你改之后

他会触发谁呢

他会触发我们生成我们

MySQL会生成我们的Binlog

Binlog一生成的Kana就能订阅了

Kana就能获取增量数据

然后我们的Kana为服务了

他就可以做这么个事

就可以订阅增量数据

订阅增量数据了

然后可以调用两个微服务

哪两个微服务呢

就是静态业微服务和搜索微服务实现更新

这是我们这个流程哈

好

我们开始来实现一下

根据ID查询

当前活动下拥有秒杀商品的一个集合

其实就是这张表中间表

SKU ACT这张中间表

他会记录当前活动ID拥有哪些秒杀商品的集合

好

我们来写一下这个查询

第一步就这个

我们用到的是SKU ACT

等于6SKU ACT点set一下ID给他

好了

给他之后

我们接着就可以去查询了

但是这一块要注意一下哈

即便我是去查询的话

我们是不是也得把他的DU给注入进来呀

这里要注入一下DU哈

不能直接查

SKU ACT Map注入进来

除了他之外

还有一个也要注入SKUMap

为什么他也要注入呢

因为一会要做修改啊

对不对

好

我们接着来

这些条件有了

接着我们就把它查询出来

list写个SKU ACT

等于SKU ACT Map

select把SKU ACT给他

集合查出来了

查出来之后呢

我们把它转成一个list集合

ids

new array list

strain

好

我们开始把这个

这个ids全部放进去

ids.add

act.get

我们要的是商品ID哈

好商品ID拿到了

第二个步骤是修改秒杀商品的状态

那么修改状态的就很容易了

状态这一块SKU等于6SKU

状态设置成1

好

这是状态

但是

必须是之前状态为什么呢

为2的时候

你设置1才有效

对不对

所以我们还要构建一个修改的条件

example

new example

这里面写SKU.class

好

我们再来写

create criteria

那我这一块开始怎么写呢

第一个首先状态

under equal

之前的状态status

必须是2

那么现在还有一个条件

create

under in

就是你所有的ID

必须是上面这个集合里面的ID

不然不允许你做相关的操作

好

接着我们就执行修改

SKU map update by select

by example selective

可以了

那我们这一块整个就搞完了

动态更新我们的索引库

动态更新我们的详情页这一块

OK

这个是根据活动结束时间来实现的

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段来自一个关于“秒杀系统”技术实现的课程，主要讲解如何使用 **ElasticJob** 框架实现**动态任务调度**。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 `ActivityService` 中根据活动信息动态创建任务，并将这些任务注册到 `ElasticJobDynamicConfig` 中。随后，讲师展示了如何编写一个实现 `SimpleJob` 接口的 `DynamicTask` 类，该类负责根据活动ID查询并修改秒杀商品的状态。整个过程涉及 Spring Boot、MyBatis、ElasticJob、以及数据库操作，旨在实现一个可动态扩展的秒杀任务调度系统。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:13**: 展示项目结构，定位到 `ActivityService` 类。
*   **00:00:14 - 00:00:25**: 在 `ActivityService` 中，讲师定位到 `update` 方法，并展示如何通过 `elasticJobDynamicConfig.addDynamicTask()` 方法动态添加任务。
*   **00:00:26 - 00:00:35**: 讲师开始编写 `DynamicTask` 类，该类实现 `SimpleJob` 接口。
*   **00:00:36 - 00:00:45**: 在 `DynamicTask` 类中，讲师编写 `execute` 方法，用于接收分片上下文并获取活动ID。
*   **00:00:46 - 00:00:55**: 讲师开始编写 `modify` 方法，用于根据活动ID查询秒杀商品集合。
*   **00:00:56 - 00:01:05**: 讲师使用 `skuMapper.select` 方法查询商品列表，并将商品ID存入 `List<String>`。
*   **00:01:06 - 00:01:15**: 讲师使用 `Example` 和 `Criteria` API 来构建查询条件，修改商品状态。
*   **00:01:16 - 00:01:25**: 讲师调用 `skuMapper.updateByExampleSelective` 方法，将修改后的状态批量更新到数据库。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段 1 (ActivityService.java)**:
    ```java
    public void update(Activity activity) {
        // 添加
        activityMapper.updateByPrimaryKeySelective(activity);
    }

    private ElasticJobDynamicConfig elasticJobDynamicConfig;

    public void update(Activity activity) {
        // 循环添加活动到数据库中
        List<Integer> seckillIds = activity.getSeckillIds();
        for (Integer seckillId : seckillIds) {
            Activity oneActivity = new Activity();
            BeanUtils.copyProperties(activity, oneActivity);
            // 查询当前活动对应的信息
            SeckillTime seckillTime = seckillTimeMapper.selectByPrimaryKey(seckillId);
            oneActivity.setTd("A" + idWorker.nextId());
            oneActivity.setBeginTime(seckillTime.getStartTime());
            oneActivity.setEndTime(seckillTime.getEndTime());
            float times = TimeUtil.diffHour(oneActivity.getBeginTime(), oneActivity.getEndTime());
            oneActivity.setTotalTime(times);
            // 添加
            activityMapper.insertSelective(oneActivity);
            // 定时任务调度，将活动结束时间作为任务开始执行时间
            elasticJobDynamicConfig.addDynamicTask(oneActivity, ElasticJobDynamicConfig.date2cron(oneActivity.getEndTime()), shardingTotalCount);
        }
    }
    ```

*   **关键代码片段 2 (DynamicTask.java)**:
    ```java
    public class DynamicTask implements SimpleJob {
        @Override
        public void execute(ShardingContext shardingContext) {
            // 活动ID
            String id = shardingContext.getJobParameter();
            // 根据活动ID查询活动ID下拥有的秒杀商品集合
            // 修改参与活动的秒杀商品状态，将状态改成非秒杀商品
            SkuAct skuAct = new SkuAct();
            skuAct.setActivityId(id);
            List<SkuAct> skuActs = skuActMapper.select(skuAct);
            for (SkuAct act : skuActs) {
                // 修改状态
                Sku sku = new Sku();
                sku.setStatus("1");
                Example example = new Example(Sku.class);
                Criteria criteria = example.createCriteria();
                criteria.andEqualTo("id", act.getSkuId());
                skuMapper.updateByExampleSelective(sku, example);
            }
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 动态任务注册**:
    讲师在 `ActivityService` 中，通过 `elasticJobDynamicConfig.addDynamicTask()` 方法，将一个 `Activity` 对象和一个 cron 表达式注册为一个动态任务。这个任务会在活动结束时被触发，用于后续的秒杀商品状态修改。

*   **场景 2: 动态任务实现**:
    讲师创建了一个 `DynamicTask` 类，该类实现了 `SimpleJob` 接口。在 `execute` 方法中，它通过 `ShardingContext` 获取到任务的分片参数（即活动ID），然后根据活动ID查询所有相关的秒杀商品。

*   **场景 3: 数据库操作与状态修改**:
    讲师使用 `Example` 和 `Criteria` API 构建了一个查询条件，用于根据商品ID查询商品信息。然后，他将商品的状态修改为“1”（表示非秒杀商品），并使用 `updateByExampleSelective` 方法将修改后的状态批量更新到数据库中。

*   **场景 4: 代码补全与调试**:
    整个过程中，讲师多次使用 IntelliJ IDEA 的智能代码补全功能，例如在 `List<SkuAct>` 中输入 `add` 时，IDEA 自动提示了 `add(int index, SkuAct element)` 方法；在使用 `Example` 类时，IDEA 提示了 `andEqualTo` 方法，帮助讲师快速构建查询条件。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解该技术课程的内容。
