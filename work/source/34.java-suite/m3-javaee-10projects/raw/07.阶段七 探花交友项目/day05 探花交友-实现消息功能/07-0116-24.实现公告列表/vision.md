# 画面线理解：24.实现公告列表

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\24.实现公告列表_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:31, 01:07, 01:58, 02:37, 03:28, 03:57, 04:19, 04:44, 05:10, 05:55, 07:05, 07:24, 07:54, 08:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:17:19

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
