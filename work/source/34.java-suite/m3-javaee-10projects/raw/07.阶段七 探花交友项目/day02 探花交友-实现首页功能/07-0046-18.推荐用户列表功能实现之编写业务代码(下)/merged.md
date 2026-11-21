# 18.推荐用户列表功能实现之编写业务代码（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\18.推荐用户列表功能实现之编写业务代码（下）_【海量资源尽在 666java.com】.mp4
- 时长 7分2秒（音频 422s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们这个执行结果呢就出来了可以看到有这样的一个结果我们把这个结果呢拷问出来我们来看一下那么目前呢我们得到的这个数据呢有这么多应该是有10条这样的一个数据但是首先我们会发现有一个问题就是在这个位置我们的原份值它的值为None说明我们没有给它设置值那就是我们刚刚在写的过程中呢出现了一个小bug那我们就来给它添加一下那么这个Today Best
[00:29] 然后点set设置一个我们这个缘分值它就等于谁呢就等于我们上面的就等于我们上面的谁呢就是我们要通过我们的这个PagerInfo中的recodes才能够去拿到那么这个位置还麻烦一点就还是需要我们去做一个便利了那我们去便利一下吧便利一下我们一个叫做recodes
[00:57] 那么我们这个位置做一个判断如果说我们recall的点get我们的这个score对吧就是得分点这个什么呢就是double value吧哎错了应该是我拿到我们的这个ID啊get什么呢这个user IDget user ID点long value如果等于我们的这个叫做就是today best中的点get
[01:26] id点什么none value如果这两个值相等的话那说明找到它的这个值了对吧那我们就给它做一个设置啊这样才能够拿到点get score那么我们可以看一下啊这个位置还是我们之前的这个问题啊就是这个需要给它去找一下啊需要给它呢去设置它的一个这个就是去除这个小数啊那我们把这个这个逻辑呢就拿过来吧
[01:56] 把这个逻辑拿过来然后呢我们丢到这个Service中来这个逻辑我们刚刚已经写过这样的一个逻辑了那么设置它这样呢就OK了就code了好那么这样的话呢我们第一个这个问题就解决了那么接下来我们来看一下还有没有其他的一些这个问题呢那么这样我们先再来执行一次看一下它的一个结果那么走好那我们再来看一下这个结果怎么样那么我们就
[02:25] 网上一丢来看一下这个结果那么这个结果呢可以看到原份值呢数据呢是已经有了对吧其实我们仔细来观察一下这个数据会发现是有问题的那么它并没有按照这个就是我们的原份值呢去做一个倒序排序为什么是这样其实可以大家去想一下能够想明白原因是呢在我们之前的这个位置就是我们去做这个我们数据库
[02:55] 查询的时候啊在这个位置啊我们做这个数据库查询的时候那我们设置了一个这个印这个操作对吧那么我们数据库在查询的时候呢并没有做排序啊并没有做排序所以他拿到的结果啊不一定就是按照我们所传这个ID的这样的一个值去查询出来的所以说呢我们是最终啊需要在这个位置啊对我们这个集合呢去做一个排序啊对我们这个结果集做一个
[03:24] 排序啊做一个排序那么做排序呢我们还是需要按照什么呢按照我们这个这个缘分值的这个缘分值做一个倒序啊倒序排序那么怎么做呢对集合做排序呢我们就直接使用这个java util中所提供的一个这个排序方法就可以了那么我们通过这个connects中的一个set这个方法
[03:53] 那么第一个呢是list那第二个参数呢就是我们的一个这个比较器啊那么list呢就是这个today sticksbest然后呢下面这个呢是我们可以使用一个lam的表达式啊去做这样的一个编写那么我们需要用什么呢就是我们需要大的排到这个前面去对吧所以说我们需要去通过谁呢我们这个o2点
[04:21] 给了谁呢他的一个这个原分值然后呢去减去O1的这个原分值就是我们这个得分了然后呢去做出这样的一个对比那么我们来看一下这个是我们的这个他所要求的是转成这个int对吧我们就需要这么来玩一下就是需要去或者是用lang吧lang.valueof然后呢点int value
[04:51] 这样的话就得到一个这个值了那我们再来去执行一下看他会怎么样去做一个输出呢走好那么我们这个结果呢就出来了我们再来去查看一下啊那么这个时候呢我们就会发现他呢是不是就按照我们的一个就是我们的一个这个得分啊或者是原分值的一个从大到小去做这样的一个排序了
[05:16] OK那么我们呢就可以把我们这个服务呢跑起来通过我们web呢去做一个测试了那么我们刚刚呢是通过我们的测试用力呢去做一个测试对吧好那么接下来我们就来测试一下那么我们去在这个位置吧然后我们去直接来做一个启动OK好我们来稍微等待一下它的一个执行好那我们就通过我们的restclient的工具我们来测试一下看它的结果
[05:44] 会怎么样,那么我们就使用它吧然后我们传递参数为1对吧,Pages等于1或者我们不传,默认其实就是1那么我们需要把这个URL,那就是它了,我们去发这个token是有点问题的,那我们来拷贝一下吧,我们需要的token是它然后我们去把它来拷贝出来然后这个是我们所需要的一个token,然后走我们来看这个结果会怎么样,OK
[06:14] 那么这个结果呢其实就是我们所看到的这样的一个结果对吧排序之后的这样的一个结果那么最后一个得分的是93然后呢我们把它设置为这个配置12的话那我们再来执行那么可以看到是93 93 92可以看到还是整体是一个倒序这样的一个排序啊ok那么这样的话呢我们这个推荐列表是不是就已经就搞定了对吧那我们来看一下讲义啊这个就是我们推荐的列表
[06:42] 然后我们去Controller的一个编写和我们Service这样的一个编写那么是一样的跟我刚才写的这个是一样的那么最后的测试的结果那就是这样的一个结果了ok好那么关于我们推荐列表的一个实现我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
@MapperScan("com.tanhua.server.Mapper") //设置Mapper接口的扫描包
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

