# 58-根据规则计算订单价格（实现步骤_4） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,刚才咱们是把这个规则文件已经编写完了

接下来我们其实可以对这个规则文件进行一个简单的优化

也就是说我们现在虽然这个规则文件写的是没有问题的

逻辑上也没问题

但是还不是一个最优的方案

所以我们接下来可以简单优化一下

大家可以想一下我们在这一共是四条规则

那么这四条规则的话有没有可能同时匹配多个

那么其实是不可能的

也就是说我们这四条规则是不是最终只能有一个去匹配

那么也就是说它们之间其实都是互斥的

那这样的话我们其实就可以把这四个规则

把它们纳为同一个组

大家还记得吧

我们前面是不是有这么一个叫做activation group

对吧

比如说叫做my group

然后我们把这四个规则都定义在这个组里边

那么一定要注意这个组的名字不要写错了

都要保持一致

这样的话呢

那么它们四个呢就归为一个组了

叫做my group

而这个activation group

它的特点是什么呢

就是同一个组里边所有的规则只能有一个处罚

只能有一个处罚

对吧

然后呢我们可以再给这些规则呢进行一个排序

进行一个排序

然后呢我们使用什么排序呢

大家还记得吧

是不是就是这个silence

然后呢给它来一个10

对吧

那么数值越大呢

它是越优先的

然后呢这个地方呢

我们给它来一个9

好

然后这个地方来一个8

最后这个来个7

那这样的话呢

它这个规则匹配的顺序呢

是不是应该就是自上而下的

对吧

自上而下的

那么首先匹配这条规则

如果这条规则匹配成功了

后边呢

其实它就不会再匹配了

对吧

不会再匹配了

所以这样的话

就更优化一点

然后呢我们来看

如果第一个规则没有匹配成功

对吧

它就来匹配第二个规则

那么它是订单距离是200公里以下

那么这块呢不用修改

然后呢如果这个匹配不成功

它再匹配第三个

对吧

这个

这个呢是不是应该就是200到500公里

这个时候呢

我们其实就可以把后边这个条件给去掉了

那么为什么

因为呢

如果说它既然能匹配到这个规则

那就说明上面的规则没有匹配上

对吧

那么没有匹配上的话呢

这就说明它肯定不是200公里以下

要不然的话

这条规则肯定就匹配上了

对吧

所以说呢

我们这个时候呢

就可以啊

不用再写那么多

直接写这个右侧

这个这个范围就可以

所以就是因为我们设置了什么呢

它这个护翅

护翅了这一点

所以说这个地方呢

我们直接写小于等于500就可以

然后如果这个也匹配不上

那就说明什么呢

那就只剩下这个了

对吧

它肯定就会有这个规则

就是500公里以上了

所以这块呢

也不用修改了

咱们这是简单的

加了这么两个属性

对吧

一个是什么呢

activation group

把这四条规则

给它加到这个组里面来

同时呢

也加了个silence

然后呢

进行一个什么排序

对吧

就是执行优先级

好

咱们这是简单这个

优化一下这个规则文件

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面内容进行的结构化分析。

---

### 1) 视频摘要

