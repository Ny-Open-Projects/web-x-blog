# 15-用户注册-全局序列号生成方案 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着的话呢

咱们开始实现了全局序列号的生成方案

咱们来看一下整体的实现步骤是怎样的

全局序列号呢

它可能会在多处出现去使用

所以呢

我们把它放在store common system的公用主件下面

第二呢

这种方式适合并发量并不大的业务场景

对高频度的交易场景呢

我们要去结合缓存去使用

因为会存在一个IO瓶颈的问题

这个呢

是全局序列号方案生成的一些缺陷

如果说我们不需要保持全局序列号

也就是说不要保证它的有序性呢

可以采用雪花算法

它的速度来讲

因为是基于内存型的一个计算

所以呢

它的速度要比这种基于数据库的方案呢

会快很多

那么咱们来看一下

基于数据库的这种方案来讲

如果是产生了IO瓶颈问题

咱们有没有更好的办法去做一个优化呢

这个时候呢

可以结合缓存去做使用

具体怎么去做呢

那么既然会产生这个IO瓶颈

我们呢

可以做一个什么事情呢

做一个预分配

预先去进行分配

也就是先拿出一段序列号

再去分配

在业务场景中去使用

这个呢

是它的一个缺陷的一个弥补方案

在这里呢

咱们呢

给大家去实现全局序列号

那么缓存这一块呢

大家有时间可以呢

再去做一个研究

去拓展一下这块的方案

和相关的知识学习

那么我们这个全局序列号的生成

为了保证它的唯一性

咱们想想

这个呢

怎么去保障呢

因为数据库的操作会存在一个什么问题啊

资源的竞争问题

对不对

大家有很多个现成

都可以呢

对这个全局序列号的这张表呢

进行操作

那么这么多并发现成过来的时候呢

咱们要怎么去处理呢

如果是加索

加索的方式呢

当然可以保证全局序列号的生成

但是呢

加索会不会存在什么问题呢

它就会存在了

整个性能会出现大幅的降价

因为呢

它要去什么排队等待

相当于话呢

其他现成全部阻塞了

对不对

这个呢

就是它的一个缺陷

影响了效率

好

那么有没有

更好的方案呢

这个呢

这个呢

实际上也有

那怎么去做的呢

在数据库里面呢

咱们基于买色口的特性

可以通过它的一个方法

也是一个函数

拉似金色的ID

去生成了我们所需要的序列号

这个呢

就能够呢

快速的生成全局有序的序列号

也就是我们本章呢

所实现的方案

那么咱们知道

这样的实现来讲呢

咱们去加索

这个呢

也能实现

对不对

但是咱们实现过程当中呢

还要注重一个非常重要的方面

就是呢

要考虑好性能

就是做任何功能的话

我们要

不仅要保障稳定性

同时呢

还要考虑好性能

这样的话呢

你这个方案

才是一个有效的

靠谱的解决方案

好

那咱们呢

就来看一下

这块呢

具体是如何实现的

咱们在数据层里面呢

先定义一个接口

这个接口的方法名称呢

是根据编号来获取呢

序列号ID

编号呢

就相当于是不同的业务类型

对吧

如果是用户表

那么在这里的话呢

它就要去生成用户编号

如果是呢

订单表

对不对

那么呢

就要生成订单编号

根据你的不同类型

传递的参数呢

来决定了

我所生成的全局序列号

这样的话呢

我们就可能支持

多种业务场景的运用

保障呢

整体全局的唯一性

当然这个呢

并不是说基于用户编号

还有订单编号

去生成的全局唯一

而是说用户编号在这里呢

生成一个全局唯一

订单编号呢

也生成一个全局唯一

好

那咱们来看一下

它的一个map

是怎么去做的呢

map文件呢

通过update

它来获取一个自身的ID

最属性名称和类型呢

咱们不要填错

好

那咱们呢

就来看一下具体的代码

打开咱们的common system

下面的话呢

有个

iShare的global config.do

对不对

那这里呢

咱们可以看到

get next by ID

对不对

那咱们看一下

它具体的实现

关键呢

是在于circle的实现

