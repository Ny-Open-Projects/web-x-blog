# 50-智能调度服务（实现过程_订单分类_19） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才咱们订单分类这个代码已经写完了

包括后边这个对象类型转换是不是也写完了

但是这块代码其实并不是很直观

所以说我们可以自己造一些数据

咱们来测试一下

那么我怎么测呢

我就可以把这块

咱们可以这样

把我们这段代码考到一个Main方法里面去

然后我们来测试一下

咱们来看看这个效果

结合着我们具体的数据来看一下

要不然的话

我们如果只看这个代码的话

可能并不是特别直观

所以说我们在这儿

你看这是咱们的Main方法

前面这是我们也是测试的

这些代码我就保留了

然后我们直接把这个注视起来

然后在下边把这个代码拿过来

但是这个DTOs

它是不是一个List集合

对吧

这个List集合我们也是把它拷过来

这些全都关闭一下

这个代码比较多

找到Execute方法

然后我们直接把这两个List全都拿过来

然后翻到咱们这个地方来

来看

这个是不是封装

封装的是什么

封装的就是我们

这个List集合里边装的

是不是就是我们各种各样的订单

当然是封装成DTO之后的订单

然后这个List集合里边装的

这个就是我们订单分类之后的

需要把它封装到这个List里面去

好

但是这个地方

我们是不是需要对这个List进行一个初始化

对吧

那么如果它这里面没有数据的话

一个订单都没有

那么我们没有办法测试效果来

所以说我们可以把这个数据给它来构造一下

你看它这里边

是不是需要来

Add

添加DTO对象

对吧

添加我们这种DTO对象

所以说我们在这儿来构造几个

DTO1

这个DTO对象我们来构造一下

它也加了Builder了

我们就直接使用它的构造器模式就可以

先让它等于空

然后我们直接通过它的一个构造

Builder来获得一个Builder

就叫Builder1

然后Builder1点什么

注意看

咱们可以来设置一个什么呢

叫什么Start Agency ID对吧

Start Agency ID

比如说是什么呢

1

我们这个ID呢

造简单一点

不造那么长的了

好

还有一个End

这是终止机构对吧

假设是10

然后呢

我们再来

这个还有Carrier呢

这就是当前机构ID对吧

假设当前机构ID呢

就是1

好

这说明它是一个新订单对吧

它是一个新订单

然后呢

在这里边呢

是不是还要关联一个原始的订单对吧

还要关联一个原始订单

因为它这里边是不是有order

好

那我们在这呢

是不是来构造一个订单对象

order

order等于new一个order

这个订单的话呢

咱们就简单设置一个什么呢

设置一个ID就行了

其他属性我就不设置了

其他属性我就不设置了

比方说是1001

好

就设置一个ID

一会儿

我们可以通过断点这种方式能够看到它

能够确认是哪个订单就可以

然后呢

把这个订单对象是不是放进去

好

那这样的话呢

我们通过这个builder

是不是就构建出来第一个

通过builder1.什么的

build方法对吧

然后呢

就构建了一个DTO

DTO1

好

下面这个就不要了

好

那这样的话呢

我们写到这儿的话

其实才是构造了一个对不对

才构造了一个

然后呢我们可以多构造几个啊

把这个代码呢

咱们再来复制两个

好

复制两个

比如说我再再来一个builder2

然后呢

这个构造的

假设它这个start agencyID等于1

然后end

这个呢我们不改

因为什么呢

我们希望能出现这种分组的效果对吧

分组的效果

就是start end还有current是不是都是相同的

那这样的话呢

这个订单呢就会被分成一类啊

这个订单应该就会被分成一类

咱们这个是1002吧

好

然后这个是builder2

这个是other2

所以你看我们测试的话呢

其实造一个数据呢也是比较繁琐的

好

然后呢这是不是又加进来一个

然后呢为了能说明问题呢

我们可以再来造一个

就是什么呢

让他们这个分成不同的类对吧

分成不同的类

这样呢再来一个builder3

然后这个builder3的话呢

我们给它改一下

比如说这个start呢

我给它改成2

对吧

然后end呢改成12

current呢改成11

随便一写就可以啊

好

这些呢都改一下

这个呢第三个订单对吧

这是第三个订单

好

order3

然后呢这个也改一个

好

OK

那这样的话我们这个数据呢

其实就已经构造好了

咱们相当于是造了三个订单对吧

造了三个订单

然后封装成相应的DTO对象

然后呢我们可以看到前两个订单呢

他们的起始机构终止机构

还有当前机构是不是都是一样的

那么我们希望看到的效果是什么呢

就是这两个订单是不是会被分成一类

然后下边这个订单呢

会单独自己是不是分成一类

好

那接下来呢我们就来看一下

最终呢它是不是都放在这个这个机构里面去啊

然后呢我们可以

在这儿呢来打印一下这个机构

在这儿呢我们可以加一个断点

通过断点这种方式来看

直接呢来执行我们这个MIM方法

debug

来看效果

稍等一下啊

好已经过来了

然后呢我们可以看一下

咱们这个集合里边

应该是已经放进去了三个对象

你看size等于3对吧

因为我们前面造完数据了啊

你看

封装的就是这种DTO对象

这个集合里面对吧

这个start呢

一个是前面这两个是相同的

后边这个是不一样的对吧

好

然后呢订单的ID呢

咱们是不是用的也是不一样的

这个订单的ID是多少呢

是

这个ID好像有点问题啊

关联的这个订单ID怎么等于空呢

是不是刚才我们写的代码有问题啊

你看这个ID是不是都没了啊

这个ID都没有设置进来

然后呢我们来看一下啊

咱们先把这个程序停一下

看看有什么问题没有

这个地方有问题啊

我们应该是没有改彻底对吧

来看一下啊

这个是order对吧

有一个order

然后呢在这儿把它加进来

前面这个是没问题的

然后后边

这个地方我们是不是没有改全对吧

因为都是改造过来的啊

然后这个需要来设置order2对吧

然后呢

同样是这个地方

这应该是order3

所以说呢我们通过断点这种方式啊

就很容易看出问题来

然后呢重新再来执行一下

先保证我们造的这个数据呢是没有问题的

然后我们再看下边

再来观察一下

这下边

呃

第一个订单

它的ID是1001

没问题

然后第二个订单对吧

它的ID是1003对吧

然后这个呢

订单呢是

嗯

这个好像也没有设置上

那等于刚才我们改的好像还是有点问题啊

来看一下

啊

这个地方对吧

这应该是order3

好

这个应该是order2

好

这个没问题

然后重新再来

好

然后呢我们来看一下

第一个订单1001

没问题

然后第二个订单1002

没问题

然后第二个订单1003

没问题

然后第三个订单1002也没问题

然后再来看第三个订单

是1003好

现在也没问题

然后呢我们这个既然没有问题

我们就可以直接往下走对吧

往下走

注意看啊

它经过这个计算之后呢

会给我们返回一个map

而这个map我说key是什么呢

key应该就是我们那个GrooveBy方法

它的返回值

value呢就是

哎

那个

收集上来的订单这个DTO对吧

哎

当然是集合

你看现在size是不是变成2了

我们原始的订单是3个对吧

而现在这个map它的size是2

说明什么呢

说明一共分成了两类

对吧

你看

第一类呢是什么呢

你看是这个2-12-11

这是什么呢

这是不是对应的就是我们current ID

什么end

end什么agency ID

还有什么current agency ID

对吧

start agency ID等等这些

好

然后呢size是1

说明它这个下边

哎只有一个

你看

这个DTO对象对吧

这个应该是ID是1003的那个

因为它自己归成了一类

然后呢另外两个呢是归成了一类

因为什么呢

因为他们计算之后这个key是相同的

好

然后呢你看key是这个

value呢是一个粒子集合

粒子的里边装的

都是一个一个的DTO对象

而每一个DTO对象里边是不是就封装了原始的这个订单

好

所以大家仔细看啊

因为我们这儿呢这个对象的封装呢比较复杂

对吧

套的比较深

啊

你看这个

这是1002

好

所以从这儿呢我们来看一下这个数据啊

应该就能看清楚了

对吧

哎这是我们对原先的这个list集合进行了一个分组

最终返回了一个map

好

然后接下来呢我们是不是对这个map进行处理

对吧

来便利它

好

便利它

哎呀

这里边呢没有直接全都执行完了

对吧

执行完之后呢

我们就看这个list的集合吧

因为在这里边的话

它是不是会会把我们这个对象创建出来

然后加到这个集合里面去

现在你看这个集合的size是不是等于2

size等于2

然后呢这里边你看有key对吧

有key

然后还有什么呢

还有这个others

这是刚才我们设置的

key的话呢就是我们刚才看到的这个key

others呢这里边关联的就是原始的订单对象

原始的订单对象

但是这个呢是单独分成了一类那个

好

然后呢这是另外一个

这里边这个others是不是包含两个原始的订单

你看这不是order对象吗

好

就是这个样子的

这个呢就是我们自己啊造了一些这个数据对吧

然后呢通过断点这种方式能够看到什么呢

经过我们这个代码处理之后

它的数据格式到底是一个什么样子

好

这是关于我们刚才写的代码呢

