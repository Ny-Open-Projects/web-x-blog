# 18.热词搜索之具体实现

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\18.热词搜索之具体实现【海量资源尽在 ubkz.com】.mp4
- 时长 17分4秒（音频 1024s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下后台的具体的实现那么实现起来呢相对就比较容易了那么我们需要解决关键问题就是在Redis中我们该如何去做一个数据的一个存储那么其实我们在学习Redis的时候也知道那么Redis呢它有很多的数据结构对不对那么我们在这选用的是一个叫Reset就是我们的一个Sorted Set就可排序的这样的一个结合那么这个是不是我们Set的这个结合
[00:29] 对吧它有很多的一些这个元素很多元素那么来看一下大概我们简单的来去说一下那么比如说我们去把它去描一下有很多这样的元素那么这些元素呢它呢我们都会给它对应一个什么它的一个得分会对应的这样的一个得分那么我们去来画一下这个它的一个得分比如说它是有什么呢五分那么下面呢比如说再来一个比如说这个呢有
[01:00] 这个有两分这个比如说我们写这两分那么我们是不是就可以按照这样的一个方式去做一个按照分数的排序的方式给它去做一个这样的处理那么就是这样的一个实现了它的一个基本的一个原理是这样的好那么下面我们就动手来去写一下这个逻辑其实我们动手去实现的逻辑就比较简单了那么我们只需要在我们的Controller里面做处理就可以了找到那个search Controller然后这个里面我们去输入一个叫做redis
[01:30] ReadyS template这个模板然后呢把它注进来那么注进来之后啊那么我们就需要去操作了那么怎么样操作呢那么在这个里面呢我们是不是先要去把它写进去对吧先写进去那么怎么写呢那么我们是不是应该this.readystemplate点来一个ops for什么呢zset就是可排序的这个set然后呢去做一个这个and添加
[02:00] 看到按的里面是不是有三个内容一个是key一个是value一个是double的一个score就它的一个得分那么我们是不是可以看作是key就是我们的一个统一的key然后object value就是我们可以把它作为是我们的一个搜索关键字然后得分就是它的一个数量这样的话是不是就可以实现那么add然后首先第一个是一个key那么我们在上面来定义一个key就比如说就叫
[02:30] 然后叫readist key它就等于比如说我们就这么来写就叫hawk然后叫hawk word或者叫hawk search这个都行大家可以随意去定义就行这个随便只要你是一个字符创就可以了然后第一个key就是它第二个就是我们的搜索的关键字那就这个keyword第一第二个就是它第三个就是我们的一个
[02:58] 拿到的一个结果那么这个结果在哪里我们是不是需要先去拿到结果再去做这样的一个逻辑操作那么拿到这个结果把它的结果我们去获取一下叫search然后最后return好那么在这个search中是不是我们应该拿到它的一个数量要注意在这个位置所填的是它的数据条数并不是页数所以我们还需要处理一下那么在这个位置通过search拿到的是一个total page
[03:28] 那么total bit怎么去得到我们的一个总的一个这个数量呢是不是需要计算一下来一个count吧等于什么呢等于是不是我们的一个数据的页数乘以我们的每页的条数再加上当前查询到的一个数据那么是不是这样的一个逻辑啊比如说它有10页对吧10页那么我们就去比如它有10页的这个数据
[03:57] 那么我们就去乘以它的每页的一个数量然后再去加上它这一页的数据是不是就可以了当然我们是需要先去配置需要简易把前面这一页给它先减掉因为最后一页可能并不满一页有可能这样一个情况所以我们应该是它简易对吧然后再去简易之后然后再去乘以
[04:24] 我们来也要写一下他去乘以数量数量是不是在我们刚刚这个Service里面是我们定义了一个ros这个应该还有印象有个ros然后注意然后我们再去加所以呢加我们的这个叫search.getlist.set再去拿他的一个这样的一个加他的一个这样的一个数字才可以
[04:52] 那么我们把这con就给他传递过去了但是要注意这个里面还有一个小的一个问题或者小的一个bug我们一起来看一下什么问题是在这个位置就是那么如果查询到的页数是1的话对吧是不是就是1.1这个没有问题如果是0的话0.1变成-1了负数显然是不对的所以这个我们需要把它去处理一下我们要保证它最大是1所以通过max.max然后一个是它一个是1
[05:22] 就是我们需要得到一个最大数是1的这样的一个数字这样可以保证我们最小可以得到是1对吧那么如果它大于1如果它大于1的话那么就选用它如果它小于1的话那就选用这1就没有问题了这样的话就可以保证没有问题好那么我们这样的话是不是就已经把我们这个数据是不是就已经写入到理解中了那么其实我们就已经完成了上面所说的这个逻辑了
[05:49] 对不对这个逻辑就搞定了那么下面我们来看一下这个逻辑这个逻辑变得就更加的简单了你只需要记一个日志就可以了因为后面我们再去做处理对不对那么记日志我们先把日志先给他记一下那么写一个private然后来一个static然后final然后来一个loggerlogger在这然后logger等于叫做loggerlog factory
[06:19] 然后点getlogger然后是searchercontroller.classok好这样的话得到一个日志然后下面我们在这个位置是不是就可以去记录通过info这个级别去做一个记录比如说记录什么来一个叫做search因为我们要给一些标识这样的话我们后续在处理的时候是不是就比较方便了比如说我们叫搜索关键字为什么加一个为keyword
[06:48] 然后呢再加一个什么呢再加一个多号加个多号然后呢这个数量为多少再加一个content就这样的意思啊就是说那么搜索关键字是这个它的数量是多少那么这样的话我们是不是就可以记录到日志里面去然后呢我们后续呢就可以去日中是不是做一些这个处理啊那么我们目前呢是不是就已经实现了实现了这个逻辑
[07:15] 对吧以及这个逻辑那么这个是不是查询是不是还没有做那我们再来去做一个这个查询那么查询是不是就需要在我们的这个前面去做一个查询那么查询的结果放哪里这也是一个问题了那么查询的结果我们是不是就有必要是不是把它丢到我们这个里面来对吧那么我们在这个里面再扩展一下扩展一个叫做private再扩展一个叫什么
[07:44] private然后来一个set来的set然后写一个street然后这里面我们去写一个叫hot那么word是热词热词好那么当我们写完之后来看一下那么在这个里面有没有问题它是不是有点问题了是不是少最后一个对吧热词我们就给它设置为num好那么设置为它然后我们再回到我们刚刚所写的Controller中
[08:13] 那么在control中就需要做这样的一个处理了给他添加这个热词那么首先需要判断一下就是说我们需不需要去查询热词那么就是我们前面所说的这个逻辑做一个判断怎么判断是不是就是通过这个设施这个结果点get这个page如果它小于等于1的话那么是不是就需要查询那如果是大于1的话就不用去查询了对吧
[08:40] 那么我们的一个需求定义是这样的看一下是不是只有一页的时候在显示OK或者是没有结果的时候没有结果它的配置肯定也是小于等于1的好那么我们这个位置去查询怎么查是不是通过this.readystamplet.然后ops reset然后再去做一个首先需要做一个反转反转就是按照我们的一个得分从大到小让着去拿然后start和一个end
[09:10] 就可以了那么我们来看一下那我们要去拿的呢就是这个readysql然后呢还有一个0还有个就是4因为我们要拿前几个呢拿前五个这个就拿到前五个拿到他的一个这个结果set然后呢我们再把它丢到这个search里面去点set好那么这样的话是不是我们就把它保存进去了那么要注意拿的前五条呢就是0到4
[09:39] 0到4下标从0开始OK好嘞那么现在我们是不是已经就实现了这个逻辑看一下这个逻辑是不是也搞定了这个是不是也搞定了这个也搞定大家这个我们只搞定一半好那么接下来我们是不是就可以来测试一下了对不对测试一下好那么我们是不是应该把我们这个服务重启一下重启一下看效果走好那么现在我们就跑起来了我们来做个测试当然我们为了测试我们
[10:10] 去这样吧我们就直接来测直接来测那么我们去还是去做一个查询这样的话测试效果应会比较明显一点把这个先清掉然后我们去搜索也比如说搜索1那么看一下1的搜索它应该是有缓存应该是有缓存可能结果中并没有返回这个发现它的返回是闹了那么我们这样搜索111然后来看一下
[10:38] 那么搜索这个三个一的时候会发现结果是不是只有一条那么结果只有一条的话发现你看这个结果是不是已经返回了搜索一搜索D是最多的那我们可以再去尝试的去搜索比如说搜索这个小区小区那么结果也是比较多的是吧那么能不能作为一个热词的返回呢我们再去搜一个一那么来看一下这个结果那么你可以看到这小区是不是也就能够显示出来了OK就是这样的一个
[11:08] 效果那么接下来我们就需要整合我们的前端把它的结果给它展现出来那么前端怎么去整合我们来看一下我们需要首先需要给我们srcbar去添加这么几个两个组件一个是label一个是container就是我们容器然后我们去找到我们的一个这个解死在这然后在这个里面做一些处理我们来看一下需要怎么去做
[11:36] 那么首先我们是需要给它去添加一个在我们这个搜索这个下面来看一下在我们这个搜索这个位置在搜索这个下面去拷贝一下那么先拷过来再说那么拷贝到这那么我们去格式化格式化也不管用那么我们还这样手动去格式化一下那么在这个位置我们需要判断一下
[12:04] 如果我们这个propos有有他的话那么才会显示没有的话就不做显示了那么如果有的话那就去给他去做一个便利然后去通过一个label编签标签去做一个显示就OK了那么这个hotword他是不是又需要通过这个叫我们这个home.js是不是传递过来那么怎么样传递呢他是不是又需要通过下面这个位置又需要引入这个位置去做一个传递那就在这
[12:34] 它等于一个hotword那么这个从哪里来呢是不是还是通过state来对吧点hotword那么state首先还是需要给它一个初始化的值那么前面走找到初始化的位置然后来一个它那么hotword它本身也是个素组所以初始化就是一个素组好搞定
[13:03] 这个就搞定了然后下面我们来看一下如果说我们的这个search结束之后搜索到结果中有hotword的话那么我们是不是就给他去做一个这个数据的一个写入写入之后是不是他就能够传递到我们这个里面去对吧我们这个search bar里面那么传递进去之后就可以去显示出来了应该没有问题看一下这个位置去传递应该没有问题
[13:33] 好那么传递过来这样的话应该就没有问题了看一下简易那么传递过来没有问题然后我们的home.js里面的一个实现是在这个位置你看传递一个传递一个这个叫hotword没有问题没有问题的这个地方去做一个传递然后这个位置也没有问题也没有问题
[13:59] 好那么我们就再来去测试一下看它会怎么样好然后我们再来看一下效果然后我们在这个位置去搜索一个比如说搜索一个1111的时候你发现这个效果是不是就出来了对吧1111的时候那么他说建议你使用它那么现在我们其实要做的事情是点击我们这个label这个标签对吧一点击但现在我们肯定会有点问题就是我们没有给他添加事件对吧那我们来找到我们的这个
[14:29] 叫做searchbar然后呢这个里面呢它有一个这个unclick事件这个我们还没有我们来找一下这个unclick事件那么我们来找一下这个事件是在上面这个位置就是这个是它把这个copy过来然后呢我们考到这就是我们去处理我们那个hot这个热搜索那么在处理热搜索的时候呢也是通过这个search page去做一个查询那通过传递一个value
[14:58] 然后通过一个value去传递我们的点击的值传递过去然后做一个搜索来看一下这个效果你搜这么多我点击小区走你会发现什么是不是已经出现了小区关键字的一个搜索但是现在还是有个问题就是在这个位置它显示的并没有显示我们热词的词它显示的还是原来词并没有改变
[15:24] 那么这个怎么做呢我们还是需要回到home这个里面来这个稍微有点麻烦了就是需要这么来做就是我们还是拿到这个search keyword然后呢我们需要给它做一个初始化就是我们那个input的一个标签做一个初始化是在这个位置然后做一个value等于this.state.一个他好那我们来看一下这个效果它会怎么样呢等待它的一个刷新
[15:52] 然后我们来看一下结果那么在这个里面搜索1123我们随便搜一点那么可以看到这个时候结果是不是比较少那么首先我们这个效果是不是已经出来了没有问题当我点击小区的时候来看一下你会发现上面这个内容是不是也跟着去做了一个改变那为什么它会改变我们简单说一下就是在设置吧里面是不是我们去传入了这个内容到这对吧然后在我们的这个home.js里面它就会去做这样的一个执行
[16:22] 往上面走是在过了就是在这个查询在这个里面设置这个里面然后他就会将这个搜索的关键字是不是写入到我们States中然后States的发生变化当然对应的他是不是也就发生了变化了OK那么到这里我们基本上我们这个搜索是不是就能搞定了随便写一些内容比如我们搜索小区这个比较少那么建议你搜索小区1我点击一个小区1这个效果是不是就出来了
[16:52] 好那么这个我们是不是就已经整合了我们的前端是不是已经实现了我们这样的一个效果ok好那么关于这个热词的一个具体的一个实现那我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import cn.itcast.haoke.dubbo.api.Service.SearchService;
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

