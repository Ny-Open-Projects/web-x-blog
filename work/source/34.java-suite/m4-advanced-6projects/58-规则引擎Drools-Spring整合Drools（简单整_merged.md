# 58-规则引擎Drools-Spring整合Drools（简单整 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来咱们来看我们课程的第七章

第七章是Spring整合D-Rose

咱们其实学习很多技术

最终是不是都要跟我们Spring这个平台来进行整合

那么我们D-Rose这门课程也是这样的

咱们前面讲了很多关于D-Rose它的用法

它的语法结构等等

那么最终我们在项目当中要使用的话

一般都是需要跟Spring来整合来使用的

咱们这一章就来看一下我们Spring如何来整合D-Rose

那么这个整合的话

我们是分成这么三个小节来讲解

分别是三种不同的整合形式

第一个是简单的整合

Spring简单整合D-Rose

这个就是在我们普通的Maven工程当中来进行整合

然后整合完成之后

可以通过我们单元测试这种方式来测试一下

咱们这个整合是否成功

而第二种方式就是加入了我们的

WinRow的WinRow

这个WinRow的WinRow的Web模块

其实也就是在我们的一个Spring MVC这个环境下来整合我们的D-Rose

最后是基于我们Spring Boot来整合D-Rose

咱们相当于是由简单到复杂

那么经过这么三种整合方式

只不过我们更多的情况下可能还是基于第三种

就是因为现在Spring Boot可能应用的会比较广泛

最后我们会基于Spring Boot来整合我们的D-Rose

那么接下来我们来看看我们的WinRow

接下来我们还是按照顺序

先来看我们第一种就是简单整合这种方式

第一步我们是不是需要来创建一个MainWin工程

所以这个的话我们就不在我们当前这个D-Rose QuickStart

这个工程上面来整合了

咱们来创建一个新的MainWin工程

然后在这个工程上面来进行整合

而这个工程的名字我就跟讲义保持一致了

就叫D-Rose-Spring

我把这个工程名考一下

然后咱们在这是不是来创建一个

新的

用一个新的Project

然后这块的话呢

因为是一个普通的MainWin工程

我们不用选择股价了

直接跳过去

这个GroupID呢

我们来设置一下

还是看不见IT黑码

模块名呢就是D-Rose-Spring

好Next

这个位置呢我们也不用调整了

直接完成

咱们直接在当前这个窗口打开就可以了

那么这样的话呢

我们就创建了一个新的

MainWin工程

对吧

在这个工程上面呢

我们来完成Spring

来整合我们的D-Rose

当然了这个工程创建完之后呢

咱们第一步是不是还是需要来导入相关的这个依赖

那么导入的依赖的话呢

除了有我们D-Rose的依赖呢

因为我们要引入Spring对吧

所以还有Spring相关的一些依赖

在我们的讲义上呢

我都已经整理好了

这块呢

这是我们设计到的这个版本的一个

属性设置对吧

后边的话我们是不是就可以通过这种方式呢

来指定我们每个框架所使用的这个版本号

D-Rose呢我们用的是这个版本

然后呢Spring用的是这个版本

具体的依赖呢就是下面在Dependency这里边

咱们整个考过来啊

整个考过来之后呢我们在idea里面来看一下

然后直接Ctrl-C拿过来

贴到我们这里面来

自动导入一下让它

咱们来看一下啊

这个呢我们已经建过了对吧

因为前面在我们那个QuickStart那个工程里边呢

我们是不是导入的就是这个依赖

但是还有这个JUnit对吧

那么除了我们前面已经导入过的这两种之外呢

因为Spring呢要跟这个D-Rose是不是来进行整合呀

所以啊我们需要导入这么一个包

你看叫做org.ke对吧

然后呢它这个模块ID呢叫做ke-spring

这个呢就是用于Spring跟D-Rose整合的啊

我们一个核心包

那么需要注意的一点是什么呢

这块呢有一个坑啊

如果大家没有经验的话

可能这块呢会遇到很多问题

就是什么呢

在我们引入这个包的时候呢

它会啊

传递过来我们Spring相关的一些架包

会传递过来Spring相关的一些架包

而这些架包呢

跟我们下边引入的这些Spring的架包

它是版本是不一样的

它们是有冲突的

所以说呢

我们一定要把

什么呀

它传递过来的这些啊

关于Spring的这些依赖给它排除掉

大家前面讲

学过Maven的应该都了解啊

通过exclusions对吧

这个标签呢

可以来排除传递过来的依赖

这个呢一定要排除

如果不排除的话呢

整个工程会报错啊

启动都都起不来

