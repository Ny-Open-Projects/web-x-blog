# 22-总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\22-总结_【海量资源尽在 ubkz.com】.mp4
- 时长 2分54秒（音频 174s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 那到目前呢我们今天的所有内容就跟各位都聊过了对于我们今天呢其实做的主要内容呢一共就这么几小块首先呢就是一个权限相关的这么一个设计希望各位要知道我们这个权限是以RBAC这套思想演化出来的在我们的权限的基础上分成了权限以及资源的这么一个控制那么权限和资源其中是一对一的这么一种关系那所以我们操作权限的时候千万别忘了
[00:31] 除了要对权限表在文操作之外还要对菜单以及它对应的按钮资源以及它的API资源进行同步操作这是一个我们要注意的点这个权限我们看过了之后接着我们第二方面就是一个分配角色分配角色和分配权限是我们完成权限控制必不可少的这么两个阶段分配角色指的是对不同的用户分配不同的角色
[00:56] 那分配权限指的是对不同的角色分配不同的权限这个有点像让口令啊那通过这样一来我们一个用户登录过来之后首先检查一下他究竟是什么角色那接着通过他的角色找到他能够访问的这些权限好了那接着我们进行控制所以这两个是我们必不可少的两个阶段那分配角色权限搞定了之后接下来我们又看了一下长期的认证机制是通过四个角度为跟各位说的最基础的HTTP base那这种方式呢是总要携带用户密码
[01:26] 它太潮漏了并且呢它的安全性最低那第二是cookie这是我们最常见的单web应用常见的一种方式借助cookie和session共同去认证我们已经登录的用户数据好了还有第三个第三个就是allalso好了这个是一个开放授权的一种标准那它是大广泛应用于第三方登录等等第三方应用获取资源的这么一种服务
[01:50] 那比如说最典型的就是我们的微信联合登录那微信登录首先呢你搞一个二维码点击确定之后就认为你默认拿到了许可拿到许可通过许可去访问令牌那这个令牌才是你访问资源必不可少的这么一个数据
[02:05] OK好了这个我们说过了接下来又就是我们token那对于token来说呢是目前微服务和我们分布式操作经常用的这一种手段那这个呢它脱离了服务端存储所有的数据全部都是以前端保存为准就是前端会把数据发送到后端后端进行校验看一下这个数据是不后端签发出来
[02:27] 那对于token现在用的最广泛的呢其实就是一个JWT那在咱们Java事件也支持JWT当然了我们玩JWT看了一下如何进行token的签发以及如何对token进行鉴定那最后呢我们在我们的系统当中使用token的方式进行了一个登录的一个认证以及从我们的token数据token当中获取了一些用户数据这个就是我们今天所有内容简单的说了两句OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解权限管理与JWT鉴权的理论与实现，包括需求分析、角色分配、常见认证机制（Basic Auth、Cookie Auth、OAuth、Token Auth）以及JWT的快速入门和实际应用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：第4章 权限管理与jwt鉴权，学习目标包括理解权限管理需求、角色分配、常见认证机制、使用WT完成Token签发与验证。展示“1.1 需求分析”部分，包含“菜单表”、“页面元素”、“API接口”、“权限表”四个实体的字段定义及它们之间的关系（FK_PM_MENU、FK_PM_ELEMENT、FK_PM_API）。
画面2：与画面1内容相同，仅页面缩放比例略有不同。
画面3：继续展示“1.1 需求分析”，下方文字说明“权限与菜单，菜单与按钮，菜单与API接口都是一对一关系”，并引出“1.2 后端实现”。
画面4：切换至“2 分配角色”章节，展示“2.1 需求分析”，包含一个“分配角色”弹窗界面，说明用户与角色之间是多对多关系。
画面5：切换至“4 常见的认证机制”章节，展示“4.1 HTTP Basic Auth”、“4.2 Cookie Auth”、“4.3 OAuth”、“4.4 Token Auth”四个小节标题。
画面6：继续展示“4.1 HTTP Basic Auth”、“4.2 Cookie Auth”、“4.3 OAuth”三个小节的介绍文字。
画面7：展示“4.3 OAuth”的流程图，包含“客户端”、“资源拥有者”、“验证服务器”、“资源服务器”四个角色，以及“1 请求授权”、“2 获取授权许可”、“3 授权访问”、“4 访问令牌”、“5 请求资源”、“6 获取资源数据”六个步骤。
画面8：与画面7内容相同，仅鼠标指针位置不同。
画面9：展示“4.4 Token Auth”的介绍文字，说明其适用于个人消费者产品，不适用于自有认证权限管理的企业应用。
画面10：继续展示“4.4 Token Auth”的介绍文字。
画面11：展示“5.2 JWT的快速入门”章节，具体为“5.2.1 token的创建”，包含“（1）创建maven工程，引入依赖”的XML配置代码和“（2）创建类CreateJwtTest，用于生成token”的Java代码。
画面12：展示“5.4 登录成功签发token”章节，包含“（1）配置jwtUtil，修改hrm_system工程的启动类”的Java代码和“（2）添加登录方法”的Java代码。
画面13：展示“5.5 获取用户信息鉴权”章节，包含“前后端约定：前端请求微服务时需要添加头信息Authorization，内容为Bearer+空格+token”的说明，以及“（1）添加响应对象”的Java代码。
画面14：与画面13内容相同，仅鼠标指针位置不同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面11：
（1）创建maven工程，引入依赖
<dependency>
<groupId>io.jsonwebtoken</groupId>
<artifactId>jjwt</artifactId>
<version>0.6.0c</version>
</dependency>

（2）创建类CreateJwtTest，用于生成token
public class CreateJwtTest {
public static void main(String[] args) {
JwtBuilder builder = Jwts.builder().setId("888")
.setSubject("小白")
.setIssuedAt(new Date())
.signatureWith(SignatureAlgorithm.HS256, "ltcast");
System.out.println( builder.compact() );
}
}

画面12：
（1）配置jwtUtil，修改hrm_system工程的启动类
@Bean
public JwtUtil jwtUtil() {
return new util.JwtUtil();
}

（2）添加登录方法
package com.ihrm.system.Controller;
import com.ihrm.common.entity.Result;
import com.ihrm.common.entity.ResultCode;
import com.ihrm.common.exception.CommonException;
import com.ihrm.common.utils.JwtUtil;
import com.ihrm.system.domain.User;
import com.ihrm.system.Service.UserService;
import io.jsonwebtoken.Claims;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

画面13：
（1）添加响应对象
@Getter
@Setter
@NoArgsConstructor
public class ProfileResult {
private String mobile;
private String username;
private String company;
private Map roles;
public ProfileResult(User user) {
this.mobile = user.getMobile();
this.username = user.getUsername();
this.company = user.getCompanyName();
//角色数据
Set<String> menus = new HashSet<>();
Set<String> points = new HashSet<>();
Set<String> units = new HashSet<>();

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面7：流程图结构：
- “客户端”指向“资源拥有者”（步骤1：请求授权）
- “资源拥有者”指向“验证服务器”（步骤2：获取授权许可）
- “验证服务器”指向“资源服务器”（步骤3：授权访问）
- “资源服务器”指向“客户端”（步骤4：访问令牌）
- “客户端”指向“资源服务器”（步骤5：请求资源）
- “资源服务器”指向“客户端”（步骤6：获取资源数据）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

