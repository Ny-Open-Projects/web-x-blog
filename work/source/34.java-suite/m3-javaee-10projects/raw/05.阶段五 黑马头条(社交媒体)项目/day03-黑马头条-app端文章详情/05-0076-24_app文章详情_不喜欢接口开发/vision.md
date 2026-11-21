# 画面线理解：24_app文章详情_不喜欢接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\24_app文章详情_不喜欢接口开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:54, 01:26, 02:17, 03:20, 04:02, 04:29, 04:58, 05:18, 05:39, 06:01, 06:35, 07:26, 08:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:24:17

1) 这一组画面整体在讲什么（一句话）：
实现用户点赞/取消点赞功能的完整代码结构，包括控制器、服务层、数据传输对象、数据库映射文件及对应的业务逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示行为控制器（BehaviorController）类，包含保存点赞和取消点赞的接口方法，分别注入了AppShowBehaviorService和AppUnlikesBehaviorService。
画面2：展示点赞/取消点赞的数据传输对象（UnLikesBehaviorDto）类，定义了设备ID、文章ID、操作类型等字段。
画面3：展示项目结构，定位到mapper包，准备查看数据库映射文件。
画面4：展示点赞/取消点赞的数据库映射文件（ApUnlikesBehaviorMapper.xml），包含查询和插入SQL语句。
画面5：展示服务接口（ApUnlikesBehaviorService）定义，声明了保存点赞/取消点赞的方法。
画面6：展示服务实现类（ApUnlikesBehaviorServiceImpl）的开头，定义了注入的Mapper和Sequences。
画面7：在服务实现类中，通过IDE自动补全选择ApBehaviorEntryMapper。
画面8：在服务实现类中，为ApUnlikesBehavior对象设置属性，如entryId、articleId、type等。
画面9：在服务实现类中，为ApUnlikesBehavior对象设置创建时间并调用mapper的insert方法。
画面10：在服务实现类中，通过IDE自动补全选择ApBehaviorEntryMapper。
画面11：在服务实现类中，为ApUnlikesBehavior对象设置属性并调用mapper的insert方法。
画面12：展示行为控制器接口（BehaviorControllerApi）定义，包含保存点赞和取消点赞的方法。
画面13：展示行为控制器（BehaviorController）类，定义了保存点赞和取消点赞的接口方法。
画面14：展示行为控制器（BehaviorController）类，定义了保存点赞和取消点赞的接口方法，其中取消点赞方法的注解为@PostMapping("/unlike_behavior")。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@RequestMapping("/api/v1/behavior")
public class BehaviorController implements BehaviorControllerApi {
    @Autowired
    private AppShowBehaviorService appShowBehaviorService;

    @PostMapping("/save_behavior")
    public ResponseResult saveShowBehavior(@RequestBody ShowBehaviorDto dto) {
        return appShowBehaviorService.saveShowBehavior(dto);
    }

    @Autowired
    private ApplikesBehaviorService applikesBehaviorService;

    @Override
    public ResponseResult saveUnlikesBehavior(LikesBehaviorDto dto) {
        return applikesBehaviorService.saveUnlikesBehavior(dto);
    }
}
```

画面2：
```java
package com.heima.model.behavior.dto;

import ...

@Data
public class UnLikesBehaviorDto {
    // 设备ID
    @IdEncrypt
    Integer equipmentId
    // 文章ID
    @IdEncrypt
    Integer articleId

    // 不喜欢操作方式
    @IdEncrypt
    Short type;
}
```

画面4：
```xml
<resultMap id="BaseResultMap" type="com.heima.model.behavior.pojos.ApUnlikesBehavior">
    <result column="id" property="id"/>
    <result column="article_id" property="articleId"/>
    <result column="type" property="type"/>
    <result column="created_time" property="createdTime"/>
</resultMap>

<sql id="BaseResultMap" type="com.heima.model.behavior.pojos.ApUnlikesBehavior">
    select * from ap_unlikes_behavior where entry_id=#{entryId} and article_id=#{articleId} order by created_time desc
</sql>

<select id="selectLastUnlike" resultType="BaseResultMap">
    select * from ap_unlikes_behavior where entry_id=#{entryId} and article_id=#{articleId} order by created_time desc
</select>

