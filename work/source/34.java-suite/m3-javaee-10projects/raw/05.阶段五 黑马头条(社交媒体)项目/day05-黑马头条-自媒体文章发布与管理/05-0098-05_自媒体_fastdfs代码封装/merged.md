# 05_自媒体_fastdfs代码封装

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\05_自媒体_fastdfs代码封装【海量资源尽在 666java.com】.mp4
- 时长 9分10秒（音频 551s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续讲刚才咱们是把登录的功能给做完了啊现在咱们已经能登录到当前的系统中了那不过呢这个页面呢咱们现在还没有数据啊所以说现在你什么也查看不了只能是登录进来然后呢咱们要去做第二个功能就是有一个素材上传其实呢最终的这个素材上传的都是为了当前文章发布做准备那首先呢咱们要说理解一下当前这个素材上传接口再去说这个需求啊
[00:30] 即使现在有页面你可以打开当前的页面里边有一个内容管理内容管理里边咱们在发布文章之前会有一个叫做素材管理因为发布文章里边有些图片咱们需要先去上传图片之后在你发布文章的时候需要从素材库中去找到当前的图片再去发送咱们点一下当前的页面它会跳到这当然目前的话它是没有数据的也找不到请求的URL这个无所谓
[00:55] 当然咱们现在要做的第一个功能呢就是先去上传图片点一下它会弹一个窗然后呢你可以选择图片然后比如选选择一个啊点开始上传这时候呢就能去把当前图片展示到这这时候呢就能在这去查看当前你的素材库里边的图片素材库的图片那这图片呢咱们要再去说一下你要上传图片的话呢首先呢你得先去准备环境那这环境呢是这样啊咱们首先呢用的是当前的一个什么
[01:26] 用的是当前的一个fast dfs就是阿里的一个分布式文件存储系统那这个存储系统咱们在之前的课上已经讲过了所以说这块的环境就不再去说了咱们主要是在课堂上该怎么去用当前的fast dfs怎么去连上咱们会去进行封装好吧那关于这环境我在这已经准备好了就在这这有一个当前的服务器就是一个fast dfs我的地址是192.168.25.133
[01:54] 行那咱们呢下面呢就来去封装当前的环境啊还是打开单本啊咱们可以参考着当前的笔记去做首先呢你要先去引入当前的栅包啊这个栅包咱们已经引入了啊你要在你的common中去引入这些其实这个大家都知道啊咱们后续如果说再用到其他技术的时候基本上都会在当前common中去集成去封装好吧行那这个啊
[02:22] 其实这个在咱们comment中已经有了你也不用去拷贝了你可以查看一下比如打开当前的comment把这些钱都没用的关掉然后你可以去找一找有一个fastdbs一个starter找一找两个这有一个fastsprint fastdbssprintbootstarter行咱们就再去往下看这时候包都倒进来了然后下面有一个配置文件咱们需要去创建一下
[02:57] 那这创建的就是在在当前的靠门下边去创建这么一个配置文件啊就是封装的过程呢咱们已经已经封装过好几个技术了这个套路大家应该能够熟悉啊在这啊我这已经有了是吧有了无所谓啊那这个已经创建了如果说你没有的话你就创建一个啊啊就把当前的地址给拷贝过来就可以了那这个呢其实就在这当然这个地址啊他默认是212啊他这个地址的话呢你要根据你自己的服务器的情况
[03:25] 把这地址去拷贝一下当然我今天也会把当前的服务器打包打包完之后放到今天的资料夹资料的文件夹中这时候你们也可以直接去挂载直接去挂载就可以了行这个已经有了既然这时候咱们就可以再继续往下走了好下面咱们要去封装一些配置配置的话其实也比较简单就是说咱们要去怎么去连上当前的发扫地板
[03:55] 就咱们在之前学的时候应该说过啊这个呢其实就是咱们要去设置一些什么东西啊设置一些tracker的client啊去连接因为tracker呢最终啊咱们要去上传文件或者下载的时候呢都要去先去找到谁啊找到tracker然后最终的tracker是帮你去连接storage然后再去再去连上你的呃叫文件服务器对吧所以说这块啊咱们内容先考过来啊直接去从这考过来好考备完之后呢咱们在这啊再创建一个包
[04:28] 那叫FastDFS好吧区分一下啊FastDFS好这是然后呢在这把这个类拷进来拷进来之后呢大家能看得懂啊把包里面都倒一下啊倒入倒入下面这也是也是LongBlock啊好倒入完之后啊咱们再往下看啊行啊这个也要倒入啊就是FastDFS里边然后下面是这边是找一个overlay的
[05:06] 这也是稍等啊他应该是能够反应过来你看他现在是缺失但是现在咱们已经有了啊那这个的话其实无所谓啊这个的话咱们在现在暂时不用考虑因为咱们一会儿还会再去设置一些东西好那咱们呢现在呢就可以简单的去读一下当年的配置文件啊那首先呢这个就不用说了是吧然后下面这个是一个配置类然后他会去读取当前的这是个前缀是吧读取当年的配置文件
[05:42] Fast-DFS-Properties然后这个是他这个简准咱们可以看一下他的简准Fast.DFS是吧后面是连接的超时时间是吧还有一些什么server最终的最终咱们会去创建一个连接池这连接池的话其实他就需要当前的一个连接servechart最终你是怎么去连上的最终连怎么去连上的咱们都需要去设置好吧
[06:08] 行那这个设置完之后啊设置完之后啊就这个关系大家应该能看明白啊来看一下啊在这啊先去创建了一个当前的连接池啊是设置了一些参数然后最终呢咱们要去创建连接的时候啊咱们需要当前的连接池这连接池的话其实就是上面这个就上面这个啊就上面的反馈因为因为他这下了个病是吧所以说呢这个只要是死病容器中存在的你都可以通过
[06:34] 当前的型餐去注入进来然后最终的这块需要用到的时候咱们可以直接直接去使用最终最终你看这是不是return了一个new当前有个travel的client管理器最终他这一个sbin就把它放到了spin的容器中对吧没问题啊行那这个加完之后啊咱们在这还有一个配置类咱们还要再去说一下啊这个配置类呢其实就是为了方便能够在客户中或者在在门项目中更方便的去使用里边呢是封装了一些
[07:04] 增伤改查的方法我们一块来我背下还是考到当前的包下边来加上之后你看一下首先这是一个compound就是让Spring去管理对吧这是一个fast device clientOK咱们来看然后下面是有一个uploadOK这时候你可以去上传可以上传的方法你可以在这去写把它给好着下包下包大家怎么上传这有一个storage client这个client其实就是谁
[07:36] 其实就是当前的这个client看到了吗就是他的client好再往下看然后下面还有啥下面还有一些就是上传的方法是吧你可以根据不同的参数去上传还有吗还有下载下载还有删除还有删除行那这些方法咱们用到的时候怎么办想用的时候就可以直接在项目中去注入当前fastDFSclient就可以了当然刚才说了
[08:07] 在咱们当前的黑马头条这种自媒体的里边呢有发布文章里边有个素材管理咱们需要去用到上传所以说要去集成当前那个发财地板4是不是很容易啊怎么办是不是在你的当前media中在这啊去加一个新的配置怎么加呀在这去写一个东西吧写个类啊咱们叫FS好吧FS Compute
[08:41] 也可以这样为了方便一些你可以在这个init里边直接去加也可以比如说你在这去加一个数组是可以加入多个的可以再去扫描另外一个包是可以的com.黑马谁com.busbfs这样也行这样也行这时候你要去用的话你直接去注入当前这个类当前这个类就可以了好吧行那这个封装的咱们就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Spring Boot 项目中集成 FastDFS 文件存储服务，包括配置文件、自动配置类、客户端工具类的编写与使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档内容，标题为“4.2 素材上传接口”下的“4.2.2 接口定义”，包含接口标准信息：接口名称 /api/v1/media/material/upload_picture，需求DTO MultipartFile，响应DTO WmMaterial。
画面2：展示 VMware Workstation 界面，显示虚拟机列表，当前选中的是“phyougou-image-server_133”。
画面3：展示 IntelliJ IDEA 中的登录服务代码，包含用户登录逻辑，使用了 WulianMapper 查询用户信息并进行密码比对。
画面4：展示 pom.xml 文件内容，包含对 Apache Curator 和 FastDFS Spring Boot Starter 的依赖配置。
画面5：展示项目资源目录结构，选中了 fast-dfs.properties 文件。
画面6：展示文档内容，标题为“4.1.2 FastDfsConfig”，说明该类用于自动化配置 FastDFS 核心参数并设置连接池。
画面7：展示 IntelliJ IDEA 中右键菜单，准备新建一个 Java 类。
画面8：展示 FastDfsConfig.java 文件内容，包含创建 PooledConnectionFactory 和 TrackerConnectionManager 的代码。
画面9：展示 fast-dfs.properties 文件内容，其中 tracker-server 配置为 192.168.25.133:22122。
画面10：展示文档内容，标题为“4.1.3 FastDfsClient”，包含上传文件方法的 JavaDoc 注释。
画面11：展示 FastDfsClient.java 文件内容，包含上传文件方法的实现，使用 storageClient 调用上传接口。
画面12：展示 FastDfsClient.java 文件内容，展示上传文件方法的完整代码，包括处理文件名和扩展名。
画面13：展示 FastDfsClient.java 文件内容，展示上传文件方法的完整代码，包括处理文件名和扩展名。
画面14：展示项目结构和 InitConfig.java 文件内容，该类用于初始化 FastDfsClient 实例并注入到 Spring 容器中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
4.2 素材上传接口
4.2.1
4.2.2 接口定义
(1) 基本定义
参考标准 请参考通用接口规范
接口名称 /api/v1/media/material/upload_picture
需求DTO MultipartFile
响应DTO WmMaterial
(2) CODE定义
```

画面4：
```xml
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-framework</artifactId>
    <version>${curator.version}</version>
