# 43-智能调度服务（实现过程_订单分类_12） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢继续来看咱们这个程序

刚才呢我们是写了这么三层4循环对吧

经过这三层4循环执行完成之后啊

我们这个agency map里边呢

应该就已经填满了值了对吧

那么这里边的它的key呢

就是我们这个机构的ID

而这个值呢就是我们计算出来的这个距离

并且呢这个距离呢

对于同一个网点来说

我们是不是保留的是最短的距离

最小的距离

好然后呢

接下来我们是不是就要从这个map里边来取

来取一个对吧

来取一个最终的一个网点

那么具体应该取哪个网点呢

是不是就需要把这个map里边的

我们保存的这些distance来进行一个比较

来取最小的一个值

所以这个地方呢

为了方便处理啊

我们需要做什么事呢

需要把这个map转换一下

把它转成一个什么呢

把它转成一个list

转成一个list之后呢

我们是不是就

可以根据这个distance来进行一个排序

来进行一个排序

然后呢

排完序之后呢

是不是就方便我们取出来最小的值

所以说呢

我们在这呢

需要把这个map转成一个什么呢

转成一个list的

所以我们在这呢

来new一个arraylist

然后呢

注意看这里边是什么呢

就是我们这个agencymap点什么呢

叫做entryset

然后呢

先把它转成一个set的

然后呢

再重新转成一个list的

好

好

这样呢

我是不是就转成了一个list的集合

当然这个地方呢

我们最好是把这个份型呢

给它补充一下

这儿直接生成一个list的

这种接口类型

然后呢

这里边是什么呢

这里边呢

是不是应该就是我们这个

叫做map.entry

是吧

map.entry

然后呢

这个entry的话呢

它是这种啊

string

对吧

对吧

对吧

double

为什么是这种类型啊

因为这个string呢

其实就是我们key

就是这个agency id

对吧

然后呢

那个value呢

其实就是什么呢

就是我们这个double类型

因为我们存的是这个distance

好

然后呢

这就把这个形式给它

变成了这么一个list

这么一个形式

好

然后呢

转成list的之后啊

我们是不是就可以进行排序了

对不对

是不是按照我们这个distance啊

distance

来进行什么呢

进行排序啊

好

好

,所以来个list点什么呢

这里边是不是有一个排序的方法

叫做sort

好

那么排序的依据是什么呢

排序的依据我们是不是就是根据这个distance来进行排序

那这个应该如何描述呢

咱们呢

是不是可以使用这个比较器对象啊

叫做comparator

comparator

就这个

然后呢

调用它的这个comparating这个方法

这里边呢

应该是有一个叫做comparating double

因为我们这是double类型对吧

double这个方法

好

然后呢

在这里边来传进来什么呢

我们要根据哪一个字段来进行比较对吧

根据哪个字段来进行比较呢

因为我们这里边是不是map.entry

所以在这呢

map.entry

然后呢

我们使用这个什么get value

也就是说我们这个entry里边

咱们是不是分成key还有value

那么很显然我们是不是应该使用value来进行排序

因为value就是我们对应的这个distance它的值

所以在这呢

我们是不是通过这种方式来进行一个排序就可以了

当然默认呢

它其实是一个生序排列

那么排好了之后呢

我们就可以通过通过这个list的点什么呢

get0

是不是来获取第一个

就可以了

获取第一个

然后呢

第一个完事之后呢

我们get什么呢

get这个key就可以

为什么是key呢

因为key我们记录的是不是我们这个agency id啊

最终呢

我们是不是想返回

就是这个agency id

只不过呢

我们需要给它封装成一个result啊

这种形式啊

这个呢

就拿到了我们这个叫做agency id

好

所以我们最终呢

给它来返回一下就可以了

转成一个result对象

直接return就可以了

在这直接return什么呢

咱们这个result点什么呢

ok点put

put

然后呢

这个key的话呢

我们就叫agency id就可以

叫做agency id

然后值的话呢

就是我们刚才这个已经拼起来的

好

这是咱们这个方法呢

是不是就已经这个写完了

一会儿呢

我们可以简单的来测试一下

但是现在整个过程我们想测的话还是挺麻烦的

我们可以单独就测这个方法

对吧

然后呢

给它造一些假数据

然后呢

我们来整体来

执行一下

看看这个方法能不能按照我们这个代码想要的这个逻辑

那么最终呢

把这些值封装好

然后呢

按照我们想要的这个效果进行排序

那么一会儿呢

我们可以来测一下

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段展示了一段 Java 代码的开发与调试过程，核心内容是实现一个“就近分配”或“按距离排序”的业务逻辑。开发者在 IntelliJ IDEA 中编写了一个名为 `caculate` 的方法，该方法接收一个机构列表和一个目标位置，计算每个机构到目标位置的距离，并将距离小于或等于之前记录的距离的机构更新到一个 Map 中。最后，开发者将 Map 转换为一个按距离排序的 List，并返回排序后距离最小的机构 ID。整个过程体现了如何使用 Java 的 `Map`、`List`、`Comparator` 等集合类和工具类来实现复杂的业务逻辑。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面中没有提供明确的时间戳，以下章节是根据画面内容和操作流程进行的逻辑划分：

