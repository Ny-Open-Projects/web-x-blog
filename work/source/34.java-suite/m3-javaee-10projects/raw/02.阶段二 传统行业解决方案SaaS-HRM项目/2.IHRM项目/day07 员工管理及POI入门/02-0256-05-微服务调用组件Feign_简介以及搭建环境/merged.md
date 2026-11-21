# 05-微服务调用组件Feign：简介以及搭建环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\05-微服务调用组件Feign：简介以及搭建环境_【海量资源尽在 ubkz.com】.mp4
- 时长 9分44秒（音频 585s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们已经把这个Erica呢全部都配置好了那这边呢配置好了之后各位会发现在Erica服务里面其实已经注册了我们所有的我们叫做微服务并且呢这边有我们的微服务名称和微服务请求的地址那其实呢咱们配置好了Erica之后这边呢给各位准备了一张图这边呢就看到了我们整个的这么一个结构那各位来看一下我们现在把所有的微服务呢全部注册到了Erica服务上
[00:32] 那接下来就是说咱们都知道在企业微服务这边我们好了我把这个图呢以另一种方式打开啊我要写点东西好了那我们都知道在企业微服务当中呢它分为有部门的这么一个概念有部门的这么一个概念都知道它有一个接口呢叫做根据ID请求部门没错吧这是一个我们的请求接口那接下来我们呢这个部门呢在企业微服务这边
[01:04] 那它连接的就是我们的企业数据库所以这个数据库在这边那如果说我想要在系统微服务当中去访问企业微服务的这个接口那我应该如何去做呢那其实要想去访问它并不难比较简单那我们都知道这个呢其实它代表的是一个http接口没错吧那我只需要在企业微服务这边发送一个hp请求到我们的企业微服
[01:33] 那是不是就能得到这个数据呢没错吧OK那其实我们自己去写一个HTTP请求发送过来也可以但是人家Spring Cloud提供了更加好的组件去帮助我们解决这个问题这个组件是什么就是我们接下来要跟各位聊的叫做微服务调用组件FIN好了这个微服务调用组件FIN它其实是一个简化的HTTP扣端工具
[02:01] 那我们刚才得知了两个之间飞幅之间调用调用发送HP请求就是就可以了那这个FIN呢其实就是一种工具它只不过降低了我们代码开发的这么一个难度而已哎那接下来呢我们就关注的我们就关注的是对于这个FIN组件如何去使用它其实就可以了那对于这个FIN组件呢要想去使用它
[02:27] 那其实不难一共呢有这么几个我们需要关注的步骤首先第一个分自然是一个组件我们就需要把它引入到我们的工程当中也就是说要添加依赖好了添加了依赖接下来第二件事第二件事注意了啊这些不管是你添加的依赖还是我们接下来要添加的注解等等等等那这些操作全部是配置到谁去调用你就配置谁那我们都知道在系统为福要想调企业的
[02:58] 我们这边是不是要去准备发送HTTP请求啊P请求那谁去调用那就要配置到哪一端所以呢我们比如说要通过系统微服务调用企业微服务那我就需要在系统微服务这边做如下的这些配置那这些配置我们刚才说过了第一个添加依赖第二个在启动类上添加两个诸解还有第三个第三个这个是比较关键的我们需要写一个接口
[03:30] 需要写一个接口这个接口里面要用注解进行配置注解这个配置配置的是什么各位咱们不是要调用企业微服务吗咱们不是要调用企业微服务吗那企业微服务我们是不是给它起了个名字叫做IHRM Company所以我要告诉它我要调用的是企业微服务这个企业微服务的名字CompanyOK那接下来
[03:57] 里面你想调用哪个接口其实说白了咱们自己发送HP请求其实就是请求HP接口其实就可以了接下来我们关注的你可以随便写一方法在这个方法上使用at request mapping你要调用到微服务上的哪个请求地址OK好了这个就是我们要创建这么一个接口写一个我们的注解需要调用到哪个请求地址写上好了接下来还有第四件事第四件事就是去使用它了OK那好了
[04:28] 当然了还有第五件事这个第五件事呢其实就是配置一个拦截器主要是为了适应我们这套系统要设置一个它的请求头好了这个呢基本的这么一个流程和各位做了一个介绍那接下来呢我们就可以写代码把它实现掉好了那接下来呢我们就一步一步的把它实现其实就可以了首先第一个谁发起调用谁发起请求就在哪个微服上添加依赖即可
[04:54] 这个依赖呢在今天的资料当中呢也给各位以碰文件形式给各位提供了在这边Ctrl C复制到我们的系统V服务当中注意是系统V服务System好了碰文件打开OK底下Ctrl V添加过来那需要注意的这个其实说明了一个通过它的名称就能看到其实它就是打开我们这个系统调用Open这个组件好了那接下来
[05:26] 坐标添加过来了之后接下来就是第二件事需要在我们的启动类上添加两个注解第一个就是Discover Client第二个就是Enable Fin Clients这两个注解其实它的主要目的就是开启发现其他的客户端因为我们要去发现咱们不是要去调用我们叫做企业为服务吗你先能找到它那如何代表能去开启找到就是Enable Discover Client
[05:52] 好了那接下来再去实现调用那调用其实借助的是fint接着就是开启调用其实就可以了所以呢把这两个注解我们也配置到我们系统微幅还是那句话谁发起就在谁上面配置系统微幅好了在上面呢添加两个注解第一个注解enablediscoveryclans好了接着enable好了我们叫做fintclans
[06:24] 好了这两个注解添加好了之后那这样一来我当前系统就具备了访问其他微服的能力好了你想要比如说呢我们刚才的案例是我想要去调用我们企业微服里面的根据ID查询部门的这个接口我们找到企业微服那找到企业微服的里面的Department Controller里面呢我们写过一个接口叫做Find By ID那需要各位注意的是
[06:54] 我怎么通过我的系统微服务去调用企业微服务很简单很简单在适当的位置你去写一个接口好了我这边呢就放到了比如说我就叫做clant这个包下注意它是一个接口这个接口的名称呢其实叫什么无所谓了department我叫finclant吧finclantok好了那这个接口呢主要目的主要目的其实就是
[07:32] 声明接口通过此接口通过fin调用其他微服好了接下来就是在这个接口上我们需要去完成一些操作这个操作我们可以打开讲义来看首先第一个就是说你需要去配置你要调用哪个微服的功能使用一个finclant来声明ata finclant来声明
[08:12] 那我们要调用的微服务呢是不是就是就是我们的IHRM企业微服务里面的内容那么的企业微服务呢其实我们之前在配置的时候已经给它起过一个名字就叫做IHRM Company所以我这边要调用哪个就直接写它的名称即可好了那接下来你要调用这个企业微服务那要调用这个企业微服务当中的什么接口我们底下就要去配置接口
[08:48] 微服务的接口上面其实在去声明调用的微服务名称OK那如何去调指定调用微服务的接口呢其实很简单了at request mapping那跟各位简单的说一下这个request mapping呢其实和我们这个企业微服务你要调用的这个配置是一模一样的所以把它直接Ctrl C拷过来即可那还有一点就是说
[09:21] 这个方法名字也可以是一模一样的只不过它是一个接口而已OK那这样一来我们这个接口就已经写好了那这个接口写好了那我们一会儿就可以通过这个接口进行调用其他的调用我们这个部门微服务里面的方法了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在微服务架构中使用 Feign 组件实现服务间的远程调用，具体操作包括添加依赖、配置注解、创建接口和修改控制器。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Eureka 服务注册中心页面，显示三个服务实例（IHRM-COMPANY、IHRM-EMPLOYEE、IHRM-SYSTEM）均处于 UP 状态，同时显示了 Windows 开始菜单。
画面2：展示一个流程图，描述 Eureka 服务注册中心与三个微服务（企业微服务、系统微服务、员工微服务）之间的注册关系，以及各服务与对应数据库的连接。
画面3：展示 PPT 页面，标题为“1.5 微服务调用组件Feign”，内容包括 Feign 的简介和快速体验步骤，其中包含添加依赖的 Maven 代码片段。
画面4：展示流程图，与画面2类似，但“企业微服务”框内文字被修改为“根据id请求部门 http接口”。
画面5：展示 PPT 页面，内容为修改 hrm_system 模块启动类添加注解的步骤，包含 @EnableDiscoveryClient 和 @EnableFeignClients 注解。
画面6：展示 PPT 页面，内容为在 hrm_system 模块中创建 com.ihrm.system.client 包并创建接口，以及修改 UserController 的代码。
画面7：展示 Notepad++ 编辑器中的配置文件，内容为服务注册到 Eureka 的配置，包含 server.port、Eureka.client.Service-url 等配置项。
画面8：展示 IntelliJ IDEA 中的项目结构，显示 hrm_system 模块的目录结构，包括 src/main/java 和 src/main/resources。
画面9：展示 Windows 系统的“显示桌面”功能，显示多个打开的窗口，包括 PPT、IDEA、Notepad++ 等。
画面10：展示 IntelliJ IDEA 中的 SystemApplication.java 文件，包含 Spring Boot 启动类代码，包括 @EnableDiscoveryClient 和 @EnableFeignClient 注解。
画面11：展示 IntelliJ IDEA 中的 DepartmentController.java 文件，包含两个 RESTful 接口方法：findALL 和 findById。
画面12：展示 IntelliJ IDEA 中的 DepartmentFeignClient.java 文件，正在输入 @FeignClient 注解。
画面13：展示 IntelliJ IDEA 中的 DepartmentController.java 文件，显示了 update 和 delete 接口方法。
画面14：展示 IntelliJ IDEA 中的 DepartmentFeignClient.java 文件，显示了 @FeignClient 注解和 findById 接口方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```
画面5：
```java
@EnableDiscoveryClient
@EnableFeignClients
```
画面6：
```java
//测试通过系统微服务调用企业微服务方法
@RequestMapping(value = "/test/{id}")
public void findDeptById(@PathVariable String id){
    Department dept = departmentFeignClient.findById(id);
    System.out.println(dept);
}
```
画面7：
```yaml
#Eureka服务的配置文件
server:
  port: 8888 #服务端口
