# 28.Nacos-配置管理-扩展配置-案例

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\28.Nacos-配置管理-扩展配置-案例【海量资源尽在 666java.com】.mp4
- 时长 5分26秒（音频 327s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那下面呢我们来针对扩展配置呢做一个案例那这个案例的需求是什么呢我们准备去还是抽取一些公用的配置比如我们抽取什么呢比如说我们把这个Spring的一些HTTP的一些比如说像这个字符集呀或者说编码呀或者说这个比如说Tomcat的投信息呀等等包括访问路径呢我们都把它统一抽出来那配在一个具体的配置文件当中
[00:29] 可以吗好这里边呢我们准备抽到一个叫eid-configure-http的配置文件首先还是我们先发布配置没问题吧好在这发布配置那这个呢是不是就是http那这里边呢我们刚才说了嘛它统一的组是不是就是common它的内容注意看啊根据讲义来注意我们现在越来越真实了因为刚才我
[00:57] 纯粹就是为了去给大家测试获取这个配置对吧现在呢我们直接要拿来用了看好这个配置是不是就是我们正儿八经的这个微服务项目所用到的一些配置你看对吧那我们是不是就把它配置到这了对吧那配置到这之后呢各位如果我想用这个配置我想用这个配置怎么办很简单那你就需要在这扩展就可以了扩展的方式这里面刚才不是说了吗它是http吗
[01:26] 这是我们的配置文件的名称这个下标往下继续走可以吧这就可以了注意现在我是不是就可以把它给重启一下没错重启完了之后注意我现在要做的事要测试怎么测你会发现它这里面是不是有一个叫做content pass对吧如果我们现在访问的话如果我现在这么访问能行吗不行了为什么
[01:54] 因为你已经干嘛使用了这个配置这个配置的路径是不是就变成了杠A了懂吧所以这里边你要用杠A看可以吧你会发现挺神奇什么意思就是如果说这个配置你在配置文件里边配其实是一样的你把这个配置考出来考到我们的这个配置文件里边OK的没问题
[02:20] 只不过现在我们把这一堆东西干嘛把它移到了NICOS里面配了大家理解吗所以说其实你在NICOS里面配它这个应用程序呢这个微服务在加载的时候它就从NICOS里面来读取这个配置来加载就跟你在配置文件里面配的效果是一样的对但有时候老师有个问题有啥问题
[02:45] 我知道了具体的配置的方法了是吧但是各位你想现在我通过-a访问那你要注意这个配置文件作为公共的配置文件所有的微服务的路径都不可能都叫-a对不对所以这时候你说如果我们说这个公用的配置有些配置信息我们微服务想个性化配置怎么办呢因为我们刚才学习过扩展配置我们说了谁的优先级最高呢
[03:13] 是不是就是组配置文件它本身的优先级最高对不对所以我们想做一件事很容易我们只要把我们想个性化配置的信息我们把它干嘛抽取到组配置文件当中就行了比如我们现在想更改路径行不行更改路径我们就这么做
[03:40] 我们就在我们的这个组配置文件里面我们把这个路径改为杠各位我问你组配置文件优先级最高它里边有这个serverletcontentcontentpath这个属性它是不是会用覆盖这个公共配置文件里边的这个属性同样的这个相同的属性所以各位我现在
[04:02] 我要把这个consumer重启了之后这时候如果我要再访问我的程序路径我访问-a我问你能访问到吗能访问到吗肯定不行为什么因为主配置文件它的优先级最高它配的是斜杠是吧所以你访问它肯定不行你必须怎么弄改成根路径对这就是我们说的一个扩展配置的案例你会发现
[04:31] 原来我给大家讲的时候呢我是不是就是通过这个application contest的这个对象来获取配置但其实真正我们去用的时候其实我们就直接把我们实际上我们应用所需要的这些配置呢全部都在我们的Necros上面去配置了这是不是就是我们说哎你说其实我们正点八经去用的时候我们不用去获取这个配置其实我们会发现这个配置呢在应用程序启动的时候它已经生效了
[04:58] 它就是我们应用程序访问的这个路径这是不是就有效果了这就是我们的自定义扩展配置的一个案例希望大家来理解一下整个的流程后边我们去做Nexus应用的时候基本上都是按照这种模式有一个组配置文件还有些扩展配置文件还有一些公共的配置文件好那这个案例我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Nacos 配置中心使用 ext-config 功能，为 Spring Cloud 应用配置多个独立的配置文件，并通过 Nacos 管理这些配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的目录结构，当前章节为“3.2 Nacos 配置管理”，具体到“3.3.1 ext-config 扩展配置”。
画面 2: 浏览器访问 Nacos 配置中心的页面，显示应用名为 application1 configzhengzhou。
画面 3: 在 Nacos 界面创建新配置，Data ID 为 ext-config-http.yaml，Group 为 COMMON_GROUP。
画面 4: IDE 中展示 bootstrap.yaml 配置文件，其中包含两个 ext-config 配置项，分别指向 ext-config-common01.yaml 和 ext-config-common02.yaml。
画面 5: 在 Nacos 界面编辑配置，配置内容为 HTTP 和 server 相关的设置，包括 encoding、remote_ip_header、protocol_header、context-path 等。
画面 6: IDE 中展示 bootstrap.yaml 配置文件，其中 server.port 设置为 9002，provider.address 设置为 127.0.0.1:9001。
画面 7: IDE 中展示 bootstrap.yaml 配置文件，其中 http 和 server 配置项被高亮显示，包括 encoding、remote_ip_header、context-path 等。
画面 8: 浏览器访问 Nacos 配置中心的页面，显示应用名为 application1 configzhengzhou。
画面 9: 在 Nacos 界面编辑配置，Data ID 为 ext-config-http.yaml，Group 为 COMMON_GROUP。
画面 10: 在 Nacos 界面编辑配置，Data ID 为 ext-config-http.yaml，Group 为 COMMON_GROUP。
画面 11: 在 Nacos 界面编辑配置，Data ID 为 Nacos-RESTful-consumer.yaml，Group 为 DEFAULT_GROUP。
画面 12: IDE 中展示 bootstrap.yaml 配置文件，其中 server.addr 设置为 127.0.0.1:8888，配置文件名与 application.name 对应。
画面 13: 展示课程 PPT 的内容，说明如何将 servlet 公用配置抽离到独立的配置文件。
画面 14: 展示课程 PPT 的内容，介绍 Nacos Server 的安装准备，包括支持的 OS、JDK 版本和 Maven 版本。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```yaml
config:
  server-addr: 127.0.0.1:8888  # 配置中心地址
  file-extension: yaml
  # 指定配置文件的扩展名，配置文件名会根据application.name的值自动加前缀
  ext-config[0]:
    data-id: ext-config-common01.yaml
    group: COMMON_GROUP
    refresh: true
  ext-config[1]:
    data-id: ext-config-common02.yaml
    group: COMMON_GROUP
    refresh: true
```

