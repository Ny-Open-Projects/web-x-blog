# 10-HDFS的API操作-配置Window系统下的Hadoop

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\10-HDFS的API操作-配置Window系统下的Hadoop【海量资源尽在 ubkz.com】.mp4
- 时长 3分15秒（音频 195s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习通过Java API的方式来操作HDFS那要去做这个操作之前啊我们首先呢需要在Windows系统里边配这个Hadoop的运行环境那这里边有四步我们先看第一步第一步呢你需要将这么一个文件夹就是Apache Hadoop 3.3.1这个文件夹拷贝到一个没有中文没有空格的路径下面那这个文件夹是什么呢其实就是
[00:29] 温度子版本的一个Hadoop来看我今天给大家提供的资料里边在资料里边有一个阿巴奇Hadoop3.1.1这个就是温度子版本的Hadoop我们要拷贝到一个目录去哪个目录都可以但是不能有中文不能有空格那我呢直接把这个文件夹拷贝到一盘在我的一盘里边我拷到这里好 这是第一步咱们来看第二步
[00:58] 第二步呢我们需要在Windows上面配这个Hadoop的环境变量这个环境变量的名字呢叫Hadoop Home来我们来看一下可以点我的电脑右键属性找一个高级系统设置找一个环境变量在下面呢这里边有个Hadoop Home好这个路径呢其实就是你Hadoop存放的这个目录把这个目录拷贝过来
[01:27] 好点确定就可以了那接下来呢我们还要做一件事情这个Hadoop Home配完之后呢我们需要将这个环境变量加载到Path里面打开我的Path打开Path在Path里面呢我们需要加一个Hadoop Home把他的闭目录呢添加进去那他的写法呢就是这样写OK这个一定要保证正确那写完之后呢我们保存我这里已经设过了所以说我就点取消
[01:58] 那么一直点确定这是第二步还有第三步这个第三步我们需要将bin目录下面的DLL文件放到一个系统盘里面去什么意思呢我们来看在这个Hadoop 3.3.1下面有个bin目录在bin目录里边有一个Hadoop.dll这个是Hadoop的一个动态链接库
[02:26] 我们需要将这个动态连接库拷贝然后放在哪里放在C盘C盘里边一个WindowsWindows里边有个System32要放在这个目录要粘到这个目录去直接我们来粘贴就可以了把它粘贴好那这里边我已经有了我就不再去直接粘贴了OK要放在这里边这是我们的第三步好做完这三步之后
[02:57] 接下来最后一步我们需要关闭Windows系统然后重启好这四步必须去做否则你的API是跑不了的好那么关于这个配置Windows下的Hadoop呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Windows 系统上配置并运行 Hadoop 3.1.1 环境，包括设置环境变量和复制核心文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Hadoop 文档的 PDF 页面，内容为 HDFS 的 API 操作，其中包含 HDFS 命令列表，如 dfs -mkdir -p /xxx，dfs -put，dfs -cat 等。页面标题为“1.9. HDFS的 API 操作”，并列出在 Windows 系统上运行 Hadoop 的三步操作：第一步将 apache-Hadoop-3.1.1 文件夹解压到无中文路径；第二步设置 HADOOP_HOME 环境变量；第三步将 Hadoop.dll 复制到 C:\Windows\System32。
画面 2: 显示 Windows 资源管理器，路径为 E:\apache-Hadoop-3.1.1，其中包含一个名为“bin”的文件夹。
画面 3: 黑马程序员和博学谷的课程封面页。
画面 4: Windows 系统属性窗口，显示系统信息：Windows 10 专业版，Intel Core i7-7500U CPU @ 2.70GHz，16.0 GB 内存，系统类型为 64 位操作系统，计算机名：LAPTOP-81ZVQ701I。
画面 5: 系统属性窗口中的“高级”选项卡，显示“环境变量”设置界面，其中“系统变量”列表中包含 HADOOP_HOME、JAVA_HOME、MAVEN_HOME 等变量，但尚未设置 HADOOP_HOME。
画面 6: 系统属性窗口中的“环境变量”设置界面，正在设置“HADOOP_HOME”变量，值为 E:\apache-Hadoop-3.1.1。
画面 7: 系统属性窗口中的“环境变量”设置界面，正在设置“HADOOP_HOME”变量，值为 E:\apache-Hadoop-3.1.1。
画面 8: 系统属性窗口中的“环境变量”设置界面，已设置“HADOOP_HOME”变量，值为 E:\apache-Hadoop-3.1.1，同时显示了“JAVA_HOME”和“MAVEN_HOME”等变量，点击“确定”按钮。
画面 9: 显示 Hadoop 文档的 PDF 页面，内容为 HDFS 的 API 操作，其中包含 HDFS 命令列表，如 dfs -mkdir -p /xxx，dfs -put，dfs -cat 等。页面标题为“1.9. HDFS的 API 操作”，并列出在 Windows 系统上运行 Hadoop 的三步操作：第一步将 apache-Hadoop-3.1.1 文件夹解压到无中文路径；第二步设置 HADOOP_HOME 环境变量；第三步将 Hadoop.dll 复制到 C:\Windows\System32。
画面 10: 显示 Windows 资源管理器，路径为 E:\apache-Hadoop-3.1.1，其中包含一个名为“bin”的文件夹。
画面 11: 显示 Windows 资源管理器，路径为 E:\apache-Hadoop-3.1.1\bin，其中包含多个文件，如 Hadoop.cmd、Hadoop.dll、hdfs.exe 等，鼠标悬停在 Hadoop.dll 文件上。
画面 12: 显示 Windows 资源管理器，路径为 C:\Windows，正在浏览系统文件夹。
画面 13: 显示 Hadoop 文档的 PDF 页面，内容为 HDFS 的 API 操作，其中包含 HDFS 命令列表，如 dfs -mkdir -p /xxx，dfs -put，dfs -cat 等。页面标题为“1.9. HDFS的 API 操作”，并列出在 Windows 系统上运行 Hadoop 的三步操作：第一步将 apache-Hadoop-3.1.1 文件夹解压到无中文路径；第二步设置 HADOOP_HOME 环境变量；第三步将 Hadoop.dll 复制到 C:\Windows\System32。
画面 14: 显示 Hadoop 文档的 PDF 页面，内容为 HDFS 的 API 操作，其中包含 HDFS 命令列表，如 dfs -mkdir -p /xxx，dfs -put，dfs -cat 等。页面标题为“1.9. HDFS的 API 操作”，并列出在 Windows 系统上运行 Hadoop 的三步操作：第一步将 apache-Hadoop-3.1.1 文件夹解压到无中文路径；第二步设置 HADOOP_HOME 环境变量；第三步将 Hadoop.dll 复制到 C:\Windows\System32。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
hdfs dfs -mkdir -p /xxx  # 在hdfs上面进行创建文件夹
hdfs dfs -moveFromLocal sourceDir (本地磁盘的文件或者文件夹的路径) destDir (hdfs的路径)
hdfs dfs -mv hdfsSourceDir hdfsDestDir  # 移动hdfs的文件或者文件夹
hdfs dfs -put localDir hdfsDir  # 将本地文件系统中的文件或者文件夹上传到hdfs上面
hdfs dfs -appendToFile A.txt B.txt  # 追加写入文件
hdfs dfs -cat hdfsDir  # 查看hdfs的文件内容
hdfs dfs -cp hdfsSourceDir hdfsDestDir  # 拷贝hdfs的文件或者文件夹
hdfs dfs -rm -r /xxx  # 删除hdfs的文件或者文件夹
hdfs dfs -chmod -R 777 /xxx  # 修改hdfs的权限
hdfs dfs -chown -R Hadoop:Hadoop /xxx  # 修改hdfs的文件所有者

画面 13:
hdfs dfs -mkdir -p /xxx  # 在hdfs上面进行创建文件夹
hdfs dfs -moveFromLocal sourceDir (本地磁盘的文件或者文件夹的路径) destDir (hdfs的路径)
hdfs dfs -mv hdfsSourceDir hdfsDestDir  # 移动hdfs的文件或者文件夹
hdfs dfs -put localDir hdfsDir  # 将本地文件系统中的文件或者文件夹上传到hdfs上面
hdfs dfs -appendToFile A.txt B.txt  # 追加写入文件
hdfs dfs -cat hdfsDir  # 查看hdfs的文件内容
hdfs dfs -cp hdfsSourceDir hdfsDestDir  # 拷贝hdfs的文件或者文件夹
hdfs dfs -rm -r /xxx  # 删除hdfs的文件或者文件夹
hdfs dfs -chmod -R 777 /xxx  # 修改hdfs的权限
hdfs dfs -chown -R Hadoop:Hadoop /xxx  # 修改hdfs的文件所有者

画面 14:
hdfs dfs -mkdir -p /xxx  # 在hdfs上面进行创建文件夹
hdfs dfs -moveFromLocal sourceDir (本地磁盘的文件或者文件夹的路径) destDir (hdfs的路径)
hdfs dfs -mv hdfsSourceDir hdfsDestDir  # 移动hdfs的文件或者文件夹
hdfs dfs -put localDir hdfsDir  # 将本地文件系统中的文件或者文件夹上传到hdfs上面
hdfs dfs -appendToFile A.txt B.txt  # 追加写入文件
hdfs dfs -cat hdfsDir  # 查看hdfs的文件内容
hdfs dfs -cp hdfsSourceDir hdfsDestDir  # 拷贝hdfs的文件或者文件夹
hdfs dfs -rm -r /xxx  # 删除hdfs的文件或者文件夹
hdfs dfs -chmod -R 777 /xxx  # 修改hdfs的权限
hdfs dfs -chown -R Hadoop:Hadoop /xxx  # 修改hdfs的文件所有者

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1.9. HDFS的 API 操作”，内容为“在windows系统配置Hadoop运行环境”，并列出四步操作：
第一步：将apache-Hadoop-3.1.1文件夹解压到一个没有中文字符的路径下面。
第二步：在windows上面配置Hadoop的环境变量：HADOOP_HOME。
第三步：把bin目录下的Hadoop.dll文件复制到系统盘根目录 C:\Windows\System32。
第四步：关闭windows重启。

画面 9: PPT 标题为“1.9. HDFS的 API 操作”，内容为“在windows系统配置Hadoop运行环境”，并列出四步操作：
第一步：将apache-Hadoop-3.1.1文件夹解压到一个没有中文字符的路径下面。
第二步：在windows上面配置Hadoop的环境变量：HADOOP_HOME。
第三步：

