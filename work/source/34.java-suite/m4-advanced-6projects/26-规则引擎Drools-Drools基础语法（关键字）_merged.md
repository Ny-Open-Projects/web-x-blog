# 26-规则引擎Drools-Drools基础语法（关键字） — 课程文稿（声音线+画面线 合并稿）

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

我们可以用这个规则名称

但是在这儿我们需要强调一下

如果说我在这儿

注意看ruler

后边这是不是定义的是规则的名称

我用的是一对双引号

这里边我来写一个true

行不行

注意这种写法其实是可以的

因为什么呢

我们认为整个我选中的这块

这个字符串

它是规则的名称

对吧

所以这样的话其实是没有问题的

那么我们说绝对不能用指的是这种写法

你注意看

它现在是不是已经开始报错了

所以我们可以来写一个true

所以我们可以来看一下

我如果说把它当成一个字符串来写

通过双引号给它引起来

这种写法其实是没有问题的

咱们可以来执行一下

大家来看

随便来执行一个单元测试就可以

你看我们这个是不是还是通过了

没有报错

但是呢

如果说你把这个规则的名称

是这样来写的

这样来写

那么你看

首先从这个地方

它是不是就已经

校验的时候

对吧

这个规则文件

校验的时候就已经报错了

同时呢

我们再来执行一下这个单元测试

你看它是不是已经开始报错了

开始报错了

所以说

这是我们这个硬关键字

那可能有的同学就说了

那如果说

我把它撤销回来

这种情况

你看

因为我们现在写的这个呢

它并不是关键字

对吧

并不是硬关键字

在这种情况下呢

其实呢

我们是可以什么呢

是可以把这个什么呢

把这个双引号给它去掉的

但是需要注意的是什么呢

因为双引号去掉了

我们为了能保证

这个是我们一个整体

对吧

所以你这儿呢

肯定就不能有空格了

就不能有空格了

表示我通过一个下滑线

好

这种其实是可以的

然后呢

我们重新再来执行一下

这个单元测试

好

你看它是不是还是可以正常执行

所以说呢

如果说我们用的不是硬关键字的话

并且呢

这中间是不是没有空格呀

相当于它是一个整体完整的字符串

一个整体

这个时候呢

其实你没有双引号也是可以的

只不过呢

我们是强烈建议啊

大家在定义规则名称的时候

尽量使用这种双引号

好

这种的是比较规范的一种写法

而且还有什么好处呢

就是刚才我们看到了

如果你双引号的话

它是不是自动能识别出来

这是规则名称是一个整体

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

true false还有no

这三个是都不能用的

比如说我在这呢

我给它改成no

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

其实都是它提前

提前的

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

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段为一门关于 **Drools 规则引擎** 的技术课程。讲师通过 **IntelliJ IDEA** 集成开发环境，演示了如何在 Java 项目中使用 Drools 进行规则匹配和执行。主要内容包括：
*   **理论讲解**：在 PPT 中讲解了 Drools 的核心概念，如“硬关键字”（Hard keywords）和“软关键字”（Soft keywords），以及内置方法（如 `update`、`insert`、`retract`）的作用。
*   **代码实践**：在 IDE 中编写并运行了测试代码，演示了如何创建 `KieServices`、`KieContainer`、`KieSession`，以及如何创建和设置 `Fact` 对象。
*   **规则文件编写**：在 `comparisonOperator.drl` 文件中编写了两个规则，分别用于测试“匹配操作符”和“不匹配操作符”的场景。
*   **结果演示**：通过运行测试，展示了规则引擎如何根据事实对象的属性匹配规则，并输出相应的日志信息。

整个过程旨在帮助学习者理解 Drools 的基本工作流程和核心 API 的使用方法。

---

### 2) 按时间顺序的章节（带时间点）

