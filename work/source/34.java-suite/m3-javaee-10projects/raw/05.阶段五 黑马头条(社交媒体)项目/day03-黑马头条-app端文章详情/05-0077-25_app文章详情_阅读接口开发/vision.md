# 画面线理解：25_app文章详情_阅读接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\25_app文章详情_阅读接口开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:29, 02:14, 03:29, 04:42, 06:05, 07:48, 09:05, 10:28, 12:07, 13:14, 14:24, 15:35, 17:38, 18:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:25:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 MyBatis 框架实现用户阅读行为数据的持久化操作，包括 Mapper 接口定义、XML 映射文件编写、Service 层实现以及 Controller 层调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示项目结构，选中 `BehaviorControllerApi` 接口，准备进入行为相关的代码实现。
画面 2: 展示 `ApReadBehaviorMapper` 接口，定义了 `insert`、`update`、`selectById` 等方法。
画面 3: 展示 `ApReadBehaviorMapper.xml` 文件内容，定义了 `Base_Column_List` 结果映射和 `selectById` 查询语句。
画面 4: 展示 `ApReadBehaviorMapper.xml` 文件内容，补充了 `insert` 和 `update` 语句，包含 `if` 条件判断和 `#` 占位符。
画面 5: 展示 `AppReadBehaviorServiceImpl` 类，开始编写服务层代码。
画面 6: 展示 `AppReadBehaviorServiceImpl` 类中，通过 `AppThreadLocalUtils` 获取当前用户信息。
画面 7: 展示 `AppReadBehaviorServiceImpl` 类中，使用 `AppThreadLocalUtils` 获取用户信息并进行非空校验。
画面 8: 展示 `AppReadBehaviorServiceImpl` 类中，注入 `ApBehaviorEntryMapper` 和 `ApReadBehaviorMapper`。
画面 9: 展示 `AppReadBehaviorServiceImpl` 类中，通过 `ApBehaviorEntryMapper` 查询行为实体并赋值。
画面 10: 展示 `AppReadBehaviorServiceImpl` 类中，通过 `ApReadBehaviorMapper` 查询行为实体并赋值。
画面 11: 展示 `AppReadBehaviorServiceImpl` 类中，创建 `ApReadBehavior` 对象并设置属性。
画面 12: 展示 `AppReadBehaviorServiceImpl` 类中，根据是否插入判断调用 `insert` 或 `update` 方法。
画面 13: 展示 `BehaviorController` 类，定义了 `saveBehavior` 方法。
画面 14: 展示 `BehaviorController` 类，定义了 `saveLikeBehavior` 和 `saveReadBehavior` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package com.heima.model.mappers.app;

import com.heima.model.behavior.pojos.ApReadBehavior;

public interface ApReadBehaviorMapper {
    int insert(ApReadBehavior record);
    int update(ApReadBehavior record);
    ApReadBehavior selectById(String burst, Integer entryId, Integer articleId);
}
```

画面 3:
```xml
<mapper namespace="com.heima.model.mappers.app.ApReadBehaviorMapper">
    <resultMap id="Base_Column_List" type="com.heima.model.behavior.pojos.ApReadBehavior">
        <id column="id" property="id" />
        <result column="entry_id" property="entryId"/>
        <result column="article_id" property="articleId"/>
        <result column="count" property="count"/>
        <result column="read_duration" property="readDuration"/>
        <result column="percentage" property="percentage"/>
        <result column="load_duration" property="loadDuration"/>
        <result column="created_time" property="createdTime"/>
        <result column="updated_time" property="updatedTime"/>
        <result column="burst" property="burst"/>
    </resultMap>
    <select id="selectById" resultMap="Base_Column_List">
        select id, entry_id, article_id, count, read_duration, percentage, load_duration, created_time, updated_time, burst
        from ap_read_behavior
        where entry_id = #{entryId} and article_id = #{articleId}
    </select>
