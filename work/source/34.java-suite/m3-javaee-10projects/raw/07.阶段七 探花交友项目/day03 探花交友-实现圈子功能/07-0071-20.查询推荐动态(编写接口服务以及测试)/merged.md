# 20.查询推荐动态（编写接口服务以及测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\20.查询推荐动态（编写接口服务以及测试）_【海量资源尽在 666java.com】.mp4
- 时长 8分38秒（音频 518s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们将来编写我们的这个接口的服务那么我们来找到这个推荐动态那么就是这样的一个Mock接口然后呢地址呢是这样的一个地址就是Moments下面这个Commode然后呢这个参数呢跟之前这个参数是一样的然后呢下面的返回数据呢也都是一样的所以说呢我们就参考它呢来去编写我们的一个Controller
[00:28] 那么在这个下面呢我们去写一个recommend这样的一个control那我们就直接来拷贝拷贝一下它拷贝一下它然后呢我们这个返回类型呢还是这个page result那么这个我们不能叫查询好友了对吧查询推荐推荐的动态信息然后呢这个我们加一个query recommend吧recommendpublish list然后呢这个参数呢都一样
[00:57] 然后呢我们到这个里面去做一个这个查询啊去做一个查询那么在这个方法中呢我们要注意了就是我们这个位置啊这个位置我们写的是不是就是通过这个用户是不是去做一个啊这个查询对吧那我们就来再写另外一个吧我们再来写另外一个这个方法吧我们就改造一下啊那么比如说我们这个
[01:23] 再重新去写一个这个方法重新写一个方法那么这个方法呢我们就来创建一个这个方法那么这个方法其实我们只需要去只需要去调用上面的上面的这个方法是不是就可以了那么我们可以把这个把这个U的这个是不是我们可以可以是放到上面是不是去做一个传递做一个这个传递
[01:51] 那么比如说我们就放到放到这来对吧放到这来那么如果我们去判断一下那么那么如果我们这个U的等于空的话如果U的等于空的话那么我们这个就如果等于空的话那么我们就不用去设置它了对吧那我们就直接去我们应该这样来写
[02:20] 那么如果UID等于空的话那我们应该这样来写叫UID等于一个那那么如果这个UID不等于空的话不等于空那么我们就把这个UID的值给它设置为点getIDgetID好好嘞好那我们最后传入它这样的话是不是就可以了对吧然后呢下面这个呢我们在调用的时候呢调用谁呢就是this.query
[02:49] query这个方法然后呢这个user对象那我们就设置为空然后呢pager然后呢pager size那么这是一个这个实现对吧那么在前面呢我们这个又该如何实现呢我们是不是应该写一个叫做query userpublish list那我们再来写另外一个方法这样的话这两个方法是不是就具体逻辑是不是得到一个共用了是不是
[03:16] 好那么这个方法应该怎么去写呢同样也是把它做一个拷贝啊就可以了只是说呢在这个位置啊我们这个user就需要通过sredlocal.get哎叫做什么的user啊叫user sredlocal.get那么这样的话呢是不是就ok了那么我们是不是就可以把这个方法给它做一个哎私有化了
[03:41] 那么只是在我们这个方法中去做一个调用啊就可以了那我们来看一下逻辑有没有问题啊就如果它为空的话啊如果它为空那这个就是为空那么就这个为空那么这个为空呢就查询的就是推荐了哎OK那么这个就是相当于什么呢默认啊查询推荐推荐的一个动态那么下面这个呢查询就是谁呢是不是查询查询好友动态哎OK
[04:08] 好那么这样的话我们设备就搞定了那么接下来呢我们把我们的这个server这个服务呢来启动一下好那我们来等待它的一个启动好那么我们这个启动呢报错了那么原因是呢我们刚刚把这个Controller拷贝过来我们没有给它去加这个url对吧那么这样的话肯定就会有冲突了肯定跑不起来那我后面需要加一个什么呢recommend加到这这样的话呢就ok了那我们重新再来启动一下
[04:37] 好那么现在呢我们这个呢服务就已经跑起来了接下来呢我们就来测试一下那么我们就在我们的这个位置吧去做一个查询走那么401登录已经超时了那我们重新再来登录一下那么比如说我们就还是使用它做一个这个应该是用json啊这种方式去提交然后呢我们再来一个通过
[05:07] 这个去做一个校验对吧好那么是不是有了这个token了然后呢我们再去做一个查询那么查询呢我们这个呢是大家这样去查询的话它显然呢是显然呢是会查询好友的这个信息那我们在后面加一个什么呢Rickmond加个Rickmond这样的话它就会去查询我们的推荐的这个信息了那我们来看一下啊对不对呢哎是不是查询到这个
[05:34] 推荐表的这个数据了对吧那我们显然呢是没有去做这个逻辑处理他是不是也能够去查到了对吧那么我们就来打一个断点吧我们去看一下啊查询这个推荐这个信息那么打到再来看他执行对不对啊好那么来看一下执行我们看一下啊recommend那么走
[06:04] 那么我们刚刚测试呢有点问题就是我们点击之后呢会发现根本没有进入这个断点啊那么原因是呢我们刚刚这个地方写错了就是我们已经写反了啊其实我们应该是写到这个位置来啊写到这个位置来那么我们去重新再启动一下啊我们来等待一下它的启动那么我们再次呢启动成功了我们再来去做一个测试那么这回呢它肯定就会进入到我们断点是不是没有去打呢我们还是打到这个位置来啊
[06:34] 走那么他显然呢会进入到我们这个断点这个位置然后呢我们去执行走那么可以看到我们在查询的时候这个用户ID啊就是为none的对吧然后呢去做一个查询这样的话呢就OK了没有问题那么到这里呢我们是不是已经就完成了我们这个这样的一个查询就是查询我们的推荐的啊这样的一个用户这样的一个动态信息
[07:01] 然后呢接下来我们来整合到我们的这个模拟器中的去做一个测试那我们还是把这个模拟器呢跑起来那么刚刚这个模拟器呢应该是就是可能过一段时间吧它可能就卡死了不能用了把它就关掉了那我们重新来启动一下好那么我们现在这个模拟器呢就跑起来了下面呢我们来打开我们这个碳花这个应用然后呢我们把我们的刚刚所
[07:28] 打的这个断点呢我们先给它去掉然后呢我们这样方便我们去做一个测试那我们去直接去还是走这个登录这个流程啊那么就是158啊0080然后呢是这个一号是多少呢哎呀忘记了啊这个是这个叫7988那么叫7988然后呢我们点击这个获取验证码啊然后呢验证码的数目是123456
[07:58] 好嘞登录成功了然后呢我们点击这个圈子那么可以看到推荐这个位置是不是已经查询到查询到这个数据了然后呢我们去点击这个好友他查询到也是这个数据当然了我们是刚刚呢是把这个用户ID为2的这个数据写入到了这个推荐表里面去那么在我们后面去集成了我们的这个推荐系统的话
[08:21] 它这个结果肯定是不一样了那么到这里呢我们是不是已经就实现了我们这个查询我们的推荐动态的这样的一个效果了OK好那么关于我们这个动态推荐动态的一个查询呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Mock 服务测试推荐动态接口，并展示后端 Java 代码实现、数据库数据及前端测试结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Mock 服务界面，接口路径为 /movements/recommend，请求头包含 Authorization 和 Content-Type。
画面 2: 展示 MovementsController.java 中 queryPublishList 方法的代码，用于查询用户发布的动态列表。
画面 3: 展示 MovementsService.java 中处理用户信息与动态关联的代码，设置动态的标签、昵称、性别等属性。
画面 4: 展示 MovementsService.java 中 queryPublishList 方法的代码，处理用户 ID 为 null 的情况并调用 quanZiApi 查询。
画面 5: 展示 MovementsController.java 中 queryRecommendPublishList 方法的代码，用于查询推荐动态列表。
画面 6: 展示 MovementsService.java 中 savePublish 方法的代码，处理上传图片并保存动态。
画面 7: 展示 Mock 服务界面，接口路径为 /movements/recommend，请求头包含 Authorization 和 Content-Type。
画面 8: 展示 Advanced REST Client 中设置请求头 Authorization 和 Content-Type，并发送 POST 请求。
画面 9: 展示 MovementsController.java 中 queryPublishList 方法的代码，用于查询用户发布的动态列表。
画面 10: 展示 Advanced REST Client 中发送 GET 请求，请求头包含 Authorization，返回状态码 200。
画面 11: 展示 Advanced REST Client 中发送 GET 请求，请求头包含 Authorization，返回状态码 200。
画面 12: 展示 Genymotion 模拟器启动界面。
画面 13: 展示 Navicat Premium 中 tb_user 表的数据，包含用户 ID、密码、创建时间等字段。
画面 14: 展示 Typora 中的文档，内容为 queryRecommendPublishList 方法的代码和测试结果截图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@GetMapping
public ResponseEntity<PageResult> queryPublishList(@RequestParam(value = "page", defaultValue = "1") Integer page,
                                                   @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
    try {
        PageResult pageResult = this.movementsService.queryPublishList(page, pageSize);
        return ResponseEntity.ok(pageResult);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 3:
```java
for (Movements movements : movementsList) {
    for (UserInfo userInfo : userInfoList) {
        if (movements.getUserId().longValue() == userInfo.getUserId().longValue()) {
            movements.setTags(StringUtils.split(userInfo.getTags(), ','));
            movements.setNickname(userInfo.getNickName());
            movements.setGender(userInfo.getName().toLowerCase());
            movements.setAvatar(userInfo.getLogo());
            break;
        }
    }
}
pageResult.setItems(movementsList);
return pageResult;
```

画面 4:
```java
public PageResult queryPublishList(User user, Integer page, Integer pageSize) {
    PageResult pageResult = new PageResult();
    Long userId = null;
    if (user != null) {
        userId = user.getId();
    }
    PageInfo<Publish> pageInfo = this.quanZiApi.queryPublishList(userId, page, pageSize);
    pageResult.setCounts(0);
    pageResult.setPages(0);
    pageResult.setPageSize(pageSize);
    pageResult.setPage(page);
    List<Publish> records = pageInfo.getRecords();
    if (CollectionUtils.isEmpty(records)) {
        // 没有查询到动态数据
    }
    return pageResult;
}
```

画面 5:
```java
@GetMapping("/recommend")
public ResponseEntity<PageResult> queryRecommendPublishList(@RequestParam(value = "page", defaultValue = "1") Integer page,
                                                          @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
    try {
        PageResult pageResult = this.movementsService.queryRecommendPublishList(page, pageSize);
        return ResponseEntity.ok(pageResult);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 6:
```java
private static final ProcessBuilder processBuilder = new ProcessBuilder();
private static final PageResult pageResult = new PageResult();
private static final List<Publish> records = pageInfo.getRecords();
```

画面 9:
```java
@GetMapping("/recommend")
public ResponseEntity<PageResult> queryPublishList(@RequestParam(value = "page", defaultValue = "1") Integer page,
                                                   @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
    try {
        PageResult pageResult = this.movementsService.queryPublishList(page, pageSize);
        return ResponseEntity.ok(pageResult);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 13:
```sql
SELECT * FROM tb_user LIMIT 1,1000;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

