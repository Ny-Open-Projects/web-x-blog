# 画面线理解：21.小视频推荐之列表查询

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\21.小视频推荐之列表查询_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:34, 00:57, 01:44, 02:17, 02:41, 03:07, 03:36, 04:11, 04:34, 04:55, 05:18, 05:39, 06:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:06:40

1) 这一组画面整体在讲什么（一句话）：
演示如何在视频推荐系统中，通过 Redis 缓存用户推荐视频列表，并在服务层实现分页查询逻辑，同时展示相关代码实现、调试过程和 API 测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 显示 IntelliJ IDEA 中 `SparkVideo.java` 文件的代码片段。
- 代码内容：将推荐视频 ID 序列化后存入 Redis，键名为 `"QUANZI_VIDEO_RECOMMEND" + userId`，并关闭 Jedis 集群连接。
- 代码片段：
```java
String key = "QUANZI_VIDEO_RECOMMEND" + userId;
jedisCluster.set(key, StringUtils.join(products, separator: ','));
jedisCluster.close();
```

画面 2:
- 显示 Typora 中 `day08.md` 文件的文档内容。
- 文档内容：展示视频推荐服务的模块结构，包括 `VideoMQService`、`VideoController`、`RecommendVideo` 等。
- 文档内容：
```
4.7. 修改查询逻辑
```

画面 3:
- 显示 IntelliJ IDEA 中 `VideoService.java` 文件的代码片段。
- 代码内容：从 Redis 获取用户推荐视频列表，计算分页起始和结束索引，构建视频 ID 列表并查询视频列表。
- 代码片段：
```java
String redisValue = this.redisTemplate.opsForValue().get("QUANZI_VIDEO_RECOMMEND" + userId);
if (StringUtils.isNotEmpty(redisValue)) {
    String[] vids = StringUtils.split(redisValue, separatorChar: ',');
    int startIndex = (page - 1) * pageSize;
    if (startIndex >= vids.length) {
        endIndex = vids.length - 1;
    }
    List<Long> vidList = new ArrayList<>();
    for (int i = startIndex; i <= endIndex; i++) {
        vidList.add(Long.valueOf(vids[i]));
    }
    List<Video> videoList = this.videoApi.queryVideoListByPids(vidList);
    pageInfo.setRecords(videoList);
}
```

画面 4:
- 显示 IntelliJ IDEA 中 `VideoApi.java` 文件的代码片段。
- 代码内容：展示 `VideoApi` 接口定义，包括 `disFollowUser`、`queryVideoById`、`queryVideoListByPids` 等方法。
- 代码片段：
```java
Boolean disFollowUser(Long userId, Long followUserId);
Video queryVideoById(String id);
List<Video> queryVideoListByPids(List<Long> vids);
```

画面 5:
- 显示 IntelliJ IDEA 中 `VideoApi.java` 文件的代码片段。
- 代码内容：展示 `VideoApi` 接口定义，包括 `disFollowUser`、`queryVideoById`、`queryVideoListByPids` 等方法。
- 代码片段：
```java
Boolean disFollowUser(Long userId, Long followUserId);
Video queryVideoById(String id);
List<Video> queryVideoListByPids(List<Long> vids);
```

画面 6:
- 显示 IntelliJ IDEA 中 `VideoService.java` 文件的代码片段。
- 代码内容：从 Redis 获取用户推荐视频列表，计算分页起始和结束索引，构建视频 ID 列表并查询视频列表。
- 代码片段：
```java
String redisValue = this.redisTemplate.opsForValue().get("QUANZI_VIDEO_RECOMMEND" + userId);
if (StringUtils.isNotEmpty(redisValue)) {
    String[] vids = StringUtils.split(redisValue, separatorChar: ',');
    int startIndex = (page - 1) * pageSize;
    if (startIndex >= vids.length) {
        endIndex = vids.length - 1;
    }
    List<Long> vidList = new ArrayList<>();
    for (int i = startIndex; i <= endIndex; i++) {
        vidList.add(Long.valueOf(vids[i]));
    }
    List<Video> videoList = this.videoApi.queryVideoListByPids(vidList);
    pageInfo.setRecords(videoList);
}
```

画面 7:
- 显示 IntelliJ IDEA 中 `VideoApiImpl.java` 文件的代码片段。
- 代码内容：实现 `disFollowUser`、`queryVideoById`、`queryVideoListByPids` 方法。
- 代码片段：
```java
@Override
public Boolean disFollowUser(Long userId, Long followUserId) {
    Query query = Query.query(Criteria.where("userId").is(userId).and("followUserId").is(followUserId));
    DeleteResult deleteResult = this.mongoTemplate.remove(query, FollowUser.class);
    return deleteResult.getDeletedCount() > 0;
}

@Override
public Video queryVideoById(String id) {
    return this.mongoTemplate.findById(id, Video.class);
}

@Override
public List<Video> queryVideoListByPids(List<Long> vids) {
    Query query = Query.query(Criteria.where("vid").in(vids));
    return this.mongoTemplate.find(query, Video.class);
}
```

画面 8:
- 显示 IntelliJ IDEA 中 `VideoApiImpl.java` 文件的代码片段。
- 代码内容：实现 `queryVideoListByPids` 方法，使用 `Criteria.where("vid").in(vids)` 查询视频。
- 代码片段：
```java
Query query = Query.query(Criteria.where("vid").in(vids));
return this.mongoTemplate.find(query, Video.class);
```

画面 9:
- 显示 Advanced REST Client 浏览器插件界面。
- 界面内容：展示历史请求记录，包括 GET、POST 请求，如 `/1smallVideos`、`/user/login`、`/movements/recommend` 等。
- 界面内容：
```
2019-10-10 15:28:55 POST http://127.0.0.1/smallVideos
2019-10-10 15:27:27 POST http://127.0.0.1/user/login
2019-10-09 13:51 GET http://127.0.0.1/movements/recommend/page-1
```

画面 10:
- 显示 Advanced REST Client 浏览器插件界面。
- 界面内容：展示请求设置，包括 `Authorization` 头部和 `User-Agent` 头部。
- 界面内容：
```
Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.123 Safari/537.36
```

画面 11:
- 显示 IntelliJ IDEA 中 `VideoService.java` 文件的调试界面。
- 调试内容：展示 `queryVideoList` 方法的调试信息，包括 `page`、`pageSize`、`userId`、`redisValue`、`vidList` 等变量。
- 调试内容：
```
page: 1
pageSize: 10
userId: "User{id=1, mobile=176202666, password=null}"
redisValue: "1019,1041,1047,1051,1053,1055,1057,1059,1061,1063,1065,1067,1069,1071,1073,1075,1077,1079,1081,1083,1085,1087,1089,1091,1093,1095,1097,1099,1101,1103,1105,1107,1109,1111,1113,1115,1117,1119,1121,1123,1125,1127,1129,1131,1133,1135,1137,1139,1141,1143,1145,1147,1149,1151,1153,1155,1157,1159,1161,1163,1165,1167,1169,1171,1173,1175,1177,1179,1181,1183,1185,1187,1189,1191,1193,1195,1197,1199,1201,1203,1205,1207,1209,1211,1213,1215,1217,1219,1
