# 画面线理解：13.优化搜索功能之高亮显示（采用反射具体代码实现）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\13.优化搜索功能之高亮显示（采用反射具体代码实现）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 03:23, 05:22, 06:42, 08:51, 11:43, 13:26, 14:30, 16:14, 17:15, 18:28, 20:01, 21:07, 22:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:08:53

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Elasticsearch 搜索结果中实现高亮显示功能，主要通过自定义 SearchResultsMapper 类和 FieldUtils 工具类完成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程讲义 PDF 的目录结构，当前章节为“4.1、高亮”，并预览了代码编辑器中的部分代码。
画面 2: 在 SearchService.java 中，使用 NativeSearchQueryBuilder 构建搜索查询，代码中高亮了 AggregatedPageImpl 类型。
画面 3: 在 SearchResultsMapper 类中，定义了 mapResults 方法，用于将搜索响应映射为 AggregatedPage，代码中高亮了 NewInstance 类型的建议。
画面 4: 在 SearchResultsMapper 类中，代码逻辑用于遍历搜索结果，通过反射工具类 ReflectUtils 获取对象字段并写入。
画面 5: 在 SearchResultsMapper 类中，代码逻辑用于遍历搜索结果的源数据（sourceAsMap），并使用 FieldUtils.writeField 方法写入对象字段。
画面 6: 在 SearchResultsMapper 类中，代码逻辑用于处理非英文字段，使用反射获取字段并写入对象。
画面 7: 在 SearchResultsMapper 类中，代码逻辑用于处理高亮字段，使用 StringBuilder 拼接高亮片段。
画面 8: 在 SearchResultsMapper 类中，代码逻辑用于将高亮片段写入对象字段，使用 FieldUtils.writeField 方法。
画面 9: 在 SearchResultsMapper 类中，代码逻辑用于处理高亮字段，使用 StringBuilder 拼接高亮片段。
画面 10: 在 SearchResultsMapper 类中，代码逻辑用于获取对象字段，使用 FieldUtils.getField 方法。
画面 11: 在 SearchResultsMapper 类中，代码逻辑用于处理高亮字段，使用 StringBuilder 拼接高亮片段。
画面 12: 展示 HouseData.java 类的定义，使用 @Document 注解指定索引名和类型。
画面 13: 在 SearchResultsMapper 类中，代码逻辑用于将高亮片段写入对象字段，使用 FieldUtils.writeField 方法。
画面 14: 展示课程讲义 PDF 的目录结构，当前章节为“4.1、高亮”，页面为空白。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
.house-title{
    overflow: hidden;
    white-space: nowrap;
}
```

画面 2:
```java
SearchQuery searchQuery = new NativeSearchQueryBuilder()
        .with()
        .with()
        .build();