由于无法提供精确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:15**: **课程引入与PPT讲解**。讲师展示 PPT，讲解 Drools 的“硬关键字”和“软关键字”的区别，强调硬关键字的强制性。
*   **00:15 - 00:30**: **PPT讲解“内置方法”**。讲师继续讲解 PPT，介绍 Drools 的内置方法（如 `update`、`insert`、`retract`）的作用，即通过修改工作内存中的 Fact 来控制规则的执行。
*   **00:30 - 00:45**: **IDE环境与测试代码演示**。讲师切换到 IntelliJ IDEA，展示项目结构，并开始讲解 `DroolsTest.java` 文件中的测试方法 `test3()`，用于执行指定规则。
*   **00:45 - 01:00**: **规则文件编写与测试**。讲师在 `comparisonOperator.drl` 文件中编写了两个规则：`rule_comparison_matches` 和 `rule_comparison_not matches`，并演示了如何通过 `KieSession.fireAllRules()` 来触发它们。
*   **01:00 - 01:15**: **运行测试与结果分析**。讲师运行测试，终端输出显示规则 `rule_comparison_notcontains` 和 `rule_comparison_not memberOf` 被触发，说明规则引擎成功匹配了事实对象。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 关键内容

*   **4.7 关键字**：
    *   **硬关键字 (Hard keywords)**：`true`, `false`, `null`。这些关键字在规则文件中定义包名或规则名时**不能使用**，否则会报错。
    *   **软关键字 (Soft keywords)**：`lock-on-active`, `date-effective`, `date-expires`, `no-loop`, `auto-focus`, `activation-group`, `agenda-group`, `ruleflow-group`, `entry-point`, `duration`, `package`, `import`, `dialect`, `salience`, `enabled`, `attributes`, `rule`, `extend`, `when`, `then`, `template`, `query`, `declare`, `function`, `global`, `eval`, `not`, `in`, `or`, `exists`, `forall`, `accumulate`, `collect`, `from`, `action`, `reverse`, `result`, `end`, `over`, `init`。这些关键字**可以使用**，但**不建议使用**，因为它们可能与规则引擎的内部机制冲突。

*   **4.8 Drools内置方法**：
    *   规则文件的 RHS 部分的主要作用是通过插入、删除或修改工作内存中的 Fact 数据，来达到控制规则引擎执行的目的。
    *   Drools 提供了一些方法（如 `update`、`insert`、`retract`）来操作工作内存中的数据。操作完成后，规则引擎会重新进行相关规则的匹配。原来没有匹配成功的规则，在我们修改数据完成后，有可能就会匹配成功。

#### 代码关键内容

*   **Java 测试代码 (`DroolsTest.java`)**：
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

*   **Drools 规则文件 (`comparisonOperator.drl`)**：
    ```drl
    // 测试比较操作符 matches
    rule "rule_comparison_matches"
        when
            ComparisonOperatorEntity(names matches "王.*")
        then
            System.out.println("规则: rule_comparison_matches触发了...");
        end

    // 测试比较操作符 not matches
    rule "rule_comparison_not matches"
        when
            ComparisonOperatorEntity(names matches "王.*")
        then
            System.out.println("规则: rule_comparison_not matches触发了...");
        end
    ```

---

### 4) 关键场景与演示描述

*   **场景一：PPT讲解硬关键字与软关键字**。
    *   讲师在 PPT 上展示“硬关键字”和“软关键字”的列表，并强调硬关键字的强制性，即在规则文件中定义包名或规则名时不能使用。
    *   讲师解释软关键字虽然可以使用，但不建议使用，因为它们可能与规则引擎的内部机制冲突。

*   **场景二：IDE环境中的测试代码演示**。
    *   讲师在 IntelliJ IDEA 中展示 `DroolsTest.java` 文件，重点讲解 `test3()` 方法。
    *   讲师演示了如何通过 `KieServices` 获取 `KieContainer`，再通过 `KieContainer` 获取 `KieSession`。
    *   讲师创建了一个 `ComparisonOperatorEntity` 类的实例，并为其设置属性值。

*   **场景三：规则文件编写与规则触发演示**。
    *   讲师在 `comparisonOperator.drl` 文件中编写了两个规则，分别用于测试“匹配操作符”和“不匹配操作符”的场景。
    *   讲师在 `DroolsTest.java` 中调用 `kieSession.fireAllRules()` 方法来触发规则。
    *   讲师运行测试，终端输出显示规则 `rule_comparison_notcontains` 和 `rule_comparison_not memberOf` 被触发，说明规则引擎成功匹配了事实对象。

*   **场景四：结果分析与总结**。
    *   讲师分析了测试结果，说明规则引擎根据事实对象的属性匹配了相应的规则。
    *   讲师总结了 Drools 的基本工作流程和核心 API 的使用方法。
