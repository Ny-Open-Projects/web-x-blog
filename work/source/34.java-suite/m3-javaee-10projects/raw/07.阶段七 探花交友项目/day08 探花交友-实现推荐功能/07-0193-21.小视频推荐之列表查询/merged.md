# 21.小视频推荐之列表查询

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\21.小视频推荐之列表查询_【海量资源尽在 666java.com】.mp4
- 时长 6分3秒（音频 364s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来修改一下我们的查询逻辑啊那么这样的话呢就可以完成我们的一个推荐列表的一个查询了那么我们还是依然呢要找到我们的这个查询的Service啊在Service下面有一个叫做我们来看一下啊叫做Service下面呢Service包下面找到这个video Service那么在这个里面呢它其实是有一个查询我们这个列表在这个位置对吧
[00:26] 然后呢怎么样去做处理呢我们来看一下这个逻辑啊那么我们就把这个逻辑一直就写到这来吧啊拷贝一下好然后呢我们呃把它就丢到这来啊丢在然后呢这个我们其实就不需要了来看一下这个逻辑啊那么呃首先呢我们呃从我们的ready stone呢进行做一个命中
[00:49] 如果要是命中的话那我们就按照这个逻辑去走如果没有命中的话还是按照原来这个逻辑去走啊那么如果命中的话那我们还是跟之前一样就是需要对我们的这个视频ID呢去做一个这个speed截取那么这个应该叫VIDS啊不应该叫PID了我们改一下啊VIDS啊VIDS好那么这样的话呢我们就拿到我们的一些这个视频的一些这个ID
[01:19] 然后呢我们去设置它的这个start index和我们的一个end index然后呢对它做一个便利然后呢去做查询那么当然了我们现在没有这个方法就是query video list by pids那么这个方法我们就需要去扩展一下了那么我们到这个里面来扩展一下然后呢它的返回值呢就是一个叫做list然后呢这video对象
[01:48] 然后呢去做一个查询那么这个里面所传的也是一个浪类型的什么呢就是一个叫VIDS这个是我们啊根据我们的一个这个就是VIDS啊然后呢去批量啊查询视频的一个列表好那么这样的话呢我们这个列表是不是就已经啊就查到了啊然后呢我们进入到进入到我们这个
[02:17] video这个Service里面刚才找到我们这个video Service那么我们来重新找一下就它好那么在这个里面呢那我们来看一下那么这个video这个Service那么video Service呢我们来看一下它的一个查询列表那么这个呢是不是就搞定了对吧然后这个就OK了好那么接下来呢我们就来把我们的服务启动一下然后呢我们去测试一下
[02:47] 那我们把之前的这个double呢我们跑起来然后呢再把我们这个server这个服务呢我们先停掉一会儿来启动一下这样的话呢就OK了当然了我们这个刚刚我们是不是还没有去编写这个实现的对吧好那么还没有写实现那我们来写一下那么这个写起来就非常的简单了那么我们就通过race.mongo.template
[03:15] 做一个分的一个查询query设置为num然后下面是一个vid.class这样的话就搞定然后query我们就来拷贝一下拷贝query然后我们去设置什么设置我们的vid然后把这个就去掉了把这个都给他拿掉点印印随Vids那么把query就给他丢到丢到这个位置来
[03:45] 好那么这样的话呢我们这个查询呢就搞定了啊就搞定了好然后呢我们把这个刚刚我们这个double呢再重新啊启动一下好那我们这个服务呢就跑起来了那么接下来呢我们还是在Service中啊那么这个位置啊去打一个断点然后呢我们去做一个小视频的一个查询的一个测试啊然后呢我们找到找到我们之前的一个这个历史记录啊
[04:15] 那我们就去做一个查询了好那我们对他发起这个get请求啊好那么来看一下对不对啊然后呢我们找到这个Controller来检查一下那么我们这个小视频要想去做查询的话那么是不是就对他发起get请求啊就可以了好走好请求是不是就来了走走走走往下走走走然后呢就要注意那么这个位置呢先去
[04:44] 做一个命中看是否能够命中到数据那么发现了数据是不是已经命中到了然后往下面走然后去做一个分割然后去拿到start index然后再拿到end index再去做一个分页查询拿到几个我们的一个vid然后断点打到这个位置来走然后去做一个执行查询我们这个就是video list
[05:13] 查到是不是有10条这个数据啊然后呢我们就可以去通过了好然后呢断点呢也给它去掉然后呢我们再来看一下这个结果是不是跟我们之前所查询的结果是一样啊这个呢其实就是我们去推荐出来的一些这个列表然后呢我们来看一下那么我们可以再去跟一个参数就叫配置等于2我们再去做查询走
[05:39] 这个结果肯定它是又是不一样了对吧好嘞好那么这样的话我们是不是就实现了我们小视频小视频这个列表的一个推荐这样的一个查询那么我们下面只需要去整合到我们的一个APP去做一个查询就可以了好那么关于我们这个的查询逻辑的一个修改那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

