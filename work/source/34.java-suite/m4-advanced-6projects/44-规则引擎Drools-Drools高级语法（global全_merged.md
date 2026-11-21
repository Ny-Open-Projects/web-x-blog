# 44-规则引擎Drools-Drools高级语法（global全 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,继续来看我们的Global全局变量

刚才咱们是演示了第一种效果

就是我定义的全局变量

它的类型是包装类型

比如说我定义integer类型

这种类型的时候

它的特点就是我们对全局变量值的改变

只针对当前规则生效

对其他规则是没有影响的

接下来咱们来看

如果我定义的全局变量

它是一个集合类型的时候

会是一个什么样的效果

咱们首先在这来加入一个全局变量

叫Global

使用它这个关键字

然后来指定我们这个类型

比如说我在这来一个java.youtube.list

list的这种类型

然后我们在这来指定一个glist

指的就是Global list

这个就是我们定义的

这么一个集合类型

定义一个集合类型的全局变量

把它定义好

定义好之后

咱们这样

我们首先还是在第一个规则里边

是不是来改变一下这个jlist的

然后在第二个规则里边

我们来输出一下

看看我们在第一个规则改变这个全局变量之后

第二个规则能不能生效

就是能不能看到是改变之后的效果

可以吧

那么怎么玩呢

咱们可以这样

我们在这儿来使用这个jlist的全局变量

第二什么呢

add

是不是就是像这个集合里边来添加一个元素

来添加一个元素

那么这个元素随便

我们就来一个

比方说就叫itcast

添加一个元素

然后我们可以在这儿来先来输出一下

咱们这样按照顺序

其实本质上你在哪儿

这个顺序其实无所谓

我只是想先让他输出这一句话

然后再输出这句话

然后我们再来改变这个

给它分清晰一点

这些都执行完之后

我们再来执行这句话

这相当于我对什么呢

我们来修改了是这种集合类型的全局变量

给它添加了一个元素

然后添加完元素之后

咱们来输出这个元素去

我们再来输出一下

就是什么呢

我们这个全局变量

这个叫glist的size

咱们就看它这里边有几个元素就行了

有几个元素

我们来看一下glist.size

它里边元素的个数

是这样的

然后我们把这句话直接Ctrl C拿过来

放在这个位置

咱们来看一下

全局变量glist在我们第二个规则里边

它的size是多少

这样的话

我这个规则文件其实就已经写好了

接下来我们需要把刚才这个单元测试也简单修改一下

怎么修改呢

你注意看

我现在是不是又定义了一个glist的这么一个全局变量

这样的话

我是不是需要在我们的扎挖程序里边

也调用setglobal

把它这个全局变量初始值给它传进来

如果你不传的话

它是不是又要报错了

也就是说我们在这个规则文件里面定义了全局变量

你看它是不是总是报这个空指针呢

因为它拿不到这个全局变量的初始值

所以说我们需要在这个地方给它来设置进来

在这儿来设置全局变量

session.setglobal

还记得吧

这个全局变量的这个名字

必须跟这个地方定义的这个名字保持一致

所以我们给它考考看

我们可以把这个全局变量的这个初始值给它传进去

然后呢

它的这个初始值是个什么值呢

你看它是不是一个list的类型

那我们可以直接给它new一个arraylist

是不是给它传进去

咱们可以这样

我们在这儿来定义一下

比如说我在这儿来定义一个list

这个范形可以给加一个

加不加其实都可以

list等于什么呢

new一个arraylist

然后呢

我可以给它一个初始值

但是这个你可以不添加都没有关系

你直接new出来直接给进去也可以

我给它一个初始值

比方说叫做it黑码

然后呢我们把这个list给它传进去

ok

这个呢是不是我又设置了一个全局变量

它是这种

list的类型的

然后它的名字呢必须叫glist

跟我们刚才定义的那个规则里面

这个保持一致

好

这弄好之后呢

咱们呢同样在我们的Java程序里边啊

注意看

在这个位置

我们来看一下

也就是说在Java程序中

这个全局变量

glist的size

为多少

多少呢

注意看我这是不是有个

我定一个list啊

给那个规则文件传进去了

那现在呢

我在这个地方我来输出一下

大家可以看到我在Java程序里边

是不是只是add了一个

然后呢我们来看这个地方它size

这个位置呢

到底是多少

好

来执行一下我们这个单元测试

好

已经执行成功了对吧

执行成功之后呢

