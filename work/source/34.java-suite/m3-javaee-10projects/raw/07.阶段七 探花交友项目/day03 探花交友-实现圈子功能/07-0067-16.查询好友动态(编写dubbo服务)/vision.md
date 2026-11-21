# 画面线理解：16.查询好友动态（编写dubbo服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\16.查询好友动态（编写dubbo服务）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:54, 01:29, 02:22, 03:16, 04:30, 05:19, 06:06, 07:26, 08:12, 08:42, 09:51, 10:48, 11:22, 12:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:43:53

1) 这一组画面整体在讲什么（一句话）：
实现查询好友动态功能，包括定义 Dubbo 接口、编写服务实现类、使用 MongoDB 操作时间线数据，并处理分页查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程笔记文件 day03 四子.md 中的章节 2.4.1，内容是“编写dubbo接口”，并显示了 QuanziApi 接口定义代码。
画面 2: 展示了 IDE 中的 QuanziApi 接口代码，光标位于方法 `boolean savePublish(Publish publish);` 的末尾。
画面 3: 展示了 QuanziApiImpl.java 文件中 `savePublish` 方法的实现，包含创建 Timeline 对象并保存到 MongoDB 的逻辑。
画面 4: 展示了 Timeline.java 文件，定义了 MongoDB 文档的实体类，包含 id、userId、publishId、date 等字段。
画面 5: 展示了 QuanziApiImpl.java 文件中 `queryPublishList` 方法的实现，正在构建 Query 对象用于查询。
画面 6: 展示了在 `queryPublishList` 方法中，使用 PageRequest.of 构建分页参数。
画面 7: 展示了在 `queryPublishList` 方法中，查询当前用户的关注列表，并为每个好友创建并保存时间线数据。
画面 8: 展示了在 `queryPublishList` 方法中，使用 `this.mongoTemplate.find` 查询 Publish 对象列表。
画面 9: 展示了在 `queryPublishList` 方法中，使用 `Query.query(Criteria.where("id").in())` 查询 Publish 对象。
画面 10: 展示了在 `queryPublishList` 方法中，使用 `Query.query(Criteria.where("id").in()).with(Sort.by(Sort.Order.desc("")))` 查询 Publish 对象。
画面 11: 展示了在 `queryPublishList` 方法中，使用 `List<ObjectId> ids = new ArrayList<>()` 存储时间线 ID。
画面 12: 展示了在 `queryPublishList` 方法中，使用 `Pageable` 的 `getTotal()` 方法获取总记录数。
画面 13: 展示了在 `queryPublishList` 方法中，使用 `Pageable` 的 `getPageInfo()` 方法获取分页信息。
画面 14: 展示了课程笔记文件 day03 四子.md 中的章节 2.4.2，内容是“编写实现”，并显示了 `queryPublishList` 方法的完整实现代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.tanhu.dubbo.server.api;
import com.tanhu.dubbo.server.pojo.Publish;
import com.tanhu.dubbo.server.vo.PageInfo;
public interface QuanziApi {
    /**
     * 发布动态
     * @param publish
     * @return
     */
    boolean savePublish(Publish publish);

    /**
     * 查询动态
     * @return
     */
    PageInfo<Publish> queryPublishList(Long userId, Integer page, Integer pageSize);
}
```

画面 2:
```java
public interface QuanziApi {
    /**
     * 发布动态
     * @param publish
     * @return
     */
    boolean savePublish(Publish publish);

