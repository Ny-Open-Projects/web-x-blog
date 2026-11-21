# 51-规则引擎Drools-Drools高级语法（LHS加强_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来咱们继续来看我们LHS加强

第三个来看的是一个NOT

这个关键字它的用法

那么这个NOT用于判断我们的工作内存中

是否存在某个FAC的对象

需要注意的是什么呢

如果不存在的时候它返回出

如果存在呢返回FALSE

所以大家要注意

因为你看它是NOT相当于整个是取反

所以说如果我们工作内存里面不存在

对象某个对象

那么它才会返回出

比如说咱们先看它的语法吧

语法结构是这样的NOT

然后后边是不是跟的是我们对象的类型

然后是再往里边是我们的属性约束

举个例子来看一下

你看原先我们是这么写的

都是STUDENT的

然后加上这种属性约束

对吧都是这种写法

相当于在我们原先条件的前面

是不是加一个NOT

相当于就取反了

那这个就表示什么呢

是否有STUDENT

工作内存里面是否有STUDENT

这种类型的对象

如果有的话呢

注意如果有它会返回FALSE

如果不存在是不是才会返回出

那么同理这个也是

到工作内存里面去找

有没有STUDENT这种类型的对象

并且AGE是小于10岁的

这种对象如果有还是返回FALSE

没有就返回出

所以整个它是其实是一个取反

这么一个效果

接下来呢我们来演示一下

咱们到这边

创建第一

创建第一

三个还是在当前这个规则文件里边

我们来创建这第四个对吧

第四个规则了

这个演示的是我们的这个NOT

那么怎么玩呢

其实非常简单

咱们呢

直接把这个拿过来

然后呢

把这个呢

我们给它改的简单一点

比如说我就先来一个这样的

看看我们工作内存里面有没有STUDENT这种对象

对吧

然后呢

我这加一个NOT

这是一个关键字

然后呢

看看工作内存里面有没有STUDENT这种对象

如果有的话呢

就会返回FALSE

没有就会返回出

然后呢

我们在控制台呢

输出一下这句话

现在呢

咱们还是来执行啊

这个是

还有就是我们的NOT关键字

大家来看

我们工作内存里面其实是有的

你看我这不是NU了一个STUDENT

然后是不是INSERT了

也就是说工作内存里面是有STUDENT这种对象的

那么既然有了STUDENT

如果有的话呢

那它这个地方是不是就会返回FALSE了

返回FALSE的话

应该是能

是看不到这句输出的啊

咱们先来看一下

你看这还是原先的输出

刚才这个呢并没有输出

那接下来呢

我们怎么做呢

我把这个STUDENT给它去掉

其实你现在不用把它删掉

直接把这句话是不是注释起来就可以

因为你NU这个STUDENT其实跟我们规则引擎

目前没有什么效

没有什么关系

因为什么呢

并没有去INSERT对不对

并没有加到我们工作内存里面去

没有加进去的话呢

那就相当于是没有

没有的话

它这是不是正好匹配上了

好

咱们现在再来执行

看一下我们这个效果

你看哎就它出发了

对不对

这个呢

就是NOT这个关键字它的用法

需要注意的是什么了

它其实是一个取反的这么一个效果

我们需要适应一下

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于 **Drools 规则引擎** 的高级 LHS（左操作数）条件语法教学。讲师通过 IntelliJ IDEA 开发环境，演示了如何使用 `not` 和 `exists` 两个关键条件元素来判断工作内存（Working Memory）中是否存在特定的 Fact 对象。视频内容主要集中在 `not` 元素的用法，通过编写和测试规则来展示其逻辑：`not` 用于判断某个对象**不存在**时返回 `true`，而 `exists` 则用于判断对象**存在**时返回 `true`。讲师还通过代码演示了如何在 Java 测试类中设置全局变量、插入 Fact 对象，并最终触发规则。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，展示的是一个 Markdown 文档，内容为 DRL（Drools Rule Language）的高级语法，当前页面是 `6.4.3 条件元素not`。
*   **00:00:05 - 00:00:15**：讲师切换到 IntelliJ IDEA，展示了一个名为 `DroolsTest.java` 的 Java 测试类，其中包含了设置全局变量和创建 `KieSession` 的代码。
*   **00:00:15 - 00:00:30**：讲师在 `DroolsTest.java` 中编写了 `test120` 方法，并在其中设置了全局变量 `count` 和 `gList`，并创建了一个 `Student` 对象 `s1`。
*   **00:00:30 - 00:00:45**：讲师切换到 `lhs.drl` 文件，开始编写规则。首先编写了一个名为 `rule_lhs_2` 的规则，使用 `not` 关键字来判断 `Student` 对象的 `name` 属性是否不在一个指定的字符串列表中。
*   **00:00:45 - 00:01:00**：讲师接着编写了 `rule_lhs_3`，使用 `eval` 关键字来判断一个布尔表达式 `1==2` 的值。
*   **00:01:00 - 00:01:15**：讲师编写了 `rule_lhs_4`，使用 `not` 关键字来判断 `Student` 对象是否不存在。
*   **00:01:15 - 00:01:30**：讲师在 `DroolsTest.java` 中调用 `session.fireAllRules(...)` 方法来激活并执行规则。
*   **00:01:30 - 00:01:45**：讲师在 `DroolsTest.java` 中调用 `session.dispose()` 方法来关闭会话。
*   **00:01:45 - 00:02:00**：讲师切换回 Markdown 文档，展示了 `6.4.4 条件元素exists` 的语法结构和示例。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **6.4.3 条件元素not**：
        *   功能描述：`not` 用于判断 Working Memory 中是否存在某个 Fact 对象，如果不存在则返回 `true`，如果存在则返回 `false`。
        *   语法结构：`not Object(可选属性约束)`
        *   示例：`not Student()`，`not Student(age < 10)`
    *   **6.4.4 条件元素exists**：
        *   功能描述：`exists` 的作用与 `not` 相反，用于判断 Working Memory 中是否存在某个 Fact 对象，如果存在则返回 `true`，不存在则返回 `false`。
        *   语法结构：`exists Object(可选属性约束)`
        *   示例：`exists Student()`，`exists Student(age < 10 && name != null)`

