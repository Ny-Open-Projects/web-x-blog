# 画面线理解：7-Azkaban-two_server模式-安装3和启动运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\7-Azkaban-two_server模式-安装3和启动运行【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:27, 00:54, 01:08, 01:37, 02:12, 02:47, 03:05, 03:38, 04:19, 04:35, 04:53, 05:15, 05:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 09:23:22

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 环境下安装并配置 Azkaban Executor Server，包括添加插件、编译源码、修改配置文件和启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Azkaban Executor Server 安装步骤的文档，重点在“添加插件”步骤，包含将 execute-as-user.c 文件复制到指定目录的命令。
画面 2: 显示终端窗口，执行了 `cd /export/servers/azkaban-exec-server-3.51.0/plugins/jobtypes` 命令，准备进行后续操作。
画面 3: 终端窗口显示在 az-exe-util 目录下执行 `ls` 和 `cd src` 命令，但提示 `cd: src: No such file or directory`，随后尝试 `s` 命令失败，最终进入 `src` 目录。
画面 4: 展示文档，内容与画面 1 相同，强调将文件复制到指定目录。
画面 5: 终端窗口显示在 jobtypes 目录下，执行 `ls` 命令，确认 `execute-as-user.c` 文件存在。
画面 6: 展示文档，内容与画面 1 相同，强调将文件复制到指定目录。
画面 7: 终端窗口显示执行 `yum -y install gcc-c++` 安装编译环境，然后执行 `gcc execute-as-user.c -o execute-as-user` 编译文件，最后执行 `chown root execute-as-user` 修改文件所有者。
画面 8: 展示文档，内容与画面 1 相同，强调将文件复制到指定目录。
画面 9: 展示文档，内容为“修改配置文件”，并列出 `cd /export/servers/azkaban-exec-server-3.47.0/plugins/jobtypes` 命令，以及 `vim commonprivate.properties` 命令。终端窗口显示 `ls` 命令列出文件，包括 `execute-as-user` 和 `execute-as-user.c`。
画面 10: 终端窗口显示编辑后的 `commonprivate.properties` 文件内容，包含 `execute.as.user=false` 和 `memCheck.enabled=false` 两行配置。
画面 11: 终端窗口显示在 Azkaban Executor Server 的 bin 目录下，执行 `ls` 命令列出 `start-exec.sh` 等文件。
画面 12: 展示文档，内容为“启动服务”，包括“第一步：启动 azkaban exec server”和“第二步：激活我们的 exec-server”命令，以及“第三步：启动 azkaban-web-server”命令。
画面 13: 展示文档，内容为“启动服务”，包括“第一步：启动 azkaban exec server”和“第二步：激活我们的 exec-server”命令，以及“第三步：启动 azkaban-web-server”命令。
画面 14: 浏览器窗口显示 Azkaban Web Client 的登录页面，地址为 `https://node03:8443`，页面提示“Click Create Project to create a new project”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
Step 6: azkaban executor server 安装 第二步: 添加插件
将我们编译好的c文件execute-as-user.c
上传到这个目录来/export/servers/azkaban-exec-server-3.51.0/plugins/jobtypes
或者直接将我们/export/software下面的文件拷贝过来也行

然后执行以下命令生成execute-as-user

1 yum -y install gcc-c++
2 cd /export/servers/azkaban-exec-server-3.51.0/plugins/jobtypes
3 gcc execute-as-user.c -o execute-as-user
4 chown root execute-as-user
5 chmod 6650 execute-as-user
```

画面 6:
```
Step 7: azkaban executor server 安装 第三步: 修改配置文件
修改配置文件

1 cd /export/servers/azkaban-exec-server-3.47.0/plugins/jobtypes
```

画面 9:
```
Step 7: azkaban executor server 安装 第三步: 修改配置文件
修改配置文件

1 cd /export/servers/azkaban-exec-server-3.47.0/plugins/jobtypes
2 vim commonprivate.properties
3 execute.as.user=false
4 memCheck.enabled=false
5 azkaban.native.lib=/export/servers/azkaban-exec-server-3.51.0/plugins/jobtypes
```

画面 10:
```
execute.as.user=false
memCheck.enabled=false
azkaban.native.lib=/export/servers/azkaban-exec-server-3.51.0/plugins/jobtypes
```

画面 12:
```
Step 7: 启动服务
第一步: 启动azkaban exec server

1 cd /export/servers/azkaban-exec-server-3.51.0
2 bin/start-exec.sh

第二步: 激活我们的exec-server
node03机器任意目录下执行以下命令

1 curl -G "node03:$(./executor.port)/executor?action=activate" && echo

第三步: 启动azkaban-web-server

1 cd /export/servers/azkaban-web-server-3.51.0/
2 bin/start-web.sh

访问地址:
https://node03:8443
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“Step 6: azkaban executor server 安装 第二步: 添加插件”。
画面 6: PPT 标题为“Step 7: azkaban executor server 安装 第三步: 修改配置文件”。
画面 12: PPT 标题为“Step 7: 启动服务”，包含三个步骤：第一步、第二步、第三步。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