所以说呢我们一定要注意啊

就是这块我们在引入它这个包的时候呢

它会传递过来关于Spring的这些

你看Spring-TX的

Beans的

Curl的

还有Context的

这几个包

一定要给它排除出去

然后呢我们再来

导入我们

自己的Spring相关的这些依赖

具体的版本号呢

我上面是不是已经锁定了

就是这个版本号

5.0.5

这个呢是关于我们

这个Maven工程

创建好之后呢

先把相关的依赖

导进来

在第一步我们是不是就已经完成了

然后接下来的第二步的话

咱们是不是就需要来

创建我们的SpringPage文件呢

当然了按照讲义来也可以啊

先来创建一个规则文件也可以

这个顺序呢其实不是固定的

那我们就按照讲义来

咱们是不是在我们的Resources目录下面

来创建一个Ruler目录

在这下面呢来创建一个Hello World

这么一个规则文件

但是这这个规则文件我们现在在来看的话

就非常简单了

你看Win

然后呢UVL True对吧

它是不是永远会成立

成立之后呢在这个部分呢

我们是不是来说出一句话

因为我们这块呢

重点讲的是我们Spring跟D-Rose

如何来整合

所以说这个规则文件呢

我们就简单处理了

写了一个最简单的一个规则文件

那接下来呢咱们先把这个目录

Ruler来创建出来

找到咱们这个Resources

在这个下边来创建一个Directory

一个目录

就叫Ruler

然后下面呢咱们来创建这个规则文件

这个规则文件呢

我们就叫HelloWorld.DR

好

这个规则文件的内容呢

我就不再写了

我就直接从讲义上拷过来了

还是比较简单的

直接拿过来

那这个规则文件我们就准备好了

对吧这一步呢

就已经算是完成了

咱们把它关上

下一步呢我们是不是就需要来

提供Spring的配置文件

那可能有的同学就有疑问了

那我们要不要去提供这个D-Rose的配置文件呢?

咱们前面在做入门案例的时候

包括我们讲语法的时候对吧

都用到了Spring

都用到了D-Rose的那个

配置文件就是那个kmodule.tmer

那现在呢我们其实就

不再需要那个文件了

因为什么呢

我们现在跟Spring已经整合了

所以

在原先在那个文件里面配置的那些项呢

我们现在呢在Spring配置文件里面呢

都可以配置

这一点呢有点类似于我们以前

Spring整合MyBatties

对吧

如果你是单独使用MyBatties的框架

那你肯定要提供MyBatties的配置文件

那么如果你引入Spring之后呢

那个配置文件是不是也就不是必须的了

所以说

我们当前

这个整合之后呢

D-Rose

自己的那个kmodule那个配置文件呢就不是必须的了

我们只要提供Spring的配置文件就可以了

那接下来呢我们来提供出来

Spring配置文件起什么名字都可以啊

咱们就叫Spring.tmer吧

然后呢我们在这个地方来

在resource下面

对吧?

来创建一个file

这个呢是作为我们Spring的配置文件

然后呢这里面这个配置呢我就直接拷过来了

因为关于我们的配置文件呢

咱们没有必要去手写

我们直接拿过来

主要呢

是能看懂这里面的配置项

然后我们真正

在这个项目开发的时候呢

直接把

相关的这些配置拷过来

会改就可以了

上面呢我们来看到

这个

这个插门文件就不用说了

然后呢

这里面需要重点关注的是什么呢

我们Spring跟这个

Dios

整合之后啊

它有专门的一个namespace

一个命名空间就叫KIE

然后呢

这里面对应的这是它的约束对吧

约束

就叫KIE-Spring

这个xsd

这么一个文件

然后重点呢我们来看的是这块配置

其实这块配置呢大家应该看得非常熟悉

因为相关的这个配置呢在我们

原先那个KModel.tml里面

咱们是不是已经配置过呀

那个标签是不是就叫

KModel

然后给它一个唯一的ID就可以然后在这里边的有个KBase对吧

代表的是我们的规则库也给一个名字

然后呢注意看

package

咱们当时是不是也有那么一个属性叫package

它指定的这个代表的是谁呢代表的是不是就是我们resources下边的一个目录

一个目录

指的就是这个rules目录

因为呢我们的

规则文件是不是都会放在这个目录下

这样的话它就

就可以加载到我们

这个目录下所有的规则文件

对吧

然后呢在这里面是不是还有个叫做KSession

这个是我们的绘画对象

给它一个唯一的

名称

就可以

所以这块配置啊其实

对应的就是我们原先

在咱们那个deroads那个核心配置文件里面配置的那些项

