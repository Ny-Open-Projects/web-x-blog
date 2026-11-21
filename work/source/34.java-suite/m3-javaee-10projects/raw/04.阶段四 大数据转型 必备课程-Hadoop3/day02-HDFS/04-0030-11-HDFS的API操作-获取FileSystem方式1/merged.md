# 11-HDFS的API操作-获取FileSystem方式1

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\11-HDFS的API操作-获取FileSystem方式1【海量资源尽在 ubkz.com】.mp4
- 时长 13分7秒（音频 788s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 配置好Windows的Hadoop环境之后接下来我们通过Java API来操作HDFS首先我们来打开ID在这里我已经提前创建了一个空的project在这里我需要在这个project之上创建一个model我们来选择Maven在这里我就不勾选股价直接点next好在这里我们给它一个group ID就是CNDR
[00:29] idcast好这个artific ID我写成day02表示第二天然后呢我们来去操作是hdfs API好点next好点finish稍等让它构建好构建完成之后呢接下来我们去导入这个maven的一些依赖我可以把这个呢直接复制好复制一下
[01:05] 然后呢放在我们的pom.xml里面导入Maven的依赖仓库OK那在这里呢我们来简单看一下从上到下首先呢这个地方repository这个地方指定我们加尔包的一个下载地址而在这个dependent这个依赖里边呢我们导入这个Hadoop commonHadoop HDFSHadoop client还有呢一个ginunit单元测试下面是它有一些插件而在这里呢
[01:35] 我规定了我们的编译的一个JDK是1.8的还有打包的一个插件叫Mainware Sheet PluginOK 把这个导进去之后接下来我们开始写代码写代码怎么去写首先我们来看我们要通过Java来操作HDFS要涉及到两个类一个叫Configuration一个叫Fail System这个Configuration
[02:05] 它主要是呢来封装了一些客户端和服务器的配置信息而这个failsetter呢它是一个代表一个文件系统所谓的文件系统呢就是来去描述文件的管理方式它是一个抽象类那它呢有很多的子类那这个failsetter我们要去得到OK那接下来呢我们来看这个获取failsetter的几种方式就是我要去操作HDFS
[02:34] 首先第一件事情我要获取这个file system也就是文件系统我拿到了这个文件系统呢我就相当于拿到了我们的这个系统中所有的原数据信息所以这个file system非常重要而要去获取这个file system呢又有四种方式我们先一个一个来看第一种方式我们呢需要去创建一个configuration对象
[03:03] 然后呢对这个configuration对象呢做一个设置指定我们的文件系统我们用的是HDFS也就是分布式文件系统那接下来通过这个呢configuration对象来获取我们指定的文件系统然后呢最后我们可以打一下这个文件系统呢是否获取成功大概是这么一个思路来接下来我们把这个代码呢给大家实现一下好在这里呢我建一个包
[03:33] new一个packet然后呢写上cn.itcast.hdfs好在这里呢我写一个类写个类那这个类呢是叫hdhdfs然后呢写上hdfsapiapistudyOK写这么一个类apistudyOK写这么一个类
[04:06] 好写这个类之后呢接下来我们需要在这里呢写一些测试类那首先我们写第一个public这个void那第一个类呢我们起个名字叫getFailSystem1表示第一种获取FailSystem的一个方式getFailSystem1OK好了那如何去获取这个文件系统呢来我们来看一下第一步
[04:35] 我们需要去创建一个configuration对象这个configuration里边封装了我们HDFS客户端和服务器的信息我们来new一个configuration好 这个里边选这个来 我们来configurationGUI configuration我们来看我们要导入这个OAGI Apache Hadoop configure这个包一定要导这个包来 我们生成一个反馈值
[05:05] 好这个对象就创建成功了这个对象呢有了之后呢来咱加个注释吧第一步获取configuration对象第二步我们需要对这个对象的进行设置设置我们的configuration对象那设置什么呢设置就是设置的目的是来指定我们要操作的
[05:47] 文件系统怎么设置呢它有一个方法叫set这个set有两个参数来我们来看一下这个set呢有两个参数第一个呢它是一个固定的值叫fs default fs我把它直接复制过来OK那第二个呢表示我们要去操作的一个文件系统那这个写法呢是这样写的hdfs 冒号 杠杠node01 8020来我们来看一下
[06:19] 第二个写HDFS冒号杠杠Node01冒号8020来我们来解释一下HDFS呢表示我们操作的是分布式文件系统这个Node01呢表示我们原数据的节点呢在Node01这台机子上大家注意这个地方既可以写个Node01也可以写上你的IP地址192.168.174.
[06:49] 100这个也可以你写这个没问题你写node01也没问题但是注意你写node01的前提是你必须在windows里边呢配一个IP和域名的映射不知道大家还记不记得这个映射在哪里配呢在我们的C盘C盘里边呢有一个windowswindows里边有一个system32给大家提一下system32
[07:19] System32里面有一个叫driversdrivers里面一个etcetc里面一个hosts这么一个文件好打开我们需要在这里去配置一个node01好了那这个我就关了好在这里我们可以写node01好那么这个写完之后呢大家注意相当于我们这个configuration呢又设置好了就指定我要操作是我们的一个分布式文件系统
[07:47] 大家注意如果你没有写这句话那其实这个configuration有个默认的值一个configure有个默认的值这个默认的是什么呢我们先继续写待会给大家分析一下好了那接下来第三步干嘛呢我们要去获取指定的一个文件系统获取我们指定的文件系统那这个时候呢我们需要用一个类这个类呢就是fail systemfail system
[08:22] 好这个包一定要导阿帕奇的包一个方法这个方法叫get你会看到这个get里边要的就是这个configuration对象我可以把configuration直接给他然后呢拿到了跑个一场拿到了就是一个fail see timer这个就是我们需要的一个文件系统好大家请注意拿到这个文件系统你可以理解成已经拿到了node01这个
[08:51] 主机上的所有的元数据信息获取fail system就相当于获取了这个主节点中主节点中所有的元数据信息你就可以这样理解那么拿到这个之后接下来我们可以直接打印一下这个地方我们可以打印fail system我们来直接fail system
[09:31] 然后调个toString方法来试一下好 我们来测一下这个代码呢能否可以运行为了测试这个代码呢我们直接加一个单元测试test好了 加这么一个单元测试来 我们来测一下来 走稍等只要这个对象呢可以打得出来说明我们和我们的服务器之间呢已经接点连接了好了 稍等他说呢这个地方请根据这个地方有一个有一个问题
[10:02] 我们来看这个问题是怎么造成的稍等一下我们再来运行一下再来点一下稍等稍等一下它已经运行了你看这个地方已经把这个对象打出来了好打出来之后说明我们和这个node01这台机子已经建立了一个连接已经获取了这个文件系统好你看到上面有一个有一个log4g的一个警告这个警告信息
[10:32] 是因为它内部需要一个log4g的日志服务而我们这里并没有去配置log4g如果你不想看到这个警告信息我可以给大家说一下怎么去做我们可以在这个资料里边我给你提供一个log4g的properties这么一个配置文件我们可以点开看一下这是log4g的日志页配置我们可以直接把这个配置然后放在我们的resource目录直接粘一下
[11:01] 粘贴了之后呢不用管这里边它写了什么内容好来直接走一下稍等稍等哎你看这个时候呢它就没有这个警告了好这个是我们获取一个文件系统的一种方式我刚才给大家提了一个问题我说这个地方你必须设置如果你不设置呢这个configuration呢有一个默认值我们来看一下这个默认值是什么好要想看这个默认值呢我们需要去看看fail system这个get方法
[11:34] 我们按住Ctrl键点进去好 稍等好 点进去之后呢这个get呢又掉了另外一个get我们再点进去好 点进之后呢这里边呢有一个有一个fail system我们来看能不能获取我们想要的信息好 这地方呢我再回来好 这地方是一个get方法好 get方法之后呢它掉了这个get那掉了这个get之后呢咱们来进行看这个好 进这个方法
[12:05] 这个方法里边你会发现它这为一个fs default fs这个就是我们刚才呢在这里指定了这么一个参数这个是文件系统它的一个名字那后面呢跟的是一个fail杠杠杠这个fail杠杠呢代表的是一个本地文件系统也就操作我们本地的一个文件那也就是如果说呢你不对它configuration做一个设置它默认是操作本地的文件
[12:34] 所以说我们在这里需要对它做一个重新的设置不让它去操作我们的本地文件而是操作一个HDFS的文件OK这就是我们设置这句话的目的好这是我们的第一种方式就是获取文件系统的第一种方式好那接下来还有其他方式我们依次给大家来再讲一下我先把这个先停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Windows 系统中配置 Hadoop 环境并使用 Java API 获取 HDFS 的 FileSystem 对象。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 HDFS API 操作章节，列出在 Windows 系统配置 Hadoop 的四个步骤，其中第一步是将 apache-Hadoop-3.1.1 文件夹解压到无中文空路径，第二步是设置 HADOOP_HOME 环境变量，第三步是将 Hadoop.dll 放入 C:\Windows\System32，第四步是关闭 Windows 防火墙。
画面 2: 展示了 Maven 依赖配置，重点是添加 Hadoop 的 common、hdfs、hdfs-client 三个模块的依赖，版本号为 3.1.1。
画面 3: 展示了在 IDEA 中导入 Maven 项目，背景任务显示正在导入和更新索引。
画面 4: 展示了 Maven 依赖配置，重点是添加 Hadoop 的 common、hdfs、hdfs-client 三个模块的依赖，版本号为 3.1.1。
画面 5: 展示了获取 FileSystem 的两种方式，第一种方式是通过 Configuration 设置 fs.defaultFS，然后调用 FileSystem.get(configuration)。
画面 6: 展示了在 IDEA 中编写 Java 代码，提示需要导入 org.apache.Hadoop.fs.FileSystem 包。
画面 7: 展示了在 Windows 系统中打开 C 盘，准备解压 Hadoop 文件。
画面 8: 展示了获取 FileSystem 的两种方式，第一种方式是通过 Configuration 设置 fs.defaultFS，然后调用 FileSystem.get(configuration)。
画面 9: 展示了在 IDEA 中编写 Java 代码，提示需要导入 org.apache.Hadoop.fs.FileSystem 包。
画面 10: 展示了运行 Java 程序，输出了 FileSystem 的信息，显示了 HDFS 的连接信息。
画面 11: 展示了在 Windows 系统中打开 C 盘，准备解压 Hadoop 文件。
画面 12: 展示了运行 Java 程序，输出了 FileSystem 的信息，显示了 HDFS 的连接信息。
画面 13: 展示了 Hadoop 的源码，显示了 FileSystem 类的 get 方法的实现。
画面 14: 展示了运行 Java 程序，输出了 FileSystem 的信息，显示了 HDFS 的连接信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
第一步：将apache-Hadoop-3.1.1文件夹解压到一个没有中文空路的路径下面
第二步：在windows上面配置Hadoop的环境变量：HADOOP_HOME
第三步：把目录下的Hadoop.dll文件放到系统盘里面去：C:\Windows\System32
第四步：关闭windows防火墙
```
画面 2:
```xml
<repositories>
    <repository>
        <id>cloudera</id>
        <url>https://repository.cloudera.com/artifactory/cloudera-repos/</url>
    </repository>
