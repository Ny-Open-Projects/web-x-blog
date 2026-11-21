# 画面线理解：23_mycat路由开发_算法测试_增删改查解决方案

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\23_mycat路由开发_算法测试_增删改查解决方案【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:55, 02:01, 03:11, 04:36, 04:44, 04:52, 05:05, 05:29, 05:46, 05:51, 05:57, 06:03, 06:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:03:58

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 MyBatis 中通过自定义 SQL 和工具类解决数据查询和插入时因 burst 字段无法直接拼接导致的逻辑问题，并演示了相关测试用例的执行过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Mapper.xml 中的 insert 语句，用于插入数据，其中包含对 burst 字段的处理逻辑。
画面2：展示 BurstUtils 类中的 calculate 方法，用于计算数据分组，其中包含对 columnValue 的处理逻辑。
画面3：展示解决数据查询问题的方案，包括将 burst 字段默认设为 0，以及通过 MyBatis 注解方式处理 SQL。
画面4：展示 MyBatis 中的 select 语句，用于查询数据，其中包含对 burst 字段的处理逻辑。
画面5：展示项目结构，包括 heima-leadnews-utils 模块中的 BurstUtils.java 文件。
画面6：展示项目结构，包括 heima-leadnews-behavior 模块中的 BehaviorTest.java 文件。
画面7：展示 ApShowBehaviorMapper.xml 中的 select 和 insert 语句，用于查询和插入数据。
画面8：展示 ap_show_behavior 表的 insert 语句，用于插入数据。
画面9：展示 BehaviorTest.java 中的 testSave 方法，用于测试数据插入。
画面10：展示测试用例执行日志，显示测试通过。
画面11：展示测试用例执行日志，显示 HikariPool-1 连接池初始化成功。
画面12：展示测试用例执行日志，显示 HikariPool-1 连接池清理状态。
画面13：展示测试用例执行日志，显示测试通过。
画面14：展示 ApShowBehaviorMapper.xml 中的 select 和 insert 语句，用于查询和插入数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<insert id="insert"
        parameterType="com.heima.article.mysql.core.pojos.app.ApLikesBehavior">
    INSERT INTO ap_likes_behavior (id, behavior_entry_id, entry_id, type, operation,
    created_time, burst)
    VALUES (#(id), #(behaviorEntryId), #(entryId), #(type), #(operation),
    #(createdTime), #(burst))
</insert>
```

画面2：
```java
public void init() {
    // ...
    public Integer calculate(String columnValue) {
        if (columnValue == null) {
            String[] temp = columnValue.split(":");
            if (temp.length == 2) {
                try {
                    Long dataId = Long.valueOf(temp[0]);
                    Long burstId = Long.valueOf(temp[1]);
                    int group = -(int)(dataId / volume); step
                    int pos = group + (int)(burstId / num);
                    return pos;
                } catch (Exception e) {
                    System.out.println("HEIMA RULE INFO [" + e.getMessage() + "]");
                }
            }
            return 0;
        }
    }
}
```

画面3：
```xml
<select id="selectLastLike" resultMap="baseResultMap">
    <if test="burst != null and burst != ''">
        select * from ap_likes_behavior where behavior_entry_id = #{behaviorEntryId} and entry_id = #{entryId} and type = #{type} order by created_time desc limit 1
    </if>
</select>
```

画面4：
```xml
<select id="selectLastLike" resultMap="baseResultMap">
    <if test="burst != null and burst != ''">
        select * from ap_likes_behavior where behavior_entry_id = #{behaviorEntryId} and entry_id = #{entryId} and type = #{type} order by created_time desc limit 1
    </if>
</select>
```

画面5：
```java
public static String groupOne(Object... fields) {
    StringBuffer sb = new StringBuffer();
    if (fields == null || fields.length == 0) {
        sb.append("0");
    } else {
        for (int i = 0; i < fields.length; i++) {
            sb.append(SPLIT_CHAR).append(fields[i]);
        }
    }
    return sb.toString();
}
```

画面6：
```java
public class BehaviorTest {
    // ...
}
```

画面7：
```xml
<select id="selectShowBehavior" resultType="com.heima.behavior.model.ApShowBehavior">
    <include refid="Base_Column_List"/>
    <foreach collection="articleIds" item="item" separator=",">
        from ap_show_behavior where entry_id = #{entryId} and article_id in
        #{item}
    </foreach>
</select>

<insert id="saveShowBehavior" parameterType="java.util.List">
    <include refid="Base_Column_List"/>
    insert into ap_show_behavior (entry_id, article_id, is_click, show_time, created_time)
    values
    <foreach item="item" collection="articleIds" separator=",">
        #{item}, #{item}, 0, now(), now()
    </foreach>
</insert>
```

画面8：
```xml
<insert id="saveBehaviors">
    <if test="burst != null and burst != ''">
        insert into ap_show_behavior (entry_id, article_id, is_click, show_time, created_time)
        values
        <foreach item="item" collection="articleIds" separator=",">
            #{item}, #{item}, 0, now(), now()
        </foreach>
    </if>
</insert>
```

画面9：
```java
@Test
public void testSave() {
    ApUser user = new ApUser();
    user.setUid(1);
    AppliedDocsUtils.setDb(user);
    ShowBehaviorDto dto = new ShowBehaviorDto();
    ApArticle apArticle = new ApArticle();
    apArticle.setId(10130);
    dto.setArticleIds(List.of(apArticle));
    appShowBehaviorService.saveShowBehavior(dto);
}
```

画面10：
```log
2019-09-16 10:29:46,133 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logStarting | Running with Spring Boot v2.1.3.RELEASE, Spring v5.1.7.RELEASE
2019-09-16 10:29:47,153 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logImplementation | Logging initialized using 'class org.springframework.boot.logging.logback.LogbackLoggingSystem'
2019-09-16 10:29:48,137 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logImplementation | Logging initialized using 'class org.springframework.boot.logging.logback.LogbackLoggingSystem'
2019-09-16 10:29:49,137 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logImplementation | Logging initialized using 'class org.springframework.boot.logging.logback.LogbackLoggingSystem'
2019-09-16 10:29:50,137 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logImplementation | Logging initialized using 'class org.springframework.boot.logging.logback.LogbackLoggingSystem'
2019-09-16 10:29:51,137 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logImplementation | Logging initialized using 'class org.springframework.boot.logging.logback.LogbackLoggingSystem'
2019-09-16 10:29:52,137 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logImplementation | Logging initialized using 'class org.springframework.boot.logging.logback.LogbackLoggingSystem'
2019-09-16 10:29:53,137 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logImplementation | Logging initialized using 'class org.springframework.boot.logging.logback.LogbackLoggingSystem'
2019-09-16 10:29:54,137 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logImplementation | Logging initialized using 'class org.springframework.boot.logging.logback.LogbackLoggingSystem'
2019-09-16 10:29:55,137 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logImplementation | Logging initialized using 'class org.springframework.boot.logging.logback.LogbackLoggingSystem'
2019-09-16 10:29:56,137 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logImplementation | Logging initialized using 'class org.springframework.boot.logging.logback.LogbackLoggingSystem'
2019-09-16 10:29:57,137 [DEBUG] main | com.heima.behavior.test.BehaviorTest | logImplementation | Logging initialized using 'class org.springframework.boot.logging.logback.LogbackLoggingSystem'
2019-09-16 10:29:58,137 [DEBUG] main
