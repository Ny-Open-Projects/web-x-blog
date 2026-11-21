# 画面线理解：8-HDFS的shell操作命令

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\8-HDFS的shell操作命令【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:32, 03:01, 04:50, 05:52, 07:37, 09:16, 10:26, 11:14, 12:12, 13:21, 14:54, 15:44, 16:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:06:42

1) 这一组画面整体在讲什么（一句话）：
演示 HDFS 命令行操作，包括目录浏览、文件创建、移动、权限修改和文件内容查看等。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 HDFS Web UI 的根目录，包含 abc.txt、export、tmp、user 四个条目。
画面 2: 在 SecureCRT 中执行命令 `hdfs dfs -ls /`，列出 HDFS 根目录下的文件和目录。
画面 3: 在 SecureCRT 中执行命令 `hdfs dfs -mkdir /test`，然后执行 `hdfs dfs -mkdir -p /test/aaa/bbb`，并再次执行 `hdfs dfs -ls /` 验证。
画面 4: 显示 HDFS Web UI 的 /test 目录，包含 aaa 文件。
画面 5: 显示 Typora 中的文档，标题为“1.8. hdfs的命令行使用”，其中列出 hdfs dfs 命令的语法和常用操作命令。
画面 6: SecureCRT 窗口空白，可能为切换或等待状态。
画面 7: 在 HDFS Web UI 中，点击文件 hello.txt 后弹出的文件信息框，显示 Block ID、Block Pool ID、Size、Availability 等信息。
画面 8: 在 SecureCRT 中执行命令 `hdfs dfs -appendToFile a.txt b.txt /test/hello.txt`，然后执行 `hdfs dfs -cat /test/hello.txt` 查看内容。
画面 9: 显示 HDFS Web UI 的根目录，包含 abc.txt、export、test、tmp、user 五个条目。
画面 10: 显示 HDFS Web UI 的根目录，包含 abc.txt、export、test、tmp、user 五个条目，鼠标悬停在 test 目录上。
画面 11: 在 SecureCRT 中执行命令 `hdfs dfs -op /test/hello.txt /tmp`，然后执行 `hdfs dfs -rm /timer.txt`，接着执行 `hdfs dfs -rm -r /test`。
画面 12: 在 SecureCRT 中执行命令 `hdfs dfs -chmod 777 /abc.txt`，然后执行 `hdfs dfs -mkdir -p /test/aaa/bbb`。
画面 13: 在 SecureCRT 中执行命令 `hdfs dfs -chmod -R 777 /test`。
画面 14: 显示 Typora 中的文档，标题为“1.8. hdfs的命令行使用”，其中列出 hdfs dfs 命令的语法和常用操作命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```
hdfs dfs -ls /
```
画面 3:
```
hdfs dfs -mkdir /test
hdfs dfs -mkdir -p /test/aaa/bbb
hdfs dfs -ls /
```
画面 4:
```
/test
```
画面 5:
```
语法: hdfs dfs 命令
hdfs dfs -ls / 查看根目录下的文件或者文件夹
hdfs dfs -mkdir -p /xxx/xxx (hdfs上面的创建文件夹)
hdfs dfs -mv localSourceDir (本地目录的文件或者文件夹) destDir (hdfs的路径)
hdfs dfs -put localFile hdfsDir
hdfs dfs -get hdfsFile localDir
hdfs dfs -appendToFile a.txt b.txt /test/hello.txt
hdfs dfs -cat hdfsSourceDir hdfsDestDir
hdfs dfs -cp hdfsSourceDir hdfsDestDir
hdfs dfs -rm -r [递归] 删除文件或者文件夹
hdfs dfs -chmod 777 /xxx
hdfs dfs -chown -R hadoop:hadoop /xxx
```
画面 7:
```
Block ID: 1073741933
Block Pool ID: BP-13329519-192.168.1.74-100-1555938164834
Generation Stamp: 1109
Size: 24
Availability:
  node02.hadoop.com
  node02.hadoop.com
  node01.hadoop.com
```
画面 8:
```
hdfs dfs -appendToFile a.txt b.txt /test/hello.txt
hdfs dfs -cat /test/hello.txt
```
画面 9:
```
/
```
画面 10:
```
/
```
画面 11:
```
hdfs dfs -op /test/hello.txt /tmp
hdfs dfs -rm /timer.txt
hdfs dfs -rm -r /test
```
画面 12:
```
hdfs dfs -chmod 777 /abc.txt
hdfs dfs -mkdir -p /test/aaa/bbb
```
画面 13:
```
hdfs dfs -chmod -R 777 /test
```
画面 14:
```
语法: hdfs dfs 命令
hdfs dfs -ls / 查看根目录下的文件或者文件夹
hdfs dfs -mkdir -p /xxx/xxx (hdfs上面的创建文件夹)
hdfs dfs -mv localSourceDir (本地目录的文件或者文件夹) destDir (hdfs的路径)
hdfs dfs -put localFile hdfsDir
hdfs dfs -get hdfsFile localDir
hdfs dfs -appendToFile a.txt b.txt /test/hello.txt
hdfs dfs -cat hdfsSourceDir hdfsDestDir
hdfs dfs -cp hdfsSourceDir hdfsDestDir
hdfs dfs -rm -r [递归] 删除文件或者文件夹
hdfs dfs -chmod 777 /xxx
hdfs dfs -chown -R hadoop:hadoop /xxx
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5 和 14: PPT 标题为“1.8. hdfs的命令行使用”，内容包括“语法: hdfs dfs 命令”和列出的 hdfs dfs 命令语法和常用操作命令。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
