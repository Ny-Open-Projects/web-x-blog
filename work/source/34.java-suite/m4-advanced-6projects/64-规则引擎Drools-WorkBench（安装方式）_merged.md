# 64-规则引擎Drools-WorkBench（安装方式） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

刚才我们是对workbench做了一个简单的介绍

通过这个介绍我们其实已经知道了

workbench本质上就是一个挖包

我们可以从这个地址去进行下载

下载下来之后就可以得到这么一个文件

你看就是kie-derose-wb.wa

那么下载到这个文件之后

我们接下来就需要来进行安装了

在安装之前我们需要说明一下

软件安装时经常会涉及到软件版本兼容性的问题

所以我们需要明确一下各个软件的使用版本

那么我们本课程使用的软件环境是这样的

操作系统Windows10 64位

然后JDK是1.8

Maven版本是3.5.4

然后Tamcat版本是8.5

这是我们把环境先说明一下

因为什么呢

如果说你环境不一样

按照相同的步骤来安装很有可能会出现问题

所以说

我们需要明确一下我们课上使用的是这种环境

而这种环境的话是我们经过测试没有问题的

具体安装步骤呢

咱们根据这个步骤来操作一下就可以了

首先呢

我们需要来配置Tamcat的环境变量

也就是说我们需要来配置一下这个Catalina Home

对应的值呢

就是Tamcat的安装目录

在我们今天资料里边呢

其实我已经提供了这么一个Tamcat 8.5

这是我们的一个Tamcat

对吧

比如我现在呢

就需要把它安装到我们当前这个Tamcat当中

那我们需要做一个什么事呢

首先来配置啊

这个Catalina Home

那么它所在的

所对应的值呢

就是我们Tamcat的安装目录

那是不是就应该就是当前这个目录

对吧

好

我把它复制一下

然后呢

修改一下咱们这个环境变量啊

好

环境变量

然后呢

在我们这个系统环境变量里边

你看是不是有个Catalina Home

但是呢

我们这是我以前的啊

咱们现在呢

可以给它切换一下

换成我们当前这个目录

OK

确定

这样的话呢

我们第一步是不是就已经操作完成了

就是设置了我们Catalina Home为我们当前这个Tamcat它的安装目录

这第一步

然后第二步呢

咱们需要在Tamcat的bin目录下来创建一个setenv.bat

这么一个文件

其实是个批处理文件

对吧

这个文件的内容呢

就是下面这一段

其实就是设置了一些这个环境变量

对吧

设置了一些环境变量

包括我们这个内存它的开销

然后还有什么呢

就是这个配置

对吧

它指定的

你看就是我们当前这个Tamcat它所在的目录

然后webapp下边

这是不是指的就是我们那个挖包所解压之后的一个目录

好

一会儿呢

咱们是不是需要把这个挖包啊

把它这个扔到我们的Tamcat这个webapp目录下面去

好

呃

这段呢

我们直接抄过来就可以了

那么需要创建这么一个叫做setenv.bat文件

其实在我当前这个Tamcat的这个bin目录下呢

已经提供好了

再来看一下

就是这个叫做setenv.bat

它的这个文件的内容呢

就是我们刚才在讲义上看到的这个内容

是没有变化的

把这段呢

直接抄过来就可以了

好

这是这个bat文件就已经搞定了

然后接下来第三步呢

我们将下载的这个workbench啊

它的挖包改名成这个呃

现在呢

你可以看到我这个其实已经改好名字了

呃

因为什么呢

我初始的刚刚下载下来的时候呢

它这个文件名比较长

后边跟的是版本号啊什么的一堆东西

呃

所以我们现在呢

给它改的短一点就改成这个KIE-DROSE-WB

人说为什么改这个名字呢

如果不改行不行呢

其实不改是不行的

因为什么呢

一会儿我们把它安装到Tamcat啊

当Tamcat启动的时候是不是就会解压

解压之后呢

它就会使用我们这个挖包这个名字作为它这个项目名

对吧

作为它的项目名

而这个项目名呢

刚才在我们这个地方你看是不是已经出现了

哎

如果说你这个解压之后呢

不是这个项目名

它是不是就找不到我们这个文件了

哎

所以说要跟我们这要前后一致

既然你前面写的是这个

那你就需要把这个挖包改成这个名字

这样解压之后呢

正好就是这个名字

它是不是正好这个目录呢

就找到了

好

这是这一步啊

改名这个对吧

这是改名这个

把它改成这个名字

并复制到Tamcat的webapps目录下

好

那接下来呢

咱们把这个已经改好名字的这个挖包复制一下

把它复制到我们Tamcat的这个webapps

这个目录下

直接粘到这儿来

好

这就弄过来了

考过来之后呢

接下来咱们需要来修改一下Tamcat的这个

config目录下的这个Tamcat-user

这个目录下的这个Tamcat-user

这个目录下的这个Tamcat-user

配置文件

这里边呢

配置的是关于我们Tamcat服务器的一些角色

还有用户信息

好

咱们先找到这个文件

Tamcat-config

下面是不是有一个叫做Tamcat-users

这个文件

然后呢

我们打开它来看一下

好

