# 画面线理解：19_自媒体文章管理_文章列表后台接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\19_自媒体文章管理_文章列表后台接口开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:10, 02:07, 02:48, 03:27, 04:11, 04:47, 05:33, 06:20, 07:10, 07:37, 08:38, 09:17, 10:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:55:12

1) 这一组画面整体在讲一个新闻内容管理系统的后端实现，重点是通过分页查询、条件筛选和数据映射来处理文章列表和图片素材。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个JSON在线解析器，其中包含一个包含文本和图片类型的JSON数组，用于模拟文章内容数据结构。
画面2：展示一个新闻管理后台的“内容列表”页面，显示文章状态筛选、分类筛选和时间范围筛选功能，当前无数据。
画面3：展示IDEA中`WinNewsMapper.java`文件，定义了`insertNews`和`selectBySelective`等方法，用于插入和分页查询文章数据。
画面4：展示`WinNewsMapper.xml`文件中的SQL映射，包含`selectBySelective`查询语句，使用`<if>`标签进行多条件动态拼接。
画面5：展示`WinNewsMapper.xml`中`countSelectBySelective`的SQL语句，用于统计符合条件的文章总数。
画面6：展示`NewsService.java`接口，定义了`saveNews`和`listByUser`等方法，用于处理新闻保存和分页查询业务。
画面7：展示`NewsServiceImpl.java`中处理图片上传的逻辑，包含对`fileServerUrl`的替换和异常处理。
画面8：展示`NewsServiceImpl.java`中`listByUser`方法的实现，创建`Map<String, Object>`并返回数据。
画面9：展示`NewsServiceImpl.java`中`listByUser`方法的实现，使用`while`循环和`ThreadLocal`进行数据处理。
画面10：展示`NewsServiceImpl.java`中`listByUser`方法的实现，使用`vulNewsMapper`进行数据查询并封装`PageResponseResult`。
画面11：展示`NewsServiceImpl.java`中`listByUser`方法的实现，设置`PageResponseResult`的`host`和`data`属性。
画面12：展示IDEA项目结构，聚焦于`heima-leadnews-media`模块下的`src/main/java`目录。
画面13：展示`NewsControllerApi.java`文件，定义了`submitNews`、`saveDraft`和`listByUser`等API接口。
画面14：展示`NewsController.java`文件，定义了`@PostMapping("/submit")`、`@PostMapping("/save_draft")`和`@PostMapping("/list")`等控制器方法。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面3：
```java
int insertNews(@Param("dto") NewsDto dto),
// ...
List<Follows> selectBySelective(@Param("dto") FollowsPageDto dto, Long uid)
// ...
int countSelectBySelective(@Param("dto") FollowsPageDto dto, Long uid);
```

画面4：
```xml
<select id="selectBySelective"
        resultType="com.heima.model.medias.VulNews">
    <include refid="Base_Column_list"/>
    from vul_news
    where
    user_id = #{dto.userId}
    and status = #{dto.status}
    and channel_id = #{dto.channelId}
    and title like concat('%', #{dto.keyword}, '%')
    and publish_time <![CDATA[>]]> #{dto.beginPubDate}
    and publish_time <![CDATA[<]]> #{dto.endPubDate}
    <if test="dto.page != null and dto.size != null">
        limit #{dto.page} , #{dto.size}
    </if>
</select>
```

画面5：
```xml
<select id="countSelectBySelective" resultType="java.lang.Integer">
    select count(1)
    from vul_news
    where
    user_id = #{uid}
</select>
```

画面6：
```java
public interface NewsService {
    // ...
    public ResponseResult saveNews(@Param("dto") NewsDto dto, Short type);
    // ...
    public ResponseResult listByUser(@Param("dto") FollowsPageDto dto);
}
```

画面7：
```java
if ("image".equals(map.get("type"))) {
    countImageNum++;
    String url = String.valueOf(map.get("value"));
    if (url.startsWith(fileServerUrl)) {
        url = url.replace(fileServerUrl, "");
    }
    // ...
}
```

画面8：
```java
Map<String, Object> res = new HashMap<>();
res.put("materials", materials);
res.put("countImageNum", countImageNum);
return res;
```

画面9：
```java
while (true) {
    wait(Long.timeout, int nanos);
    if (ThreadLocalUtils.get() != null) {
        // ...
    }
}
```

画面10：
```java
Long uid = WulNewsUtils.getUid();
List<VulNews> datas = vulNewsMapper.selectBySelective(dto, uid);
int total = vulNewsMapper.countSelectBySelective(dto, uid);
PageResponseResult responseResult = new PageResponseResult(dto.getPage(), dto.getSize(), total);
responseResult.setData(datas);
```

画面11：
```java
responseResult.setHost(fileServerUrl);
responseResult.setData(datas);
return responseResult;
```

画面12：
```text
src
├── main
│   └── java
│       └── com.heima.media
│           ├── config
│           ├── controller
│           ├── service
│           └── NewsService
└── test
```

画面13：
```java
public ResponseResult submitNews(@RequestBody NewsDto dto);
public ResponseResult saveDraft(@RequestBody NewsDto dto);
public ResponseResult listByUser(@Param("dto") FollowsPageDto dto);
```

画面14：
```java
@PostMapping("/submit")
public ResponseResult submitNews(@RequestBody NewsDto dto) {
    return newsService.saveNews(dto, (short) 1);
}

@PostMapping("/save_draft")
public ResponseResult saveDraft(@RequestBody NewsDto dto) {
    return newsService.saveNews(dto, (short) 2);
}

@PostMapping("/list")
public ResponseResult listByUser(@RequestBody FollowsPageDto dto) {
    return newsService.listByUser(dto);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。
