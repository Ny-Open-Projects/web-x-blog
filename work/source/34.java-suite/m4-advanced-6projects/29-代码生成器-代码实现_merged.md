# 29-代码生成器-代码实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们继续实现MyBattisGenerate工程

之前咱们实现了它对应的配置

那么接下来我们就将代码

以及Maven插件集成到我们的工程当中

好

首先我们将代码做一个实现

我们要创建一个包

右键创建一个package

这个我们就叫timeItCast

MyBattis.Generate

好

下面我们再创建两个包

OpenIntomid

MakeDir

一个包是Custom

实现了我们的自定义的

MyBattis.Generate的生成器

在这里面的话

我们要实现一个自定义的注视生成器

将它放在Custom包下面

另外一个的话

就是我们的启动内

Startup

好

创建完成之后

咱们先来实现了自定义的注视生成器

好

注视生成器我们从讲义当中直接Copy进来

这个我们找一下是在这里面Custom

首先创建对应的Class

好

创建完成之后

我们将代码Copy进来

让它自动导入相关的依赖

这里面的话还没找到

我们把它引入进来

在这里对是在MyBattis.Generate的包下面

不要引入错误

我们要打这个包一定要指定正确

好

指定完成之后

咱们就来看一下

它这一块是怎么做的实现呢

Custom.Common.Generate

它是继承一个D4的Common.Generate

也就是说咱们如果不自定义的话

它就会采用MyBattis.Generate的默认的注视生成器

那么我们可以看一下

默认的注视生成器里面

它怎么去做呢

在这里面它会去添加对应的注视

对不对

我们可以看到它生成的都是些什么

都是些英文字

对不对

对不对

对不对

对不对

对不对

对不对

对不对

对不对

对不对

对不对

对不对

对不对

对不对

对不对

对不对

对不对

可以看到有些MyBattis很多的一些标签在这里面

那这样是非常不直观

咱们可以看到会生成很多的一些不必要的信息

而且它还将它MyBattis.Generate的这样的一些说明

也放入在里面

所以我们不需要怎么办

那就通过我们的自定义的注视生成器

在这里面的话

我们去重写它对应的方法

我们修改了哪些

在这里面的话

是将类的头部信息

这个呢重新生成一下

好

这一个地方呢要做修改

另外的话呢

就是生成类的成员变量

也就是属性的注释

这一块呢也做的重写

接下来的话呢

就是生成类的

就是它对应的

我们可以看到

一个呢是add field common

对不对

一个呢是有field

然后在这里面的话呢

是table

另外的话呢

我们可以看到

这里面呢

它还多了一个参数

是interspect chromium

这个的话呢

是多了一个列性性的传递

也就这两个方法的话呢

它们是重载的

那么它实际上会调用哪个方法呢

它会调用这个方法

因为它会根据那个列名里面的信息

去添加它对应的注释

所以话呢

最主要咱们要重写这里面的一个实现

那这里的话呢

咱们去写也可以

那我们看一下

在这里面我们去怎么做呢

我们是将

在circle里面这个列定义的属性

将它呢读取出来

看到没有

读取它的备注描述

然后呢

我们再将它呢

通过

这种方式

就是最后拼接成为呢

就是我们这种完整的注释

在这里面我们可以看一下

这个比如说你是一个订单电号

对不对

那它呢最终就会生成这样一个格式

然后在这里面的话呢

就是buy with

然后bin order number

这样的一个生成格式

好

这个呢是它的方法

这一块的重写

然后呢还有get方法

对不对

get方法的话呢

同样我们在get方法的注释上面的话呢

为了防止它生成默认的注释

咱们将这一块呢也做了一个调整和修改

那么主要的话呢

是定义的注释实现类呢

它在这里面一个呢是修改它头部信息

然后呢还修改它的一个成员变量信息

以及呢它的get方法

下面呢咱们来找到对应的启动类

public generate application

near一个class

这个启动类呢就比较简单

我们来看一下

启动类它要做什么事情呢

它要去加载我们对应的项目呢

对于我们的项目呢它要去加载我们对应的项目呢

对应的之前所定义的XML配置

然后呢去生成对应的代码

在这里呢我们要注意一下

在windows下面

如果它给的project输出目录呢

我们是要加上工程名称的

那它给的project的话呢

在windows下面的这个情形下

通过neverplugin呢

生成的话呢就不需要加这个工程名

这个呢我们一定要注意一下

不然的话呢它生成的这个

输出的目录

它找不到这个目录

找不到你相对的一个路线

所以呢它到时候生成的话呢

就不能按照你指定的要求生成在对应的目录下面

比如说咱们想让它生成在mybattisgenerator的这个output目录下面

我们把它创建一下

那这样的话呢

你怎么去配置呢

我们要在它给的project下面去指定了你的工程模块

也就是说它的相对路径是在哪里