circle在这一块呢

咱们可以看到

它传了一个什么

key

对不对

这个key是什么

next ID

这个property属性呢

也是next ID

咱们看一下

这段circle

具体是什么含义呢

它是update

提circle这个表

将它的next ID

也就是存储我们全局区的

ID的这个属性呢

进行了一个什么

累加

但咱们可以看到

这种累加方式呢

并非直接的累加

对不对

它外面呢

加了一个函数

然后呢

咱们可以看到

它传了一个code

根据这个code呢

去设定了

它指定的全局区的ID

最后呢

它要去circle这个key

然后呢

获取到最新的xID

这个呢

有点类似于呢

新增的表数据

对不对

咱们在新增一条数据的时候呢

咱们记不记得

在这组件的时候呢

就会circle那属性的ID

对不对

同样的道理

在这里面呢

咱们去修改了

nextID

那么呢

它会将它最新的返回结果呢

作为一个key

那么设置到哪里呢

设置到这个nextID里面

也就是为什么咱们在这里呢

要传递一个参数对象

对不对

而不是传递一个参数属性

那么咱们再具体一点

结合了具体的表结构

来做一个讲解

可以看到tcircle这个表

它的表结构呢

在这里面呢

咱们扩大一点

它是一个code

对不对

组件标识

下面呢

是一个下一个虚拙号的ID

那么

primary key

组件是谁呢

是code

那咱们看一下

它具体的值是怎样的

在这里面的话呢

有两条记录

一个呢

是交易账号的编号

另外呢

是用户账号的编号

对不对

好

那么基于这个表结构呢

非常简单

那咱们呢

看这个circle

就应该呢

能明白它的意思

对不对

就是呢

将这个值

然后呢

通过lasting色的ID

为什么要加这个函数呢

因为呢

它能保证整个操作的原子性

如果说咱们在这里

直接累加

咱们想想

另外一个线程呢

也做同样的操作

对不对

你先要什么

你要累加的时候

你是不是先要查到它的值

对吧

你要先知道它当前nextID是多少

在你查它的值的过程当中

其他另外一个线程

就抢占了你的资源

查到对应的nextID

那么这样呢

就会带来数据的不一致

产生了涨读换读的现象

好

这也就是为什么要讲

lasting色的ID

这个函数的作用

希望这一点呢

大家要理解清楚

再往下面呢

咱们来看一下

service层的一个

实现

那service层呢

它的实现就比较简单

因为呢

咱们没有加任何所处理

对不对

咱们可以看一下

teacher.global.config.service

那么呢

找到对应的实现类

看到没有

在这里呢

它只是传递对应的code

对不对

你的业务类型

然后呢

去获取对应的ID

那么它会将它的最新的nextID呢

放到sequence对象里面的

nextID这个属性里面

然后呢

你直接将这个属性返回

这样呢

就取到了指定序列的增长ID

好

这个呢

就是它

service层接口的一个实现

那么咱们呢

再往下面看

那么stock user service

在这一块怎么去运用呢

咱们可以看到

打开这个service

应该是用户

它注册时候

要去生成的

对不对

注册的接口呢

咱们先暂时还没有实现

咱们呢

先把序列号方法呢

实现完成之后

在下面的服务层呢

再去实现它的注册接口

将这个方法copy过来

好

咱们来看一下

它的这个处理逻辑是怎样的

把这个service注入下

在上面

因为它是一个公用的主线

对不对

common system

要引入进来

找到了咱们的POM文件

在这里面呢

加上它的公用主线依赖

直接呢

在这里copy一下

公用的系统层依赖

它的模块名称呢

是system

导入完成之后呢

咱们再回来看看

咱们再回来看看

回到刚才

将这个接口呢

导入进来

它已经导入完成

咱们可以看到

生成用户编号呢

实现起来就非常简单了

因为咱们把底层这块呢

全部打通了

它怎样呢

直接去调用这个service

对不对

拿到呢

它指定序列的增长ID就可以了

咱们呢

也不用去考虑它的现成安全性等问题

因为底层这一块呢

数据库就已经帮我们考虑到了

