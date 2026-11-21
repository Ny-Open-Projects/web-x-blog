# 21-规则引擎Drools-Drools基础语法（比较操作 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看啊,D-Rose基础语法。

那么第五个小节呢,讲的是比较操作符。

这些比较操作符呢,主要是用在我们在进行模式匹配的时候会用到。

比如说啊,咱们这个入门案例里边其实已经用到了。

像我们在这儿进行这个匹配的时候,这里边这块呢,这是一个表达式。

前面我们已经提到了,这叫做什么呢?这叫做属性约束,对吧?属性约束。

前面这个order呢,这代表的是类型约束,后面这个是属性约束。

在属性约束这儿呢,咱们是不是使用到了一个小语号?

但是后面还有大于等于,对吧?大于等于,这些。

那么这些呢,都称为叫做比较操作符。

那么我们这个小节呢,就系统的来学习一下,我们D-Rose当中提供的比较操作符都有哪些。

那么咱们在这儿呢,列了这么一个表格,一起来看一下。

第一个呢,是大于,然后呢,还有小于,还有大于等于。

小于等于,还有等于,对吧?注意是两个等号,代表的是等于。

然后呢,这个一个碳号,一个等号,这个就是不等于。

前面这六个呢,我们比较熟悉了。

因为这个前面这六个写法呢,跟咱们在写Java代码当中对应的这些操作符呢,

它的含义还有用法是完全一样的。

所以我们重点呢,来看一下后面这几个,前面这几个我们就不再多看了。

然后呢,我们再往后看呢,就是这个contains。

contains呢。

字面翻译过来叫做包含。

它的含义是什么呢?

是检查我们一个fact对象的某个属性值是否包含一个指定的对象值。

然后呢,这个not contents呢,

not contents它检查的是我们fact对象的某个属性值是否不包含一个指定的对象值。

所以你注意看到,它俩其实是一对,对不对?

一个是包含,一个是不包含。

那么,

那么,

这是咱们这个,

这一对。

包含,

或者不包含。

然后呢,再往后呢,是叫做member of。

member呢,字面翻译过来是不是就是这个成员,对吧?

成员的意思。

它的作用是判断一个fact对象的当中的某个属性值是否在一个或多个集合中。

其实说白了就是,

我们这个fact对象的某个属性值是否是一个集合的什么呢?

成员。

是否在集合当中。

OK。

那么,

那么跟它成对的呢,是not member of。

那是不是就是取反呢?

就是这个属性值是否不在一个或多个集合中。

好,

这是not member of。

然后再往下呢,是matches。

matches呢,

字面翻译过来呢,

是不是叫做匹配。

它的作用呢,是用来判断啊,

我们这个fact对象的属性值是否与我们后边提供的标准的Java的证则表达式进行匹配。

但是后边我们肯定是需要,

编写这个证则表达式,

对吧?

然后跟我们这个属性值来进行匹配。

如果能够匹配成功,

它就会返回处。

好,

那么它的作用呢,

是跟我们提供的证则表达式来进行匹配的。

那么跟它成对的呢,

叫做not matchs。

那是不是就是取反呢?

就是不与,

与这个提供的这个表达式不进行匹配。

好。

前面这几个呢,

就是大于等于等等这几个,

对吧?

跟我们Java当中的这个用法是完全相同的。

所以我们就不再说了。

重点呢,

我们是学习后边,

后边这也是六个啊。

重点,

重点学习的是后边这六个。

好,

那接下来呢,

咱们就来看一下,

我们后边这六个,

这个比较操作符,

它的语法结构应该是什么样子的。

首先呢,

我们先来看啊,

第一对。

注意咱们都是成对的,

因为我们这个,

你看,

是不是有这个contents,

not contents,

member,

not member,

还有match的,

not member,

not match,

所以我们成对来学习。

那么它们两,

两之间呢,

都是取反的,

对吧。

那首先呢,

我们来看contents,

以及这个not contents,

它的语法结构。

什么样的结构呢?

首先呢,

我们在写这个表达式的时候啊,

得有一个类型约束,

这就类似于咱们这个地方,

对吧。

我约束的是other这种类型,

然后后边呢,

是不是进行这个属性约束。

属性约束的时候呢,

我们就可以啊,

使用这个contents。

然后呢,

这个地方呢,

是不是就是我们这个类里边的某个属性,

对吧,

某个属性。

然后呢,

这个属性要包含contents,

包含我们传进来的某个值。

后边呢,

我们肯定要写一个value值,

