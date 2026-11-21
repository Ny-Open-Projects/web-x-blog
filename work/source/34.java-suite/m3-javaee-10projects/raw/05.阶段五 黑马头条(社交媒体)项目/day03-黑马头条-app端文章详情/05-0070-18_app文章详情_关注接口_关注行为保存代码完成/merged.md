# 18_app文章详情_关注接口_关注行为保存代码完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\18_app文章详情_关注接口_关注行为保存代码完成【海量资源尽在 666java.com】.mp4
- 时长 8分34秒（音频 515s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下讲下面呢咱们就首先来去完成第一个就是当前保存关注的行为啊就是保存关注行为那这个呢咱们需要去涉及到两张表第一个呢咱们要先去查询行为实体那这一步呢其实咱们之前已经做过了啊然后第二个呢就是咱们需要去保存当前的这种关注的行为首先呢咱们还是老套路啊首先还是要去创建咱们的MAP啊这MAP啊
[00:28] 这个Map的话咱们还是从当前的笔记中拷贝一下去创建当前的一个这种APflow的BecoverMap然后到哪呢还是到咱们的modo中把它给关一下打开modo然后这有一个Mapos是吧APP还是APP拷贝一下它里边就只有一个Insert这时候咱们需要去在这去创建一个什么呢创建一个映射文件
[01:01] 这个就叫做啥呢上面名称保持一致啊load比cover好ok之后呢咱们再去把它给删掉啊因为咱们现在呢是不一样了是吧ap叫什么来着load比cover是吧叫它啊行那下面咱们需要去设一些映射加一个保存是吧很简单啊我们在这直接去考过来
[01:34] 跑不来之后咱们简单说一下你看这个就是AP flood behavior是吧这是映射ok没问题然后下面是一个搜索编段然后搜索编段好像目前用不着没有问题有后面用到的时候咱们再说然后下面它这一份是一个保存的操作保存保存的话目前的话就只非常简单就只有这4个就可以了好吧然后这时候咱们就可以写当前的第1个Service就是首先要获取当前的一个行为尸体然后再去植
[02:04] 执行真正的保存这时候咱们要去创建一个Service这个Service咱们统一都在当前的用户某块去创建就可以了在这其实这个uservice包怎么就创建完了在这去创建一个什么创建一个这种叫appapp叫codecoverservice好吧那它是一个接口它是一个接口
[02:35] 然后这里边有什么方法呢其实方法就只有一个指示啥呢存储关注行为数据是吧然后在这去加public其实写不写public无所谓是吧然后最终是responds without然后咱们要saveflow的flow然后是cover完了这个参数是啥呢这个参数看来因为咱们也说了这个参数的话其实就是当前的
[03:09] 然后是behind DTO是吧所以说咱们把这个参数给加加上啊开玩笑啊他叫做DTO好了啊这时候咱们要再去写他的一个实现类是吧好把这个实现类写下m.2就是当前的APPAppload Service im好吧拿下啊嗯没错是吧
[03:44] 没错点OK这时候让他去实现当前的接口然后是Ctrl-A一下这时候把这个方法重写然后是加一个Service好了这时候算是创建完了之后咱们就去实现一下那里边该去怎么去做其实这个咱们之前刚才已经说完这个思路了这个思路的话首先咱们要去干嘛要去先去把这个行为尸体查出来是吧行咱们就写下查明行为尸体就是首先你要获取到用户是吧
[04:15] 用户还是一样app-slide-local.youtube.user.就能拿到当前的用户然后咱们要去判断这个就是当前用户它等于空吧等于空判断什么呢cto.getIncrement ID就说设备ID也等于空说错了等于none
[04:45] 不等于乱的话我们就直接return一个参数错误参数缺少参数就可以了respawns without第二error without然后是apph是吧这有一个参数的憋尸我看是哪个啊就它是吧好就它啊这个呢其实就是当前的什么东西你看这不是就是缺少参数啊没问题啊然后再往下看啊然后这个说了完之后呢如果说都没问题咱们就可以去查了啊查之前呢咱们还是老套路
[05:16] 我现在在这去加一个user id等于呢是吧其实这个代码咱们完全可以从之前的考过来啊那当前的用户啊说用户不等于空不等于空啊然后呢咱们就可以去user iduser id啊等下呢user.id好吧然后我们再去查询查询的话首先你要去注入一个东西过来注哪个注入当前的一个行为实体是吧
[05:46] 什么APBehaviourEntryMapper然后是把Mapper注入进来之后呢咱们写一个然后把它呢查询查询只有一个一个呢就是当前的什么userID那就是userID然后第二个是dto.incrementID是吧就是当前的设备ID好他就能去查到一个行为实体如果说这个行为实体还是不行
[06:17] 它还是空的话也是不行是吧等一等一让我们还是再去返回这个东西说你的参数还是有问题是吧应该是参数非法参数非法是哪个二是第二个无效参数好吧那这个设置完之后呢咱们下面呢就来去做保存了如果说现在这个行为尸体我都没问题都能找着那这时候咱们就进行保存操作保存行为操作
[06:49] 这时候咱们去创建一个AP-behind-get-id
[07:15] 然后再往下,ALB,是什么set article id,是吧就是BTO.article id,因为这个是从前台传过来的啊然后还有什么ALB,是什么set当前的一个float id这个float id其实也传过来了,是吧,而float id,完事最后一个是ALB,是讲什么set,是不是有一个name啊time啊,时间,又一个date呗好,那这样的话其实就完了啊
[07:44] 那设置完之后呢咱们就可以进行保存了那保存的时候呢咱们还要再去注入另外一个mypro 再加入再加一个private什么来着apfloat然后是behaviourmypro然后是他注入吧注入完之后呢咱们在这啊就可以去保存了啊而insert就是alb好它返回一个东西insert它是
[08:15] 影响的行处是影响的还是一个印的这时候你可以返回了返回一个responseresult.ok就把当前那个insert跑进去说insert返回就可以了钱的话这个东西咱们就算是做完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何实现用户关注行为的持久化，包括定义DTO、Mapper接口与SQL、Service层的业务逻辑实现。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了FollowBehaviorDto类的定义，包含equipmentId、articleId、followId等字段，并附有红色手写注释说明根据equipmentId或userId查询行为实体、保存关注行为。
画面2: 展示了UserRelationDto类的定义，包含authorId、userId、articleId等字段。
画面3: 展示了创建ApFollowBehaviorMapper接口和对应的ApFollowBehaviorMapper.xml映射文件的步骤。
画面4: 展示了ApFollowBehaviorMapper.xml中的SQL映射配置，定义了BaseResultMap和insert语句。
画面5: 展示了AppFollowBehaviorService接口的定义。
画面6: 展示了AppFollowBehaviorServiceImpl类的初始骨架。
画面7: 展示了AppFollowBehaviorServiceImpl中对user和equipmentId进行非空校验的代码。
画面8: 展示了IDE中自动补全的User对象属性，用于获取userId。
画面9: 展示了通过ApBehaviorEntryMapper查询行为实体的代码，并提示需要注入该Mapper。
画面10: 展示了根据查询结果判断是否为空并返回错误码的代码。
画面11: 展示了创建ApFollowBehavior对象并设置其属性的代码。
画面12: 展示了为ApFollowBehavior对象设置articleId和followId属性的代码。
画面13: 展示了为ApFollowBehavior对象设置createdTime属性的代码。
画面14: 展示了调用ApFollowBehaviorMapper的insert方法保存数据并返回结果的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
public class FollowBehaviorDto {
    //设备id
    @IdEncrypt
    Integer equipmentId;
    //文章id
    @IdEncrypt
    Integer articleId;
    @IdEncrypt
    Integer followId,
}
```
画面2:
```java
public class UserRelationDto {
    //文章作者id
    @IdEncrypt
    Integer authorId;
    //用户
    @IdEncrypt
    Integer userId;
    //文章
    @IdEncrypt
    Integer articleId;
}
```
画面3:
```java
创建接口ApFollowBehaviorMapper {
    int insert(ApFollowBehavior record);
}
```
画面4:
```xml
<Mapper namespace="com.heima.model.mappers.app.ApFollowBehaviorMapper">
    <resultMap id="BaseResultMap" type="com.heima.model.behavior.pojos.ApFollowBehavior">
        <id column="id" property="id" />
        <result column="entry_id" property="articleId"/>
        <result column="follow_id" property="followId"/>
        <result column="created_time" property="createdTime"/>
    </resultMap>
    <sql id="Base_Column_List">
        id, entry_id, article_id, follow_id, created_time
    </sql>
    <insert id="insert" parameterType="com.heima.model.behavior.pojos.ApFollowBehavior">
        insert into ap_follow_behavior (entry_id, article_id, follow_id, created_time)
        values
        (#entryId, #articleId, #followId, #createdTime)
    </insert>
</Mapper>
```
画面5:
```java
package com.heima.user.Service;
import com.heima.model.common.dtos.ResponseResult;
public interface AppFollowBehaviorService {
    //存储关注行为数据
    public ResponseResult saveFollowBehavior();
}
```
画面6:
```java
package com.heima.user.Service.impl;
import com.heima.model.behavior.dtos.FollowBehaviorDto;
import com.heima.model.common.dtos.ResponseResult;
import com.heima.model.user.pojos.ApUser;
import com.heima.user.Service.AppFollowBehaviorService;
import org.springframework.stereotype.Service;
@Service
public class AppFollowBehaviorServiceImpl implements AppFollowBehaviorService {
    @Override
    public ResponseResult saveFollowBehavior(FollowBehaviorDto dto) {
        return null;
    }
}
```
画面7:
```java
public ResponseResult saveFollowBehavior(FollowBehaviorDto dto) {
    ApUser user = AppThreadLocalUtils.getUser();
    if (user == null && dto.getEquipmentId() == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
    }
    return null;
}
```
画面8:
```java
ApUser user = AppThreadLocalUtils.getUser();
Long userId = user.getId();
```
画面9:
```java
ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectByUserIdAndEquipmentId(userId, dto.getEquipmentId());
if (apBehaviorEntry == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```
画面10:
```java
if (apBehaviorEntry == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```
画面11:
```java
ApFollowBehavior alb = new ApFollowBehavior();
```
画面12:
```java
alb.setArticleId(dto.getArticleId());
alb.setFollowId(dto.getFollowId());
```
画面13:
```java
alb.setCreatedTime(new Date());
```
画面14:
```java
int insert = apFollowBehaviorMapper.insert(alb);
return ResponseResult.success(insert);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

