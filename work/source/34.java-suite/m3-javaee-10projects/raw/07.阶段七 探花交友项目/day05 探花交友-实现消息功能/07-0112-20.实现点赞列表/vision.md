# 画面线理解：20.实现点赞列表

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\20.实现点赞列表_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:41, 01:49, 02:44, 03:11, 03:41, 04:01, 04:53, 05:30, 06:00, 06:52, 07:24, 08:05, 09:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:14:46

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
package com.tanhu.server.controller;
import com.tanhu.server.vo.PageInfo;
import com.tanhu.server.service.IMService;
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
