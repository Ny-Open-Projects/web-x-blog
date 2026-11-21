# 51-智能调度服务（实现过程_订单分类_20） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么刚才呢

咱们是对我们订单分类啊

我们写的这段代码呢

进行了一个简单的测试

好 那么测试完成之后啊

接下来呢 我们就来看

再往下写呢

就是将我们分类之后的结果呢

把它保存到我们的数据库

那么分类之后的结果呢

咱们是不是封装成了这么一个

粒子的集合 对不对

那么全都在这个集合里面

所以说呢 我们在这儿呢

要操作数据库的话呢

主要就是操作这个集合

好 所以我们在这儿呢

可以来扩展这么一个方法

叫做Save Record

保存记录 对吧

然后呢 很明显

就是把我们这个集合对象

把它放进去

然后呢 我们在保存的时候呢

还需要什么呢

把咱们这个Job ID

还有Log ID呢

也一块存进去

也一块传进去

因为在这里面呢

会使用到它

包括我们记录日志啊

等等这些

所以说呢 我们一块传进去

那这样的话呢

我们就需要来

扩展一个新的方法 对吧

这个方法呢

它的作用就是什么呢

就是保存

保存我们这个订单分类结果

那接下来呢

我们就需要来考虑一下

我们要操作数据库的话

具体是需要操作哪些表

这个地方呢

其实主要操作的是两张表

是两张表

大家还有印象吗

咱们直接看我们的实体就可以了

我们的实体跟表已经做了映射对吧

那么我们订单分类呢

会分成多类

那么每一种类型呢

会分每种类型呢

会对应的这么一个实体

就这么一个实体

叫做Other Classified Entity

订单分类记录

它所对应的表呢

就是这个订单分类表

你看这里边是不是有我们的这个ID

对吧

还有Job ID Job Log ID

日志的ID

包括这个什么起始机构

终止机构对吧

还有呢

订单类别

注意这个类别

大家看这个

这种形式还记得吧

咱们是不是就是我们的起始机构

加上一个警号

加上终止机构

再加上当前机构对吧

所以这个类别呢

它其实存的就是那个字符串

包括这个类别下边

一共有多少个订单

对吧

订单的数量

好

这就是个分类

然后呢

具体这一个类型下边

都有哪些订单呢

咱们是不是还有一个关联表

那么对应的有这么一个实体

你看就是这个

订单分类

还有订单关联

对应的是这个表

然后这个表里边呢

你看是不是有订单分类的ID

还有我们原始订单的ID

所以说呢

我们这块呢

主要操作的就是这两张表

比如说我们这一批订单

对吧

分成了十个类别

那这样的话呢

它就会像这个表里面

是不是来插入十条记录

那么每一条记录呢

代表的就是一个分类

对吧

然后呢

再操作这个关联表

具体哪一个订单

对应哪个类别

是不是这样来保存

一条一条的关联数据保存

就可以了

好

所以这块呢

其实就是一个

纯数据库的操作

那么

既然是纯数据库操作呢

我们在这呢

就不再去手敲了

咱们直接把我们

讲义上的代码

拷过来就可以了

包括我们这个地方呢

要操作那两张表呢

还要创建两个不同的service

两个新的service

一个是这个

叫做IOtherClassifiedService

咱们呢

先把这个service接口呢

来创建一下

在我们这个service包下边

我们来创建

一个interface

对吧

然后具体这个代码呢

我就不再去写了

就是这个

对吧

然后呢

这是订单分类的service

然后呢

把这个代码拷过来

放在这

好

这一个service

当然了

还有对应的实现类

对吧

还有对应的实现类

对应这个实现类呢

我们应该的创建出来

放在impl

这个包下边

这个代码的话呢

都是比较简单的

只要看一下什么呢

这个service

它这里边呢

注入的是这么一个map

对吧

使用的是这种map

这种类型

然后操作的实体呢

刚才我们也看了

就是订单分类

这个实体

然后呢

这个service就已经搞定了

然后还有一个service

还有另外一个呢

就是我们刚才看到的

那个关联的service

对吧

首先呢

也是先把这个接口拿过来

这些呢

咱们全都关一下

好

在service包下边

先来创建

接口

OK

这些接口呢

我们全都是继承的

买卖plus

给咱们提供的这个附接口

对吧

叫做iservice

好

然后呢

实现类

先把类名考一下

咱们这些类呀

名字都比较长

类名都比较长

然后呢

具体的代码

也是考过来

好

那这样的话

我们这个service呢

是不是就会

就已经搞定了

对吧

然后呢

service有了之后啊

我们是不是就可以干什么呢

回到我们刚才

这个订单分类

这边来

找到我们刚才

那个service

task

这个service

对吧

save record

那么在这个地方呢

我们也是啊

从简易上

