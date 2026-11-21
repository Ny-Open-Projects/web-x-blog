# 04_图片缓存_图片微服务导入及代码思路分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\04_图片缓存_图片微服务导入及代码思路分析【海量资源尽在 666java.com】.mp4
- 时长 5分27秒（音频 327s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来去开发当前的图片的微服务首先这一块咱们还是要去导入当前的一个微服务模块然后是专门来处理图片相关的这种业务行那咱们怎么导入在今天的资料中有一个这么一个文件是吧直接去拷贝一下或者你在这解压也行解压完成后你可以看一眼然后你就把它可以拷贝拷贝到哪拷贝到你当前的这种
[00:30] 开门的打开然后呢我直接就放到这好放到这之后啊你下面要去改一个东西还知道吧改哪啊你要去在这个POM中在这去加一个东西往这地一下好这是啥呢是以密之丝你可以拷贝下它这样的话就加进来了啊那加进来之后啊这可还是灰的是吧怎么办呢你需要去导入呗导入怎么导啊你右键啊不是右键啊点这个点这个啊加号然后呢去
[01:06] 打开当前的这种找到当前的这个images然后找到palm然后点OK这样的话就算是导入进来了好吧行那这个颜色已经变了啊好那这个那这个导入进来之后啊下面呢咱们就可以看一下里边的内容好那首先呢这是palm呢其实跟咱们之前是差不多的啊是差不多的啊这个咱们没啥可看的啊然后呢咱们下面呢去可以看一下里边到底有什么文件啊其实这是有几个配置啊这个都有是吧
[01:36] 好我再关了然后你可以看一下这里边还有一些东西Test是没有东西的这个是一个配置好吧然后这jar里边是有一些代码的这个代码的话最主要的是有一个config它需要去引入那么多文件第一个就是当前的引导类是吧这个没啥可说的
[01:58] 然后主要是看当前的配置里边是有一个fastdevice有一个配置好吧这个有一个图片的转换器是有个对象咱们需要去给它注入进来需要去扭一下就可以了这只是一个工具类然后还有啥还有一个是初日化的一些东西比如说咱们要去设置一个这种路径的头头线期这个其实改了改了你们也改了改成你们自己的比如说叫我是叫localhost不是localhost
[02:27] 192.168.25.133我是133是专顾号没有啊就是当前的80啊还有卡不卡的是吧有两个啊然后还有是mycircle的还有什么呢redis的证明这块呢要用到redis所以说你要用到一个redis
[02:49] 还有一个登录相关认证相关的这个咱们暂时也用不着但是这个加进来也行好吧这个最起码也能看明白当前的这个微服务里边所有的配置你要能够看明白就可以唯一不一样的地方就是在这去加了一个这种转换就是一个图片的转换器咱们在这去拗了一下并且加了一个admin就是把当前这个类干嘛呢放到了死门的容器中好吧行那这个加完之后那这个所有的微服务都已经做完了
[03:17] 这个最基础的工程你不用再去写了然后下面还有一个东西我要去说一说就是当前有一个叫做base64什么youtube就是有一个这种url的解码和编码两个工具类这个类其实已经考我已经考完了其实你们要没有的话你们就在哪就在哪去创建就在当前的youtube4下边有一个什么找到这有一个靠问其实你把它直接考过来也行
[03:47] 你直接考过来之后呢我把这个路径稍微改一改啊好你们要没有的话就去创建好吧创建当前这个工具类然后呢以备咱们后面去使用那行那这个基础工程啊咱们就说到这儿啊你们也要把这个东西给导入好下面呢咱们可以再去看一下这里边有一个思路分析咱们可以简单说一说啊首先呢是要去什么第一个啊要去监听Article V服务的消息刚才其实呢咱们已经发了消息了啊
[04:18] 然后从中是获取到热点文章的数据然后你拿到热点文章之后咱们就可以去再去获得content其实这个里边刚才说了其实这个文章这个文章数据热点文章数据里边包含了当前的article id这时候你就可以去查询当前的内容然后内容里边是有图片的所以说咱们这一部分图片需要进行缓存需要进行缓存然后第二个就是要去获取文章封面的图片
[04:48] 然后也是要进行redis缓存好吧一共是有两块这边是有一个注意事项大家一定要注意哪个呢就是说这缓存FastDLS中图片信息那你说还有其他的吗有哪块呢就是当前的比如说你要是从爬虫系统去获取的图片信息的话那这时候那个图片咱们没有必要进行缓存
[05:13] 那个不下载到本地啊所以说呢直接去访问网络图片就可以了不需要是进行缓存好吧那行那这个思路啊咱们就说完了啊一会呢咱们就按照这个思路去把代码开发出来

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解微服务中处理热点文章图片的模块，包括图片的BASE64解码、Redis缓存、Kafka消息发送以及相关配置和工具类的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDEA中“images”微服务模块的代码，包含BASE64解码工具类的实现。
画面2：展示“article”服务中处理热点文章的代码，包括计算热点文章、保存热点文章、发送Kafka消息等逻辑。
画面3：展示项目结构，突出“images”模块。
画面4：展示“images”模块的pom.xml文件，包含Spring Boot父工程配置和模块依赖。
画面5：展示“images”模块的pom.xml文件，包含引入的依赖和排除的依赖。
画面6：展示“images”模块的application.properties文件，包含日志配置。
画面7：展示“images”模块的项目结构，聚焦于src/main/java目录。
画面8：展示“images”模块的项目结构，聚焦于src/main/java/com.heima.images/config目录。
画面9：展示“images”模块的项目结构，聚焦于src/main/java/com.heima.images目录。
画面10：展示“images”模块的SecurityConfig.java文件，包含Spring Security配置。
画面11：展示“utils”模块的项目结构，聚焦于target目录。
画面12：展示“utils”模块的项目结构，聚焦于src/main/java/com.heima.utils目录。
画面13：展示“images”模块的BASE64Utils类的代码，包含BASE64解码方法。
画面14：展示“images”模块的CacheImageService接口，包含缓存图片到Redis的方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public static byte[] decode(String base64) {
    BASE64Decoder decoder = new BASE64Decoder();
    try {
        byte[] b = decoder.decodeBuffer(base64);
        for (int i = 0; i < b.length; ++i) {
            if (b[i] < 0) { // 转换异常处理
                b[i] += 256;
            }
        }
        return b;
    } catch (Exception e) {
        return null;
    }
}
```

画面2：
```java
String lastDay = DateTime.now().minusDays(1).toString("yyyy-MM-dd 00:00:00");
List<Article> articleList = apArticleMapper.loadLastArticlesForHot(lastDay);
//缓存热点文章
cacheTaskRedis.setHotArticleList(articleList);
for (ApBehaviorEntry entryList = apBehaviorEntryMapper.selectEntryList() {
    //保存热点文章
    apArticleMapper.insert(hot);
    //缓存热点文章
    cacheArticleForEntryList(hot, entryList);
    //缓存文章中的图片
    kafkaSender.sendArticleMessage(hot);
}
```

画面4：
```xml
<groupId>com.heima</groupId>
<artifactId>heima-leadnews</artifactId>
<packaging>pom</packaging>
<version>1.0-SNAPSHOT</version>
<modules>
    <module>heima-leadnews-admin</module>
    <module>heima-leadnews-apis</module>
    <module>heima-leadnews-article</module>
    <module>heima-leadnews-behavior</module>
    <module>heima-leadnews-common</module>
    <module>heima-leadnews-crawler</module>
    <module>heima-leadnews-login</module>
    <module>heima-leadnews-media</module>
    <module>heima-leadnews-model</module>
    <module>heima-leadnews-user</module>
    <module>heima-leadnews-utils</module>
    <module>Service-mycat</module>
</modules>
```

画面5：
```xml
<dependencies>
    <dependency>
        <groupId>com.heima</groupId>
        <artifactId>heima-leadnews-model</artifactId>
    </dependency>
    <dependency>
        <groupId>com.heima</groupId>
        <artifactId>heima-leadnews-common</artifactId>
        <exclusions>
            <exclusion>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-logging</artifactId>
            </exclusion>
            <exclusion>
                <groupId>org.slf4j</groupId>
                <artifactId>slf4j-log4j12</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
</dependencies>
```

画面6：
```properties
log.level=DEBUG
log.pattern=%d{DEFAULT} [%n] %level | %t | %M | %msg%n
```

画面13：
```java
public class Base64Utils {
    /**
     * 解码
     * @param base64
     * @return
     */
    public static byte[] decode(String base64) {
        BASE64Decoder decoder = new BASE64Decoder();
        try {
            byte[] b = decoder.decodeBuffer(base64);
            for (int i = 0; i < b.length; ++i) {
                if (b[i] < 0) { // 转换异常处理
                    b[i] += 256;
                }
            }
            return b;
        } catch (Exception e) {
            return null;
        }
    }
}
```

画面14：
```java
public interface CacheImageService {
    /**
     * 缓存图片到redis
     * @param imgUrl
     * @param isCache
     * @return
     */
    byte[] cacheRedis(String imgUrl, boolean isCache);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“1.3 images微服务接收热点文章，处理图片”。
画面13：PPT标题为“导入资料中模块heima-leadnews-images 专门处理图片相关的微服务 集成redis 工具类：”。
画面14：PPT标题为“思路分析：”和“(2) 创建com.heima.images.Service.CacheImageService 缓存图片”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