对吧。

好,

这是它的一个语法结构。

而我们这个field呢,

往往是什么类型的呢?

因为你想啊,

它包含某个值,

那么我们这个field啊,

就是我们这个属性呢,

往往是这种数组类型的,

或者是集合类型的,

用法比较多。

好,

所以这儿,

你看我写了个collection,

还有array,

这是不是代表的是我们这个field的类型。

好,

那么同理啊,

还有一个not contents,

它的语法结构其实是一样的,

只不过在前面加个not就可以了。

好,

然后再往下呢,

是member of,

以及not member of。

它的语法结构呢,

也是这样的,

首先是类型约束,

然后呢,

是我们这类里边的某个字段,

对吧,

某个字段。

这个字段值呢,

member of,

是否是我们给定进来的,

这个值的一个什么成员。

而我们给进来的这个值呢,

这个value呢,

往往是什么呢,

是否是我们的数组或者是集合类型。

说白了就是什么呢,

我们这个集合或者数组里边是否包含这个元素,

包含这个元素。

其实你仔细看的话,

这个contents跟这个member of,

它俩呢,

其实是非常类似的,

只不过是什么呢,

一个描述的是什么呢,

是前面这个值,

是不是包含后边这个值。

而这个member of代表的是什么呢,

是我们后边这个值包含前面这个值。

大家能看明白这个意思吧,

就是我们前面这个值,

是后边这个数组的一个成员。

那是不是意味着就是我们这个数组包含前面这个成员。

大概是这么一个含义啊。

member of呢,

还有一个not member of,

但是语法结构是一样的,

前面加个not就可以了。

再往后呢,

就是matches以及not matches。

那么它的语法结构是这样的,

首先呢还是我们这个类型约束对吧,

然后就是我们这个具体的某个属性。

这个属性呢,

matches是否匹配,

匹配什么呢,

后边我们是不是要传进来一个正则表达式。

如果能匹配上的话,

整个它是不是就会这个表达式就会返回一个true,

否则就会返回false。

但是还有not matches,

前面加一个not就可以了。

这是我们整体来过了一下,

咱们这个比较操作符它的语法结构。

但是这样看的话呢,

还是比较枯燥,

也不太形象对吧。

所以一会呢,

我们就需要来实际搞几个案例啊,

来操作一下,

实际来编写一下这个语法结构。

这样的话,

效果会比较明显。

那么我们这个小节呢,

主要就是来讲一下它这个语法结构到底应该是一个什么样的结构。

然后一会呢,

我们会实际来操作一下。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面内容，进行的结构化中文技术课程摘要。

---

### 1) 视频摘要

本视频课程是关于 **Drools 规则引擎** 的基础语法教学，重点讲解 **比较操作符** 的使用。讲师通过在 IntelliJ IDEA 中编辑 `bookDiscount.drl` 规则文件，演示了如何为不同价格区间的订单设置折扣规则。同时，讲师切换到 PPT 文档，系统地介绍了 Drools 提供的比较操作符，包括标准的 `>`, `<`, `>=`, `<=`, `==`, `!=`，以及特有的 `contains`, `not contains`, `memberOf`, `not memberOf`, `matches`, `not matches` 等操作符，并详细说明了它们的语法结构和用途。课程旨在帮助学习者掌握规则文件中条件判断的编写方法。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：开场，展示 IntelliJ IDEA 中的 `bookDiscount.drl` 规则文件，介绍课程主题——Drools 规则引擎。
*   **00:05 - 00:15**：在代码编辑器中，讲师展示了三个已编写的折扣规则：`book_discount_1`（总价 < 100 元）、`book_discount_2`（总价在 100-200 元之间）、`book_discount_3`（总价在 200-300 元之间）。
*   **00:15 - 00:30**：讲师切换到 PPT，进入“4.5 比较操作符”章节，展示一个包含标准比较符的表格。
*   **00:30 - 00:45**：PPT 展示了“4.5.1 语法”部分，详细列出 `contains`, `not contains`, `memberOf`, `not memberOf`, `matches`, `not matches` 等操作符的定义和用途。
*   **00:45 - 01:00**：PPT 展示了这些操作符的语法结构，包括 `contains | not contains` 和 `memberOf | not memberOf` 的用法。
*   **01:00 - 01:15**：PPT 展示了 `matches | not matches` 的语法结构，用于正则表达式匹配。
*   **01:15 - 01:30**：讲师在 PPT 上滚动，展示“4.5.2 操作步骤”章节，开始讲解如何创建用于测试的实体类。
*   **01:30 - 01:45**：在 PPT 上展示 `ComparisonOperatorEntity` 类的代码，该类包含一个 `String` 类型的 `names` 属性和一个 `List<String>` 类型的 `list` 属性，用于后续测试。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容：