直接把咱们这个代码拿过来

这个代码呢

你看

其实比较长

对吧

那么我们可以

简单来分析一下

考过来

来分析一下这个代码

好

实际上都是一些数据库操作

好

那这边它为什么报错呢

是因为我们这两个service呢

没有注进来

咱们呢给它注入一下

一个是这个叫做

I order classify

I order classify service

好

好

然后呢再来一个

I什么呢

order classify order

这是关联的那个

对吧

现在呢

它之所以报错

应该是命名的问题啊

应该是命名问题啊

应该是命名问题啊

因为它们的命名不一致

啊

这儿还有一个这个youtube

来导入一下

好

应该是我们下面这个

好

现在是没有问题了

然后呢

我们来看一下这个代码啊

这是save record

对吧

在这个地方呢

你看我这是我们传进来这个list的

刚才这是我们在这个地方是不是调的

把这个list传过来

传到这儿来

然后呢

我们是不是对这个list进行一个便利

对吧

调用4H方法

然后便利出来之后呢

就是一个一个的

这个DTO对象

然后在这里边呢

我们是分分了if else这么两个分支

你看这是if

对吧

下面这是else

那么为什么分了这么两个分支呢

因为这块呢

我们分出来的这个类别呢

有可能是新订单

也有可能是中转订单

那么新订单跟中转订单呢

这个地方处理方式不一样

对于新订单来说呢

是需要干什么呢

把它保存在我们刚才看到的

这两张表里面去的

你看是不是调用我们这个service

把它保存进去

而对于中转订单来说呢

其实不需要保存

我们只需要从原先的这个数据库里面

把它这个查出来就行

类别查出来就可以

为什么呢

为什么这个地方不用保存呢

就是因为我们中转订单的话

当它发出的时候

它在第一个发出的网点

它其实网点的时候

其实已经进行了什么呢

这个保存

所以它中转到我们当前这个点的时候呢

其实已经有了他们这个分类的数据了

大家明白吧

所以说呢

我们这个地方只有是新订单的时候

我们保存一次

中转订单的时候呢

其实就已经保存过了

那么这块呢

你看代码比较多对吧

其实呢

我们简单分析一下

首先呢

怎么判断当前这个订单是一个新订单呢

is new

这个其实也比较简单

就是什么呢

其实机构跟当前机构是同一个

它就是新订单

对吧

其实机构跟当前机构是同一个

代表的是新订单

好

所以我们判断啊

is new

就说明它是个新订单

如果是新订单的话呢

我们是不是需要把它转换一下

因为我们这个list是不是

里边装的是这种DTO对象

对吧

还需要进行一个转换

这里边你看它是一堆list的

一堆这个order

对吧

订单

所以说呢

我们在这儿呢

需要把它转换一下

转换成什么呢

我们这种entity对象

是不是来设置什么呢

它的这个分类对吧

就是使用key

还jobid logid

包括什么startagencyid

还有endagencyid

还有total

一共有多少个订单对吧

然后呢

设置它的ID

这个ID呢生成一下

然后这个entity搞定之后呢

在这个地方呢

是不是直接把它save了

那这块是干什么呢

这块其实是在设置我们那个关联表

对不对

设置那个关联表

设置关联表呢

就需要封成这个类

在这里呢

你看我是不是设置什么呢

设置我的这个orderid

对吧

然后就是什么呢

这个分类ID

只不过这个代码写起来呢

是比较繁琐的

然后再生成一个ID

所以你看到这一堆呢

其实就是在设置这个分类

这个关联

对吧

设置关联

然后呢

再批量保存就可以了

这是对于咱们这个新订单

对吧

那么主要操作的就是

我们刚才看到的那两张表

一个是分类

还有一个是关联表

好

然后对于中转订单来说呢

我们就直接拿着他这个什么呢

拿着他把他这个订单的ID是不是都取出来

都给他取出来

取出来之后呢

去查询

去查询就可以

把它原先的我们保存的这个关联信息

是不是给他查出来就可以了

查出来之后呢

然后呢

再把他这个订单的ID

对吧

订单分类的ID给他取出来

这都是进行对象的转换啊

对象类型的转换

基本上全都是用的stream流这种方式啊

转换完之后呢

我们把这个item

item是啥呢

item就是我们这里边一个一个的DTO对吧

然后呢

设置一下他的ID就可以

好

因为什么呢

因为我们在后边呢

会使用到这个ID啊

因为我们当前的是在进行订单分类

分类完成之后啊

后边是不是要进行路线规划

到时候会使用到这个ID

所以说我们在这呢

就是作为中转订单的话

因为已经把这个分类保存过了

所以在这呢

就是给他查出来

查出来之后呢

来设置一下这个ID的值就可以了

好

OK

那么到这的话呢

我们就已经啊

