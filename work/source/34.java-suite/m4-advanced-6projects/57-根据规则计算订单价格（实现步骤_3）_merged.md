# 57-根据规则计算订单价格（实现步骤_3） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是把这个规则计算的方法呢,已经写完了,接下来呢,我们就需要来编写我们这个规则文件,对吧,这是非常重要的一个步骤,然后在这个规则文件里边呢,就需要来根据我们这些条件来进行匹配,然后匹配完之后呢,来最终在规则文件当中来调用我们service的这个方法,当然在调用它的时候呢,我们这个类里边的属性呢,在咱们规则文件当中啊,就已经相应的设置好了。

好,那接下来呢,我们就需要来创建这么一个规则文件,在咱们这个resource rulers目录下边来创建这么一个规则文件,叫做order amount calculator,DIR,对吧,这个翻译过来叫做订单价格计算,对吧。

好,在这儿呢,我们来创建这么一个文件出来,这就是咱们的规则文件,然后呢,我们在这里边来创建啊,这个规则文件呢,别忘了,首先呢,我们是不是来一个package。

好,指定一个包,对吧,这个包呢,就叫rules吧,这个其实无所谓,都是逻辑概念上的。

然后接下来呢,我们是不是就需要来定义相应的规则,但是在这里边呢,会使用到咱们这个什么address ruler呀,还有我们这个service类呀,还有什么呢,还有我们这个address check result等等,这几个类。

所以说呢,我们先给它引入一下,咱们先import,来引入一下,import,在哪个包呢,com的it黑码,点什么呢。

品达,然后呢,是entity,对吧,然后是fact,把这个引进来,然后呢,再引入一个,com的it黑码,点品达,点entity,然后fact,另外一个,对吧。

然后还有咱们这个service啊,也会用到,品达点service,直接引入什么呢,直接引入,先把这个接口引入一下。

然后呢,我们这个实现类呢,是不是。

也需要引入一下,实现类也引入一下吧。

因为前面我们已经介绍到了,咱们这个service啊,不需要什么呢,不需要我们这个spring容器来管理,我们直接在规则文件当中啊,来自己new这个service对象就可以了。

好,然后呢,来指定一下我们这个规则文件呢,它的这个什么呢,dialect,对吧,大家还记得吧,就是它使用的这个语言,对吧,咱们呢,使用java就可以了。

好,接下来呢,我们来编写规则。

咱们是不是一共有四个规则,回到这边来,对吧,一共有四个规则,那么一千颗以内的这种,那么这个结果直接就是二十元,对吧。

所以说这个是比较简单的,咱们先定义第一个规则,这个规则的名称呢,我们复制一下,就是这个,使用如了关键字,后边是规则的名称,对吧,规则的名称我直接粘贴在这个位置。

然后呢,我们是不是来指定win,先把整体这个结构写一下吧,win。

然后,然后呢,咱们要匹配的话呢,肯定是模式匹配,对吧,那么需要我们的程序啊,给我们传进来这么两个对象,一个是什么呢,一个是这个address ruler,还有一个是address check result。

address ruler里边封装的是什么呢,就是我们规则计算的这些参数,而这个result呢,其实封装的就是我们计算之后的结果,对吧。

好,那也就是说我们工作内存里面必须得有address ruler这种对象。

好,咱们就叫address.

address ruler。

好,address ruler。

然后呢,第一个呢,是不是要求是1000克以内的,对吧,总的重量是1000克以内,也就是我们的这个什么total weight啊,哎,total weight不等于空。

同时什么呢,同时还要求它是不是total weight啊,应该是小于,对吧,小于,等于吧,小于等于。

好,1,1.00。

好。

因为它是一个double类型的,所以我们给它加个小数点。

那么1000克以内的。

同时呢,还需要,还需要在工作内存里面有我们这个什么check result对象,对吧。

check result。

好,咱们这个叫做address check result。

这里边这个参数呢,就不用去设置了。

然后呢,如果能匹配上,匹配上的话呢,这种呢,我们是不是这个订单价格就不用算了。

