# 44-智能调度服务（实现过程_订单分类_13） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好

那么刚才呢

咱们这个calculate

也就是计算的这个方法呢

咱们是不是已经这个写完了

那接下来呢

我们就可以简单来测试一下它

那么要测试的话呢

咱们可以这样

在咱们这个main方法里面来测一下

就可以了

好

但是因为它不是一个静态方法

所以我们直接要调它那个方法呢

不好调

那怎么办呢

我们可以把当前这个对象呢

自己new一个出来

new一个什么呢

我们当前这个task

就是当前我们这个时间类

对吧

然后呢调用它的这个

刚才我们看到叫calculate

对吧

然后呢传进来一个agency

agency list

scope list

然后呢还要传一个什么呢

location对吧

location

OK

但是这呢就需要我们自己来造一下这个数据啊

那么我们可以自己来造一个数据

new一个array list

好

然后这个location的话呢

我们也给它来造一个

好

比如这个location呢

我们就可以使用我们刚才这个

好

到这个点的距离

你看它是一个坐标值对吧

静微度坐标值

然后呢

关键就是这个list的集合

这个list的集合呢

你看这里边封装的是这个什么DTO对象

对吧

DTO对象

然后每一个DTO对象呢

是不是对应的就是什么呢

对应的其实就是一个

这个DTO对象呢

这个DTO对象呢

这个DTO对象呢

这个DTO对象呢

这个DTO的作业范围

你看它这是不是存在有我们这个机构的ID

以及这个机构

它的作业范围是不是通过我们这个multipoint

这些坐标点是不是去围成一个图形

通过这种方式来描述

所以我们在这呢需要来干什么呢

把这个DTO呢来

封装一下

咱们就叫DTO1

new一个什么呢

agency

这个什么DTO

然后呢我们DTO1.set

注意看

这个DTO1.set

然后呢我们在这呢

其实这个error ID啊

咱们写不写都可以

那么我们主要是写一个什么呢

agency ID

比如说这个机构ID是1

因为都是假数据啊

所以我尽量就造一些简单一点的

好读的

然后呢DTO1.什么呢

set这个

叫做multipoints

这是不是就是

坐标点对吧

这些坐标点

然后呢这个坐标点的话呢

我们可以看到它其实又是一个

什么呢

point1

它又是一个集合

所以这个数据呢

其实造起来还挺麻烦的

还挺麻烦的

然后呢我们在这呢

直接new一个什么呢

array list

对吧

一个array list

然后呢它这里边呢

是不是又需要有一个什么

list的集合

list就是套的map

因为我们前面也分析了

它是一个二维数组啊

是集合里面套集合

然后集合里面的元素呢

是map

是这么一个关系啊

所以这儿呢确实是比较繁琐的

然后呢我们可以在这个point1里边

对吧

再来一个

它又是一个list

又是一个list

然后list里面是map

这么一个结构啊

咱们这叫points1-1

就这么一个效果

又一个array list

而这个里边呢

它是不是要装map

对吧

要装一些map

所以我们在这儿呢

是不是又要造一些map出来

这个就是我们的

point1

咱们就直接new一个什么呢

hashimap就可以

所以大家可以看到

我们现在呢

其实想测试一下也挺繁琐的

就是因为它这个数据呢

比较复杂

然后呢

我们在这里边来put

这个put的是什么东西呢

是不是就是我们一个一个的这个坐标点

对不对

一个一个的坐标点

然后呢

每一个map其实对应的是什么呢

每一个map其实这里边对应的就是我们的这么一个json对象

然后呢

比如说啊

我们这里面呢

需要有这个进度

对吧

lng

然后呢

它所对应的值

是不是应该就是我们

这个值

就是这个值

好

然后呢

我们再来put一个

再来put一个

还有一个是不是叫做lat对吧

LAT这个是纬度

然后这个纬度这个值呢

我就放后边这个值

是这个值

这样的话呢

我们这一个点是不是就有了

这个点就有了

然后呢

咱们可以再来一个啊

这个point1就有了

然后呢

我们可以再来一个

因为这个数据造起来比较繁琐

