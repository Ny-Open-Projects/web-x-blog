# 画面线理解：19_app文章详情_关注接口_关注操作_mapper接口编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\19_app文章详情_关注接口_关注操作_mapper接口编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:55, 01:50, 02:23, 03:29, 03:52, 04:21, 04:45, 05:12, 05:35, 06:07, 06:46, 07:29, 07:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:19:17

1) 这一组画面整体在讲什么（一句话）：
实现用户关注与取消关注功能，包括数据表设计、Mapper接口与XML映射文件、Service层接口与实现类的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了关注与取消关注功能的业务逻辑说明。
- 代码结构：UserRelationDto、ap_user_follow、ap_user_fan、ap_user、ap_author 表结构。
- 业务逻辑：
  1. 通过dto中的userId去获取关注人的id。如果没有userId可以通过当前的作者id去查询，作者的app账号信息 followId。
  2. 判断用户是否是关注或者取消。
  3. 关注：先去ap_user_follow表，检查是否已经关注。如果没关注，再进行保存。
  4. 取消关注：删除数据 ap_user_follow、ap_user_fan。

画面2：
- 展示了项目结构，选中了 ApFollowBehaviorMapper 接口文件。

画面3：
- 展示了项目结构，选中了 ApFollowBehaviorMapper 接口文件。

画面4：
- 展示了 UserRelationDto 的类定义，包含 authorId、userId、articleId、operation 等字段。
- 业务逻辑说明：通过dto中的userId去获取关注人的id。如果没有userId可以通过当前的作者id去查询，作者的app账号信息 followId。判断用户是否是关注或者取消。关注：先去ap_user_follow表，检查是否已经关注。如果没关注，再进行保存。取消关注：删除数据 ap_user_follow、ap_user_fan。

画面5：
- 展示了复制文件的对话框，准备将 ApFollowBehaviorMapper.xml 文件复制到指定目录。

画面6：
- 展示了 ApUserFan 表的 SQL 语句，包括 select、delete、insert 语句。

画面7：
- 展示了 ApUserFan 表的 SQL 语句，包括 select、delete、insert 语句。

画面8：
- 展示了 ApUser 类的定义，包含 id、salt、name、password、phone、image、sex、isCertification、identityAuthentication、status、flag 等字段。

画面9：
- 展示了 ApUserMapper.xml 文件的开头部分，包含 XML 版本、DTD 公共标识和命名空间。

画面10：
- 展示了 ApUserMapper.xml 文件中的 resultMap 和 select 语句，用于查询用户信息。

画面11：
- 展示了 AppFollowBehaviorService 接口的定义，包含 saveFollowBehavior 方法。

画面12：
- 展示了项目结构，选中了 AppUserRelationService 接口文件。

画面13：
- 展示了 AppUserRelationService 接口的定义，包含 follow 方法。