把这个整个所有的订单分类这块呢

就已经搞定了

咱们再来梳理一下

他的主线呢

就是这个方法

execute的方法

对吧

然后这个execute的方法里边呢

主要是分成了这么几个关键的步骤啊

第一个步骤就是什么呢

就是把我们这个网点

或者我们这个转运中心

下边所有的新订单

还有中转订单给他加进来

但是加进来的过程当中啊

构建的过程当中

其实有很多细节对不对

需要去查对吧

然后还要去获取一些

比方说骑士机构啊

中置机构啊

动态去获取

这里面有很多细节问题

那么最终呢

就把我们这些订单

全都装到集合里面去了

装进来之后呢

是不是调用这种方式来进行分类

对吧

分类之后呢

进行保存

所以说主要的思路呢

其实就是这么三个步骤

只不过是在这三个步骤过程当中

有很多细节问题是需要我们去处理的

那么每一个细节问题呢

可能都能展开对不对

所以说整个这个处理逻辑

还是比较复杂的

好

这是咱们关于我们这个订单分类

我们就先说到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”（pd-dispatch）的Java后端系统开发教程，具体聚焦于“智能调度服务”模块中的“订单分类”功能。讲师通过 IntelliJ IDEA 开发环境，演示了如何实现一个订单分类服务，该服务需要处理两种类型的订单：新订单和中转订单。核心内容包括：
- **设计与实现**：创建 `IOrderClassifyService` 接口及其 `OrderClassifyOrderServiceImpl` 实现类。
- **数据模型**：定义了 `OrderClassifyEntity` 实体类，用于存储订单分类记录。
- **业务逻辑**：在 `execute` 方法中，根据传入的 `agencyId`、`jobId` 和 `logId`，查询并分组当前机构下的所有订单，然后根据订单类型（新订单或中转订单）进行不同的处理。
- **数据持久化**：通过 `saveRecord` 方法，将处理后的订单分类结果保存到数据库中，其中涉及对 `OrderClassifyEntity` 的创建、属性设置和批量插入。
- **技术栈**：使用了 Spring Boot、MyBatis-Plus、LambdaQueryWrapper、Lombok 等主流 Java 开发框架和工具。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **00:00 - 00:05**: 项目结构概览。讲师展示了项目 `pd-dispatch` 的目录结构，重点指向 `src/main/java/com/itheima/pinda/service/impl/` 包下的 `TaskOrderClassifyServiceImpl.java` 文件。
- **00:05 - 00:15**: 介绍 `OrderClassifyEntity` 实体类。讲师打开了 `OrderClassifyEntity.java` 文件，展示了其定义，包括 `@TableName` 注解、`@TableId` 注解和 `private` 字段。
- **00:15 - 00:25**: 创建服务接口。讲师在 `TaskOrderClassifyServiceImpl.java` 文件中，定义了 `IOrderClassifyService` 接口，其中包含 `findByJobLogId` 方法。
- **00:25 - 00:35**: 实现服务接口。讲师展示了 `OrderClassifyOrderServiceImpl` 类，其中包含 `getOrderClassifyId` 方法，用于根据订单ID查询分类ID。
- **00:35 - 00:45**: 业务逻辑核心方法 `execute`。讲师展示了 `execute` 方法的完整代码，包括初始化 `orderClassifyDTOS` 和 `orderClassifyGroupDTOS` 列表，以及使用 `Collectors.groupingBy` 对订单进行分组。
- **00:45 - 00:55**: 对象转换与构建。讲师演示了如何使用 `OrderClassifyGroupDTO.OrderClassifyGroupDTOBuilder` 对象将分组后的数据转换为 `OrderClassifyGroupDTO` 类型。
- **00:55 - 01:05**: 保存订单分类结果。讲师聚焦于 `saveRecord` 方法，演示了如何遍历 `orderClassifyGroupDTOS` 列表，根据 `isNew()` 判断是新订单还是中转订单，并分别进行处理。
- **01:05 - 01:15**: 新订单处理逻辑。讲师详细讲解了 `if (item.isNew())` 分支，创建 `OrderClassifyEntity` 对象并设置其属性，如 `classify`、`jobId`、`logId`、`startAgencyId`、`endAgencyId`、`total` 和 `id`。
- **01:15 - 01:25**: 中转订单处理逻辑。讲师讲解了 `else` 分支，用于处理中转订单，包括查询分组信息、获取订单ID列表、调用 `list` 方法查询数据库、处理异常并设置 `orderClassifyIds`。
- **01:25 - 01:35**: 保存到数据库。讲师展示了 `orderClassifyOrderService.saveBatch` 方法的调用，用于将 `orderClassifyOrders` 列表批量保存到数据库。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **文档标题**：`品达物流TMS项目 - 第8章 智能调度服务`
- **子章节**：
  - 3.1 业务说明
  - 3.2 数据模型
  - 3.3 实现过程
    - 3.3.1 基础环境
    - 3.3.2 驱动定时任务
    - 3.3.3 初始化定时任务
    - 3.3.4 完善定时任务
    - 3.3.5 编写智能调度组件
