# 12-HDFS的API操作-获取FileSystem其他方式

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\12-HDFS的API操作-获取FileSystem其他方式【海量资源尽在 ubkz.com】.mp4
- 时长 6分6秒（音频 366s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 学习完第一种获取文件系统的方式之后呢咱们接下来再看其他方式这里边呢还有其他三种方式我们来看第二种第二种呢是使用fail system这个类呢然后有个get方法这里边new了一个uri这个uri呢它的意思就是统一资源标示符它呢其实就是一个路径这个指定了我们NameNode所在的一个主机还有呢一个端口8020
[00:29] 那第二个参数呢你有一个configurationOK这两个参数合在一起我们就可以得到一个fail system来我们来看一下好打开这里咱们呢接下来是获取文件系统第二种方式咱们把这个呢直接把这个模板拷过来好这里呢我改成2然后呢咱们这里边首先呢我们可以用个fail system这个包一定要导对然后呢获取
[01:02] 一个get需要new个UI这个UI呢来指定一个分布式文件系统一个路径node01然后呢8020那后面呢这个地方呢我们需要去new一个configuration对象我们new一个configuration这样子的话呢我们就得到了一个fail system这里边有一个这里边呢我把这个异常呢已经抛出了这里边有个异常
[01:34] OK我们直接呢打印这个fail systemOK你可以调个to stream来我们来试一下这个异常是吧我抛一下我们来测试一下走好稍等你看我们这个也可以的这是第二种方式那咱们接下来再看第三种这个第三种方式呢你乍一眼看呢你发现它和第一种是不是很类似呀其实这个地方呢有点不一样的是
[02:09] 我们第一种呢在fail system调的方法叫get而这个里边呢是调的instancenew instance其实是差不多的OK这种方式那我也给大家去来演示一下这是第三种方式好我们来同样的把这个呢模板直接拷过来一份我直接先抛一个大的一场然后我们来测一下这个地方是写3好那么首先呢我们需要new一个configuration对象
[02:53] 然后呢对这个configuration对象进行设置set一个什么东西呢我们来看set一个dfs default fs这是一个参数的名字fs.default dfalt fsOK那么我们指定的文件系统是什么呢就是hdfs冒号杠杠node01然后呢8020
[03:21] 好设置完之后呢接下来我们需要通过fail system来去new instance来创建一个fail system的一个实例一个对象把你刚才的configuration给它它呢也可以获取这个文件系统fail system咱们也可以直接打印一下fail system或者说你直接打印或者调图形都可以来我们来试一下这是第三种稍等这种也是可以的
[04:00] 那接下来呢我们再看第四种第四种方式把这个模板呢也是直接卡过来然后呢改成getFailSense4这个第四种方式呢我们来看一下第四种方式和第二种也很像第二种呢它调的是get方法而这种调的是new instance就这点差别来我们来看一下那么首先呢new instance
[04:37] 第一个需要new一个UI第二个需要new一个configuration然后最后打一下它的一个对象我们来看failsetum它有个方法叫new instance这个new一个URI我们还是写hdfs-node01-8020第二个参数我们在这里需要去new一个configuration对象
[05:08] 你有一个configuration对象来拿到这个发挥值OK我们来直接打印failsetup to stream好这也是可以的我们来试一下最后一种好稍等OK这个也没有问题那么这四种呢你可以挑一个你自己觉得比较擅长的一种这四种都是可以的你比如说呢第一种它的思路很清晰我们指定一个自己的文件系统而第二种方式呢它的语法比较简化OK
[05:45] 这是四种获取fail system的方式那么获取完fail system之后呢接下来我们就可以对这个文件系统的数据呢进行增删改查好那关于它的获取方式呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileSystem;
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
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileSystem;
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
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileSystem;
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
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileSystem;
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
Configuration (org.apache.Hadoop.conf)
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

