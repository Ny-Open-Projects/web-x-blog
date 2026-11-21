# 画面线理解：14.优化搜索功能之高亮显示（整合前端实现）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\14.优化搜索功能之高亮显示（整合前端实现）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:11, 00:27, 01:13, 01:21, 01:30, 01:39, 01:57, 02:23, 02:29, 02:41, 02:48, 02:58, 03:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:09:38

1) 这一组画面整体在讲一个房屋租赁信息搜索系统的前端页面展示与后端搜索服务实现。

2) 按时间顺序列出每张画面的要点：
画面1：展示《讲义.pdf》文档目录，内容包含“2、开发搜索接口”、“3、整合前端开发”、“4、优化搜索功能”等章节。
画面2：前端页面展示房屋列表，右侧开发者工具显示HTML模板和JavaScript构建信息。
画面3：前端页面展示房屋列表，右侧开发者工具显示HTML模板和JavaScript构建信息。
画面4：IDE中打开搜索栏组件文件，展示React组件代码，包含`props.searchData.map`和`<Item.Image>`等结构。
画面5：IDE中打开搜索栏组件文件，展示React组件代码，光标位于`<Item.Header>`标签内。
画面6：IDE中打开搜索栏组件文件，展示React组件代码，光标位于`<Item.Meta>`标签内。
画面7：前端页面展示搜索框，输入“d”，右侧开发者工具显示HTML模板和JavaScript构建信息。
画面8：IDE中打开`search.css`文件，光标位于`house-title`样式定义处。
画面9：前端页面展示房屋列表，右侧开发者工具显示HTML模板和JavaScript构建信息。
画面10：展示《讲义.pdf》文档目录，内容包含“2、开发搜索接口”、“3、整合前端开发”、“4、优化搜索功能”等章节。
画面11：IDE中打开`SearchService.java`文件，展示Elasticsearch搜索服务代码，包含`AggregatedPage<HouseData>`和`FieldUtils.writeField`等。
画面12：IDE中打开`SearchService.java`文件，展示Elasticsearch搜索服务代码，光标位于`withQuery`方法调用处。
画面13：IDE中打开`SearchService.java`文件，展示Elasticsearch搜索服务代码，光标位于`for (Map.Entry<String, Object> entry : searchHit.getSourceAsMap())`循环体。
画面14：IDE中打开`SearchService.java`文件，展示Elasticsearch搜索服务代码，光标位于`SearchQuery searchQuery = new NativeSearchQueryBuilder()`行。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```jsx
h-bar>
.is.hideSearchBar name = 'angle left' size = 'large'/>
search-bar-content>
ivided unstackable
props.searchData.map(item => {
  return (
    <Item.Image
      src={https://itcast-haoke.oss-cn-qingdao.aliyuncs.com/lj/" + item.id + ".jpg">
    <Item.Content>
      <Item.Header><div className='house-title'>{item.title}</div></Item.Header>
      <span className='cinema'>
        {item.orientation}/{item.houseType}</span>
      <Item.Meta>
      <Item.Description>
        上海
      </Item.Description>
      <Item.Description>{item.rent}</Item.Description>
    </Item.Content>
  )
})
```

画面5：
```jsx
h-bar>
.is.hideSearchBar name = 'angle left' size = 'large'/>
search-bar-content>
ivided unstackable
props.searchData.map(item => {
  return (
    <Item.Image
      src={https://itcast-haoke.oss-cn-qingdao.aliyuncs.com/lj/" + item.id + ".jpg">
    <Item.Content>
      <Item.Header><div className='house-title' dangerouslySetInnerHTML={{ __html: item.title }}></div></Item.Header>
      <span className='cinema'>
        {item.orientation}/{item.houseType}</span>
      <Item.Meta>
      <Item.Description>
        上海
      </Item.Description>
      <Item.Description>{item.rent}</Item.Description>
    </Item.Content>
  )
})
```

