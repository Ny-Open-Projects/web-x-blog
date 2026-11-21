# 画面线理解：13-HDFS的API操作-获取文件列表信息

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\13-HDFS的API操作-获取文件列表信息【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 01:23, 02:19, 03:09, 03:53, 04:49, 06:07, 07:32, 08:40, 08:59, 09:39, 10:08, 10:42, 10:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:20:43

1) 这一组画面整体在讲如何使用 Java API 遍历 HDFS 中的所有文件并获取每个文件的路径、名称和 Block 存储位置信息。

2) 按时间顺序列出每张画面的要点：
画面1：展示 HDFS 文件系统 API 的四种获取文件系统的方式，其中第四种方式使用 new URI 和 new Configuration 构造 FileSystem 对象。
画面2：展示如何使用 API 遍历 HDFS 中所有文件，代码中使用 FileSystem.listFiles() 获取 RemoteIterator，然后通过 hasNext() 和 next() 遍历。
画面3：IDE 中显示代码，光标位于 getFileSystem4() 方法的定义处，展示获取文件系统第四种方式的代码。
画面4：IDE 中显示代码，光标位于 getFileSystem4() 方法的定义处，展示获取文件系统第四种方式的代码。
画面5：IDE 中显示代码，光标位于 listFiles() 方法的返回值 RemoteIterator<LocatedFileStatus> 上，展示其类型。
画面6：IDE 中显示代码，光标位于 while 循环体中，展示如何获取每个文件的详细信息。
画面7：IDE 中显示代码，光标位于 System.out.println(fileStatus.getPath().getFileName()); 行，展示获取文件名。
画面8：IDE 中显示代码，光标位于 System.out.println(blockLocations.length); 行，展示打印 Block 数量。
画面9：IDE 中显示代码，光标位于 getFileSystem1() 方法的定义处，展示获取文件系统第一种方式的代码。
画面10：IDE 中显示代码，光标位于 getFileSystem1() 方法的定义处，展示获取文件系统第一种方式的代码。
画面11：运行结果窗口显示程序成功执行，输出了 HDFS 中某个文件的路径。
画面12：运行结果窗口显示程序成功执行，输出了 HDFS 中某个文件的路径。
画面13：运行结果窗口显示程序成功执行，输出了 HDFS 中某个文件的 Block 存储位置。
画面14：IDE 中显示代码，光标位于 for 循环中，展示如何遍历每个 Block 的存储位置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Test
public void getFileSystem4() throws Exception{
    FileSystem fileSystem = FileSystem.newInstance(new URI("hdfs://node01:8020"), new Configuration());
    System.out.println(fileSystem.toString());
}
```

画面2：
```java
@Test
public void listMyFiles() throws Exception{
    FileSystem fileSystem = FileSystem.get(new URI("hdfs://192.168.52.250:8828"), new Configuration());
    RemoteIterator<LocatedFileStatus> locatedFileStatusRemoteIterator = fileSystem.listFiles(new Path("/"), true);
    while (locatedFileStatusRemoteIterator.hasNext()){
        LocatedFileStatus next = locatedFileStatusRemoteIterator.next();
        System.out.println(next.getPath().toString());
    }
    fileSystem.close();
}
```

画面3：
```java
@Test
public void getFileSystem4() throws Exception {
    FileSystem fileSystem = FileSystem.newInstance(new URI("hdfs://node01:8020"), new Configuration());
    System.out.println(fileSystem.toString());
}
```

画面4：
```java
@Test
public void getFileSystem4() throws Exception {
    FileSystem fileSystem = FileSystem.newInstance(new URI("hdfs://node01:8020"), new Configuration());
    System.out.println(fileSystem.toString());
}
```

画面5：
```java
RemoteIterator<LocatedFileStatus> iterator = fileSystem.listFiles(new Path("/"), true);
```

画面6：
```java
while (iterator.hasNext()){
    //获取每一个文件详细信息
    LocatedFileStatus fileStatus = iterator.next();
```

画面7：
```java
System.out.println(fileStatus.getPath().getFileName()); //hdfs://
```

画面8：
```java
System.out.println(blockLocations.length);
```

画面9：
```java
@Test
public void getFileSystem1() throws Exception {
    FileSystem fileSystem = FileSystem.get(new URI("hdfs://node01:8020"), new Configuration());
    System.out.println(fileSystem.toString());
}
```

画面10：
```java
@Test
public void getFileSystem1() throws Exception {
    FileSystem fileSystem = FileSystem.get(new URI("hdfs://node01:8020"), new Configuration());
    System.out.println(fileSystem.toString());
}
```

画面11：
```text
556071533781.jhist---job_15559081963_0001-1556074220928-root-QuasiMonteCarlo-155607456128-2-1-SUCCEEDED-default-1556074333781.jhist
```

画面12：
```text
D:\develop\jdk8.0\bin\java ...
hdfs://node01:8020/export/servers/hadoop-3.1.1/datas/jobsitory/DoneDats/2019/04/24/000000/job_1555938431963_0001-1556074220928-root-QuasiMonteCarlo-155607456128-2-1-SUCCEEDED-default-1556074333781.jhist
```

画面13：
```text
node01.hadoop.com
node02.hadoop.com
node03.hadoop.com
hdfs://node01:8020/export/servers/hadoop-3.1.1/datas/jobsitory/DoneDats/2019/04/24/000000/job_1555938431963_0001-1556074220928-root-QuasiMonteCarlo-155607456128-2-1-SUCCEEDED-default-1556074333781.jhist
```

画面14：
```java
for (BlockLocation blockLocation : blockLocations) {
    String[] hosts = blockLocation.get_hosts();
    for (String host : hosts) {
        System.out.println(host);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