因为它是1000克以内,所以直接设置它这个result就可以了。

直接设置result啊。

别忘了,我们先来check result点,set什么呢,它这里边是不是有两个啊。

一个是这个匹配的结果,对吧,匹配的结果。

匹配上是这条了,那么我们给它设置成处。

好。

然后呢,再来设置什么呢,设置我们这个订单价格。

set result,订单的价格呢,是不是就是20。

好。

订单价格就是20。

这个呢,就已经匹配上了。

为了一会儿呢,便用我们测试呢,咱们可以给它来一个输出语句啊,来一个输出语句。

好。

这个输出语句呢,咱们就写这个。

好。

OK。

这是第一个规则,是不是就已经搞定了。

然后接下来呢,我们是不是来编写第二个规则啊。

在这儿来写第二个规则,ruler。

然后呢,规则的名称呢,还是我们来复制一下。

规则的名称,就是这个。

好。

这个规则的名称比较长。

嗯。

这都没有关系啊。

好。

这是规则名称。

然后呢,我们写win。

然后,then,and。

好。

先把整体这个结构啊,给它写上。

然后接下来呢,我们是不是来进行匹配。

这个匹配的话呢,咱们就把上面这个抄一下。

然后呢,相应的稍微修改一下就可以。

主要是改第一个。

就是这个地方。

对吧。

这个要求是什么呢?

这个total weight啊,是不是应该是什么,1000克以上,对吧。

对吧。

对吧。

所以这个地方呢,应该是1000克以上。

所以这个地方呢,应该是1000克以上。

这个地方呢,应该是大于1。

同时什么呢?

是不是要求我们这个订单的距离。

订单距离是200公里以下,对吧。

200公里以下。

所以说应该就是我们这个distance啊。

distance是不是应该是小于200。

小于200。

好。

嗯。

因为都是w类型的,所以都给它加个小数点。

好。

这是我们这个,呃,要求的是重量,对吧。

重量大于1。

然后呢,订单距离小于200。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

所以我们这个,到时候呢,呃,通过百度地图来计算订单距离的时候呢,需要给它换算成公里啊。

因为我们前面讲那个接口的时候呢,它的单位还是米,对不对?

所以说呢,我们还需要给它来这个换算一下。

好。

那么换算成这个公里,也就是千米,其实是一回事儿啊。

然后呢,传进来,在这儿呢,来进行匹配,就可以了。

好。

呃,这是咱们这个toto位的。

那么如果是匹配上这一条之后呢,是不是就要执行?

我们Zen这一部分

这一部分的话就怎么算呢

这个时候呢

我们是不是就需要来设置什么呢

设置相应的什么手中啊

什么手中价格啊等等

把这些参数都设置好

设置好之后呢

调用我们刚才编写的service的这个方法

对吧

调用这个方法来进行计算

所以你看我们其实在这个规则文件里面呢

只是把我们要计算之前的这些参数给它设置好

真正计算的逻辑呢

是封上到这个service里面去了

当然前面我们其实也提到了

就是说我们这块计算的逻辑呢

你其实写在规则文件里面

在我这个Zen这个部分来算

也是没有问题的

也是没有问题的

就是都可以

只不过是什么呢

因为我们后边这三条啊

它计算的逻辑是不是都一样的

无非就是什么呢

这个序重这个数字不一样

对吧

整个计算的流程都一样

所以说呢

我就不在这个规则文件里面重复写三遍了

而是在我们这个方法上统一抽取一遍

就可以了

然后在这个地方呢

我们直接调这个service

所以大家明白这个意思就可以了

好

那么在这个地方呢

我们是不是就需要给我们这个address ruler

这个fact对象来set一下

set什么呢

一个是什么呢

叫做first fee

这叫做手中价格对吧

手中价格是不是20

然后呢

还有什么呢

还有就是我们这个

这个first weight对吧

手中

手中的话是不是就是1

好

但是都加上小数字

好

小数点

然后呢

还有什么呢

是不是还有这个序重对吧

序重的话是不是叫做continued fee

continued fee

序重的话应该是6

