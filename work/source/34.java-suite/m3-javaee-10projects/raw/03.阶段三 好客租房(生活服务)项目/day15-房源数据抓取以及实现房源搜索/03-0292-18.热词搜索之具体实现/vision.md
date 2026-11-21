# 画面线理解：18.热词搜索之具体实现

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\18.热词搜索之具体实现【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:53, 04:42, 06:18, 07:42, 08:29, 09:33, 10:42, 11:42, 12:48, 14:11, 15:13, 16:14, 16:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:11:52

1) 这一组画面整体在讲什么（一句话）：
演示一个房屋租赁搜索系统的后端 Java 代码实现（使用 Spring Boot 和 Redis）以及前端 React 组件的开发与调试过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示在百度搜索“java”，结果页包含 Java 官网、Java 百度百科、Java SE 下载等链接。
画面 2: IDE 中展示 SearchController.java 代码，定义了 @Autowired RedisTemplate redisTemplate; 和 this.redisTemplate.opsForZSet() 方法。
画面 3: IDE 中展示 SearchController.java 代码，添加了分页逻辑：if (page > 100) { page = 1; }。
画面 4: IDE 中展示 SearchController.java 代码，定义了 @RequestMapping、@RestController、@Autowired 等注解和 Logger、SearchService、RedisTemplate 字段。
画面 5: IDE 中展示 SearchResult.java 代码，定义了 totalPage 和 list 字段。
画面 6: IDE 中展示 SearchController.java 代码，使用 getHotWord() 方法获取热门搜索词并记录到 Redis。
画面 7: IDE 中展示 SearchController.java 代码，使用 reverseRange 方法将热门搜索词按热度逆序排列。
画面 8: 浏览器中展示搜索结果页面，显示“整租-杭州路111弄1居室 4:”等房源信息，同时 Network 面板显示了多个 API 请求。
画面 9: Adobe Reader 中展示 PDF 文档，内容为 React 组件的 Pagination 和 hotWord 显示逻辑。
画面 10: IDE 中展示 searchbar.js 代码，定义了 swipeLoading、menuLoading 等状态和渲染逻辑。
画面 11: 浏览器中展示搜索页面，输入框为空，显示“搜索错误码：”。
画面 12: 浏览器中展示搜索结果页面，显示多个房源信息，如“整租-金平小区精装大三房”等。
画面 13: IDE 中展示 searchbar.js 代码，定义了 handlePageChange 和 handleHotSearch 方法。
画面 14: Adobe Reader 中展示 PDF 文档，内容为 home.js 中的 search 函数，用于处理搜索请求并更新状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@Autowired
private RedisTemplate redisTemplate;
```
画面 3:
```java
if (page > 100) { //防止爬虫抓取过多的数据
    page = 1;
}
```
画面 4:
```java
import cn.itcast.haoke.dubbo.api.service.SearchService;
import cn.itcast.haoke.dubbo.api.vo.SearchResult;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

private static final Logger LOGGER = LoggerFactory.getLogger(SearchController.class);

@Autowired
SearchService searchService;
@Autowired
private RedisTemplate redisTemplate;

@GetMapping("/search")
public SearchResult search(@RequestParam("keyword") String keyword,
                           @RequestParam(value = "page", defaultValue = "1") Integer page) {
```
画面 5:
```java
package cn.itcast.haoke.dubbo.api.vo;

import ...

@Data
@AllArgsConstructor
@NoArgsConstructor
public class SearchResult {
    private Integer totalPage;
    private List<HouseData> list;
```
画面 6:
```java
if (search.getTotalPage() <= 1) {
    this.redisTemplate.opsForZSet().add(redisKey, keyword, _);
    search.getHotWord().set(1);
}
```
画面 7:
```java
if (search.getTotalPage() <= 1) {
    this.redisTemplate.opsForZSet().reverseRange(redisKey, start: 0, end: 4);
    search.getHotWord().set(1);
}
```
画面 9:
```jsx
<Pagination
    defaultActivePage={1}
    firstItem={null}
    lastItem={null}
    totalPages={this.props.totalPage}
    onPageChange={this.handlePageChange}
/>
```
画面 10:
```jsx
const swipeLoading = this.state.swipeLoading;
const swipeData = this.state.swipeData;
if (swipe !== null) {
    swipe = <ImageGallery
        preventDefaultTouchmoveEvent={true}
        autoPlay={true}
        disableSwipe={false}
        showThumbnails={false}
        items={swipeData} />
}
```
画面 13:
```jsx
handlePageChange = (e, {activePage}) => {
    this.props.searchPage(null, {
        page: activePage
    });
};

handleHotSearch = (e, data) => {
    this.props.searchPage(null, {value: data.children});
};
```
画面 14:
```js
search = (event, data) => {
    let value = data.value; this.state.searchKeyword;
    let page = data.page; page = 1;
    let _this = this;
    this.setState({
        searchKeyword: value
    });
    this._searchHandle();
    axios.get('http://127.0.0.1:18080/search?keyword=' + value + '&page=' + page).then((data) => {
        _this.setState({searchData: data.list, hotWord: data.hotWord, totalPage: data.totalPage});
    });
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 9: PDF 文档中包含 React 组件的 Pagination 和 hotWord 显示逻辑，其中 Pagination 组件的属性包括 defaultActivePage、firstItem、lastItem、totalPages、onPageChange。
画面 14: PDF 文档中包含 home.js 中的 search 函数，用于处理搜索请求并更新状态。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
