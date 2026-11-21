# 55-根据规则计算订单价格（实现步骤_1） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是说了一下我们计算订单价格的规则

那接下来呢,我们就需要来通过代码的方式呢

把我们这个订单价格把它计算出来

首先呢,我们第一步呢,需要来封装一个实体类

这个实体类呢,其实充当的就是我们的fact对象

那么它这个实体类里边啊,主要封装的属性是什么呢

就是计算我们订单价格所需要的这些参数

比如说什么呢,比如说我们这个货物总重量

你看我们这个,说1000克以内,这个指的是货物重量

是1000克以内,然后还有什么呢,订单的距离

这是不是我们的参数,包括还有手重,然后还有什么呢

手重的价格是多少,还有什么呢,续重的资费是多少

这些呢,都需要,这相当于都是我们计算订单价格的参数

那这个时候呢,我们可以封装这么一个实体类

然后呢,咱们这个实体类里边,那么这些属性呢

就是封装的这些维度,这些参数

那么后边呢,我们是不是就需要把这个实体类呢

作为什么呢,作为我们的fact的对象

把它传到我们规则引擎的这个什么呢

它的这个工作内存当中,来进行什么呢

模式的匹配,最终呢,根据这些参数是不是来进行计算

那接下来呢,我们就需要来创建这么一个实体

然后呢,我们先来创建一个包啊,叫做fact

在我们entity下面呢,咱们来创建一个子包,叫做fact

然后呢,我们把这个fact的类呢,把它创建出来

就叫做address rule了吧

跟我们讲义呢,保持一致

然后呢,这里边封装的属性呢,咱们可以整体来看一下

你看有一个total weight,这是货物的总重量,对吧

然后呢,还有什么呢,distance,这个是订单的距离

但是这个呢,我们肯定是需要计算的,对吧

咱们可以通过百度地图,相关的那些接口

然后呢,把它算出来

然后呢,设置到这个维度,对吧

好,那我们就来看这个

这个属性上就可以了

然后还有什么虚重的价格,对吧

还有手重,还有手重的价格

那么这些呢,都是我们计算的维度

咱们呢,就直接把这个代码抄过来了

好,整个复制一下

OK,那么这个fact类呢,我们就定义好了

然后接下来呢,我们需要再来定义一个fact类

这个fact类是干什么呢

是用来封装我们这个计算后的结果的

前面这个呢,相当于是计算

前,对吧

我们的依据

我们需要依据这些参数来进行计算

那么算完之后呢,需要有一个结果,对吧

所以说呢,我们也专门封装了这么一个类啊

就是用来存放什么呢

用来存放我们这个,或者是封装我们计算后的结果

这个类呢,就叫做addressCheckResult

也是放在咱们这个fact包下边就可以了

因为到时候呢,我们也是需要把这个fact的对象

把它传到我们规则引擎

它的这个工作内存当中

然后呢,这里边呢,也是有这么两个属性啊

一个是什么呢

一个是其实是校验

也就是说我们一会儿肯定要编写规则文件,对吧

那么首先呢,我们需要去根据这些参数啊

根据这些参数是不是来进行匹配,对吧

进行这个模式匹配

如果匹配上了之后啊

那么有可能它匹配第一条

也有可能匹配第二条

不管是哪一条

只要匹配成功,任意一条

那这个时候呢,我们就说校验通过了,对吧

那这个时候呢

我们就把这个属性给它改成true

所以你看咱们默认属性是false,对吧

那么一旦匹配上某一条之后呢

我们就把这个计算的结果

这个属性改成true

同时呢,咱们是不是计算订单价格

算出来之后呢

把它设置到result这个属性上就可以了

所以说这里边呢,有这么两个属性啊

一个是什么呢

相当于是否通过校验

指的就是是否匹配

就是我们这个规则匹配是否成功

那么匹配成功之后呢

计算,计算完结果之后呢

把那个订单价格设置到

这个属性上就可以了

好

所以说呢,我们接下来呢

就需要在这里边呢

来封装这么两个属性

那么我就不手敲了啊

咱们直接把这个代码抄过来就可以了

好,就这么两个属性,对吧

这个呢是封装啊

我们写个注释

这个是封装我们这个规则

订单吧

订单这个价格计算后的结果

好

这是这个类

前面这个