因为我们匹配的是第二条对吧

第二条

所以它这个序重呢是6

然后呢

我们把这三个参数是不是给它

这个设置好就可以了

设置好之后啊

然后呢

传给我们的service就可以了

那有的同学可能会有疑问

他说你怎么这个地方不设置好

设置这个货物总重量啊

其实货物总重量不是在我们这个地方设置的啊

不是在这个地方设置的

货物总重量是不是应该是由前端传给我们的

也就是说它其实在

将这个fact的对象啊

也就是这个address ruler对象

传进来的时候呢

那个total weight呢

就已经确定了

就已经确定了

所以说我们这个地方不用设置

你看咱们这是不是使用它作为一个什么条件进行匹配对吧

所以说我们在这个地方只要设置这三个参数就可以了

好

那么设置完之后呢

咱们是不是需要来创建一个service对象

这个service对象呢

就是它

把这个service创建出来

当然需要创建它的实现类对吧

impl

然后呢

我们就可以来调用它

它是不是里边是不是有这么一个方法

叫做什么呢

这个calculate fee

然后呢

把咱们这个address ruler对象是不是给传进去

好

传进去之后呢

它就会给我们返回这个价格对吧

订单价格

对吧

我们叫order amount吧

order amount

好

订单价格

好

然后呢

我们是不是就可以来设置相应的结果

这个结果的话呢

就跟这儿是类似的了

把这个拷过来

只不过呢

我们这个价格这儿就不是固定了20了

而是什么呢

我们计算出来的这个值

好

OK

那接下来呢

我们可以在这儿来输出一句话

便于我们一会儿测试对吧

好

如果说在控制台能看到这句话

那就说明是这条规则被触发了

好

这是我们第二条规则

是不是就已经写完了

然后接下来呢

我们把这个规则呀

复制一下

把它改造成我们第三条规则

这个改造呢

其实就非常简单了

那么

你看变化是不是非常小

就是序重这一块

是不是把这个原先的6给它改成9就可以了

这个地方覆盖一下

然后呢

这个地方

我们可以把这个原先的6给它改成9就可以了

那我们来看啊

Total weight还是大于1对吧

总重量大于1

同时呢

这个距离

你看啊

这个订单距离应该是200到500公里对吧

所以说这个distance应该是小于什么呢

小于500

然后呢

同时大于200对吧

同时

这个distance啊

应该是大于200

把这个范围给它卡好了

就可以了

然后接下来呢

我们把这个序重呢

给它改成9

就可以了

好

然后呢

把下面这个输出语句呢

也给它同步的改过来啊

要不然就有奇异了

好

把这块拿过来

OK

这样的话

我们第三条规则是不是就写完了

然后呢

我们再把第三条规则复制一下

然后呢

给它改成改造成第四条规则

第四条规则

把这个规则名称啊

Ctrl C复制一下

那这个时候呢

它这个订单的距离呢

注意看是500公里

以上对吧

500公里以上

那我们这个呢

就不要了

大于500

500公里以上

然后呢

把这块呢

改成什么呢

是不是改成15

好

咱们把这块呢

再来复制一下

Ctrl C复制一下

OK

保存一下

这是我们整体呢

把这四条规则呢

其实就已经写完了

对吧

就已经写完了

但是在这个地方呢

要注意一下

我们这个边界呢

边界值对吧

你比如说我们这个500

下面这个呢

写的是大于500

对吧

然后呢

上面这个是小于500

那恰好

假设我们算出来一个距离

恰好是500整

那500整的话

它是不是两头都够不着啊

所以说这个边界值呢

咱们需要给它来处理一下

看一下我们这边是怎么处理的

跟我们讲义保持一致就可以了

看看它是往上去

还是往下去

这是小于200

没有等号对吧

这是大于200

对吧

这个地方呢

好像我们这块呢

都没有处理

那么咱们需要来处理一下

这个边界值啊

咱们这样

咱们把这个边界值

给它处理一下

这样

我这儿呢

写个小于等于

对吧

小于等于

这样是不是就包含200了

然后呢

我们这儿呢

