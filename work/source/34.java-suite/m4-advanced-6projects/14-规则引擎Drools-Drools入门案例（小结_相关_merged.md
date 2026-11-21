# 14-规则引擎Drools-Drools入门案例（小结_相关 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来我们来看一下相关概念说明

刚才我们在规则引擎构成当中

其实有一些概念已经提到过了

但是因为这些概念是非常重要的

所以说我们在这有必要再来重复一遍

让大家加深印象

因为我们后边在应用当中经常会用到这些东西

首先第一个叫做Working Memory

我们已经强调过了

这个叫做工作内存

那么D-Rose规则引擎

它会从我们Working Memory工作内存中来获取数据

并和我们规则文件中定义的这些规则

是不是来进行模式匹配

所以说我们在开发的应用

只需要将我们的数据插入到工作内存中就可以了

比如说咱们入门案例里边

咱们是不是通过调用了一个KIE Session的insert方法

把order对象是不是插入到了工作内存里面去了

这是第一个概念

我们需要把我们的数据插入到工作内存里面

去规则引擎它在运行的时候

它会自动的到工作内存里面来取这些对象

而这些对象叫什么

我们统一的称为叫做Fact

字面翻译过来就是事实

事实对象

它是指在我们D-Rose规则应用过程当中

将一个普通的Jarbin插入到工作内存后的对象

就是Fact的对象

例如咱们案例当中的order对象

因为它插入到了工作内存里面去了

所以说我们就把它称为Fact的对象

所以我们要注意

只有插入到工作内存里面的这一类的对象

才称为Fact的对象

如果说你只是普通new了一个

简单new了一个order对象

并没有插入到工作内存里面去

那它是不能称为Fact的对象的

而这个Fact的对象

是我们的应用和规则引擎进行什么呢

数据交互的桥梁或者是通道

比如说我们的应用和规则引擎进行什么呢

比如说咱们再结合我们的案例来看一下

比如说在我们这个地方

我通过这个session.insert

把这个order对象插入到工作内存里面去了

这个时候我可以把它称为就是Fact的对象

那么插进去之后

在咱们这个地方

是不是就可以进行模式匹配

匹配到之后

我是不是就可以通过这个dollar order

这种方式来引用到这个对象

而这个对象

其实就是我们这个地方

自己new的这个对象

同时呢

在我们这个地方

我是不是对这个real price进行了一个设置

设置完之后呢

在我们的应用程序里边

我是不是就可以通过order.getPrice

这个real price

就可以取到它的值

也就是说

我们这个Fact的对象

它起的作用就是什么呢

就是我们的应用程序和规则引擎

进行数据交互的桥梁或者通道

这个是非常重要的

这是第二个Fact

然后第三个呢

叫做Ruler Base

前面其实也提到过了

对吧

这个叫做规则库

我们编写的这个规则文件中

定义的这些规则呢

最终都会被加载到规则库中

来进行使用

这是规则库

再往下呢

是不是就是匹配器

匹配器它的作用就是什么呢

将我们规则库中所有的规则

与什么呢

与我们工作内存中

这些Fact的对象

对吧

来进行模式匹配

匹配成功之后呢

这些规则是不是将被激活

然后呢

放入到我们的

真的

就是议程当中

你看下面就是

用于存放匹配成功的

这些规则

最后呢

就是执行引擎

它是不是就来执行我们

这些

真的

就是议程当中被激活的

这些规则

好

这些概念呢

我们刚才其实都已经提到过了

咱们在这呢

再统一

再来说一下

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面内容，进行的结构化中文技术分析：

---

### 1) 视频摘要

本视频为一门关于 **Drools 规则引擎** 的技术课程，旨在讲解其核心概念与基础应用。讲师通过 **PowerPoint 幻灯片** 介绍规则引擎的架构（Rule Base, Agenda, Working Memory）和执行流程，并通过 **IntelliJ IDEA** 开发环境中的 Java 代码演示了如何定义规则、创建事实对象、将事实插入工作内存、激活规则并最终获取结果。视频内容聚焦于 DRL（Drools Rule Language）规则文件的编写和 Java 代码的集成，以“图书折扣”为业务场景进行教学。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程开场，讲师展示 PPT 大纲，介绍本节将讲解 DRL 规则语言和 Java 代码的结合。
*   **00:16 - 00:40**: 讲解 DRL 规则文件的结构，展示 `bookDiscount_3.drl` 和 `bookDiscount_4.drl` 两个规则文件的内容。
*   **00:41 - 01:00**: 讲解 Java 代码 `DroolsTest.java`，展示如何创建 `Order` 对象、调用 `kieContainer.newKieSession()` 创建会话、使用 `session.insert()` 将事实插入工作内存。
*   **01:01 - 01:20**: 讲解 `session.fireAllRules()` 方法，演示规则引擎如何自动匹配并执行规则。
*   **01:21 - 01:40**: 讲解 `session.dispose()` 方法，演示如何关闭会话。
*   **01:41 - 02:00**: 讲解规则引擎的执行流程，结合 PPT 上的架构图进行说明。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 关键内容：

