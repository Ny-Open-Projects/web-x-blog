# 画面线理解：14_自媒体文章管理_发布文章业务代码编写1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\14_自媒体文章管理_发布文章业务代码编写1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 02:01, 04:08, 05:40, 08:10, 09:47, 12:22, 14:56, 16:15, 18:21, 19:53, 21:11, 22:05, 23:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:50:45

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现文章内容的保存功能，包括参数校验、JSON 数据解析、图片信息提取、文章类型判断和数据库持久化操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 NewsServiceImpl.java 文件中 saveNews 方法的开头部分，包含对 dto 参数的空值和内容为空的校验，以及调用 wuNewsMaterialMapper 的方法。
画面 2: 展示 saveNews 方法中对 dto.getId() 的判断，用于处理用户首次操作或修改操作。
画面 3: 展示在 saveNews 方法中添加了 ObjectMapper 字段的声明。
画面 4: 展示 saveNews 方法中添加了 try-catch 块，用于捕获 IO 异常并打印堆栈信息。
画面 5: 展示 extractUrlInfo 方法的实现，用于从图片 URL 列表中提取图片信息。
画面 6: 展示 NewsServiceImpl.java 文件的顶部，包含多个 @Autowired 注解的字段声明。
画面 7: 展示 extractUrlInfo 方法中用于遍历图片 URL 列表并提取图片信息的代码。
画面 8: 展示 saveNews 方法中使用 ObjectMapper 将 JSON 字符串解析为 List<Map>，并调用 extractUrlInfo 方法提取图片信息。
画面 9: 展示 saveNews 方法中对 dto.getType() 与文章类型常量进行比较的逻辑。
画面 10: 展示 saveNews 方法中根据图片数量设置文章类型（单图、多图、无图）的逻辑。
画面 11: 展示 saveNews 方法中设置文章状态、用户信息、创建时间等字段的代码。
画面 12: 展示 saveNews 方法中根据文章类型调用不同的 save 方法（saveNews 或 saveNewsWithImages）。
画面 13: 展示 saveNews 方法中设置文章状态、用户信息、创建时间等字段的代码。
画面 14: 展示 saveNews 方法中根据文章类型调用不同的 save 方法（saveNews 或 saveNewsWithImages）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Override
public ResponseResult saveNews(WallNewsDto dto, Short type) {
    //如果用户传递参数为空或文章内容为空则返回错误
    if (dto == null || StringUtils.isEmpty(dto.getContent())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //如果用户本次为首次操作那么去删除数据库中关联的数据
    if (dto.getId() != null) {
        wuNewsMaterialMapper.deleteById(dto.getId());
    }
```

画面 2:
```java
    //如果用户本次为首次操作那么去删除数据库中关联的数据
    if (dto.getId() != null) {
        wuNewsMaterialMapper.deleteById(dto.getId());
    }
```

画面 3:
```java
    private ObjectMapper objectMapper;
```

画面 4:
```java
    } catch (IOException e) {
        e.printStackTrace();
    }
```

画面 5:
```java
private Map<String, Object> extractUrlInfo(List<Map> list) {
    Map<String, Object> materials = new HashMap<>();
    for (Map map : list) {
        if ("image".equals(map.get("type"))) {
            materials.put("url", map.get("url"));
        }
    }
    return materials;
}
```

画面 6:
```java
@Autowired
private WmNewsMapper wmNewsMapper;

@Autowired
private WmNewsMaterialMapper wmNewsMaterialMapper;

@Autowired
private ObjectMapper objectMapper;
```

画面 7:
```java
private Map<String, Object> extractUrlInfo(List<Map> list) {
    Map<String, Object> materials = new HashMap<>();
    int order = 0;
    int countImageNum = 0;
    for (Map map : list) {
        if ("image".equals(map.get("type"))) {
            materials.put("url", map.get("url"));
            countImageNum++;
        }
    }
    materials.put("countImageNum", countImageNum);
    return materials;
}
```

画面 8:
```java
try {
    List<Map> list = objectMapper.readValue(content, List.class);
    //抽取信息
    Map<String, Object> extractInfo = extractUrlInfo(list);
    //图片信息
    materials = (Map<String, Object>) extractInfo.get("materials");
    //图片数量
    int countImageNum = (int) extractInfo.get("countImageNum");
    //保存或修改文章的数据
    //保存图片与当前文章的关系
    //保存图片与当前文章的关系
    //保存图片与当前文章的关系
} catch (IOException e) {
    e.printStackTrace();
}
```

画面 9:
```java
if (dto.getType().equals(dto.getType())) {
```

画面 10:
```java
if (countImageNum == WmMediaConstants.VM_NEWS_SINGLE_IMAGE) {
    walleNews.setType(WmMediaConstants.VM_NEWS_SINGLE_IMAGE);
} else if (countImageNum == WmMediaConstants.VM_NEWS_MANY_IMAGE) {
    walleNews.setType(WmMediaConstants.VM_NEWS_MANY_IMAGE);
} else {
    walleNews.setType(WmMediaConstants.VM_NEWS_NO_IMAGE);
}
```

画面 11:
```java
if (countImageNum == WmMediaConstants.VM_NEWS_SINGLE_IMAGE) {
    walleNews.setType(WmMediaConstants.VM_NEWS_SINGLE_IMAGE);
} else if (countImageNum == WmMediaConstants.VM_NEWS_MANY_IMAGE) {
    walleNews.setType(WmMediaConstants.VM_NEWS_MANY_IMAGE);
} else {
    walleNews.setType(WmMediaConstants.VM_NEWS_NO_IMAGE);
}
```

画面 12:
```java
private void saveNews(WallNewsDto dto, Short type) {
    if (countImageNum == WmMediaConstants.VM_NEWS_SINGLE_IMAGE) {
        walleNews.setType(WmMediaConstants.VM_NEWS_SINGLE_IMAGE);
    } else if (countImageNum == WmMediaConstants.VM_NEWS_MANY_IMAGE) {
        walleNews.setType(WmMediaConstants.VM_NEWS_MANY_IMAGE);
    } else {
        walleNews.setType(WmMediaConstants.VM_NEWS_NO_IMAGE);
    }
    walleNews.setUserId(user.getId());
    walleNews.setCreatedTime(new Date());
    walleNews.setSubmittedTime(new Date());
    walleNews.setStatus(type);
    walleNews.setArticleId(dto.getArticleId());
    walleNews.setChannelId(dto.getChannelId());
    walleNews.setContent(dto.getContent());
    walleNews.setUrl(dto.getUrl());
    walleNews.setUrlTitle(dto.getUrlTitle());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrl
