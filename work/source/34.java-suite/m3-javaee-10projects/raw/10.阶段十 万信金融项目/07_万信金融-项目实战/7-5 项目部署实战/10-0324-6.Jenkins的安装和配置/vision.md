# 画面线理解：6.Jenkins的安装和配置

- 阶段：10.阶段十 万信金融项目
- 章节：07_万信金融-项目实战/7-5 项目部署实战
- 源文件：10.阶段十 万信金融项目\07_万信金融-项目实战\7-5 项目部署实战\6.Jenkins的安装和配置_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 02:12, 03:52, 05:41, 06:36, 07:05, 07:53, 08:45, 09:09, 09:47, 10:52, 12:05, 12:39, 13:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:01:38

1) 这一组画面整体在讲什么（一句话）：
讲解如何搭建持续集成环境，包括安装 Gogs 作为 Git 仓库、安装 Jenkins 作为 CI 工具、配置 Jenkins 全局工具以及创建构建任务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档“3.2 搭建持续集成环境”，重点在“3.2.1 安装 Git/Gogs”章节，介绍 Gogs 作为 Git 仓库的优势和安装方法。
画面 2: 展示 PDF 文档“3.3 创建持续集成任务”，重点在“3.3.1 创建构建任务”章节，介绍创建万信金融的构建任务。
画面 3: 展示 Jenkins 的“解锁 Jenkins”页面，提示管理员密码位于 `/var/jenkins_home/secrets/initialAdminPassword`，并提供获取密码的命令。
画面 4: 与画面 1 内容相同，再次强调“3.2.1 安装 Git/Gogs”章节内容。
画面 5: 展示 Jenkins 主界面的“系统设置”、“全局安全配置”、“凭据配置”、“全局工具配置”、“读取设置”和“插件管理”等主要功能模块。
画面 6: 展示 Jenkins 插件管理页面，列出多个可用插件，如 CCM、FxCode Runner、MSBuild、MSTestRunner、NUnit、PowerShell、Videoban 等。
画面 7: 展示 Jenkins 插件管理页面，列出已安装的插件，如 Artifactory、Authentication Tokens API Plugin、Branch API、Build Timeout、Command Agent Launcher、Credentials、Credentials Binding、Display URL API 等。
画面 8: 展示 Jenkins 插件管理页面，列出已安装的插件，如 Generic Webhook Trigger、Git、Git client、Git server、GitHub、GitHub API Plugin、GitHub Branch Source、Gogs plugin、Gradle、Infrastructure plugin for Publish Over X、Jackson 2 API、JavaDoc Plugin、JavaRector GUI Lib ACE Editor bundle plugin 等。
画面 9: 展示 Jenkins 主界面，突出“Manage Jenkins”选项。
画面 10: 展示 Jenkins “全局工具配置”页面，配置 Maven 和 JDK。
画面 11: 展示 Jenkins “全局工具配置”页面，配置 Maven 和 JDK，其中“文件路径”字段被选中。
画面 12: 展示 PDF 文档“3.3.1 创建构建任务”，突出“新建任务”选项。
画面 13: 展示 Jenkins “系统”页面，列出“全局凭据”、“凭据”、“系统”、“锁存资源”、“构建队列”、“构建执行状态”等选项。
画面 14: 展示 PDF 文档“Jenkins 安装文档”，介绍如何配置 JDK 和 Git。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```
docker exec -it jenkins /bin/bash
cat /var/jenkins_home/secrets/initialAdminPassword
```

画面 10:
```
默认 settings 文件
文件路径: /home/apache-maven-3.6.3/conf/settings.xml
默认 settings 文件
文件路径: /home/apache-maven-3.6.3/conf/settings.xml
```

画面 14:
```
JDK 版本
JDK 版本
JAVA_HOME: /usr/local/jdk-1.8.0_212
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“3.2 搭建持续集成环境”，子标题“3.2.1 安装 Git/Gogs”。
画面 2: PPT 标题为“3.3 创建持续集成任务”，子标题“3.3.1 创建构建任务”。
画面 5: Jenkins 主界面功能模块包括“系统设置”、“全局安全配置”、“凭据配置”、“全局工具配置”、“读取设置”和“插件管理”。
画面 6: 插件管理页面列出多个插件，如 CCM、FxCode Runner、MSBuild、MSTestRunner、NUnit、PowerShell、Videoban 等。
画面 7: 插件管理页面列出已安装的插件，如 Artifactory、Authentication Tokens API Plugin、Branch API、Build Timeout、Command Agent Launcher、Credentials、Credentials Binding、Display URL API 等。
画面 8: 插件管理页面列出已安装的插件，如 Generic Webhook Trigger、Git、Git client、Git server、GitHub、GitHub API Plugin、GitHub Branch Source、Gogs plugin、Gradle、Infrastructure plugin for Publish Over X、Jackson 2 API、JavaDoc Plugin、JavaRector GUI Lib ACE Editor bundle plugin 等。
画面 9: Jenkins 主界面突出“Manage Jenkins”选项。
画面 10: Jenkins “全局工具配置”页面，配置 Maven 和 JDK。
画面 12: PPT 标题为“3.3.1 创建构建任务”，突出“新建任务”选项。
画面 13: Jenkins “系统”页面，列出“全局凭据”、“凭据”、“系统”、“锁存资源”、“构建队列”、“构建执行状态”等选项。
画面 14: PDF 文档“Jenkins 安装文档”，介绍如何配置 JDK 和 Git。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