*   **架构图**：展示了 Drools 规则引擎的核心组件：
    *   **Rule Base (规则库)**：存储从规则文件加载的规则。
    *   **Working Memory (工作内存)**：存储事实对象（Fact）。
    *   **Agenda (议程)**：存储通过模式匹配后被激活的规则。
    *   **Execution Engine (执行引擎)**：执行议程中的规则。
*   **3.3.2 相关概念说明**：
    *   **Working Memory**：规则引擎从其中获取数据并进行模式匹配。
    *   **Fact (事实)**：插入到工作内存中的对象，是应用与引擎交互的桥梁。
    *   **Rule Base**：规则库，存储规则文件定义的规则。
    *   **Pattern Matcher (匹配器)**：将规则库中的规则与工作内存中的事实进行模式匹配。
    *   **Agenda**：用于存放匹配成功的规则。
    *   **Execution Engine**：执行引擎，执行议程中的规则。
*   **3.3.3 规则引擎执行过程**：
    *   **第一步**：将初始数据（fact）输入至工作内存（Working Memory）。
    *   **第二步**：匹配器（Pattern Matcher）进行模式匹配。
    *   **第三步**：匹配成功的规则被放入议程（Agenda）。
    *   **第四步**：执行引擎（Execution Engine）执行议程中的规则。

#### 代码关键内容：

*   **规则文件 `bookDiscount_3.drl`**：
    ```drl
    rule "book_discount_3"
    when
        $order:Order(originalPrice >= 200 && originalPrice < 300)
    then
        $order.setRealPrice($order.getOriginalPrice() - 50);
        System.out.println("成功匹配到规则三");
    end
    ```

*   **规则文件 `bookDiscount_4.drl`**：
    ```drl
    rule "book_discount_4"
    when
        $order:Order(originalPrice >= 300)
    then
        $order.setRealPrice($order.getOriginalPrice() - 100);
        System.out.println("成功匹配到规则四");
    end
    ```

*   **Java 代码 `DroolsTest.java`**：
    ```java
    KieSession session = kieContainer.newKieSession();
    // Fact对象，事实对象
    Order order = new Order();
    order.setOriginalPrice(500);
    // 将Order对象插入到工作内存中
    session.insert(order);
    System.out.println("----优惠后价格：" + order.getRealPrice());
    // 激活规则，由Drools框架自动进行规则匹配，如果规则匹配成功，则执行当前规则
    session.fireAllRules();
    // 关闭会话
    session.dispose();
    System.out.println("优惠后价格：" + order.getRealPrice());
    ```

---

### 4) 关键场景与演示描述

*   **场景一：规则文件展示** (00:16 - 00:40)
    *   讲师在 IntelliJ IDEA 中打开 `bookDiscount_3.drl` 和 `bookDiscount_4.drl` 文件。
    *   通过高亮和滚动，展示规则的 `when` 和 `then` 部分，解释条件（`originalPrice >= 200 && originalPrice < 300`）和动作（`setRealPrice`）。
    *   屏幕上显示了中文注释，如“模式匹配，到规则引擎中（工作内存）查找Order对象”。

*   **场景二：Java 代码演示** (00:41 - 01:20)
    *   讲师在 `DroolsTest.java` 中高亮 `Order order = new Order();` 行，说明创建事实对象。
    *   高亮 `order.setOriginalPrice(500);`，说明设置原始价格。
    *   高亮 `session.insert(order);`，说明将事实插入工作内存。
    *   高亮 `session.fireAllRules();`，说明激活所有规则。
    *   讲师解释 `fireAllRules()` 方法会自动匹配规则并执行，最终 `order.getRealPrice()` 会返回折扣后的价格。

*   **场景三：规则引擎执行流程演示** (01:21 - 02:00)
    *   讲师切换回 PPT，展示“3.3.3 规则引擎执行过程”的架构图。
    *   通过鼠标指针和文字说明，演示了“将初始数据（fact）输入至工作内存（Working Memory）”这一第一步。
    *   讲师结合代码和 PPT，说明后续的匹配、激活和执行过程。

---

以上是根据视频画面内容整理的结构化技术分析。