所以我们就造这两个就可以好

然后呢

这个是point2

这两个点对吧

然后呢具体这个值呢是什么呢

这个值呢我们给它改一下吧

改成下面这个值

但是这个值呢其实都是真实的值啊

你看差别都不是很大对吧

哎

这都是一些

真实的坐标值

好

这样我们是不是够到了两个点

这两个点呢别忘了

是不是应该放到这个

list的集合里面去啊

所以说呢

我们需要给它干什么呢

add一下

add一个

一个是什么呢

point1对吧

然后呢再来add一个

point4

点add

再来一个point2

ok

这样的话呢

我们是不是就把这两个点加到这个list里面去了

然后别忘了是什么呢

咱们这个list是不是还要加在这个list里面去

所以说这个地方大家不要弄混了啊

也就是说我们这个point1

point1点什么呢

add这个

那么到这儿的话

你看我们现在造了这么一堆假数据对吧

整个这一堆造完之后呢

这其实仅仅是造出来一个机构

对吧

一个机构的

所以说呢

我们在这儿呢

可以再来复制一份出来啊

再来复制一份出来

然后再来造什么呢

第二个机构的

咱们就造这两个机构的数据就可以了

因为这儿确实挺繁琐的

好

然后呢

这个agencyID呢

比如等于2

然后呢

这儿我们也给它改成2

好

好

嗯

这个呢

应该是

嗯

3吧

啊

4

一共是这么4个点啊

然后呢

把这边呢

来整体来改一下

这个值呢

我就手动给它改一下了

改成这个值

加个1

好

然后呢

别忘了

这个地方呢

需要给它改统一了

这point3

然后呢

下面这是point4

然后呢

这个的话是不是应该是

首先是这个

把这两个map是不是加到

我们这个point3

point3

然后下面这个point4

这么4个点

好

然后呢

这个地方呢

是不是应该改成我们这个point2

嗯

来看一下

2-1

然后呢

这个是不是对应的

应该就是我们

这个point2啊

好

这个就是2-1

好

嗯

这个需要仔细一点

把这个数据呢

不是把它造出来

嗯

这个地方呢是不是也得改一下呢

这个还没有改

好

那到这儿的话呢

我们是已经造了这么两个数据

对吧

两个这个机构

好

然后呢

我们再把这两个机构

这个数据呢

给它放到这个最终的这个list的集合里面去

.add

一个是dto1

对吧

然后呢

agency list.add

这个dto2

好

到这儿的话呢

才算是把这个数据呢

给造出来啊

然后呢

它是不是调用我们这个calculate这个方法

对吧

好

然后呢

我们可以在这个calculate这个方法这呢

来加一个断点呢

我们可以来跟一下

好

咱们直接执行这个mint方法

debug方式来执行

好

然后呢

我们来看啊

它现在是不是已经到这了

然后看传进来这个list的集合是不是size等于2

因为我们造的是两个机构

对吧

哎

一个是agency id等于

哎

这儿好像有点问题啊

agency id

这个

好像有点问题

那么我们直接先给它放过去啊

来看一下我们刚才造的这个数据应该是有点问题啊

这个地方你看我是不是没有改彻底啊

没有改彻底啊

应该是dto2

然后呢

points2

points2里面加的是这两个

这两个啊

这回应该可以

然后呢

重新再来一看

再来一遍啊

好

又过来了

看这个agency list

list里边一个是agency id是1

一个是2

对吧

然后呢

重点看的是这个multipoints

multipoints呢

咱们直接到这边来看

你看它是不是

呃

有两个的

有一个

这个呢

是multipoints它的size是1

哎

因为它是个二维数组啊

然后相对于list集合里面又套了个集合

这个集合里面长度是2

因为我们是不是造了两个数据

对吧

两个数据哎

这是净维度啊

然后呢

这是又是一组净维度

好

然后呢

这是agency

看这个也是这个样的结构

好

因为这个嵌套的很深呢

刚才我们通过造数据

大家应该也能感受出来

对吧

哎

这个数据套的非常深

好

然后呢

我们这个数据没问题啊

然后再看这个location