画面 5:
```yaml
http:
  encoding:
    charset: UTF-8
    force: true
    enabled: true
  messages:
    encoding: UTF-8
server:
  local:
    remote_ip_header: x-forwarded-for
    protocol_header: x-forwarded-proto
    servlet:
      context-path: /
      use-forward-headers: true
```

画面 6:
```yaml
server:
  port: 9002
provider:
  address: 127.0.0.1:9001
spring:
  application:
    name: Nacos-RESTful-consumer  # 服务名
  cloud:
    Nacos:
      discovery:
        server-addr: 127.0.0.1:8888  # 服务发现中心地址
        namespace: f8ee3c1-1005-40c9-96a6-8c81f1512ab1  # 指定命名空间的id
      config:
        server-addr: 127.0.0.1:8888  # 配置中心地址
        file-extension: yaml  # 指定配置文件的扩展名，配置文件名会根据application.name的值自动加前缀
        ext-config[0]:
          data-id: ext-config-common01.yaml
          group: COMMON_GROUP
          refresh: true
        ext-config[1]:
          data-id: ext-config-common02.yaml
          group: COMMON_GROUP
          refresh: true
```

画面 7:
```yaml
http:
  encoding:
    charset: UTF-8
    force: true
    enabled: true
  messages:
    encoding: UTF-8
server:
  local:
    remote_ip_header: x-forwarded-for
    protocol_header: x-forwarded-proto
    servlet:
      context-path: /
      use-forward-headers: true
```

画面 12:
```yaml
spring:
  cloud:
    Nacos:
      discovery:
        server-addr: 127.0.0.1:8888  # 服务发现中心地址
        namespace: f8ee3c1-1005-40c9-96a6-8c81f1512ab1  # 指定命名空间的id
      config:
        server-addr: 127.0.0.1:8888  # 配置中心地址
        file-extension: yaml  # 指定配置文件的扩展名，配置文件名会根据application.name的值自动加前缀
        ext-config[0]:
          data-id: ext-config-common01.yaml
          group: COMMON_GROUP
          refresh: true
        ext-config[1]:
          data-id: ext-config-common02.yaml
          group: COMMON_GROUP
          refresh: true
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“3.2 Nacos 配置管理”，子标题包括“3.3.1 ext-config 扩展配置”。
画面 13: PPT 标题为“4. 服务和元数据管理”，子标题为“2.2.1 安装 Nacos Server”，内容包括“Nacos 预备 Java 环境来运行”，并列出支持的 OS、JDK 版本和 Maven 版本。
画面 14: PPT 标题为“2.2.2 下载源码或者安装包”，内容包括“你可以通过源码和发行包两种方式来获取 Nacos”，并列出从 GitHub 下载源码的方式。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