这里边呢

你看我其实提前已经改好了

默认情况下

这里边是没有这个东西的

我们是加了这么一个角色的标签

Row是不是就是角色的意思

然后呢

角色的名字叫Admin

然后呢

我们又提供了一个user

一个用户的配置

然后它的username叫KIE

password也是KIE

它的角色就是我们上面定义的这个Admin角色

OK

这个跟咱们的讲义是一致的

就是这样的

咱们把这段拿过来

因为它这个是带有注释的

这个是定义Admin角色

下面这个是定义用户

对吧

用户名是KIE

密码也是KIE

对应的角色就是上面定义的Admin角色

OK

这样的话

我们这个Tamcat-users呢

我们可以看到呢

这个文件是不是也就改造好了

改造好之后呢

还要去下载三个架包

这三个架包呢

你可以从Maven的官方网站去下载

我这呢其实已经下载好了

在我们今天资料里边

我已经准备好了

就是这么三个架包

好

那么我们需要把这三个架包干什么呢

把它复制到Tamcat的lib目录下

好

咱们把这三个架包啊

来复制一下

复制到我们刚才这个Tamcat

这个Tamcatlib目录下

好

来覆盖一下

那么这一步就已经搞定了

这是把我们的三个架包

把它复制到Tamcatlib目录下

好

其实你可以看一下

这个KIE-Tamcat-integration

一看这个名字也能知道

这是KIE啊

跟我们Tamcat做集成的一个架包

然后这个呢是关于安全的

对吧

这个是关于日志的

好

把这三个架包呢都拷过去就可以了

然后接下来呢

我们来修改一下Tamcat的这个config目录下

server.channel文件

添加这么一个标签

内容呢就是下面这个内容

而指定的其实你会发现这是一个类名对不对

而这个类在哪呢

就在我们刚才拷进来的这个架包里边

就在这个架包里边是这么一个类

咱们打开Tamcat

config目录

然后呢找到什么呢

找到我们这个server.channel

对吧

找到这个文件

然后这里面呢

其实我是应该是已经提前配置好了

咱们直接来看一下就可以了

来找一下

在这个位置

大家看

就这么value

这么一个标签

对吧

把它呢直接拷过来就可以了

我这个呢因为是提前准备好的

所以其实都已经拷完的

那么你可以按照我呢讲义上来操作

需要注意的就是这个位置啊

这个位置不要搞错了

你看它是在什么位置啊

因为Tamcat它自带的是不是有这么一个标签

然后呢你在它这个下面呢

紧按着它来加这个标签就可以了

这个标签的层次呢不要写错了啊

一定要放在相应的这个位置上

好

这一步呢我们也就做完了

这些步骤呢其实都是比较固定的

好

那么这些操作都做完之后呢

接下来呢我们就可以来启动咱们的Tamcat了

启动完之后呢

我们就可以来访问这个地址

当然这个端口号呢

你的Tamcat不一定是8080对吧

那么需要根据你实际啊

启动的这个Tamcat的端口号来

我当前这个呢就是默认的8080这个端口

而我们这个项目名呢

其实就是我们这个名字

ke-derose-wb

为什么是这个呢

就是因为我们当前在这个webapps下边

这个挖包是不是叫这个名字

所以它解压之后呢

用的就是我们前面这个名字

好那接下来呢咱们来启动一下

直接在并目录下边

双击这个什么呢

startup

好

它现在正在启动

启动的过程当中呢

它就会给我们进行解压对不对

看它就会解压我们这个挖包

咱们呢可以直接到我们的webapps下边来

你看它现在是不是已经解开了

但这个启动的是需要有一段时间的

因为这个工程呢还是比较大的

所以需要有一定的这个时间

我们耐心等待一下

好的

现在呢我们这个工程呢已经启动成功了

启动成功之后呢

咱们接下来呢就可以来

访问一下我们这个地址

好

我们打开一个浏览器页面

然后呢我们来访问一下这个地址

大家来看

好现在呢你看我们是不是就访问到了这么一个页面

然后呢用户名呢是KIE

密码呢也是KIE

好

然后直接点这个登录按钮进来

稍微等待一下

好

那么如果你看到这个欢迎界面呢

这就说明啊我们这个WB啊

我个bench已经安装成功了

好

咱们这边呢也都有提示

如果你看到这个欢迎页面

到这儿的话呢我们这个安装就已经搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一个关于如何在 Windows 10 系统上安装和配置 **Drools WorkBench** 的技术教程。教程的核心是将 Drools WorkBench（一个用于开发和管理业务规则的 Web 应用）部署到 Apache Tomcat 服务器上。视频详细演示了从准备环境（如设置环境变量、下载必要的 JAR 包）、修改 Tomcat 配置文件（`server.xml` 和 `tomcat-users.xml`），到最终启动服务器并访问 WorkBench 登录页面的完整流程。整个过程旨在指导开发者或系统管理员成功部署 Drools WorkBench。

---

### 2) 按时间顺序的章节（带时间点）

