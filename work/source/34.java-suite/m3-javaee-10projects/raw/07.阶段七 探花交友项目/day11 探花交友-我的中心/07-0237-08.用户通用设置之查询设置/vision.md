# 画面线理解：08.用户通用设置之查询设置

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\08.用户通用设置之查询设置_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 02:33, 03:34, 04:47, 05:51, 06:48, 07:58, 09:47, 10:36, 11:44, 12:25, 13:45, 14:37, 16:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:41:46

1) 这一组画面整体在讲什么（一句话）：
讲解用户服务模块中，如何通过 UserService 实现用户点赞、取消点赞、查询设置、查询陌生人问题等功能，并展示相关代码和接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中“2.1、表结构”部分，包含一个手机界面截图，显示“深花交友-传智播客研究院”应用的用户功能按钮，以及一个 SQL 语句：
CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `like_r` int(11) NOT NULL,
  `gongga` varchar(255) NOT NULL,
  `create` datetime NOT NULL,
  `update` datetime NOT NULL,
  `PRATH` varchar(255) NOT NULL,
  `FICNT` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

画面2：展示 IntelliJ IDEA 中 UserService.java 文件的代码，其中包含一个 `likeFan` 方法，调用 `this.userLikeApi.saveUserLike(user.getId(), userId)`。

画面3：展示 IntelliJ IDEA 中 SettingsService.java 文件的代码，包含包声明和多个注解，如 `@Configuration`, `@EnableConfigurationProperties`, `@ComponentScan` 等。

画面4：展示 Advanced REST Client 界面，显示一个 API 接口的参数表，包含字段如 `id`, `name`, `gender`, `age`, `education` 等，以及它们的类型、是否必填、默认值和备注。

画面5：展示 Typora 文档中“2.2、pojo”部分，包含一个 API 接口的请求参数表，Headers 中包含 `Content-Type: application/json`，以及一个模糊的响应体。

画面6：展示 IntelliJ IDEA 中 UserService.java 文件的代码，包含 `@Autowired` 注解的多个私有属性，如 `userInfoService`, `userLikeApi`, `visitorsApi`, `recommendUserService`。

画面7：展示 IntelliJ IDEA 中 SettingsService.java 文件的代码，包含 `import` 语句和一个 `querySettings` 方法，其中调用 `this.settingsMapper.selectOne()`。

画面8：展示 IntelliJ IDEA 中 UserService.java 文件的代码，包含 `dislike` 方法，调用 `this.userLikeApi.deleteUserLike(user.getId(), userId)`。

画面9：展示 IntelliJ IDEA 中 UserService.java 文件的代码，包含 `likeFan` 方法，调用 `this.userLikeApi.saveUserLike(user.getId(), userId)`。

画面10：展示 IntelliJ IDEA 中 UserService.java 文件的代码，包含一个 `switch` 语句，处理不同类型的用户列表查询，如 `case 1:`, `case 2:`, `case 3:`, `case 4:`。

画面11：展示 IntelliJ IDEA 中 SettingsVo 类的代码，包含 `settingsService`, `settings`, `setting`, `settingsMapper` 等属性，以及 `set` 方法。

画面12：展示 Advanced REST Client 界面，显示一个 HTTP 请求的响应，状态码为 401，响应体为空。

画面13：展示 IntelliJ IDEA 中 UserService.java 文件的代码，包含 `querySettings` 方法，调用 `this.settingsService.querySettingsByUserId(user.getId())`，并设置 `SettingsVo` 对象的属性。

画面14：展示 Typora 文档中“2.6、保存陌生人问题”部分，包含一个 API 接口的请求和响应，以及一个模糊的响应体。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `like_r` int(11) NOT NULL,
  `gongga` varchar(255) NOT NULL,
  `create` datetime NOT NULL,
  `update` datetime NOT NULL,
  `PRATH` varchar(255) NOT NULL,
  `FICNT` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

画面2：
public void likeFan(Long userId) {
  User user = UserThreadLocal.get();
  this.userLikeApi.saveUserLike(user.getId(), userId);
}

画面3：
package com.tanhua.server.service;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableConfigurationProperties;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Primary;
import org.springframework.context.annotation.Scope;
import org.springframework.context.annotation.Lazy;
import org.springframework.context.annotation.Import;
import org.springframework.context.annotation.ImportResource;
import org.springframework.context.annotation.ImportSelector;
import org.springframework.context.annotation.ImportBeanDefinitionRegistrar;
import org.springframework.context.annotation.ConfigurationClassPostProcessor;
import org.springframework.context.annotation.ConfigurationClass;
import org.springframework.context.annotation.ConfigurationClassParser;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistry;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import org.springframework.context.annotation.ConfigurationClassBeanDefinitionRegistryPostProcessor;
import
