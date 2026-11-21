# 04.搜附近功能实现之编写APP接口

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\04.搜附近功能实现之编写APP接口_【海量资源尽在 666java.com】.mp4
- 时长 13分58秒（音频 839s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们来看一下我们的这个MOOC接口那么下面我们来编写我们的APP的这个服务的接口啊那我们打开这个地址,我们来看一下那么这个呢就是我们的收附近啊这样的一个,它的一个MOOC地址然后呢,探花,下面一个search,做搜索啊然后呢,参数呢,有两个,一个呢就是我们的性别另外一个呢就是我们的这个距离啊,就是我们那个半径然后下面这个就是返回的数据啊,是一个数组
[00:29] 那么接下来呢我们就根据这个结构啊我们首先来定义我们的一个VO就叫什么Near User VO就是我们附近的人啊这个VO对象那我们来打开我们的IDEA然后呢我们去找到我们的这个Server这个工程那么找到Server然后呢下面呢会有一个VO这个包然后呢我们把它丢过来就是Near User VO里面呢有三个属性啊
[00:56] 用户ID和这个头像还有这个昵称那么接下来呢我们就来看一下我们的Controller那么这个Controller中的方法我们依然呢要把它去写到我们这个todaybest这个Controller中那么我们来找到我们这个todaybest这个里面来然后呢往这丢啊
[01:15] 然后我们来看一下在这个里面我们把它拷贝过来之后我们可以看到它是有两个请求的参数那么一个就是我们的性别另外一个就是我们的一个距离那么如果这个距离没有传的话那么默认的就是两公里这样的一个值然后我们把这个方法创建出来接下来我们就来实现这个方法
[01:38] 好那么我们来看一下如何去做一个实现那么首先呢我们先要去查询我们当前啊当前用户的一个地理位置啊那么我们首先呢来拿到我们这个Ura这个对象那么Ura等于UraClocal.get然后呢我们去查询我们通过瑞士点什么UraLocation这个还没有定义是吧那我们就到上面来
[02:07] 然后呢我们去定义一个什么呢叫做Urallocation一个API然后呢我们把它呢reface进入进来然后呢我们指定这个Warsen这个版本呢是1.20.0这样的一个版本然后呢下面呢我们就通过reface.Urallocation这个API然后呢我们去query去查询
[02:35] 我们的一个当前这个用户的一个地理位置啊那么他呢就会拿到是一个叫做Ura LocationVO这个对象那么通过这个Ura LocationVO对象那么就可以拿到他的一个这个经纬度啊那么这个呢是他的纬度啊这个是经度啊那么经度然后呢我们再去拿到他的一个纬度
[03:04] 好那么我们这个地方啊去接收一下然后呢我们接下来呢就要去查询我们的一个这个附近的一个这个好友那我们通过我们这个API点query去做一个查询那我们把这个经纬度呢传递过来然后呢再传递我们的dxtens那么要注意的是呢我们在这个位置需要去转一下这个类型啊那么应该是int类型对吧
[03:34] 点value of去转一下它然后我们就会得到一个我们这个list那么就叫就叫这个吧有的location view一个list然后我们去做一个判断那么应该有个connection utils点easy empty那么如果它为空的话那我们就给它return一个空气核点
[04:03] 空集合好那么这样的话呢我们就处理完这个空了对吧那么接下来呢我们就来看一下这个非空那么非空呢就代表着我们是不是已经查询到这个数据了那么接下来呢我们来看一下那么最后我们返回的是这个NearUseVO它呢是和我们用户相关所以说呢我们又要去查询用户的信息了对不对所以呢我们定义一个List集合所存储的是浪类型的叫做Use
[04:33] userids等于new一个arrayvrlist然后呢我们去做一个做一个做一个便利啊然后呢我们去去便利它然后呢往这个userids中按着去添加一个locationvlocation.getthreader userid拿到这个userid然后呢我们这样的话呢是不是就
[05:02] OK了对吧然后呢我们接下来呢就可以去做一个这个查询了那么查询呢我们是不是要根据我们这个user info这个servicequery这个user info list那么传递两个参数那我们需要传递一个查询对象那叫queryrop这样的一个对象那么我们传递它这个user info然后呢叫queryropnew一个queryrop
[05:31] 然后呢我们把这块wrap呢就给他传过来啊呃然后呢我们来呃呃还要传递什么呢我们来看一下参数啊那么一个啊就是一个参数就可以了啊那就一个参数那就他然后呢他的返回值呢就是我们这个user info一个list啊然后呢我们来设置我们的查询条件那么第一个呢就是我们的一个这个eq啊相等我们user下载性id然后呢
[06:00] 应该是什么呢应该是硬硬这个操作然后呢我们把这个我们的一个叫EO的idslist传递过来那么这个就是我们的一个条件那么接下来呢还有一个条件就是我们传入了我们这个性别对吧所以说呢我们还是需要去做一下这个判断那么如果有tilsEQs然后呢去忽略这个大小写如果它和等于这个men的话
[06:29] 我们就应该设置我们的一个查询条件对吧然后点EQEQ谁就是我们的Sex然后去有个Sex美举然后设置一个Man好那么这个是男性用户对吧如果是女性的话我们再来去来一个else if去判断如果它等于什么这个Woman的话
[06:58] 那么我们就给他设置谁的设置我们条件的是这个woman这个对象这个美娶好那么这样的话我们是不是就设置完这两个条件那么接下来我们就来做我们的两层循环那么外面循环循环我们location的list然后再来一个循环循环我们有的info的list那么要注意的是那么前面的我们其实可以看到
[07:26] 当我们去查询了我们附近的这个好友的时候呢会把自己也查出来所以我们首先需要什么呢要排除自己那么怎么样去排除自己呢我们去拿到这个location v oget一个uid他的一个值如果等于我们当前的这个用户的值的话那就说明这是自己对吧那就干嘛呢直接continue就可以了啊continue
[07:52] 那么继续往下面走就OK了跳到下一个然后呢在这个位置那我们又需要去做一个判断了那么如果我们这个location这个VO.getUserID然后呢long value如果等于我们这个UserInfo.get这个UserID然后呢点这个long value的话那么
[08:19] 我们的话是不是就可以去找到了对吧那么就来一个break那么然后我们就去new谁是不是new我们返回的nearUseView这个对象new一个nearUseView这个对象然后我们是不是就需要在我们的上面这个位置我们需要定义一个什么叫做list然后存的是nearUseView然后我们就设置它为result
[08:50] Nil一个result然后呢最后呢我们return的就是这个result然后呢我们在上的result按的添加一个Nil这个VO好嘞那么我们去做一些这个设置这个Nickname那就是这个useinfo.getNickname然后呢设置三个然后呢还有设置是我们的这个头像那么我们来get一下get一个这个logo
[09:18] 然后呢在set设置一个UID那么就是这个getUID好那么三个这个属性就设置好了那么这样的话呢我们这个方法呢是不是就已经啊结束了那么这样的话就搞定了啊那么接下来呢我们就来测试一下我们这个方法好那么现在我们需要把我们的double服务以及SSO呢都跑起来那我们做一个测试啊好那么我们现在呢已经就把服务呢都跑起来了
[09:44] 那么跑起来之后啊那么接下来呢我们就来测试一下这个接口啊那我们去测试一下接口是OK的没有问题那么接下来呢我们就把它整合到啊我们的这个呃模拟器里面那我们用我们真实的这个APP呢来做一个测试啊那么我们来呃打开我们的一个这个碳花的这个APP然后呢我们来看一下它的一个整合到我们的一个APP中的一个结果啊然后呢我们来看一下服务呢首先确定的是
[10:14] 访问到我们的这个机器然后呢我们去做一个这个登录那么还是通过我们这个1这个用户去做一个登录658 68然后呢去获取验证码然后呢去输入123456好嘞那么他现在呢就会进入到我们的这个首页然后呢进入之后接下来呢我们点击这个位置有一个收付镜点击它
[10:46] 那么现在呢说这个有零个好友原因是我们的这个距离啊那么他呢会传递距离呢是默认是500那么我们来设置2000来设置一下走那么有查到数据吗2000是不是也没有啊那我们再来设置大一点吧因为我们还有个条件是性别是吧哎这个也没有查询到吗那我们再来看一下那么我们设置这个性别
[11:15] 这回是不是就有数据了对吧所以说呢跟我们这个查询的这个条件呢是有关系的比如说我们把这个距离再放大一点看有没有那也没有那我们这个呢也没有所以说这是根据我们这个条件来的这个就能查到好嘞好那么这样的话呢我们是不是就已经实现了我们的一个这个收付镜这个功能好嘞那么我们再返回再进入试一下
[11:45] 那应该是没有问题的那么我们可以把那个条件呢就放大一点去查当然我们现在数据量比较少比较少那我们就当然我们可以打个断点我们来看一下那么我们找到我们这个就是我刚刚我们所编写的这块那么就是在这个位置对吧那我们就去查一下那么比方说我们现在这个条件进入那么可以看到现在查询的是这个男性用户
[12:12] 然后呢再去查询我们的一个这个距离距离是多少呢来看一下距离呢是3000然后呢往下面走走去查询然后呢这块呢查询好友这个查询到6个然后呢往下面走然后断点我们就丢到这吧通过然后呢往下面走走走那么要注意的我们这个由着info查到几个呢这个也查到是6个对吧然后呢我们继续再往下面走
[12:43] 把自己排掉然后呢其他就不排了那就对了啊那么最后应该返回这五个才对啊这个应该是我们超时了那我们可以把这个断点呢就去掉啊再来测一下这个也有点卡了啊那么当然我们可以通过什么呢通过我们的这个我们就直接通过我们的这个APP通过我们这个接口去做一个测试啊就可以了那么去设置我们的查询的这个条件对吧等于这个慢
[13:16] 然后还有什么我们的一个ant去再去跟一个我们的distance等于2000去做一个查询好那么可以看到这个是有5个那么放到2500这是5个对的刚刚我们是6个排除掉自己那就是5个了ok没有问题那么这个我们就已经实现了我们的一个收付进这个功能那么这个就是我们所写的这个Service
[13:48] 然后呢是下面一个它的一个测试啊最后的一个效果呢就是这样的一个效果了好那么关于我们这个搜附近的功能的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的“附近好友”功能的后端实现，包括控制器、服务层代码编写、API 调用调试及前端效果展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：浏览器打开 MockBox 网站，页面为空白，可能用于演示接口测试环境。
画面2：IntelliJ IDEA 中显示 `TodayBestController.java` 代码，定义了 `@GetMapping("/search")` 接口，用于查询附近用户，返回 `ResponseEntity.ok(list)`。
画面3：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，包含 `queryRecommendUserList` 方法，用于查询推荐用户列表。
画面4：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中调用 `this.userLocationApi.queryUserFromLocation` 查询附近用户。
画面5：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中对查询到的用户列表进行空值判断，若为空则返回 `Collections.emptyList()`。
画面6：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中使用 `QueryWrapper` 构建查询条件，根据性别筛选用户。
画面7：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中遍历用户列表，排除自己。
画面8：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中创建 `NearUserVo` 对象，准备返回数据。
画面9：Advanced REST Client 发送 POST 请求到 `http://192.168.31.90/tanhu/search`，请求头包含 `Authorization`，响应状态码为 200，响应体为 JSON 格式数据。
画面10：Genymotion 模拟器显示“附近”功能界面，用户点击“筛选”按钮。
画面11：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中调用 `this.userLocationApi.queryUserFromLocation` 获取用户位置信息。
画面12：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中使用 `restTemplate.postForEntity` 发起 HTTP 请求。
画面13：Typora 编辑器显示“day10 讲义.md”文档，内容为“2. Elasticsearch 实现位置查询”，并附带一张“附近好友”功能的 UI 截图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@GetMapping("/search")
public ResponseEntity<List<NearUserVo>> queryNearUser(@RequestParam(value = "gender", required = false) String gender,
        @RequestParam(value = "distance", required = false) String distance) {
    try {
        List<NearUserVo> list = this.todayBeatService.queryNearUser(gender, distance);
        return ResponseEntity.ok(list);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面3：
```java
// 为当前用户生成一个默认推荐用户
todayBest = new TodayBest();
todayBest.setUserId(defaultUserId);
todayBest.setFateValue(99L);

// 补全用户信息
UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBest.getUserId());
if (null != userInfo) {
    todayBest.setAge(userInfo.getAge());
    todayBest.setAvatar(userInfo.getLogo());
    todayBest.setGender(userInfo.getSex().name().toLowerCase());
    todayBest.setNickname(userInfo.getNickName());
    todayBest.setTags(StringUtils.split(userInfo.getTags(), separatorChar));
}

return todayBest;

public PageResult queryRecommendUserList(RecommendUserQueryParam queryParam) {
    User user = UserThreadLocal.get();
```

画面4：
```java
this.userLocationApi.queryUserFromLocation(longitude, latitude, 10)
```

画面5：
```java
if (CollectionUtils.isEmpty(userLocationVoList)) {
    return Collections.emptyList();
}
```

画面6：
```java
List<Long> userIds = new ArrayList<>();
for (UserLocationVo locationVo : userLocationVoList) {
    userIds.add(locationVo.getUserId());
}
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in("user_id", userIds);
if (StringUtils.isNotBlank(gender)) {
    if (StringUtils.equalsIgnoreCase(gender, "man")) {
        queryWrapper.eq("sex", SexEnum.MAN);
    } else if (StringUtils.equalsIgnoreCase(gender, "woman")) {
        queryWrapper.eq("sex", SexEnum.WOMAN);
    }
}
```

画面7：
```java
for (UserLocationVo locationVo : userLocationVoList) {
    if (locationVo.getUserId().longValue() == user.getUserId().longValue()) {
        continue;
    }
    for (UserInfo userInfo : userInfoList) {
        if (locationVo.getUserId().longValue() == userInfo.getUserId().longValue()) {
            NearUserVo nearUserVo = new
```

画面8：
```java
NearUserVo (com.tanhu.server.vo)
double[]
int[]
boolean[]
char[]
float[]
long[]
short[]
void[]
```

画面9：
```json
{
  "code": 12,
  "userList": [
    {
      "userId": 25,
      "avatar": "https://itcast-tanhu.oss-cn-shanghai.aliyuncs.com/avatar_25.jpg",
      "nickname": "helma_25"
    },
    {
      "userId": 27,
      "avatar": "https://itcast-tanhu.oss-cn-shanghai.aliyuncs.com/avatar_27.jpg",
      "nickname": "helma_27"
    },
    {
      "userId": 10,
      "avatar": "https://itcast-tanhu.oss-cn-shanghai.aliyuncs.com/avatar_10.jpg",
      "nickname": "helma_10"
    }
  ]
}
```

画面12：
```java
HttpEntity<MultiValueMap<String, String>> httpEntity = new HttpEntity<>(params, headers);
ResponseEntity<Void> responseEntity = this.restTemplate.postForEntity(targetUrl, httpEntity, Void.class);
return responseEntity.getStatusCodeValue() == 200;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：Typora 文档标题为“day10 讲义.md”，二级标题“2. Elasticsearch 实现位置查询”，下方附带一张“附近好友”功能的 UI 截图，截图中显示“您附近有6个好友，选择他们聊聊吧！”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