由于无法提供精确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:15**: **环境准备与介绍**。画面显示了 `Drools` 文件夹，其中包含 `apache-tomcat-8.5.24`、`kie-drools-web.war`、`setenv.bat` 等关键文件，以及 `javax.security.jacc-api-1.5.jar`、`kie-tomcat-integration-7.10.0.Final.jar` 等 JAR 包。讲师介绍了本课程将使用 Windows 10 64位系统、JDK 1.8、Maven 3.5.4 和 Tomcat 8.5。
*   **00:16 - 00:30**: **配置 Tomcat 环境变量**。画面切换到“系统属性”窗口，讲师演示了如何设置 `CATALINA_HOME` 环境变量，指向 Tomcat 的安装目录。
*   **00:31 - 00:45**: **创建 `setenv.bat` 文件**。讲师在 Tomcat 的 `bin` 目录下创建并编辑 `setenv.bat` 文件，配置 `CATALINA_OPTS` 环境变量，以支持 Drools WorkBench 的运行。
*   **00:46 - 01:00**: **修改 `tomcat-users.xml` 文件**。讲师使用 Notepad++ 打开 `conf/tomcat-users.xml` 文件，添加了用于登录 WorkBench 的用户和角色配置。
*   **01:01 - 01:15**: **修改 `server.xml` 文件**。讲师在 `conf/server.xml` 文件中，定位到 `<Host>` 标签内，添加了 `<Valve className="org.kie.integration.tomcat.JACCValve"/>` 标签，以启用 Drools WorkBench 的 JACC（Java Authorization Contract for Containers）安全功能。
*   **01:16 - 01:30**: **复制 JAR 包并启动服务**。讲师将下载的三个 JAR 包（`kie-tomcat-integration-7.10.0.Final.jar`、`javax.security.jacc-api-1.5.jar`、`slf4j-api-1.7.25.jar`）复制到 Tomcat 的 `lib` 目录下。然后，通过双击 `startup.bat` 文件启动 Tomcat 服务器。
*   **01:31 - 01:45**: **访问 WorkBench**。讲师在浏览器中访问 `http://localhost:8080/kie-drools-web.wb`，成功打开了 WorkBench 的登录页面，并使用之前配置的用户名和密码登录。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **环境要求**: Windows 10 64位, JDK 1.8, Maven 3.5.4, Tomcat 8.5。
    *   **安装步骤**:
        1.  设置 `CATALINA_HOME` 环境变量。
        2.  在 `bin` 目录下创建 `setenv.bat` 文件，并配置 `CATALINA_OPTS`。
        3.  将 `kie-drools-web.war` 包重命名为 `kie-drools-web.war` 并复制到 `webapps` 目录。
        4.  修改 `conf/tomcat-users.xml` 文件，添加用户和角色。
        5.  修改 `conf/server.xml` 文件，添加 `<Valve className="org.kie.integration.tomcat.JACCValve"/>`。
        6.  将三个 JAR 包复制到 `lib` 目录。
        7.  启动 Tomcat 并访问 `http://localhost:8080/kie-drools-web.wb`。

*   **关键代码/配置**:
    *   **`setenv.bat` 文件内容**:
        ```bash
        CATALINA_OPTS="-Xmx512M \
        -Djava.security.auth.login.config=$CATALINA_HOME/webapps/kie-drools-wb/WEB-INF/classes/login.config \
        -Dorg.jboss.logging.provider=jdk"
        ```
    *   **`tomcat-users.xml` 文件内容**:
        ```xml
        <role rolename="admin"/>
        <user username="kie" password="kie" roles="admin"/>
        ```
    *   **`server.xml` 文件内容**:
        ```xml
        <Valve className="org.kie.integration.tomcat.JACCValve"/>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境准备**。讲师在文件资源管理器中展示了 `Drools` 文件夹，重点指出了 `apache-tomcat-8.5.24`、`kie-drools-web.war` 和 `setenv.bat` 等文件，说明了这些是部署所需的组件。
*   **场景二：配置环境变量**。讲师在“系统属性”窗口中，点击“环境变量”，在“系统变量”中新建或修改 `CATALINA_HOME`，并将其值设置为 Tomcat 的安装路径。
*   **场景三：创建并编辑 `setenv.bat`**。讲师在 Tomcat 的 `bin` 目录下，右键新建文本文档并重命名为 `setenv.bat`，然后用记事本打开，粘贴并保存了配置 `CATALINA_OPTS` 的代码。
*   **场景四：修改 `tomcat-users.xml`**。讲师使用 Notepad++ 打开 `conf/tomcat-users.xml` 文件，将光标定位到 `<tomcat-users>` 标签内，添加了 `<role rolename="admin"/>` 和 `<user username="kie" password="kie" roles="admin"/>` 两行代码。
*   **场景五：修改 `server.xml`**。讲师在 `conf/server.xml` 文件中，将光标移动到 `<Host>` 标签内，添加了 `<Valve className="org.kie.integration.tomcat.JACCValve"/>` 标签。
*   **场景六：启动并访问**。讲师双击 `bin` 目录下的 `startup.bat` 文件启动 Tomcat 服务器。随后，在浏览器中输入 `http://localhost:8080/kie-drools-web.wb`，成功打开了 WorkBench 的登录页面，并演示了登录过程。
