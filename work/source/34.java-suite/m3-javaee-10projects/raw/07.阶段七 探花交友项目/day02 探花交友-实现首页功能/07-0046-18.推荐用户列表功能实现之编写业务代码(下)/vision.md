# 画面线理解：18.推荐用户列表功能实现之编写业务代码（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\18.推荐用户列表功能实现之编写业务代码（下）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:38, 00:59, 01:17, 01:37, 01:57, 02:26, 04:01, 04:30, 05:02, 05:37, 05:59, 06:29, 06:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:29:49

1) 这一组画面整体在讲什么（一句话）：
演示一个推荐系统服务的 Java 代码实现，包括用户信息查询、推荐用户匹配、分数计算、排序和分页返回，以及服务启动和 API 测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 EditPlus 编辑器，打开一个名为 "Noname6" 的空白文件，左侧文件树显示项目目录结构，包含 "album.pl", "README", "u_data", "user", "u1", "u2" 等文件夹和文件。
画面 2: 显示 IntelliJ IDEA，打开 "TodayBestService.java" 文件，代码中正在构建一个 TodayBest 对象，设置用户 ID、年龄、性别、昵称、标签和 fateValue。
画面 3: 显示 IntelliJ IDEA，代码中正在使用 Lambda 表达式对 List 进行排序，排序依据是 TodayBest 对象的 fateValue。
画面 4: 显示 IntelliJ IDEA，代码中正在使用 IDE 的自动补全功能，为 todayBest 对象设置属性，如 setAge、setGender、setTags 等。
画面 5: 显示 IntelliJ IDEA，代码中正在使用 IDE 的自动补全功能，为 todayBest 对象设置属性，如 setScore、setUserId 等。
画面 6: 显示 IntelliJ IDEA，打开 "RecommendUserService.java" 文件，代码中定义了 queryTodayBest 方法，用于查询推荐用户，并设置 TodayBest 对象的属性。
画面 7: 显示 EditPlus 编辑器，打开一个名为 "Noname6" 的文件，内容为 PageResult 对象的 JSON 格式数据，包含多个 TodayBest 对象的信息。
画面 8: 显示 IntelliJ IDEA，代码中正在使用 Collections.sort 方法对 todayBests 列表进行排序。
画面 9: 显示 IntelliJ IDEA，代码中正在使用 IDE 的自动补全功能，为 Collections.sort 方法设置排序条件。
画面 10: 显示 EditPlus 编辑器，打开一个名为 "Noname6" 的文件，内容为 PageResult 对象的 JSON 格式数据，包含多个 TodayBest 对象的信息。
画面 11: 显示 IntelliJ IDEA，打开 "ServerApplication.java" 文件，代码中使用 @MapperScan 注解配置 Mapper 接口的扫描包，并调用 SpringApplication.run 方法启动服务。
画面 12: 显示 IntelliJ IDEA，打开 "application.properties" 文件，内容为 Spring Boot 的配置文件，包含 server.port、spring.application.name 等配置项。
画面 13: 显示 Advanced REST Client 浏览器插件，显示一个 JSON 格式的 API 响应数据，包含多个 TodayBest 对象的信息。
画面 14: 显示 Typora 编辑器，打开 "day02.md" 文件，内容为测试部分，包含一个 HTTP GET 请求的 URL 和响应数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
if (StringUtils.isNotEmpty(queryParam.getCity())) {
    queryWrapper.eq("column", "city", queryParam.getCity()); //城市
}
//需要查询用户的信息，并且按照条件查询
List<UserInfo> userInfos = this.userInfoService.queryUserInfoList(queryWrapper);
List<TodayBest> todayBests = new ArrayList<>();
for (UserInfo userInfo : userInfos) {
    TodayBest todayBest = new TodayBest();
    todayBest.setUserId(userInfo.getUserId());
    todayBest.setAge(userInfo.getAge());
    todayBest.setGender(userInfo.getSex().toLowerCase());
    todayBest.setNickName(userInfo.getNickName());
    todayBest.setTags(StringUtils.split(userInfo.getTags(), separatorChar: ','));
    todayBest.setFateValue();
    todayBests.add(todayBest);
}
```

画面 3:
```java
List<TodayBest> todayBests = new ArrayList<>();
for (RecommendUser record : records) {
    if (record.getUserId().longValue() == todayBest.getId().longValue()) {
        todayBest.setFateValue(record);
    }
}
```

画面 4:
```java
todayBest.setAge(userInfo.getAge());
todayBest.setGender(userInfo.getSex().toLowerCase());
todayBest.setNickName(userInfo.getNickName());
todayBest.setTags(StringUtils.split(userInfo.getTags(), separatorChar: ','));
```

画面 5:
```java
for (RecommendUser record : records) {
    if (record.getUserId().longValue() == todayBest.getId().longValue()) {
        double score = Math.floor(record.getScore());
        todayBest.setFateValue(Double.valueOf(score).longValue()); //分值
    }
}
```

画面 6:
```java
@Reference(version = "1.0.0")
private RecommendUserApi recommendUserApi;