就是在你的project复集工程下面

它就去下面找到mybattisgenerator

然后再找到对应的这个目录

这一点呢大家要清楚

那如果是通过neverplugin呢

就在下面的通过never的这个插件去生成的话呢

在这里就不需要去指定了它对应的工程名称

在下面章节我们去操作和演示的时候呢

还会做一个讲解介绍

那我们来看一下

在这里呢

它会定义输出的预警信息

对不对

这个呢警告内容呢

我们可以看到

如果说你不输出这个警告内容

那么执行完成之后没有生成代码

你这个时候就不太好去排错

明白吗

所以呢

我们要将它的警告信息呢

要将它打印出来

那么打印出来之后呢

咱们就可以很习惯的看到具体是什么原因会导致这个代码没有生成成功

好

这一点呢

是要注意的地方

那么其他这一块我们可以看到

它要读取它的配置

对不对

这个配置的话呢

首先要创建一个configure

play一个

配置转换器

然后呢configure在这里面的话呢

通过playconfiguration

然后呢指定它的class的内的加载器

那么指定了内加载器之后的话呢

还有一个callback的回调函数

那么就通过mybatties的generator

这个处理对象呢

将这些配置呢

注入到它的属性当中

通过构造方法

可以看到它是怎么去注入呢

这里面的话呢

都已经定义了对应的一个配置

对不对

好

通过构造方法

注入它的配置

进去之后呢

然后再通过mybatties的generator

这个对象呢

去生成对应的代码

那么执行到这个方法之后呢

这个代码呢

如果是正常的话呢

就是能够成功生成

那如果是出现错误呢

咱们要注意

因为呢

这个处理起来会有些坑

它不会像我们之前的这种服务也好

运行的时候呢

都会爆出明确的错误

像那个servinboot服务启动的时候

它都会抛出一些exception

但在这里面呢

有些情况下面

你没有生成代码

它也不会抛出异常

所以呢

我们就需要让它将警告信息呢

也给我们打印出来

可以看到

它生成的警告信息之后呢

不会直接走到异常

除非它是发现很严重的错误

所以呢

我们就需要将它的那个警告信息呢

输出出来

好

这一块呢

就是启动内的一个实现逻辑

以及呢

要注意的地方

那么在这里呢

我们就实现了它的一个制定的注释

对不对

还有呢

启动器

那接下来呢

咱们就来看看

我们对代码生成器呢

做一个测试和验证

我们呢

先将启动内呢

执行一下右键

run运行

它会连接我们的虚拟机的数据库

好

它是告诉我们呢

没有找到什么

制定的注释生成器

因为这个路径不正确

我们可以copy一下

在这里面呢

去做一个调整

像这种错误呢

它都会明显的跑出来

可以看到

这个是配置正确了

对不对

如果说一些警告信息呢

它是不会抛出一个safety

这种严重错误的话呢

因为阻塞了它的一个运行对应

所以呢

它就会进入到这里面的逻辑

好

那咱们呢

再重新执行一遍

看一下呢

我的boot目录

能否呢

正常生成对应的代码

好

在这里面的话呢

它提示什么

一个jst file

说这个文件呢

已经生成了

我们来看一下

com idcast

shed stock

do

然后呢

nt

是不是有两个实体啊

对吧

一个实体的话是acad

一个是user

就在我们配置文件当中

在一个table的这个配置当中

我们呢

是指定了一个

t-shirt的user表

以及呢

t-shirt的acad表

那么呢

它也是按照我们的要求

生成这两个对象

对不对

并且呢

将它的那个map接口呢

还有它的map文件呢

都给我们生成好了

我们可以看一下

map文件

对不对

像这种话呢

实体的这种属性映射

都帮我们自动生成好了

这样呢

就能够

解化我们很多的一些工作量

而且呢

也不容易出错

对吧

因为你自己去手写的话呢

万一敲错了一个字母

或者说大小写错误的话呢

运行起来的话呢

又会出现问题

好

在这里面呢

咱们就看到了

它整个代码生成的话呢

都是ok的

而且注释生成器

咱们也可以看到

是不是按照自定义的注释

去生成了对应的

这个说明

对吧

这些的话呢

都没有问题

那么

我们可以看一下get方法

get方法的话呢

也是按照那个列的注释

生成了

这个对应的一个说明

那么如果说你没有去修改的话

我们可以看到

它就会生成一大串的这个注释

非常不直观

对吧

而且没有实际的参考和接近意义

好

那这一块呢

就是对代码生成器的一个实现