写个小于等于

这样是不是就

包含这个500了

对吧

这样就没有问题了

你看啊

这个边界值就没有问题了

那么相当于是什么呢

小于等于200

200的话是归到这一条

然后如果是大于200

200到500之间

对吧

但是这边呢是包含500

那么它会符合这一条

然后大于500的话

那就符合最后一条

好

这样是不是就没有问题了

咱们把这个边界值给它处理一下

好

就是防止出现这种正好是边界值

对吧

那这个时候呢

两条都够不着

那这样就比较尴尬啊

好

那这样的话呢

我们这个规则文件呢

就已经写好了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个基于 **Drools** 规则引擎的订单运费计算系统的开发演示。讲师通过 IntelliJ IDEA 开发环境，逐步展示了如何实现一个服务接口 `DroolsRulesService`，并编写对应的 Drools 规则文件 `orderAmountCalc.drl` 来处理不同重量和距离条件下的运费计算逻辑。演示内容包括：创建服务实现类、编写规则文件、定义多个规则（按重量和距离分段计费）、以及在主方法中进行测试调用。整个过程旨在说明如何将业务规则与核心代码解耦，通过规则引擎实现灵活的业务逻辑管理。

---

### 2) 按时间顺序的章节（带时间点）

*   **0:00 - 0:05**: 视频开头，展示项目结构和当前正在编辑的 `DroolsRulesServiceImpl.java` 文件，讲师说明这是第四步，即创建接口的实现类。
*   **0:05 - 0:15**: 讲师在 `DroolsRulesServiceImpl.java` 中编写 `calcFee` 方法的实现，使用 `BigDecimal` 进行精确的金额计算，包括计算差额、保留整数部分和计算续重费。
*   **0:15 - 0:25**: 讲师切换到 `orderAmountCalc.drl` 文件，开始编写 Drools 规则。首先定义了 `package` 和 `import` 语句，并设置 `dialect "java"`。
*   **0:25 - 0:35**: 讲师编写第一个规则，用于处理“1千克以内20元”的计费场景，规则中设置 `checkResult` 的状态和打印日志。
*   **0:35 - 0:45**: 讲师编写第二个规则，用于处理“1千克以上，订单距离在200公里以下”的计费场景，规则中设置 `addressRule` 的 `firstFee`、`firstWeight` 和 `continuedFee`。
*   **0:45 - 0:55**: 讲师在主方法中调用 `calcFee` 方法，并打印出计算结果，验证规则是否生效。
*   **0:55 - 1:05**: 讲师继续编写第三个规则，用于处理“订单距离在200~500公里”的计费场景，设置 `continuedFee` 为 9 元。
*   **1:05 - 1:15**: 讲师编写第四个规则，用于处理“订单距离在500公里以上”的计费场景，设置 `continuedFee` 为 15 元。
*   **1:15 - 1:25**: 讲师在主方法中添加了对第四个规则的测试调用，并打印出相应的结果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲显示当前章节为“7.2 实现步骤”。
    *   屏幕左上角显示了项目结构，包括 `pd-oms`、`pd-service-api`、`pd-user` 等模块。
    *   屏幕右下角有水印“海量一手资源：666java.com”。

