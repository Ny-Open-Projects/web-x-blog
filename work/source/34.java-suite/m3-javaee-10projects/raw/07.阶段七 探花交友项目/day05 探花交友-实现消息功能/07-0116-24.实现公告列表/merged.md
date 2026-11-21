# 24.实现公告列表

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\24.实现公告列表_【海量资源尽在 666java.com】.mp4
- 时长 8分53秒（音频 533s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来实现我们这个公告列表啊那么这个公告呢其实是我们的后台系统啊对所有用户发布的这个公告的一个消息比如说呢我们的系统升级啊或者新功能的上线啊等等这样的一些这个消息那么需要注意的是呢这个是不区分用户的所有的用户呢都会去接收到这个消息或者说这条数据啊
[00:26] 那么接下来呢我们就来实现一下啊那么我们这里呢所采用的是使用数据库呢来存储我们的公告的这个数据那么我先把这个表结构呢先创建出来那么找到我们这个麦探花啊然后呢我们去点击这个查询然后呢我们去运行一下这个呢就是我们的一些啊这个表结构呢就已经创建好了我们来看一下啊那么来到这个位置来刷新一下啊表结构呢就OK了
[00:55] 那么接下来呢我们给它来插入一些数据啊那么在我的这个里面是有这个数据的啊那我们把这个数据呢就呃就把它复制成一个insert语句吧然后呢再回到我们的这个里面去做一个插入就可以了那我们把这个前面这个库呢给它去掉那么这样的话呢我们就可以去去做一个这个插入了那把它拿掉然后呢把这个呢也拿掉
[01:24] 然后呢我们去支援一下三条数据呢就已经有了我把这个呢给大家写到这个讲义中啊那么下面的这个就是我们的这个插入数据的然后呢插入啊插入插入我们的数据啊哎好嘞大概呢是有这三条数据啊好嘞那么我们这个表结构啊大概呢会有主要呢是两个字段一个呢是我们的
[01:52] 标题一个就是我们的这个描述啊也就详情好那么第一步呢我们这个就搞定了第二步呢我们来看一下这个poll那么这个poll呢我们还是把它直接写到我们的server里面就ok了那么要注意的是呢我们这个呢是后台系统给我们发布这个消息啊但是呢我们现在并没有去开发后台系统啊假设我们现在如果有后台系统的话就应该在后台中直接去发布这个消息啊就可以了
[02:17] 然后我们去创建我们这个Pozole这个对象那么把这个Pozole创建出来那么我们回到我们的这个就是Server下面一个Pozole这个包把它拷贝一下它去继承我们的一个BasePozole然后有三个资短当然了BasePozole中有两个Credit和Update
[02:40] 下面呢我们来创建这个map叫enforcement Mapper那我们把这个map呢我们来创建一下还是进入到我们这个server这个工程然后呢我们去这个里面去拷贝一下那么就OK了那么写这样的一个接口去继承basic Mapper那就OK好然后呢下面我们写一个enforcement一个Service那么这个Service呢我们来拷贝一下那我们回到这个Service这个下面啊倒载来
[03:10] 那么在这个Service中啊那么我们去注入了我们这个announcement Mapper然后呢我们去写一个查询就查询我们这个列表就可以了然后呢我们根据我们的created去做一个倒序排序啊就ok好做一个slack page做一个这个分页查询就ok了好那么下面我们定义一个VO对象那么VO对象呢是根据我们的这个就是我们的这个接口啊
[03:38] 我们的这个接口来看一下在下面的这个位置找一下这个消息上面的有一个叫做公告列表那么这个呢是我们的公告列表那么在这个里面呢我们返回的数据按照这个结构呢我们定义了一个announcement message叫message announcement这样的一个对象把它拷贝一下然后呢同样的也丢到我们的这个VO这个里面来丢到这个里面来
[04:05] 那么丢进来之后啊那么下面呢我们就要编写我们具体的逻辑了那么我们同样的把这个逻辑的也写到我们的im的这个Controller里面来那么我们写了这啊然后呢我们丢到它最下面来就是去查询我们的一个公告的一个列表然后呢在我们的im的一个Service中啊那我们来实现这个方法那么这个方法呢就是去实现它这个非常简单啊就是去查询我们的数据库啊就可以了
[04:33] 好那我们来看一下这个里面的一个实现那么这呢我们是缺少一个announcement的一个Service那我们就把它注入进来那好那我们在上面这个位置去注一下那我们叫announcement Service把它呢注入进来好那么注入进来之后这个是不是就搞定了那么还缺少一个created就是什么呢record它里面缺了created也就这个里面
[05:03] 我们缺少要把它加一个date这样的话呢就它有了这个get这个方法了那我们来看一下它的一个实现那么通过调用我们Service中所提供的一个query list这个方法得到一个这个列表然后拿到它的recode然后呢我们去分装成一个message announcement这样的一个对象
[05:24] 最后呢我们得到一个这个集合返回就可以了啊非常简单的这样的一个逻辑啊好那么接下来呢我们就把我们这个server呢重新启动一下那我们来看一下这个结果啊好那么我们来打开我们的这个APP啊我们来测试一下那么我们还是通过我们的一个这个020226962这个用户啊去做一个登录啊其实哪个用户呢都可以啊
[05:52] 123456啊做一个这个登录然后呢我们点击我们的这个消息啊点击这个消息然后呢可以看到呢在这个位置有一个公告啊我们点击这个公告然后呢就查询到了这个数据了对吧那么当然了这块呢是我们的这个APP这一端呢它的显示呢有点问题啊这个
[06:14] 应该是这个内容比较长超出它的一个显示的一个范围了它就会出现这样的一个问题那么这个其实没什么太大的关系只是我们这个APP这端的一些这个编写的问题但是我们这个接口的一个提供是不是已经就OK了对吧好那么这个呢就是我们的一个公告那么其实呢我们是可以对我们这个公告呢去做一个优化那么就是说那么我们其实查询这个公告呢是没有必要去
[06:44] 做一个这个登录校验的对吧那我们就给他加一个什么呢No Assault Ascent这样的一个注解就是说这个只要加了这个注解之后啊那我们拦截器是不是就不会再去对他做一个校验了对吧因为公告就是所有的人都能够去做查询那么没有必要去做一个登录啊那我们来测试一下那么重启一下他肯定也是OK的啊其实我们这个不测试呢也是可以的
[07:11] 既然登录可以那么不登录啊当然也是可以的啊OK好那么其实这个呢就是我们啊最终所实现的啊这样的一个这个效果那么关于我们这个接口的测试呢我们就不测了效果是一样的啊OK那么大家呢那么我们也可以来测一下吧就是如果说啊那么我们加了我们这个注解之后啊那么其实我们就没有必要去没有必要去跟谁呢是不是跟我们这个一个token了那我们直接去做一个
[07:39] 请求就可以了那我们可以来测试一下那么对他发起一个get请求那么get请求呢我们还得往上面找啊找到一个messages那么找到这个位置来那么再去跟一个下面一个什么呢announcement然后呢我们把这个的头去掉啊直接做请求就可以了他跑起来了吗现在可能还没有完全跑起来那我们需要稍微等待一下
[08:09] 好那么目前呢就已经跑起来了那么接下来我们发起请求哎OK那么数据是不是也可以拿到呀那么这个时候呢我们就更符合我们的这样的一个这个需求了对吧好那么我们在我们讲义中呢给大家也去加一下这个实现啊那么在Controller里面我们可以加这样的一个租节那么这个其实我们就对我们的代码做了一个小小的一个优化我们做一个优化
[08:40] 就是无需进行这个tokentoken的一个校验好嘞好那么关于我们这个公告列表的一个功能这个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个公告列表功能的完整开发流程，包括数据库表结构设计、POJO类、Mapper、Service、Controller层代码实现，以及最终的前端展示效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示公告列表功能的文档结构，包含表结构和POJO定义。
画面2：在Navicat中查看数据库表结构，确认`tb_announcement`表的字段。
画面3：展示POJO类的代码，包含`@Data`、`@AllArgsConstructor`等注解。
画面4：在IntelliJ IDEA中查看POJO类代码，确认字段定义。
画面5：展示Service层代码，包含分页查询方法。
画面6：展示VO对象定义的代码，包含`@Data`注解和字段。
画面7：在IntelliJ IDEA中查看Controller层代码，包含`@GetMapping("announcements")`方法。
画面8：展示Service层代码，包含`@Autowired`注解和`QuanZiApi`引用。
画面9：展示Service层代码，包含`PageResult`的构建和日期格式化。
画面10：展示调试过程，包含Genymotion模拟器界面和代码调试信息。
画面11：展示调试日志，包含Dubbo调用链路。
画面12：展示手机端公告列表的UI界面。
画面13：在IntelliJ IDEA中查看Controller层代码，包含`@RestController`和`@RequestMapping("messages")`。
画面14：展示Controller层代码，包含`@GetMapping("announcements")`方法和分页参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```sql
CREATE TABLE `tb_announcement` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL COMMENT '标题',
  `description` text COMMENT '描述',
  `deleted` int(11) DEFAULT '0' COMMENT '是否删除',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `created` (`created`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='公告表';
```

