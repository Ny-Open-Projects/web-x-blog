# 43-drools基础语法（比较操作符_memberof和 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们的比较操作符啊,刚才呢,我们是演示了一下这个contains以及not contains,对吧,就是一个是包含,一个是不包含,对吧,就contains,not contains,然后再往下呢,我们要看的是这个什么呢,是这个member of以及not member of,好,在这儿呢,我们要测试的是这个,测试的是我们的比较操作符,对吧,比较操作符叫做member of,好,

那么我们把这个规则来写一下,这个规则的名称呢,我们把这个考一下,然后稍微修改一下,把这儿改成什么呢,改成我们的member of,然后后边是不是写问,然后是then,最后是and,然后这个问这个部分呢,这个呢,我们当时提过,这叫做lhs,对不对,然后then这个部分呢,是不是叫做rhs,好,然后在这部分我们应该怎么写呢,

其实跟前面这个写法非常类似,把它拿过来,首先呢,进行类型匹配,对吧,到工作内存里面去找这种类型的元素,并且这里边我们要测试的是member of,这个代表的就是什么呢,我们前面这个值必须是后边那个值的一个什么成员,比如说我们这里边是不是有个names属性,它要member of什么呀,list,大家还记得吧,在我们这个类里面是不是有个names属性,它是个词,

对吧,还有一个list的属性,它是这种集合类型的,那么我们现在这个表达式它的含义是什么呢,就是说我们必须要到工作内存里面去查找这么一种类型的元素,并且它的names属性要什么呢,要是我们这个list集合里边的一个成员,一个成员,member of,如果能够匹配成功的话,能够匹配成功的话,它是不是就要执行then这个部分,在then这个部分呢,我们现在呢也没什么好做的,所以我就直接输出了一下,

好,直接输出一下,咱们把这块呢来输出一下,规则,哪个规则呢,把这个规则的名称是不是来改造一下,改成这个,如果我们在控制台呢能够看到这句话的话,这就说明这个规则是成立了,好,那么这个规则呢,非常简单,我们就已经编写完了,重点呢就是来看一下这个member of它的用法,

然后接下来呢我们来执行一下咱们刚才编写的这个test2这个单元测试,

但是在执行之前呢我们先来分析一下,就拿我们当前给进去的这个值来看的话,我们当前刚刚编写的这个规则能够触发吗,那你就看names是不是这个list的一个元素呢,你看names我是不是给的是理4啊,而这个list里边只有一个元素是张三二对不对,那很明显,它是不是应该不会成立啊,你看啊,我现在来执行一下,来看控制台,

当然注意看啊,控制台输出的时候呢,

这个not contains那个啊,

因为我们刚才测试过了,它是不是是上面这个规则触发了,

下面这个规则是不是并没有触发,

那么现在呢我如果希望啊,

下面这个规则触发,

那怎么办呢,那是不是意味着我这个names啊,

必须是这个list它的一个元素,

names是不是理4,

那我list里边我是不是加一个理4进去就可以了,

你看啊,list.add,

什么呢,理4,

这样的话我的names是不是就是这个list它的一个元素了,

那这样的话呢,

我们就可以看到,

后边那个规则应该就可以触发了,

大家来看,

你看memberof,

这个时候呢它是不是就触发了,

它就触发这个规则了,

这是刚才我们测试了一下,

我们这个memberof,

那么同时呢我们再来复制一段,

给它加一个什么not memberof,

这个呢我们想测试的是not memberof,

把这儿呢是不是给加一个not就可以了,

注意中间是有空格的啊,

别连一块写,

然后呢在这儿我们来个not memberof,

好,

那就是不包含对吧,

不包含的话,

那又意味着我们这个这个这个names啊,

应该不是这个list它的成员变量,

那么当前呢,

很明显它是对吧,

是不是理4啊,

这儿也一个理4,

所以是它的成员变量,

那么我们刚刚编写的最后一个规则呢,

它应该是不能成立的,

你看它是不是并没有触发,

如果我想想上的触发的话呢,

那就,

那我就可以怎么做呢,

我把这个是不是给注视起来,

注视起来,

这是不是意味着我的这个names并不是这个list它的成员,

这样的话呢,

我们这个规则是不是就,

这个模式是不是就匹配上了,

匹配上之后呢,

那这个规则是不是就会触发,

好,

咱们来看一下,

好,

你看这个memberof,

当然了,

因为我那个代码改回去了,

原先,

原先这个是不是not contains这个也触发了,

也触发了,

好,

这个我们前面已经讲过了,

就不再多说了,

重点我们关注的是后边这个,

not memberof,

它是不是就触发了,

所以通过控制台这个输出呢,

我们也能够看到就是什么呢,

当我们在这个执行我们的这个规则引擎的时候呢,

有可能啊,

有多个规则是不是同时都都执行了,

因为它都匹配到了嘛,

所以说它并不是说只有一个规则能执行,

如果你所有的规则都能够匹配成功,

那它都可以触发,

就是说它可以同时触发多个规则,

这都是可以的,

好,

刚才呢,

我们主要就是讲了一下这个memberof,

以及not memberof,

