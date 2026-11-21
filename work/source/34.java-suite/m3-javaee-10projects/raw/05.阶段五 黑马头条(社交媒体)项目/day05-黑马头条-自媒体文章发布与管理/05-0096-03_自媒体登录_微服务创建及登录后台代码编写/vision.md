# 画面线理解：03_自媒体登录_微服务创建及登录后台代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\03_自媒体登录_微服务创建及登录后台代码编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 01:27, 02:31, 03:51, 06:04, 08:01, 09:18, 11:06, 12:18, 13:44, 15:33, 17:16, 18:27, 19:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:40:38

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的用户登录功能的开发过程，包括项目结构、配置文件、数据库表设计、Mapper 接口、Service 实现和 Controller 控制器的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 打开 IntelliJ IDEA，显示项目结构，当前选中 pom.xml。
画面 2: 打开 application.properties 文件，显示配置项 server.port=3(port.media) 和 spring.application.name=3(sn.media)。
画面 3: 打开 MediaApplication.java，展示 Spring Boot 启动类，光标在 main 方法中。
画面 4: 打开 IntConfig.java 文件，展示 @Configuration 注解和 @ComponentScan 注解。
画面 5: 打开 Navicat for MySQL，显示数据库表结构，正在编写 CREATE TABLE `wm_user` 语句。
画面 6: 在 IDEA 中，弹出复制文件对话框，准备复制文件到 mappers 目录。
画面 7: 在 IDEA 中，右键点击项目目录，弹出创建新文件的菜单。
画面 8: 打开 UserLoginServiceImpl.java，正在编写 login 方法，光标在 if (StringUtils.isEmpty(user.getUserName())) 判断语句。
画面 9: 在 UserLoginServiceImpl.java 中，光标在 wuUserMapper.selectByName(user.getUserName()) 方法调用处。
画面 10: 在 UserLoginServiceImpl.java 中，光标在 if (user.getPassword().equals(wuUser.getPassword())) 判断语句。
画面 11: 在 UserLoginServiceImpl.java 中，光标在 result.put("token", JwtUtil.getToken()) 语句。
画面 12: 打开 UserLoginService.java 接口文件，定义 login 方法。
画面 13: 打开 LoginControllerApi.java，展示 @RestController 和 @RequestMapping 注解。
画面 14: 打开 LoginController.java，展示 @RestController、@RequestMapping("/api/v1/media") 和 login 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
server.port=3(port.media)
spring.application.name=3(sn.media)

画面 3:
package com.heima.media;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MediaApplication {
    public static void main(String[] args) {
        SpringApplication.run(MediaApplication.class, args);
    }
}

画面 4:
package com.heima.media.config;
import ...
@Configuration
@ComponentScan("com.heima.login.common.init")
public class IntConfig {

}

画面 5:
CREATE TABLE `wm_user` (
  id int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  ap_author_id int(11) DEFAULT NULL,
  name varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '登录用户名',
  password varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '登录密码',
  nickname varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '昵称',
  image varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '头像',
  phone varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号',
  email varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '邮箱',
  score tinyint(3) unsigned DEFAULT NULL COMMENT '积分',
  login_time datetime DEFAULT NULL COMMENT '登录时间',
  status tinyint(1) DEFAULT '1' COMMENT '状态',
  create_time datetime DEFAULT NULL COMMENT '创建时间',
  update_time datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `idx_user_name` (`name`),
  KEY `idx_user_email` (`email`),
  KEY `idx_user_phone` (`phone`),
  KEY `idx_user_password` (`password`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
  KEY `idx_user_score` (`score`),
  KEY `idx_user_status` (`status`),
  KEY `idx_user_ap_author_id` (`ap_author_id`),
  KEY `idx_user_create_time` (`create_time`),
  KEY `idx_user_update_time` (`update_time`),
  KEY `idx_user_login_time` (`login_time`),
