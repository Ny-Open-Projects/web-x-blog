# 05.阿里云OSS存储之SDK的使用

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\05.阿里云OSS存储之SDK的使用【海量资源尽在 ubkz.com】.mp4
- 时长 14分44秒（音频 885s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就基于这个OSS服务呢我们来实现图片的上传我们将我们的图片上传的功能呢然后呢在这个工程中去做一个实现就是我们这个manager API server那么在这个里面呢去做一个实现然后呢去为我们的一些其他的一些模块呢去提供这种上传的服务那么我们的工程呢是在这里就在这个里面去做一个实现在这个里面做一个实现
[00:28] 好那么我们接下来就来看一下那么我们现在想要使用这个OSS做一个图片上传的一个服务那么我们应该解决什么问题呢首先我们得知道这个OSS这个服务对吧那么我们要通过这个Java的一个代码如何去上传我们的图片到我们这个OSS中对吧那么我们前面是不是说过通过这个它的界面的工具是不是可以点击上传这种方式我们
[00:56] 大家知道也学会了可以去做一个上传但是我们通过我们的代码又该如何去做上传所以我们需要去看一下它的一个开发者指南在这点击我们这个概览然后在这个位置有一个开发者指南我们点击来看一下那么在这个里面我们其实要找到它的一个
[01:17] 叫做SDK的一个参考在这个位置啊SDK的参考然后呢我们找到对应的相关的语言那么我们想要看的是这个加码语言那么点击之后呢它其实下面的有一些很多的一些这个内容啊那我们就不一一去做查看了我们直接去看它的一个这个上传文件啊因为我们就需要去做一个上传文件吧对吧然后呢在这个里面呢有一个简单的一个上传我们点击它
[01:44] 那么在这个里面我们可以看到他会有一些代码那么我可以看到在这个位置是不是一个流式上传那么他简单的代码是这样的对吧然后还有一个byte数组的一个上传还有一个网络流的一个上传还有一个上传文件流那么其实我们可以看到他的一些代码基本上的可能都差不多只是你最后提交的这个流会有点不一样而已
[02:10] 所以我们就基于它的第一个代码我们去做我们的一个实现就可以了好 那我们来看一下那么我们想要使用它所提供的OSS的一个SDK那么首先其实要导入的是一个依赖那我们先把这个依赖先导入进来那么咱们把这几个都导入进来这个是我们后面都需要的一些依赖好 那么我们找到我们的工程然后在这个POP文件中把相关需要的一些依赖都导入进来
[02:38] 导到最下面放到这我们来看一下导入的依赖的一些内容有哪些内容那么首先第一个我们导入了它的阿里云的SDK OSS这个就是我们需要它的一个SDK版本使用的是2.8.3这个版本然后下面这个我们导入的是一个Longbook这个前面我们讲过就是用于简化我们Pozo的一个编写是不是可以帮我们自动去生成一些get和set
[03:06] 然后下面JODA是一会儿我们在后面去做上传的时候会使用到的一个包这个是关于一个日期处理的一个相关的一个包那么好那么我们接着继续往下面看下面我们就参考于这个代码去做一个实现对吧那么这个代码它是使用了SDK去做这样的一个上传那我们来看一下那么这个代码首先它需要有这三个信息对吧
[03:35] 一个叫endpoint就是你上传的一个目标点然后下面一个accesskeyid还有一个accesskeysecret那么这么两个信息然后通过这三个信息就可以去构建一个ossclient客户端然后通过ossclient客户端就可以去做一个putobject那么就可以做一个上传了那么也就是说我们想要去玩上传你首先得有ossclient对吧
[04:05] 那么我们可以看到它只是通过Java的方式是不是调用了SDK那么我们需要是不是在我们的springboard中去整合这个SDK对吧那么来看一下怎么整合那么接下来我们就需要这么来玩那么我们就需要是不是在我们的spring容器中要有一个这个ossclient这个对象然后在所需要的上传的位置把它注入进来是不是就可以了好那么我们来先来看一下
[04:33] 那么我们在这个下面吧创建一个包啊创建一个什么包呢咱们来看一下叫一个就叫config这个包吧config这个包由于我们是要读取一些配置文件啊所以我们创建一个包叫configconfig包然后在这个config包下面呢我们创建一个类啊就叫阿里吧阿里云啊阿里云config
[05:00] 好我们创建一个这个文件啊那么这个文件显然呢需要给他个注解叫configureconfiguration这是一个啊他是一个我们的一个配置类然后呢在这个里面呢我们要去给他去去做一个bin的一个实例化bin的一个实例化实例化谁呢其实就是我们刚才所看到这个ossclient
[05:24] OSSCLENT把这个包我们导入进来然后我们就叫OSSCLENT然后第一个字母O改成小写好嘞好那么这个里面代码怎么写是不是我们就参考这个代码是不是我们去new一个对象就可以了intent一个他好那么我们这个基本设备就搞定了但是问题来了那么这三个内容怎么办是不是我们可以参考他这个代码把这个代码是不是拷过来我们贴到这
[05:54] 他的一些注释就不需要了这个也就不需要了好嘞好那么下面我们来看一下这三个内容怎么去做一个处理那么首先我们先要知道的一点是这三个内容你不能写死到我们 java代码中对不对所以我们需要把它写到外部的一个配置文件中去做一个读取然后我们在resource下面创建一个publish文件就叫阿里云.publish好publish文件
[06:25] 那么这个就是一个阿里云的一个配置文件那么我们需要哪些内容把这个内容拷过来我们需要配置的是这三个内容好贴过来来看一下这个里面的一个配置那么把前面这个string给他拿掉进行拿掉那么我们是不是写这个配置文件的时候最好是不是要给他个前缀所以给他一个阿里云点什么什么ok第一个是他的一个endpoint第二个是他的一个access key id还有一个第三个是access key的一个secret
[06:55] 那么我们一个一个来看一下它的一个这个内容应该怎么去填对吧好那么我们来看一下这样咱们这样咱们先把这个内容呢给它去读取到我们的配读取到我们这个代码中然后呢我们再来看一下它内容的一个填写那么在Springboard中如何去读取配置文件呢是不是我们可以通过一些注解去完成一个配置对吧那么首先第一个注解呢是不是有一个叫Property一个Source
[07:21] 是不是去做一个这个读取那么这个下面我们是不是就可以去写一个我们的一个这个配置文件的一个地址那是不是就在classpass下面的有一个叫做aliyun.publist哎呀ok是不是可以通过这样的一个读取就可以读取到我们的一个配置文件啊对吧然后呢这个第一步是不是就搞定了那么第二步我们又如何
[07:47] 去将我们这个里面的这个内容是不是映射到我们的这个属性上面呢怎么样去做一个映射呢我们需要这么来玩给它去设置一个叫做configurationconfiguration有一个publish看到了吗是不是有一个publish然后呢通过它呢去我们设置它的一个pre pre prefix
[08:14] prefix是它的前缀前缀是什么呢前缀是阿里云那么也就是说我们希望它去通过前缀去跟我们属性的做一个映射当然了我们要把它设置为是一个私有要注意的是那么你设置为私有之后它并不是说我们添加一个这个它就能够帮我们做个映射我们需要给它添加什么呢
[08:41] 添加一个set方法这三个的一个set方法设置一个set方法把它作为一个添加好那么给他这三个属性添加每个都添加一个set这个方法然后我们把它去掉这个就不需要了这个就不需要了把这个也去掉然后下面这个也去掉这样的话就可以完成自动做一个映射这个相信大家在前面是不是也讲过通过这样的一个注解就可以去自动读取
[09:11] 配置文件中的相关的信息那么然后自动就会注入到我们这三个属性中那么我们在这个方法中就可以拿到这三个属性的值然后我们就可以完成一个 ossclient的一个实例化ok好那么接下来我们要解决的问题就是这三个的内容那么应该怎么样做一个处理那么我们来看一下第一个是endpoint那么endpoint的值在哪里找到我们是不是回到我们的一个控制台
[09:38] 那么我们希望我们的图片的内容都上传到这个下面对吧当然了你要根据你自己的实际情况的去看一下那么在这个点击我们这个里面可以看到是不是在这个endpoint的一个域名的一个这个节点那么外网访问是不是就这个点那么拷贝他ok那么就叫谁呢那我们就把它放到这吧你看是不是变成了osscn这个青岛阿里云这个.com好那么第一个这个
[10:08] Enterport是不是我们就搞定了第二个我们来看一下Access ID这个又从哪里去找到那么如果你要是不知道哪里去找那么可以点击它的一个官方有一个文档在这来看一下在下面这个位置有一个文档这个里面有一个说如何获取Access KeyAccess KeySecret这两个怎么获取你可以点击这个位置也可以什么也可以去在这个位置有一个
[10:36] 叫做access key按钮点击它也可以去使用我们点击它要注意的是它官方其实有一个access key那么access key是一个权限比较大的这样的一个access key然后我们他建议我们使用的是一个
[10:58] 纸账户来做一个使用那么我们也使用纸账户的形式你可以去创建一个账户那么这个账户我就不创建了因为我都创建好了我叫IDcast浩克那么我点击进去之后就可以看到他的信息那么我们可以看到在这个位置是不是有个access key那么我把它拷过来就拷贝到我的里面来这个就不需要了要注意的是这个也不需要引号把它拿掉把这个也拿掉
[11:26] 好 那么这个就是它的一个配置那么问题来了这个access key secret这个从哪来要注意就拷贝到我的这个里面来这个就不需要了要注意的是这个也不需要这个引号把它拿掉把这个也拿掉
[11:40] 好那么这个就是它的一个配置那么问题来了这个access key secret这个从哪来呢要注意的是那么在我们这个页面中的你找不到这个access key secret找不到那么这个值要注意这个值是你在创建用户的时候他会有一个提示说你要去下载这个值或者说要去保存这个值这个是你下载这个值的唯一的一次机会
[12:05] 那么如果你在创建用户之后创建用户成功之后啊没有去下载这个值那么这个值是找不到就找不到了OK那么所以呢你需要在下载需要在创建用户成功之后呢要把这个值呢保存下来好那么这个要提醒大家了所以呢我在这个位置呢我就在我的这个讲义中呢我已经把这个值是否保存进来了好那么我就去使用它去做一个上传啊那么我就到这贴一下
[12:35] 这个就是我的access key的secret值我建议大家就不要使用我的这个key了因为我这个会在后面会把这个账号给它禁用掉那么你们可能也用不了这个只是给大家做一个演示ok好那么这两个值是不是我们就都有了那么我们也就意味着
[12:55] 也就意味着我们在这个里面我们这个OSSCLAND是不是已经就加入到我们这个SPOIN的一个容器对吧那么我们就可以在我们需要去使用我们这个OSSCLAND的位置是不是直接去注入就可以了好那我们来看一下我们的一个讲义那么前面我们是不是导入了这个依赖然后我们编写了一个阿里云的一个PoPTIS文件那么在这个文件中我们写了一些这个内容对吧写了一些内容ok
[13:21] 好那么我们还有这两个内容我们并没有去用到并没有去用到那么一会我们在用到的时候我们再来做一个添加ok
[13:30] 好然后我们继续往下面看那么如果我们不知道你如果你不知道如何去获取这access key的话那么就通过这个地址去做一个查看刚刚我们通过编写这个阿里云的config是不是将我们的ossclient这个对象是不是已经就加入到我们的spin容器了对吧那么在需要的用的位置就给他去做一个注入就可以了那么我们来看一下讲义在我们讲义中会发现其实我们并没有给他设置这个set的方法
[13:59] 对吧并不是说他不需要set的方法而是什么呢而是我们添加了一个这个date注解还记得吗这是个long book这是他的一个注解那我们通过这个date注解是不是可以简化我们这个set的方法的一个创建所以我们在这个位置给他添加一个date
[14:16] 这个注解那么下面的get和set的方法是不是就不需要了对吧OK好那么我们来看一下它有没有帮我们去生成这get和set的方法是不是有好嘞那么这样的话我们是不是就完成了我们这个阿里云config的一个编写那么这样的话我们就可以把它加入到我们的容器那么后面我们是不是就可以去使用它去做一个图片上传了好那么关于这个阿里云的一个config的配置我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成阿里云 OSS 服务，实现图片上传功能，包括添加依赖、配置文件和编写配置类。