Eureka:
  client:
    registerWithEureka: false #是否将自己注册到Eureka服务中，本身就是所有无需注册
    fetchRegistry: false #是否从Eureka中获取注册信息
    serviceUrl:
      defaultZone: http://127.0.0.1:6888/Eureka/
#微服务注册到Eureka配置
Eureka:
  client:
    Service-url:
      defaultZone: http://localhost:6888/Eureka/
```
画面10：
```java
package com.ihrm.system;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@EnableDiscoveryClient
@EnableFeignClients
@ComponentScan(basePackages = "com.ihrm")
public class SystemApplication {
    public static void main(String[] args) {
        SpringApplication.run(SystemApplication.class, args);
    }
}
```
画面11：
```java
//企业id，目前使用固定值1，以后会根据企业id查询
//调用Service完成保存企业
departmentService.save(department);
return new Result(ResultCode.SUCCESS);
```
画面12：
```java
package com.ihrm.system.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient("ihrm-company")
public interface DepartmentFeignClient {

    @RequestMapping(value = "/department/{id}", method = RequestMethod.GET)
    public Result findById(@PathVariable(value = "id") String id);
}
```
画面13：
```java
//根据id删除department
@RequestMapping(value = "/department/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(value = "id") String id) {
    departmentService.delete(id);
    return new Result(ResultCode.SUCCESS);
}
```
画面14：
```java
package com.ihrm.system.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient("ihrm-company")
public interface DepartmentFeignClient {

