# 10.佳人信息的之用户相册展现

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\10.佳人信息的之用户相册展现_【海量资源尽在 666java.com】.mp4
- 时长 18分15秒（音频 1095s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们来看一下我们查看自己的相册这个功能的一个实现那么在前面呢,我们提到过就是在查看用户的这个详情的时候会同时呢,要查看他的一个相册其实就是他所发布的一些动态那么下面呢,我们先来看一下他的墨盒接口那么这个呢,就是他的一个墨盒接口然后呢,他的这个路径呢,是叫做MovementsAll然后呢,他的请求的参数呢,有三个
[00:28] 就是PagePageSize和UID这是标准的一个分页查询的一个参数然后下面这个结果呢也是一个标准的一个分页的一个响应的一个结果然后呢下面这个呢是我们的一些关于圈子中动态的一些相关的一些数据基本的一些数据返回好那么这个呢就是它的一个默克接口的一个定义那么下面呢我们就来实现那么首先呢我们需要在我们的
[00:56] 圈子API里面的去定义我们的一个这个接口啊就是我们那个是定义这个double这个接口啊好那么我们来拷贝一下然后呢我们进入到前面我们啊所写的这个double的一个接口找到这个圈子啊然后呢我们把它加到最下面来加到这个位置来那么要注意的是呢这个方法呢叫query什么呢apollo那么就是我们要查询自己的那个相册就是那么用户在
[01:26] 发布这个动态的时候呢会把这个动态信息先写到自己的这个就是相册表里面来所以说呢我们只要查询自己的相册表就可以了但是要注意的是呢虽然我们查询的是自己的相册表但是你最终返回或者响应的一个数据或者说一个对象呢是一个public对象因为呢我们
[01:51] 真正的一些动态的数据都是存储在public这个对象中啊这一点啊要注意那么也就是说我们来看一下我们的这个结构吧那么你比如说啊那么apollo的这个是一啊用户id为一的这个用户它是不是有一个这个动态对吧然后呢我们来看一下那么我们查询这个表其实它要找到就是public id然后呢我们再到public id中找到对应的一个数据返回这个大家应该能够理解了吧最终返回的还是public啊
[02:21] 所以说呢这一点要注意一下好那么下面呢我们就进入到我们的这个Service然后呢我们去做一个实现啊到这吧我们去上面去做一个实现呃做一个这个实现好那么这个就是我们的一个呃方法啊那么下面呢我们来看一下具体的一个实现呃那么他要求我们返回啊配置info那么我们就定义一个配置info
[02:52] PageInfo等于new一个PageInfo然后呢最后呢去做一个return啊然后呢我们给它set一些内容比如set我们的这个叫PageNumber那么就Pager然后呢我们再去set一个PageSize那就是PageSize然后呢我们再set一个我们的一个total那么总数呢我们是不提供的对吧不提供不提供我们的一个总数啊
[03:19] 然后呢,recode的呢我们就放到下面再去做一个这个提供那么接下来呢我们要去通过我们的mongo template然后呢去做一个查询那么fund啊fund去做一个查询那么需要一个query那么还需要一个class那么就是一个谁呢abolo.class那么要注意的是呢我们的这个
[03:47] 每一个人都有自己的一个相册啊所以说这个我们的一个表明呢需要去传递一下那么这个表明呢它就是这个Apollo然后呢下环线下环线再加一个谁呢再加一个这个我们啊由来地好这样的话呢就设置完成这个查询了那么接下来呢我写一下这个query啊那么query呢我们要知道的是呢
[04:12] 那么我们查询自己的相册表其实没有条件那我们直接去new一个这个query但是呢我们需要做分页所以需要定义一个pageable然后呢pageable等于什么page request.off然后去做一个search那个pagepage size然后呢我们再去设置一个排序对吧那我们肯定要按照按照什么呢
[04:42] 按照我们的时间的一个倒序排序DSA那么我们来看一下这个根据哪个字段呢我们来找一下它里面是不是有created根据这个字段我们去做一个倒序的一个排序这就是我们需要去写的这个Pageable
[05:02] 然后呢把这个pay table呢就丢进来然后呢query就丢到这个里面来那么这样的话呢我们其实就拿到了谁呢拿到我们这个Apollo的一个list但是呢我们还并没有结束是吧那么我们最终返回的并不是这个对象所以说呢我们需要先做一个判断啊那么如果说我们的这个就是有tils找一下啊那么就用它吧点isempty如果
[05:30] 它为空啊就是我们这个集合如果为空的话那我们就给它return啊一个呃那我们是不是应该这样来设置就是那么我们就设置一个呃配置info啊配直接啊直接return配置info就可以了那么因为配置info中呢我们的这个这个record就是就本身就是空那个集合所以我们直接是不是做return啊就ok了那么接下来呢我们其实就需要去呃查询我们的相册
[05:59] 所对应的我们的这个动态信息了对吧好那么我们来看一下怎么样去做一个查询那么肯定我们需要拿到我们的publish id所以说呢我们需要定义一个集合那么它所存储就是object id然后呢叫做publishpublish idids然后等于new一个arrival list
[06:27] 然后呢我们去做一个便利啊便利的就是Apollo的一个list然后呢publish ids按的去添加一个Apollo.get什么publish id啊那么这样的话呢我们是不是就拿到这个publish id了那么接下来呢我们再去做一个查询那么通过mongo template然后呢fend去做一个这个查询那么同样呢我们是需要去设置一个query对吧那我们就来设置吧
[06:56] 一个query然后呢这个叫叫这个我们写publish query吧query它等于什么呢等于我们的query点querycreator.avail去设置一个这个条件那么它所查询的这个条件呢肯定就是会根据我们的这个ID对吧
[07:22] 然后呢设置一个印这个操作印谁那就是我们public id啊啊去做这样的一个操作然后呢我们再去做一个啊viz再去做一个什么呢去做一个我们的一个哎应该是做排序对吧那我们就直接去做一个排序就好了通过一个sortsort by order然后呢来一个order dsc那么他呢同样的也是需要这个created
[07:51] 这个字段去做一个排序啊去做一个排序好嘞那么这样的话呢我们是不是就构造完成一个快语对象了然后呢我们的这个class呢就是这个publish.class然后呢它的返回呢其实就返回的就是我们这个publish的一个list然后呢我们把我们的这个publish list放到我们配置infoset一个record
[08:19] 那么set record我给它丢进来丢到这个里面来好那么这样的话呢是不是就返回了那这样的话其实我们的这个double的这个接口的一个编写呢其实我们又已经编写完成了那么下面我们来看一下讲义那么这个其实就是我们这个double的接口的一个编写跟我们写的是一样的那么接下来呢我们就需要去根据我们的这个这个Mock接口所定义
[08:46] 然后呢我们去设置我们的这个编写我们的Controller以及Service那么这样我们来就把这个Controller我们来拷贝一下那我们来找到我们的一个这个哎这个里面还有报错的地方吗我们来看一下哪里有错误呢嗯检查一下啊讲一下哪里有错误然后哎再再有错误看一下什么情况少一个封号好嘞好这样的这样的话呢就结束了
[09:16] 那我们把这个Controller我们来拷贝一下那么找到我们的这个server这个工程那么movins这个里面然后呢我们把它丢到下面来往下面去丢然后呢丢到哪里丢到这然后呢这是一个这个all这个操作然后呢我们它需要去通过一个我们的query去做一个查询那么我们就那就这样吧创建出来这个没有提示了吗
[09:49] 那么我们来放大看一下啊啊没有提示了那么没有提示了那我们就自己来有了好那么来创建啊好那么下面呢我们来编写这个方法这个方法编写就其实啊比较简单了啊那我们呃来看一下啊那么最终它反而是一个配置呃呃reward对吧那么我们就去去定义一个我们的一个配置啊reward啊定义它然后呢去return它啊
[10:21] 那么接下来呢我们去做一个这个查询对吧那我们去做这个查询啊先放到这来这个代码大家应该能看懂啊那我们就直接来拷贝了那么去通过我们刚刚所写的这个方法啊传递UID和我们的Page和Page Size然后呢有个Record拿到Record判断如果为空那就直接去Return我们这个PageResult就可以了好那么这是这个逻辑啊那么接下来呢我们就需要去干嘛呢去
[10:50] 最终我们所返回的是个Movements这个对象所以我们还需要去做这样的一个便利那我们把这个的也拷贝过来那么其实我们是便利我们的Record然后呢去得到我们那个Movements这么多一些这个数据然后呢我们通过因为在我们的Movements中这个里面的还是有一些需要我们去分装一些用户相关的一些信息的所以说呢我们还需要下面去做一个用户信息的一个查询那我们就
[11:19] 把这个就直接来拷贝过来吧这个代码大家应该是很熟悉了这样的一个代码好嘞来看一下那么我们在这个位置去遍历遍历我们这个moments list然后得到一个uids这样的一个集合然后我们去做这样的一个查询然后我们去query your info list然后我们去做这样的一个这个方法
[11:47] 我们调用当前的这个方法我们之前是不是分装过一个私有的一个方法去填充这里面的这个信息啊那我们来看一下啊那么呃我们去看一下这个是哦他是传递的是一个list进去那我们来看一下这个方法怎么去调用啊那么他传递的是一个这个list呃那么这个方法其实我们我们之前所分装的这个方法他已经呢就
[12:16] 包含了一些前面我们所写的这个就是创建这个Moments然后呢去去便利啊得到一个UIDs这样的一个集合去查用户的信息啊等等这个逻辑已经包含进去了所以说我们就没有必要这样去做了啊那么我们来看一下这个代码我们来修改一下那我们直接直接调用它然后呢到哪里呢一直到那么就就到这里把它这个都去掉啊这个我们不需要了
[12:43] 我们直接调用 race.for去做一个填充recodes那么这样的话就OK了那么这个就变得就更加的简单了因为我们之前做了这样的方法的一个分装然后它所返回就是一个moments的一个list那么去相当于就是拿到一个publist然后呢去分装得到一个我们的一个这个moments这样的一个集合这个里面就分装了一会所有的逻辑所以说我们直接调用它就OK了
[13:13] 这个应该是没有问题的好那么接下来呢我们就来测试一下这个接口啊好那么我们先把这个服务呢先重重启一下好那么现在呢我们服务呢都跑起来了那我们来查询一下啊那么我们呃用户ID1的他的呃今日最呃今日家人呢是57这个用户所以说我们呃给他传递一个我们这样我们就呃这样来拷贝一下啊导致啊呃然后我们去
[13:43] 去拷贝一下这个路径啊往这一丢然后呢我们需要去跟一个参数对吧那么跟一个那就是他了就是用户ID呢为57这个用户走查看他的一个这个就是圈子的一些这个信息这个他是不是没有数据啊没有数据那么我们来看一下他究竟有没有数据啊那么我们来找一下我们的这个57是有
[14:09] 然后呢是有应该是有一条然后呢尾号这个是173然后呢我们来看一下Publish中那么173是有但是他没有查到那我们来看一下究竟是为什么那么我们就在我们刚刚所写的这个往下面拉在我们这个位置去打一个断点我们来试一下测试一下看他是什么情况然后呢我们就跟进去然后呢往下面走
[14:38] 走然后呢走看一下这个Polo这个PageInfo这个有没有拿到数据那么这块就没有拿到数据对吧没有拿到数据那么肯定就return down了那就说明问题呢出现在哪里呢是出现在我们的刚刚所编写的这个逻辑中那么我们来找一下我们这个具体的逻辑的实现呢就在这儿我们来检查一下这个是UserID
[15:08] UID然后呢我们去去做一个查询去做这块做一个查询然后呢目前我们从代码上面直接来看的话可能也看不出这个问题那我们就去编写一个测试用力我们去debug跟踪一下这个问题他肯定能够找到那么这边来测试一下好那么我们编写一个这个测试用力那么去测试一下那么
[15:34] 我们就在这个位置去打一个断点然后呢我们debug去走一下好那么我们稍微等待一下好那么断点呢我们就跟进去来看一下这个查询走走走去做查询那么这一块哎他就没查到那么问题在哪呢其实我们现在呢已经就应该看到问题了其实我们这个配置呢没有简易啊这个是我们需要简易的一个操作那么没有简易的话他查询是我们的第二页啊这一点
[16:04] 要注意了好那我们再次来测试一下那我们走好那么我们再跟踪进去我们再来测试一下走走走走走查询那么看到这块是不是就有数据了对吧然后呢我们继续往下面走去查询我们的publish那么肯定能拿到一个这个publish来看一下这个publish list是不是也拿到我们所需要的这个数据了然后呢我们就直接通过好嘞那么
[16:34] 这样的话呢就保证我们这个方法呢是OK的没有问题那么接下来呢我们还是呢需要呢把我们的这个就是double服务呢再重启一下我们重新来做一个测试好那么我们这个服务呢就跑起来了那么接下来我们重新啊再来测试一下看一下这个结果怎么样那么我们等待一下他第一次这个请求呢会这个是有断点对吧那么就通过好那么我们来看一下他的结果这回应该是没有断点了啊
[17:04] 那么是出问题了是吧那么看一下什么问题呢是这个是超时了那我们再重新试一下OK好那么这回呢是不是就没有问题了那么接下来呢我们就整合到我们的APP来看一下那么我们就登录一下02026868然后呢我们去获取我们的验证码然后呢输入验证码23
[17:33] 四五六去做一个校验啊然后呢去登录到我们的首页那么这个就是我们的首页啊然后呢我们去点击我们的一个今日家人就是我们的五日期这个用户哎会发现呢上面是不是显示他的一些用户的基本信息然后呢下面是不是就显示他的发送的一些动态啊是不是就显示出来了哎OK好那么这样的话呢其实我们就完成了我们的这个
[18:01] 家人信息的这样的一个展现那么最后整合测试也是那么也是ok的ok好嘞那么关于我们家人信息的一个展现我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Dubbo 服务中实现分页查询用户相册功能，并通过 MongoDB 和 Redis 进行数据操作和缓存。

