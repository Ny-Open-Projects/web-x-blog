# 20.实现点赞列表

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\20.实现点赞列表_【海量资源尽在 666java.com】.mp4
- 时长 9分11秒（音频 551s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续啊那么接下来呢我们来实现我们的点赞列表这个功能那么首先呢我们来看一下它的一个Mock地址啊是这样的一个地址那么就是这个点赞这个列表啊然后呢它呢是Message是Likes这样的一个地址get请求然后呢请求的时候呢携带两个参数那么一个是Page和PageSign
[00:24] 然后呢下面呢是它的返回的数据结构啊那么关键的是下面的item这个数据啊那么接下来呢我们就根据这个数据结构啊那我们定义一个对象啊叫做message like对象那么它呢也是放到我们这个VO对象中啊这个包里面来那么我们来拷贝一下啊然后呢进入我们这个server然后呢在这个server下面呢我们找到啊找到我们这个VO这个包丢到这来
[00:52] 好那么这个呢就是我们的message like啊这样的一个对象那么接下来呢我们就来编写我们的double的接口那么首先呢我们来编写的是我们的这个接口的一个定义啊那么这个呢我们要写到这个圈子啊这个API里面来那么我们先把它拷贝一下好然后呢我们找到我们的double这个interface然后呢我们找到这个下面的API圈子这个API那么我们丢到最下面来
[01:20] 那么这个方法定义了一个什么样的一个方法呢我们一起来看一下那么就是去查询我们的这个评论评论数据那么然后呢去by user也就通过用户去做一个查询那么传递参数呢传递了有user id和这个type还有page和page size那么有这四个参数那么接下来呢我们就来实现我们这个方法
[01:46] 那么我们打开我们的API然后呢打开这个圈子的这个实现然后呢下面我们来看一下具体的这个实现啊那我们把它来拷贝一下那我们来丢到这个里面来那么我们来看一下这个里面的一个实现呢还是比较简单的就是首先构造一个PageRequest然后呢排序呢是根据我们的Created做一个倒序的这样的一个
[02:11] 排序那么接下来呢我们就去构造我们的查询条件两个条件第一个呢就是UID啊等于这个UID然后呢按的什么呢就是comment type那么就是说我们含次查询这个comment的这个这张表那么我们所有的这个点赞呢评论呢我们的一些这个喜欢的都是丢到这个里面来啊所以我们就直接的可以去做这样的一个查询那么最后把数据返回啊就可以了
[02:39] 好嘞那么这个呢就是我们的double服务啊那么接下来呢我们就来编写我们的接口服务那么这个服务呢同样的我们是把它写到我们的imcontroller中那么我们把这个点赞列表的这个方法呢我们来拷贝一下那么拷贝到我们的这个server这个下面来那我们来找到这个server下面呢找到这个Controller有个叫imcontroller那么我们就丢到再来
[03:07] 好那么我们来看一下这个方法那么这个方法呢就是按照我们的一个Mock的一个结构呢做一个这个定义啊接收两个参数一个呢就是Page和PageSize然后呢下面呢我们去做一个这个查询那么接下来呢我们把这个查询把这个查询给它去创建出来来看一下好做一个这个创建好那么我们来看一下这个的实现啊这个实现呢也是比较简单的一个实现啊那我们就
[03:38] 直接把它拷贝过来吧我们就拷贝到这好那我们拷贝过来一起来看一下就OK了好那么我们来去有一些这个包没导入进来那我们来导一下好那么这个里面我们缺少这个圈子的API那么我们注入一下叫圈子API对象把它呢reference去注入进来
[04:09] 1.0.0啊这样的一个版本然后呢我们来看一下下面这个方法的实现啊那么首先呢我们来看一下那么接收两个参数对吧配置和配置size然后呢获取了我们当前的这个用户然后呢通过我们刚刚所写这个方法呢去做一个查询那么这个呢是我们的一个UID啊然后呢是type是1type为1的是我们的这个点赞的这个数据啊
[04:38] 然后呢还有什么呢Page和Page Size然后呢拿到Page Info那么拿到Page Info之后呢我们是需要拿到它的一个Records就是它的一个数据集然后呢我们去搜集它的数据中的一个这个用户ID拿到用户ID然后呢我们还是去查询这个用户那么这个方法叫Query User Info List把它传递过去那么传递过去之后呢然后就可以拿到这个User Info List
[05:05] 然后呢我们来看一下这块呢对它做两层这个便利啊跟我们之前写的逻辑呢是一样的主要呢是要去获取用户的一些信息啊然后呢在这个位置呢去给它去填充了这个ID啊以及这个头像昵称啊还有它的这个创建时间那么这个时间呢我们把这个JOD的一个TimeDataTime的导入进来那我们需要对它做个格式化那么就通过这个年月日啊然后呢时分
[05:35] 然后呢去做一个这格式化最后呢去做一个返回啊那么就是这样的一个哎有报错的地方吗就是这样的一个实现啊我们来看一下错误在哪里呢错误是不是多了一个这个括号啊哎多了括号好这样的话就没有错误了啊好嘞好那么接下来呢我们就把我们这个double啊那么我们重启一下啊然后呢我们就来重新去做一个测试啊
[06:02] 好的我们来等待它的一个启动好那么现在呢我们就double服务和我们这个server服务呢都已经跑起来了那么接下来呢我们就来测试一下那么首先呢我们还是需要去先去做登录那么要注意这个登录呢因为我们查询的是我们点赞的数据那么我们用这个用户去登录的话那么显然我们肯定是没有数据的对吧那么就用之前的这个用户去登录那就是0202
[06:30] 0202 6868这样的一个这个手机号然后呢去发送这个验证码这个用户呢就是我们的这个第一个这个用户用户ID唯一的唯一的这个用户然后呢我们去再次做一个登录这个操作那么就通过这个用户呢去做一个登录拿到了这个token
[06:54] 那么拿到这个token之后啊那么接下来呢我们就去做一个查询啊首先我们把它先写到帐来然后呢我们来找到我们的这个Controller啊那么就是那我们直接来这个里面考吧啊那么这个是我们点赞的一个列表那么就message likes那我们就写到帐来啊写到它然后呢我们去发起一个get请求去做一个查询数据啊那么可以看到呢是不是我们已经就啊查询到
[07:23] 这个数据了对吧当然这个数据可能现在比较少因为只有一条这个数据好嘞那么这个就是我们的一个点赞这样的一个列表当然如果我们要是这个数据比较多的话他就会查到比较真实的一些这个数据了好嘞那么这样的话我们是不是就已经完成了我们这个点赞列表的这样的一个编写那么接下来我们就可以去把它去整合到我们的这个模拟器里面来然后我们去测试一下
[07:53] 那么我现在呢把我这个模拟器呢来启动一下那我们来稍微等待一下那么把它呢来启动一下啊好那么现在我们这个模拟器呢就跑起来了然后呢我们打开我们这个探花打开这个探花这个APP应用然后呢我们就
[08:14] 检查一下我们这个配置配置呢是这个是没有问题的然后呢我们就去登录一下那么还是通过我们这个17602026868这个用户去做一个登录那我们需要稍微等待一下响应超时我们再来点击一下那么可能是我们这个环境有点问题吧那我们稍微等待一下
[08:42] 好那么现在呢我们就登录进来了然后呢我们来看一下啊这块呢有个点赞我们点击这个点赞就可以去查询这个点赞列表了那么这个是不是就是我们刚刚我们所看到的这个数据啊所以说我们现在是不是已经就完成了我们这个点赞列表啊和我们的这个APP的这样的一个整合的一个测试啊OK好那么关于我们这个点赞列表的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现“点赞列表”接口，包括前端 Mock 数据配置、后端 Controller 层、Service 层代码编写，以及最终的接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Mock 服务中“点赞列表”接口的基本信息，包括接口名称、状态（已生成）、Mock 地址（https://mock.boxuegu.com/mock/164/messages/likes）。
画面 2: 展示了 IMService.java 文件中查询用户好友列表的代码，使用了 StringUtils.isEmpty 判断关键词，并通过 usersApi.queryUsersList 查询。
画面 3: 展示了 QuanzApi.java 文件中定义的查询评论列表的接口方法 queryCommentListByUser。
画面 4: 展示了 Typora 中的文档 day05 满课.md，当前章节为 7.4.1 “编写接口服务”，并显示了部分 Java 代码，包括 import 语句和 PageInfo 类的使用。
画面 5: 展示了 IMController.java 文件中定义的 @GetMapping("/likes") 接口，用于查询点赞列表。
画面 6: 展示了 Typora 文档中关于 queryMessageLikeList 方法的代码，其中包含获取用户信息、调用 QuanzApi 查询评论数据、并构建 PageResult。
画面 7: 展示了 IMService.java 文件中定义的 Quanzia 字段，用于调用 Dubbo 服务。
画面 8: 展示了 IMService.java 文件中 queryMessageLikeList 方法的代码，其中包含遍历评论列表、收集用户 ID、查询用户信息、并构建 MessageLike 对象。
画面 9: 展示了 IMService.java 文件中构建 MessageLike 对象的代码，包括设置 ID、头像、昵称、创建时间等属性。
画面 10: 展示了 IMService.java 文件中处理用户信息的代码，包括设置城市、用户 ID、昵称、性别等，并将结果添加到 contacts 列表。
画面 11: 展示了 Advanced REST Client 中发送请求的界面，请求体为 {"id": "126020983", "content": "11358"}。
画面 12: 展示了 Advanced REST Client 中成功返回的 JSON 响应数据，包含 page、size、total、records 等字段。
画面 13: 展示了 Genymotion 模拟器界面，用于测试 Android 应用。
画面 14: 展示了 Typora 文档中关于 queryMessageLikeList 方法的代码，与画面 6 和 8 的代码内容一致。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
接口名称: 点赞列表
Mock地址: https://mock.boxuegu.com/mock/164/messages/likes