大家可以来看一下

第一个规则是不是先触发了

这些我们都说过了

然后呢全局变量它的size是不是2

这句是从哪来的呢

是不是就是来自于我们第一个规则

最后这一句话

原先我们给进去的初始值是不是

它的size是1

因为加进了个itk码对吧

然后我在这个地方加进了itcast的

所以它的size等于1

应该是没啥问题

然后接下来我们第二个规则是不是触发

第二个规则触发的时候呢

直接打印它的size等于2

那看来我们在第一个规则里边

对这个全局变量的修改

是不是已经影响到第二个规则了

同样的在我们Java程序中

全局变量它的size是不是也是2啊

也是2

那就说明什么呢

我们对于这种集合类型的全局变量

它是比较特殊的

就是什么呢

一旦你对这个全局变量进行了修改

它在任何地方

任何地方指的就是什么呢

就是指的是其他的规则

或者是我们的Java程序

都会受到影响

都会受到影响

咱们可以通过加一个断点这种方式

其实看得更加清晰一点

咱们在这儿这个地方加一个断点

来看我们debug来调试一下

这种看得会更清晰一些

因为我们刚才只是打印了一个size对不对

好

现在你注意看啊

现在我们让程序呢

往下执行一步

执行一步

现在这个size呢

它等于0

因为只是刚new出来这个对象对吧

里边还没有东西

然后呢我们再往下走一步

是不是add了一个

这个时候呢它的size是不是等于1了

我们可以看到这里边

是不是有一个itk码

然后接下来呢我们程序继续往下执行

走

然后呢要执行我们的规则了

走

好现在规则是不是已经执行完

执行完之后呢咱们回过头来再来看一下我们

这个

list

你看它的size是不是已经变成了2

里边是不是加进来了

一个这个itcast

这通过我们这种调试的方式

我们可以看到

这个效果

看的会更加清晰一点

这个呢我们演示的是什么呢

对象类型是这种集合类型的时候

它这种特点

它的特点是什么呢我们再来强调一下

就是在我们这个规则文件里面进行的修改

它会影响到其他的规则以及我们的Java程序

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析：

---

### 1) 视频摘要

本视频片段是关于 **Drools 规则引擎** 的技术教学内容，主要讲解 **全局变量（global）** 的概念、语法及其在规则文件中的作用。讲师通过 IntelliJ IDEA 开发环境，演示了如何在规则文件（`.drl`）中定义全局变量（如 `java.lang.Integer` 和 `java.util.List`），并编写了两个规则 `rule_global_1` 和 `rule_global_2` 来分别修改和读取这些变量。随后，讲师通过 Java 测试代码 `DroolsTest.java`，演示了如何在程序中设置全局变量，并通过 `session.fireAllRules()` 触发规则执行。视频重点在于对比和验证：**当全局变量是包装类型（如 Integer）时，其修改仅对当前规则有效；而当全局变量是集合类型（如 List）时，其修改对所有规则都有效**。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，讲师在 DRL 文件中展示本章节标题“6.1 global全局变量”，并简要介绍 `global` 关键字用于定义全局变量。
*   **00:00:05 - 00:00:15**：讲师在 DRL 文件中展示 `global` 关键字的语法结构：`global 对象类型 对象名称`。
*   **00:00:15 - 00:00:30**：讲师在 DRL 文件中展示 `global java.lang.Integer count` 和 `global java.util.List glist` 的定义，并解释了两种类型变量的修改范围。
*   **00:00:30 - 00:00:45**：讲师在 DRL 文件中编写规则 `rule_global_1`，其中包含 `count += 10;` 和 `System.out.println(...)` 语句。
*   **00:00:45 - 00:01:00**：讲师在 DRL 文件中编写规则 `rule_global_2`，其中包含 `System.out.println(...)` 语句。
*   **00:01:00 - 00:01:15**：讲师在 DRL 文件中添加 `glist.add("itcast");` 语句，并在下方添加 `System.out.println("全局变量glist的size: " + glist.size());` 语句。
*   **00:01:15 - 00:01:30**：讲师切换到 Java 测试文件 `DroolsTest.java`，并开始编写测试代码。
*   **00:01:30 - 00:01:45**：讲师在 `DroolsTest.java` 中编写 `session.setGlobal(identifier: "count", value: 5);` 语句。
*   **00:01:45 - 00:02:00**：讲师在 `DroolsTest.java` 中编写 `List<String> list = new ArrayList<String>(); list.add("itheima");` 语句。
*   **00:02:00 - 00:02:15**：讲师在 `DroolsTest.java` 中编写 `session.setGlobal(identifier: "gList", list);` 语句。
*   **00:02:15 - 00:02:30**：讲师在 `DroolsTest.java` 中编写 `session.fireAllRules();` 语句。
*   **00:02:30 - 00:02:45**：讲师在 `DroolsTest.java` 中编写 `System.out.println("在Java程序中全局变量gList的size为: " + list.size());` 语句。
*   **00:02:45 - 00:03:00**：讲师运行测试代码，查看控制台输出结果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   本章节标题：“6.1 global全局变量”。
    *   `global` 关键字的语法结构：`global 对象类型 对象名称`。
    *   使用 `global` 定义的全局变量时的注意事项：
        1.  如果对象类型为包装类型时，在一个规则中改变了 `global` 的值，那么只针对当前规则有效，对其他规则中的 `global` 不会有影响。
        2.  如果对象类型为集合类型或 JavaBean 时，在一个规则中改变了 `global` 的值，对 Java 代码和所有规则都有效。