AggregatedPage<?> AggregatedPageImpl<...> { ... }
return new AggregatedPageImpl<...>(...);
return new SearchResult(housePage.getTotalPages(), housePage.getContent());
```

画面 3:
```java
HouseData.class, new SearchResultMapper() {
    @Override
    public <T> AggregatedPage<T> mapResults(SearchResponse response, Class<T> clazz) {
        if (response.getHits().totalHits == 0) {
            return new AggregatedPageImpl<>(Collections.emptyList(), pageable,
                    Collections.emptyList(), 0L);
        }
        List<T> list = new ArrayList<>();
        return new AggregatedPageImpl<>(list, pageable, Collections.emptyList(), 0L);
    }
}
```

画面 4:
```java
List<T> result = new ArrayList<>();
if (response.getHits().totalHits == 0) {
    return new AggregatedPageImpl<>(Collections.emptyList(), pageable,
            Collections.emptyList(), 0L);
}
for (SearchHit searchHit : response.getHits()) {
    // 通过反射导入数据到对象中
    T obj = ReflectUtils.newInstance(clazz);
    searchHit.getId(), true);
    try {
        FieldUtils.writeField(obj, entry.getKey(), entry.getValue(), true);
    } catch (IllegalAccessException e) {
        e.printStackTrace();
    }
    Map<String, Object> sourceAsMap = searchHit.getSourceAsMap();
    for (Map.Entry<String, Object> entry : sourceAsMap.entrySet()) {
        Field field = FieldUtils.getField(clazz, entry.getKey(), true);
        if (null == field) {
            continue;
        }
        try {
            FieldUtils.writeField(obj, entry.getKey(), entry.getValue(), true);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }
    }
    list.add(obj);
}
return new SearchResult(housePage.getTotalPages(), housePage.getContent());
```

画面 5:
```java
if (response.getHits().totalHits == 0) {
    return new AggregatedPageImpl<>(Collections.emptyList(), pageable,
            Collections.emptyList(), 0L);
}
List<T> list = new ArrayList<>();
for (SearchHit searchHit : response.getHits()) {
    Object obj = ReflectUtils.newInstance(clazz);
    for (Map.Entry<String, Object> entry : searchHit.getSourceAsMap().entrySet()) {
        Field field = FieldUtils.getField(clazz, entry.getKey(), true);
        if (null == field) {
            continue;
        }
        try {
            FieldUtils.writeField(obj, entry.getKey(), entry.getValue(), true);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }
    }
    list.add(obj);
}
return new SearchResult(housePage.getTotalPages(), housePage.getContent());
```

画面 6:
```java
int
Integer (java.lang)
IllegalAccessError (java.lang)
IllegalArgumentException (java.lang)
IllegalMonitorStateException (java.lang)
IllegalStateException (java.lang)
IllegalThreadStateException (java.lang)
IncompatibleClassChangeError (java.lang)
IndexOutOfBoundsException (java.lang)
```

画面 7:
```java
for (Map.Entry<String, Object> entry : searchHit.getSourceAsMap().entrySet()) {
    try {
        FieldUtils.writeField(obj, entry.getKey(), entry.getValue(), true);
    } catch (IllegalAccessException e) {
        e.printStackTrace();
    }
}
for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields().entrySet()) {
    StringBuilder sb = new StringBuilder();
    for (Text fragment : entry.getValue().getFragments()) {
        sb.append(fragment.toString());
    }
    try {
        FieldUtils.writeField(obj, entry.getKey(), sb.toString(), true);
    } catch (IllegalAccessException e) {
        e.printStackTrace();
    }
    list.add(obj);
}
return new AggregatedPageImpl<>(list, pageable, Collections.emptyList(), 0L);
```

画面 8:
```java
for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields().entrySet()) {
    StringBuilder sb = new StringBuilder();
    for (Text fragment : entry.getValue().getFragments()) {
        sb.append(fragment.toString());
    }
    try {
        FieldUtils.writeField(obj, entry.getKey(), sb.toString(), true);
    } catch (IllegalAccessException e) {
        e.printStackTrace();
    }
    list.add(obj);
}
return new AggregatedPageImpl<>(list, pageable, Collections.emptyList(), 0L);
```

画面 9:
```java
List<T> list = new ArrayList<>();
for (SearchHit searchHit : response.getHits()) {
    // 非英文字段的数据写入
    for (Map.Entry<String, Object> entry : searchHit.getSourceAsMap().entrySet()) {
        try {
            FieldUtils.writeField(obj, entry.getKey(), entry.getValue(), true);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }
    }
    for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields().entrySet()) {
        StringBuilder sb = new StringBuilder();
        for (Text fragment : entry.getValue().getFragments()) {
            sb.append(fragment.toString());
        }
        try {
            FieldUtils.writeField(obj, entry.getKey(), sb.toString(), true);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }
        list.add(obj);
    }
}
return new AggregatedPageImpl<>(list, pageable, Collections.emptyList(), 0L);
```

画面 10:
```java
FieldUtils.getField(Class<?> cla, String fieldName)
FieldUtils.getAllFields(Class<?> cla)
FieldUtils.getDeclaredFields(Class<?> cla)
FieldUtils.getDeclaredField(Class<?> cla, String fieldName)
FieldUtils.getDeclaredField(Class<?> cla, String fieldName, boolean forceAccess)
FieldUtils.getFieldsListWithAnnotation(Class<?> cla, Class<? extends Annotation> annotation)
```

画面 11:
```java
for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields().entrySet()) {
    StringBuilder sb = new StringBuilder();
    for (Text fragment : entry.getValue().getFragments()) {
        sb.append(fragment.toString());
    }
    try {
        FieldUtils.writeField(obj, entry.getKey(), sb.toString(), true);
    } catch (IllegalAccessException e) {
        e.printStackTrace();
    }
    list.add(obj);
}
return new AggregatedPageImpl<>(list, pageable, Collections.emptyList(), 0L);
```

画面 12:
```java
@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(indexName = "haoke", type = "house", createIndex = false)
public class HouseData {
    @Id
    private String id;
    private String title;
    private String rent;
    private String floor;
    private String image;
    private String orientation;
    private String houseType;
    private String rentMethod;
    private String time;
}
```

画面 13:
```java
for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields().entrySet()) {
    StringBuilder sb = new StringBuilder();
    for (Text fragment :