2) 按时间顺序列出每张画面的要点：
画面 1: 课程文档页面，标题为“2.4、实现图片上传”，说明在 itcast-haoke-manage-api-server 中实现图片上传功能。
画面 2: 阿里云 OSS 官方文档页面，展示“文件上传”和“流式上传”等概念。
画面 3: 阿里云 OSS 官方文档页面，展示“流式上传”部分的 Java 代码示例。
画面 4: IntelliJ IDEA 编辑器中显示 Maven 依赖配置，包含 aliyun-sdk-oss、lombok 和 joda-time。
画面 5: IntelliJ IDEA 编辑器中显示 Maven 依赖配置，包含 ZooKeeper、zkclient、lombok 和 joda-time。
画面 6: IntelliJ IDEA 编辑器中显示 AliyunConfig.java 文件，正在编写 @Bean 注解的 OSSClient。
画面 7: IntelliJ IDEA 编辑器中显示 resources 目录，弹出“New File”对话框，准备创建 aliyun.properties 文件。
画面 8: IntelliJ IDEA 编辑器中显示 AliyunConfig.java 文件，已编写 @PropertySource 注解和构造方法。
画面 9: IntelliJ IDEA 编辑器中显示 AliyunConfig.java 文件，弹出“Generate”菜单，准备生成 Getter 方法。
画面 10: IntelliJ IDEA 编辑器中显示 aliyun.properties 文件，已编写 endpoint、accessKeyId 和 accessKeySecret 的配置。
画面 11: 阿里云 RAM 控制台页面，显示“用户AccessKey”列表，正在加载。
画面 12: 课程文档页面，标题为“2.4.3、编写AliyunConfig”，显示 aliyun.endpoint、aliyun.accessKeyId、aliyun.accessKeySecret、aliyun.bucketName 和 aliyn.urlPrefix 的配置示例。
画面 13: 课程文档页面，标题为“2.4.3、编写AliyunConfig”，显示 AliyunConfig.java 文件的完整代码。
画面 14: 课程文档页面，标题为“2.4.3、编写AliyunConfig”，显示 AliyunConfig.java 文件的完整代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```xml
<dependency>
    <groupId>com.github.sgroschupf</groupId>
    <artifactId>zkclient</artifactId>
    <version>0.1</version>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.4</version>
</dependency>
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.9.3</version>
</dependency>
```