</mapper>
```

画面 4:
```xml
<insert id="insert" parameterType="com.heima.model.behavior.pojos.ApReadBehavior">
    insert into ap_read_behavior (id, entry_id, article_id, count, read_duration, percentage, load_duration, created_time, updated_time, burst)
    values (#{id}, #{entryId}, #{articleId}, #{count}, #{readDuration}, #{percentage}, #{loadDuration}, #{createdTime}, #{updatedTime}, #{burst})
</insert>

<update id="update" parameterType="com.heima.model.behavior.pojos.ApReadBehavior">
    <if test="id != null">
        update ap_read_behavior
        set
            read_duration = #{readDuration},
            percentage = #{percentage},
            load_duration = #{loadDuration},
            count = #{count},
            created_time = #{createdTime},
            updated_time = #{updatedTime},
            burst = #{burst}
        where id = #{id}
    </if>
</update>
```

画面 5:
```java
package com.heima.behavior.service.impl;

import com.heima.behavior.service.AppReadBehaviorService;
import com.heima.model.behavior.dto.ReadBehaviorDto;
import org.springframework.stereotype.Service;

@Service
@SuppressWarrnings
public class AppReadBehaviorServiceImpl implements AppReadBehaviorService {
    @Override
    public ResponseResult saveReadBehavior(ReadBehaviorDto dto) {
        return null;
    }
}
```

画面 6:
```java
//获取用户信息，获取设备id
ApUser user = AppThreadLocalUtils.get().getUser();
//根据当前的用户信息或设备id查询行为实体
ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectById(user.getId(), dto.getEntryId());
if (apBehaviorEntry == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```

画面 7:
```java
//获取用户信息，获取设备id
ApUser user = AppThreadLocalUtils.get().getUser();
//根据当前的用户信息或设备id查询行为实体
ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectById(user.getId(), dto.getEntryId());
if (apBehaviorEntry == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```

画面 8:
```java
@Autowired
private ApBehaviorEntryMapper apBehaviorEntryMapper;
@Autowired
private ApReadBehaviorMapper apReadBehaviorMapper;
```

画面 9:
```java
//获取用户信息，获取设备id
ApUser user = AppThreadLocalUtils.get().getUser();
//根据当前的用户信息或设备id查询行为实体
ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectById(user.getId(), dto.getEntryId());
if (apBehaviorEntry == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```

画面 10:
```java
//获取用户信息，获取设备id
ApUser user = AppThreadLocalUtils.get().getUser();
//根据当前的用户信息或设备id查询行为实体
ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectById(user.getId(), dto.getEntryId());
if (apBehaviorEntry == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```

画面 11:
```java
ApReadBehavior apReadBehavior = apReadBehaviorMapper.selectById(user.getId(), dto.getEntryId());
boolean isInsert = false;
if (apReadBehavior == null) {
    isInsert = true;
    apReadBehavior = new ApReadBehavior();
    apReadBehavior.setId(sequences.sequenceReadBehavior());
}
apReadBehavior.setEntryId(apBehaviorEntry.getEntryId());
```

画面 12:
```java
ApReadBehavior apReadBehavior = apReadBehaviorMapper.selectById(user.getId(), dto.getEntryId());
boolean isInsert = false;
if (apReadBehavior == null) {
    isInsert = true;
    apReadBehavior = new ApReadBehavior();
    apReadBehavior.setId(sequences.sequenceReadBehavior());
}
apReadBehavior.setEntryId(apBehaviorEntry.getEntryId());
```

画面 13:
```java
package com.heima.behavior.controller.v1;

import org.springframework.web.bind.annotation.*;

@RestController("/api/v1/behavior")
public class BehaviorController implements BehaviorControllerApi {
    @Autowired
    private AppShowBehaviorService appShowBehaviorService;

    @PostMapping("/save_behavior")
    public ResponseResult saveShowBehavior(@RequestBody ShowBehaviorDto dto) {
        return appShowBehaviorService.saveShowBehavior(dto);
    }
}
```

画面 14:
```java
@Autowired
private AppLikesBehaviorService appLikesBehaviorService;

@PostMapping("/like_behavior")
public ResponseResult saveLikeBehavior(@RequestBody LikeBehaviorDto dto) {
    return appLikesBehaviorService.saveLikeBehavior(dto);
}

@Autowired
private AppReadBehaviorService appReadBehaviorService;

@PostMapping("/read_behavior")
public ResponseResult saveReadBehavior(@RequestBody ReadBehaviorDto dto) {
    return appReadBehaviorService.saveReadBehavior(dto);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
