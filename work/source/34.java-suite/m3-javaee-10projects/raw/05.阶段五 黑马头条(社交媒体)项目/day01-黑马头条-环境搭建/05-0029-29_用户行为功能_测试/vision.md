# 画面线理解：29_用户行为功能_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\29_用户行为功能_测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:49, 01:38, 02:10, 02:40, 03:16, 03:42, 04:06, 04:38, 05:03, 05:37, 05:56, 06:20, 06:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:45:48

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中编写测试用例，通过 MyBatis 持久层操作数据库，实现对“用户行为”（show_behavior）数据的增删改查功能，并展示测试失败与成功的过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 在 IntelliJ IDEA 中，右键点击项目目录 `heima-leadnews-behavior` 的 `test` 包，选择“Show Image Thumbnail”。
- 编辑器中显示 `AppShowBehaviorMapper.xml` 文件，其中包含两个 SQL 映射语句：
  ```xml
  <select id="selectListByEntryIdAndArticleIds" resultMap="BaseResultMap">
      select
      <include refid="Base_Column_List"/>
      from ap_show_behavior
      where entry_id = #{entryId} and article_id in
      <foreach collection="articleIds" item="item" separator=",">
          #{item}
      </foreach>
  </select>

  <insert id="saveShowBehavior">
      insert into ap_show_behavior (entry_id, article_id, is_click, show_time, created_time) values
      <foreach collection="articleIds" item="item" separator=",">
          (#{entryId}, #{item}, 0, now(), now())
      </foreach>
  </insert>
  ```

画面 2：
- 项目结构中，`test` 包下的 `BehaviorTest.java` 文件被选中。
- 编辑器中显示 `BehaviorTest.java` 文件，内容为：
  ```java
  package com.heima.behavior.test;

  import com.heima.behavior.BehaviorJarApplication;
  import org.springframework.boot.test.context.SpringBootTest;

  @SpringBootTest(classes = BehaviorJarApplication.class)
  class BehaviorTest {
  }
  ```

画面 3：
- 项目结构中，鼠标悬停在 `test` 包下的 `resources` 目录上。
- 编辑器中显示 `AppShowBehaviorMapper.xml` 文件，内容与画面 1 相同。

画面 4：
- 项目结构中，`test` 包下的 `BehaviorTest.java` 文件被选中。
- 编辑器中显示 `BehaviorTest.java` 文件，内容为：
  ```java
  package com.heima.behavior.test;

  import com.heima.behavior.BehaviorJarApplication;
  import org.springframework.boot.test.context.SpringBootTest;

  @SpringBootTest(classes = BehaviorJarApplication.class)
  class BehaviorTest {
  }
  ```

画面 5：
- 项目结构中，`test` 包下的 `BehaviorTest.java` 文件被选中。
- 编辑器中显示 `BehaviorTest.java` 文件，内容为：
  ```java
  package com.heima.behavior.test;

  import com.heima.behavior.service.AppShowBehaviorService;
  import org.junit.runner.RunWith;
  import org.springframework.boot.test.context.SpringBootTest;
  import org.springframework.test.context.junit4.SpringRunner;

  @RunWith(SpringRunner.class)
  @SpringBootTest(classes = BehaviorJarApplication.class)
  public class BehaviorTest {

  }
  ```

画面 6：
- 在 Navicat for MySQL 中，选中数据库 `heima_leadnews`。
- 数据库表列表中，`ap_behavior_entry` 表被选中。
- 表结构显示为：
  ```sql
  CREATE TABLE `ap_behavior_entry` (
      `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
      `type_id` int(11) unsigned DEFAULT NULL COMMENT '实体类型id',
      `entry_id` int(11) unsigned DEFAULT NULL COMMENT '实体id',
      `created_time` datetime DEFAULT NULL COMMENT '创建时间',
      `buser` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户',
      `engine` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '引擎',
      `content` text COLLATE utf8mb4_unicode_ci,
      `status` int(11) DEFAULT '0' COMMENT '状态',
      `version` int(11) DEFAULT '0' COMMENT '版本',
      `is_deleted` int(11) DEFAULT '0' COMMENT '是否删除',
      `is_deleted_time` datetime DEFAULT NULL COMMENT '删除时间',
      `is_deleted_user` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除人',
      `is_deleted_reason` text COLLATE utf8mb4_unicode_ci,
      `is_deleted_ip` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除ip',
      `is_deleted_agent` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除agent',
      `is_deleted_browser` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除浏览器',
      `is_deleted_os` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除操作系统',
      `is_deleted_device` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除设备',
      `is_deleted_location` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除位置',
      `is_deleted_referer` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除来源',
      `is_deleted_url` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除url',
      `is_deleted_user_agent` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user agent',
      `is_deleted_user_ip` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user ip',
      `is_deleted_user_browser` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user browser',
      `is_deleted_user_os` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user os',
      `is_deleted_user_device` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user device',
      `is_deleted_user_location` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user location',
      `is_deleted_user_referer` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user referer',
      `is_deleted_user_url` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user url',
      `is_deleted_user_user_agent` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user agent',
      `is_deleted_user_user_ip` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user ip',
      `is_deleted_user_user_browser` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user browser',
      `is_deleted_user_user_os` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user os',
      `is_deleted_user_user_device` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user device',
      `is_deleted_user_user_location` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user location',
      `is_deleted_user_user_referer` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user referer',
      `is_deleted_user_user_url` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user url',
      `is_deleted_user_user_user_agent` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user user agent',
      `is_deleted_user_user_user_ip` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user user ip',
      `is_deleted_user_user_user_browser` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user user browser',
      `is_deleted_user_user_user_os` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user user os',
      `is_deleted_user_user_user_device` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user user device',
      `is_deleted_user_user_user_location` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user user location',
      `is_deleted_user_user_user_referer` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user user referer',
      `is_deleted_user_user_user_url` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user user url',
      `is_deleted_user_user_user_user_agent` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user user user agent',
      `is_deleted_user_user_user_user_ip` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user user user ip',
      `is_deleted_user_user_user_user_browser` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '删除user user user user browser',
      `is_deleted_user_user_user_user_os` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '
