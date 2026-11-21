# 21.搭建微聊系统以及编写基础代码

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\21.搭建微聊系统以及编写基础代码【海量资源尽在 ubkz.com】.mp4
- 时长 13分43秒（音频 824s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们就正式的来实现我们的微聊的这个功能那么我们要去搭建一个微聊的系统为我们这个整个系统来提供一个即时通讯的这样一个功能那么所用的技术呢是Spring的这个WebSocket其实本质上面来讲它还是WebSocket只是Spring做了一些分装然后呢我们要使用的是MangoDB需要把一些聊天的记录聊天的数据
[00:29] 都存到mongoDB里面去当然了这两个是我们的主要的一些技术啊ok好那么我们首先我们来搭建一个工程啊这工程呢就叫itcast浩克im那么im是不是就是啊集中去啊这样的一个意思啊然后呢我们去把它呃拷贝一下然后呢我们去进入到我们的这个工程然后在这个位置呢我们创建一个projector然后我们点击下一步然后呢国牌地呢就叫cn.it
[00:58] cast.hawk对吧hawk.im然后呢这个artifact id呢就叫它然后呢拷过来然后点击finish完成呃他说已经存在啊这个已经存在那么也就是说之前可能我自己已经创了这个工程那我把它删掉啊找到那个呃叫什么呢im啊已经有这工程已经有我把它删掉然后呢我再来重新创建一个啊
[01:27] 好点击这个finish完成然后呢new window把它打开那么ok这个工程呢就创建好了但是呢这工程的创建失败了那么这个就需要我把它关掉重新再创建一下那么我再找到它把刚才这个im的这个工程继续给它删掉然后呢我来重新创建一个new一个projector然后呢下一步然后呢这个叫cnditcast然后呢叫
[01:59] 这个im浩克.im然后呢名字的就是他下一步名字是他然后点击finish完成new window好那么这个工程应该就创建好了ok创建结束了那么创建好之后呢别忘记这个位置把这个打开就是enableauto import那么把这个打开之后呢我们就来看他的一些依赖下面我们把一些必要的一些依赖包的都抠过来
[02:29] 那么首先这个工程要去继承parent继承这个sprint boot的parent然后下面去导入一些相关的一些依赖那么ok那么这样我们先写一个dependencies然后下面再去把它的一些相关的依赖都拷贝进来我们来看一下这个是sprint boot start web因为我们要去做一个web的这样一个支持所以这个包是肯定需要的然后这个是sprint
[02:58] 这个Data的一个MongoDB这个显然也是需要的然后还有一个Spring Boot的这个star这个WebSocket这个肯定也是需要的然后这个是测试没有问题下面这个是MongoDB的一个驱动包然后这个是junit的一个测试测试那么我们把这个都给他拷过来拷贝一下到这OK然后我们把它拷到这好那么接下来我们继续往下面看在下面这个位置我们把他俩拷过来
[03:28] 他俩什么呢是Langbook和这个Commons的一个浪包这个啊就不用过多解释啊这个大家都认识啊然后呢我们下面把这个这个插件也靠过来插件靠过来靠到这哎OK好嘞那么这样的话呢我们就基本上呢把所需要的一些依赖和插件呢都已经导入导入进来了那么下面我们就可以做开发了对吧那么接下来呢我们来编写一个message对象就是我们这个消息这个对象啊
[03:56] 那我们这样吧咱们先把这个对象我们创建出来然后呢我们去然后呢我们再去把代码贴过来我们来做一个分析啊咱们先把这个包呢这个先拿过来就这个pojo这个包创建一个这个包然后呢我们把这个message这个对象在这个pojo这个包下面呢我们去做一个创建创建一个class叫message然后呢我们来看一下给他去添加一些
[04:24] 这个注解还是比较多的我们来一个一个的去说一下吧我们先把我们把这个拷进来那么我们先把它的内容贴进来之后我们再去做一个讲解好把它贴过来那么贴过来之后呢我们去做这样的一个说明来看一下这个是有报错吗我这个ID那就是它然后呢这个是index那么就是它OK这个是failedOK
[04:58] 好了还有什么还有date还有date把它导入进来还有什么的user我们现在还没有这样我们把下面这个user也call过来这样我们就直接call吧然后我们在这个puzzle里面OK好那么这样的话我们这个user这个就搞定了这个puzzle我们基本搞定了我们来看一下这个是我们最主要的一个对象叫message就是我们的消息对象
[05:25] 在上面我们添加了有4个我们的注解那我们来看一下前面三个我相信大家应该都认识这个是longbook的三个注解那么一个data一个是全参数的一个构造器一个是没有参数构造器那么下面的这个是document这个是谁注解的这个是我们smoothie的一个关于mongodb的这样的一个注解可以看到是不是在这这样的一个注解那么这个注解的一个作用是什么呢
[05:51] 就是来指定注意他是去指定我们的一个这个表的名称表这个名称那么其实在我们当前这个案例中那么他的写不写效果都一样为什么呢因为这个summitDate的默认情况下面会采用你这个类的这个全称类这个全称然后把这个首字母做一个小写作为你的一个connection集合去做一个使用
[06:18] 那么我们其实小写之后呢就本身就是它对不对但是呢为了给大家去演示它的一个用法所以呢我们在这去添加一个这个connection那么也就是说其实我们通过这个注解你可以做一个自定义比如说我就叫abc那么我这个表明就叫abc可以吗那还可以的哎ok通过这个注解去做一个这样这样的一个定义啊ok然后呢下面这个呢build这个呢是呃前面我们在前面也用过啊这样的一个方式啊也说过
[06:45] 通过这个build就是我们去会给我们的这个message去通过build的一种方式去构建我们这个对象让我们去后面去构建这个对象的时候呢变得更容易一些啊ok好那么这就是这么几个注解那么下面我们来看一下在我们这个message中啊那么先来看一下这个结构啊结构这个显然呢它是这样的一个结构就是ID是它那个主电对吧然后那个message是个消息那么它应该是有这样的一个结构就是
[07:13] 它的最外面的是一个最外面的是一个对象的对象然后呢这个里面呢有这么几个字段第一个呢是ID第一个是ID对吧ID比如说是一个字步号吧随便写啊写个字步号然后呢第二个呢是第二个是它的消息message叫message然后呢冒号这也是一个内容就是消息OK然后呢还有一个什么呢是它的一个状态
[07:43] 因为我们知道每一个消息它其实有个状态是已读还是未读所以我们会给它一个状态那么如果它为一代表的就是未读如果为二就是已读OK然后还有一个是它的一个send date就是它发动时间那么发动时间我们就叉叉叉在代表发动时间了那么要注意的是我们发动时间往往我们在阶层中所写的一个
[08:08] 字段的名称的往往是这样的一种结构就类似于我们的数据库中的一个这样的一个结构但是呢我们的对象中呢又是需要这样的一个驼分式的一个这样的一个指定对吧那么这个时候就需要去借助于一个fail的这个注解来指定它的一个名称来做这样的一个映射因为默认情况下面呢去根据你的属性名去找你的一个这个字段哎OK那默认是这样的啊然后在下面还有一个叫read date就是我们这个
[08:37] 如果你这个消息已经被标记为已读状态那么我们就要去设置它的一个已读的一个时间XXX这样的一个时间然后呢下面还有两个很重要的一个属性一个叫做from2那么from就说这个消息是发至于谁谁发来这个消息那第二个就是2这个消息发给谁的那大家想一下这个消息是不是一定有这样的特点就是说谁发过来这条消息然后这条消息发给谁
[09:07] OK那么一个是flub一个to那么flub和to呢我们都给它是指定这个user对象那么在这个user对象中呢又有一个什么呢ID又有一个ID然后呢冒号比如说前面写啊写一个这么串吧随便写啊然后呢我们下面还有一个叫做什么呢叫usernameOK那么它是一个对象啊username冒号叉叉叉吧
[09:35] 然后我们把这两个也给它扣过来OK好那么做这样的一个编写好那么现在我们这个结构基本行长就出来了这是我们整个消息的一个结构这个结构在我们的对象中做体现的话就是需要做一个嵌套就在message的对象中嵌套我们这个U这个对象OK那么就这样的一个结构那么在这个里面我们还有这么几个注点我们需要给大家去说一下一个是ID这个ID就代表着我们这个
[10:09] 这个是我们的主件是我们主件的这个标识做这样的一个标识然后呢下面还有一个叫indexed那么indexed就是代表着我们这个字段需要做索引那么这个字段也是一样需要做索引那么为什么他需要索引呢有些时候呢我们需要去根据这个状态去查找他的一些比如说查找未读的消息所以他需要去有一个状态通过状态去做一个查找所以他需要呢有这个索引那么还有呢发送的时间
[10:39] 和我们的已读的时间发送时间需要做索引已读的时间就不需要做索引了因为我们没有这种需求是吧根据已读的时间去查找这个数据这种需求是没有的那么然后呢我们可以看一下下面这个是Fram和To那么这两个呢都有这个索引那么都有这个索引呢也就意味着我们都可能会通过这个Fram或者是To去查找我们的数据对不对OK那么我在这个点我们特别要注意一点是
[11:08] 当我们给这个字段添加这个锁引的这个注解之后呢那么我们的这个SupplyData去把我们这个数据去做一个保存的时候比如说它保存到我们的一个保存到我们的一个MongoDB的话保存到我MongoDB的话那么MongoDB中的会自动创建我们的这个表以及注意啊以及会自动创建它的一个锁引那么一会儿呢我们可以做一个测试就是我们把我们那个数据的让它去
[11:37] 创造了超过一条数据我们看一下他自动创建的表以及自动创建的一个所以哎OK好那么到这里呢我们基本上呢就把这个项目的是不是就基本上搭建出来了下面还有一个啊就是我们这个优的对的啊那么这个我们要说一下就是在我们的这个项目中呢我们更关注点是在于我们的这个消息的发送和接收
[12:02] 以及我们的一个数据的一个存储那么对于在这个里面的一些会涉及到一些用户登录的一些用户的相关的一些这个数据我们暂时的先不做一个设计所以呢我们先给他去构造一些我们构造一些这个用户的数据来做方便我们去做一个业务的开发等到我们后面呢我们去可能会去实现他的一个用户的一个登录或者说用户集中的一个管理啊这样的一个功能那么如果实现这样的功能的话那么我们就可以去
[12:31] 对接到我们那个功能里面去做了哎呀OK那样的话用户就会比较真实了那么下面我们把这个类我们就创建出来吧这个只是一个做一些数据的一些模拟啊那么在这个里面呢我们给他去设置一个静态的一个这样的一个对象就是UserMap就假设我们现在有这么几个对象了然后呢我们写一个Static的静态块然后静态块里面去给他构造一系列的一些数据那么这个呢就是张三
[13:01] 然后下面再去构造李四王五很多这些数据大概就这么几条245条数据然后张三李四王五赵六孙七大概有5条数据那么有了这5条数据后面我们是不是方便我们去做开发了OK因为我们一会后面去实现的是
[13:20] A用户发给B用户你至少是不是有两个用户才能去做这样的这样的一个功能所以我们先去构造一些这样的一些这个用户的数据那么到这里我们的这个工程的这个搭建就算是完成了能把一些基础性的一些这个代码也写好了然后我们对这个里面的一些内容也做了一些讲解那么OK那么搭建我们的工程我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
搭建一个基于 Spring Boot 和 MongoDB 的即时通讯系统，包括创建工程、编写 Message 和 User 对象、以及构造用户数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程讲义 PDF 的第 4 章“搭建微聊系统”，说明使用 Spring WebSocket 和 Spring-data-MongoDB 技术。
画面 2: IntelliJ IDEA 界面，提示项目已存在，准备创建 Maven 项目。
画面 3: 显示 pom.xml 文件内容，包含项目的基本配置。
画面 4: 展示 pom.xml 中的 <dependencies> 部分，列出 Spring Boot Web、MongoDB Driver、WebSocket 等依赖。
画面 5: 展示 pom.xml 中的测试依赖，包括 JUnit。
画面 6: 讲义 PDF 中的“4.2. 编写 Message 对象”，开始编写 Message 类。
画面 7: 讲义 PDF 中的“4.2. 编写 Message 对象”，继续展示 Message 类的代码。
画面 8: IntelliJ IDEA 中编写 Message.java，使用 @Indexed 注解。
画面 9: IntelliJ IDEA 中编写 Message.java，添加 @Field 注解。
画面 10: IntelliJ IDEA 中编写 Message.java，添加 @Indexed 注解。
画面 11: IntelliJ IDEA 中编写 User.java，定义 User 类。
画面 12: 讲义 PDF 中的“构造用户数据”，展示 UserDate 类的代码。
画面 13: IntelliJ IDEA 中显示 UserDate.java 的代码。
画面 14: 讲义 PDF 中的“4.2. 编写 Message 对象”，展示 Message 类的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.haoke.im</groupId>
    <artifactId>itcast-haoke-im</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>
