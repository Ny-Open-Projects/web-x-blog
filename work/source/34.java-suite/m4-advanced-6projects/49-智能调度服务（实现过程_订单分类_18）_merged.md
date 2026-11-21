# 49-智能调度服务（实现过程_订单分类_18） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢继续来看咱们的程序

刚才呢我们是已经完成了整个build transfer order这个方法

这个呢就是构建我们中转订单对吧

那么中转订单呢获取出来之后呢

同样是把它加到这个集合里面去

好那么程序呢到这之后呢

相当于我们的新订单还有中转订单呢

都已经加到这个集合里面来了

那接下来呢我们就要对这个集合里面所有的这些订单呢

来进行一个什么呢分类对不对

所以下边呢就是对这个订单进行分类

那么我们需要来说一下

我们需要把这些订单进行分类

需要按照什么规则来进行分

也就是说什么样的订单会分成一类呢

注意看啊在我们这个DTO里面

这是我们封装的这个DTO对吧

Other Classified DTO

那么在这里边呢我们提供了这么一个方法

叫做Group By

这个方法非常重要

一会儿呢我们

就要使用到它

而这个方法呢就是用来对我们当前这个类

因为这里面封装的是不是就是我们

这个分类之后的那个订单对吧

这是原始的订单

然后呢

我们把它封装成了这个DTO对象

那么一会儿呢我们要进行订单分类

就会使用到这个方法

这个方法呢

它就是作为我们分类的依据

那么大家可以看一下

咱们这个Group By呢

你看它是不是会返回这么一个

就是这个值

而这个值是怎么拼起来的呢

大家来看一下

是什么呢

是我们这个Start Agency ID

这是不是就是起始机构的ID

然后呢再加上一个井号

再加上End Agency ID

然后再加上一个井号

再加上什么呢

Current Agency ID

这是不是指的就是我们当前机构的ID

那也就是说我们是不是

运用这个方法

它就会返回这么一个字符串

而这个字符串相同的情况下

订单呢就会被分成一类

所以呢

我们的分类依据其实就是什么呢

就是使用这么三个维度啊

一个是起始机构

一个是终止机构

对吧

还有一个就是当前当前机构

那么如果是相同的话

那么这些订单呢

就会被归成一类

所以我们这个方法

也就是当我们调用这个方法

那么反位值相同的情况下

这两个订单呢

就会被分成一类

这是咱们这个格入败

这个方法

好

那接下来呢

我们来看一下

如何来具体代码

如何来写进行订单分类

你看我们现在呢

是已经把这个新订单

还有中转订单

都已经放到这个集合里面去了

对吧

那么要进行订单分类的话呢

其实非常简单

直接调用什么呢

调用这个stream流

对吧

获得一个流对象

然后呢

我们直接调用clack的收集

那相当于

我就把这个集合里面的

这个数据收集上来

收集上来

的同时呢

来进行一个什么呢

来进行一个分类

所以这儿呢

有个collectors点什么呢

你看有个叫grouping by

然后呢

进行分组对吧

也就是说

对我们这个集合里面

这些订单进行分组

那么分组的时候

是根据什么分呢

依据呢

我们刚才说了

是不是就是这个类里面的

这个方法

对吧

所以说呢

我们可以使用这种语法

把这个类名考过来

好

两个冒号

对吧

然后呢

格入败

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

哎

针对每一个

针对每一个

DTO对象

是不是都去调永格入败

这个方法

然后呢

如果这个方法

相同的

返回值相同的

这些DTO呢

会被分成一类

好

刚才我们也看了

就是通过这三个

三个属性

作为维度

对吧

好

那么这样的话呢

它就会给我们

分好类

那这样的话

这个返回值是什么呢

其实是一个map

哎

大家看

是一个map

好

然后我们这个map呢

就叫什么呢

就叫order classifier DTO group

这是不是已经分好组了

注意看啊

我们返回值呢

是一个map

map的key呢

是什么呢

key的话

其实就是咱们这个group by方法

它的返回值

不是这个group by啊

是我们刚才调的这一个group by方法

它的返回值

作为key

而value是什么呢

而value就是一个list集合

就是一个list集合

这个集合里面装的是什么呢

就是我们多个

多个这个DTO对象

封装成的集合

这就表示当前这几个订单

是不是被分成了一类

被分成了一类

比如说我们举个例子

