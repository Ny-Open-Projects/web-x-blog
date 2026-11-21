# 画面线理解：18_app文章详情_关注接口_关注行为保存代码完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\18_app文章详情_关注接口_关注行为保存代码完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:48, 01:30, 02:09, 03:13, 04:11, 04:53, 05:32, 06:03, 06:32, 07:11, 07:30, 07:53, 08:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:18:18

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
<mapper namespace="com.heima.model.mappers.app.ApFollowBehaviorMapper">
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
</mapper>
```
画面5:
```java
package com.heima.user.service;
import com.heima.model.common.dtos.ResponseResult;
public interface AppFollowBehaviorService {
    //存储关注行为数据
    public ResponseResult saveFollowBehavior();
}
```
画面6:
```java
package com.heima.user.service.impl;
import com.heima.model.behavior.dtos.FollowBehaviorDto;
import com.heima.model.common.dtos.ResponseResult;
import com.heima.model.user.pojos.ApUser;
import com.heima.user.service.AppFollowBehaviorService;
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
