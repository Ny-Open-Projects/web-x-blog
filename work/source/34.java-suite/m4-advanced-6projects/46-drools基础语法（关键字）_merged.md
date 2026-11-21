# 46-drools基础语法（关键字） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来我们继续来学习D-Rose基础语法

那么接下来我们要学习的是关键字

其实我们都知道

咱们在编写Java代码的时候

是不是就涉及到很多关键字

那么在我们的规则文件当中

也存在关键字

只不过D-Rose里边这些关键字

它是分成两类

一类叫做硬关键字

其实就是hard keywords

和这个什么呢

软关键字叫soft keywords

那么这两类关键字有什么区别呢

是这样的

硬关键字是我们在规则文件中

定义包名或者是规则名是

不能使用的

否则程序会报错

也就是说硬关键字是一定不能使用的

否则程序它会报错

而这个软关键字

其实是可以使用的

只不过是不建议使用

所以说它是分成硬关键字

软关键字两类

硬关键字是绝对不能用的

如果你用了的话

那程序都会报错

那接下来我们来看一下

硬关键字比较少

就三个

一个是true

一个是false

还有一个是not

软关键字就比较多了

但是现在可能大家看的这些

不太熟悉

这些有很多是什么呢

是我们在规则文件当中

它对应的一些属性

后边我们随着讲这个规则属性的时候

你会发现

你看这个lock on active

什么

data effective等等这些

其实都是对应的一些属性名

那么既然是属性的话

我们就不建议

你把它定义成包名

或者规则名称了

所以说下面这些是不建议使用的

咱们可以来演示一下

我们主要就是拿硬关键字来演示一下

比如说true false还有not

这是这么三个硬关键字

刚才我们提到

它是绝对不能用做什么呢

我们的这个规则名称的

但是在这儿呢

我们需要强调一下

如果说

如果说我在这儿

注意看 ruler

后边这是不是定义的是规则的名称

我用的是一对双引号

这里边呢

我来写一个true

行不行啊

注意这种写法其实是可以的

因为什么呢

我们认为整个我选中的这块

这个字符串

它是规则的名称

对吧

所以这样的话

其实是没有问题的

那么我们说绝对不能用

指的是这种写法

你注意看

它现在是不是已经开始报错了

哎

哎

所以我们可以来看一下

我如果说把它当成一个字符串来写

通过双引号给它引起来

这种写法其实是没有问题的

咱们呢

可以来执行一下

大家来看

随便来执行一个单元测试就可以啊

你看我们这个是不是还是通过了

哎

没有报错

但是呢

如果说你把这个规则的名称

是这样来写的

这样来写

好

那么你看

首先从这个地方

它是不是就已经

嗯

校验的时候

对吧

这个规则文件

校验的时候就已经报错了

同时呢

我们再来执行一下这个单元测试

哎

你看它是不是已经开始报错了

开始报错了

所以说啊

这是我们这个硬关键字

那可能有的同学就说了

那如果说

我把它撤销回来啊

这种情况

你看啊

因为我们现在写的这个呢

它并不是关键字

对吧

并不是硬关键字

在这种情况下呢

其实呢

我们是可以什么呢

是可以把这个什么呢

把这个双引号给它取回来

去掉的

但是需要注意的是什么呢

因为双引号去掉了

我们为了能保证

这个是我们一个整体

对吧

所以你这儿呢

肯定就不能有空格了

就不能有空格了

表示我通过一个下发线

好

这种其实是可以的啊

然后呢

我们重新再来执行一下

这个单元测试

好

你看它是不是还是可以正常执行

嗯

所以说呢

如果说我们用的不是硬关键字的话

并且呢

这中间是不是没有空格呀

相当于它是一个整体完整的字符串

嗯

一个整体的字符串

一个整体

这个时候呢

其实你没有双引号也是可以的

只不过呢

我们是强烈建议啊

大家在定义规则名称的时候

尽量使用这种双引号

好

这种呢

是比较规范的一种写法

而且还有什么好处呢

就是刚才我们看到的

如果你双引号的话

它是不是自动能识别出来

这是规则名称

是一个整体

所以即使说你这里边有空格

它也没有问题

对吧

其实是这种方式

它也没有问题

因为它是一个整体了嘛

大家来看一下

你看

还是可以的

好

这是我们刚才说了一下

咱们这个硬关键字

对吧

true false还有now

这三个是都不能用的

比如说我在这呢

我给它改成now

这种呢

也是不可以的

也是不可以的

好

那么关于这些软关键字呢

我们就不再试了

因为软关键字呢

其实是可以使用的

对吧

可以使用

但是只是不建议啊

只是不建议使用

因为呢

我们下面看到的这些呢

其实都是不建议的

就是它提前

我们后边学习语法的时候

你就知道了

是它的一些属性

属性

所以说呢

就不建议把它作为规则名称

或者是包名了

OK