这个这两个比较操作服,

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是一个关于 **Drools 规则引擎** 的 Java 项目实战教学。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 DRL（Drools Rule Language）文件中定义和测试不同的比较操作符（`contains`, `not contains`, `memberOf`）。视频的核心是编写和调试规则，并通过 Java 测试类 `DroolsTest` 来验证规则引擎的执行结果。最终，通过运行测试，成功触发了 `not contains` 和 `memberOf` 两个规则，证明了规则的正确性。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从画面中精确获取时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: 开场，展示项目结构和 `comparisonOperator.drl` 文件，介绍将要演示的规则。
*   **00:05 - 00:15**: 演示 `contains` 和 `not contains` 操作符的规则。讲师在 DRL 文件中编辑并测试了这两个规则。
*   **00:15 - 00:25**: 演示 `memberOf` 操作符的规则。讲师在 DRL 文件中编写了 `memberOf` 规则，并在 `then` 子句中添加了打印语句。
*   **00:25 - 00:35**: 演示 `not memberOf` 操作符的规则。讲师在 DRL 文件中编写了 `not memberOf` 规则。
*   **00:35 - 00:45**: 转到 Java 测试类 `DroolsTest.java`，展示如何初始化 `KieContainer` 和 `KieSession`，并插入事实对象 `ComparisonOperatorEntity`。
*   **00:45 - 00:55**: 在测试类中调用 `session.fireAllRules()` 来激活并执行所有规则。
*   **00:55 - 01:05**: 运行测试，终端输出显示 `rule_comparison_notcontains` 和 `rule_comparison_memberOf` 规则成功触发，证明了规则引擎的工作。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **DRL 文件 (`comparisonOperator.drl`) 关键代码**:
    *   **`contains` 规则**:
        ```drl
        rule "rule_comparison_contains"
        when
            ComparisonOperatorEntity(names contains "张三")
            ComparisonOperatorEntity(list contains names)
        then
            System.out.println("规则: rule_comparison_contains触发了...");
        end
        ```
    *   **`not contains` 规则**:
        ```drl
        rule "rule_comparison_notcontains"
        when
            ComparisonOperatorEntity(names not contains "张三")
            ComparisonOperatorEntity(list not contains names)
        then
            System.out.println("规则: rule_comparison_notcontains触发了...");
        end
        ```
    *   **`memberOf` 规则**:
        ```drl
        rule "rule_comparison_memberOf"
        when
            ComparisonOperatorEntity(names memberOf list)
        then
            System.out.println("规则: rule_comparison_memberOf触发了...");
        end
        ```
    *   **`not memberOf` 规则**:
        ```drl
        rule "rule_comparison_not memberOf"
        when
            ComparisonOperatorEntity(names not memberOf list)
        then
            System.out.println("规则: rule_comparison_not memberOf触发了...");
        end
        ```

*   **Java 测试类 (`DroolsTest.java`) 关键代码**:
    *   **初始化 KieContainer 和 KieSession**:
        ```java
        KieServices kieServices = KieServices.Factory.get();
        KieContainer kieContainer = kieServices.newKieClasspathContainer();
        KieSession session = kieContainer.newKieSession();
        ```
    *   **插入事实对象并触发规则**:
        ```java
        // 假设 list 是一个包含 "张三" 的 List
        list.add("张三");
        fact.setList(list);
        session.insert(fact);
        session.fireAllRules(); // 激活并执行所有规则
        ```

---

### 4) 关键场景与演示描述

*   **场景一：编辑 `contains` 和 `not contains` 规则** (画面 00:05-00:15)
    *   讲师在 DRL 文件中，先定义了一个 `contains` 规则，用于匹配 `names` 字段包含 "张三" 且 `list` 字段包含 `names` 的对象。
    *   接着，他定义了一个 `not contains` 规则，用于匹配 `names` 字段不包含 "张三" 且 `list` 字段不包含 `names` 的对象。
    *   他通过在 `then` 子句中添加 `System.out.println` 语句来观察规则是否被触发。

*   **场景二：编写 `memberOf` 规则** (画面 00:15-00:25)
    *   讲师在 DRL 文件中，编写了一个名为 `rule_comparison_memberOf` 的规则。
    *   该规则的 `when` 子句使用了 `memberOf` 操作符，用于匹配 `names` 字段是 `list` 中的一个元素。
    *   他同样在 `then` 子句中添加了打印语句。

*   **场景三：编写 `not memberOf` 规则** (画面 00:25-00:35)
    *   讲师在 DRL 文件中，编写了一个名为 `rule_comparison_not memberOf` 的规则。
    *   该规则的 `when` 子句使用了 `not memberOf` 操作符，用于匹配 `names` 字段不是 `list` 中的任何一个元素。
    *   他同样在 `then` 子句中添加了打印语句。

*   **场景四：Java 测试类编写与执行** (画面 00:35-01:05)
    *   讲师切换到 `DroolsTest.java` 文件，编写了测试方法 `test20`。
    *   他在方法中初始化了 `KieContainer` 和 `KieSession`。
    *   他创建了一个 `ComparisonOperatorEntity` 对象，并设置其 `list` 属性为一个包含 "张三" 的列表。
    *   他将该对象插入到 `KieSession` 中，并调用 `session.fireAllRules()` 来激活所有规则。
    *   最后，他运行了测试，终端输出显示 `rule_comparison_notcontains` 和 `rule_comparison_memberOf` 规则成功触发，证明了规则引擎的正确性。