画面3：
```java
package com.tanhua.server.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Announcement extends BasePojo {
    private Long id;
    private String title;
    private String description;
}
```

画面5：
```java
@Service
public class AnnouncementService {

    @Autowired
    private AnnouncementMapper announcementMapper;

    public IPage<Announcement> queryList(Integer page, Integer pageSize) {
        QueryWrapper<Announcement> queryWrapper = new QueryWrapper<>();
        queryWrapper.orderByDesc("created");
        return this.announcementMapper.selectPage(new Page<Announcement>(page, pageSize), queryWrapper);
    }
}
```

画面6：
```java
package com.tanhua.server.vo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class MessageAnnouncement {
    private String id;
    private String title;
    private String description;
    private String createDate;
}
```

画面7：
```java
@GetMapping("announcements")
public ResponseEntity<PageResult> queryMessageAnnouncementList(@RequestParam("page") Integer page,
                                                              @RequestParam("pageSize") Integer pageSize) {
    PageResult pageResult = this.imService.queryMessageAnnouncementList(page, pageSize);
    return ResponseEntity.ok(pageResult);
}
```

画面8：
```java
@Autowired
private RestTemplate restTemplate;

@Value("${http://127.0.0.1:18080}")
private String ssoUrl;

@Autowired
private UserInfoService userInfoService;

@Reference(version = "1.0.0")
private QuanZiApi quanZiApi;

public Boolean contactUser(Long userId) {
    Users users = new Users();
    users.setUserId(UserThreadLocal.get().getId());
    users.setFriendId(userId);
    // 1、保存数据到MongoDB
    this.usersApi.saveUsers(users);
}
```