```

画面 4:
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-mongodb</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.mongodb</groupId>
        <artifactId>mongodb-driver-sync</artifactId>
        <version>3.9.1</version>
    </dependency>
</dependencies>
```

画面 5:
```xml
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
    <scope>test</scope>
</dependency>
```

画面 6:
```java
package cn.itcast.haoke.im.pojo;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
@Data
@Builder
public class Message {
```

画面 8:
```java
@Indexed
private Date readDate;
```

画面 9:
```java
@Field("send_date")
@Indexed
private Date sendDate;
@Field("read_date")
@Indexed
private Date readDate;
```

画面 11:
```java
package cn.itcast.haoke.im.pojo;
import lombok.Data;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.NoArgsConstructor;
public class User {
    private Long id;
    private String username;
}
```

画面 12:
```java
package cn.itcast.haoke.im.pojo;
import java.util.HashMap;
import java.util.Map;
public class UserData {
    public static final Map<Long, User> USER_MAP = new HashMap<>();
    static {
        USER_MAP.put(1001L, User.builder().id(1001L).username("zhangsan").build());
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“4. 搭建微聊系统”，副标题“下面我们将开发微聊系统，实现好客房屋项目的即时通讯功能。”，技术列表为“Spring WebSocket”、“Spring-data-MongoDB”。
画面 6: PPT 标题为“4.2. 编写 Message 对象”。
画面 12: PPT 标题为“构造用户数据”，代码部分为“USER_MAP.put(1001L, User.builder().id(1001L).username("zhangsan").build());”等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