哎

location呢

是咱们写死的

这就传过来了

然后呢

我们程序继续往下走

注意看

走

开始便利

对吧

把第一个便利出来

啊

把第一个便利出来

好

就是这个数据

刚才也看了

然后呢

再来继续便利

哎

把这个map

这其实对应的就是我们multipoint

对吧

哎

把它便利出来

好

然后呢

便利出来之后呢

继续再往下找

是不是就找到具体的map了

找到具体的map

好

你看

这个map里边是不是净度维度

好

然后接下来呢

我们调用getpoint的方法

走

它会跟我们拼

对吧

哎

这个地方好像有点问题啊

来看一下

控制台

应该是报错了

你看控制台应该是报错了

嗯

来看看是什么问题呢

啊

啊

这个地方的问题是一个什么呢

class case的一个ception

是一个强转的问题

来点一下

是这个地方

强转有问题

那这个地方呢

看来还不能强转过来

因为它是一个double类型

对吧

不能强转成string

那怎么办呢

哎

那既然不让强转

那我就toString吧

调用这个toString方法

好

这样的话呢

我们就不用强转了

所以呢

我们在测试的时候呢

还是能测试出来一些问题啊

这个地方

好

那么接下来呢

咱们重新再来执行一下我们这个MIM方法

看看现在还有没有什么问题

走

好

又过来了

对吧

然后呢

程序继续往下走

刚才我们是执行到这个getPoint的方法

是不是报错了

走

好

现在已经过来了

看这个point

啊

你看它是不是已经拼完了

对吧

静伪度

然后接下来调用

百度地图

对吧

然后呢

把这个值给我们返回

走

啊

计算出来了一个值

这是distance

对吧

是2510

哎

计算出了一个w类型的这么一个值

这就是一个距离啊

然后呢

因为这是第一次便利

对吧

所以说以前肯定是没有

所以这个拿出来肯定是空

你看是不是闹啊

既然是空的话

if是不是就成立了

啊

然后呢

它是不是就会放进去一个

好

放进去一个

放进一个之后呢

我们看这个agency map里边

是不是就已经有了一个值

key呢就是1

也就是我们刚才看到的

机构id对吧

值呢就是这个2510

然后接下来呢

我们是不是继续来便利

继续来便利

嗯

这个地方呢

我们最好给它加一个断点

要不然它就跑了啊

走

是不是又过来一个

这第二次过来

第二次过来的话呢

这是另外又第二个点了

对吧

第二个点了

好

然后呢

我们接下来呢

再来计算出来一个距离

看这个距离是多少呢

是2446

刚才那个是2510对吧

所以说呢

它应该是

比上一个是不是更近一些

所以说呢

它是不是又一比较对吧

哎

然后呢

它就会把上一个给覆盖掉

咱们来看

走

好

你看现在这个agency group里边

size还是1

但是这个值是不是变成了什么呢

2446

好

然后呢

我们继续

往下走

好

然后呢

这一次便利出来的这个

是谁呢

这应该是第二个机构了啊

第二个机构

你看啊

我们这个

dto里边这个agency id

是不是2啊

对吧

哎

这是第二个机构的东西了

那这个时候呢

它这是不是又是空

对吧

第一次便利又是空

所以过

然后呢

又过来一次

再来便利

好

但是我们刚才没有注意看啊

它这里边

你看它这一次计算出来的

呃

原先的这个呢

是2454对吧

然后这一次计算出来的这个是

83

那这样的话它是不是不成立

不成立

你看

好

直接过

那么这样的话呢

我们

整个程序其实就已经跑过去了

嗯

那么刚才我们测的是前面这

这几层放云环是没啥问题的

对吧

然后呢

我们可以

让程序停在这啊

因为刚才我们是不是想看一下这个排序的效果

对吧

好

然后呢

再来一遍啊

走

好

那么到这

咱们来看啊

这个agency map里边呢

应该是存了两个值

对吧

哎

一个是1

一个是2

这是它的key

然后呢

value的话呢

你看

这两个value当然很接近啊

这是由于

我们的数据造成的

好

然后接下来我是不是需要给它进行排序