只不过呢现在就是

前面给它加了一个什么呢

名称空间对不对

然后呢把它放到了我们Spring

这个文件里面来

其实它描述的

信息是完全一致的

OK

那么这块配置呢我们直接拿过来啊

直接拷过来

就可以了

然后下面这个呢我们

没有见过对吧

KModel annotation post processor

这个是什么意思呢

这个呢是我们一会儿在进行单元测试的时候呢

要使用到

这个deroads提供的一些

注解

一些注解

那么这块呢其实就是来

启用我们这些注解

如果你没有

这个bin配置的话呢我们

那些注解是没法正常使用的

所以说呢加入这个呢是为了我们

后边那个注解能够生效

你看annotation不就是注解的意思吧

那这块配置呢其实相对来说都是非常固定的

我们直接

把这个配置文件拷过来能看懂它是什么意思

就可以了

这是关于我们的配置文件是不是就已经搞定了

然后接下来呢我们就可以来编写咱们的单元测试了

所以下一步呢我们编写单元测试

在这里面来测试我们的单元测试

我们的代码

来测试我们这个整合是否成功

而且呢大家可以看到

咱们是不是在我们刚才那个POM文件里面已经引入了什么呢

已经引入了这个

JUnit

并且呢引入了我们Spring跟这个

JUnit这种单元测试对吧

这样的话呢我们在单元测试里边呢就可以通过这个什么run with,contact,configuration

来使用到

我们这个单元测试

通过这种方式来进行

测试啊

这个测试的话呢我就在test的这个下边来创建一个类啊

同时呢把包也来创建一下com.it

黑码

然后呢test的这个就叫derose

然后呢Spring

test

这个是

测试我们这个

derose和这个Spring整合

那么要整合的话呢

要测试的话呢是这样的咱们是基于

我们的这个

Spring

跟JUnit来进行单元测试对吧

所以我们在这上面呢需要加入这么两个注解啊一个是什么呢一个是run with对吧

run with

然后呢这个是SpringJUnit

class render

好这个是固定写法

然后呢还有一个是context configuration

那么这个呢用来加载我们的配置文件对吧

用来加载我们的配置文件

locations等于什么呢

咱们那个Spring配置文件呢

现在是不是在我们的classpass下面

叫做什么呢叫做Spring.dll

这样的话是不是就可以

加载到我们这个Spring配置文件了

加载到这个配置文件之后呢

它相当于

我们在进行单元测试的时候呢就把这个配置文件加载到

把Spring工厂是不是给初始化好

那么相关的对象呢

是不是也都给我们

这个初始化到我们的工厂里面去了

这样的话我们需要哪个对象呢是不是直接

注入到我们当前这个类里面来

来进行测试就可以了

那么我们当前应该把谁注进来呢

当前呢我们其实

应该注进来的是一个什么呢

应该注进来的是一个KBase对象

因为KBase对象里面是不是有我们的Session

那可能有的同学会说我直接把这个KSession注进来行不行

其实也是可以的

但是呢这个KSession它代表的是绘画对不对

那也就意味着

我们基本上就是一次交互

或者一次请求

应该创建一个新的KSession对象

然后呢

请求完之后呢

这个Session是不是就要销毁

所以说呢我们在这个地方呢

应该是注入KBase

是比较合适的

把我们这个规则库注进来

然后呢通过它呢

来创建一个Session

然后呢

使用这个Session来进行相关的操作

操作完之后把Session给关闭掉

那么全局的应该是它

叫KBase

所以说我们在这呢

是使用的

注进来的是KBase

也叫KIE Base

只不过这个注入呢大家可以看一下

注入的时候呢我们并没有使用到什么呢

原先我们那个Spring的AutoVal的

因为这块呢它这个整合比较特殊啊

刚才我们也提到了

它是不是有注解呀

你看在这个地方我们说要使用这个

这个Spring

跟这个

D-Rose整合之后的注解

那这块呢我们就会使用到这个注解来进行注入

而这个注解的话呢

就叫KBase

就是KBase

所以说呢这块呢比较特殊啊

咱们直接

把它拿过来大家来看一下

需要注意的是什么啊

你看这个KBase对应的是谁呢

其实对应的是我们这个

名称Name

跟它是对应的

这样的话呢就

注进来了一个KBase对象

KBase对象呢其实代表的就是我们的这个

规则库了

然后呢通过它的话

通过它的话呢我们就可以获得一个Session对象

获得一个Session对象

然后呢我们

在这儿呢来编写一个单元测试方法

咱们来测试一下

就叫test1吧

加一个test注解

那这块呢我们写下来就比较简单了