这种并发所产生的问题

能够呢

保证生成了全局的唯一序列ID

好

那么在这个处理的时候呢

因为咱们用户编号

生成的时候呢

大家想想

这个用户编号的生成呢

会有一定的格式

这个长度呢

咱们是固定的

比如说固定的是8位长度

8位长度

你下面所生成的

这个用户账号

如果是

有的是123

对吧

有的长度呢

又是4位

12345

就长度不一样

这样的话呢

这个整个用户编号

是不是看起来非常不值款

对不对

那所以的话呢

咱们要做一个什么事情啊

就是保证呢

他们都是统一的长度

那比如说这个123

最后呢

就会变成8位吧

1235

5个0

然后是123

在这里面呢

它本来就有5位

对不对

那它就要铺几个0了

铺3个0

12345

好

这个呢

就变成一个

有一定规律的用户编号

对吧

在这里呢

就做了一个补0的处理

这个呢

是它的作用

就是生成了固定8位的长度

好

百分之号

然后08

0表示补0

那么后面的话呢

是标识的

就是它的一个长度

如果是你想生成9位呢

在这里改成9D就可以了

好

在这一块呢

就是对全局序列号

生成方案的具体实现

那这一讲呢

咱们就讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出：

---

### 1) 视频摘要

本视频课程主要讲解了在分布式系统中如何实现一个**全局唯一序列号（ID）生成方案**，并将其应用于用户注册功能中。讲师通过一个名为 `bulls-stock` 的项目，演示了如何将该方案封装为一个公共组件 `stock-common-system`，并集成到业务模块中。整个实现过程包括：定义数据层接口、编写 MyBatis Mapper 文件、实现 Service 层逻辑、以及在业务代码中调用。同时，视频也展示了如何在用户注册流程中，利用该序列号生成器来生成符合业务规则的用户编号。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程引入，展示当前正在讲解的章节是“3.6 全局序列号生成方案”。
*   **00:16 - 00:30**: 讲解全局序列号方案的适用场景和设计思路，强调其在多业务系统中的复用性，并指出对于高并发场景，可以结合缓存或采用雪花算法。
*   **00:31 - 00:45**: 展示数据层接口 `ITradeGlobalConfigDao` 的定义，包含 `getNextId(TradeSeq record)` 方法。
*   **00:46 - 01:00**: 展示对应的 MyBatis Mapper XML 文件，其中包含 `update` 语句用于自增 ID，以及 `selectKey` 语句用于获取 `LAST_INSERT_ID()`。
*   **01:01 - 01:15**: 展示 Service 层接口 `ITradeGlobalConfigService` 的定义。
*   **01:16 - 01:30**: 展示 Service 层实现类 `TradeGlobalConfigServiceImpl` 中的 `getNextSeqId` 方法，该方法调用 DAO 层获取序列号。
*   **01:31 - 01:45**: 展示在用户注册 Service 中如何调用 `TradeGlobalConfigService` 来生成用户编号。
*   **01:46 - 02:00**: 展示如何在 `pom.xml` 中引入 `spring-cloud-starter-alibaba-sentinel` 和 `sentinel-datasource-nacos` 依赖，为后续的限流功能做准备。
*   **02:01 - 02:15**: 展示项目结构，重点说明 `bulls-stock-common-system` 这个公共组件的目录结构和依赖关系。
*   **02:16 - 02:30**: 展示 `TradeGlobalConfigService` 的实现类 `TradeGlobalConfigServiceImpl` 的完整代码，以及 `generateUserNo` 方法的实现细节。
*   **02:31 - 02:45**: 展示用户注册接口 `IStockUserService` 的定义。
*   **02:46 - 03:00**: 展示用户注册的 Service 实现类 `StockUserServiceImpl`，其中包含了用户登录限流规则的处理逻辑。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容

*   **章节标题**: “3.6 全局序列号生成方案”
*   **核心要点**:
    1.  全局序列号可多处复用，实现放在 `stock-common-system` 公用组件下。
    2.  适用于并发量不大的业务场景；高并发场景可结合缓存或用雪花算法。
    3.  数据层定义接口 `ITradeGlobalConfigDao`。
    4.  Mapper 文件通过 `update` 获取自增 ID。
    5.  Service 层接口实现。