2) 按时间顺序列出每张画面的要点：
画面1：展示接口文档，接口名称为“用户动态”，接口路径为“/movements/all”，Mock地址为“https://mock.boxuegu.com/mock/164/movements/all”，请求头包含“Content-Type: application/json”和“Authorization”令牌。
画面2：展示接口定义文件，方法为 `queryCommentListByUser`，参数为 `userId`, `type`, `page`, `pageSize`。
画面3：展示服务实现类 `QuanziApiImpl` 中的 `queryAlbumList` 方法，初始化 `PageInfo` 对象并设置分页参数。
画面4：展示 `queryAlbumList` 方法中使用 `mongoTemplate.find(null)` 查询数据库。
画面5：展示 `queryAlbumList` 方法中使用 `mongoTemplate.find(query, Album.class, collectionName)` 查询数据库。
画面6：展示 `queryAlbumList` 方法中使用 `Query.query(Criteria.where("id").in(publishIds))` 查询数据库。
画面7：展示项目结构，包含 `my-tanhu-dubbo-Service` 模块。
画面8：展示 Markdown 文档，内容为“3.5.4. MovementsService”和“4. 聊一下”。
画面9：展示 `MovementsService` 类中的 `loveComment` 方法，使用 Redis 操作点赞数。
画面10：展示 `MovementsService` 类中的 `queryAlbumList` 方法，将查询结果转换为 `Movements` 对象列表。
画面11：展示 `MovementsController` 类中的 `saveMovements` 方法，处理上传的图片并发送消息。
画面12：展示 `QuanziApiImpl` 类中的 `queryAlbumList` 方法，使用 `PageRequest.of(page, pageSize, Sort.by(Sort.Order.desc("created")))` 设置分页参数。
画面13：展示 REST 客户端发送 GET 请求，响应状态为 200，返回 JSON 数据。
画面14：展示 Markdown 文档，内容为“4. 聊一下”和“聊一下功能包含了2个接口”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2：
```java
@Override
PageInfo<Comment> queryCommentListByUser(Long userId, Integer type, Integer page, Integer pageSize)
```
画面3：
```java
@Override
PageInfo<Publish> queryAlbumList(Long userId, Integer page, Integer pageSize) {
    PageInfo<Publish> pageInfo = new PageInfo<>();
    pageInfo.setPageNum(page);
    pageInfo.setPageSize(pageSize);
    pageInfo.setTotal(0); //不提供总数
    return pageInfo;
}
```
画面4：
```java
this.mongoTemplate.find(null)
```
画面5：
```java
this.mongoTemplate.find(query, Album.class, collectionName);
```
画面6：
```java
Query publishQuery = Query.query(Criteria.where("id").in(publishIds)).with(Sort.by(Sort.Order.desc("created")));
List<Publish> publishList = this.mongoTemplate.find(publishQuery, Publish.class);
```
画面7：
```text
my-tanhu-dubbo-Service
├── src
│   └── main
│       └── java
│           └── com
│               └── tanhua
│                   └── dubbo
│                       └── server
│                           └── api
│                               └── MovementsApi.java
```
画面9：
```java
public Long loveComment(String publishId) {
    User user = UserThreadLocal.get();
    boolean bool = this.quanziApi.saveLoveComment(user.getId(), publishId);
    if (!bool) {
        return null;
    }
    // 保存成功，获取喜欢数
    Long loveCount = 0L;
    if (this.likeCommentKey.hasKey(likeCommentKey)) {
        Long count = this.quanziApi.queryCommentCount(publishId, type: 1);
        loveCount = count;
    } else {
        loveCount = this.redisTemplate.opsForValue().set(likeCommentKey, String.valueOf(loveCount));
    }
}
```
画面10：
```java
List<Movements> movementList = new ArrayList<>();
for (Publish record : records) {
    Movements movements = new Movements();
    movements.setId(record.getId().toHexString());
    movements.setImageContent(record.getMedia().toArray(new String[]{}));
    movements.setTextContent(record.getText());
    movements.setUserId(record.getUserId());
}
```
画面11：
```java
try {
    String publishId = this.movementsService.saveMovements(textContent, location, longitude, latitude);
    if (StringUtils.isNotEmpty(publishId)) {
        // 发送消息
        this.quanziMQService.sendPublishMsg(publishId);
        return ResponseEntity.ok(null);
    }
} catch (Exception e) {
    e.printStackTrace();
}
return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
```
画面12：
```java
Pageable pageable = PageRequest.of(page, pageSize, Sort.by(Sort.Order.desc("created")));
Query query = new Query().with(pageable);
```
画面13：
```json
{
  "code": 0,
  "page": 1,
  "size": 10,
  "items": []
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面8：
标题：4. 聊一下
内容：
- 聊一下功能包含了2个接口：
  - 查询对方设置的问题
  - 接收答案
  - 提交答案后要发送消息给对方
  - mock接口：https://mock.boxuegu.com/project/164/interface/api/77973

5) 不涉及。

