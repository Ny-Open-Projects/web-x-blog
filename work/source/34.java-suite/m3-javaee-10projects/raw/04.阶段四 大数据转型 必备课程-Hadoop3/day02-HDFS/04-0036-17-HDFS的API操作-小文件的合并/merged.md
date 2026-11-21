# 17-HDFS的API操作-小文件的合并

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\17-HDFS的API操作-小文件的合并【海量资源尽在 ubkz.com】.mp4
- 时长 11分55秒（音频 715s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习HDFS小文件的合并这个HDFS呢它是一个分布式的文件系统它最擅长的呢其实是存储大文件但是呢在实际的工作中呢有时候有很多的小文件如果呢把这些小文件呢直接存储在HDFS上每一个小文件呢它都有一份独立的原数据信息那小文件过多呀那你的
[00:28] 原数据信息就过多那这个时候呢会增加呢我们NameNode管理原数据的一个内存压力怎么解决这个问题呢一般的在工作中呢我们需要将这些小文件呢合并成一个大文件然后呢由HDFS来进行存储好那接下来呢我们来学习一下如何进行小文件的合并在我们的HDFS一个shell命令的模式下呢有一个命令
[00:57] 它也可以实现文件的合并这个命令叫getmargin注意这个getmargin是将我们HDFS上的小文件合并成一个大文件并且下载到本地注意它是将HDFS的文件合并合并完之后下载到本地来我们简单给大家演示一下这个比如说在我的HDFS上在这个根目录下面你看有很多txt结尾的文件这些都是小文件
[01:27] 那我可以呢利用这个get margin将这些小文件合并完之后呢我可以放在我的本地来我们来操作一下在这里呢我写个hdfs dfsget margin然后呢把根目录下面新点txt就是所有的txt结尾的文件那合并完之后呢下载到本地那么本地呢这个文件呢比如说我叫叫big.txt
[01:57] OK回车稍等来我们来看一下这个cat也逼个点贴地这个里边呢其实就是这些所有的小文件合并出来的一个大文件OK这是一个一个命令叫getmerg那接下来呢我们再看另外一个问题我们刚才呢是将hdfs文件进行合并下载到本地那么接下来我们要思考一个问题这个问题就是说我们本地呢有很多的小文件
[02:26] 我们需要将它们合并之后呢上传到HDFS那这个呢如何实现合并呢这个时候呢我们需要去写加入程序来我们来看下面这个代码这个代码呢就是将本地的小文件合并成大文件并且上传到HDFS来我们来看这个代码呢是怎么实现的第一步呢还是获取fail system对象那这个最后一个参数呢注意
[02:53] 这个地方呢表示伪造用户以root用户的身份呢去获取那获取完这个fail system之后呢接下来我在fail system里边创建了一个文件叫bigfail.xmail这个其实就是一个大文件我得改成.txt吧也就是说我要将所有的本地的.txt合并成一个大的.txtOK创建文件那接下来呢我们还要获取本地的文件系统
[03:22] 因为呢我是要把本地的一些文件的合并那这个本地的文件系统呢就是用fail system来调一个方法叫get local里边呢你有一个configuration好那接下来呢我拿到这个本地的文件系统之后呢调一个方法叫list status这个呢可以获取本地的一个目录下面所有文件的详情然后呢便利这个数组每便利一个呢每便利一个
[03:51] 那我就去获取这个文件的一个输入流好现在输入流有了而刚才呢我们又拿到了输出流我们就可以用IoUtils这个拷贝方法把输入流的数据呢拷贝到输出流也就是拷贝到HDFS上那关闭一下输入流OK最后呢把这个资源释放这个就是整个的一个代码来接下来呢我把它给实现一下首先呢我们打开这个ID
[04:19] 在这里呢我们再写个代码就是小文件的合并在这里呢我们写个单元测试public void然后呢这个地方就是merge那这个地方呢merge testOK我就写这么一个方法好那么在这里呢我们首先呢第一步干嘛呢我们第一步要获取fail system好那这里边呢我们去
[04:57] 通过failsystem来调一个方法叫get那这里边呢我们用的是这个方法好第一个呢是拧一个uri这里边我们写hdfs冒号刚刚node01它的一个端口是8020第二个参数呢是拧一个configuration好第三个参数呢是一个伪造用户我们以root用户的身份获取好这个地方呢是一个failsystem
[05:30] 把这个异常呢先抛出好获取完文件系统之后呢第二步我们需要在呢在HDFS上创建一个大文件好那咱们来调一下第二步在HDFS创建一个大文件这个大文件呢就是通过这个地方呢写成file systemfile system.createnew一个pass
[06:05] 这个里面呢写上一个大文件的路径那在这里呢好大文件路径那这个呢在根目录下面我写个叫big testbig test.txt好写这么一个文件好创建完之后呢这个大文件已经有了但是呢里面的内容是空的那接下来呢我们来看我们需要去获取一个本地的文件系统来通过failsystem.getlocal然后new configuration
[06:36] 然后接下来呢获取这个本地文件系统的一个文件列表好那么接下来第三步获取本地的文件系统注意这个本地呢指的是我们window的系统那这个failsystem有个方法叫getlocalgetlocal直接呢扭一个configuration就可以获取本地的文件系统叫localfailsystem好获取完之后呢第四步我们要获取
[07:11] 本地文件夹下所有文件的详情信息就信息吧OK这个时候呢我们要调用这个localfile statement有个方法这个方法呢这个方法叫list status后面呢跟上一个本地的一个目录叫list稍等
[07:42] 这个方法叫listlist statusOK那这里边呢我们来看这里边需要一个需要一个路径那我们给它一个路径OKlist status好我们给它一个路径new一个pass这个是指定你小文件所在的位置我的小文件在哪里呢在我这个一排在我这个一排有个input目录这里边存放的都是小文件
[08:12] 我把这个路径呢直接放在这里一盘放完之后呢我们可以获取这个文件的详情就是failstats那接下来我们要干嘛呢我们第五个呢需要遍历遍历这个数组然后呢获取每一个每一个文件的信息好所以说我们要遍历它遍历完之后可以拿到每一个failstats
[08:44] 拿到每个fail system之后干什么呢我们既然呢需要去通过一个open方法拿到每一个文件的一个输入流注意open里边呢调了一个方法叫get pass就获取这个文件的路径来我们来看那这里边就是一个local fail system点一个方法叫什么呢openopen呢这里边呢需要去拿到每一个fail system的get pass
[09:14] OK拿到这个之后呢我们就可以获取每一个文件的输入流OK获取输入流输入流有了上面呢我们又拿到了一个我们来看我们这里边呢拿到这个地方呢我们还可以生成这个文件的返回值来我们生成返回值那么生成返回值之后呢你会发现在创建完这个文件之后我们可以拿到它的输出流也就是说输入流已经有了我们也有一个输出流那这个时候呢
[09:43] 我们就可以用个IoIoUtilsIoUtils这个我们选Commons.io它有个方法叫copy好可以将呢input stream里面的数据拷贝到output stream好实现这么一个拷贝拷贝完之后呢咱们顺便呢把这个IoUtils把这个文件呢给关闭把这个数留好可以写写个close queryOK这里边是input stream
[10:14] 好这个把这个文件关闭关闭完之后呢咱们好这个地方应该是写错了close qualityok那这就是input stream咱们还可以把output stream也可以关闭ioutils.close quality然后呢是output stream可以把fail system也给关闭ok那这地方呢fail systemok第二close这个本地的文件系统也可以关闭
[10:51] 第二closeok文码都关闭好关闭完之后呢这个代码呢就写完了写完之后呢呃我们来测试一下好咱们在这里点直接点运行稍等我们来看一下看能不能将这些本地的小文件合并成一个大文件并且放在HDFS上稍等好代码没有问题来咱们打开HDFS刷新一下好你会发现呢这里多了一个big txtok咱们打开
[11:24] 当一下当一下之后呢我们来看这里边文件的内容哎看是不是已经合并了OK这个呢其实就是一个简单的文件合并哎它是将本地的一些小文件呢合并成一个大文件并且放在HDFS上那这样做了之后呢就可以呢减少元数据信息哎然后呢它的一些它呢就可以减轻了内门Node的压力好关于小文件的合并呢我们呢就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.*;
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

