# 19-文件服务课程-文件服务开发（文件处理策略_L — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么前面呢,咱们是已经实现完了这个抽象的文件策略处理类,然后接下来呢,我们要实现的就是一个具体的一个处理类,就是当我们这个文件的存储策略选择的是本地存储的时候,那么我们就需要提供这么一个叫做local service impr,那么它是什么呢?

它是我们这个abstract file strategy,也就是这个抽象类的一个子类,负责什么呢?处理存储策略为本地时的文件上传和删除这些操作。

当然了,为了使我们这个程序能够动态的来选择具体的一个策略处理类,前面我们也反复强调,我们这个策略处理类呢,咱们在课上呢,会提供这么三种,对吧?分别是本地,还有Faas的DFS存储,还有一个就是阿里云存储。

那么也就是说,为了能让我们这个程序啊,

我们可以通过一个动态的去选择具体的一个策略处理类,那么我们可以通过一个什么呢?配置类,然后呢,通过配置类这种方式来动态去选择。

所以说呢,我们具体的这个local service impr呢,这个类呢,就需要定义到我们的策略类里面。

首先呢,由策略类动态去选择,对吧?然后呢,当我们这个某个条件成立的时候,比如说什么呢?

比如说我们配置的这个属性,对吧?

Pin打点file,点type,对吧?

然后呢,如果设置的是local,这个时候呢,我们就会使用我们这个local service impr。

所以说呢,我们是通过一个配置类来动态的去选择一个什么呢?具体的策略处理类。

好。

那接下来呢,咱们就先把这个什么呢?先把我们这个配置类来创建一下。

咱们这个配置类的名字呢,就叫什么呢?就叫做local auto configure就可以了。

好,放在什么呢?放在我们这个storage这个目录下面。

好。

然后呢,我们就把这个配置类呢,就叫做local auto configure就可以了。好,放在什么呢?放在我们这个storage这个目录下面。

好。

好。

然后呢,我们回到idea。

在我们的file这层目录下面来创建一个新的目录,对吧?storage指的就是存储的意思,对吧?

然后呢,我们在这下面来创建我们这个什么呢?叫做local auto configure。

好。

那么这个类呢,是一个配置类,对吧?它是一个配置类。

然后呢,它做的事是什么呢?咱们来写一下。

这个呢,就是处理这个配置类。

处理的是我们本地上传一个这个策略,这么一个配置类吧,配置类。

好。

那么,既然它是一个配置类的话呢,咱们是不是需要来加入相关的一些注解?比如说什么呢?一个是configuration,对吧?

配置类必须要加这么一个注解。

然后呢,咱们为了方便接日志啊,我们再加一个这个slip4j的。

然后这样的话,我们就可以直接使用那个log对象了,对吧?进行日志记录。

好。

然后呢,我们在这里边呢,可能还需要来这个加在我们配置文件里面的一些属性,对吧?

所以说呢,我们要启用什么呢?启用我们这个配置属性类。

所以在这儿呢,还要加一个什么?enable configuration properties。

然后指定是哪一个配置属性类,大家还记得吧?前面我们是不是定义了这么一个啊,叫做file server properties。

所以在这儿呢,需要把它启用了。

file server properties。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

什么生效呢

它是基于一个属性

而这个属性呢

我们应该是在配置文件里面

是不是去配置的

应该是在配置文件里面去配置的

所以我们在这呢

来指定一下name

这个属性的名字

注意这个名字不是随便定义的

需要跟我们的配置文件

是不是保持一致

咱们来看一下

我们这是不是有这一个配置文件

PDFile

Server

对吧

然后呢

我们来看一下

咱们是不是在这

最高层的是品达

然后再往下一层是File

然后是Type

对吧

指定的就是我们文件存储类型

然后这个存储类型呢

我们是不是可以有多个选择

比如说我现在呢

其实配置的是FastDFS

我还可以配置什么呢

Local

还可以配置Ali

对吧

如果是你扩展了其他的呢

你可以再配置自己扩展的

比如说你扩展七牛的

对吧

腾讯的等等

那么都可以

咱们呢

只不过是在课上呢

只是提供了其中的三种

好

所以说我们在这呢

