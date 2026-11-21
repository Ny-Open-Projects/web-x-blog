# 14.优化搜索功能之高亮显示（整合前端实现）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\14.优化搜索功能之高亮显示（整合前端实现）【海量资源尽在 ubkz.com】.mp4
- 时长 3分10秒（音频 190s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着上一个视频呢我们继续啊那么我们还是去把它整合到前端的去做一个测试那么最终效果呢就是可以看到啊来看一下效果先看效果吧在这个里面我们可以去刷新一下然后呢来看一下然后我们在这个位置去搜索一下比如说我们搜索这个东方东方好,那么它的一个结果这个应该是结果被缓存了比如说来一个地铁
[00:28] 好那么可以看到是不是有这样的一个效果那么会发现我们其实已经返回了这个高亮只是呢在我们前端的并没有把它显示出来那么这个应该怎么去做呢那么我们就应该去来看一下我们这个React然后呢这个使用的一个UI组件它应该去这样去做那么它需要呢在这个去通过这样的一个方式就是因的html这种方式去通过下滑线两个下滑线html
[00:58] 去获取这个值才能够去把在我们返回的内容中的html作为一个标签去做一个显示就是稍显繁琐一点那么我们把这个拷贝一下然后去进入到我们的一个标题里面找一下这个标题那么标题标题就我看一下没错就在在这个位置那么把它直接覆盖掉就好了好那么我们来把它就我们把这个
[01:28] 去整理一下好那么这样的话呢应该就OK了好保存那么刷新我们来看一下这个效果看它会怎么样那么我们还是搜索这个地铁地铁那么你会发现呢它其实已经有点变化了对吧这个地铁这个好像这个字是不是有点倾斜了对吧斜体啊其实它默认的就是斜体那么需要接下来我们就需要去修改它的一个样式那我们去在我们的刚刚所写的这个
[01:57] 叫设置点css下面再加一个样式就是这个host title下面em给它添加一个这个样式采用一个默认就是字体样式采用默认然后呢颜色设置为一个red就是一个红色来看一下这个效果效果是不是就出来了那么这个是不是就是我们所期望是不是看到的一个这个效果是吧所有包含这个地铁的关键字的作为高亮显示那么这样的话我们是不是就已经实现了对吧来一个地铁1会怎么样呢地铁1号线地铁1
[02:26] OK好没有问题然后呢我们下面来看一下结果是不是就这样的一个这个效果呀好那么这个就是我们去整合前端的去实现的一个高亮显示那么在我们的高亮显示中啊其实它的一个难点或者说重点内容的其实就是我们刚刚所写的这么一堆这个代码就是在我们在查询结果之后面啊然后呢去自己去分装的这个结果自己分装这个结果然后呢
[02:54] 去处理非高量之段以及高量之段然后处理完成之后再把它填回到对象中然后最后做一个返回就这样的一个逻辑那么希望大家把这个代码能够去自己去编写一下OK好那么关于这高量的实现我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