怎么排呢

首先转成一个例子的集合

对吧

转成一个例子的集合

集合里边是不是现在就是这两个啊

这两个map

然后呢

我们接下来sort

是不是来进行排序

对吧

进行排序

好

排完之后啊

再来看这个例子的

里边

注意现在这个顺序

你看

那小的一定是放上面去了

对吧

你看这是2446

这个是2454

好

然后呢

排好了之后呢

咱们是不是

把这个小的这个get0

是不是就拿第一个

然后getkey

这样的话

这个agencyid是不是就是1

ok

没问题

好

这是咱们测试了一下

但是这个测试的过程

大家也看到了

主要就是我们要造一些这个测试数据呢

其实还是非常繁琐的

好

那么刚才我们在测试的时候呢

也测出来了一个小问题

对吧

哎

就是这个地方啊

我刚才是强转成了一个stream

看来还不行

因为get出来之后呢

它是double

那么我们调用toString方法就可以了

好

那么这是关于

咱们这个方法的一个简单测试

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一段 Java 代码实战教学，主要演示如何实现一个“任务订单分类服务”，其核心功能是根据给定的地理位置（经纬度），计算并返回距离该位置最近的机构（或业务点）的 ID。代码在 IntelliJ IDEA 中编写和调试，主要涉及数据结构（`List`, `Map`, `List<Map>`）、面向对象设计（`AgencyScopeDto` 类）、以及使用百度地图 API 计算两点间距离。视频通过逐步编写、调试和注释代码，展示了如何处理多机构、多坐标点的场景，并最终返回最优解。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **章节 1: 项目环境与核心类定义 (00:00 - 00:20)**
    *   展示了项目结构，包括 `pd-service-api`、`pd-service-impl` 等模块。
    *   重点展示了 `AgencyScopeDto` 类的定义，该类用于封装机构信息，包含机构 ID (`agencyId`)、行政区 ID (`areaId`) 和一个多边形坐标点集合 (`multiPoints`)。

*   **章节 2: 构建测试数据与核心服务调用 (00:20 - 00:45)**
    *   在 `TaskOrderClassifyServiceImpl` 类中，演示了如何创建 `AgencyScopeDto` 对象。
    *   通过 `Map` 结构构建了两个坐标点（`point1` 和 `point2`），并将其添加到 `List<Map>` 中，最终设置到 `AgencyScopeDto` 的 `multiPoints` 字段。
    *   定义了目标位置 `location` 字符串，并调用 `calculate` 方法进行计算。

*   **章节 3: 核心计算逻辑实现 (00:45 - 01:15)**
    *   详细讲解了 `calculate` 方法的实现。
    *   遍历 `agencyList`，对每个机构的 `multiPoints` 进行遍历。
    *   调用 `getPoint` 方法提取坐标点，并使用 `EntCoordSyncJob.getDistance` 方法计算该点与目标位置的距离。
    *   使用 `Map` 结构 `agencyMap` 来存储机构 ID 与其对应距离的映射关系。

*   **章节 4: 数据排序与结果返回 (01:15 - 01:35)**
    *   将 `agencyMap` 中的 `Entry` 转换为 `List<Map.Entry<String, Double>>`。
    *   使用 `Comparator.comparingDouble(Map.Entry::getValue)` 对距离进行升序排序。
    *   取出排序后第一个元素的 key（即机构 ID），并返回 `Result.ok().put("agencyId", agencyId)`。

