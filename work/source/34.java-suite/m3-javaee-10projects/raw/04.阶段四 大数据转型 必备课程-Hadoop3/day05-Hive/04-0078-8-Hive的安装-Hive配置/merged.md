# 8-Hive的安装-Hive配置

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\8-Hive的安装-Hive配置【海量资源尽在 ubkz.com】.mp4
- 时长 4分23秒（音频 264s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来呢我们来配置Hive那么首先要配置Hive even.sh这个文件来打开我们的进到我们刚才的这个apacheexport serviceapache然后呢Hive 1.1.1在这里边呢有一个configure目录好在这里边呢我们要配置要配置这个Hive inv那这个Hive inv呢它有个模板文件我们要拷贝一个出来
[00:30] Hive env然后呢我来配一个Hive env好把后面那个点template的删掉好在这里我们打开Hive env打开之后呢我们在这里需要配置几个参数向下翻第一个呢是我们Hadoop的一个位置向下翻啊是这个Hadoop的一个home那这个Hadoop home呢我们要去指定我们Hadoop的一个位置
[01:02] 我克隆一个绘画出来稍等没有打开那这样我来再退出一下我来保存退出一下稍等好保存退出之后呢我们来看一下Export Service一个Hadoop 3.3.1就这个目录我把它拷过来保证它不会出错好我们再来再来之后呢记着把后面这个呢给它替换掉好替换掉
[01:44] 替换调完之后呢还有一个叫Hive的一个配置目录叫Hive的configure目录这个我们要去收拾一下这个configure目录呢其实就是我们当前的这个目录也就这个目录好我们再来把它也配一下好配置完了之后呢基本上这两个呢就搞定了好这个文件就配置结束了那配置完了之后呢还有下一个文件叫Hive set的插面来我们来看
[02:15] 我们看一下当前有没有have set的插面没有没有的话我们新建一个have set.插面好这个文件里边呢我们需要将刚才这个插面中所有的数据呢直接拷贝过来就行了直接拷贝过来好直接粘粘的时候不要多粘也不要少粘OK简单解释一下大家简单看一下在这个位置呢
[02:49] 配的是我们连接数据库的一个用户名这个是数据库的一个密码这个是数据库的一个位置在node03 3306他说呢呃这个有个Hive数据库如果说你不存在那他就会自动创建好那下面呢是我们的一个mycircle的一个驱动一个驱动再向下看好别的的话我们采用默认值就可以了好
[03:19] 那这个呢我们就配好了这个地方呢你可以改成node03就是你的主机名啊如果没有配这个node03.hardop.com你可以写成node03好那我们就配好了配好之后我们保存退出保存退出之后呢还有一件事情要去做我们还要将mycircle的连接驱动包放在Hive的一个lab目楼下面这里呢需要准备一个mycircle的驱动包我呢可以直接把它放在Hive下面
[03:49] 这个驱动包呢我已经放在桌面上了我直接把它拿过来好咱们回到上一集回到这个lab下面我们来看一下把这个驱动包从桌面上桌面在这里有一个myserver5.5.18好把它拿过来好放在这里好放在这里之后呢基本上我们的整个的Hive呢就配好了整个的这个Hive配好了配好之后呢我们就可以来做一些测试
[04:19] 好那么关于Hive的一个配置呢我就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Linux 系统中配置和修改 Hive 环境变量文件 Hive-env.sh，以适配 Hadoop 环境并调整 JVM 堆内存大小。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了课程视频的抽帧画面，左侧是课程目录结构，包含“Hive 基础”、“Hive 的元数据管理”等章节。
- 右侧是文本编辑器，显示了“第三步：修改Hive的配置文件”和“第四步：进入mysql的客户端然后进行授权”的说明。
- 文本编辑器中包含以下代码：
  ```
  grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;
  flush privileges;
  ```
- 同时显示了两个 SecureCRT 会话窗口，分别连接到 192.168.174.120 和 192.168.174.120（第二个窗口为未激活状态）。

画面 2：
- 展示了 SecureCRT 会话窗口，用户在节点 node03 上执行了命令：
  ```
  [root@node03 ~]# ls /export/servers/
  apache-Hive-3.1.1-bin/ Hadoop-3.1.1/ JDK 8.0_141/ ZooKeeper-3.4.9/
  [root@node03 ~]# cd /export/servers/apache-Hive-3.1.1-bin/
  [root@node03 conf]# ls
  bin  binar-package  licenses  conf  examples  hostlog  jdb  lib  LICENSE  NOTICE  RELEASE_NOTES.txt  script
  beeline-log4j2.properties  Hive-default.xml.template  Hive-env.sh.template  Hive-log4j2.properties.template
  Hive-exec-log4j2.properties.template  ivysettings.xml  llap-cli-log4j2.properties.template  llap-daemon-log4j2.properties.template
  parquet-logging.properties
  [root@node03 conf]# cp Hive-env.sh.template Hive-env.sh
  ```