    @RequestMapping(value = "/department/{id}", method = RequestMethod.GET)
    public Result findById(@PathVariable(value = "id") String id);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：流程图结构：
- “Eureka 服务”指向“企业微服务”、“系统微服务”、“员工微服务”，标注“注册”；
- “企业微服务”指向“企业库”，标注“根据id请求部门 http接口”；
- “系统微服务”指向“系统库”，标注“根据id请求部门 http接口”；
- “员工微服务”指向“员工”，标注“根据id请求部门 http接口”。

画面3：PPT标题为“1.5 微服务调用组件Feign”，内容包括：
- 1.5.1 简介：Feign 是简化 Java HTTP 客户端开发的工具，灵感来自 Retrofit、JAXRS-2.0 和 WebSocket。
- 1.5.2 快速体验：包括三个步骤，分别对应添加依赖、修改启动类、创建接口。

画面6：PPT标题为“1.5.2 快速体验”，内容包括：
- （4）修改 hrm_system 模块的 UserController，包含测试通过系统微服务调用企业微服务方法的代码。

画面10：PPT标题为“1.5.2 快速体验”，内容包括：
- （2）修改 hrm_system 模块的启动类，添加注解 @EnableDiscoveryClient 和 @EnableFeignClients。

画面12：PPT标题为“1.5.2 快速体验”，内容包括：
- （3）在 hrm_system 模块创建 com.ihrm.system.client 包，包内创建接口。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