画面 5:
```xml
<dependency>
    <groupId>org.apache.ZooKeeper</groupId>
    <artifactId>ZooKeeper</artifactId>
    <version>3.4.13</version>
</dependency>
<dependency>
    <groupId>com.github.sgroschupf</groupId>
    <artifactId>zkclient</artifactId>
    <version>0.1</version>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.4</version>
</dependency>
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.9.3</version>
</dependency>
```

画面 6:
```java
package cn.itcast.haoke.dubbo.api.config;

import com.aliyun.oss.OSSClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AliyunConfig {

    @Bean
    public OSSClient ossClient() {
    }
}
```

画面 8:
```java
package cn.itcast.haoke.dubbo.api.config;

import com.aliyun.oss.OSSClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource("classpath:aliyun.properties")
public class AliyunConfig {

    @Bean
    public OSSClient ossClient() {
        return new OSSClient(endpoint, accessKeyId, accessKeySecret);
    }
}
```

画面 9:
```java
package cn.itcast.haoke.dubbo.api.config;

import com.aliyun.oss.OSSClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Configuration
@PropertySource("classpath:aliyun.properties")
@ConfigurationProperties(prefix = "aliyun")
public class AliyunConfig {

    private String endpoint;
    private String accessKeyId;
    private String accessKeySecret;
    private String bucketName;
    private String urlPrefix;

    @Bean
    public OSSClient ossClient() {
        return new OSSClient(endpoint, accessKeyId, accessKeySecret);
    }
}
```

画面 10:
```properties
aliyun.endpoint = "http://oss-cn-hangzhou.aliyuncs.com";
aliyun.accessKeyId = "<yourAccessKeyId>";
aliyun.accessKeySecret = "<yourAccessKeySecret>";
```

画面 12:
```properties
aliyun.endpoint:oss-cn-qingdao.aliyuncs.com
aliyun.accessKeyId:LTIAFc7FusP7Rfq
aliyun.accessKeySecret:2Vvo3qlMwvTy81xcmFsCfU2ZcHCK
aliyun.bucketName:itcast-haoke
aliyun.urlPrefix:http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2.4、实现图片上传”，说明在 itcast-haoke-manage-api-server 中实现图片上传功能。
画面 12: PPT 标题为“2.4.3、编写AliyunConfig”，显示 aliyun.endpoint、aliyun.accessKeyId、aliyun.accessKeySecret、aliyun.bucketName 和 aliyn.urlPrefix 的配置示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