画面9：
```java
public PageResult queryMessageAnnouncementList(Integer page, Integer pageSize) {
    IPage<Announcement> announcementPage = this.announcementService.queryList(page, pageSize);
    List<MessageAnnouncement> messageAnnouncementList = new ArrayList<>();

    for (Announcement record : announcementPage.getRecords()) {
        MessageAnnouncement messageAnnouncement = new MessageAnnouncement();
        messageAnnouncement.setId(record.getId());
        messageAnnouncement.setTitle(record.getTitle());
        messageAnnouncement.setDescription(record.getDescription());
        messageAnnouncement.setCreateDate(new DateTime(record.getCreated()).toString("yyyy-MM-dd HH:mm:ss"));
        messageAnnouncementList.add(messageAnnouncement);
    }

    PageResult pageResult = new PageResult();
    pageResult.setPage(page);
    pageResult.setPageSize(pageSize);
    pageResult.setItems(messageAnnouncementList);
    return pageResult;
}
```

画面13：
```java
@RestController
@RequestMapping("messages")
public class IMController {

    private static final Logger LOGGER = LoggerFactory.getLogger(IMController.class);
}
```

画面14：
```java
@GetMapping("announcements")
public ResponseEntity<PageResult> queryMessageAnnouncementList(@RequestParam("page") Integer page,
                                                              @RequestParam("pageSize") Integer pageSize) {
    PageResult pageResult = this.imService.queryMessageAnnouncementList(page, pageSize);
    return ResponseEntity.ok(pageResult);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“9. 公告列表”，子标题“9.1、表结构”和“9.2、pojo”。
画面6：PPT标题为“9.5、定义vo对象”和“9.6、IMController”。
画面14：PPT标题为“9.6、IMController”，包含`@GetMapping("announcements")`方法和分页参数。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