#### 代码关键内容

*   **数据层接口 (`ITradeGlobalConfigDao`)**:
    ```java
    /**
     * 根据编号获取序列ID
     * @param code
     * @return
     */
    int getNextId(TradeSeq record);
    ```

*   **Mapper XML 文件**:
    ```xml
    <update id="getNextId" keyColumn="nextId" keyProperty="nextId"
            parameterType="com.ictast.trade.stock.entity.system.TradeSeq">
        update t_seq set nextId = last_insert_id(nextId + 1) where code = #{code};
        <selectKey resultType="long" keyProperty="nextId" keyColumn="nextId">
            SELECT LAST_INSERT_ID()
        </selectKey>
    </update>
    ```

*   **Service 层接口 (`ITradeGlobalConfigService`)**:
    ```java
    public interface ITradeGlobalConfigService {
        Long getNextSeqId(String code);
    }
    ```

*   **Service 层实现 (`TradeGlobalConfigServiceImpl`)**:
    ```java
    @Override
    public Long getNextSeqId(String code) {
        TradeSeq seq = new TradeSeq();
        seq.setCode(code);
        tradeGlobalConfigDao.getNextId(seq);
        return seq.getNextId();
    }
    ```

*   **用户注册 Service 中的用户编号生成方法 (`generateUserNo`)**:
    ```java
    private String generateUserNo() {
        // 获取用户账号
        Long nextUserNo = tradeGlobalConfigService.getNextSeqId(GlobalSeq.USER_NO);
        log.info("get the next userNo : " + nextUserNo);
        // 其中0表示补零，后面标识长度
        return String.format("%08d", nextUserNo);
    }
    ```

*   **用户登录限流规则处理代码**:
    ```java
    if (abstractRule instanceof DegradeRule) {
        throw new ComponentException(ApplicationErrorCodeEnum.SYS_DEGRADE);
    } else if (abstractRule instanceof FlowRule) {
        throw new ComponentException(ApplicationErrorCodeEnum.SYS_FLOW);
    } else {
        throw new ComponentException(ApplicationErrorCodeEnum.FAILED);
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：全局序列号方案设计**
    *   讲师在 PPT 上展示“3.6 全局序列号生成方案”章节。
    *   通过文字描述，说明该方案的适用范围和设计原则，强调其可复用性。

*   **场景二：数据层接口与 Mapper 实现**
    *   讲师在 IDE 中展示 `ITradeGlobalConfigDao` 接口定义。
    *   切换到 Mapper XML 文件，演示如何使用 MyBatis 的 `update` 和 `selectKey` 标签来实现自增 ID 的获取。

*   **场景三：Service 层实现与调用**
    *   讲师在 IDE 中展示 `TradeGlobalConfigServiceImpl` 的实现代码。
    *   展示如何在 `StockUserServiceImpl` 中调用 `tradeGlobalConfigService.getNextSeqId(GlobalSeq.USER_NO)` 来获取用户编号。

*   **场景四：项目结构与依赖管理**
    *   讲师在 IDE 中展示项目结构，重点指出 `bulls-stock-common-system` 这个公共组件。
    *   在 `pom.xml` 中添加 `spring-cloud-starter-alibaba-sentinel` 和 `sentinel-datasource-nacos` 依赖，为后续功能做准备。

*   **场景五：用户注册功能集成**
    *   讲师在 `StockUserServiceImpl` 中展示 `generateUserNo` 方法的实现。
    *   该方法通过 `tradeGlobalConfigService` 获取序列号，并使用 `String.format("%08d", ...)` 格式化为 8 位数字，作为用户编号。

*   **场景六：限流规则处理**
    *   讲师在 `StockUserServiceImpl` 中展示用户登录时的限流规则处理逻辑。
    *   通过 `if-else` 判断不同的限流规则（降级、流量控制），并抛出相应的异常。

---

以上是根据视频画面整理出的技术课程结构化信息。
