# 17.FastDFS环境搭建（java client使用）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\17.FastDFS环境搭建（java client使用）_【海量资源尽在 666java.com】.mp4
- 时长 4分9秒（音频 249s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们就来测试一下我们的这个FastDFS这个环境那我们就使用它的这个Java API呢来做一个测试那么首先呢我们需要导入我们的FastDFS Client这个API然后版本呢是1.26.7啊这样的一个版本那么同时呢我们需要把这个Logback这个依赖呢去做一个排除因为它会和我们的SpinBoot框架呢有冲突啊把它排除掉
[00:29] 好那么接下来呢我们就把它来导入一下那么我们还是进入到我们这个server这个工程那么在这个里面呢我们去找到我们的POM文件然后呢往这一丢这样的话呢我们这个依赖呢就拷贝进来了那么拷贝进来之后呢我们就来看一下相关的一些这个配置那我们需要在我们的application properties文件中嘛去添加一些关于我们这个fastdfs的一些相关的配置啊那么我们就丢到这吧
[00:59] 那么写错了应该是不是阿里云是这个然后我们往下面走这个是相关的一些配置那么其实关键的它的参数其实就是这个对吧就是我们这个trunk的一个地址那么是3181然后22122这样的一个地址而上面这个是我们的一些深层缩略图的
[01:25] 一些这个参数啊然后呢上面这个是我们的一些超时的时间它做了这样的一个设置好那么接下来呢我们就来编写这个测试代码去来测试一下那么我们来找到我们的一个测试用力啊那么我们来找一下那么我们来测试一下它那么我们把这个代码呢我们来拷贝到我们这个server下面来那么拷进来之后啊
[01:50] 那么下面呢我们就来做一个测试那么在这个位置可以看到呢我们注入了一个我们这个fast fail的一个storage client一个客户端然后呢我们通过这个client呢去做一个upload fail去做一个上传那么在这呢我们指定它是一个这个fail文件那么这个文件呢我们来看一下这个文件我们应该是存在的我就打个浏览器吧直接来做一个访问
[02:18] 那么OK这个文件呢是存在的对吧好那么接下来我们就尝试着把这个文件呢去上传到我们的这个fastDFS中那么我们来看一下需要这么几个参数啊那么首先第一个这个是给他一个inputStream按流然后给他一个文件的长度再给一个什么的扩展名在metadata我们就不做一些这个设置就是我们可以去设置原数据啊都可以丢到这个里面来比如说设置他的一些
[02:45] 这个它的宽是多少啊高是多少啊这样的一些数据去存储进去也是可以的好那么下面呢我们就打印它的这个路径啊还有它的一些这个ful pass啊我们一起来看一下啊好那我们来执行一下走好那我们来等待它的一个执行好那么到现在呢我们就已经上传成功了那么接下来呢我们就来测试一下啊呃那么这个其实就是他打印出来一些内容啊他的group呢是group1然后呢pass呢是这样的一个路径
[03:14] 然后这个是它的一个全路径我们来尝试的去访问一下全路径看是否能够访问到这张图片我们需要输入的是谁就是我们的http然后冒号双斜杠19168然后31.81下面什么就4个8我们是给它设置了有4个8这样的一个端口然后把这个地址就拷贝过来走那么会发现是不是也可以去访问到
[03:43] 我们这样的一个图片那么它是访问的ngxngx再去访问我们的fastdfs这样的一个文件系统那么就可以去查询到这样的一个图片了那么就说明我们这个fastdfs环境是不是就已经搭建好了ok好那么关于我们这个fastdfs的一个java client的使用我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中集成 FastDFS 客户端，配置分布式文件系统，并通过单元测试上传文件验证功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中关于 Java 客户端的 Maven 依赖配置，包含 FastDFS 客户端和排除 logback-classic 依赖。
画面2：在 IntelliJ IDEA 中展示 my-tanhua-server 项目的 pom.xml 文件，其中包含 FastDFS 客户端依赖和排除配置。
画面3：同画面2，展示 pom.xml 文件中 FastDFS 客户端依赖和排除配置。
画面4：展示 application.properties 文件中的 FastDFS 配置，包括连接超时、跟踪器列表等。
画面5：展示 TestFastDFS.java 测试类的开头部分，导入 FastDFS 客户端和 Spring Boot 测试相关包。
画面6：在测试类中，展示上传文件的代码逻辑，包括获取文件路径、创建 File 对象、调用 uploadFile 方法。
画面7：展示上传文件的代码逻辑，包括获取文件路径、创建 File 对象、调用 uploadFile 方法。
画面8：展示上传成功后，浏览器中显示的图片内容。
画面9：展示上传文件的代码逻辑，包括获取文件路径、创建 File 对象、调用 uploadFile 方法。
画面10：展示测试通过，控制台输出上传成功的路径信息。
画面11：展示上传成功后，浏览器中显示的图片内容。
画面12：展示浏览器中点击图片链接后，显示的图片内容。
画面13：展示浏览器中点击图片链接后，显示的图片内容。
画面14：展示 Typora 文档中关于 Java 客户端的 Maven 依赖配置，包含 FastDFS 客户端和排除 logback-classic 依赖。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependency>
    <groupId>com.github.tobato</groupId>
    <artifactId>fastdfs-client</artifactId>
    <version>1.26.7</version>
    <exclusions>
        <exclusion>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

画面2：
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
</dependency>
<dependency>
    <groupId>com.github.tobato</groupId>
    <artifactId>fastdfs-client</artifactId>
    <version>1.26.7</version>
    <exclusions>
        <exclusion>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

画面4：
```properties
#分布式文件系统FDFS配置
fdfs.so-timeout = 1501
fdfs.connect-timeout = 601
#缩略图生成参数
fdfs.thumb-image.width = 150
fdfs.thumb-image.height = 150
#TrackerList参数，支持多个
fdfs.tracker-list=192.168.31.81:22122
```

画面5：
```java
package com.tanhua.server;

import com.github.tobato.fastdfs.domain.fdfs.StorePath;
import com.github.tobato.fastdfs.Service.FastFileStorageClient;
import org.apache.commons.io.FileUtils;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import java.io.File;
import java.io.IOException;
```

画面6：
```java
try {
    StorePath storePath = this.storageClient.uploadFile(FileUtils.openInputStream(file), file.length(), "jpg", null);
    System.out.println(storePath); //StorePath [group-group1, path-MOO/00/00/wKgfUV2GJsuAOUd_AAHnjh7KpOc1.1.jpg]
    System.out.println(storePath.getFullPath()); //group1/MOO/00/02/wKgfUV2GJsuAOUd_AAHnjh7KpOc1.1.jpg
} catch (IOException e) {
    e.printStackTrace();
}
```

画面7：
```java
@Test
public void testUpload() {
    String path = "C:\\Users\\zhijun\\Desktop\\pics\\1.jpg";
    File file = new File(path);
    try {
        StorePath storePath = this.storageClient.uploadFile(FileUtils.openInputStream(file), file.length(), "jpg", null);
        System.out.println(storePath); //StorePath [group-group1, path-MOO/00/00/wKgfUV2GJsuAOUd_AAHnjh7KpOc1.1.jpg]
        System.out.println(storePath.getFullPath()); //group1/MOO/00/02/wKgfUV2GJsuAOUd_AAHnjh7KpOc1.1.jpg
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

画面10：
```text
Tests passed: 1 of 1 test
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