- **关键步骤**：第十三步：创建 `IOrderClassifyService` 接口和对应的实现类，用于操作订单分类表 `pd_order_classify`。

#### 代码关键内容

- **`OrderClassifyEntity` 实体类**：
  ```java
  @Data
  @TableName("pd_order_classify")
  public class OrderClassifyEntity implements Serializable {
      private static final long serialVersionUID = 1L;
      @TableId(value = "id", type = IdType.INPUT)
      private String id;
      private String jobld;
      private String logId;
      // 其他属性...
  }
  ```

- **`IOrderClassifyService` 接口**：
  ```java
  public interface IOrderClassifyService extends IService<OrderClassifyEntity> {
      List<OrderClassifyEntity> findByJobLogId(String id);
  }
  ```

- **`OrderClassifyOrderServiceImpl` 实现类**：
  ```java
  @Service
  public class OrderClassifyOrderServiceImpl extends ServiceImpl<OrderClassifyOrderMapper, OrderClassifyOrderEntity> implements IOrderClassifyOrderService {
      @Override
      public String getClassifyId(String orderld) {
          LambdaQueryWrapper<OrderClassifyOrderEntity> wrapper = new LambdaQueryWrapper<>();
          wrapper.eq(OrderClassifyOrderEntity::getOrderld, orderld);
          OrderClassifyOrderEntity entity = this.baseMapper.selectOne(wrapper);
          return entity.getOrderClassifyId();
      }
  }
  ```

- **`TaskOrderClassifyServiceImpl` 核心方法 `execute`**：
  ```java
  @Override
  public List<OrderClassifyGroupDTO> execute(String agencyId, String jobId, String logId) {
      List<OrderClassifyDTO> orderClassifyDTOS = new ArrayList<>();
      List<OrderClassifyGroupDTO> orderClassifyGroupDTOS = new ArrayList<>();

      // 获取当前机构下的所有订单数据
      orderClassifyDTOS.addAll(buildNewOrder(agencyId));
      orderClassifyDTOS.addAll(buildTransferOrder(agencyId));

      // 进行订单分类
      Map<String, List<OrderClassifyDTO>> orderClassifyDTOGroup = orderClassifyDTOS.stream()
          .collect(Collectors.groupingBy(OrderClassifyDTO::getClassify));

      // 进行对象转换
      OrderClassifyGroupDTO.OrderClassifyGroupDTOBuilder builder = OrderClassifyGroupDTO.builder();
      orderClassifyDTOGroup.forEach((key, value) -> {
          builder.key(key);
          List<Order> orders = value.stream().map(item -> item.getOrder()).collect(Collectors.toList());
          OrderClassifyGroupDTO orderClassifyGroupDTO = builder.build();
          orderClassifyGroupDTOS.add(orderClassifyGroupDTO);
      });

      return orderClassifyGroupDTOS;
  }
  ```

- **`saveRecord` 方法**：
  ```java
  private void saveRecord(List<OrderClassifyGroupDTO> orderClassifyGroupDTOS, String jobId, String logId) {
      orderClassifyGroupDTOS.forEach(item -> {
          if (item.isNew()) {
              log.info("新订单 保存分组信息");
              OrderClassifyEntity entity = new OrderClassifyEntity();
              entity.setClassify(item.getKey());
              entity.setJobId(jobId);
              entity.setLogId(logId);
              if (entity.getClassify().equals("ERROR")) {
                  entity.setStartAgencyId(item.getStartAgencyId());
                  entity.setEndAgencyId(item.getEndAgencyId());
              }
              entity.setTotal(item.getOrders().size());
              entity.setId(IdUtils.get());
              List<OrderClassifyOrderEntity> orderClassifyOrders = item.getOrders().stream()
                  .map(order -> {
                      OrderClassifyOrderEntity orderClassifyOrderEntity = new OrderClassifyOrderEntity();
                      orderClassifyOrderEntity.setOrderld(order.getId());
                      orderClassifyOrderEntity.setJobId(jobId);
                      orderClassifyOrderEntity.setLogId(logId);
                      return orderClassifyOrderEntity;
                  })
                  .collect(Collectors.toList());
              orderClassifyOrderService.saveBatch(orderClassifyOrders);
          } else {
              log.info("中转订单，查询分组信息");
              List<String> orderIds = item.getOrders().stream().map(order -> order.getId()).collect(Collectors.toList());
              LambdaQueryWrapper<OrderClassifyOrderEntity> wrapper = new LambdaQueryWrapper<>();