</dependency>
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-recipes</artifactId>
    <version>${curator.version}</version>
</dependency>
<dependency>
    <groupId>com.luban</groupId>
    <artifactId>fastdfs-spring-boot-starter</artifactId>
    <version>${fastdfs.version}</version>
    <exclusions>
    </exclusions>
</dependency>
```

画面5：
```
fast-dfs.properties
fast.dfs.connect-timeout=3000
fast.dfs.so-timeout=6000
fast.dfs.tracker-server=192.168.25.133:22122
```

画面6：
```java
/**
 * 自动化配置核心数据的连接池
 */
@Configuration
@ConfigurationProperties(prefix = "fast.dfs")
@PropertySource({"classpath:fast-dfs.properties"})
public class FastDfsConfig extends FeatsAutoConfiguration {
    public FastDfsConfig(GdfsProperties properties) {
        super(properties);
    }
    @Bean
    public PooledConnectionFactory pooledConnectionFactory() {
        PooledConnectionFactory pooledConnectionFactory = new PooledConnectionFactory();
        pooledConnectionFactory.setConnectTimeout(getConnectTimeout());
        pooledConnectionFactory.setSoTimeout(getSoTimeout());
        return pooledConnectionFactory;
    }
}
```

画面8：
```java
public PooledConnectionFactory pooledConnectionFactory() {
    PooledConnectionFactory pooledConnectionFactory = new PooledConnectionFactory();
    pooledConnectionFactory.setConnectTimeout(getConnectTimeout());
    pooledConnectionFactory.setSoTimeout(getSoTimeout());
    return pooledConnectionFactory;
}

