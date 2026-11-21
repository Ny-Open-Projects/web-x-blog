# 19_app文章详情_关注接口_关注操作_mapper接口编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\19_app文章详情_关注接口_关注操作_mapper接口编写【海量资源尽在 666java.com】.mp4
- 时长 9分38秒（音频 578s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去完成第二块业务就是当用户的关注和取消关注的这个操作首先呢咱们还是去完成当前的mypro文件啊这个mypro呢一共是分了四块啊分了四块咱们一块来去根据当前的文档啊讲一样咱们再去拷贝一下啊行那首先第一块内容呢就是当前的一个这种user flow啊这mypro啊这个mypro呢其实咱们之前已经创建完了
[00:27] 咱们之前在上一个节目做的时候是一个查询的操作啊然后现在现在呢咱们要去做一个新增和一个删除所以说咱们在当前这个mypro文件中去找到啊找到完之后呢咱们再去添加两个方法来打开当前的modelmodel里边啊找到mypro4打开app然后是哪个是不是找一找啊叫userflow他
[00:56] 在这去下面加一个东西就加这两个东西就可以了当然了加的时候你要注意一下这个你需要去加一个什么这个pairing是吧你们在这加上省得后面再去报错然后把这个拷贝一下我把这两个也加上一个参数无所谓一个参数就不用加了一个参数的话它本身就是能找到然后这是user id这是float id好没问题
[01:27] 说到这呢咱们刚才那个接口好像是也没有加是吧咱们再来看一下就是它这只有一个参数是吧那咱们就不用加了行那这个加完之后呢咱们现在呢需要去创建当前的一个mypro文件把这个mypro文件也创建出来来这个mypro文件已经有了是吧有的话咱们只需要从这去拷贝就是把一个保存一个删除就可以了这块内容呢它是有关注关注就是保存取消就是删除所以说有一个
[01:56] 保存和有一个删除打开当前的AP然后APP里边有一个叫做userflowapp然后是打开它OK在这之后就算是做完了完了做完之后咱们再来看第二个这个接口这个当前的map做完了然后下面还有一个粉丝是吧再往下看下面咱们的粉丝粉丝的话其实一样粉丝的话他也有保存和删除的操作对吧
[02:22] 所以说咱们在这再去把它给拷贝一下当然这里边还有一个插群插群什么时候用插群的话其实咱们要我现在要去查一下看看有没有数据有数据的话咱们就不再去进行保存了没有数据再进行保存是这么个情况这么个思路所以说咱们在这再去创建一个MIPL接口还是这个APP下边直接拷贝就可以了做完之后还是团套路在这去加上
[02:52] 好上完之后呢这是然后拷贝就直接拷贝完了啊然后拷贝完之后咱们改一改好一共是这几个然后这是user id好拷过来这是fans id好fans id还有是user id好burst没了啊那这个咱们就算是做完了啊做完之后咱们下面就来去创建当前的一个mypro应售店啊然后在这去右键啊不用右键直接拷贝一个吧好吧
[03:29] 叫啥呢叫apuserfan是吧userfan好mypro删掉完之后呢咱们在这内容删掉啊删掉完之后呢咱们在这去拷贝过来往下走这个内容比较多一些啊因为它是有三个方法啊一个是删除一个是新增一个是查询好拷贝过来之后呢咱们再来说一下啊拷贝过来之后啊拷贝过来之后这个好像报错了是吧
[03:59] 不过没有问题啊咱们主要是来去检查一下当前到底对不对啊当前这个东西好像不对是吧所以说咱们在这啊去改一下User Fun好然后把后边删了好那这样其实就没事了啊首先呢是当前的一个这种映射是自转的映射然后下面呢是有一个查询啊有个查询
[04:22] 这个查询的时候是加一个Boss大家要一段注意然后下面还有一个删除根据当前的这种组件去删除用户ID和Face ID去删除然后下面还有一个新增新增的话就没啥可说的就是把这个字段做一个Insert就可以了行这个其实也做完了就是当前的咱们第二个表也做完了还有一个表是吧你们再往下看是有一个AP User这个只是一个查询咱们这个之前没有创建过咱们再去创建当前的MyPool接口
[04:52] 好考到这考到这之后呢这个不用加那个那个诸解啊因为咱们需要去只有一个参数啊所以说咱们不需要去加诸解了再拷贝一个吧然后这是叫什么AP user mypro是吧然后把这个内容呢删掉删完之后呢这稍微改一改啊叫AP user mypro啊不对这不是fun啊是myuser加上之后呢咱们再从这去订一下就可以了用这里边呢只有一个
[05:24] 不是只是一个查询好 站过来之后你看啊目前的这个呢还是映射是吧是一个circle片段然后下面是一个查询根据主件去查询就可以了好吧行 那这个加完之后呢看看还有没有啊咱们目前的话就算是做完了啊那最后一个呢最后一个作者信息呢其实咱们在上一个节目里边已经做完了就是根据当前的作者ID去查询作者的信息这个已经做完了啊下面咱们就来去完成当前的这个业务
[05:57] 这个业务就是当前的这么一段逻辑首先咱们还要再去创建Service创建Service这个Service怎么创建的来看一看首先咱们要去创建哪个Service就是第二个Service这个Service咱们已经创建完了咱们看第二个Service就当前这个这儿咱们需要去创建一个这样的接口这样接口好在这创建当前优色模块下创建右键然后是一个类是吧它这个接口放到这儿它是一个
[06:28] App user relation就是用户的关系的什么Service然后呢这个接口是吧然后这个方法这个方法呢主要呢就是进行咱们的一个什么不关注的一个操作啊所以说咱们在这直接叫float就可以了public response without然后是float参数是啥呢参数是不是就是咱们之前那个叫什么user relation took啊写上
[06:59] user-relation-go-to那这个创建完之后呢咱们下面就来去创建它的实现类是吧好它的实现类咱们在这写下在这写个注释也行注释是用户的关注什么取消然后下面咱们去创建这个实现类这个实现类拷贝一下它这就创建一个类就是它加上mpl
[07:32] 然后是实现当前的这个那这个呢咱们就在这去加一个Service诸解啊这个千万别忘了行那这个咱们下面就来去设置啊那这个逻辑是啥呢那这个逻辑是啥这个逻辑的还是咱们看当前咱们之前写的东西啊首先的咱们要去获取到当前的float id啊在这写下首先第一个获取到float id
[08:06] ID,Float ID,这Float ID其实就是当前你关注的用户的ID当前关注用户的ID然后第二步要去判断当前是否当前用户是否已经关注了已经关注了下面咱们就去说两个东西一个是关注,没关注吧就是关注,关注操作一个是什么
[08:38] 取消关注关注操作的话咱们在怎么做呀这儿去怎么做呀这是不是有保存的保存哪个一个是APAPAPUser还有什么APUser这是一个取消关注的话其实咱们这一块是只需要去
[09:13] 删除啊删除这两个就可以了删除这两条数据就可以了这个里边其实还加一个东西是吧还需要干嘛呢还需要去调用什么保存关注的行为这个呢其实就是咱们的一个整体思路啊行那咱们下面呢一会儿就去来完成当前的这个代码

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