*   **代码内容**：
    *   **DRL 文件 (`global.drl`)：**
        ```drl
        // 当前规则文件用于测试global全局变量
        global java.lang.Integer count // 定义一个包装类型的全局变量
        global java.util.List glist // 定义一个集合类型的全局变量

        rule "rule_global_1"
        when
        then
            count += 10; // 对于包装类型的全局变量的修改只针对当前规则生效
            System.out.println("规则: rule_global_1触发了...");
            System.out.println("全局变量count计算之后的值为: " + count);
        end

        rule "rule_global_2"
        when
        then
            System.out.println("规则: rule_global_2触发了...");
            System.out.println("全局变量的值为: " + count);
        end
        ```

    *   **Java 测试文件 (`DroolsTest.java`)：**
        ```java
        // 设置日期格式
        System.setProperty("drools.dateformat", "yyyy-MM-dd HH:mm");

        // 获得Kie容器对象
        KieServices kieServices = KieServices.Factory.get();
        KieContainer kieContainer = kieServices.newKieClasspathContainer();
        KieSession session = kieContainer.newKieSession();

        // 设置全局变量，变量名称必须和规则文件中定义的变量名一致
        session.setGlobal("count", 5);

        List<String> list = new ArrayList<String>();
        list.add("itheima");

        session.setGlobal("gList", list);

        // 激活规则，由Drools框架自动进行规则匹配，如果规则匹配成功，则执行当前规则
        session.fireAllRules();

        // 在Java程序中全局变量gList的size为: 1
        System.out.println("在Java程序中全局变量gList的size为: " + list.size());

        // 关闭会话
        session.dispose();
        ```

---

### 4) 关键场景与演示描述

*   **场景一：定义全局变量并编写规则**
    *   讲师在 DRL 文件中定义了两个全局变量：`count`（`java.lang.Integer` 类型）和 `glist`（`java.util.List` 类型）。
    *   讲师编写了两个规则 `rule_global_1` 和 `rule_global_2`。
    *   在 `rule_global_1` 中，讲师修改了 `count` 的值并打印了结果。
    *   在 `rule_global_2` 中，讲师打印了 `count` 的值。

*   **场景二：演示包装类型全局变量的修改范围**
    *   讲师在 `rule_global_1` 中修改了 `count` 的值。
    *   讲师在 `rule_global_2` 中打印了 `count` 的值。
    *   讲师通过控制台输出结果，验证了 `count` 的修改只对当前规则有效。

*   **场景三：演示集合类型全局变量的修改范围**
    *   讲师在 `rule_global_1` 中向 `glist` 添加了一个元素。
    *   讲师在 `rule_global_2` 中打印了 `glist` 的大小。
    *   讲师通过控制台输出结果，验证了 `glist` 的修改对所有规则都有效。

*   **场景四：Java 程序中设置和读取全局变量**
    *   讲师在 Java 测试文件中，通过 `session.setGlobal()` 方法设置全局变量 `count` 和 `gList`。
    *   讲师通过 `session.fireAllRules()` 方法触发规则执行。
    *   讲师通过 `System.out.println()` 方法打印了 `gList` 的大小。
    *   讲师通过控制台输出结果，验证了 Java 程序中对全局变量的修改和读取。

---

以上是根据视频画面进行的结构化技术分析。
