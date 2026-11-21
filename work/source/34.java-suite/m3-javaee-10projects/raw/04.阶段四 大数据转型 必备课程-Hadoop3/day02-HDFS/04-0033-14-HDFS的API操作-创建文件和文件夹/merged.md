# 14-HDFS的API操作-创建文件和文件夹

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\14-HDFS的API操作-创建文件和文件夹【海量资源尽在 ubkz.com】.mp4
- 时长 3分38秒（音频 219s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习下一个操作就是在HDFS上创建文件夹这个操作也非常简单有两步第一步我们还是获取failsetterm对象接下来通过这个failsetterm来调个方法叫make ds后面你有一个pass对象这个可以做到地归创建也就是可以创建多级文件夹来我们来演示一下好在这里我们先加个注释
[00:28] 就在HDFS上创建文件夹好加个单元测试然后呢这个名字我写成make ds test来我们第一步呢还是获取file system对象那就是file system.getnuguri好这里边呢我写成HDFS冒号刚刚node01
[01:04] 8020后面呢直接new一个configuration这里边呢有个异常我们来抛一下好拿到这个fail system对象之后呢接下来呢我们直接创建文件夹创建文件夹呢调一个方法叫make-4这么一个方法这个方法的内部呢需要一个参数这个参数呢
[01:39] 是一个pass所以说我new一个pass给它一个路径比如说呢我想在根目录下面呢创建文件夹这个文件夹呢叫叫appapp下面呢我想再创建一个文件夹呢假设叫testtest下面创建一个hellook我们创建一个三级文件夹好这个代码就写完了写完之后呢我们来测试一下好在这直接运行走好稍等
[02:13] 好 没有问题来 我们来看一下这个文件系统看有没有多一个APP下面有一个TestTest有个HelloOK 这个文件夹就创建好了那大家想一个问题我在这里既然可以创建文件夹那我能不能创建文件呢答案是可以的来 我们来第三步我们可以做一个创建文件如何去创建文件呢也非常简单我们可以用FailSystem来第二个方法叫Create
[02:45] 这个create呢也需要一个pass对象我们new一个pass比如说呢我们可以在根目录里边创一个文件叫a.tit好那我先把上面这个注释了我们来试一下看它能不能创进这个a.tit来我们来运行好稍等好没有问题没有问题之后我来直接刷新刷新回到根目录来看一下你会发现这里边呢多了一个文件a.tit
[03:25] 也就是说我们既可以在HDFS上创建文件夹我们也可以创建文件好关于它的文件夹或文件的创建我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

