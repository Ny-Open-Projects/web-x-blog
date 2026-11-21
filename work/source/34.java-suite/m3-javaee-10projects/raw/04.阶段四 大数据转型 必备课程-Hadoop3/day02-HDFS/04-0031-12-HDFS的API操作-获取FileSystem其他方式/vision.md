# 画面线理解：12-HDFS的API操作-获取FileSystem其他方式

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\12-HDFS的API操作-获取FileSystem其他方式【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:47, 01:06, 01:37, 02:02, 02:23, 02:57, 03:28, 03:54, 04:22, 04:47, 05:09, 05:32, 05:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:18:00

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中通过不同方式获取 HDFS 文件系统实例，包括使用 URI、Configuration 对象和默认配置等方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 HDFS API 获取文件系统实例的三种方式的代码示例。
- 第一种方式：通过 Configuration 对象和 URI 获取 FileSystem。
- 第二种方式：通过 URI 和 new Configuration() 获取 FileSystem。
- 第三种方式：通过 Configuration 对象设置属性后，调用 newInstance() 获取 FileSystem。

画面 2：
- 展示了第一种方式的完整代码：使用 new Configuration() 创建 Configuration 对象，设置 "fs.defaultFS" 属性为 "hdfs://node01:8020"，然后调用 FileSystem.get() 获取 FileSystem 实例。

画面 3：
- 展示了第一种方式的代码，光标位于 FileSystem.get() 方法的参数部分，准备输入 URI 和 Configuration。

画面 4：
- 展示了第一种方式的完整代码，光标位于 System.out.println() 方法的括号内，准备输入 fileSystem.toString()。

画面 5：
- 展示了 HDFS API 获取文件系统实例的四种方式的代码示例。
- 第一种方式：通过 Configuration 对象和 URI 获取 FileSystem。
- 第二种方式：通过 URI 和 new Configuration() 获取 FileSystem。
- 第三种方式：通过 Configuration 对象设置属性后，调用 newInstance() 获取 FileSystem。
- 第四种方式：通过 URI 和 new Configuration() 获取 FileSystem。

画面 6：
- 展示了第一种方式的完整代码，光标位于 System.out.println() 方法的括号内，准备输入 fileSystem.toString()。

画面 7：
- 展示了 Configuration 类的常用方法，包括 set、setBoolean、setDouble、setEnum 等。

画面 8：
- 展示了第三种方式的完整代码：创建 Configuration 对象，设置 "fs.defaultFS" 属性，然后调用 FileSystem.newInstance(configuration) 获取 FileSystem 实例。

画面 9：
- 展示了第三种方式的完整代码，光标位于 System.out.println() 方法的括号内，准备输入 fileSystem.toString()。

画面 10：
- 展示了 HDFS API 获取文件系统实例的四种方式的代码示例。
- 第一种方式：通过 Configuration 对象和 URI 获取 FileSystem。
- 第二种方式：通过 URI 和 new Configuration() 获取 FileSystem。
- 第三种方式：通过 Configuration 对象设置属性后，调用 newInstance() 获取 FileSystem。
- 第四种方式：通过 URI 和 new Configuration() 获取 FileSystem。

画面 11：
- 展示了 HDFS API 中 FileSystem 类的常用方法，包括 open、close、mkdir、delete 等。

画面 12：
- 展示了第四种方式的完整代码：通过 URI 和 new Configuration() 获取 FileSystem 实例。

画面 13：
- 展示了第一种方式的完整代码，光标位于 System.out.println() 方法的括号内，准备输入 fileSystem.toString()。

画面 14：
- 展示了第一种方式的完整代码，光标位于 System.out.println() 方法的括号内，准备输入 fileSystem.toString()。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
configuration.set("fs.defaultFS", "hdfs://node01:8020");
//获取指定的文件系统
FileSystem fileSystem = FileSystem.get(configuration);
System.out.println(fileSystem.toString());
```

画面 2：
```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

public class HdfsApiStudy {
    //获取文件系统的第 一种方式
    @Test
    public void getFileSystem1() throws IOException {
        Configuration configuration = new Configuration();
        //设置Configuration对象，设置默认的FS，来指定我们要操作的文件系统
        configuration.set("fs.defaultFS", "hdfs://node01:8020");
        //获取我们指定的文件系统，获取FileSystem相当于获取了上节点中所有的元数据信息
        FileSystem fileSystem = FileSystem.get(configuration);
        System.out.println(fileSystem.toString());
    }
```

画面 3：
```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

public class HdfsApiStudy {
    //获取文件系统的第 一种方式
    @Test
    public void getFileSystem2() throws IOException, URISyntaxException {
        FileSystem fileSystem = FileSystem.get(new URI("hdfs://node01:8020"), new Configuration());
        System.out.println(fileSystem.toString());
    }
```

画面 4：
```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

public class HdfsApiStudy {
    //获取文件系统的第 一种方式
    @Test
    public void getFileSystem2() throws IOException, URISyntaxException {
        FileSystem fileSystem = FileSystem.get(new URI("hdfs://node01:8020"), new Configuration());
        System.out.println(fileSystem.toString());
    }
```

画面 5：
```java
@Test
public void getFileSystem2() throws Exception{
    FileSystem fileSystem = FileSystem.get(new URI("hdfs://node01:8020"), new Configuration());
    System.out.println("fileSystem:"+fileSystem);
}

@Test
public void getFileSystem3() throws Exception{
    Configuration configuration = new Configuration();
    configuration.set("fs.defaultFS", "hdfs://node01:8020");
    FileSystem fileSystem = FileSystem.newInstance(configuration);
    System.out.println(fileSystem.toString());
}

@Test
public void getFileSystem4() throws Exception{
    FileSystem fileSystem = FileSystem.newInstance(new URI("hdfs://node01:8020"), new Configuration());
    System.out.println(fileSystem.toString());
}
```

画面 6：
```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

public class HdfsApiStudy {
    //获取文件系统的第 一种方式
    @Test
    public void getFileSystem2() throws IOException, URISyntaxException {
        FileSystem fileSystem = FileSystem.get(new URI("hdfs://node01:8020"), new Configuration());
        System.out.println(fileSystem.toString());
    }
```

画面 7：
```java
Configuration (org.apache.hadoop.conf)
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprecationDelta
ConfigurationWithLogging
ConfigurationWithDeprec