</repositories>
<dependencies>
    <dependency>
        <groupId>org.apache.Hadoop</groupId>
        <artifactId>Hadoop-common</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.Hadoop</groupId>
        <artifactId>Hadoop-hdfs</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.Hadoop</groupId>
        <artifactId>Hadoop-hdfs-client</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```
画面 3:
```
Importing Maven projects
Updating indices
Configuring Maven projects
```
画面 4:
```xml
<repositories>
    <repository>
        <id>cloudera</id>
        <url>https://repository.cloudera.com/artifactory/cloudera-repos/</url>
    </repository>
</repositories>
<dependencies>
    <dependency>
        <groupId>org.apache.Hadoop</groupId>
        <artifactId>Hadoop-common</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.Hadoop</groupId>
        <artifactId>Hadoop-hdfs</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.Hadoop</groupId>
        <artifactId>Hadoop-hdfs-client</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```
画面 5:
```java
@Test
public void getFileSystem1() throws IOException {
    Configuration configuration = new Configuration();
    //设置Configuration对象，设置的目的是来指定我们要操作的文件系统
    configuration.set("fs.defaultFS", "hdfs://node01:8020");
    //获取我们指定的文件系统，获取FileSystem就相当于获取了主节点中所有的元数据信息
    FileSystem fileSystem = FileSystem.get(configuration);
    System.out.println("fileSystem:"+fileSystem.toString());
}
```
画面 6:
```
new Con
```
画面 7:
```
Windows (C:)
```
画面 8:
```java
@Test
public void getFileSystem1() throws IOException {
    Configuration configuration = new Configuration();
    //设置Configuration对象，设置的目的是来指定我们要操作的文件系统
    configuration.set("fs.defaultFS", "hdfs://node01:8020");
    //获取我们指定的文件系统，获取FileSystem就相当于获取了主节点中所有的元数据信息
    FileSystem fileSystem = FileSystem.get(configuration);
    System.out.println("fileSystem:"+fileSystem.toString());
}
```
画面 9:
```
import org.apache.Hadoop.fs.FileSystem;
import org.junit.jupiter.api.Test;
```
画面 10:
```
log4j:WARN No appenders could be found for logger (org.apache.Hadoop.metrics2.lib.MutableMetricsFactory).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/fap.html#noconfig for more info.
fileSystem:DFSClient[clientName=DFSClient_NONMAPREDUCE_1851825033_1, ugi=lift (auth:SIMPLE)]
Process finished with exit code 0
```
画面 11:
```
Best (E:)
```
画面 12:
```
log4j:WARN See http://logging.apache.org/log4j/1.2/fap.html#noconfig for more info.
fileSystem:DFSClient[clientName=DFSClient_NONMAPREDUCE_1851825033_1, ugi=lift (auth:SIMPLE)]
Process finished with exit code 0
```
画面 13:
```java
if (scheme == null && authority == null) {
    return get(conf);
} else {
    if (scheme != null && authority == null) {
        URI defaultUri = getDefaultUri(conf);
        if (scheme.equals(defaultUri.getScheme()) && defaultUri.getAuthority() == null) {
            return get(defaultUri, conf);
        }
    }
}
String disableCacheName = String.format("fs.%s.impl.disable.cache", scheme);
if (conf.getBoolean(disableCacheName, false)) {
    LOGGER.debug("Bypassing cache to create filesystem {}", uri);
    return createFileSystem(uri, conf);
} else {
    return CACHE.get(uri, conf);
}
```
画面 14:
```
D:\develop\jdk8.0\bin\java ...
fileSystem:DFSClient[clientName=DFSClient_NONMAPREDUCE_352001840_1, ugi=lift (auth:SIMPLE)]
Process finished with exit code 0
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5: PPT 标题为“1.9.3 获取 FileSystem 的几种方式”，内容包括“第一种方式”和“第二种方式”。
画面 8: PPT 标题为“1.9.3 获取 FileSystem 的几种方式”，内容包括“第一种方式”和“第二种方式”。
画面 12: PPT 标题为“1.9.3 获取 FileSystem 的几种方式”，内容包括“第一种方式”和“第二种方式”。
画面 14: PPT 标题为“1.9.3 获取 FileSystem 的几种方式”，内容包括“第一种方式”和“第二种方式”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