画面 3：
- 展示了 SecureCRT 会话窗口，显示了编辑后的 Hive-env.sh 文件内容：
  ```
  # if [ -z "$SDEBUG" ]; then
  # export HADOOP_OPTS="$SHADOOP_OPTS -XX:NewRatio=12 -Xms10m -XX:MaxHeapFreeRatio=40 -XX:MinHeapFreeRatio=15
  -XX:+UseParNewGC -XX:+UseGCOverheadLimit"
  # else
  # export HADOOP_OPTS="$SHADOOP_OPTS -XX:NewRatio=12 -Xms10m -XX:MaxHeapFreeRatio=40 -XX:MinHeapFreeRatio=15
  -XX:+UseGCOverheadLimit"
  # fi
  # The heap size of the jvm stared by Hive shell script can be controlled via:
  # export HADOOP_HEAPSIZE=1024
  # Larger heap size may be required when running queries over large number of files or partitions.
  # By default Hive shell scripts use a heap size of 256 (MB). Larger heap size would also be
  # appropriate for Hive server.
  ```
- 窗口底部显示了编辑状态：46, 0-1 78%。

画面 4：
- 展示了 SecureCRT 会话窗口，显示了空的终端界面，仅包含提示符“^C”和“^C”。
- 顶部显示了多个会话标签，包括 192.168.174.120、192.168.174.120、192.168.174.120（第三个为未激活状态）。

画面 5：
- 展示了 SecureCRT 会话窗口，显示了编辑后的 Hive-env.sh 文件内容：
  ```
  # The heap size of the jvm stared by Hive shell script can be controlled via:
  # export HADOOP_HEAPSIZE=1024
  # Larger heap size may be required when running queries over large number of files or partitions.
  # By default Hive shell scripts use a heap size of 256 (MB). Larger heap size would also be
  # appropriate for Hive server.
  # Set HADOOP_HOME to point to a specific Hadoop install directory
  HADOOP_HOME=/export/servers/Hadoop-3.1.1/
  # Hive Configuration Directory can be controlled by:
  # export HIVE_CONF_DIR=
  # Folder containing extra libraries required for Hive compilation/execution can be controlled by:
  # export HIVE_AUX_JARS_PATH=
  ```
- 窗口底部显示了编辑状态：48, 18 Bot。

画面 6：
- 展示了 SecureCRT 会话窗口，显示了编辑后的 Hive-env.sh 文件内容：
  ```
  # The heap size of the jvm stared by Hive shell script can be controlled via:
  # export HADOOP_HEAPSIZE=1024
  # Larger heap size may be required when running queries over large number of files or partitions.
  # By default Hive shell scripts use a heap size of 256 (MB). Larger heap size would also be
  # appropriate for Hive server.
  # Set HADOOP_HOME to point to a specific Hadoop install directory
  HADOOP_HOME=/export/servers/Hadoop-3.1.1/
  # Hive Configuration Directory can be controlled by:
  export HIVE_CONF_DIR=/export/servers/apache-Hive-3.1.1-bin/conf
  # Folder containing extra libraries required for Hive compilation/execution can be controlled by:
  # export HIVE_AUX_JARS_PATH=
  ```
- 窗口底部显示了编辑状态：54L, 2413C written。
- 同时显示了两个 SecureCRT 会话窗口，分别连接到 192.168.174.120 和 192.168.174.120（第二个窗口为未激活状态）。

画面 7：
- 展示了 SecureCRT 会话窗口，显示了编辑后的 Hive-site.xml 文件内容：
  ```
  # Set HADOOP_HOME to point to a specific Hadoop install directory
  HADOOP_HOME=/export/servers/Hadoop-3.1.1/
  # Hive Configuration Directory can be controlled by:
  # export HIVE_CONF_DIR=
  export HIVE_CONF_DIR=/export/servers/apache-Hive-3.1.1-bin/conf
  # Folder containing extra libraries required for Hive compilation/execution can be controlled by:
  # export HIVE_AUX_JARS_PATH=
  ```
- 窗口底部显示了编辑状态：54L, 2413C written。
- 同时显示了两个 SecureCRT 会话窗口，分别连接到 192.168.174.120 和 192.168.174.120（第二个窗口为未激活状态）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```
grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;
flush privileges;
```

画面 2：
```
[root@node03 ~]# ls /export/servers/
apache-Hive-3.1.1-bin/ Hadoop-3.1.1/ JDK 8.0_141/ ZooKeeper-3.4.9/
[root@node03 ~]# cd /export/servers/apache-Hive-3.1.1-bin/
[root@node03 conf]# ls
bin  binar-package  licenses  conf  examples  hostlog  jdb  lib  LICENSE  NOTICE  RELEASE_NOTES.txt  script
beeline-log4j2.properties  Hive-default.xml.template  Hive-env.sh.template  Hive-log4j2.properties.template
Hive-exec-log4j2.properties.template  ivysettings.xml  llap-cli-log4j2.properties.template  llap-daemon-log4j2.properties.template
parquet-logging.properties
[root@node03 conf]# cp Hive-env.sh.template Hive-env.sh
```

画面 3：
```
# if [ -z "$SDEBUG" ]; then
# export HADOOP_OPTS="$SHADOOP_OPTS -XX:NewRatio=12 -Xms10m -XX:MaxHeapFreeRatio=40 -XX:MinHeapFreeRatio=15
-XX:+UseParNewGC -XX:+UseGCOverheadLimit"
# else
# export HADOOP_OPTS="$SHADOOP_OPTS -XX:NewRatio=12 -Xms10m -XX:MaxHeapFreeRatio=40 -XX:MinHeapFreeRatio=15
-XX:+UseGCOverheadLimit"
# fi
#