画面 2:
if (StringUtils.isNotEmpty(keyword)) {
    userList = this.usersApi.queryAllUsersList(user.getId());
} else {
    PageInfo<Users> pageInfo = this.usersApi.queryUsersList(user.getId(), page, pageSize);
    userList = pageInfo.getRecords();
}

List<Long> userIds = new ArrayList<>();
for (Users users : userList) {
    userIds.add(users.getUserId());
}

//查询用户（好友）的信息
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in(column: "user_id", userIds);
if (StringUtils.isNotEmpty(keyword)) {
    queryWrapper.like(column: "nick_name", keyword);
}
List<UserInfo> userInfoList = this.userInfoService.queryUserInfList(queryWrapper);
List<Contacts> contactsList = new ArrayList<>();

画面 3:
/**
 * 根据pId批量查询数据
 * @param pids
 * @return
 */
List<Publish> queryPublishByPids(List<Long> pids);

/**
 * 查询用户的评论数据
 * @return
 */
PageInfo<Comment> queryCommentListByUser(Long userId, Integer type, Integer page, Integer pageSize);

画面 4:
package com.tanhu.server.Controller;
import com.tanhu.server.vo.PageInfo;
import com.tanhu.server.Service.IMService;
import com.tanhu.server.vo.Contacts;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

