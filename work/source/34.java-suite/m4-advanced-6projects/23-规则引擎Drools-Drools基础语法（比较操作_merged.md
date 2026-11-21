# 23-规则引擎Drools-Drools基础语法（比较操作 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

咱们继续来看我们的比较操作符啊

刚才呢我们是演示了一下这个contains

以及not contains

就是一个是包含

一个是不包含

然后再往下呢

我们要看的是这个什么呢

是这个member of

以及not member of

在这呢我们要测试的是这个

测试的是我们的比较操作符

比较操作符叫做member of

那么我们把这个规则来写一下

这个规则的名称呢

我们把这个考一下

然后稍微修改一下

把这改成什么呢

改成我们的member of

然后后边是不是写问

然后是then

最后是and

然后这个问这个部分呢

这个呢我们当时提过

这叫做lhs对不对

然后then这个部分呢

是不是叫做rhs

然后在这部分我们应该怎么写呢

其实跟前面这个写法非常类似

把它拿过来

首先呢进行类型匹配

对吧

到工作内存里面去找这种类型的元素

并且这里边我们要测试的是member of

这个代表的就是什么呢

我们前面这个值

必须是后边那个值的一个什么成员

比如说我们这里边是不是有个names属性

它要member of

什么呀list

大家还记得吧

在我们这个类里面

是不是有个names属性

它是个string

还有个list的属性

它是这种集合类型的

那么我们现在这个表达式

它的含义是什么呢

就是说我们必须要到工作内存里面

去查找这么一种类型的元素

并且它的names属性要什么呢

要是我们这个list集合里边的一个成员

一个成员member of

如果能够匹配成功的话

能够匹配成功的话

它是不是就要执行then这个部分

在then这个部分呢

我们现在呢也没什么好做的

所以我就直接输出了一下

好

直接输出一下

咱们把这块呢来输出一下

规则哪个规则呢

把这个规则的名称是不是来改造一下

改成这个

如果我们在控制台呢

能够看到这句话的话

这就说明这个规则是成立了

好

那么这个规则呢

非常简单

我们就已经编写完了

重点呢

就是来看一下这个member of

它的用法

然后接下来呢

我们来执行一下

咱们刚才编写的这个test2

这个单元测试

当然在执行之前呢

我们先来分析一下

就拿我们当前给进去的这个值来看的话

我们当前刚刚编写的这个规则能够触发吗

那你就看names是不是

这个list的一个元素呢

你看names我是不是给的是理四啊

而这个list里边只有一个元素是张三二

对不对

那很明显

它是不是应该不会成立啊

你看啊

我现在来执行一下

来看控制台

当然注意看啊

控制台输出的是

这个not-content那个啊

因为我们刚才测试过了

它是不是是上面这个规则触发了

下面这个规则是不是并没有触发

那么现在呢

我如果希望啊

下面这个规则触发

那怎么办呢

那是不是意味着我这个names啊

必须是这个list它的一个元素

names是不是理四

那我list里边

我是不是加一个理四进去就可以了

你看啊

list.add什么呢

理四

这样的话

我的names是不是就是这个list它的一个元素了

那这样的话呢

我们后边那个规则应该就可以触发了

大家来看啊

你看memberof

这个时候呢

它是不是就触发了

它就触发这个规则了啊

这是刚才我们测试了一下

我们这个memberof

那么同时呢

我们再来复制一段

给它加一个什么not member of

这个呢

我们想测试的是

not member of

把这呢

是不是给加一个not就可以了

注意中间是有空格的啊

别连一块写

然后呢

在这我们来个not member of

好

那就是不包含对吧

不包含的话

那又意味着我们这个这个这个names啊

应该不是这个list它的成员变量

那么当前呢

很明显它是对吧

是不是理四啊

这儿也一个理四

所以是它的成员变量

那么我们刚刚编写的最后一个规则呢

它应该是不能成立的

你看它是不是并没有触发

如果我想想上的触发的话呢

那就那我就可以怎么做呢

我把这个是不是给注视起来

注视起来

这是不是意味着我的这个names

并不是这个list它的成员

这样的话呢

我们这个规则是不是就这个模式是不是就匹配上了

匹配上之后呢

那这个规则是不是就会触发

咱们来看一下

你看这个memberof

当然了

因为我那个代码改回去了

原先原先这个是不是not contains这个也触发了

也触发了

这个我们前面已经讲过了

就不再多说了

重点我们关注的是后边这个

not memberof

它是不是就触发了

所以通过控制台这个输出呢

我们也能够看到就是什么呢

当我们在这个执行我们的这个规则引擎的时候呢

有可能啊

有多个规则是不是同时都都执行了

因为它都匹配到了嘛

所以说它并不是说只有一个规则能执行

如果你所有的规则都能够匹配成功

那它都可以触发

就是说它可以同时触发多个规则

这都是可以的

好

那我们主要就是讲了一下这个memberof

以及not memberof

这两个比较操作服

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析报告。

---

### 1) 视频摘要

本视频是一段关于 **Drools 规则引擎** 的技术教学演示，主要讲解如何在 Java 项目中使用 Drools 的 **比较操作符（Comparison Operators）**。演示者通过 IntelliJ IDEA 开发环境，展示了如何在 `rules.drl` 文件中定义规则，以及如何在测试类 `DroolsTest.java` 中加载规则、创建事实对象并触发规则匹配。视频重点演示了 `contains`、`not contains`、`memberOf` 和 `not memberOf` 四种比较操作符的用法，并通过控制台输出验证了规则的触发结果。

---

### 2) 按时间顺序的章节（带时间点）