*   **章节 5: 辅助方法 `getPoint` 与调试 (01:35 - 01:50)**
    *   展示了 `getPoint` 方法的实现，该方法从 `Map` 中提取 `lng` 和 `lat` 字符串，并拼接返回。
    *   在调试模式下，观察了 `agencyMap` 的内容和排序后的结果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段：**

    *   **`AgencyScopeDto` 类定义：**
        ```java
        @Data
        public class AgencyScopeDto implements Serializable {
            private static final long serialVersionUID = 3513029168661385887L;
            private String id;
            private String agencyId;
            private String areaId;
            private List<List<Map>> multiPoints;
        }
        ```

    *   **`calculate` 方法核心逻辑：**
        ```java
        private Map<String, Double> calculate(List<AgencyScopeDto> agencyList, String location) {
            Map<String, Double> agencyMap = Maps.newHashMap();
            for (AgencyScopeDto agencyScopeDto : agencyList) {
                for (List<Map> maps : agencyScopeDto.getMultiPoints()) {
                    for (Map map : maps) {
                        String point = getPoint(map);
                        Double distance = EntCoordSyncJob.getDistance(point, location);
                        if (preDistance == null || distance < preDistance) {
                            preDistance = distance;
                        }
                        agencyMap.put(agencyScopeDto.getAgencyId(), distance);
                    }
                }
            }
            List<Map.Entry<String, Double>> list = new ArrayList<>(agencyMap.entrySet());
            list.sort(Comparator.comparingDouble(Map.Entry::getValue));
            String agencyId = list.get(0).getKey();
            return Result.ok().put("agencyId", agencyId);
        }
        ```

    *   **`getPoint` 方法：**
        ```java
        private String getPoint(Map map) {
            String lng = map.get("lng").toString();
            String lat = map.get("lat").toString();
            return lng + "," + lat;
        }
        ```

*   **关键公式/函数：**

    *   **距离计算函数：** `EntCoordSyncJob.getDistance(point, location)`。这是一个封装好的方法，用于计算两个经纬度点之间的距离。视频中未展示其内部实现，但其功能是核心。

*   **关键图表/演示：**

    *   **调试控制台输出：** 在调试过程中，控制台显示了 `agencyList`、`location`、`maps` 等变量的值，以及最终返回的 `agencyId`。例如：
        ```
        agencyList = [AgencyScopeDto{...}]
        location = "116.349936,40.066258"
        maps = [Map{...}, Map{...}]
        agencyMap = {1=2454.0, 2=1112.5}
        agencyId = 2
        ```

---

### 4) 关键场景与演示描述

*   **场景 1: 数据结构初始化与测试数据构建**
    *   讲师在 `TaskOrderClassifyServiceImpl` 类中，通过 `new ArrayList<>()` 创建了 `agencyScopeList`。
    *   通过 `new AgencyScopeDto()` 创建了 `dtol` 对象，并设置了 `agencyId`。
    *   使用 `new ArrayList<>()` 和 `new HashMap<>()` 构建了 `points1_1`，并填充了两个坐标点 `point1` 和 `point2`。
    *   调用 `dtol.setMultiPoints(points1)` 将坐标点集合设置到 `AgencyScopeDto` 对象中。

*   **场景 2: 核心计算逻辑的逐步实现**
    *   讲师在 `calculate` 方法中，使用 `Maps.newHashMap()` 创建了一个 `Map<String, Double>` 来存储机构 ID 和距离。
    *   使用嵌套的 `for` 循环遍历 `agencyList` 中的每个机构，再遍历其 `multiPoints` 中的每个坐标点。
    *   调用 `getPoint` 方法提取坐标点字符串，并调用 `EntCoordSyncJob.getDistance` 计算距离。
    *   使用 `if (preDistance == null || distance < preDistance)` 逻辑来记录每个机构的最小距离。

*   **场景 3: 排序与结果返回**
    *   讲师将 `agencyMap` 的 `entrySet()` 转换为 `List<Map.Entry<String, Double>>`。
    *   使用 `list.sort(Comparator.comparingDouble(Map.Entry::getValue))` 对距离进行升序排序。
    *   通过 `list.get(0).getKey()` 获取距离最小的机构 ID。
    *   最终返回 `Result.ok().put("agencyId", agencyId)`。

*   **场景 4: 调试与验证**
    *   讲师在调试模式下，观察了 `agencyMap` 的内容，确认了距离计算的正确性。
    *   通过控制台输出，验证了排序后的结果，最终返回的机构 ID 为 `2`，其距离为 `1112.5`，小于机构 `1` 的距离 `2454.0`。

---

以上是根据视频画面进行的结构化分析。视频内容清晰地展示了如何在 Java 中实现一个基于地理距离的机构分类服务。