*   **章节标题**：4.5 比较操作符
*   **4.5.1 语法**：
    *   `contains`：检查一个 Fact 对象的某个属性值是否包含一个指定的对象值。
    *   `not contains`：检查一个 Fact 对象的某个属性值是否不包含一个指定的对象值。
    *   `memberOf`：判断一个 Fact 对象的某个属性值是否在一个或多个集合中。
    *   `not memberOf`：判断一个 Fact 对象的某个属性值是否不在一个或多个集合中。
    *   `matches`：判断一个 Fact 对象的属性是否与提供的标准的 Java 正则表达式进行匹配。
    *   `not matches`：判断一个 Fact 对象的属性是否与提供的标准的 Java 正则表达式进行匹配。
*   **4.5.2 操作步骤**：
    *   第一步：创建实体类，用于测试比较操作符。
*   **4.5.1 语法结构**：
    *   `contains | not contains` 语法结构：`Object(Field(Collection/Array) contains value)` 和 `Object(Field(Collection/Array) not contains value)`。
    *   `memberOf | not memberOf` 语法结构：`Object(field memberOf value(Collection/Array))` 和 `Object(field not memberOf value(Collection/Array))`。
    *   `matches | not matches` 语法结构：`Object(field matches "正则表达式")` 和 `Object(field not matches "正则表达式")`。

#### 代码内容：

*   **规则文件 `bookDiscount.drl`**：
    *   **规则 `book_discount_1`**：
        ```drl
        rule "book_discount_1"
        when
            $order:Order(originalPrice < 100)
        then
            $order.setRealPrice($order.getOriginalPrice());
            System.out.println("成功匹配到规则一");
        end
        ```
    *   **规则 `book_discount_2`**：
        ```drl
        rule "book_discount_2"
        when
            $order:Order(originalPrice >= 100 && originalPrice < 200)
        then
            $order.setRealPrice($order.getOriginalPrice() - 20);
            System.out.println("成功匹配到规则二");
        end
        ```
    *   **规则 `book_discount_3`**：
        ```drl
        rule "book_discount_3"
        when
            $order:Order(originalPrice >= 200 && originalPrice < 300)
        then
            $order.setRealPrice($order.getOriginalPrice() - 50);
            System.out.println("成功匹配到规则三");
        end
        ```
    *   **规则 `book_discount_4`**：
        ```drl
        rule "book_discount_4"
        when
            $order:Order(originalPrice >= 300)
        then
            $order.setRealPrice($order.getOriginalPrice() - 100);
            System.out.println("成功匹配到规则四");
        end
        ```

*   **实体类 `ComparisonOperatorEntity`**：
    ```java
    package com.ithema.drools.entity;
    import java.util.List;

    /**
     * 实体类
     * 用于测试比较操作符
     */
    public class ComparisonOperatorEntity {
        private String names;
        private List<String> list;
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：规则文件编辑**：讲师在 IntelliJ IDEA 中打开 `bookDiscount.drl` 文件，逐行展示并讲解了四个折扣规则的编写。规则的 `when` 子句使用了 `>`、`<`、`>=`、`&&` 等比较操作符来定义条件，`then` 子句则执行设置价格和打印日志的操作。
*   **场景二：PPT 讲解比较操作符**：讲师切换到 PPT，首先展示一个包含标准比较符的表格，然后重点讲解了 Drools 特有的六个比较操作符：`contains`, `not contains`, `memberOf`, `not memberOf`, `matches`, `not matches`。通过滚动页面，讲师详细说明了每个操作符的含义和适用场景。
*   **场景三：语法结构演示**：在 PPT 的“4.5.1 语法”部分，讲师通过滚动页面，展示了 `contains | not contains`、`memberOf | not memberOf` 和 `matches | not matches` 三种操作符的语法结构，并用代码片段的形式进行说明。
*   **场景四：创建测试实体类**：讲师在 PPT 上展示“4.5.2 操作步骤”，并开始编写 `ComparisonOperatorEntity` 类的代码，为后续的规则测试做准备。该类包含一个 `String` 类型的 `names` 属性和一个 `List<String>` 类型的 `list` 属性，用于测试 `contains`、`memberOf` 等操作符。