大家还记得吧原先呢我们

写的时候呢都用到了一堆API对吧什么KE Service啊

什么KE Container啊

然后最后最终获得Session对吧

现在呢我们就比较简单了

我们直接

通过这个什么呢

KE Base

然后通过它呢来

来创建一个Session

你看

我是不是就拿到这个Session对象了

拿到Session对象之后呢我们就可以直接通过Session对象

点什么呢

这拿到Session之后呢

咱们是不是就可以

向我们的工作内存里面来插入对象

只不过当前呢我们不用插入了

因为我们

刚才编写的那个规则

它是不是直接就等于触了

所以并不需要

插入对象

那我们就直接

怎么着

Fair or Rulers

让它进行匹配对吧

然后呢我们就把这个Session

关闭掉

它这个关闭叫做Dispose

这就是释放资源

那么这个单元测试写起来你看比我们原先那些单元测试就简单多了

好接下来我们来执行一下这个单元测试方法

大家来看一下

看一下我们那个控制台输出

你看它是不是已经

触发了

这样的话我们这个单元测试呢就已经测试成功了

刚才我提到咱们在这个地方是不是直接注入

我们那个KBase对象对吧

其实呢我们直接注入Session对象也是可以的

只不过我们是不建议这么做

咱们也可以来演示一下

来演示一下

比如说我现在呢我就想直接注入Session对象

这样的话从我们编写代码这个角度来看的话

是不是更加

更加简单一点对吧

我就不用通过KBase来获得Session了

而是直接

从我们Spring工厂里面来

注入一个Session进来

所以我们在这呢

可以通过这个KIE Session

Session

这个

KIE Session

然后呢

这个地方

直接注入呢就使用KSession

这个注解

就可以了

然后呢这个地方是不是来指定我们这个Session的名称

Session的名称呢我们

就叫KSession

对应的是Name这个属性值

就叫KSession

这样的话也可以注入它

也可以注入它

那么注入它之后呢咱们再来编写一个单元测试

这是改成Test2

那这样的话呢我就

就不用这个KBase了而是直接用我们的这个什么呢

KIE Session

直接用它

咱们来执行Test2

这是直接注进来一个

Session对象你看

它是不是也可以

也可以做到

只不过呢我们是不建议啊

这我们来写一下

不建议

直接

直接

注入我们的Session对象

当然我只是给你演示一下我们通过这种方式是可以做到的对吧

那么我们还是建议使用上面这种方式

那么到这儿的话呢咱们这种

第一个就是Supreme简单整合DRoze呢就已经搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为“Drools规则引擎”系列的第7章“Spring整合Drools”中的第7.1节“Spring简单整合Drools”。课程主要演示了如何在Spring项目中集成Drools，以实现规则引擎的自动化管理。讲师通过IntelliJ IDEA开发环境，逐步展示了从创建Maven项目、配置`pom.xml`依赖（包括Drools和Spring的特定版本），到创建规则文件（`.drl`）、配置Spring XML文件（`spring.xml`），最后编写并运行单元测试类（`DroolsSpringTest.java`）的完整流程。核心内容是通过Spring的`@ContextConfiguration`注解加载配置文件，并使用`KieServices`和`KieSession`来管理规则引擎的生命周期和执行。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在Typora编辑器中展示课程大纲，定位到“7. Spring整合Drools”章节。
*   **00:00:05 - 00:00:15**: 讲师开始讲解“7.1 Spring简单整合Drools”小节，说明在项目中使用Drools时通常会与Spring整合。
*   **00:00:15 - 00:00:30**: 讲师在IDE中打开`pom.xml`文件，开始配置项目依赖。
*   **00:00:30 - 00:01:00**: 讲师在`pom.xml`中添加Drools和Spring的依赖，并重点讲解了`<exclusions>`标签，用于排除Spring框架中的`spring-tx`、`spring-beans`和`spring-context`等包，以避免与项目中已有的Spring版本冲突。
*   **00:01:00 - 00:01:30**: 讲师在IDE中创建了`resources/rules`目录，并在其中创建了名为`helloworld.drl`的规则文件。
*   **00:01:30 - 00:02:00**: 讲师在IDE中创建了`spring.xml`配置文件，并配置了`<kie:kmodule>`、`<kie:kbase>`和`<kie:ksession>`等标签，用于定义规则库和会话。
*   **00:02:00 - 00:02:30**: 讲师在`pom.xml`中添加了Spring测试相关的依赖（`spring-test`）。
*   **00:02:30 - 00:03:00**: 讲师在IDE中创建了测试类`DroolsSpringTest.java`，并使用`@RunWith(SpringJUnit4ClassRunner.class)`和`@ContextConfiguration(locations = "classpath:spring.xml")`注解来加载配置。
*   **00:03:00 - 00:03:30**: 讲师在测试类中通过`KieServices`获取`KieBase`，并创建`KieSession`实例。
*   **00:03:30 - 00:04:00**: 讲师调用`KieSession.fireAllRules()`方法触发规则执行，并调用`dispose()`方法释放资源。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT内容**:
    *   课程大纲：`7. Spring整合Drools` -> `7.1 Spring简单整合Drools`。
    *   关键提示：`Drools默认dialect为"java"，尽量避免使用dialect "mvel"`。
