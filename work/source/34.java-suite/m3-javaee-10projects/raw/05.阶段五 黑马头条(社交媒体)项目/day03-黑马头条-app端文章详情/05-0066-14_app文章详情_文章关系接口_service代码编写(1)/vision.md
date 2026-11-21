# 画面线理解：14_app文章详情_文章关系接口_service代码编写(1)

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\14_app文章详情_文章关系接口_service代码编写(1)【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:07, 00:31, 02:01, 02:57, 03:39, 04:15, 04:53, 05:35, 06:06, 07:23, 08:31, 09:05, 10:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:14:49

1) 这一组画面整体在讲如何通过文章ID查询文章详情并加载用户行为（收藏、点赞、不喜欢、关注）数据，涉及服务层代码实现与数据库表结构设计。

2) 按时间顺序列出每张画面的要点：
画面1: 展示ArticleInfoDto类定义及行为表映射说明，右侧列出通过equipmentId或userId查询行为实体（entryId）的逻辑。
画面2: 展示IDE中项目结构，定位到heima-leadnews-article模块下的service包。
画面3: 展示AppArticleInfoServiceImpl类中根据文章ID查询文章内容和配置的代码。
画面4: 展示AppArticleInfoServiceImpl类中loadArticleBehavior方法的开始部分，注释说明通过equipmentId或userId查询行为实体。
画面5: 展示loadArticleBehavior方法中对user和equipmentId的非空校验逻辑。
画面6: 展示loadArticleBehavior方法中对user和equipmentId的非空校验逻辑，使用AppThreadLocal工具类获取用户信息。
画面7: 展示loadArticleBehavior方法中声明并初始化ApBehaviorEntryMapper。
画面8: 展示loadArticleBehavior方法中通过ApBehaviorEntryMapper查询行为实体。
画面9: 展示loadArticleBehavior方法中对user非空的判断逻辑。
画面10: 展示loadArticleBehavior方法中对user非空的判断逻辑，以及查询行为实体的SQL语句。
画面11: 重复画面1的内容，展示ArticleInfoDto类定义及行为表映射说明。
画面12: 展示Typora中文章行为表的表结构设计，包含ap_follow_behavior、ap_share_behavior、ap_collection、ap_likes_behavior等表。
画面13: 展示Typora中文章行为表的表结构设计，继续展示ap_likes_behavior表的详细配置。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3:
```java
//根据文章id查询content信息
ArticleConfig aparticleConfig = aparticleConfigMapper.selectByArticleId(articleId);
if(aparticleConfig==null){
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}else if(!aparticleConfig.getIsData()){
    aparticleContent = aparticleContentMapper.selectByArticleId(articleId);
    String content = StringUtils.join(aparticleContent.getContent(), "");
    aparticleContent.setContent(content);
    data.put("content",aparticleContent);
    data.put("config",aparticleConfig);
}
return ResponseResult.okResult(data);
```

画面4:
```java
@Override
public ResponseResult loadArticleBehavior(ArticleInfoDto dto) {
    //1. 通过equipmentId或userId查看行为实体 -->entryId
    //2. 通过entryId和articleId去查看收藏表，看是否有数据，有数据就说明已经收藏，否则就是没有收藏
    //3. 通过entryId和articleId去查看点赞表，看是否有数据，有数据就说明已经点赞，否则就是没有点赞
    //4. 通过entryId和articleId去查看不喜欢表，看是否有数据，有数据就说明不喜欢，否则就是喜欢
    //5. 通过authorId去app的id  user_id( app账号信息id)
    //查看关注表，根据当前登录人的userId与作者的app账号id去查询，如果有数据，就说明已经关注，没有则说明没有关注
    return null;
}
```

画面5:
```java
if(user==null && dto.getEquipmentId()==null){
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
}
```

画面6:
```java
if(user==null && dto.getEquipmentId()==null){
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
}
```

画面7:
```java
@Autowired
private ApBehaviorEntryMapper apBehaviorEntryMapper;
```

画面8:
```java
@Override
public ResponseResult loadArticleBehavior(ArticleInfoDto dto) {
    ApUser user = AppThreadLocalUtils.getUser();
    if(user==null && dto.getEquipmentId()==null){
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
    }
    //1. 通过equipmentId或userId查看行为实体 -->entryId
    ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectByUserIdEquipmentId(user.getId(), dto.getEquipmentId());
```

画面9:
```java
if(user==null){
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
}
```

画面10:
```java
if(user==null){
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRE);
}
```

画面12:
```markdown
| 表名 | 是否分库 | 分库类型 | 分库数量 | 分库策略 | 主键 |
|------|----------|----------|----------|----------|------|
| ap_follow_behavior | 是 | mycat | 2,000,000 | 1 | DN[1] | entry_id |
| ap_share_behavior | 是 | mycat | 1,000,000 | 1 | DN[2] | entry_id |
| ap_collection | 否 | zk_sequence | 1,000,000 | 50 | DN[0~49] | burst-(id_entry_id) |
| ap_likes_behavior | 否 | zk_sequence | 5,000,000 | 50 | DN[0~49] | burst-(id_behavior_entry_id) |
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面12、13: 展示Typora中文章行为表的表结构设计，包含ap_follow_behavior、ap_share_behavior、ap_collection、ap_likes_behavior等表，以及它们的分库、分库类型、分库数量、分库策略和主键等信息。

5) 无。