本视频是一节关于 **Drools 规则引擎** 的技术课程，主要演示如何在 Java 代码中使用 Drools DSL（领域特定语言）来编写和管理复杂的业务规则。课程的核心内容是通过修改规则文件中的 `salience`（优先级）和 `activation-group`（激活组）属性，来控制规则的执行顺序，从而解决在多规则场景下可能出现的“规则冲突”或“执行顺序不一致”的问题。视频通过逐步修改代码并演示其效果，直观地展示了 Drools 规则引擎的配置机制。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示当前正在编辑的 Drools 规则文件 `DroolsRules.drl`，并简要介绍课程目标：学习如何控制规则的执行顺序。
*   **00:05 - 00:15**: 展示初始的三个规则，分别对应“1千克以内”、“200公里以内”和“500公里以上”的运费计算逻辑。此时规则的执行顺序是默认的，可能不符合预期。
*   **00:15 - 00:30**: 讲师开始讲解 `salience` 属性，演示如何通过为规则设置不同的优先级值（如 10、9、7）来强制改变规则的执行顺序。代码中展示了如何修改 `salience` 的值。
*   **00:30 - 00:45**: 讲师讲解 `activation-group` 属性，演示如何将多个规则分组到同一个激活组中，以确保组内规则按指定顺序执行。代码中展示了如何为规则添加 `activation-group "mygroup"`。
*   **00:45 - 01:00**: 讲师总结，强调 `salience` 用于全局控制规则优先级，而 `activation-group` 用于局部控制组内规则的顺序。视频结束。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **核心代码片段**：
    *   **规则文件 (`DroolsRules.drl`) 的结构**：
        ```java
        dialect "java"

        rule "1千克以内20元"
            activation-group "mygroup"
            salience 10
            when
                addressRule : AddressRule(totalWeight != null && totalWeight <= 1.00)
            then
                checkResult.setPostCodeResult(true);
                checkResult.setResult("20");
                System.out.println("1千克以内20元");
            end
        ```

        ```java
        rule "1千克以上，订单距离在200公里以下的，首重1千克，首重价格20元，续重每1千克资费为6元"
            activation-group "mygroup"
            salience 9
            when
                addressRule : AddressRule(totalWeight != null && totalWeight > 1.00 && distance <= 200.00)
            then
                addressRule.setFirstFee(20.00);
                addressRule.setFirstWeight(1.00);
                addressRule.setContinuedFee(6.00);
                DroolsRulesService droolsRulesService = new DroolsRulesServiceImpl();
                String orderAmount = droolsRulesService.calcFee(addressRule);
                checkResult.setPostCodeResult(true);
                checkResult.setResult(orderAmount);
                System.out.println("1千克以上，订单距离在200公里以下的，首重1千克，首重价格20元，续重每1千克资费为6元");
            end
        ```

        ```java
        rule "1千克以上，订单距离在200~500公里的，首重1千克，首重价格20元，续重每1千克资费为9元"
            activation-group "mygroup"
            salience 8
            when
                addressRule : AddressRule(totalWeight != null && totalWeight > 1.00 && distance <= 500.00 && distance > 200.00)
            then
                addressRule.setFirstFee(20.00);
                addressRule.setFirstWeight(1.00);
                addressRule.setContinuedFee(9.00);
                DroolsRulesService droolsRulesService = new DroolsRulesServiceImpl();
                String orderAmount = droolsRulesService.calcFee(addressRule);
                checkResult.setPostCodeResult(true);
                checkResult.setResult(orderAmount);
                System.out.println("1千克以上，订单距离在200~500公里的，首重1千克，首重价格20元，续重每1千克资费为9元");
            end
        ```

        ```java
        rule "1千克以上，订单距离在500公里以上的，首重1千克，首重价格20元，续重每1千克资费为15元"
            activation-group "mygroup"
            salience 7
            when
                addressRule : AddressRule(totalWeight != null && totalWeight > 1.00 && distance > 500.00)
            then
                addressRule.setFirstFee(20.00);
                addressRule.setFirstWeight(1.00);
                addressRule.setContinuedFee(15.00);
                DroolsRulesService droolsRulesService = new DroolsRulesServiceImpl();
                String orderAmount = droolsRulesService.calcFee(addressRule);
                checkResult.setPostCodeResult(true);
                checkResult.setResult(orderAmount);
                System.out.println("1千克以上，订单距离在500公里以上的，首重1千克，首重价格20元，续重每1千克资费为15元");
            end
        ```

*   **关键概念**：
    *   `salience`：用于设置规则的优先级，数值越大，优先级越高，越先执行。
    *   `activation-group`：用于将多个规则分组，组内规则会按 `salience` 值排序执行。
    *   `when`：规则的条件部分，定义了规则触发的条件。
    *   `then`：规则的执行部分，定义了规则触发后要执行的代码。

---

### 4) 关键场景与演示描述

*   **场景一：初始规则状态（00:05）**
    *   **描述**：讲师首先展示了三个规则的初始状态，没有设置 `salience` 或 `activation-group`。此时，规则的执行顺序是不确定的，可能导致计算结果不一致。
    *   **演示**：讲师通过修改代码，为每个规则添加了 `salience` 属性，并设置了不同的值（10、9、7），以强制改变执行顺序。

*   **场景二：使用 `salience` 控制执行顺序（00:15）**
    *   **描述**：讲师演示了如何通过设置 `salience` 来控制规则的执行顺序。例如，将“1千克以内”的规则 `salience` 设置为 10，使其优先于其他规则执行。
    *   **演示**：讲师在代码中修改了 `salience` 的值，并通过运行程序来验证规则的执行顺序。

*   **场景三：使用 `activation-group` 控制组内顺序（00:30）**
    *   **描述**：讲师演示了如何使用 `activation-group` 将多个规则分组，并在组内按 `salience` 值排序执行。例如，将所有运费计算规则都放入 `mygroup` 组。
    *   **演示**：讲师在代码中为每个规则添加了 `activation-group "mygroup"`，并设置了不同的 `salience` 值，以确保组内规则按预期顺序执行。

*   **场景四：总结与对比（00:45）**
    *   **描述**：讲师总结了 `salience` 和 `activation-group` 的区别和用法。`salience` 用于全局控制，而 `activation-group` 用于局部控制。
    *   **演示**：讲师通过对比修改前后的代码和运行结果，展示了规则执行顺序的可控性。

---

以上是根据视频画面内容整理的结构化分析。