<insert id="insert" parameterType="com.heima.model.behavior.pojos.ApUnlikesBehavior">
    insert into ap_unlikes_behavior (entry_id, article_id, type, created_time) values (#{entryId}, #{articleId}, #{type}, #{createdTime})
</insert>
```

画面5：
```java
interface ApUnlikesBehaviorService {
    ResponseResult saveUnlikesBehavior(UnLikesBehaviorDto dto);
}
```

画面6：
```java
@Service
@RequiredArgsConstructor
public class ApUnlikesBehaviorServiceImpl implements ApUnlikesBehaviorService {
    @Autowired
    private ApBehaviorEntryMapper apBehaviorEntryMapper;

    @Autowired
    private ApUnlikesBehaviorMapper apUnlikesBehaviorMapper;

    @Autowired
    private Sequences sequences;

    @Override
    public ResponseResult saveUnlikesBehavior(LikesBehaviorDto dto) {
        // 获取用户id，获取设备id
        ApUser user = ApUserContext.getCurrentUser();
        if (user == null || user.getEquipmentId() == null) {
            return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRES);
        }
        long userId = null;
        if (user != null) {
            userId = user.getId();
        }
        ApUnlikesBehavior abl = new ApUnlikesBehavior();
        abl.setEquipmentId(user.getEquipmentId());
        abl.setArticleId(Integer articleId);
        abl.setEntryId(Integer entryId);
        abl.setType(Short type);
        abl.setCreatedTime(new Date());
        abl.setUserId(userId);
        return null;
    }
}
```

画面7：
```java
private ApBehaviorEntryMapper apBehaviorEntryMapper;
```

画面8：
```java
if (user == null || user.getEquipmentId() == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRES);
}
long userId = null;
if (user != null) {
    userId = user.getId();
}
ApUnlikesBehavior abl = new ApUnlikesBehavior();
abl.setEquipmentId(user.getEquipmentId());
abl.setArticleId(Integer articleId);
abl.setEntryId(Integer entryId);
abl.setType(Short type);
abl.setCreatedTime(new Date());
abl.setUserId(userId);
```

画面9：
```java
ApUnlikesBehavior abl = new ApUnlikesBehavior();
abl.setEquipmentId(user.getEquipmentId());
abl.setArticleId(Integer articleId);
abl.setEntryId(Integer entryId);
abl.setType(Short type);
abl.setCreatedTime(new Date());
abl.setUserId(userId);
apUnlikesBehaviorMapper.insert(abl);
return null;
```

画面10：
```java
private ApBehaviorEntryMapper apBehaviorEntryMapper;
```

画面11：
```java
ApUnlikesBehavior abl = new ApUnlikesBehavior();
abl.setEquipmentId(user.getEquipmentId());
abl.setArticleId(Integer articleId);
abl.setEntryId(Integer entryId);
abl.setType(Short type);
abl.setCreatedTime(new Date());
abl.setUserId(userId);
apUnlikesBehaviorMapper.insert(abl);
return null;
```

画面12：
```java
package com.heima.behavior.apis;

import ...

public interface BehaviorControllerApi {
    // 保存用户点赞文章的行为
    @PostMapping("/save_behavior")
    ResponseResult saveShowBehavior(ShowBehaviorDto dto);

    // 保存点赞行为
    @PostMapping("/like_behavior")
    ResponseResult saveLikeBehavior(LikesBehaviorDto dto);

    // 保存取消点赞行为
    @PostMapping("/unlike_behavior")
    ResponseResult saveUnlikesBehavior(LikesBehaviorDto dto);
}
```

画面13：
```java
private AppShowBehaviorService appShowBehaviorService;

@Override
@PostMapping("/save_behavior")
public ResponseResult saveShowBehavior(@RequestBody ShowBehaviorDto dto) {
    return appShowBehaviorService.saveShowBehavior(dto);
}

@Autowired
private ApplikesBehaviorService applikesBehaviorService;

@Override
@PostMapping("/like_behavior")
public ResponseResult saveLikeBehavior(@RequestBody LikesBehaviorDto dto) {
    return applikesBehaviorService.saveLikeBehavior(dto);
}

@Override
@PostMapping("/unlike_behavior")
public ResponseResult saveUnlikesBehavior(@RequestBody LikesBehaviorDto dto) {
    return applikesBehaviorService.saveUnlikesBehavior(dto);
}
```

画面14：
```java
@Autowired
private ApplikesBehaviorService applikesBehaviorService;

@Override
@PostMapping("/like_behavior")
public ResponseResult saveLikeBehavior(@RequestBody LikesBehaviorDto dto) {
    return applikesBehaviorService.saveLikeBehavior(dto);
}

@Override
@PostMapping("/unlike_behavior")
public ResponseResult saveUnlikesBehavior(@RequestBody LikesBehaviorDto dto) {
    return applikesBehaviorService.saveUnlikesBehavior(dto);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