*   **章节 1：方法初始化与数据结构创建 (0:00 - 0:03)**
    *   展示了 `caculate` 方法的开头，创建了一个 `Map<String, Double> agencyMap` 用于存储机构 ID 和其到目标位置的距离。

*   **章节 2：遍历机构列表并计算距离 (0:03 - 0:07)**
    *   使用 `for` 循环遍历 `agencyList`。
    *   对每个机构，通过 `getMutPoints()` 获取其坐标点列表。
    *   调用 `EntCoordSyncJob.getDistance(point, location)` 计算当前机构到目标位置的距离。

*   **章节 3：更新最小距离 (0:07 - 0:12)**
    *   获取机构已保存的距离 `preDistance`。
    *   使用 `if(preDistance == null || distance < preDistance)` 判断是否需要更新。
    *   如果需要更新，则调用 `agencyMap.put(...)`。

*   **章节 4：转换为排序列表并返回结果 (0:12 - 0:18)**
    *   将 `agencyMap.entrySet()` 转换为 `List<Map.Entry<String, Double>>`。
    *   使用 `Comparator.comparingDouble(Map.Entry::getValue)` 对列表按距离进行排序。
    *   取出排序后第一个元素的 key（机构 ID）。
    *   返回 `Result.ok().put("agencyId", agencyId)`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码关键内容：**

    ```java
    private Result caculate(List<AgencyScopeDto> agencyList, String location) {
        Map<String, Double> agencyMap = Maps.newHashMap();
        for (AgencyScopeDto agencyScopeDto : agencyList) {
            for (List<Map> maps : agencyScopeDto.getMutPoints()) {
                for (Map map : maps) {
                    String point = getPoint(map);
                    Double distance = EntCoordSyncJob.getDistance(point, location);
                    Double preDistance = (Double) agencyMap.get(agencyScopeDto.getAgencyId());
                    if (preDistance == null || distance < preDistance) {
                        agencyMap.put(agencyScopeDto.getAgencyId(), distance);
                    }
                }
            }
        }
        List<Map.Entry<String, Double>> list = new ArrayList<>(agencyMap.entrySet());
        list.sort(Comparator.comparingDouble(Map.Entry::getValue));
        String agencyId = list.get(0).getKey();
        return Result.ok().put("agencyId", agencyId);
    }
    ```

*   **关键操作与工具：**

    *   **`EntCoordSyncJob.getDistance(point, location)`**: 一个自定义工具类，用于计算两点之间的距离。
    *   **`Maps.newHashMap()`**: Google Guava 库中的工具类，用于创建一个 `HashMap`。
    *   **`Comparator.comparingDouble(Map.Entry::getValue)`**: Java 8 的函数式接口，用于根据 Map 中 value（距离）对 Entry 进行排序。
    *   **`List<Map.Entry<String, Double>>`**: 将 Map 转换为 List 以便排序。
    *   **`Result.ok().put("agencyId", agencyId)`**: 返回一个包含结果的封装对象。

---

### 4) 关键场景与演示描述

*   **场景 1：代码逻辑的逐步构建**
    *   开发者首先定义了 `caculate` 方法，并初始化了一个 `Map` 来存储机构 ID 和距离。
    *   通过三层 `for` 循环，依次遍历机构列表、机构的坐标点列表，最终获取到每个机构的坐标点。
    *   使用 `EntCoordSyncJob.getDistance` 计算距离，并与已保存的距离进行比较，更新最小距离。

*   **场景 2：数据结构的转换与排序**
    *   在完成所有距离计算后，开发者将 `agencyMap` 转换为一个 `List<Map.Entry<String, Double>>`。
    *   使用 `Comparator.comparingDouble(Map.Entry::getValue)` 对这个列表进行排序，确保距离最小的机构排在最前面。
    *   通过 `list.get(0).getKey()` 获取排序后第一个元素的 key，即距离最小的机构 ID。

*   **场景 3：返回结果**
    *   最后，开发者将机构 ID 封装到 `Result` 对象中，并返回 `Result.ok().put("agencyId", agencyId)`，表示操作成功并返回结果。

*   **场景 4：IDEA 的智能提示与调试**
    *   在编写 `list.sort(...)` 时，IDEA 提供了 `Comparator` 的自动补全建议，开发者选择了 `comparingDouble(Map.Entry::getValue)`。
    *   在返回语句中，IDEA 提示了 `Result.ok().put("agencyId", agencyId)` 的写法，开发者直接使用了该建议。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解这段代码的开发过程。
