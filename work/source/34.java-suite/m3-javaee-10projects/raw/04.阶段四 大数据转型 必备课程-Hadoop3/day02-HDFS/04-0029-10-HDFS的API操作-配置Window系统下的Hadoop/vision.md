# 画面线理解：10-HDFS的API操作-配置Window系统下的Hadoop

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\10-HDFS的API操作-配置Window系统下的Hadoop【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:33, 00:54, 01:08, 01:13, 01:16, 01:23, 01:26, 01:55, 02:01, 02:15, 02:31, 02:35, 02:52, 03:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:11:57

1) 这一组画面整体在讲什么（一句话）：
在 Windows 系统上配置并运行 Hadoop 3.1.1 环境，包括设置环境变量和复制核心文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Hadoop 文档的 PDF 页面，内容为 HDFS 的 API 操作，其中包含 HDFS 命令列表，如 dfs -mkdir -p /xxx，dfs -put，dfs -cat 等。页面标题为“1.9. HDFS的 API 操作”，并列出在 Windows 系统上运行 Hadoop 的三步操作：第一步将 apache-hadoop-3.1.1 文件夹解压到无中文路径；第二步设置 HADOOP_HOME 环境变量；第三步将 hadoop.dll 复制到 C:\Windows\System32。
画面 2: 显示 Windows 资源管理器，路径为 E:\apache-hadoop-3.1.1，其中包含一个名为“bin”的文件夹。
画面 3: 黑马程序员和博学谷的课程封面页。
画面 4: Windows 系统属性窗口，显示系统信息：Windows 10 专业版，Intel Core i7-7500U CPU @ 2.70GHz，16.0 GB 内存，系统类型为 64 位操作系统，计算机名：LAPTOP-81ZVQ701I。
画面 5: 系统属性窗口中的“高级”选项卡，显示“环境变量”设置界面，其中“系统变量”列表中包含 HADOOP_HOME、JAVA_HOME、MAVEN_HOME 等变量，但尚未设置 HADOOP_HOME。
画面 6: 系统属性窗口中的“环境变量”设置界面，正在设置“HADOOP_HOME”变量，值为 E:\apache-hadoop-3.1.1。
画面 7: 系统属性窗口中的“环境变量”设置界面，正在设置“HADOOP_HOME”变量，值为 E:\apache-hadoop-3.1.1。
画面 8: 系统属性窗口中的“环境变量”设置界面，已设置“HADOOP_HOME”变量，值为 E:\apache-hadoop-3.1.1，同时显示了“JAVA_HOME”和“MAVEN_HOME”等变量，点击“确定”按钮。
画面 9: 显示 Hadoop 文档的 PDF 页面，内容为 HDFS 的 API 操作，其中包含 HDFS 命令列表，如 dfs -mkdir -p /xxx，dfs -put，dfs -cat 等。页面标题为“1.9. HDFS的 API 操作”，并列出在 Windows 系统上运行 Hadoop 的三步操作：第一步将 apache-hadoop-3.1.1 文件夹解压到无中文路径；第二步设置 HADOOP_HOME 环境变量；第三步将 hadoop.dll 复制到 C:\Windows\System32。
画面 10: 显示 Windows 资源管理器，路径为 E:\apache-hadoop-3.1.1，其中包含一个名为“bin”的文件夹。
画面 11: 显示 Windows 资源管理器，路径为 E:\apache-hadoop-3.1.1\bin，其中包含多个文件，如 hadoop.cmd、hadoop.dll、hdfs.exe 等，鼠标悬停在 hadoop.dll 文件上。
画面 12: 显示 Windows 资源管理器，路径为 C:\Windows，正在浏览系统文件夹。
画面 13: 显示 Hadoop 文档的 PDF 页面，内容为 HDFS 的 API 操作，其中包含 HDFS 命令列表，如 dfs -mkdir -p /xxx，dfs -put，dfs -cat 等。页面标题为“1.9. HDFS的 API 操作”，并列出在 Windows 系统上运行 Hadoop 的三步操作：第一步将 apache-hadoop-3.1.1 文件夹解压到无中文路径；第二步设置 HADOOP_HOME 环境变量；第三步将 hadoop.dll 复制到 C:\Windows\System32。
画面 14: 显示 Hadoop 文档的 PDF 页面，内容为 HDFS 的 API 操作，其中包含 HDFS 命令列表，如 dfs -mkdir -p /xxx，dfs -put，dfs -cat 等。页面标题为“1.9. HDFS的 API 操作”，并列出在 Windows 系统上运行 Hadoop 的三步操作：第一步将 apache-hadoop-3.1.1 文件夹解压到无中文路径；第二步设置 HADOOP_HOME 环境变量；第三步将 hadoop.dll 复制到 C:\Windows\System32。

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
hdfs dfs -chown -R hadoop:hadoop /xxx  # 修改hdfs的文件所有者

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
hdfs dfs -chown -R hadoop:hadoop /xxx  # 修改hdfs的文件所有者

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
hdfs dfs -chown -R hadoop:hadoop /xxx  # 修改hdfs的文件所有者

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1.9. HDFS的 API 操作”，内容为“在windows系统配置hadoop运行环境”，并列出四步操作：
第一步：将apache-hadoop-3.1.1文件夹解压到一个没有中文字符的路径下面。
第二步：在windows上面配置hadoop的环境变量：HADOOP_HOME。
第三步：把bin目录下的hadoop.dll文件复制到系统盘根目录 C:\Windows\System32。
第四步：关闭windows重启。

画面 9: PPT 标题为“1.9. HDFS的 API 操作”，内容为“在windows系统配置hadoop运行环境”，并列出四步操作：
第一步：将apache-hadoop-3.1.1文件夹解压到一个没有中文字符的路径下面。
第二步：在windows上面配置hadoop的环境变量：HADOOP_HOME。
第三步：
