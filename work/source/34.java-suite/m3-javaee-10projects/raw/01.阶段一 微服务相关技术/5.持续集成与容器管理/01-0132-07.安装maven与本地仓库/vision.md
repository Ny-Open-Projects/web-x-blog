# 画面线理解：07.安装maven与本地仓库

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\07.安装maven与本地仓库_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:01, 01:16, 02:13, 02:34, 02:50, 03:03, 03:47, 04:30, 04:37, 05:10, 05:17, 05:21, 06:04, 06:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:19:19

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