*   **代码关键内容**：
    *   **Java 测试类 `DroolsTest.java`**：
        ```java
        // 设置日期格式
        System.setProperty("drools.dateformat", "yyyy-MM-dd HH:mm");
        // 获取Kie容器对象
        KieServices kieServices = KieServices.Factory.get();
        KieContainer kieContainer = kieServices.newKieClasspathContainer();
        KieSession session = kieContainer.newKieSession();

        // 设置全局变量
        session.setGlobal("count", 5);
        List<String> list = new ArrayList<String>();
        list.add("itheima");
        session.setGlobal("gList", list);

        // 创建并插入Fact对象
        Student s1 = new Student();
        s1.setName("test");
        session.insert(s1);

        // 激活规则
        session.fireAllRules(new RuleNameStartsWithAgendaFilter("rule_lhs"));

        // 关闭会话
        session.dispose();
        ```
    *   **DRL 规则文件 `lhs.drl`**：
        ```drl
        // 编写规则，演示not关键字用法
        rule "rule_lhs_2"
        when
            $s:Student(name not in ("张三","李四","王五"))
        then
            System.out.println("规则：rule_lhs_2触发了...");
        end

        // 编写规则，演示eval关键字用法
        rule "rule_lhs_3"
        when
            eval(1==2)
        then
            System.out.println("规则：rule_lhs_3触发了...");
        end

        // 编写规则，演示not关键字用法
        rule "rule_lhs_4"
        when
            not Student()
        then
            System.out.println("规则：rule_lhs_4触发了...");
        end
        ```

---

### 4) 关键场景与演示描述

*   **场景一：讲解 `not` 元素** (00:00:30 - 00:00:45)
    *   讲师在 `lhs.drl` 文件中编写了一个名为 `rule_lhs_2` 的规则。
    *   该规则的条件部分使用了 `not` 关键字，判断 `Student` 对象的 `name` 属性是否不在一个指定的字符串列表中。
    *   讲师解释了 `not` 的逻辑：当条件不满足时，规则才会触发。

*   **场景二：演示 `eval` 关键字** (00:00:45 - 00:01:00)
    *   讲师编写了 `rule_lhs_3`，其条件部分使用了 `eval` 关键字来判断一个布尔表达式 `1==2`。
    *   由于 `1==2` 为 `false`，所以该规则不会触发。
    *   讲师解释了 `eval` 的作用：它允许在规则的 LHS 中直接评估一个表达式。

*   **场景三：演示 `not` 关键字的另一种用法** (00:01:00 - 00:01:15)
    *   讲师编写了 `rule_lhs_4`，其条件部分使用了 `not Student()`。
    *   这个规则的含义是：当工作内存中不存在任何 `Student` 对象时，规则会触发。
    *   讲师解释了 `not` 关键字的通用性：它可以用于判断任何类型的对象是否存在。

*   **场景四：执行规则并观察结果** (00:01:15 - 00:01:30)
    *   讲师在 `DroolsTest.java` 中调用 `session.fireAllRules(...)` 方法。
    *   该方法会激活并执行所有匹配的规则。
    *   讲师观察到控制台输出了 `规则：rule_lhs_2触发了...`，说明 `rule_lhs_2` 成功触发。
    *   讲师解释了规则触发的条件和结果。

*   **场景五：讲解 `exists` 元素** (00:01:45 - 00:02:00)
    *   讲师切换回 Markdown 文档，展示了 `6.4.4 条件元素exists` 的语法结构和示例。
    *   讲师解释了 `exists` 的作用：它与 `not` 相反，用于判断某个对象是否存在。
    *   讲师强调了 `exists` 的重要性：它在某些场景下比 `not` 更加灵活和高效。

---