这是关于咱们这个关键字

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段为一门关于 **Drools 规则引擎** 的技术课程。讲师正在演示如何在 Java 项目中使用 Drools 的内置方法来执行规则。视频内容主要围绕 **“执行指定规则”** 这一主题展开，通过一个具体的测试用例 `test3()` 来展示如何创建 `KieSession`、插入事实对象 `ComparisonOperatorEntity`，并最终触发规则。过程中，讲师通过 IntelliJ IDEA IDE 展示了代码编写、调试和运行测试的全过程，并在遇到错误时（如 `java.lang.RuntimeException: Error while creating kieBase`）进行了分析和演示。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: 课程引入，展示课程大纲，定位到“4.7 关键字”和“4.8 Drools内置方法”章节。
*   **00:05 - 00:15**: 讲师讲解 Drools 的“硬关键字”和“软关键字”的概念，并列出其具体名称。
*   **00:15 - 00:25**: 讲师过渡到“4.8 Drools内置方法”章节，解释规则文件的 RHS 部分的作用。
*   **00:25 - 00:35**: 讲师在 IntelliJ IDEA 中打开项目，展示 `DroolsTest.java` 文件，并定位到 `test3()` 方法。
*   **00:35 - 00:45**: 讲师编写并运行 `test3()` 方法，该方法用于测试“执行指定规则”的功能。
*   **00:45 - 00:55**: 讲师在 `DroolsTest.java` 中编写规则文件 `comparisonOperator.drl` 的内容，定义了两个规则：`rule_comparison_matches` 和 `rule_comparison_not_matches`。
*   **00:55 - 01:05**: 讲师运行测试，但测试失败，终端输出错误信息 `java.lang.RuntimeException: Error while creating kieBase`。
*   **01:05 - 01:15**: 讲师分析错误，指出问题在于规则中使用了硬关键字 `true`，但未在规则文件中定义包名或规则名，导致程序报错。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “4.7 关键字”、“4.8 Drools内置方法”。
    *   **硬关键字**: `true`, `false`, `null`。
    *   **软关键字**: `lock-on`, `active`, `date-effective`, `date-expires`, `no-loop`, `auto-focus`, `activation-group`, `agenda-group`, `ruleflow-group`, `entry-point`, `duration`, `package`, `import`, `dialect`, `salience`, `enabled`, `attributes`, `rule`, `extend`, `when`, `then`, `template`, `query`, `declare`, `function`, `global`, `eval`, `not`, `in`, `or`, `exists`, `forall`, `accumulate`, `collect`, `from`, `action`, `reverse`, `result`, `end`, `over`, `init`。
    *   **Drools内置方法**: `update`, `insert`, `retract`。
    *   **规则文件 RHS 部分的作用**: 通过插入、删除或修改工作内存中的 `Fact` 数据，来控制规则引擎的执行。

*   **代码关键内容**:
    *   **Java 测试代码 (`DroolsTest.java`)**:
        ```java
        // 获取Kie容器对象
        KieServices kieServices = KieServices.Factory.get();
        KieContainer kieContainer = kieServices.newKieClasspathContainer();
        // 从Kie容器对象中获取会话对象
        KieSession session = kieContainer.newKieSession();

        // Fact对象，事实对象
        ComparisonOperatorEntity fact = new ComparisonOperatorEntity();
        fact.setNames("李四");
        ```
    *   **Drools 规则文件 (`comparisonOperator.drl`)**:
        ```drl
        rule "rule_comparison_matches"
            when
                ComparisonOperatorEntity(names matches "王.*")
            then
                System.out.println("规则：rule_comparison_matches触发了...");
            end

        rule "rule_comparison_not_matches"
            when
                ComparisonOperatorEntity(names matches "李.*")
            then
                System.out.println("规则：rule_comparison_not_matches触发了...");
            end
        ```
    *   **错误信息**:
        ```
        java.lang.RuntimeException: Error while creating kieBase
        ...
        Message [id=2, kieBase=myKbase, level=ERROR, text=Parser returned a null Package]
        ```

---

### 4) 关键场景与演示描述

*   **场景一：讲解关键字概念** (00:05 - 00:15)
    *   讲师在 PPT 上展示“4.7 关键字”章节，解释硬关键字和软关键字的区别。
    *   通过列出硬关键字 `true`, `false`, `null` 和软关键字列表，强调硬关键字在规则文件中必须明确使用，否则会报错。

*   **场景二：演示执行指定规则** (00:25 - 00:45)
    *   讲师在 IntelliJ IDEA 中打开项目，展示 `DroolsTest.java` 文件。
    *   讲师定位到 `test3()` 方法，该方法用于测试“执行指定规则”的功能。
    *   讲师在代码中创建 `KieSession` 对象，并插入一个 `ComparisonOperatorEntity` 事实对象。

*   **场景三：编写和测试规则** (00:45 - 00:55)
    *   讲师在 `comparisonOperator.drl` 文件中编写两个规则，分别匹配以“王”和“李”开头的姓名。
    *   讲师在 `DroolsTest.java` 中调用 `kieSession.fireAllRules()` 方法来触发所有规则。

*   **场景四：调试和分析错误** (00:55 - 01:15)
    *   讲师运行测试，但测试失败，终端输出错误信息。
    *   讲师分析错误，指出问题在于规则中使用了硬关键字 `true`，但未在规则文件中定义包名或规则名，导致程序报错。
    *   讲师在 PPT 上强调，硬关键字在规则文件中必须明确使用，否则会报错。

---

以上是根据视频画面进行的结构化分析。