就需要

哎

是

Verex

就是什么呢

叫做品达

File

然后Type

来看这个属性

对吧

品达

然后呢

File.Type

这是跟咱们配置文件保持一致

我们来看这个属性

然后呢

在它等于什么

什么的时候

我们当前这个配置类生效呢

咱们通过一个Heaving Value

等于什么呢

等于Local

Local

哎

你看

Local是不是就是本地

所以说呢

如果说我们这个地方

这个Type设置的是Local呢

这个地方呢

这个时候我们当前这个配置类就会生效

当前这个配置类就会生效

那这样的话

我就可以在我们这个配置类里面

来创建什么

创建我们真正的local service MPL

创建具体的策略处理类

所以我们在这里面

就需要来定义一个类

public class

你看在这里面来定义一个内部类

叫做什么

叫做local service MPL

然后别忘了让它继承一下

我们前面实现的

已经完成的抽象类

叫做abstract file strategy

abstract file strategy

就是继承它

那么这里面因为它有抽象方法

所以我们在当前这个类里面

需要去实现

分别是upload file

还有delete这两个方法

这个方法很明显

这就是我们文件上传的方法了

好

文件上传

然后这个是删除

好

文件删除

然后我们需要注意

咱们是不是需要给这个类

来加一个注解

因为最终这个service类

也是需要到

让我们这个sprint容器去管理

对吧

所以说我们需要给它在这来

加一个什么

service注解

这个别忘了

这个就是我们本地文件策略处理类

本地文件策略

处理类

好

那么这个类什么时候会被创建呢

就是当我们配置的什么呢

当我们配置的这个品达file type

对吧

然后呢

它的值给的是local

那这个时候呢

我们这个配置类才会生效

那么它生效的话呢

这个service也就会被创建出来了

假设啊

假设我们配置的不是这个local

对吧

那这就说明我们当前这个配置类啊

它不会生效

那么不会生效的话呢

我们当前这个service呢

我们当前这个service呢

我们当前这个service呢

我们当前这个service呢

我们当前这个service呢

也不会被创建

也不会加到我们这个support容器当中

所以它是通过这么一种方式啊

就是通过我们这个配置类

然后呢

间接的来控制咱们这个service是否要实力化

好

那么这是先把我们这个配置类

以及这个什么呢

service啊

先创建出来

后边的话呢

我们是不是就具体去实现咱们这个细节

比如说我们要将这个上传的文件保存在本地

对吧

对吧

应该具体如何保存

这就是真正细节处理

以及删除文件对吧

那么具体怎么删除

那么这就是我们需要去编写的

好

咱们这个小节呢

先把这个架子给搭起来

所需要的这两个类先创建好

一会儿呢

我们再去实现具体的这两个方法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个文件服务模块中“本地存储策略”的实现教程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建一个名为 `LocalServiceImpl` 的具体策略类，该类继承自抽象策略类 `AbstractFileStrategy`。核心内容包括：定义配置类 `LocalAutoConfigure`，使用 Spring Boot 的 `@Configuration`、`@EnableConfigurationProperties` 和 `@ConditionalOnProperty` 注解，使该策略在配置文件中设置 `pinda.file.type=LOCAL` 时被激活。同时，讲师展示了该策略类中需要实现的两个核心方法：`uploadFile` 用于文件上传，以及 `delete` 用于文件删除，并在方法中添加了占位符实现。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 展示课程大纲，定位到“5.2 文件处理策略”下的“5.2.3 LocalServiceImpl”章节。
*   **00:00:05 - 00:00:15**: 讲师在代码编辑器中展示 `LocalServiceImpl` 类的定义，说明其是 `AbstractFileStrategy` 的子类，负责本地文件的上传和删除操作。
*   **00:00:15 - 00:00:30**: 讲师切换到 `LocalAutoConfigure` 配置类，开始编写配置逻辑。
*   **00:00:30 - 00:00:45**: 讲师在 `LocalAutoConfigure` 类中添加 `@Configuration`、`@Slf4j`、`@EnableConfigurationProperties(FileServerProperties.class)` 和 `@ConditionalOnProperty(name = "pinda.file.type", havingValue = "LOCAL")` 注解，用于条件化配置。
*   **00:00:45 - 00:01:00**: 讲师在 `LocalAutoConfigure` 类中定义 `LocalServiceImpl` 类，并使其继承 `AbstractFileStrategy`。
*   **00:01:00 - 00:01:15**: 讲师在 `LocalServiceImpl` 类中定义 `uploadFile` 方法，参数为 `File` 和 `MultipartFile`，并返回 `null`。
*   **00:01:15 - 00:01:30**: 讲师在 `LocalServiceImpl` 类中定义 `delete` 方法，参数为 `FileDeleteDO`，并添加注释。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲中明确列出了“5.2.3 LocalServiceImpl”章节。
    *   文档中描述了 `LocalServiceImpl` 是 `AbstractFileStrategy` 的子类，负责本地文件的上传和删除。
    *   文档中提到，为了使程序能够动态选择具体的策略处理类，可以提供一个配置类，在配置类中定义 `LocalServiceImpl`。

