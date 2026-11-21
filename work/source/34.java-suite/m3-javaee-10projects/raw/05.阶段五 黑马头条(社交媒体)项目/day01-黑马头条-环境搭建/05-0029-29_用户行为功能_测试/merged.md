# 29_用户行为功能_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\29_用户行为功能_测试【海量资源尽在 666java.com】.mp4
- 时长 6分51秒（音频 411s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那到目前为止呢咱们把单本呢都已经写完了咱们下面呢就来去测试一下那测试之前呢咱们还要再改两处东西第一个呢咱们在这得需要把当前的mycircle给加载进来所以说咱们在这再加一个配置类叫mycircle的config同时呢这里边也有配置类里边也有mylist的一些组合所以说咱们要在这去一定要加这些东西要不然的话你可能跑不到数据库
[00:29] 这块首先是一个complication然后是扫描扫描谁呢扫描common包下边的一个东西是吧是com.kma然后是commonmycircle核心那这样的话咱们就算是完了啊这样之后啊咱们这还要再改另外一个东西那改哪个呢就是改保存这一块保存这块是这样啊因为咱们在目前这个表呢这个ID啊并不是自增
[00:59] 如果说你要是不给这个表去设置ID的话它有可能保存的时候会报错那这个其实不用担心咱们到明天呢会去集成买KIT到时候呢买KIT呢会帮着咱们去把这个ID给生成了或者逐渐给生成了目前的话还不行所以说今天呢咱们就暂时先写死那写死的话很容易是吧给个ID然后的话咱们就直接给个值就可以了我就直接还给当前这个intradit付两次就可以了
[01:28] 第一个呢就是ID复制第二个是才开始给空吹ID复制好吧嗯行那这个咱们改完之后咱们就来去写一段测试代码来去测一测啊来创建一个测试类靠谱点黑码是吧have test什么behave test好吧然后呢怎么办呢是加一个诸解叫什么诸解叫Spring Boot test然后是assist哪个呢叫behave
[02:05] 把当前的引导类给加进来好第二个是runways然后serverender.classok那这样环境算是完成完了下面咱们就来去测试void然后是testsave好吧测试之前咱们需要把当前的Service给注入进来哪个ap-type咱们试一下我看看它是吧就它
[02:40] 好 带进来之后呢咱们下面呢就可以进行保存对吧点savesave里边咱们需要去来一个show-dto对吧创建一个呗show-dto等于new一个那设完之后啊咱们在这啊简单说一说啊那要测试的话大家要注意啊前的话呢咱们表中啊没有设备ID是吧咱们可以打开看一下嗯这个
[03:16] 我在这呢是手动去加了一条并且呢你看type是1那1的意思就是用户ID所以说我这entry ID是当前的某一个用户所以说呢咱们在这测试之前呢应该是往当前的现成中去加一条什么呢加一个用户可以说什么呢jp user user等于什么user然后是给一个给个IDID的话就是1OK啊这是已经固定好了就是1你想要测试成功的话
[03:47] 这些东西需要你的保证保持一致好吧那行那这个咱们就用当前的threadlocalutils.setuser把当前的user放进去好吧那这里边咱们还需要去设置一些参数这里边设置哪些参数呢来看一看这部ID咱们不用设置了因为咱们用通货ID也行然后下面咱们主要是用主要是设置当前的article ID那这个是一个文章并且是个列表所以说咱们要
[04:17] 创建的话怎么创建呢这个就很容易了啊比如说咱们先放到这啊比如说咱们先去创建一个list里边是 run的article一批article啊好list就等于什么呢relist好呃就创建完之后呢咱们再去创建一个一批article等于new一个一批article好这个这个叫什么来着
[04:55] 前的Tico的ID咱们也设置一个setID的话你随便设好吧叫200然后你把当前这个去装到这个集合里边是吧.addArticle完了最终再把这个集合装到DTO中所以说什么DTO.setArticleIDs就是当前的list那这样的话
[05:24] 我们就算是设置完了啊行那咱们就来测一下啊不说有问题的话咱们再调试好吧稍等看看有没有错误啊有错误咱们就调一下没有错误能保存没有错误必须是能够在这去保存一条数据才行啊当前的这当前这保存保存的数据行好像是报错了是吧来看一眼啊说这是一个A.TYPE这好像写错了是吧写错的话咱们就改一改啊
[06:07] 当前的这个里边这写错了是吧叫什么gype然后这个呢也是gype这个我们就完了咱们再测看看还有没有错误它保存成功之后应该是在这给我保存一条数据这样才算成功好成功了是吧成功之后呢咱们来去刷新一下看这个数据是不是有了当前的ID有了entry ID是1没问题然后下面是一个
[06:43] 200是不是也没问题啊那到目前的话咱们这个整个测试呢就都已经做完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

  import com.heima.behavior.Service.AppShowBehaviorService;
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