我们进行了一个测试

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频演示了一个 Java 项目中“订单分类服务”的核心逻辑。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何将一组订单（`Order` 对象）根据其所属机构（`agencyId`）进行分组，并将分组后的结果封装成一个更复杂的分组数据传输对象（`OrderClassifyGroupDTO`）。整个过程涉及 Java Stream API、`Collectors.groupingBy`、`Builder` 模式以及对百度地图 API 的调用以获取地理位置信息。视频重点在于展示如何将原始数据结构转换为业务所需的聚合结构，并通过调试输出验证了转换结果。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开场，展示 `TaskOrderClassifyServiceImpl.java` 文件，讲师准备演示订单分类逻辑。
*   **00:00:05 - 00:00:15**: 讲师开始编写代码，创建 `OrderClassifyDTO` 对象并添加到 `orderClassifyDTOS` 列表中。
*   **00:00:15 - 00:00:30**: 讲师使用 `Stream` API 和 `Collectors.groupingBy` 对 `orderClassifyDTOS` 进行分组，生成 `Map<String, List<OrderClassifyDTO>>`。
*   **00:00:30 - 00:00:45**: 讲师创建 `OrderClassifyGroupDTO.OrderClassifyGroupDTOBuilder`，并遍历分组结果，将每个分组中的 `Order` 对象提取出来，构建新的 `OrderClassifyGroupDTO` 对象并添加到 `orderClassifyGroupDTOS` 列表中。
*   **00:00:45 - 00:01:00**: 讲师在 `main` 方法中创建了三个 `Order` 对象，并分别使用 `OrderClassifyDTO.Builder` 构建了三个 `OrderClassifyDTO` 对象，模拟了不同机构的订单。
*   **00:01:00 - 00:01:15**: 讲师将三个 `OrderClassifyDTO` 对象添加到 `orderClassifyDTOS` 列表中，并再次调用 `groupingBy` 进行分组。
*   **00:01:15 - 00:01:30**: 讲师通过 `System.out.println` 输出 `orderClassifyGroupDTOS` 的内容，验证分组转换结果。
*   **00:01:30 - 00:01:45**: 讲师在调试器中查看 `orderClassifyGroupDTOS` 的内容，确认分组逻辑正确执行。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **核心代码逻辑**:
    *   **分组转换**:
        ```java
        Map<String, List<OrderClassifyDTO>> orderClassifyDTOGroup = orderClassifyDTOS.stream().collect(Collectors.groupingBy(OrderClassifyDTO::getAgencyId));
        ```
    *   **构建分组对象**:
        ```java
        OrderClassifyGroupDTO.OrderClassifyGroupDTOBuilder builder = OrderClassifyGroupDTO.builder();
        orderClassifyDTOGroup.forEach((key, value) -> {
            builder.key(key);
            List<Order> orders = value.stream().map(item -> item.getOrder()).collect(Collectors.toList());
            builder.orders(orders);
            OrderClassifyGroupDTO orderClassifyGroupDTO = builder.build();
            orderClassifyGroupDTOS.add(orderClassifyGroupDTO);
        });
        ```
*   **模拟数据**:
    *   讲师创建了三个 `Order` 对象，分别设置 `orderId` 为 `"10001"`, `"10002"`, `"10003"`。
    *   使用 `OrderClassifyDTO.Builder` 构建了三个 `OrderClassifyDTO` 对象，分别设置 `startAgencyId`, `endAgencyId`, `currentAgencyId`。
*   **调试输出**:
    *   `System.out.println(orderClassifyGroupDTOS);`
    *   调试器中显示 `orderClassifyGroupDTOS` 的内容，确认分组成功。

---

### 4) 关键场景与演示描述

*   **场景一：分组逻辑演示**
    *   讲师首先在 `main` 方法中创建了一个 `OrderClassifyDTO` 对象 `dto1`，并将其添加到 `orderClassifyDTOS` 列表中。
    *   接着，讲师使用 `Stream` API 和 `Collectors.groupingBy` 对 `orderClassifyDTOS` 进行分组，生成一个 `Map<String, List<OrderClassifyDTO>>`。
    *   讲师通过 `forEach` 遍历分组结果，将每个分组中的 `Order` 对象提取出来，构建新的 `OrderClassifyGroupDTO` 对象并添加到 `orderClassifyGroupDTOS` 列表中。
    *   最后，讲师通过 `System.out.println` 输出 `orderClassifyGroupDTOS` 的内容，验证分组转换结果。

*   **场景二：模拟数据与分组结果验证**
    *   讲师在 `main` 方法中创建了三个 `Order` 对象，分别设置 `orderId` 为 `"10001"`, `"10002"`, `"10003"`。
    *   讲师使用 `OrderClassifyDTO.Builder` 构建了三个 `OrderClassifyDTO` 对象，分别设置 `startAgencyId`, `endAgencyId`, `currentAgencyId`。
    *   讲师将三个 `OrderClassifyDTO` 对象添加到 `orderClassifyDTOS` 列表中。
    *   讲师再次调用 `groupingBy` 进行分组，并通过调试器查看 `orderClassifyGroupDTOS` 的内容，确认分组逻辑正确执行。

*   **场景三：调试器验证**
    *   讲师在调试器中查看 `orderClassifyGroupDTOS` 的内容，确认分组逻辑正确执行。
    *   讲师通过 `System.out.println` 输出 `orderClassifyGroupDTOS` 的内容，验证分组转换结果。

---

以上是根据视频画面进行的结构化技术分析报告。
