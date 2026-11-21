# 画面线理解：14-HDFS的API操作-创建文件和文件夹

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\14-HDFS的API操作-创建文件和文件夹【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:26, 00:38, 00:53, 00:59, 01:29, 01:41, 02:14, 02:21, 02:41, 02:49, 03:01, 03:21, 03:27, 03:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:23:39

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Java API 在 HDFS 上创建目录和文件，并通过 Web 界面验证操作结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 HDFS API 程序的代码，包含创建目录的示例代码，以及 HDFS 的 Web 界面截图，显示了 HDFS 的目录结构。
画面 2: 展示 Java 代码中获取 HDFS 文件系统对象的代码片段。
画面 3: 展示 Java 代码中创建目录的代码片段。
画面 4: 展示在代码中输入 URI 时，IDE 提供的自动补全建议。
画面 5: 展示在代码中输入文件系统对象后，IDE 提供的自动补全建议。
画面 6: 展示在代码中输入文件系统对象后，IDE 提供的自动补全建议。
画面 7: 展示 HDFS Web 界面，显示了 HDFS 的目录结构。
画面 8: 展示 Java 代码中创建目录的代码片段。
画面 9: 展示在代码中输入文件系统对象后，IDE 提供的自动补全建议。
画面 10: 展示在代码中输入文件系统对象后，IDE 提供的自动补全建议。
画面 11: 展示 Java 代码中创建文件的代码片段。
画面 12: 展示 HDFS Web 界面，显示了 HDFS 的目录结构。
画面 13: 展示 Java 代码中创建文件的代码片段。
画面 14: 展示 Java 代码中创建文件的代码片段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
//遍历
RemoteIterator<LocatedFileStatus> locatedFileStatusRemoteIterator =
        filesystem.listFiles(new Path("/"), true);
while (locatedFileStatusRemoteIterator.hasNext()) {
    LocatedFileStatus next = locatedFileStatusRemoteIterator.next();
    System.out.println(next.getPath().toString());
}
filesystem.close();
```
画面 2:
```java
@Test
public void getListFiles() throws URISyntaxException, IOException {
    //1:获取FileSystem对象
    FileSystem fileSystem = FileSystem.get(new URI("hdfs://node01:8020"), new Configuration());
    //2:获取指定目录下的所有文件信息
    RemoteIterator<LocatedFileStatus> iterator = fileSystem.listFiles(new Path("/"), true);
    //3:遍历迭代器
    while (iterator.hasNext()) {
        LocatedFileStatus next = iterator.next();
        System.out.println(next.getPath().toString());
    }
    fileSystem.close();
}
```
画面 3:
```java
@Test
public void mkdirsTest() throws URISyntaxException, IOException {
    //1:获取FileSystem对象
    FileSystem fileSystem = FileSystem.get(new URI("hdfs://node01:8020"), new Configuration());
    //2:创建文件夹
    fileSystem.mkdirs(new Path("/app/test/hello"));
}
```
画面 4:
```java
FileSystem.get(new URI("hdfs://node01:8020"), new Configuration());
```
画面 5:
```java
FileSystem
    finalize()
    getFileSystem1()
    getFileSystem2()
    getFileSystem3()
    getFileSystem4()
    getListFiles()
    close()
```
画面 6:
```java
fileSystem.mkdirs(new Path("/app/test/hello"));
```
画面 7:
```html
<table>
    <thead>
        <tr>
            <th>Permission</th>
            <th>Owner</th>
            <th>Group</th>
            <th>Size</th>
            <th>Last Modified</th>
            <th>Replication</th>
            <th>Block Size</th>
            <th>Name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>drwxr-xr-x</td>
            <td>root</td>
            <td>supergroup</td>
            <td>0 B</td>
            <td>Apr 24 10:55</td>
            <td>0</td>
            <td>0 B</td>
            <td>export</td>
        </tr>
        <tr>
            <td>drwxr-xr-x</td>
            <td>root</td>
            <td>supergroup</td>
            <td>0 B</td>
            <td>Apr 27 17:55</td>
            <td>0</td>
            <td>0 B</td>
            <td>test</td>
        </tr>
        <tr>
            <td>-rw-rw-rw-</td>
            <td>root</td>
            <td>supergroup</td>
            <td>58 B</td>
            <td>Apr 28 10:21</td>
            <td>3</td>
            <td>128 MB</td>
            <td>timer.txt</td>
        </tr>
        <tr>
            <td>drwxr-xr-x</td>
            <td>root</td>
            <td>supergroup</td>
            <td>0 B</td>
            <td>Apr 27 17:45</td>
            <td>0</td>
            <td>0 B</td>
            <td>tmp</td>
        </tr>
        <tr>
            <td>drwxr-xr-x</td>
            <td>root</td>
            <td>supergroup</td>
            <td>0 B</td>
            <td>Apr 24 10:51</td>
            <td>0</td>
            <td>0 B</td>
            <td>user</td>
        </tr>
    </tbody>
</table>
```
画面 8:
```java
fileSystem.mkdirs(new Path("/app/test/hello"));
```
画面 9:
```java
FileSystem
    finalize()
    getFileSystem1()
    getFileSystem2()
    getFileSystem3()
    getFileSystem4()
    getListFiles()
    close()
```
画面 10:
```java
FileSystem
    finalize()
    getFileSystem1()
    getFileSystem2()
    getFileSystem3()
    getFileSystem4()
    getListFiles()
    close()
```
画面 11:
```java
fileSystem.create(new Path("/a.txt"));
```
画面 12:
```html
<table>
    <thead>
        <tr>
            <th>Permission</th>
            <th>Owner</th>
            <th>Group</th>
            <th>Size</th>
            <th>Last Modified</th>
            <th>Replication</th>
            <th>Block Size</th>
            <th>Name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>-rw-rw-rw-</td>
            <td>ift</td>
            <td>supergroup</td>
            <td>0 B</td>
            <td>Apr 26 11:03</td>
            <td>3</td>
            <td>128 MB</td>
            <td>a.txt</td>
        </tr>
        <tr>
            <td>drwxr-xr-x</td>
            <td>root</td>
            <td>supergroup</td>
            <td>0 B</td>
            <td>Apr 24 10:52</td>
            <td>0</td>
            <td>0 B</td>
            <td>app</td>
        </tr>
        <tr>
            <td>drwxr-xr-x</td>
            <td>root</td>
            <td>supergroup</td>
            <td>0 B</td>
            <td>Apr 24 10:51</td>
            <td>0</td>
            <td>0 B</td>
            <td>export</td>
        </tr>
        <tr>
            <td>drwxr-xr-x</td>
            <td>root</td>
            <td>supergroup</td>
            <td>0 B</td>
            <td>Apr 27 17:55</td>
            <td>0</td>
            <td>0 B</td>
            <td>test</td>
        </tr>
        <tr>
            <td>-rw-rw-rw-</td>
            <td>root</td>
            <td>supergroup</td>
            <td>58 B</td>
            <td>Apr 28 10:21</td>
            <td>3</td>
            <td>128 MB</td>
            <td>timer.txt</td>
        </tr>
        <tr>
            <td>drwxr-xr-x</td>
            <td>root</td>
            <td>supergroup</
