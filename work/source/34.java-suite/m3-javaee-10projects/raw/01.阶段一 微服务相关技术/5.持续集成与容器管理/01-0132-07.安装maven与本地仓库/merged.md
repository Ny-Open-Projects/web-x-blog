# 07.安装maven与本地仓库

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\07.安装maven与本地仓库_【海量资源尽在 ubkz.com】.mp4
- 时长 6分23秒（音频 383s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们来进行全局工具配置那么在这一步我们主要分两部分第一我们先安装Maven与本地仓库刚才我们安装了一个叫Maven的插件实际上这个插件是什么呢就是Jax之所以能够实现持续集成其实主要就是调用这个Maven插件通过调Maven插件来执行一个Maven的命令
[00:28] 来达到这么一种集成的效果那么这个Maven命令呢就是我们在第一个环节所讲的这个Docker的用Docker Maven插件来实现的那么这样一来呢我们就可以通过一个Maven命令将我们当前的微服务部署到Docker里但是我们说Maven插件本身并不是Maven它只是Maven的一个入口所以说真正执行的还是Maven软件本身这就要求我们必须要在我们的服务器上
[00:58] 安装Maven的安装包我已经给大家提供了是Maven3.5.4的这么一个版本首先咱们给他上传到我们的服务器上我们先给他先放到一个目录下好了放到这儿然后接下来我们现在去上传put地盘的地盘的setup下的什么apache
[01:31] 然后这是3.5.4,APAC M1,3.5.4上传这个传上之后接下来我们怎么办我们就可以将其解压我来看一下这个是在这儿这时候我们通过p2,zx,zx,vf然后我们给它解压开解压之后这里会出了这么一个目录叫
[02:09] apache maven 3.5.4我们现在就需要把给它转移到一个目录之下给它移动到local下的maven目录给它进行一个转移然后我们移动到usr的local下的maven这时候我们就转移成功了转移成功之后接下来我们来看一下这时候我们需要去配置我们的配置文件maven的配置文件我们需要配置
[02:44] 这时候咱们看一下先进到这个目录里local maven然后我们这里头进到config下config有一个settings我们编辑编辑的话找到我们的本地仓库的配置在这有个本地仓库配置我们可以这样把这句话复制到外面然后我们去修改一下这个目录修改成什么
[03:23] 修改成usrlocal下的reposteryrepostery好我们就给它定义为这个目录修改完成之后我们现在wq退出现在就已经完成了配置文件的更改那么完成配置文件更改本地仓库现在是空的我们需要怎么办我们需要把本地仓库上传到服务器上
[03:57] 其实我们这一步不做也行但是呢会存在什么问题呢存在存在存在你在持续集成的执行过程中会比较慢因为本地仓库是没有东西的他所有需要依赖的账号都要重新下载那么如果说我把本地的这个仓库传上去那这个时候呢我们会节省一些这个他持续集成的所花费的时间啊所以说我们要把本地的给他传上去啊呃那这个时候一样啊我们需要去
[04:28] 看一下本地仓库是在这个目录就是repositoryboot这个目录下我们现在把它上传上去地盘的repositoryboot这个目录这个是个目录所以说就加-2现在它正在上传这个时间可能会长一些上传完成,完成之后
[05:27] 我们看一下到底有没有上传成功,这有一个repository boot然后我们现在就可以把它给它转到usr local repository这个目录之下那怎么做mv repository boot然后是usr local下的repository这个目录
[06:01] 好咱们现在呢这个回车回来之后呢我们现在看一下到底有没有转移成功啊好现在呢这个仓库呢都有了好这是我们就完成了Maven软件的安装以及本地仓库的这么一个上传

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Linux 服务器上安装 Maven 并配置本地仓库，以实现离线构建。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示 Typora 文档，内容为“2.5 全局工具配置”章节，其中“2.5.1 安装Maven与本地仓库”部分列出了安装步骤，包括解压命令 `tar zxvf apache-maven-3.5.4-bin.tar.gz` 和移动目录命令 `mv apache-maven-3.5.4 /usr/local/maven`。
画面 2: 同画面 1，内容一致。
画面 3: 同画面 1，内容一致。
画面 4: 显示 Windows 桌面，有“传智播客”和“黑马程序员”的联合出品标志。
画面 5: 显示 SecureCRT 连接的 Linux 服务器终端，执行了 `mv apache-maven-3.5.4 /usr/local/maven` 命令，成功移动了 Maven 文件夹。
画面 6: 显示 SecureCRT 终端，内容为 Maven 的 `settings.xml` 配置文件的说明，包括用户级和全局级配置路径。
画面 7: 显示 SecureCRT 终端，内容为 Maven 的 `settings.xml` 配置文件的详细内容，包括 `localRepository`、`interactiveMode` 和 `offline` 等配置项。
画面 8: 显示 Windows 资源管理器，浏览文件夹，选中了 `repository_boot` 文件夹。
画面 9: 显示 Windows 资源管理器，浏览文件夹，选中了 `repository_boot` 文件夹。
画面 10: 显示 SecureCRT 终端，正在上传 Maven 仓库的文件，如 `maven-plugin-parameter-documenter-2.1.1.pom`。
画面 11: 显示 SecureCRT 终端，正在上传 Maven 仓库的文件，如 `maven-plugin-registry-2.0.8.jar`。
画面 12: 显示 SecureCRT 终端，正在上传 Maven 仓库的文件，如 `maven-plugin-registry-2.2.0.pom`。
画面 13: 显示 SecureCRT 终端，内容为 Maven 的 `settings.xml` 配置文件的说明，包括用户级和全局级配置路径。
画面 14: 显示 Typora 文档，内容为“2.5 全局工具配置”章节，其中“2.5.1 安装Maven与本地仓库”部分列出了安装步骤，包括解压命令 `tar zxvf apache-maven-3.5.4-bin.tar.gz` 和移动目录命令 `mv apache-maven-3.5.4 /usr/local/maven`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
(1) 将Maven压缩包上传至服务器（虚拟机）
(2) 解压
tar zxvf apache-maven-3.5.4-bin.tar.gz
(3) 移动目录
mv apache-maven-3.5.4 /usr/local/maven
(4) 编辑setting.xml配置文件 vi /usr/local/maven/conf/settings.xml，配置本地仓库目录，内容如下
<localRepository>/usr/local/repository</localRepository>
(5) 将开发环境的本地仓库上传至服务器（虚拟机）并移动到/usr/local/repository 。
mv repository_boot /usr/local/repository
```

画面 6:
```
This is the configuration file for Maven. It can be specified at two levels:
1. User Level. This settings.xml file provides configuration for a single user,
and is normally provided in $user.home/.m2/settings.xml.
NOTE: this location can be overridden with the CLI option:
-s /path/to/user/settings.xml
2. Global Level. This settings.xml file provides configuration for all Maven
users on a machine (assuming they're all using the same Maven
installation). This file is normally provided in
$Maven.conf/settings.xml.
NOTE: this location can be overridden with the CLI option:
-gs /path/to/global/settings.xml
```

画面 7:
```
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
http://maven.apache.org/xsd/settings-1.0.0.xsd">
<localRepository>/usr/local/repository</localRepository>
<interactiveMode>true</interactiveMode>
<offline>false</offline>
<pluginGroups>
This is a list of additional group identifiers that will be searched when resolving plugins by their prefix, i.e.
when invoking a command like "mvn prefix:goal". Maven will automatically add the group identifiers
"org.apache.maven.plugins" and "org.codehaus.mojo" if these are not already contained in the list.
</pluginGroups>
```

画面 13:
```
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
http://maven.apache.org/xsd/settings-1.0.0.xsd">
<localRepository>/usr/local/repository</localRepository>
<interactiveMode>true</interactiveMode>
<offline>false</offline>
<pluginGroups>
This is a list of additional group identifiers that will be searched when resolving plugins by their prefix, i.e.
when invoking a command like "mvn prefix:goal". Maven will automatically add the group identifiers
"org.apache.maven.plugins" and "org.codehaus.mojo" if these are not already contained in the list.
</pluginGroups>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

