# 画面线理解：20.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\20.课程总结【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:32, 00:46, 01:02, 01:15, 01:42, 02:18, 02:30, 02:59, 03:27, 03:55, 04:31, 04:49, 05:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:38:29

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Dubbo 的微服务架构搭建，包括前端工程、服务注册与发现、负载均衡等核心内容。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前选中“2.1.1 创建工程”。
画面2：展示“2. 后台系统搭建”章节，介绍后端采用 SpringBoot + StringMVC + Dubbo + MyBatis 技术栈。
画面3：展示“2.1.2 倾听log以及配置项”章节，显示项目目录结构，包含 src、test、docker、config 等文件夹。
画面4：展示前端页面设计，包含表单元素和按钮。
画面5：展示父子组件间数据传递的代码示例，包括父组件的 handleChange 方法和子组件的 handleFileList 方法。
画面6：展示“3.2.1、什么是dubbo?”章节，介绍 Apache Dubbo 是一款高性能 Java RPC 框架。
画面7：继续展示“3.2.1、什么是dubbo?”章节，介绍 Dubbo 的早期介绍和架构。
画面8：展示 Dubbo 架构图，包括 Registry、Provider、Consumer、Monitor 等组件及其交互关系。
画面9：展示使用 Docker 部署 ZooKeeper 的命令，包括 docker pull、docker create、docker start。
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
docker pull zookeeper:3.5
#创建容器
docker create --name zk -p 2181:2181 zookeeper:3.5
#启动容器
docker start zk
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
<!-- 添加spring boot依赖，web组件 -->
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
<groupId>org.apache.zookeeper</groupId>
<artifactId>zookeeper</artifactId>
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
dubbo.registry.address=zookeeper://127.0.0.1:2181
画面12：
dubbo.registry.address=zookeeper://127.0.0.1:2181
画面13：
package cn.itcast.dubbo.consumer;
import cn.itcast.dubbo.pojo.User;
import cn.itcast.dubbo.service.UserService;
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
内容：后台系统采用前后端分离开发模式，前端使用 Ant Design Pro 作为模板进行开发，后端采用 SpringBoot + StringMVC + Dubbo + MyBatis 的架构进行开发。
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
