# 画面线理解：22-总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\22-总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:07, 00:42, 00:45, 01:21, 01:29, 01:54, 01:58, 02:08, 02:13, 02:34, 02:43, 02:46, 02:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:03:18

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
package com.ihrm.system.controller;
import com.ihrm.common.entity.Result;
import com.ihrm.common.entity.ResultCode;
import com.ihrm.common.exception.CommonException;
import com.ihrm.common.utils.JwtUtil;
import com.ihrm.system.domain.User;
import com.ihrm.system.service.UserService;
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
