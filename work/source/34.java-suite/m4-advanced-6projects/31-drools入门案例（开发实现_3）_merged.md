# 31-drools入门案例（开发实现_3） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好

那么刚才呢

咱们是已经完成了

我们这个规则文件的编写

再往下呢

我们就来编写一个单元测试

来测试一下我们这个D-Rose

看看我们的规则能不能匹配成功

好

编写单元测试呢

咱们可以在这个test的目录下边呢

来创建一个类吧

好

同时呢

连这个包一块给它创建上

这个就叫什么了

D-Rose test

好

在这里边呢

我们来编写一个单元测试的方法

好

别忘了加一个test注解

对吧

好

那么具体这里边这个代码怎么写

其实呢

前面呢

我们在进行这个规则引擎

D-Rose介绍的时候呢

也提到了

这是它的API开发的步骤

咱们可以对比着这个步骤呢

来编写

首先呢

我们第一步呢

需要来获取一个KIE service

好

那么它叫

KIE service

你看它这里边

主要KIE

注意啊

是带S的这个啊

别找错了

好

就是这个

那么这个类怎么获得呢

注意并不是new出来的

而是它这里边有一个factory

这么一个方法

这么一个对象

对吧

然后呢

调用get方法

来获得这么一个KIE service

好

这个是固定的

这样就获得了一个KIE service

那么拿到它之后呢

我们可以通过它呢

来获得一个KIE什么呢

container

好

而它这个呢

底层呢

它会去默认去读取我们提供的这个Kmodel

对吧

Kmodel这个文件

而在这个文件里边

我们是不是指定了这么一个Rules目录

那这样的话呢

我们的框架呢

就会到Rules目录下边来加载所有的规则文件

那这样的话

我们这些规则呢

是都被加载到了

都被加载到了

好

那么加载到之后呢

来创建一个容器对象

好

有了容器对象之后呢

就可以在容器对象里面来获得一个Session

KIE Session

是不是就是一个绘画对象啊

所以接下来我们需要从我们的这个

KIE容器对象中来获取什么呢

绘画对象

好

那么通过KIE Container点什么呢

叫New KIE Session

这样的话呢

就能够得到一个Session对象

就是一个绘画对象

但是需要注意的是什么呢

并不是所有的情况下都能够获得这个Session

当前我们

这个为什么能获得呢

是因为我们在这个配置文件里面

是不是确实配置了这么一个标签呢

并且它是还是默认的

对不对

你看我们在这儿

是不是并没有去指定这个Session的名称

它为什么也能拿到

就是因为啊

我们在这儿指定的

它是一个默认的Session

所以从这个容器里边呢

就可以把这个默认的Session对象给获取到

好

那么这样的话

我是不是就把这个Session对象

绘画对象拿到了

因为我们拿这个绘画对象干什么呢

因为我们接下来要做的

是不是就需要

把我们的

这个数据啊

提供给我们的规则引擎

对不对

因为前面我们也看到了

它是一个输入输出平台啊

我们需要把这个数据

是不是给它输入到我们规则引擎里面去

通过什么呢

我们通过这个Session对象就可以完成

所以我们会调用这个Session对象的一个什么呢

叫做Insert这么一个方法

这个方法的作用就是将我们的这个对象

把它插入到我们工作内存里面去

大家还记得吧

我们说到有个工作内存这么一个概念对吧

插入到工作内存里面去

其实它是我们这个规则引擎里边的一个内存区域

叫做工作内存

好

那么我们要插进去什么样的数据呢

刚才我们也提到了

咱们这个order这个对象是不是就是我们的数据的载体

所以说呢

咱们在这呢

需要来构造一个

构造一个order对象

order 订单对象

那么把它导进来

那么我们直接new一个order就可以了

把它导进来

并且呢

我是不是需要来设置一下什么呢

设置一下我们这个原始的价格

那么最终价格还用我们设置吗

其实不用啊

因为我们用工作

我们需要理解啊

咱们使用这个D-Rose

目的是什么呢

目的是不是就是让它帮我们去计算最终的价格

我们是不是把规则告诉它

它会自动的来进行规则的匹配

然后最终呢

帮我们来算出来一个最终的价格

对不对

所以说我们要做的只是原始的价格

原始的价格

你需要给它设置进去

然后这个D-Rose呢

这个框架呢

会告诉我们计算之后的结果

也就是优惠后的价格

比如说我当前呢

先整一个50

那么加个D啊

因为它是这种double类型的

你看啊

我们这儿呢

是不是这种double类型的

所以说呢

需要加一个D

好

这是我们原始的数据

对吧

它是通过这个order对象

那么反映出来的

而实际上呢

在我们D-Rose里边呢

它对于order类似于这种对象

给它起了个名字啊

特有的这个名字叫做什么呢

叫做fact

叫做fact的对象

其实就是什么呢

事实对象

事实对象

这是我们给它这个翻译成汉语

对吧

翻译成汉语

就是事实对象

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段关于 Drools 规则引擎入门教程的技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程旨在为初学者讲解 Drools 规则引擎的基本使用方法。讲师通过一个“图书订单折扣”的业务场景，演示了如何在 Java 项目中集成 Drools，编写规则文件（`.drl`），并通过单元测试（JUnit）来验证规则的执行效果。核心内容包括：获取 KieServices 和 KieContainer，创建 KieSession，插入事实对象（Order），激活规则（fireAllRules），以及获取最终的优惠后价格。整个过程旨在帮助学习者理解规则引擎的核心工作流程。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的截图未包含明确的时间戳，以下章节结构是根据画面内容和典型课程结构推断的：