画面 5:
/**
 * 查询点赞列表
 * @param page
 * @param pageSize
 * @return
 */
@GetMapping("/likes")
public ResponseEntity<PageResult> queryMessageLikeList(@RequestParam(value = "page", defaultValue = "1") Integer page, @RequestParam(value = "pageSize", defaultValue = "10") Integer pageSize) {
    PageResult pageResult = this.imService.queryMessageLikeList(page, pageSize);
    return ResponseEntity.ok(pageResult);
}

画面 6:
@Value("${tanhu.url}")
private String url;

@Autowired
private UserInfoService userInfoService;

@Reference(version = "1.0.0")
private QuanzApi quanzApi;

public PageResult queryMessageLikeList(Integer page, Integer pageSize) {
    User user = ThreadLocal.get();
    PageInfo<Comment> pageInfo = new PageInfo<>();
    pageInfo.setPage(page);
    pageInfo.setPageSize(pageSize);
    pageInfo.setTotal(0);
    pageInfo.setRecords(0);
    List<Comment> records = pageInfo.getRecords();
    List<Long> userIds = new ArrayList<>();
    for (Comment comment : records) {
        userIds.add(comment.getUserId());
    }
    QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
    queryWrapper.in(column: "user_id", userIds);
    List<UserInfo> userInfoList = this.userInfoService.queryList(queryWrapper);
    List<MessageLike> messageLikeList = new ArrayList<>();
    for (UserInfo userInfo : userInfoList) {
        if (userInfo.getUserId().longValue() == comment.getUserId().longValue()) {
            MessageLike messageLike = new MessageLike();
            messageLike.setID(comment.getId().toHexString());
            messageLike.setAvatar(userInfo.getLogo());
            messageLike.setNickName(userInfo.getNickName());
            messageLike.setCreateDate(new DateTime(comment.getCreated()).toString("yyyy-MM-dd HH:mm"));
            messageLikeList.add(messageLike);
        }
    }
    pageInfo.setRecords(messageLikeList);
    return pageInfo;
}