假设在我们这个网点对吧

那么我们一共呢

是新订单加上中转订单的

一共是有1000个订单

对吧

然后这1000个订单呢

很有可能被分成几十类

对吧

被分成几十类

那这样的话呢

我们最终得到的这个map呢

其他的key呢

就是我们刚才看到那个group by

它的返回值

因为他们的起始机构

终止机构

包括当前机构都是相同的

而这个value呢

就是每一类下边具体的这些单子

当然了这些单子呢

我们再强调一遍

它是封装成了DTO这种方式

这种对象

在这里边是不是就关联了

我们原始的订单

好

这是进行订单分类

好

订单分类完成之后呢

我们就需要干什么呢

对这个map对象呢

进行一个转换

为什么要进行转换呢

因为我们这个方法要求返回的

其实是一个例子的集合

对不对

是个例子集合

而现在呢

我们分类完成之后呢

它是一个map

所以呢

我们接下来呢

需要来进行一个对象转换

然后将我们当前这个

什么

map对象转为什么呢

转为这种对象

例子的

然后里边放的是这种DTO对象

这种类型

好

这就是对象的一个转换

对吧

对象的一个转换

那么这个对象具体怎么转呢

咱们来看一下

我们是不是需要把这个map便利一下

然后呢

把这里边的key

还有value取出来

对吧

然后想办法给它封装成这种对象

然后再扔到例子集合里面去

就可以了

咱们可以来看一下

我们可以来看一下

我们要封装成这个

你看

这里边是不是就是key

然后对应的还有什么呢

还有others

这就是我们原始的订单集合

对吧

所以说封装成这种对象呢

是比较好用的

方便我们后边进行处理

因为我们当前呢

只是我们真正这个智能调度的第一步

就是订单分类

对吧

分类之后呢

后边还要进行相应的其他的

比如说路线规划

对吧

司机的规划

还有这个什么呢

一些这个工作单的一些生成等等

所以说

我们现在就需要对我们当前这个map对象来进行一个转换

转换成这种类型

方便后面程序使用

好

所以这样的话

我们就需要把这个map来进行一个便利

便利map其实也比较简单

直接调用什么

调用它的4-H方法

是不是就可以

然后呢

便利出来之后

是不是就是一个一个的key value

对吧

所以说我们在这可以写一个Lambda表达式

key

然后呢

value

key value

而这个key是谁呢

对应的就是这个

那么具体它的值呢

就是我们刚才反复强调的这个GrooveBind方法

它的返回值

这就是它的key的值

好

然后呢

我们刚才提到

我是不是需要给它封装成粒子集合

对吧

首先呢

我们先封装成这个对象

然后再一个一个加到粒子里面去

是不是就可以了

而这个对象怎么获得呢

咱们可以使用它的构建器模式

先获得一个builder对象

对吧

获得一个builder对象

然后呢

在这里边呢

我们就可以通过builder.key来指定什么呢

指定我们这个DTO里边

这个key

这个字段它的值

代表的是什么

这个key代表的就是分组的维度

对不对

好

OK

这个key是不是就设置好了

然后呢

我们还要设置一个什么呢

还要设置一个就是它的Others

就是原始的订单集合

这就表示这一堆订单是分成了一类

对吧

所以我们就需要把这个原始的订单集合给它设置好

而原始的订单集合呢

通过这个value就能够获得

为什么呢

因为我们这个map里边

你看它所对应的value是不是就是这个粒子的

而在这里边

粒子里边都是封装的一个一个的DTO

而每一个DTO里面是不是都有一个order

所以说呢

我们就可以从这个value里边

干什么呢

来把我们这个原始的order对象是不是给它获得

而现在这个value对应的是一个粒子的集合

对吧

所以说呢

我们需要从这个value出发

注意看

然后呢

还是通过stream流

对吧

然后调用map方法来遍历

遍历一个一个DTO出来

对吧

这里边呢

每一个都是一个DTO

然后呢

我们在这要谁呢

是不是要我们这个DTO里边的那个order对象

order对象

所以说呢

我们这里边呢

直接通过item.getorder

这样是不是就获取到

然后呢

把它收集起来collect的

然后呢

转成list的就可以了

这样的话呢

我们相当于就把orders是不是给原始的订单

获取原始订单

获取原始订单对象

然后呢

再通过这个构建器builder呢

来设置orders

ok