和它的一个基本配置

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频课程讲解了 MyBatis-Generator 的高级定制化功能，核心是通过自定义注释生成器（`CustomCommentGenerator`）来控制代码生成时的注释内容。讲师首先展示了如何在 `generatorConfig.xml` 配置文件中指定使用自定义的注释生成器，然后详细演示了如何编写 `CustomCommentGenerator` 类，使其能够根据数据库表的备注信息（`remarks`）自动生成 Java 类的注释。最后，通过运行 `GeneratorApplication` 主程序，验证了自定义注释生成器的成功应用，并展示了生成的 Java 实体类和 Mapper 接口文件。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，讲师介绍本节内容为 MyBatis-Generator 的高级定制。
*   **00:05 - 00:15**: 展示 `generatorConfig.xml` 配置文件，重点讲解如何通过 `<plugin>` 标签指定自定义注释生成器 `CustomCommentGenerator`。
*   **00:15 - 00:30**: 讲解自定义注释生成器的实现原理，展示 `CustomCommentGenerator.java` 文件的代码结构。
*   **00:30 - 00:45**: 详细分析 `addFieldComment` 方法，演示如何从数据库字段的备注中提取信息并生成 Java 字段的注释。
*   **00:45 - 01:00**: 讲解 `addModelClassComment` 方法，演示如何为生成的 Java 类添加注释。
*   **01:00 - 01:15**: 展示 `GeneratorApplication.java` 的主方法，讲解其如何初始化并调用 MyBatis-Generator。
*   **01:15 - 01:30**: 通过终端运行 `GeneratorApplication`，演示代码生成过程。
*   **01:30 - 01:45**: 展示生成结果，包括生成的 `TradeUser.java` 和 `TradeAccount.java` 文件，以及终端输出的警告信息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **左侧大纲**: 显示了课程的章节结构，包括“第5章 MyBatis Generator代码生成器”下的“3.3 使用说明”和“3.4 通过MAVEN插件形式生成”。
    *   **`generatorConfig.xml` 配置文件**:
        ```xml
        <generatorConfiguration>
            <context id="DB2Tables">
                <plugin type="org.mybatis.generator.plugins.SerializablePlugin"/>
                <!-- 其他配置 -->
                <commentGenerator type="com.icast.mybatis.generator.CustomCommentGenerator"/>
            </context>
        </generatorConfiguration>
        ```
    *   **`CustomCommentGenerator.java` 代码**:
        ```java
        public class CustomCommentGenerator extends DefaultCommentGenerator {
            // 重写 addFieldComment 方法
            @Override
            public void addFieldComment(Field field, IntrospectedTable introspectedTable, IntrospectedColumn introspectedColumn) {
                String remarks = introspectedColumn.getRemarks();
                if (StringUtility.stringHasValue(remarks)) {
                    String[] remarkLines = remarks.split(System.getProperty("line.separator"));
                    for (String remarkLine : remarkLines) {
                        field.addJavaDocLine(" * " + remarkLine);
                    }
                }
                field.addJavaDocLine(" * ");
            }
            // 重写 addModelClassComment 方法
            @Override
            public void addModelClassComment(......) {
                // 生成类注释
            }
        }
        ```
    *   **`GeneratorApplication.java` 代码**:
        ```java
        public class GeneratorApplication {
            public static void main(String[] args) {
                List<String> warnings = new ArrayList<String>();
                boolean overwrite = true;
                ConfigurationParser cp = new ConfigurationParser(warnings);
                Configuration config = cp.parseConfiguration(GeneratorApplication.class.getClassLoader().getResourceAsStream("generatorConfig.xml"));
                DefaultShellCallback callback = new DefaultShellCallback(overwrite);
                MyBatisGenerator myBatisGenerator = new MyBatisGenerator(config, callback, warnings);
                try {
                    myBatisGenerator.generate(null);
                    if (warnings.size() > 0) {
                        for (String warn : warnings) {
                            System.out.println(warn);
                        }
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：配置自定义注释生成器** (00:05-00:15)
    *   **描述**: 讲师在 `generatorConfig.xml` 文件中，通过 `<plugin>` 标签指定了自定义注释生成器 `CustomCommentGenerator`。他强调，通过这种方式，可以完全控制生成的 Java 代码中的注释内容。
*   **场景二：实现 `addFieldComment` 方法** (00:30-00:45)
    *   **描述**: 讲师在 `CustomCommentGenerator.java` 文件中，展示了 `addFieldComment` 方法的实现。该方法首先获取数据库字段的备注信息（`remarks`），然后将其按行分割，并逐行添加到 Java 字段的注释中。他特别强调了 `StringUtility.stringHasValue(remarks)` 的判断，以避免空值导致的异常。
*   **场景三：运行生成器并查看结果** (01:15-01:45)
    *   **描述**: 讲师在终端中运行 `GeneratorApplication`。程序成功执行后，终端输出了生成的文件列表，包括 `TradeUser.java` 和 `TradeAccount.java`。同时，也输出了警告信息，提示某些字段（如 `FRED`、`DATE_FIELD`）在数据库中不存在，这表明自定义注释生成器已成功应用，并且能够根据数据库结构动态生成注释。
