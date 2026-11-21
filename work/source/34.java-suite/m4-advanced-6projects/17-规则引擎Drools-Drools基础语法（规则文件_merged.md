# 17-规则引擎Drools-Drools基础语法（规则文件 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来我们一起来看一下D-Rose的基础语法

那么基础语法里面第一个小节是规则文件的构成

我们在使用D-Rose时非常重要的一个工作就是编写规则文件

通常我们编写的规则文件后缀是这种DRL的

前面在我们入门案例里面咱们已经写过一个规则文件了

那这个DRL它其实是一个缩写

是什么呢?是D-Rose Ruler Language的缩写

翻译过来就是D-Rose规则语言,这么一个缩写

那么在规则文件中编写具体的规则的内容

一套完整的规则文件,它的内容是由下面这些关键字来构成的

第一个是package,它是不是定义包名

但是我们前面也强调了它是相当于是一个逻辑上的管理

同一个包名下的查询或者是函数是可以直接调用的

比如说咱们编写了D-Rose的规则文件

我们编写的这个规则文件,那么我们第一行就是package

然后后边这个呢,其实它只是一个逻辑上的一个概念

它并不一定跟我们当前这个规则文件实际所在的那个目录呢

并不是必须要对应的

它不像咱们编写的lay,lay的话你这是不是也一个package

而这上面这个,它是跟我们具体这个lay它的包是必须要完全对应的

而这个呢只是一个逻辑的概念

好,这个是package

这个规则文件的规则文件的规定只限于逻辑上的管理

好,那么对于一个规则文件的话呢必须要有一个package

好,然后呢还有import

import是用来导入lay或者静态方法的

比如说咱们这个地方就用到了import对吧

咱们在这是不是导入了一个order这个lay

因为在我们规则文件里面可能会用到这些lay

所以说呢就需要给它导入

那么这个呢是跟咱们在lay里面来引入

类似的啊

这个是import

还有global

global呢我们后边会讲到

它也是我们规则文件里面的一个关键字

它的作用是用来定义什么呢

全局变量

咱们在这里面呢你可以在这提示一下

你看,global

你看,它是能够提示出来的

那么这是它的这个global关键字

用来定义全局变量的

还有function

function呢是用来定义函数的

咱们在那都可以敲一下

你看function对吧

这个呢是用来定义函数的这么一个关键字

还有query

query呢是用来定义查询的

然后我在这来定义一个query

那么可以看到它都会变颜色对吧

那么这个是定义查询的关键字

然后呢还有一个是我们的规则体

这个呢是我们整个规则文件里边最重要的一部分

就是ruler end

这个呢称为规则体

那么我们可以看一下

咱们在这是不是定义了一个规则

你看它是以ruler开始

以end结尾

这就表示这一块呢是一个规则

然后呢下边是不是又一个ruler

一个end

这代表的是不是第二个规则

那么整个我选中的这一部分呢

就称为规则体

它是我们这个规则文件里面最重要的一部分内容

叫做ruler end

那么D-Rose支持的这个规则文件形式

其实除了这个规则文件形式之外呢

除了咱们这种D-R-L这种形式的规则文件之外呢

还有这种Excel文件形式的

那么只不过我们课上呢

大部分时间用的都是这种D-R-L的

因为这种用的是比较多的

那么我们这个小节呢

主要就讲了一下

我们作为一个规则文件对吧

都会有哪些构成部分

那么这些呢

我们可以看到

这一列全都是列出来的是关键字

通过关键字呢来定义相关的一些信息

这是规则文件的构成

那么我们可以看到

在这个J- request 里面

我们可以看到

我们可以看到

沿着这个J- request

这样一个J- request

这个J- request

要有一个个J- request

来定义则要在这3C-E-R-U-R-I-S 里面

那么这个J- request

就是关键字的一个G- request

我们按这个G- request

我们来看看

它再按一次

看看这个G- request

就是这个G- request

那这G- request

就是这个G- request

不过我们可以看到

这个G- request

这个G- request