*   **00:00 - 00:30**: 课程引言与问题引入。讲师介绍规则引擎的概念，并展示一个简单的图书折扣业务场景，引出需要使用规则引擎来动态处理不同折扣规则。
*   **00:30 - 01:00**: 规则引擎概述。讲解规则引擎的优势（如业务逻辑与代码分离、易于维护和扩展），并介绍 Drools 作为主流的规则引擎。
*   **01:00 - 01:30**: Drools 简介与入门案例。展示项目结构，包括 `src/main/resources/rules/` 目录下的规则文件（`.drl`），并介绍 `Order` 实体类。
*   **01:30 - 02:00**: 业务场景说明。详细说明“图书订单折扣”的业务规则，包括：
    *   原价低于 100 元：无优惠。
    *   原价在 100-200 元之间：优惠 20 元。
    *   原价在 200-300 元之间：优惠 50 元。
    *   原价高于 300 元：优惠 100 元。
*   **02:00 - 02:30**: 开发实现 - 第五步：编写单元测试。讲师开始编写 `DroolsTest.java` 文件，演示如何通过 `KieServices` 获取 `KieContainer`，并创建 `KieSession`。
*   **02:30 - 03:00**: 开发实现 - 第五步：编写单元测试（续）。讲师创建 `Order` 对象，设置原价为 504 元，并将其插入到 `KieSession` 中。
*   **03:00 - 03:30**: 开发实现 - 第五步：编写单元测试（续）。讲师调用 `session.fireAllRules()` 方法激活规则，并在会话结束后调用 `session.dispose()` 关闭会话。
*   **03:30 - 04:00**: 开发实现 - 第五步：编写单元测试（续）。讲师添加 `System.out.println` 语句，用于打印最终的优惠后价格，以验证规则执行结果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档结构**:
    *   展示了课程大纲，包含“问题引入”、“规则引擎概述”、“Drools介绍”、“业务场景说明”、“开发实现”等主要部分。
    *   展示了项目结构图，包括 `src/main/java`、`src/main/resources`、`test` 等目录。

*   **代码关键内容**:
    *   **规则文件 (`bookDiscount.drl`)**:
        ```drl
        // 所购图书总价在100元以下的没有优惠
        rule "book_discount_1"
        when
            $order: Order(originalPrice < 100)
        then
            $order.setRealPrice($order.getOriginalPrice());
            System.out.println("成功匹配到规则一");
        end

        // 所购图书总价在100到200元的优惠20元
        rule "book_discount_2"
        when
            $order: Order(originalPrice >= 100 && originalPrice < 200)
        then
            $order.setRealPrice($order.getOriginalPrice() - 20);
            System.out.println("成功匹配到规则二");
        end

        // 所购图书总价在200到300元的优惠50元
        rule "book_discount_3"
        when
            $order: Order(originalPrice >= 200 && originalPrice < 300)
        then
            $order.setRealPrice($order.getOriginalPrice() - 50);
            System.out.println("成功匹配到规则三");
        end

        // 所购图书总价在300元以上的优惠100元
        rule "book_discount_4"
        when
            $order: Order(originalPrice >= 300)
        then
            $order.setRealPrice($order.getOriginalPrice() - 100);
            System.out.println("成功匹配到规则四");
        end
        ```
    *   **测试代码 (`DroolsTest.java`)**:
        ```java
        import org.junit.Test;
        import org.kie.api.KieServices;
        import org.kie.api.runtime.KieContainer;
        import org.kie.api.runtime.KieSession;

        public class DroolsTest {
            @Test
            public void test1() {
                // 获取Kie容器对象
                KieServices kieServices = KieServices.Factory.get();
                KieContainer kieContainer = kieServices.newKieClasspathContainer();

                // 从Kie容器对象中获取会话对象
                KieSession session = kieContainer.newKieSession();

                // Fact对象，事实对象
                Order order = new Order();
                order.setOriginalPrice(504);

                // 将Order对象插入到工作内存中
                session.insert(order);

                // 激活规则，由Drools框架自动进行规则匹配，如果规则匹配成功，则执行当前规则
                session.fireAllRules();

                // 关闭会话
                session.dispose();

                // 打印优惠后价格
                System.out.println("优惠后价格：" + order.getRealPrice());
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与规则文件创建**。
    *   讲师在 IntelliJ IDEA 中展示项目结构，重点指向 `src/main/resources/rules/` 目录。
    *   讲师在该目录下创建并编辑 `bookDiscount.drl` 文件，逐条编写四个折扣规则，使用 `when` 和 `then` 关键字定义条件和操作。

*   **场景二：编写测试类 `DroolsTest.java`**。
    *   讲师在 `src/test/java` 目录下创建 `DroolsTest.java` 文件。
    *   讲师导入必要的包，如 `org.junit.Test`、`org.kie.api.KieServices` 等。
    *   讲师编写 `@Test` 方法 `test1()`，并逐步添加代码：
        1.  通过 `KieServices.Factory.get()` 获取 `KieServices` 实例。
        2.  通过 `newKieClasspathContainer()` 创建 `KieContainer`。
        3.  通过 `newKieSession()` 创建 `KieSession`。
        4.  创建 `Order` 对象并设置原价为 504。
        5.  调用 `session.insert(order)` 将事实对象插入工作内存。
        6.  调用 `session.fireAllRules()` 激活并执行所有匹配的规则。
        7.  调用 `session.dispose()` 关闭会话。
        8.  最后，通过 `System.out.println` 打印 `order.getRealPrice()`，以验证规则执行后的结果。

*   **场景三：规则执行与结果验证**。
    *   讲师在代码中添加了 `System.out.println` 语句，用于在控制台输出最终的优惠后价格。
    *   讲师强调，当原价为 504 元时，会匹配到规则四（原价 >= 300），因此优惠后价格应为 404 元。
    *   讲师通过运行测试，演示了规则引擎如何根据条件自动匹配并执行相应的规则，最终输出结果。