画面 7:
import java.util.List;

@Service
public class IMService {

@Reference(version = "1.0.0")
private UsersApi usersApi;

@Autowired
private RestTemplate restTemplate;

@Value("http://127.0.1:18080")
private String ssoUrl;

@Autowired
private Quanzia quanzia;

public Boolean contactUser(Long userId) {
    //需要做2件事，1、保存数据到MongoDB，2、好友关系注册到微信
    Users users = new Users();
}

画面 8:
pageResult.setPage(page);
pageResult.setPages(0);
pageResult.setCounts(0);
pageResult.setPageSize(pageSize);

List<Comment> records = pageInfo.getRecords();

List<Long> userIds = new ArrayList<>();
for (Comment comment : records) {
    userIds.add(comment.getUserId());
}

QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in(column: "user_id", userIds);
List<UserInfo> userInfoList = this.userInfoService.queryList(queryWrapper);

画面 9:
List<MessageLike> messageLikeList = new ArrayList<>();
for (Comment record : records) {
    for (UserInfo userInfo : userInfoList) {
        if (userInfo.getUserId().longValue() == record.getUserId().longValue()) {
            MessageLike messageLike = new MessageLike();
            messageLike.setID(record.getId().toHexString());
            messageLike.setAvatar(userInfo.getLogo());
            messageLike.setNickName(userInfo.getNickName());
            messageLike.setCreateDate(new DateTime(record.getCreated()).toString("yyyy-MM-dd HH:mm"));
            messageLikeList.add(messageLike);
        }
    }
}

画面 10:
contact.list.add(contacts);
break;
} else {
    for (UserInfo userInfo : userInfoList) {
        Contacts contacts = new Contacts();
        contacts.setCity(StringUtils.substringBefore(userInfo.getCity(), separator: "-"));
        contacts.setUserId(userInfo.getUserId().toString());
        contacts.setNickName(userInfo.getNickName());
        contacts.setSenderUserInfo(userInfo.getSex().name().toLowerCase());
        contacts.setSenderUserInfo(userInfo.getSex().name().toLowerCase());
    }
}

画面 11:
{
    "id": "126020983",
    "content": "11358"
}

画面 12:
{
    "page": 0,
    "size": 10,
    "total": 1,
    "records": [
        {
            "id": "6d1d6f8920a2b2d46608",
            "avatar": "https://mock.boxuegu.com/tanhu/1124.jpg",
            "nickName": "123",
            "createDate": "2019-10-10 10:21"
        }
    ]
}

画面 13:
无代码或配置。

画面 14:
List<MessageLike> messageLikeList = new ArrayList<>();
for (Comment record : records) {
    for (UserInfo userInfo : userInfoList) {
        if (userInfo.getUserId().longValue() == record.getUserId().longValue()) {