public TodayBest queryTodayBest(Long userId) {
    RecommendUser recommendUser = this.recommendUserApi.queryWithMaxScore(userId);
    if (null == recommendUser) {
        return null;
    }
    TodayBest todayBest = new TodayBest();
    // 如果得分为96.2时，需要显示的分值是96
    double score = Math.floor(recommendUser.getScore());
    todayBest.setFateValue(Double.valueOf(score).longValue()); //分值
    todayBest.setId(recommendUser.getUserId()); //用户id
    return todayBest;
}

public PageInfo<RecommendUser> queryRecommendUserList(Long id, Integer page, Integer pagesize) {
    return this.recommendUserApi.queryPageInfo(id, page, pagesize);
}
```

画面 7:
```json
PageResult(counts=0, pagesize=10, pages=0, page=1, items=[TodayBest(id=5, nickname=heima_5, avatar=https://itcast-tanhua.css-cn-shanghai.aliyuncs.com/images/logo/16.jpg, gender=man, age=23, tags=[单身, 本科, 年龄相仿], fateValue=94), TodayBest(id=11, nickname=heima_11, avatar=https://itcast-tanhua.css-cn-shanghai.aliyuncs.com/images/logo/5.jpg, gender=man, age=34, tags=[单身, 本科, 年龄相仿], fateValue=93), TodayBest(id=18, nickname=heima_18, avatar=https://itcast-tanhua.css-cn-shanghai.aliyuncs.com/images/logo/15.jpg, gender=man, age=20, tags=[单身, 本科, 年龄相仿], fateValue=96), TodayBest(id=32, nickname=heima_32, avatar=https://itcast-tanhua.css-cn-shanghai.aliyuncs.com/images/logo/10.jpg, gender=man, age=26, tags=[单身, 本科, 年龄相仿], fateValue=93), TodayBest(id=45, nickname=heima_45, avatar=https://itcast-tanhua.css-cn-shanghai.aliyuncs.com/images/logo/13.jpg, gender=man, age=38, tags=[单身, 本科, 年龄相仿], fateValue=98), TodayBest(id=56, nickname=heima_56, avatar=https://itcast-tanhua.css-cn-shanghai.aliyuncs.com/images/logo/19.jpg, gender=man, age=41, tags=[单身, 本科, 年龄相仿], fateValue=97)])
```

画面 8:
```java
Collections.sort(todayBests, (o1, o2) -> new Long(o2.getFateValue() - o1.getFateValue()).intValue());
```

画面 9:
```java
Collections.sort(todayBests, (o1, o2) -> new Long(o2.getFateValue() - o1.getFateValue()).intValue());
```

画面 11:
```java
@MapperScan("com.tanhua.server.mapper") //设置mapper接口的扫描包
@SpringBootApplication(exclude = {MongoAutoConfiguration.class, MongoDataAutoConfiguration.class})
public class ServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ServerApplication.class, args);
    }
}
```

画面 12:
```properties
server.port=8080
spring.application.name=tanhua-server
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14: 显示 Typora 编辑器，打开 "day02.md" 文件，内容为测试部分，包含一个 HTTP GET 请求的 URL 和响应数据。
画面 14 的标题为 "3.6. 测试"。
画面 14 的 URL 为 "http://127.0.0.1/tanhua/recommend?page=1&gender=man"。
画面 14 的响应数据为：
```json
{
  "counts": 0,
  "items": [
    {
      "id": 5,
      "nickname": "heima_5",
      "avatar": "https://itcast-tanhua.css-cn-shanghai.aliyuncs.com/images/logo/16.jpg",
      "gender": "man",
      "age": 23,
      "tags": ["单身", "本科", "年龄相仿