设置好了之后呢

我们是不是需要给它封装成一个什么呢

封装成一个DTO对象

对吧

对吧

我们可以把这个dto的这个dto

这个dto的这个dto

这个dto对象对吧

所以我们通过这个builder.build的方法

来构建对吧

来构建

这样我们这个dto是不是就已经

创建好了

就已经创建好了

创建好之后呢

咱们是不是就可以干什么呢

把这个dto啊

把它加到我们这个list的集合里面去了

好

在这点什么呢

add

好

然后呢

把上面这个order什么

groupDTO给它创建

给它加进去

就可以了

所以大家来看一下

这块的话呢

这个代码写起来呢

其实还是挺繁琐的

那么大家呢

只要知道啊

我们这块其实就是做了一个对象的转换

对不对

就是把我们这个订单分类之后的这个结果

因为它是一个map

需要转换成一种类型

转换成哪种类型啊

我最终想要的其实是这种类型

对不对

是一个list集合

所以说呢

我们需要把这个map进行一个便利

for each是不是就是在便利这个map

好

便利的时候呢

每一次便利出来之后呢

是不是就是一个简直就是key value

所以我们在这通过key value这种方式来描述

对吧

这其实就是一个Lambda的表达式

然后呢

在这里边

我们要构建这个DTO对象呢

是通过这个

通过它提供的一个builder

构建器这种模式

因为在DTO上

上面咱们是不是加了builder这个注解

好

这样的话呢

我把这个构建器创建出来

然后呢

设置它这里边的两个属性就可以了

一个是key

对吧

这个key的话呢

直接对应的就是我们这个key

然后还有一个就是什么呢

others

而这个others怎么获得呢

是通过我们这个value

而这个value对应的是不是就是一个list集合

我们需要把它处理一下

转换成这种类型

对吧

转换成这种类型

然后给它加进去

然后呢

再把这个DTO对象是不是

调用build方法构建出来

最后呢

再把这个对象加到我们外围的这个

已经创建好的这个集合里面去

就可以了

最终呢

我们其实返回的就是这个集合

好

所以这块呢

咱们就已经完成了什么呢

订单分类

然后呢

对数据进行一个转换

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段展示了一个 Java 项目中订单分类服务的代码实现过程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何将原始订单数据（`OrderClassifyDTO`）根据机构和类型进行分组，并将分组后的结果转换为一个新的数据传输对象（`OrderClassifyGroupDTO`）。核心内容包括：
- 定义用于封装原始订单信息的 `OrderClassifyDTO` 类，其中包含分组所需的字段（如 `startAgencyId`, `endAgencyId`, `orderType`）和一个自定义的 `groupBy` 方法。
- 在 `TaskOrderClassifyServiceImpl` 服务类中，通过 `Stream` API 对订单列表进行分组操作，使用 `Collectors.groupingBy`。
- 使用 `OrderClassifyGroupDTO` 的 Builder 模式，将分组后的 `Map<String, List<OrderClassifyDTO>>` 结构转换为 `List<OrderClassifyGroupDTO>`，以便于后续的数据库存储或业务处理。

整个过程体现了 Java 中函数式编程（Stream API）和 Builder 模式的应用，旨在实现数据的高效分组和转换。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 展示 `OrderClassifyDTO` 类的定义，包含分组字段和 `groupBy` 方法。
*   **00:00:05 - 00:00:10**: 展示 `TaskOrderClassifyServiceImpl` 类中的 `execute` 方法，用于处理订单分类逻辑。
*   **00:00:10 - 00:00:15**: 代码中创建 `orderClassifyDTOs` 和 `orderClassifyGroupDTOs` 列表，并添加新订单和中转订单。
*   **00:00:15 - 00:00:20**: 使用 `Stream` API 对 `orderClassifyDTOs` 进行分组，生成 `Map<String, List<OrderClassifyDTO>>`。
*   **00:00:20 - 00:00:25**: 使用 `OrderClassifyGroupDTO` 的 Builder 模式，开始将分组结果转换为目标对象。
*   **00:00:25 - 00:00:30**: 通过 `forEach` 方法遍历分组结果，并使用 `builder` 构建 `OrderClassifyGroupDTO` 对象。
*   **00:00:30 - 00:00:35**: 从 `List<OrderClassifyDTO>` 中提取 `Order` 对象，并使用 `builder.orders(orders)` 方法设置分组数据。
*   **00:00:35 - 00:00:40**: 完成 `OrderClassifyGroupDTO` 的构建，并将其添加到 `orderClassifyGroupDTOs` 列表中。
*   **00:00:40 - 00:00:45**: 最终返回 `orderClassifyGroupDTOs`，完成订单分类和转换。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段 1 (OrderClassifyDTO)**:
    ```java
    public class OrderClassifyDTO {
        // 分组信息
        private String startAgencyId;
        private String endAgencyId;
        private Integer orderType;
        private String goodsType;
        private String currentAgencyId;

        public String groupBy() {
            if (StringUtils.isNotBlank(this.startAgencyId) && StringUtils.isNotBlank(this.endAgencyId) && StringUtils.isNotBlank(this.currentAgencyId)) {
                return this.startAgencyId + "#" + this.endAgencyId + "#" + this.currentAgencyId;
            }
            return "";
        }
    }
    ```