*   **代码关键内容**:
    *   **配置类 `LocalAutoConfigure`**:
        ```java
        @Configuration
        @Slf4j
        @EnableConfigurationProperties(FileServerProperties.class)
        @ConditionalOnProperty(name = "pinda.file.type", havingValue = "LOCAL")
        public class LocalAutoConfigure {
            // ... (后续代码)
        }
        ```
    *   **策略类 `LocalServiceImpl`**:
        ```java
        public class LocalServiceImpl extends AbstractFileStrategy {
            // 文件上传
            @Override
            public File uploadFile(File file, MultipartFile multipartFile) {
                return null;
            }

            // 文件删除
            @Override
            public void delete(FileDeleteDO fileDeleteDO) {
            }
        }
        ```
    *   **配置属性类 `FileServerProperties`**:
        ```java
        @Data
        public static class Properties {
            private String uriPrefix;
            private String endpoint;
            private String accessKeyId;
            private String accessKeySecret;
            private String bucketName;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：定位与介绍** (00:00:00 - 00:00:05)
    *   讲师首先在左侧的项目结构面板中，通过点击展开“5.2 文件处理策略”下的“5.2.3 LocalServiceImpl”节点，将焦点定位到该章节。
    *   随后，讲师在右侧的代码编辑器中，展示了 `LocalServiceImpl` 类的定义和注释，向观众说明该类的作用是处理本地文件的上传和删除。

*   **场景二：创建配置类** (00:00:15 - 00:00:45)
    *   讲师在代码编辑器中创建了一个名为 `LocalAutoConfigure` 的新类。
    *   讲师依次添加了四个注解：
        1.  `@Configuration`：声明这是一个配置类。
        2.  `@Slf4j`：用于自动导入日志记录功能。
        3.  `@EnableConfigurationProperties(FileServerProperties.class)`：启用对 `FileServerProperties` 配置类的属性绑定。
        4.  `@ConditionalOnProperty(name = "pinda.file.type", havingValue = "LOCAL")`：这是一个条件注解，只有当配置文件中 `pinda.file.type` 的值为 `LOCAL` 时，该配置类才会生效，从而激活 `LocalServiceImpl` 策略。

*   **场景三：定义策略类** (00:00:45 - 00:01:15)
    *   讲师在 `LocalAutoConfigure` 类中，定义了一个名为 `LocalServiceImpl` 的内部类，并使其继承自 `AbstractFileStrategy`。
    *   讲师在 `LocalServiceImpl` 类中，定义了 `uploadFile` 方法，该方法接收一个 `File` 对象和一个 `MultipartFile` 对象作为参数，并返回一个 `File` 对象。
    *   讲师在 `LocalServiceImpl` 类中，定义了 `delete` 方法，该方法接收一个 `FileDeleteDO` 对象作为参数，用于处理文件删除逻辑。

*   **场景四：方法实现** (00:01:15 - 00:01:30)
    *   讲师在 `uploadFile` 方法中添加了 `return null;` 作为占位符实现。
    *   讲师在 `delete` 方法中添加了空的实现体，用于后续开发。

---

以上是根据视频画面进行的结构化分析，旨在帮助理解该技术课程的核心内容和实现过程。
