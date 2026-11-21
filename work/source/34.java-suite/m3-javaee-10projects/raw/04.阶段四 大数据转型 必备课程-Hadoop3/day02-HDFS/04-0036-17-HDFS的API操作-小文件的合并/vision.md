# 画面线理解：17-HDFS的API操作-小文件的合并

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\17-HDFS的API操作-小文件的合并【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:52, 02:37, 04:21, 05:09, 06:22, 07:28, 07:59, 08:59, 09:13, 10:03, 10:29, 10:50, 11:19, 11:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:31:50

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Hadoop API 编写 Java 程序，将本地文件夹中的多个小文件合并上传到 HDFS 中的一个大文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 内容：展示 Hadoop 文档中关于“小文件合并”的章节，说明小文件过多会增加 NameNode 内存压力，建议合并。
- 代码：在命令行中执行 `hdfs dfs -getmerge /config/*.xml /hello.xml` 命令，将 HDFS 中多个小文件合并为一个大文件下载到本地。
- 图表：展示 HDFS 架构图，包含 NameNode、DataNode、SecondaryNameNode、Client、DFS 等组件。

画面 2：
- 内容：展示 HDFS Shell 命令 `hdfs dfs -getmerge` 的使用方法。
- 代码：`cd /export/servers` 和 `hdfs dfs -getmerge /config/*.xml /hello.xml`。
- 图表：与画面 1 相同的 HDFS 架构图。

画面 3：
- 内容：展示 IDEA 开发环境，项目结构为 `day02_hdfs_api`，包含 `src/main/java` 和 `src/main/resources` 目录。
- 代码：Java 类 `HdfsApiStudy` 的开头部分，包含多个 import 语句。

画面 4：
- 内容：展示 `HdfsApiStudy` 类中 `mergeFileTest` 方法的定义，用于实现小文件合并功能。
- 代码：`public void mergeFileTest() throws URISyntaxException, IOException, InterruptedException {`

画面 5：
- 内容：展示 `mergeFileTest` 方法中获取 HDFS 文件系统实例的代码。
- 代码：`FileSystem fileSystem = FileSystem.get(new URI("hdfs://node01:8020"), new Configuration(), "root");`

画面 6：
- 内容：展示在 HDFS 中创建一个大文件的代码。
- 代码：`fileSystem.create(new Path("/bigtxt.txt"));`

画面 7：
- 内容：展示获取本地文件系统实例的代码。
- 代码：`LocalFileSystem localFileSystem = FileSystem.getLocal(new Configuration());`

画面 8：
- 内容：展示获取本地文件夹中所有文件信息的代码。
- 代码：`FileStatus[] fileStatuses = localFileSystem.listStatus(new Path("E:\\input"));`

画面 9：
- 内容：展示遍历文件状态并打开每个文件的代码。
- 代码：`for (FileStatus fileStatus : fileStatuses) {`
- 代码：`localFileSystem.open(fileStatus.getPath());`

画面 10：
- 内容：展示 IDE 中的自动补全提示，列出 `FileStatus` 类的成员方法。
- 代码：`FileStatus[] fileStatuses = localFileSystem.listStatus(new Path("E:\\input"));`

画面 11：
- 内容：展示 IDE 中的自动补全提示，列出 `Path` 类的成员方法。
- 代码：`localFileSystem.open(fileStatus.getPath());`

画面 12：
- 内容：展示 IDE 中的自动补全提示，列出 `LocalFileSystem` 类的成员方法。
- 代码：`FileStatus[] fileStatuses = localFileSystem.listStatus(new Path("E:\\input"));`

画面 13：
- 内容：展示 Hadoop Web UI 的“Browse Directory”页面，显示 HDFS 的文件浏览功能。
- 代码：无。

画面 14：
- 内容：展示 `mergeFileTest` 方法中实现文件上传的完整代码。
- 代码：`FSDataOutputStream outputStream = fileSystem.create(new Path("/bigtxt.txt"));`
- 代码：`for (FileStatus fileStatus : fileStatuses) {`
- 代码：`FSDataInputStream inputStream = localFileSystem.open(fileStatus.getPath());`
- 代码：`IOUtils.copy(inputStream, outputStream);`
- 代码：`IOUtils.closeQuietly(inputStream);`

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
configuration(); 
filesystem.copyFromLocalFile(new Path("/config/core-site.xml"), new Path("file:///c:/core-site.xml")); 
filesystem.close(); 
```

画面 2：
```bash
cd /export/servers
hdfs dfs -getmerge /config/*.xml /hello.xml
```

画面 3：
```java
package cn.itcast.hdfs;
import org.apache.commons.io.IOUtils;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;
import org.junit.jupiter.api.Test;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
```

画面 4：
```java
public void mergeFileTest() throws URISyntaxException, IOException, InterruptedException {
```

画面 5：
```java
FileSystem fileSystem = FileSystem.get(new URI("hdfs://node01:8020"), new Configuration(), "root");
```

画面 6：
```java
fileSystem.create(new Path("/bigtxt.txt"));
```

画面 7：
```java
LocalFileSystem localFileSystem = FileSystem.getLocal(new Configuration());
```

画面 8：
```java
FileStatus[] fileStatuses = localFileSystem.listStatus(new Path("E:\\input"));
```

画面 9：
```java
for (FileStatus fileStatus : fileStatuses) {
    localFileSystem.open(fileStatus.getPath());
```

画面 10：
```java
FileStatus[] fileStatuses = localFileSystem.listStatus(new Path("E:\\input"));
```

画面 11：
```java
localFileSystem.open(fileStatus.getPath());
```

画面 12：
```java
FileStatus[] fileStatuses = localFileSystem.listStatus(new Path("E:\\input"));
```

画面 14：
```java
FSDataOutputStream outputStream = fileSystem.create(new Path("/bigtxt.txt"));
for (FileStatus fileStatus : fileStatuses) {
    FSDataInputStream inputStream = localFileSystem.open(fileStatus.getPath());
    IOUtils.copy(inputStream, outputStream);
    IOUtils.closeQuietly(inputStream);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：
- 标题：1.9.9. 小文件合并
- 内容：说明小文件过多会增加 NameNode 内存压力，建议合并。
- 图表：HDFS 架构图，包含 NameNode、DataNode、SecondaryNameNode、Client、DFS 等组件。

画面 2：
- 图表：与画面 1 相同的 HDFS 架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