*   **代码关键内容**:

    **Java 服务实现类 (`DroolsRulesServiceImpl.java`)**
    ```java
    package com.ithema.pinda.service.impl;

    import com.ithema.pinda.entity.fact.AddressRule;
    import com.ithema.pinda.service.DroolsRulesService;
    import org.springframework.stereotype.Service;
    import java.math.BigDecimal;

    public class DroolsRulesServiceImpl implements DroolsRulesService {
        public String calcFee(AddressRule addressRule) {
            // 计算总重量与首重差额
            BigDecimal lost = new BigDecimal(addressRule.getTotalWeight()).subtract(new BigDecimal(addressRule.getFirstWeight()));
            // 保留整数部分
            lost = lost.setScale(0, BigDecimal.ROUND_DOWN);
            // 计算续重费
            BigDecimal continuedFee = lost.multiply(new BigDecimal(addressRule.getContinuedFee())).toString();
            // 返回总费用
            return continuedFee.add(new BigDecimal(addressRule.getFirstFee())).toString();
        }
    }
    ```

    **Drools 规则文件 (`orderAmountCalc.drl`)**
    ```drl
    package rules;
    import com.ithema.pinda.entity.fact.AddressRule;
    import com.ithema.pinda.entity.fact.AddressCheckResult;
    import com.ithema.pinda.service.DroolsRulesService;
    import com.ithema.pinda.service.impl.DroolsRulesServiceImpl;

    dialect "java"

    rule "1千克以内20元"
        when
            addressRule : AddressRule(totalWeight != null && totalWeight <= 1.00)
            checkResult : AddressCheckResult()
        then
            checkResult.setPostCodeResult(true);
            checkResult.setResult("20");
            System.out.println("1千克以内20元");
        end

    rule "1千克以上，订单距离在200公里以下的，首重1千克，首重价格20元，续重每1千克资费为6元"
        when
            addressRule : AddressRule(totalWeight != null && totalWeight > 1.00 && distance < 200.00)
            checkResult : AddressCheckResult()
        then
            addressRule.setFirstFee(20.00);
            addressRule.setFirstWeight(1.00);
            addressRule.setContinuedFee(6.00);
        end

    rule "1千克以上，订单距离在200~500公里的，首重1千克，首重价格20元，续重每1千克资费为9元"
        when
            addressRule : AddressRule(totalWeight != null && totalWeight > 1.00 && distance >= 200.00 && distance < 500.00)
            checkResult : AddressCheckResult()
        then
            addressRule.setFirstFee(20.00);
            addressRule.setFirstWeight(1.00);
            addressRule.setContinuedFee(9.00);
        end

    rule "1千克以上，订单距离在500公里以上的，首重1千克，首重价格20元，续重每1千克资费为15元"
        when
            addressRule : AddressRule(totalWeight != null && totalWeight > 1.00 && distance >= 500.00)
            checkResult : AddressCheckResult()
        then
            addressRule.setFirstFee(20.00);
            addressRule.setFirstWeight(1.00);
            addressRule.setContinuedFee(15.00);
        end
    ```

    **主方法测试代码 (`DroolsRulesServiceImpl.java`)**
    ```java
    public static void main(String[] args) {
        AddressRule addressRule = new AddressRule();
        addressRule.setTotalWeight(5.3);
        addressRule.setFirstWeight(1);
        addressRule.setFirstFee(20);
        // ... (后续规则调用)
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：服务接口实现** (0:00 - 0:15)
    *   讲师在 `DroolsRulesServiceImpl.java` 文件中，编写了 `calcFee` 方法的实现。
    *   该方法接收一个 `AddressRule` 对象，计算总运费，逻辑包括：计算总重量与首重的差额、保留整数部分、计算续重费，并返回总费用。
    *   代码中使用了 `BigDecimal` 类型以确保金额计算的精确性。

*   **场景二：规则文件编写** (0:15 - 1:25)
    *   讲师在 `orderAmountCalc.drl` 文件中，逐步编写了四个规则。
    *   **规则一**：处理“1千克以内20元”的场景，规则中设置 `checkResult` 的状态并打印日志。
    *   **规则二**：处理“1千克以上，订单距离在200公里以下”的场景，规则中设置 `addressRule` 的 `firstFee`、`firstWeight` 和 `continuedFee`。
    *   **规则三**：处理“订单距离在200~500公里”的场景，设置 `continuedFee` 为 9 元。
    *   **规则四**：处理“订单距离在500公里以上”的场景，设置 `continuedFee` 为 15 元。
    *   讲师在每个规则中都使用了 `when` 和 `then` 子句来定义条件和动作。

*   **场景三：主方法测试** (0:45 - 1:25)
    *   讲师在 `main` 方法中创建了 `AddressRule` 对象，并设置了不同的重量和距离参数。
    *   讲师调用 `calcFee` 方法，并打印出计算结果，验证规则是否按预期工作。
    *   通过在主