@Bean
public TrackerConnectionManager trackerConnectionManager(GdfsConnectionPool gdfsConnectionPool) {
    return new TrackerConnectionManager(gdfsConnectionPool, Arrays.asList(trackerServer));
}
```

画面9：
```
fast.dfs.connect-timeout=3000
fast.dfs.so-timeout=6000
fast.dfs.tracker-server=192.168.25.133:22122
```

画面10：
```java
/**
 * 上传文件方法
 * @Title: uploadFile
 * @Description: /
 * @param fileName 文件全路径
 * @param extName 文件扩展名，不包含（.）
 * @return
 * @throws Exception
 */
public String uploadFile(String fileName, String extName) throws Exception {
    StorePath s = storageClient.uploadFile(FileUtils.readFileToByteArray(new File(fileName)), extName);
    String result = s.getFullPath();
    return result;
}
```

画面11：
```java
/**
 * 上传文件方法
 * @Title: uploadFile
 * @Description: /
 * @param fileName 文件全路径
 * @param extName 文件扩展名，不包含（.）
 * @return
 * @throws Exception
 */
public String uploadFile(String fileName, String extName) throws Exception {
    StorePath s = storageClient.uploadFile(FileUtils.readFileToByteArray(new File(fileName)), extName);
    String result = s.getFullPath();
    return result;
}
```

画面12：
```java
/**
 * 上传文件方法
 * @Title: uploadFile
 * @Description: /
 * @param fileContent 文件的内容，字节数组
 * @param extName 文件扩展名
 * @return
 * @throws Exception
 */
public String uploadFile(byte[] fileContent, String extName) throws Exception {
    StorePath s = storageClient.uploadFile(fileContent, extName);
    String result = s.getFullPath();
    return result;
}
```

画面13：
```java
/**
 * 上传文件方法
 * @Title: uploadFile
 * @Description: /
 * @param fileName 文件全路径
 * @param extName 文件扩展名，不包含（.）
 * @return
 * @throws Exception
 */
public String uploadFile(String fileName, String extName) throws Exception {
    StorePath s = storageClient.uploadFile(FileUtils.readFileToByteArray(new File(fileName)), extName);
    String result = s.getFullPath();
    return result;
}
```

画面14：
```java
package com.heima.common.fastdfs;

import com.lubanuguo.fastdfs.domain.StorePath;
import com.lubanuguo.fastdfs.Service.FastFileStorageClient;
import org.apache.commons.io.FileUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.io.File;

@Component
public class FastDfsClient {
    @Autowired
    FastFileStorageClient storageClient;
    /**
     * 上传文件方法
     * @Title: uploadFile
     * @Description: /
     * @param fileName 文件全路径
     * @param extName 文件扩展名，不包含（.）
     * @return
     * @throws Exception
     */
    public String uploadFile(String fileName, String extName) throws Exception {
        StorePath s = storageClient.uploadFile(FileUtils.readFileToByteArray(new File(fileName)), extName);
        String result = s.getFullPath();
        return result;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“4.2 素材上传接口”，子标题“4.2.2 接口定义”，包含表格数据：接口名称、需求DTO、响应DTO。
画面6：PPT 标题为“4.1.2 FastDfsConfig”，说明该类用于自动化配置 FastDFS 核心参数并设置连接池。
画面14：PPT 标题为“InitConfig.java”，说明该类用于初始化 FastDfsClient 实例并注入到 Spring 容器中。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

