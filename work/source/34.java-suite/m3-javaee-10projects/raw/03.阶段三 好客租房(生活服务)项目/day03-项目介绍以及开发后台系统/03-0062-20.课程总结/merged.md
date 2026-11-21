# 20.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\20.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 5分16秒（音频 316s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们对今天的这个内容呢,做一个简单的一个小节那么今天呢,我们讲了哪些内容呢,我们来过一下那么今天我们讲了这个项目的一个介绍啊,包括项目的背景啊,它的一些介绍啊,它的一些这个技术架构啊
[00:17] 包括它的系统架构我们也是提了一下我们整体会采用这种v服务的一种架构方式去做一个架构那么我们使用的一个主要的服务治理框架就是阿帕奇的 double框架ok好那么我们
[00:33] 去讲了后台系统这个搭建那么我们基于我们这个pro这个系统为我们的一个模板系统然后呢去做了一个项目的一个搭建对吧那么在搭建完成之后呢我们去对他的这个logo以及他的版权信心的做了一些修改然后呢我们又去制定了一些左侧的一些菜单
[00:54] 然后我们重点就讲了一下新增房源包括它的一些数据结构以及它的一些页面中的一些需要大家注意的一些点对吧包括这个form组件的使用表单的提交以及这个自动完成的功能的实现以及我们后面讲的图片的上传OK那么到这我们就已经把我们的后台系统的一些前端是不是已经搭建完成
[01:18] 那么我们就需要后台系统给我们提供一些服务的支撑那么我们是不是就可以去开发这样的一些功能了对不对所以我们就去搭建后台系统的服务那么我们后台系统的服务我其实我们讲的是通过这种double的形式是不是去做一个服务的提供那么这个double我们又没有去学过对吧所以我们下面又讲了一个double的一个快速入门OK包括讲了什么是double以及这个double是怎么去
[01:46] double的一个由来那么在这其实提一下double的读音其实是有一点点争议的那么有些资料上面去说它叫double有些叫duble那么其实我们统一一下我们就把它称之为叫做doubleok
[02:04] 好那么这个double呢以前的是这个阿里这个团队去应该是归属于这个阿里的那么现在呢他已经是在阿巴铁下面做一个孵化做一个孵化的一个动作预计可能很快会毕业好那么这个呢是讲了做了一个简单的介绍然后后面我们也讲了一些这个double这个框架的说明包括他的一些这个背景以及他的一些这个需求然后呢讲他的一个架构那么这个图非常重要
[02:33] 就是帮助我们去理解这个double这个框架呢这个图是非常重要的它的几部分的角色这个一定要搞清楚啊OK后面我们讲了注册中心注册中心呢可以有好多种注册中心但是呢比较推荐的使用的是什么呢这个ZooKeeper这种的注册中心哎OK好
[02:54] 那么我们是不是也去搭建了一个这个Rowkeeper那么Rowkeeper搭建的时候我们所采用的是这种Docker的形式那么这个也是比较建议推荐大家所使用的一种形式OK好那么我们接着继续往下面看那么下面我们又去编写了这种服务的提供方对吧然后我们最后在运行完成之后我们就可以发现
[03:18] 是不是我们的这个服务就可以成功的去注册到我们的注册中心里面去然后呢我们后面的又去编写了服务的这个消费方然后呢我们可以发现那么我们的这个消费方呢是不是也可以成功的去拿到我们的一个数据对吧那这样的话我们就已经把我们那个double是不是已经跑起来了哎OK好那么后面呢我们又讲了一个double的这个admin它呢是一个可视化的一个这样的管理工具那么这个也是官方所提供的一个管理工具然后呢
[03:48] 他的一个代码地址是在这然后他自己安装的步骤那都一一给大家做了一个讲解那么需要注意的是这个动作可能是相对比较时间比较长的一个动作这个需要大家耐心耐心的等待一下如果你第一次失败那么可以建议尝试第二次第三次那么他应该是能够成功的只要你的网络环境OK那么把这个MEMON的这个伺服改成阿里云的那个伺服
[04:14] 应该就问题不大然后最后我通过Mavin这个命令去启动我们这个项目然后通过我们这个浏览器去查看你就可以看到这样的一些页面那么通过我们这个人民管理工具就可以去管理我们的一些服务查看服务的一些具体的情况OK
[04:32] 后面的我们又讲了一些服务的负载均衡那么重点我们其实讲的是他的一个叫做轮旋的一种负载均衡那么我们通过一种测试的方式也看出他的一些这个结果啊就说的确会出现这种轮型这种效果的哎OK大家都他默认采用的呢负载均衡的是这种随机的这种负载均衡的方式哎OK好那么最后呢我们去给大家介绍了一下
[04:56] double框架一种double的协议它的相对比较适合用的是这种小数据量大并发的这种这样的场景OK好那么关于这个小节我们就讲到这里了那么在我们的下天的内容我们将去实现具体的功能好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Dubbo 的微服务架构搭建，包括前端工程、服务注册与发现、负载均衡等核心内容。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前选中“2.1.1 创建工程”。
画面2：展示“2. 后台系统搭建”章节，介绍后端采用 Spring Boot + StringMVC + Dubbo + MyBatis 技术栈。
画面3：展示“2.1.2 倾听log以及配置项”章节，显示项目目录结构，包含 src、test、Docker、config 等文件夹。
画面4：展示前端页面设计，包含表单元素和按钮。
画面5：展示父子组件间数据传递的代码示例，包括父组件的 handleChange 方法和子组件的 handleFileList 方法。
画面6：展示“3.2.1、什么是dubbo?”章节，介绍 Apache Dubbo 是一款高性能 Java RPC 框架。
画面7：继续展示“3.2.1、什么是dubbo?”章节，介绍 Dubbo 的早期介绍和架构。
画面8：展示 Dubbo 架构图，包括 Registry、Provider、Consumer、Monitor 等组件及其交互关系。
画面9：展示使用 Docker 部署 ZooKeeper 的命令，包括 Docker pull、Docker create、Docker start。
画面10：展示 Maven 项目中的 pom.xml 文件，包含 dubbo-consumer、dubbo-services 等依赖。
画面11：展示 Dubbo 服务的配置文件，包括 dubbo.registry.address 和 application.properties。
画面12：展示服务的负载均衡页面，包含 Provider 和 Consumer 的信息。
画面13：展示设置负载均衡策略的 Java 代码，包括 TestUserService 类和 testQueryAll 方法。
画面14：展示 Dubbo 通信流程图，包括 Client、Header、Body、Server、Dispatcher 等组件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
父组件中的方法，获取数据：
handleFileList = (obj) => {
console.log(obj, "图片列表");
}
画面9：
#拉取镜像
Docker pull ZooKeeper:3.5
#创建容器
Docker create --name zk -p 2181:2181 ZooKeeper:3.5
#启动容器
Docker start zk
画面10：
<project xmlns="http://maven.apache.org/POM/4.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
<parent>
<artifactId>itcast-dubbo</artifactId>
<groupId>itcast.dubbo</groupId>
<version>1.0-SNAPSHOT</version>
</parent>
<modelVersion>4.0.0</modelVersion>
<artifactId>itcast-dubbo-consumer</artifactId>
<dependencies>
<!-- 添加Spring Boot依赖，web组件 -->
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-web</artifactId>
</dependency>
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
<groupId>itcast.dubbo</groupId>
<artifactId>itcast-dubbo-services</artifactId>
<version>1.0-SNAPSHOT</version>
</dependency>
</dependencies>
画面11：
dubbo.registry.address=ZooKeeper://127.0.0.1:2181
画面12：
dubbo.registry.address=ZooKeeper://127.0.0.1:2181
画面13：
package cn.itcast.dubbo.consumer;
import cn.itcast.dubbo.pojo.User;
import cn.itcast.dubbo.Service.UserService;
import com.alibaba.dubbo.config.annotation.Reference;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import java.util.List;
@RunWith(SpringRunner.class)
@SpringBootTest
public class TestUserService {
@Reference(version = "1.0.0", loadbalance = "roundrobin")
private UserService userService;
@Test
public void testQueryAll(){
for (int i = 0; i < 50; i++) {
List<User> users = this.userService.queryAll();
}
}
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
标题：2、后台系统搭建
内容：后台系统采用前后端分离开发模式，前端使用 Ant Design Pro 作为模板进行开发，后端采用 Spring Boot + StringMVC + Dubbo + MyBatis 的架构进行开发。
画面8：
标题：Dubbo Architecture
结构：
- init → subscribe → notify → register → count → start
- Consumer → Provider → Monitor
画面14：
标题：Dubbo 通信流程图
结构：
Client → Header → Body → Server → Dispatcher
- Transporter：min，netty，grizzly
- Serialization：dubbo，hessian2，java，json
- Dispatcher：all，direct，message，execution，connection
- ThreadPool：fixed，cached
- 协议：TCP
- 序列化：Hessian 二进制序列化
- 适用场景：常规远程服务方法调用

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

