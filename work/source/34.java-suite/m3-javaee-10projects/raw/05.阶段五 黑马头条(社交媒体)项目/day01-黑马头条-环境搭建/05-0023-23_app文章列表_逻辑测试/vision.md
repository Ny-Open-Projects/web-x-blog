# 画面线理解：23_app文章列表_逻辑测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\23_app文章列表_逻辑测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:55, 01:49, 02:25, 03:14, 03:58, 04:43, 05:24, 06:14, 06:57, 07:51, 08:27, 09:12, 09:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:40:46

1) 这一组画面整体在讲什么（一句话）：
演示如何通过单元测试驱动开发，验证文章服务加载逻辑，包括SQL动态条件构建、分页处理和数据库查询结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDE中ArticleTest.java文件，准备编写测试用例，鼠标悬停在@Autowired注解上，提示其作用。
画面2：在ArticleTest.java中，定义了测试类，使用@SpringBootTest和@RunWith注解，准备测试AppArticleService。
画面3：在测试方法中调用appArticleService.load方法，传入null参数和LOADTYPE_LOAD_MORE常量，IDE提示“Expression expected”。
画面4：运行测试，控制台输出Hibernate初始化日志，显示连接池已添加连接，但提示“hibernate.properties not found”。
画面5：测试运行中，控制台输出Spring Boot初始化日志，包括RepositoryConfigurationDelegate的注册信息。
画面6：进入调试模式，查看AppArticleServiceImpl中的load方法，变量dto的size被设置为20。
画面7：调试器中显示dto对象的属性，包括size=20，tag=null，其他字段如provincId、child等为null。
画面8：在测试方法中，IDE提示“Press Ctrl+空格 to choose the selected for first suggestion...”，准备输入代码。
画面9：在测试方法中，创建ApUser对象并设置其id为2104，调用AppThreadLocalUtils.setUser()设置当前用户。
画面10：运行测试，控制台输出Spring Boot启动日志，显示“Started ArticleTest in 10.319 seconds”。
画面11：切换到Navicat，查看数据库表ap_user_article_list，显示一条记录，其中user_id=2104，channel_id=10120。
画面12：在AppArticleMapper.xml中，展示SQL语句，包含动态条件判断和分页限制。
画面13：在AppArticleServiceImpl中，展示getArticleList方法的逻辑，根据用户是否存在返回不同结果。
画面14：运行测试，控制台输出测试通过的日志，显示“Tests passed: 1”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<select id="loadArticleListByUser" resultMap="BaseResultMap">
    select * from ap_user_article_list
    where
        user_id = #{user.id} and is_show = 0 and is_read = 0
    <if test="type != null and type == 1">
        and recommend_time <![CDATA[>]]> #{dto.minShowTime}
    </if>
    <if test="type != null and type == 2">
        and recommend_time <![CDATA[<]]> #{dto.maxShowTime}
    </if>
    <if test="dto.tag == '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag != '_all'">
        and channel_id = #{dto.tag}
    </if>
    <if test="dto.tag
