# 画面线理解：9-HDFS的页面操作

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\9-HDFS的页面操作【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:57, 01:38, 01:58, 02:56, 03:02, 03:13, 03:19, 03:34, 03:56, 04:27, 04:35, 04:51, 04:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:09:01

1) 这一组画面整体在讲什么（一句话）：
演示 HDFS 文件系统 Web 界面的基本操作，包括浏览目录、上传文件、查看文件信息和删除文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 HDFS Web 界面的根目录下，显示了 5 个文件/目录：export、test、timer.txt、tmp、user。
画面 2: 鼠标悬停在“test”文件上，未执行任何操作。
画面 3: 鼠标悬停在“app”文件上，未执行任何操作。
画面 4: 点击“Upload File”按钮后弹出的上传对话框，提示“选择文件，未选择任何文件”。
画面 5: 点击“user”目录后，进入该目录，显示其中包含一个名为“root”的文件。
画面 6: 点击“hello.txt”文件后弹出的文件信息对话框，显示其 Block ID、Block Pool ID、Generation Stamp、Size 和 Availability（node01.hadoop.com、node02.hadoop.com、node03.hadoop.com）。
画面 7: 在文件信息对话框中，鼠标悬停在“Head the file (first 32K)”链接上。
画面 8: 在根目录下，点击“Go!”按钮后，页面显示了 6 个文件/目录：Note02.md、app、export、test、tmp、user。
画面 9: 点击“Upload File”按钮后弹出的上传对话框，提示“选择文件 Note02.md”。
画面 10: 点击“Note02.md”文件后弹出的删除确认对话框，提示“Are you sure you want to delete Note02.md?”，并提供“Cancel”和“Delete”按钮。
画面 11: 显示了《Note02.md - Typora》文档的第 1.8 节“hdfs的命令行使用”和第 1.9 节“HDFS 的 API 操作”内容。
画面 12: 在根目录下，鼠标悬停在“Last Modified”列的“Apr 27 17:55”上。
画面 13: 在根目录下，鼠标悬停在“Replication”列的“0”上。
画面 14: 在根目录下，鼠标悬停在“Block Size”列的“0 B”上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 11:
```
语法: hdfs dfs 参数
hdfs dfs -ls / 查看根路径下面的文件或者文件夹
hdfs dfs -mkdir -p /xxx/xxx 在hdfs上面递归的创建文件夹
hdfs dfs -mv hdfsSourceDir hdfsDestDir (本地磁盘的文件或者文件夹的路径) desDir (hdfs的路径)
hdfs dfs -put localFile hdfsDir 将本地文件系统的文件或者文件夹放到hdfs上面去
hdfs dfs -cat hdfsDir 查看hdfs的文件内容
hdfs dfs -cp hdfsSourceDir hdfsDestDir 拷贝文件或者文件夹
hdfs dfs -rm -r (递归) 删除文件或者文件夹
hdfs dfs -chmod R 777 /xxx
hdfs dfs -chown -R hadoop:hadoop /xxx
```
画面 11:
```
1.9.1 导入 Maven 依赖
<repositories>
    <repository>
        <id>hadoop</id>
    </repository>
</repositories>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