这个呢,这个是封装的是什么呢

咱们也写一下

这个是封装我们这个计算什么呢

订单价格所需的什么呢

所需的参数吧

这两个类呢

还是比较简单的

主要大家能够理解

它起的作用就可以了

好,那接下来呢

我们就需要来创建一个什么呢

service

这个service呢

就实现什么呢

我们具体的计算逻辑

其实具体的计算逻辑呢

我们可以来强调一下

就是在我们的规则文件当中

其实也是可以计算的

但是呢,你发现没有

我们这个在计算的时候啊

后边这三条你看

基本上套路是完全一样的

无非就是什么呢

这个续重的资费是不是不一样

6,9,15,对不对

也就是说这个续重的资费啊

不一样

其他的呢,其实都是一样的

所以说呢,我们如果说

把这个计算的过程

把它写到我们的规则文件里面的话呢

这样的话其实相当于就很多

有这三个啊

其实就重复了

无非就是数字不一样

对不对

所以说呢,我们这块呢

就单独提一个service出来

然后呢

在我们的service里面来计算

我们就不在规则文件当中来计算了

咱们规则文件呢

直接调这个service

然后呢

把所需的参数传给这个service

由service的方法来

在这个方法内部呢

来完成计算

那么我们就不在这个规则文件里面

去进行计算了

所以接下来呢

就要来创建一个service接口

这个service接口呢

叫做什么呢

叫做derose ruler service

那么它就这么一个方法

你看

叫做什么呢

calc对吧

这个其实就是calculator

就是计算

只不过是一个缩写对吧

然后费

这个就是价格

或者叫做费用都可以

那么我们来

先来创建这么一个接口

叫做derose ruler service

在咱们这个service下边

对吧

对吧

然后呢

我们来创建这么一个

接口

好

然后呢

我们把这个方法呢

方法的声明直接考过来

大家可以来看一下

你看我们这个方法呢

传进去的是什么呢

传进去的是不是就是一个

derose ruler

derose ruler我们刚才刚写了

对吧

是不是就是这个

这是封装的是我们计算

订单价格所需的这些参数

对吧

然后呢传给我们这个方法

好

然后呢

这个方法的返回值是什么呢

它其实返回的就是我们订单的价格

好

那我们是不是就需要来提供一个service的实现类

对吧

然后呢

在这个实现类里面来实现这个方法

好

那么咱们在这呢

来创建这个实现类

实现类呢

就叫derose ruler service

impl吧

按照我们的这个命名规则

对吧

然后呢

加一个impl

然后咱们让它实现我们这个derose

那么呢

ruler service

接口

好

那么这个service呢

大家来看啊

我们其实并不需要去加service注解

为什么呢

因为我们这个service并不需要我们这个

spring容器跟我们去创建

咱们一会儿呢

在规则文件当中

自己把这个service对象拗出来就可以了

好

所以说呢

我们就不用加注解了

这个呢

就是计算什么呢

计算我们这个订单价格

对吧

好

根据条件

来计算订单价格

好

好

咱们把这个代码呢

复制过来

那么一会儿呢

我们再具体来看一下我们这个方法应该是如何计算

对吧

那么计算肯定就是按照我们刚才说的那个规则去进行计算

好

那么暂时呢

我们先写这么多

一会儿呢