由于无法提供精确的时间戳，以下章节按视频画面内容的逻辑顺序排列：

*   **章节 1: 项目结构与规则文件概览 (00:00 - 00:05)**
    *   展示了项目结构，重点是 `src/main/resources/rules/comparisonOperator.drl` 文件。
    *   画面显示了 `rule "rule_comparison_contains"` 的代码，用于演示 `contains` 操作符。

*   **章节 2: 演示 `not contains` 操作符 (00:05 - 00:15)**
    *   画面聚焦于 `rule "rule_comparison_notcontains"`，演示了 `not contains` 操作符。
    *   代码中包含 `names not contains "张三"` 和 `list not contains names`。

*   **章节 3: 演示 `memberOf` 操作符 (00:15 - 00:25)**
    *   画面切换到 `rule "rule_comparison_memberOf"`。
    *   代码中包含 `names memberOf list`，用于演示 `memberOf` 操作符。

*   **章节 4: 演示 `not memberOf` 操作符 (00:25 - 00:35)**
    *   画面展示了 `rule "rule_comparison_not memberOf"`。
    *   代码中包含 `names not memberOf list`，用于演示 `not memberOf` 操作符。

*   **章节 5: 测试类代码与规则触发 (00:35 - 00:50)**
    *   画面切换到 `DroolsTest.java` 文件。
    *   演示了如何通过 `KieServices` 和 `KieContainer` 获取规则引擎会话。
    *   代码中调用 `session.insert(fact)` 插入事实对象，并通过 `session.fireAllRules()` 触发规则匹配。

*   **章节 6: 规则触发结果验证 (00:50 - 01:00)**
    *   画面切换到控制台（Terminal）。
    *   显示了测试执行后的输出，确认了 `rule_comparison_notcontains` 和 `rule_comparison_memberOf` 两条规则成功触发。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段 (Drools 规则文件 `comparisonOperator.drl`)：**

    ```drl
    rule "rule_comparison_contains"
    when
        ComparisonOperatorEntity(names contains "张三")
        ComparisonOperatorEntity(list contains names)
    then
        System.out.println("规则：rule_comparison_contains触发了...");
    end

    rule "rule_comparison_notcontains"
    when
        ComparisonOperatorEntity(names not contains "张三")
        ComparisonOperatorEntity(list not contains names)
    then
        System.out.println("规则：rule_comparison_notcontains触发了...");
    end

    rule "rule_comparison_memberOf"
    when
        ComparisonOperatorEntity(names memberOf list)
    then
        System.out.println("规则：rule_comparison_memberOf触发了...");
    end

    rule "rule_comparison_not memberOf"
    when
        ComparisonOperatorEntity(names not memberOf list)
    then
        System.out.println("规则：rule_comparison_not memberOf触发了...");
    end
    ```

*   **关键代码片段 (Java 测试类 `DroolsTest.java`)：**

    ```java
    // 获取Kie容器对象
    KieServices kieServices = KieServices.Factory.get();
    KieContainer kieContainer = kieServices.newKieClasspathContainer();

    // 从Kie容器对象中获取会话对象
    KieSession session = kieContainer.newKieSession();

    // 创建事实对象
    ComparisonOperatorEntity fact = new ComparisonOperatorEntity();
    fact.setNames("张三");
    List<String> list = new ArrayList<>();
    list.add("张三");
    list.add("李四");
    fact.setList(list);

    // 插入事实对象
    session.insert(fact);

    // 激活规则，由Drools框架自动进行规则匹配
    session.fireAllRules();
    ```

*   **关键类定义 (`ComparisonOperatorEntity.java`)：**

    ```java
    import java.util.List;

    public class ComparisonOperatorEntity {
        private String names;
        private List<String> list;

        public String getNames() {
            return names;
        }

        public void setNames(String names) {
            this.names = names;
        }

        public List<String> getList() {
            return list;
        }

        public void setList(List<String> list) {
            this.list = list;
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 规则文件编辑 (00:00 - 00:15)**
    *   演示者在 `comparisonOperator.drl` 文件中逐个编写和高亮显示规则。
    *   通过鼠标光标移动和选中，展示了 `contains`、`not contains` 和 `memberOf` 等操作符的语法结构。
    *   每个规则都包含 `when` 条件和 `then` 动作，动作部分是打印日志。

*   **场景 2: 测试类编写与规则触发 (00:15 - 00:35)**
    *   演示者切换到 `DroolsTest.java` 文件。
    *   通过代码高亮和光标移动，演示了如何创建 `KieContainer` 和 `KieSession`。
    *   代码中创建了 `ComparisonOperatorEntity` 实例，并设置了 `names` 和 `list` 属性。
    *   调用 `session.insert(fact)` 将事实对象插入会话，然后调用 `session.fireAllRules()` 触发规则匹配。

*   **场景 3: 控制台输出验证 (00:35 - 01:00)**
    *   演示者运行测试。
    *   控制台输出显示了两条规则的触发信息：
        *   `规则：rule_comparison_notcontains触发了...`
        *   `规则：rule_comparison_memberOf触发了...`
    *   这表明规则引擎成功匹配并执行了定义的规则。

*   **场景 4: 项目结构与依赖管理 (00:00 - 00:05)**
    *   画面展示了项目结构，包括 `src/main/resources` 目录下的 `rules` 文件夹。
    *   项目中包含 `pom.xml` 文件，表明这是一个 Maven 项目，用于管理依赖。
    *   项目依赖了 `drools` 和 `drools-compiler` 等库。

---

以上是根据视频画面内容整理出的结构化报告。