*   **代码内容**:
    *   **`pom.xml` 依赖配置**:
        ```xml
        <properties>
            <drools.version>7.1.0.0.Final</drools.version>
            <spring.version>5.0.5.RELEASE</spring.version>
        </properties>

        <dependency>
            <groupId>org.drools</groupId>
            <artifactId>drools-compiler</artifactId>
            <version>${drools.version}</version>
        </dependency>

        <dependency>
            <groupId>org.kie</groupId>
            <artifactId>kie-spring</artifactId>
            <version>${drools.version}</version>
            <exclusions>
                <exclusion>
                    <groupId>org.springframework</groupId>
                    <artifactId>spring-tx</artifactId>
                </exclusion>
                <exclusion>
                    <groupId>org.springframework</groupId>
                    <artifactId>spring-beans</artifactId>
                </exclusion>
                <exclusion>
                    <groupId>org.springframework</groupId>
                    <artifactId>spring-context</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>${spring.version}</version>
        </dependency>

        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-test</artifactId>
            <version>${spring.version}</version>
        </dependency>
        ```
    *   **`helloworld.drl` 规则文件**:
        ```drl
        package helloWorld

        rule "rule_helloworld"
            when
                eval(true)
            then
                System.out.println("规则 rule_helloworld 触发...");
            end
        ```
    *   **`spring.xml` 配置文件**:
        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <beans xmlns="http://www.springframework.org/schema/beans"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xmlns:kie="http://drools.org/schema/kie-spring"
               xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd
                http://drools.org/schema/kie-spring
                http://drools.org/schema/kie-spring.xsd">

            <kie:kmodule>
                <kie:kbase name="kbase" packages="rules">
                    <kie:ksession name="ksession"></kie:ksession>
                </kie:kbase>
                <bean class="org.kie.spring.annotations.KModuleAnnotationPostProcessor"></bean>
            </kie:kmodule>

        </beans>
        ```
    *   **`DroolsSpringTest.java` 测试类**:
        ```java
        package com.itehima.test;

        import org.junit.Test;
        import org.junit.runner.RunWith;
        import org.springframework.test.context.ContextConfiguration;
        import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

        @RunWith(SpringJUnit4ClassRunner.class)
        @ContextConfiguration(locations = "classpath:spring.xml")
        public class DroolsSpringTest {

            @Test
            public void test1() {
                KieServices kieServices = KieServices.Factory.get();
                KieContainer kieContainer = kieServices.getKieContainer();
                KieSession kieSession = kieContainer.newKieSession();
                kieSession.fireAllRules();
                kieSession.dispose();
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖管理** (00:00:15 - 00:01:30)
    *   讲师在IntelliJ IDEA中打开一个名为`drools_spring`的Maven项目。
    *   讲师在`pom.xml`中添加了Drools和Spring的依赖，并特别强调了使用`<exclusions>`标签排除Spring框架中的特定包，以避免版本冲突。
    *   讲师在项目中创建了`resources/rules`目录，并在其中创建了`helloworld.drl`规则文件。
*   **场景二：Spring配置文件编写** (00:01:30 - 00:02:30)
    *   讲师在项目中创建了`spring.xml`文件。
    *   讲师在`spring.xml`中配置了`<kie:kmodule>`、`<kie:kbase>`和`<kie:ksession>`等标签，用于定义规则库和会话。
    *   讲师在`pom.xml`中添加了Spring测试相关的依赖。
*   **场景三：单元测试编写与执行** (00:02:30 - 00:04:00)
    *   讲师在`src/test/java`目录下创建了`DroolsSpringTest.java`测试类。
    *   讲师在测试类中使用`@RunWith(SpringJUnit4ClassRunner.class)`和`@ContextConfiguration(locations = "classpath:spring.xml")`注解来加载配置。
    *   讲师在测试方法中通过`KieServices`获取`KieBase`，并创建`KieSession`实例。
    *   讲