这都是我们的基建

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于 **Drools 规则引擎** 的入门教程，主要讲解 **Drools 规则文件（.drl）的基础语法**。讲师通过在 IntelliJ IDEA 中演示，逐步介绍了规则文件的构成要素，包括 `package`、`import`、`rule`、`when` 和 `then` 等核心结构。视频通过一个“图书折扣”的简单业务场景，演示了如何编写规则来根据订单金额自动计算优惠后的价格。讲师还展示了如何在规则文件中使用 `global` 关键字来定义全局变量，并通过注释解释了规则的执行逻辑。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，讲师在 Typora 文档中展示课程大纲，定位到“4.1 规则文件构成”章节。
*   **00:00:05 - 00:00:15**：讲师切换到 IntelliJ IDEA，展示一个名为 `Order.java` 的 Java 类，该类定义了订单实体，包含 `originalPrice`（原价）和 `realPrice`（实付价格）两个属性。
*   **00:00:15 - 00:00:30**：讲师在 IDEA 中打开并编辑 `bookDiscount.drl` 规则文件，开始编写第一个规则 `book_discount_1`，用于处理总价低于 100 元的订单。
*   **00:00:30 - 00:00:45**：讲师编写第二个规则 `book_discount_2`，用于处理总价在 100 到 200 元之间的订单。
*   **00:00:45 - 00:00:55**：讲师在规则文件中添加了 `global` 关键字，并演示了如何定义一个全局变量。
*   **00:00:55 - 00:01:05**：讲师在规则文件中添加了 `rule end` 关键字，用于结束规则体。
*   **00:01:05 - 00:01:15**：讲师在规则文件中添加了第三个规则 `book_discount_3`，用于处理总价在 200 到 300 元之间的订单。
*   **00:01:15 - 00:01:25**：讲师切换回 Typora 文档，展示“4.2 规则体语法结构”章节，准备讲解规则体的详细语法。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节标题**：`4.1 规则文件构成` 和 `4.2 规则体语法结构`。
    *   **规则文件构成表**：
        | 关键字 | 描述 |
        | :--- | :--- |
        | `package` | 包名，只限于逻辑的管理，同一个包名下的查询或者函数可以直接调用 |
        | `import` | 用于导入类或者静态方法 |
        | `global` | 全局变量 |
        | `function` | 自定义函数 |
        | `query` | 查询 |
        | `rule end` | 规则体 |
    *   **规则体语法结构**：规则体是规则文件内容的重要组成部分，用于进行业务规则判断和处理业务结果。
*   **代码示例**：
    *   **Java 实体类 `Order.java`**：
        ```java
        package com.itheima.drools.entity;

        public class Order {
            private Double originalPrice; // 订单原始价格，即优惠前价格
            private Double realPrice;     // 订单真实价格，即优惠后价格

            public String toString() {
                return "Order{" +
                        "originalPrice=" + originalPrice +
                        ", realPrice=" + realPrice +
                        '}';
            }

            public Double getOriginalPrice() {
                return originalPrice;
            }
        }
        ```
    *   **Drools 规则文件 `bookDiscount.drl`**：
        ```drl
        package book.discount
        import com.itheima.drools.entity.Order

        // 所购图书总价在100元以下的没有优惠
        rule "book_discount_1"
        when
            $order:Order(originalPrice < 100) // 模式匹配，到规则引擎中（工作内存）查找Order对象
        then
            $order.setRealPrice($order.getOriginalPrice());
            System.out.println("成功匹配到规则一");
        end

        // 所购图书总价在100到200元的优惠20元
        rule "book_discount_2"
        when
            $order:Order(originalPrice >= 100 && originalPrice < 200) // 模式匹配，到规则引擎中（工作内存）查找Order对象
        then
            $order.setRealPrice($order.getOriginalPrice() - 20);
            System.out.println("成功匹配到规则二");
        end

        // 所购图书总价在200到300元的优惠50元
        rule "book_discount_3"
        when
            $order:Order(originalPrice >= 200 && originalPrice < 300) // 模式匹配，到规则引擎中（工作内存）查找Order对象
        then
            $order.setRealPrice($order.getOriginalPrice() - 50);
            System.out.println("成功匹配到规则三");
        end
        ```

---

### 4) 关键场景与演示描述

*   **场景一：规则文件构成介绍**（00:00:00 - 00:00:15）
    *   讲师首先在 Typora 文档中展示了课程大纲，明确当前讲解的是“4.1 规则文件构成”。
    *   接着，讲师切换到 IntelliJ IDEA，展示了一个 `Order.java` 类，用于定义订单实体，为后续规则提供数据模型。
*   **场景二：编写第一个规则**（00:00:15 - 00:00:30）
    *   讲师在 IDEA 中打开 `bookDiscount.drl` 文件，开始编写第一个规则 `book_discount_1`。
    *   讲师在 `when` 子句中使用了 `Order(originalPrice < 100)` 来定义匹配条件，即当订单原价低于 100 元时触发。
    *   在 `then` 子句中，讲师编写了设置实付价格和打印日志的代码。
*   **场景三：编写第二个规则**（00:00:30 - 00:00:45）
    *   讲师在第一个规则下方，编写了第二个规则 `book_discount_2`。
    *   该规则的 `when` 子句条件为 `originalPrice >= 100 && originalPrice < 200`，用于处理 100-200 元区间的订单。
    *   `then` 子句中，讲师编写了减去 20 元的逻辑。
*   **场景四：演示 `global` 关键字**（00:00:45 - 00:00:55）
    *   讲师在规则文件中添加了 `global` 关键字，并演示了如何定义一个全局变量，用于在规则中共享数据。
*   **场景五：演示 `rule end` 关键字**（00:00:55 - 00:01:05）
    *   讲师在第一个规则的 `then` 子句后，添加了 `end` 关键字，用于结束规则体。
*   **场景六：演示第三个规则**（00:01:05 - 00:01:15）
    *   讲师在第二个规则下方，编写了第三个规则 `book_discount_3`。
    *   该规则的 `when` 子句条件为 `originalPrice >= 200 && originalPrice < 300`，用于处理 200-300 元区间的订单。
    *   `then` 子句中，讲师编写了减去 50 元的逻辑。
*   **场景七：切换到规则体语法结构**（00:01:15 - 00:01:25）
    *   讲师切换回 Typora 文档，展示“4.2 规则体语法结构”章节，为后续讲解规则体的详细语法做准备。