*   **关键代码片段 2 (TaskOrderClassifyServiceImpl)**:
    ```java
    @Override
    public List<OrderClassifyGroupDTO> execute(String agencyId, String jobId, String logId) {
        // 用于存放当前机构下的订单
        List<OrderClassifyDTO> orderClassifyDTOs = new ArrayList<>();
        List<OrderClassifyGroupDTO> orderClassifyGroupDTOs = new ArrayList<>();

        // 获取当前机构下所有的订单数据(分为新订单和中转订单)
        orderClassifyDTOs.addAll(buildNewOrder(agencyId));
        orderClassifyDTOs.addAll(buildTransferOrder(agencyId));

        // 进行订单分类
        Map<String, List<OrderClassifyDTO>> orderClassifyDTOGroup = orderClassifyDTOs.stream()
            .collect(Collectors.groupingBy(OrderClassifyDTO::groupBy));

        // 进行对象转换，将当前Map对象转为 List<OrderClassifyGroupDTO>类型
        OrderClassifyGroupDTO.OrderClassifyGroupDTOBuilder builder = OrderClassifyGroupDTO.builder();
        orderClassifyDTOGroup.forEach((key, value) -> {
            builder.key(key);
            List<Order> orders = value.stream().map(item -> item.getOrder()).collect(Collectors.toList());
            builder.orders(orders);
            OrderClassifyGroupDTO orderClassifyGroupDTO = builder.build();
            orderClassifyGroupDTOs.add(orderClassifyGroupDTO);
        });

        // 将分类结果保存到数据库
        return orderClassifyGroupDTOs;
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 数据结构定义**
    讲师首先展示了 `OrderClassifyDTO` 类的代码，强调其用于封装原始订单信息，并定义了 `groupBy` 方法，该方法根据 `startAgencyId`, `endAgencyId`, `currentAgencyId` 三个字段生成一个唯一的分组键（字符串），用于后续的分组操作。

*   **场景 2: 分组与转换逻辑**
    讲师在 `execute` 方法中，首先创建了两个列表 `orderClassifyDTOs` 和 `orderClassifyGroupDTOs`，用于存放原始数据和最终的分组结果。
    接着，通过 `Stream` API 对 `orderClassifyDTOs` 进行分组，使用 `Collectors.groupingBy(OrderClassifyDTO::groupBy)`，将数据按 `groupBy` 方法返回的键进行分组，得到一个 `Map<String, List<OrderClassifyDTO>>`。

*   **场景 3: Builder 模式应用**
    讲师使用 `OrderClassifyGroupDTO.builder()` 创建一个 Builder 实例。
    然后，通过 `forEach` 方法遍历分组结果 `Map`，对每个键值对进行处理：
    - 调用 `builder.key(key)` 设置分组键。
    - 从 `List<OrderClassifyDTO>` 中提取 `Order` 对象，并使用 `builder.orders(orders)` 设置分组数据。
    - 调用 `builder.build()` 构建一个 `OrderClassifyGroupDTO` 对象，并将其添加到 `orderClassifyGroupDTOs` 列表中。

*   **场景 4: 最终结果**
    最终，方法返回 `orderClassifyGroupDTOs`，这是一个包含所有分组后订单数据的列表，可以直接用于后续的业务处理或数据库存储。整个过程展示了如何利用 Java 的 Stream API 和 Builder 模式，实现复杂的数据分组和转换逻辑。
