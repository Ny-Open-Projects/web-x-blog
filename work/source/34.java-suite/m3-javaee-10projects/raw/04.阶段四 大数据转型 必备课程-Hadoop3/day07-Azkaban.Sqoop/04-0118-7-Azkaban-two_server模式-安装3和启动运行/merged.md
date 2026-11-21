# 7-Azkaban-two_server模式-安装3和启动运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\7-Azkaban-two_server模式-安装3和启动运行【海量资源尽在 ubkz.com】.mp4
- 时长 6分6秒（音频 366s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来继续对这个阿兹卡版进行配置好回到讲义在这里呢我们刚才呢做到第几步呢我们做到第五步我们来看第六步第六步的话呢我们需要去安装一个插件什么做呢首先将我们编译后生成的这么execute as users.c拷贝到这个目录那我们先去找到这个文件好这个文件在哪里呢
[00:27] 编译完之后应该是在我们export serviceadk 3.5.这个主目录下面有一个az exe utilsaz exe utils我们来看一下这个目录在这个目录下面有一个srcsrc目录src下面有一个mint这个mint下面有个c
[00:59] 这个C里边呢就这个文件好我们现在在这个目录我需要把它拷到哪里去呢我们来看一下我需要将这个文件拷贝到拷贝到这个地方阿兹卡班3.5 51.0这个目录那我直接把它复制一下来把这个路径复制一下我要拷贝到这个job types这个目录好我们来cp sc.c拷贝到这个目录好拷贝进去那我再进到这个目录
[01:30] 我要进去粘贴走我现在就在这里在这里的话呢你看这里边有一个这么一个文件就是我刚才拷贝过来的接下来干什么事情呢我们来看好接下来呢我们需要在这个目录下面就先进到这个目录进到这个目录之后呢我们先装一个gcc++然后呢将我们刚才这个c程序啊编译成一个目标文件来我们来先安装这个
[01:59] 来先安装这个gccc加加一个编译器稍等它这个地方提醒呢说我已经安装过了OK那我已经安装过了那接下来我们来继续安装完之后呢我们进到这个目录我现在已经在这个job types目录了接下来将我们这个c文件通过gccc编译器这是一个编译器啊-o表示生成一个目标文件也就是这个文件是一个二进制文件我们把它编一下来在这里我们来编一下走
[02:33] 好编译完之后呢它就生成了一个这么一个可执行文件那么接下来呢我们需要给它改一个所属用户所属用户给它改成把这个文件的所属用户改成root改完之后呢我们还要给它加一个权限这个权限呢叫清洁MOD6050给它添加一个所属的权限OK好权限加完了加完之后我们再来看一下你会发现它变成红色这是一个特殊的权限OK
[03:04] 那么有了这个权限之后呢我们来进行第七步那么对这个地方呢修改对这个executeSummon呢修改配置文件怎么修改呢我们进到这个目录我们现在已经在这个目录了直接打开这个文件然后呢在这里边加上这几句话我们来看一下好在这里呢有一个文件叫common-predative这个进入进来好进来之后呢我们需要加一些内容那怎么配呢
[03:34] 我们来看我们来把讲义上的这三句话把这三句话第一句话应该应该拥有了来我们把它复制一下来看一下把这个呢直接粘贴到我们这里那第一句话拥有了把它删掉好这个地方呢表示跳过内存检查而这个地方呢表示我本地库的位置呢是在这个目楼下面OK也就是我当前所在的目楼来我们来保存退出
[04:03] 那么到现在为止呢我们基本上把AzureKarban的配置已经做完了做完之后呢我们来看一下下一步的一个操作我们接下来呢可以启动我们的AzureKarban怎么启动呢我们先进到这个ESC Server来启动这个ESC Server我们来进来来在这里呢我们进到这里边我们启动怎么启动呢在这里呢并目录下面有一个有一个什么叫startesc.sh来看一下startesc.sh我们来
[04:33] 做一个start esh走ok已经启动了启动完之后呢我们再来启动我们需要激活我们的esh server在任意一个目录下面呢运行这个命令ok激活走一下回程它出现这个success表示激活成功那接下来呢我们还要去启动我们的这个web server好进到这个web server下面我们来做一下好那这个地方呢在bin下面有一个start
[05:04] webserver.shOK到此的话呢我们基本上把我们的webserver和esc server都启动成功了那怎么去验证能否使用呢我们来看我们需要在这个浏览器里边输入一个https记着是https然后呢node03后面跟上8443我们来看一下在这里我加一下我们来看https好这地方是node03
[05:32] 然后呢8443好回车这个时候你看它呢直接就跳到这个登录页面跳到这个登录页面之后呢我们可以输入我们的用户名和密码用户名是阿兹卡班密码呢阿兹卡班好我们来登录好登录之后呢大家就看到了这个界面那么到此为止呢我们一个to server模式它的一个安装呢已经结束了OK那么关于
[06:02] 这个安装模式我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