画面14：
- 展示了 AppUserRelationServiceImpl 类的实现，包含 follow 方法的实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
Integer followId,
UserRelationDto
// 文章作者id
@IdEncrypt
Integer authorId;
// 用户id
@IdEncrypt
Integer userId;
// 文章
@IdEncrypt
Integer articleId;
// 操作方式
// 0 关注
```
```text
1. 通过dto中的userId去获取关注人的id.如果没有userId可以通过当前的作者id去查询，作者的app账号信息 followId
2. 判断用户是否是关注或者取消
3. 关注
先去ap_user_follow表，检查是否已经关注
如果没关注，再进行保存
4. 取消关注
删除数据
ap_user_follow
ap_user_fan
```

画面2：
```java
package com.heima.model.mappers.app;
import com.heima.model.user.pojos.ApUserFollow;
import org.apache.ibatis.annotations.Param;
public interface ApUserFollowMapper {
    String selectById(@Param("burst") String burst, @Param("userId") long userId, @Param("fansId") long fansId);
}
```

画面3：
```java
package com.heima.model.mappers.app;
import com.heima.model.behavior.pojos.ApFollowBehavior;
public interface ApFollowBehaviorMapper {
    int insert(ApFollowBehavior record);
}
```

画面4：
```java
public class UserRelationDto {
    // 文章作者id
    @IdEncrypt
    Integer authorId;
    // 用户id
    @IdEncrypt
    Integer userId;
    // 文章
    @IdEncrypt
    Integer articleId;
    // 操作方式
    // 0 关注
    private Integer operation;
    private String followName;
    private Integer level;
    private Integer isNotice;
    private Date createdTime;
    private Boolean isShieldLetter;
    private Boolean isShieldComment;
    private String burst;
}
```
```text
1. 通过dto中的userId去获取关注人的id。如果没有userId可以通过当前的作者id去查询，作者的app账号信息 followId
2. 判断用户是否是关注或者取消
3. 关注
先去ap_user_follow表，检查是否已经关注
如果没关注，再进行保存
4. 取消关注
删除数据
ap_user_follow
ap_user_fan
```

画面5：
```text
Copy file D:\heima_leadnews\_resources\mappers\app\ApFollowBehaviorMapper.xml
New name: ApFollowBehaviorMapper.xml
To directory: d:\heima_leadnews\heima_leadnews-model\src\main\resources\mappers\app
Use Ctrl+空格 for path completion
```

画面6：
```xml
<resultMap id="Base_Column_List" type="com.heima.model.user.pojos.ApUserFan">
    <id column="id" property="id"/>
    <result column="user_id" property="userId"/>
    <result column="fans_id" property="fansId"/>
    <result column="level" property="level"/>
    <result column="created_time" property="createdTime"/>
    <result column="is_display" property="isDisplay"/>
    <result column="is_shield_letter" property="isShieldLetter"/>
    <result column="is_shield_comment" property="isShieldComment"/>
    <result column="burst" property="burst"/>
</resultMap>
<select id="selectById" resultType="Base_Column_List">
    select id, user_id, fans_id, level, created_time, is_display, is_shield_letter, is_shield_comment, burst from ap_user_fan where user_id = #{userId} and fans_id = #{fansId}
</select>
<delete id="deleteByFansId">
    <foreach collection="list" item="item" separator="union all">
        delete from ap_user_fan where user_id = #{userId} and fans_id = #{item}
    </foreach>
</delete>
<insert id="insert" parameterType="com.heima.model.user.pojos.ApUserFan">
    insert into ap_user_fan (id, user_id, fans_id, level, created_time, is_display, is_shield_letter, is_shield_comment, burst)
    values (#{id}, #{userId}, #{fansId}, #{level}, #{createdTime}, #{isDisplay}, #{isShieldLetter}, #{isShieldComment}, #{burst})
</insert>
```

画面7：
```xml
<resultMap id="Base_Column_List" type="com.heima.model.user.pojos.ApUserFan">
    <id column="id" property="id"/>
    <result column="user_id" property="userId"/>
    <result column="fans_id" property="fansId"/>
    <result column="level" property="level"/>
    <result column="created_time" property="createdTime"/>
    <result column="is_display" property="isDisplay"/>
    <result column="is_shield_letter" property="isShieldLetter"/>
    <result column="is_shield_comment" property="isShieldComment"/>
    <result column="burst" property="burst"/>
</resultMap>
<select id="selectById" resultMap="BaseResultMap">
    select <include refid="Base_Column_List"/> from ap_user_fan where user_id = #{userId} and fans_id = #{fansId}
</select>
<delete id="deleteByFansId">
    <foreach collection="list" item="item" separator="union all">
        delete from ap_user_fan where user_id = #{userId} and fans_id = #{item}
    </foreach>
</delete>
<insert id="insert" parameterType="com.heima.model.user.pojos.ApUserFan">
    insert into ap_user_fan (id, user_id, fans_id, level, created_time, is_display, is_shield_letter, is_shield_comment, burst)
    values (#{id}, #{userId}, #{fansId}, #{level}, #{createdTime}, #{isDisplay}, #{isShieldLetter}, #{isShieldComment}, #{burst})
</insert>
```

画面8：
```java
@Data
public class ApUser {
    private Long id;
    private String salt;
    private String name;
    private String password;
    private String phone;
    private String image;
    private String sex;
    private Boolean isCertification;
    private Boolean identityAuthentication;
    private Boolean status;
    private String flag;
}
```

画面9：
```xml
<?xml version="1.0