画面6：
```jsx
h-bar>
.is.hideSearchBar name = 'angle left' size = 'large'/>
search-bar-content>
ivided unstackable
.searchData.map(item => {
  return (
    <Item.Image
      src={https://itcast-haoke.oss-cn-qingdao.aliyuncs.com/lj/" + item.id + ".jpg">
    <Item.Content>
      <Item.Header><div className='house-title' dangerouslySetInnerHTML={{ __html: item.title }}></div></Item.Header>
      <span className='cinema'>
        {item.orientation}/{item.houseType}</span>
      <Item.Meta>
      <Item.Description>
        上海
      </Item.Description>
      <Item.Description>{item.rent}</Item.Description>
    </Item.Content>
  )
})
```

画面8：
```css
.house-title{
  overflow: hidden;
  white-space: nowrap;
}
```

画面11：
```java
@Override
public <T> AggregatedPage<T> mapResults(SearchResponse response, Class<T> clazz) {
  if (response.getHits().totalHits == 0) {
    return new AggregatedPageImpl<>(Collections.emptyList(), pageable,
        response.getHits().totalHits);
  }
  List<T> list = new ArrayList<>();
  for (SearchHit searchHit : response.getHits().getHits()) {
    T obj = (T) ReflectUtils.newInstance(clazz);
    try {
      FieldUtils.writeField(obj, fieldName, searchHit.getId(),
          true);
    } catch (IllegalAccessException e) {
      e.printStackTrace();
    }
  }
  return new AggregatedPageImpl<>(list, pageable, response.getHits().totalHits);
}
```

画面12：
```java
@Override
public <T> AggregatedPage<T> mapResults(SearchResponse response, Class<T> clazz) {
  if (response.getHits().totalHits == 0) {
    return new AggregatedPageImpl<>(Collections.emptyList(), pageable,
        response.getHits().totalHits);
  }
  List<T> list = new ArrayList<>();
  for (SearchHit searchHit : response.getHits().getHits()) {
    T obj = (T) ReflectUtils.newInstance(clazz);
    try {
      FieldUtils.writeField(obj, fieldName, searchHit.getId(),
          true);
    } catch (IllegalAccessException e) {
      e.printStackTrace();
    }
  }
  return new AggregatedPageImpl<>(list, pageable, response.getHits().totalHits);
}
```

画面13：
```java
for (Map.Entry<String, Object> entry : searchHit.getSourceAsMap()) {
  Field field = FieldUtils.getField(clazz, entry.getKey(), force);
  if (null == field) {
    continue;
  }
  try {
    FieldUtils.writeField(obj, entry.getKey(), entry.getValue());
  } catch (IllegalAccessException e) {
    e.printStackTrace();
  }
}
for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields()) {
  StringBuilder sb = new StringBuilder();
  Text[] fragments = entry.getValue().getFragments();
  for (Text fragment : fragments) {
    sb.append(fragment.toString());
  }
  // 写入高亮的内容
}
```

画面14：
```java
SearchQuery searchQuery = new NativeSearchQueryBuilder()
  .withQuery(QueryBuilders.matchQuery(name, title)
    .operator(Operator.AND)) // match查询
  .withPageable(pageRequest)
  .withHighlightFields(new HighlightBuilder.Field(name)) // 设置高亮
  .build();
AggregatedPage<HouseData> housePage = this.elasticsearchTemplate.queryForPage(searchQuery,
  HouseData.class, new SearchResultMapper() {
    @Override
    public <T> AggregatedPage<T> mapResults(SearchResponse response, Class<T> clazz) {
      if (response.getHits().totalHits == 0) {
        return new AggregatedPageImpl<>(Collections.emptyList(), pageable,
          response.getHits().totalHits);
      }
      List<T> list = new ArrayList<>();
      for (SearchHit searchHit : response.getHits().getHits()) {
        T obj = (T) ReflectUtils.newInstance(clazz);
        try {
          FieldUtils.writeField(obj, fieldName, searchHit.getId(),
            true);
        } catch (IllegalAccessException e) {
          e.printStackTrace();
        }
      }
      return new AggregatedPageImpl<>(list, pageable, response.getHits().totalHits);
    }
  });
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