    /**
     * 查询动态
     * @return
     */
    PageInfo<Publish> queryPublishList(Long userId, Integer page, Integer pageSize);
}
```

画面 3:
```java
Timeline timeline = new Timeline();
timeline.setId(ObjectId.get());
timeline.setUserId(publish.getUserId());
timeline.setPublishId(publish.getId());
timeline.setDate(System.currentTimeMillis());
this.mongoTemplate.save(timeline, collectionName: "quanzi_time_line_" + user.getFriendId());
return true;
```

画面 4:
```java
package com.tanhu.dubbo.server.pojo;
import ...
/**
 * 时间线表，用于存储发布（或推荐）的数据，每一个用户一张表进行存储
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "quanzi_time_line")
public class Timeline implements java.io.Serializable {
    private static final long serialVersionUID = 8096178416317502524L;
    private ObjectId id;
    private Long userId; // 好友id
    private ObjectId publishId; // 发布id
    private Long date; // 发布的时间
}
```

画面 5:
```java
Query query = new Query().with();
this.mongoTemplate.find(query, Timeline.class, collectionName: "quanzi_time_line_" + userId);
return null;
```

画面 6:
```java
Pageable pageable = PageRequest.of(int page, int size, Sort sort)
PageRequest.of(int page, int size, Direction direction, String... properties)
PageRequest new T()
try { exp } catch(Exception e) {
```

画面 7:
```java
//查询当前用户的关注数据，将动态数据写入到好友的时间线表中
Query query = Query.query(Criteria.where("userId").is(publish.getUserId()));
List<Users> users = this.mongoTemplate.find(query, Users.class);
for (Users user : users) {
    Timeline timeline = new Timeline();
    timeline.setId(ObjectId.get());
    timeline.setUserId(publish.getUserId());
    timeline.setPublishId(publish.getId());
    timeline.setDate(System.currentTimeMillis());
    this.mongoTemplate.save(timeline, collectionName: "quanzi_time_line_" + user.getFriendId());
}
return true;
```

画面 8:
```java
//TODO 事务回滚
Query query = Query.query(Criteria.where("id").in());
List<Publish> publishlist = this.mongoTemplate.find(query, null, Publish.class);
return null;
```

画面 9:
```java
Query queryPublish = Query.query(Criteria.where("id").in()).with(Sort.by(Sort.Order.desc("")));
List<Publish> publishlist = this.mongoTemplate.find(query, null, Publish.class);
return null;
```

画面 10:
```java
Query queryPublish = Query.query(Criteria.where("id").in()).with(Sort.by(Sort.Order.desc("")));
List<Publish> publishlist = this.mongoTemplate.find(query, null, Publish.class);
return null;
```

画面 11:
```java
List<ObjectId> ids = new ArrayList<>();
for (Timeline timeline : timelines) {
    ids.add(timeline.getId());
}
```

画面 12:
```java
Pageable pageable = PageRequest.of(page - 1, pageSize, Sort.by(Sort.Order.desc("date")));
Query query = new Query().with(pageable);
List<Timeline> timelines = this.mongoTemplate.find(query, Timeline.class, collectionName: "quanzi_time_line_" + userId);
Query queryPublish = Query.query(Criteria.where("id").in(ids)).with(Sort.by(Sort.Order.desc("")));
List<Publish> publishlist = this.mongoTemplate.find(query, null, Publish.class);
return null;
```

画面 13:
```java
Pageable pageable = PageRequest.of(page - 1, pageSize, Sort.by(Sort.Order.desc("date")));
Query query = new Query().with(pageable);
List<Timeline> timelines = this.mongoTemplate.find(query, Timeline.class, collectionName: "quanzi_time_line_" + userId);
Query queryPublish = Query.query(Criteria.where("id").in(ids)).with(Sort.by(Sort.Order.desc("")));
List<Publish> publishlist = this.mongoTemplate.find(query, null, Publish.class);
return null;
```

画面 14:
```java
@Override
public PageInfo<Publish> queryPublishList(Long userId, Integer page, Integer pageSize) {
    PageRequest pageable = PageRequest.of(page - 1, pageSize, Sort.by(Sort.Order.desc("date")));
    Query query = new Query().with(pageable);
    List<Timeline> timelines = this.mongoTemplate.find(query, Timeline.class, collectionName: "quanzi_time_line_" + userId);
    List<ObjectId> publishIds = new ArrayList<>();
    for (Timeline timeline : timelines) {
        publishIds.add(timeline.getPublishId());
    }
    Query queryPublish = Query.query(Criteria.where("id").in(publishIds)).with(Sort.by(Sort.Order.desc("")));
    List<Publish> publishlist = this.mongoTemplate.find(query, null, Publish.class);
    PageInfo<Publish> pageInfo = new PageInfo<>();
    pageInfo.setPageNum(page);
    pageInfo.setPageSize(pageSize);
    pageInfo.setTotal(timelines.size());
    pageInfo.setRecords(publishlist);
    return pageInfo;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