我们再来完善一下这个具体计算的方法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化中文技术分析：

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的技术课程，具体讲解了如何在Java项目中使用Drools规则引擎来实现“根据规则计算订单价格”的功能。课程内容主要分为两部分：第一部分是定义计算订单价格的业务规则（包括重量和距离两个维度），第二部分是将这些规则封装到Java实体类中，并为规则引擎创建服务接口和实现类。视频通过展示Typora文档、IntelliJ IDEA开发环境中的代码和项目结构，逐步演示了从规则定义到代码实现的全过程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开始，展示Typora文档，内容为“7. 根据规则计算订单价格”章节的“7.1 规则”部分，详细列出了四种不同的计价规则。
*   **00:05 - 00:15**: 展示“7.2 实现步骤”部分，讲师说明第一步是封装实体类 `AddressRule`，用于存储订单价格计算所需的参数。
*   **00:15 - 00:30**: 在IntelliJ IDEA中，讲师创建并编辑 `AddressRule.java` 文件，定义了 `totalWeight`、`distance`、`continuedFee`、`firstWeight` 和 `firstFee` 等私有属性，并为其添加了对应的getter和setter方法。
*   **00:30 - 00:45**: 讲师切换到 `DroolsRulesService.java` 文件，创建一个服务接口 `DroolsRulesService`。
*   **00:45 - 01:00**: 讲师创建 `DroolsRulesServiceImpl.java` 文件，实现上述接口，并定义了一个 `calcFee` 方法，该方法接收一个 `AddressRule` 对象作为参数，用于后续的规则计算。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **规则定义**: 在“7.1 规则”部分，明确列出了四种计价规则：
        1.  1千克以内：20元。
        2.  1千克以上，距离在200公里以内：首重20元，续重6元/千克。
        3.  1千克以上，距离在200-500公里：首重20元，续重9元/千克。
        4.  1千克以上，距离在500公里以上：首重20元，续重15元/千克。
    *   **实现步骤**: 在“7.2 实现步骤”部分，说明了第一步是封装 `AddressRule` 实体类。

*   **代码关键内容**:
    *   **`AddressRule.java`**:
        ```java
        package com.ithema.pinda.entity.fact;

        public class AddressRule {
            // 货品总重量
            private double totalWeight;
            // 距离
            private double distance;
            // 续重价格
            private double continuedFee;
            // 首重
            private double firstWeight;
            // 首重价格
            private double firstFee;

            // getter 和 setter 方法
            public double getFirstFee() {
                return firstFee;
            }

            public void setFirstFee(double firstFee) {
                this.firstFee = firstFee;
            }

            public double getTotalWeight() {
                return totalWeight;
            }

            public void setTotalWeight(double totalWeight) {
                this.totalWeight = totalWeight;
            }

            public double getDistance() {
                return distance;
            }

            public void setDistance(double distance) {
                this.distance = distance;
            }

            public double getContinuedFee() {
                return continuedFee;
            }

            public void setContinuedFee(double continuedFee) {
                this.continuedFee = continuedFee;
            }
        }
        ```
    *   **`DroolsRulesService.java`**:
        ```java
        package com.ithema.pinda.service;

        public interface DroolsRulesService {
            // 根据条件计算订单价格
            String calcFee(AddressRule addressRule);
        }
        ```
    *   **`DroolsRulesServiceImpl.java`**:
        ```java
        package com.ithema.pinda.service.impl;

        import com.ithema.pinda.entity.fact.AddressRule;
        import com.ithema.pinda.service.DroolsRulesService;

        public class DroolsRulesServiceImpl implements DroolsRulesService {
            // 根据条件计算订单价格
            @Override
            public String calcFee(AddressRule addressRule) {
                return null;
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：规则定义与实体类封装** (00:00 - 00:30)
    *   讲师首先在Typora文档中展示业务规则，明确了计算订单价格需要考虑“重量”和“距离”两个维度，并给出了具体的计价标准。
    *   接着，讲师在IntelliJ IDEA中创建并编辑 `AddressRule.java` 文件，将规则中的参数（总重量、距离、续重价格、首重、首重价格）封装为类的私有属性，并为每个属性编写了标准的getter和setter方法，以便在后续的规则引擎中使用。

*   **场景二：服务接口与实现类创建** (00:30 - 01:00)
    *   讲师在IDE中创建了 `DroolsRulesService.java` 接口文件，定义了一个 `calcFee` 方法，该方法接收一个 `AddressRule` 对象作为参数，用于封装业务逻辑。
    *   随后，讲师创建了 `DroolsRulesServiceImpl.java` 实现类，实现了上述接口。在实现类中，讲师为 `calcFee` 方法添加了方法体，虽然目前仅返回 `null`，但为后续集成Drools规则引擎预留了接口。

*   **场景三：项目结构与编译** (00:15 - 00:30)
    *   在IDE的项目结构视图中，讲师展示了 `AddressRule.java` 文件位于 `com.ithema.pinda.entity.fact` 包下，以及 `DroolsRulesService.java` 和 `DroolsRulesServiceImpl.java` 文件位于 `com.ithema.pinda.service` 包下。
    *   讲师在IDE的底部状态栏中显示了“Compilation completed successfully in 60.1ms”，表明代码编译成功，项目结构和代码逻辑已准备就绪。

---
