# 37-drools基础语法（规则文件构成） — 课程文稿（声音线+画面线 合并稿）

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

这个逻辑的概念只限于逻辑上的管理

那么对于一个规则文件的话呢,必须要有一个package

然后呢还有import

import是用来导入lay或者静态方法的

比如说咱们这个地方就用到了import

咱们在这是不是导入了一个order这个lay

因为在我们规则文件里面可能会用到这些lay

所以说呢就需要给它导入

那么这个呢是跟咱们在lay里面来引入

其他的lay呢是类似的

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

function对吧

这个呢是用来定义函数的这么一个关键字

还有query

query呢是用来定义查询的

比方说我在这来定义一个query

那么可以看到它都会变颜色对吧

那么这个是定义查询的关键字

然后呢还有一个是我们的规则体

这个呢是我们整个规则文件里边最重要的一部分

就是ruler end

这个呢称为规则体

那么我们可以看到这个规则体呢

看一下

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

那么Diros支持的这个规则文件形式

其实除了咱们这种DRR

这种形式的规则文件之外呢

还有这种Excel文件形式的

那么只不过我们课上呢

大部分时间用的都是这种DRR的

因为这种用的是比较多的

那么我们这个小节呢

主要就讲了一下

我们作为一个规则文件对吧

都会有哪些构成部分

那么这些呢

我们可以看到

这一列全都是列出来的是关键字

通过关键字呢

来定义相关的一些信息

这是规则文件的构成

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于 **Drools 规则引擎** 的入门教程，主要讲解 **Drools 规则文件（.drl）的基础语法**。讲师通过演示一个简单的图书折扣业务场景，逐步介绍规则文件的构成要素，包括 `package`、`import`、`rule`、`when`、`then` 等核心结构。视频通过 IntelliJ IDEA 编辑器展示代码，并结合 PPT 文档进行讲解，旨在帮助学习者理解如何编写和组织 Drools 规则。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节划分基于画面内容和逻辑顺序进行推断：

*   **00:00 - 00:05**: **课程引入与PPT概览**
    *   展示课程PPT的目录结构，定位到“4. Drools基础语法”章节。
    *   重点介绍“4.1 规则文件构成”部分，强调编写 `.drl` 文件的重要性。

*   **00:05 - 00:15**: **规则文件构成详解**
    *   讲解 `.drl` 文件是 Drools Rule Language 的缩写。
    *   通过PPT表格展示规则文件的关键字及其功能：
        *   `package`: 用于逻辑分组，同包下的查询或函数可直接调用。
        *   `import`: 用于导入类或静态方法。
        *   `global`: 定义全局变量。
        *   `function`: 定义自定义函数。
        *   `query`: 定义查询。
        *   `rule end`: 规则体的结束标记。
    *   说明 Drools 支持的规则文件类型，除了 `.drl` 还有 Excel 文件。

*   **00:15 - 00:30**: **规则体语法结构**
    *   进入“4.2 规则体语法结构”章节。
    *   解释规则体是规则文件的核心，用于进行业务规则判断和处理。
    *   展示一个完整的规则示例，包含 `rule`、`when` 和 `then` 三个部分。

*   **00:30 - 00:45**: **代码演示与场景构建**
    *   在 IntelliJ IDEA 中打开 `bookDiscount.drl` 文件。
    *   展示 `Order` 实体类的代码，定义了 `originalPrice`（原价）和 `realPrice`（实付价格）两个属性。
    *   在规则文件中编写第一个规则 `book_discount_1`，用于处理总价低于 100 元的订单，不提供优惠。
    *   编写第二个规则 `book_discount_2`，用于处理总价在 100 到 200 元之间的订单，提供 20 元优惠。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容**：
    *   **章节标题**：`4. Drools基础语法`，`4.1 规则文件构成`，`4.2 规则体语法结构`。
    *   **规则文件构成表格**：
        | 关键字 | 描述 |
        | :--- | :--- |
        | package | 包名，只限于逻辑的管理，同一个包名下的查询或者函数可以直接调用 |
        | import | 用于导入类或者静态方法 |
        | global | 全局变量 |
        | function | 自定义函数 |
        | query | 查询 |
        | rule end | 规则体 |
    *   **规则体语法结构说明**：规则体是规则文件的重要组成部分，用于进行业务规则判断和处理业务结果。
    *   **规则文件类型**：除了 `.drl` 文件，Drools 还支持 Excel 文件类型的规则。

*   **代码关键内容**：

    **实体类 `Order.java`**：
    ```java
    package com.ithema.drools.entity;
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

    **规则文件 `bookDiscount.drl`**：
    ```drl
    package book.discount
    import com.ithema.drools.entity.Order

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
    ```

---

### 4) 关键场景与演示描述

*   **场景一：环境与文件结构展示**
    *   讲师首先在 IntelliJ IDEA 中打开项目，展示 `bookDiscount.drl` 文件和 `Order.java` 实体类，为后续规则编写做准备。

*   **场景二：规则文件语法讲解**
    *   讲师切换到 PPT，通过表格详细讲解 `.drl` 文件中每个关键字的作用，如 `package` 用于逻辑分组，`import` 用于导入实体类，`rule end` 用于标记规则体结束。

*   **场景三：规则体结构演示**
    *   讲师在 PPT 中介绍规则体的结构，强调 `when` 子句用于定义条件模式，`then` 子句用于定义规则触发后的操作。

*   **场景四：实际规则编写**
    *   讲师在 `bookDiscount.drl` 文件中编写第一个规则 `book_discount_1`，其 `when` 条件为 `originalPrice < 100`，`then` 操作为设置 `realPrice` 为 `originalPrice`。
    *   随后，讲师编写第二个规则 `book_discount_2`，其 `when` 条件为 `originalPrice >= 100 && originalPrice < 200`，`then` 操作为将 `realPrice` 设置为 `originalPrice - 20`。
    *   通过注释清晰地说明了每个规则的业务含义，使学习者能够将代码与业务逻辑对应起来。

*   **场景五：代码高亮与交互**
    *   在演示过程中，讲师使用鼠标高亮选中代码行，如 `rule "book_discount_1"` 和 `when` 子句，以引导观众关注关键部分。
    *   通过在 `end` 关键字处进行光标停留，强调规则体的结束。

---

以上是根据视频画面内容进行的结构化分析，旨在帮助理解 Drools 规则引擎的基础语法和实际应用。
