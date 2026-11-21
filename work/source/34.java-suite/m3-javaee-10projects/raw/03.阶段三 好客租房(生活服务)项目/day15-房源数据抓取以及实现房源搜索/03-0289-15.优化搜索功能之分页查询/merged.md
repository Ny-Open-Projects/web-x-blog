# 15.优化搜索功能之分页查询

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\15.优化搜索功能之分页查询【海量资源尽在 ubkz.com】.mp4
- 时长 9分23秒（音频 564s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来去添加这个分页那么首先我们需要添加一个分页的一个组件那么我们来添加一下那么拷贝一下这个分页组件然后呢我们去进入这个srcbar那么在这个里面去添加一下然后呢我们在这个item这个后面再去更一个这个pager这个组件然后呢我们导入进来之后那么我们需要需要呢在我们的这个位置去做一些这个处理我们先来
[00:29] 看一下吧它需要的是在我们去显示的位置就是我们分叶这个组件它显示在哪里呢我们看一下它应该显示在是不是显示的可以显示在这个位置就是我们的这个就是回退的这样一个图标这个位置那么我们把它显示出来那么怎么样去显示呢那么显示的其实我们会有一个逻辑会有逻辑什么逻辑呢就是
[00:55] 什么时候我们会显示我们的分页的一个组件就是当我们的这个页数它大于1的时候是不是才有必要去显示分页那么如果你的这个结果数它只有1这页数只有1的话那么是不是就没有必要去显示这个分页所以我们要基本有这个逻辑的一个判断那么我们来找一个位置就找到我们这个叫search bar里面的来看一下里面的是在icon是不是这个位置
[01:24] 在这个位置吧然后呢我们去显示一个分页那么在这个里面因为有逻辑判断嘛所以我们要去写一些相关的一些这个代码那么我们去判断一下这个this.propos中的total page然后呢如果如果我们来看一下先把这个写完啊那么如果它是大于1的话那么就显示如果不是的话那就说呢
[01:52] 那么prop使用的totalPager这个又从哪里来呢是不是显然又是从前面的home.js中是不是来的那么我们又要找到前面我们的这个home.js在这在这那么我还是加到这个位置来吧它是不是就等于一个totalPager那么它显然肯定也是要去通过state去拿到点totalPager那么这个totalPager我们去是不是还需要在我们前面states中去做一个初始化
[02:22] 找一下找到这个位置就刚刚我们初始化这个位置然后去给他去初始化一下然后默认给他设置为0然后total page那么这个值在哪里做一个改变是不是在我们查询完数据查询完数据之后是不是做一个改变那么在这个里面我们结果中式来看一下结果中式就包含了一个total page所以说我们需要在这个位置逗号来一个total page冒号然后date点
[02:52] TotalBase,好那么这样的话我们是不是就完成数据的一个变更那么以及数据的一个传递它就会传递到我们这个searchbar里面然后在这个里面我们就是判断如果大于一的话那么就有必要去显示我们的这个分页这个组件那么把这个分页组件的内容我们拷贝过来然后还有这个网站ecoOK好那么这样的话是不是我们就做了这样的一个判断那么默认页数是一
[03:21] 然后首页第一页Fast和Last我们没有然后TotalPages是不是就是刚刚我们传入TotalPages然后OnPageChange就是我们的数据页面发生变化的时候就点击页数的时候它应该做什么操作那么它的操作我们上面有定义的这样的方法那么把这个方法我们也拷贝过来同样的定义到这个位置那么在这个里面我们就需要去做的事情就是我们去调用Properties中的SearchPages
[03:50] 然后去把这个页数传递回去那么这个searchPager是不是就是我们需要去在我们的这个home.js中去传递的这个searchPager那么又需要把这个参数给他传递过去了再找一下那么在这个位置就是searchPager等于谁我们来看一下讲义那么searchPager它就等于在home里面
[04:17] 那么search page就需要在下面这个位置是不是有一个叫做,看一下,search我看一下叫什么,search bar,search bar然后是它search page你看,search page等于什么的等于这个race点这个searchrace点search那么race点search是就是我们刚刚所写的这个设置这个方法但是大家想一下那么刚刚我们所写的这个方法在这个方法里面我们并没有去处理
[04:46] 并没有去处理我们这个页数是不是并没有处理因为这个页数都是写死的对不对所以我们来看他怎么传递过来的这个地方稍微可能有一点点反数可以看一下就是我们调用这个source page传递两个参数第一个称none第一个none就调用home中的他第一个参数none他为none这个没有关系那第二个参数是第二个参数是这个page那么第二个参数是page那么也就意味着什么也就意味着
[05:14] 我们在这个home这个里面在这个里面是不是就拿到需要拿到一个配置对吧那么是不是怎么拿呢是不是来一个配置等于叫做应该这么写叫date.page如果它要是有这个内容的话因为在我们前面做搜索的时候它是没有这个配置的对吧那么我们把它摸如果有那么就采用
[05:41] 这个date下面的配置如果没有的话那就用什么呢1就这样的一个逻辑这样逻辑所以这个配置我们就应该把它加到这个位置来这个大家能看懂吗ok他就是应该这样去写但是大家要想一下当我点击这个分页的时候那么这个kword这个值它是不是也会丢失对不对也会丢失那么我们应该怎么去做呢那么我们是不是就应该来看一下在这个里面在这个里面
[06:11] 那么想一下应该是这样的在home这个里面那么我们其实是应该去把我们这个就是search就是我们这个keyword我们去记录下来就可以需要记录到我们的就需要记录哪里还是需要记录到我们的states里面这样的话才能够保存下来要不然我们保存不了这个数据那么我们这个里面来一个它那就叫keyword我们叫不叫keyword叫search
[06:42] search keyword好然后呢冒号来一个冒号来一个来一个空字不串吧然后呢当我们去做当我们去做搜索的时候当我们去做搜索的时候呢我们再给它去做一个setthis.叫set stateset state然后呢这个searchsearch keyword那么冒号
[07:12] 那就是刚刚传入的这个value就是这个意思了这个value然后在这个点需要注意一下就当我们做分页的时候刚才我们说这个问题这keyword怎么会丢失那么会丢失怎么办我们就需要还是在这个位置来判断一下如果它传入的这个data value如果有值的话那就使用data.value如果没有的话那就使用我们的stays中的点这个叫search keyword这样的话是不是就没有问题了
[07:40] 对吧OK那么如果你传入那我就使用那么没有传入我就使用我前面的这个保存到我的states中的这个keyword那么这样的话应该就没有问题了好我们再来去测试一下吧看它会怎么样刷新一下刷新然后呢我们来看一下效果那我点输入这个1那么显然可以看到是不是有了一个分页这样的一个分页条然后点击这个页数看它会怎么样走
[08:08] 是不是已经完成了这样的一个分页的效果对吧包括我们这个传递的一个就是我们查询字数还在我们可以去看一下他查询的一个对不对那么查询的一个get请求的keyword我们来看一下keyword没错是1没有问题没有丢失并且页数也改为5可以看一下在右侧这个位置大家去关注一下在这个位置keyword是不是等于1配置等于5那么所以说我们刚刚的这个
[08:37] 说设计这个逻辑呢它是没有问题的比如说我们搜索一下地铁地铁然后呢有这么多然后去走那我们来看一下它的一个搜索的一个结果你看是不是就是一个地铁下面看到吧OK没有任何问题好那么现在呢我们这个是不是我们这个做一个分页那么是不是就已经搞定了对吧就搞定了那么这个代码呢其实就是跟我们讲义中这个代码呢应该是一样的应该是一样的这样的一个代码
[09:07] OK好嘞那么最后测试这个结果呢就是这样的一个测试结果虽然在我们这个位置啊它的这个显示的这个效果会有点有点丑啊但是没关系但是我们这个功能是它是不是已经实现了OK好这个就是给大家所讲的一个分裂的这样的一个效果

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解一个租房网站前端搜索与分页功能的实现，包括分页组件的引入、搜索逻辑、数据加载和热词搜索功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“4.2.1. 添加分页组件”部分，代码中导入了 `Pagination` 组件并定义了 `handlePageChange` 函数，用于处理分页变化。
画面 2: PDF 文档中展示分页组件的配置代码，包括 `defaultActivePage`、`firstItem` 和 `lastItem` 的设置。
画面 3: 在 IntelliJ IDEA 中查看 `searchbar.js` 文件，展示 `SearchBar` 组件的 `render` 方法，其中包含 `this.props.totalPage > 1 ? : null` 条件判断。
画面 4: 在 IntelliJ IDEA 中查看 `home.js` 文件，展示 `state` 中的 `searchBarFlag`、`totalPage` 和 `searchData` 等属性，以及 `render` 方法中的 `onFocus` 事件绑定。
画面 5: 在 IntelliJ IDEA 中查看 `home.js` 文件，展示 `Promise.all` 用于并行加载多个数据（swipe, menu, info, faq, house），并更新 `setState`。
画面 6: PDF 文档中展示分页组件的配置代码，包括 `totalPages` 和 `onPageChange` 的设置。
画面 7: PDF 文档中展示 `home.js` 文件中 `search` 函数的实现，用于处理搜索输入和分页。
画面 8: 在 IntelliJ IDEA 中查看 `home.js` 文件，展示 `switch` 语句中根据不同关键词（租房、海外、问答）跳转到不同页面的逻辑。
画面 9: 在 IntelliJ IDEA 中查看 `home.js` 文件，展示 `search` 函数中 `axios.get` 请求的代码，用于获取搜索结果。
画面 10: 在 IntelliJ IDEA 中查看 `home.js` 文件，展示 `constructor` 中初始化 `state` 的代码，包括 `swipeData`、`menuData`、`infoData`、`faqData`、`searchData` 等。
画面 11: 在 IntelliJ IDEA 中查看 `home.js` 文件，展示 `search` 函数中 `axios.get` 请求的代码，用于获取搜索结果。
画面 12: 在浏览器中查看 `localhost:9000/home` 页面，展示搜索结果列表和分页控件，同时显示开发服务器的 HTML 模板和 JavaScript 代码。
画面 13: PDF 文档中展示 `home.js` 文件中 `search` 函数的完整实现，包括 `setState` 更新搜索结果和分页信息。
画面 14: PDF 文档中展示“5、热词搜索”部分，描述热词搜索的需求和效果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```javascript
import { Icon, Item, Pagination } from 'semantic-ui-React';

handlePageChange = (e, { activePage }) => {
  this.props.searchPage(null);
  page:activePage
};

this.props.totalPage > 1 ? (
  <Pagination
    defaultActivePage={1}
    firstItem={null}
    lastItem={null}
```

画面 2:
```javascript
totalPages={this.props.totalPage}
onPageChange={this.handlePageChange}
```

画面 3:
```javascript
render() {
  return (
    <div className='search-bar'>
      <Icon onClick={this.hideSearchBar} name='angle left' size='large'/>
      {this.props.totalPage > 1 ? : null}
      <div className='search-bar-content'>
        {this.props.searchData.map(item => {
          return (
            <Item key={item.id}>
              <Item.Image
                src="https://itcast-haoke.oss-cn-qingdao.aliyuncs.com/lj/"
              />
              <Item.Content>
```

画面 4:
```javascript
state.mapShowFlag=<MapHouse hideMap={this.hideMap} />:null
state.calcShowFlag=<Calculator hideCalc={this.hideCalc} />:null
state.searchFlag=<SearchBar totalPages={this.state.totalPage} searchData={this.state.searchData} hide={this.hideSearchBar} />
```

画面 5:
```javascript
let house = new Promise(resolve, reject) => {
  axios.get('http://127.0.0.1:18080/mock/index/house').then((data) => {
    resolve(data.data.list);
  });
};

Promise.all([swipe, menu, info, faq, house]).then((result) => {
  this.setState({
    swipeData: result[0],
    menuData: result[1],
    infoData: result[2],
    faqData: result[3],
    houseData: result[4],
    swipeLoading: true,
    menuLoading: true,
    infoLoading: true,
    faqLoading: true,
    houseLoading: true,
    globalLoading: false
  });
```

画面 6:
```javascript
totalPages={this.props.totalPage}
onPageChange={this.handlePageChange}
```

画面 7:
```javascript
--home.js---
search = (event, data) => {
  let value = data.value ? data.value : this.state.searchKeyword;
  let page = data.page ? data.page : 1;
  let _this = this;
  this.searchHandle();
  axios.get('http://127.0.0.1:18080/search?keyWord=' + value + '&page=' + page).then((data) => {
    this.setState({searchData:data.list, totalPage:data.totalPage, searchKeyword:value});
  });
};
```

画面 8:
```javascript
switch (type) {
  case '租房':
    this.props.history.push('/home/list', {query: {name: name, type: 3}});
    break;
  case '海外':
    this.props.history.push('/home/list', {query: {name: name, type: 4}});
    break;
  case '问答':
    this.props.history.push('/home/find', {query: {flag: true}});
    break;
  default:
    break;
}

searchHandle = () => {
  this.setState({
    searchBarFlag: true
  })
}
```

画面 9:
```javascript
render() {
  const swipeLoading = this.state.swipeLoading;
  const swipeData = this.state.swipeData;
  let swipe = null;
  if (swipeLoading) {
    swipe = <Loader />;
  }
```

画面 10:
```javascript
constructor(props) {
  super(props);
  this.state = {
    swipeData: [],
    swipeLoading: false,
    menuData: [],
    menuLoading: false,
    infoData: [],
    infoLoading: false,
    faqData: [],
    faqLoading: false,
    globalLoading: true,
    mapShowFlag: false,
    searchBarFlag: false,
    searchData: [],
    totalPage: 0,
    keyword: ''
  };
}
```

画面 11:
```javascript
search = (event, data) => {
  let value = data.value ? data.value : '';
  let page = data.page ? data.page : 1;
  let _this = this;
  this.searchHandle();
  axios.get('http://127.0.0.1:18080/search?keyWord=' + value + '&page=' + page).then((data) => {
    this.setState({searchData:data.list, totalPage:data.totalPage});
  });
};
```

画面 12:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title></title>
  <link rel="stylesheet" href="https://itcast-haoke.oss-cn-qingdao.aliyuncs.com/lj/">
  <script type="text/javascript" src="static/dist/bundle.js"></script>
</head>
<body>
  <div class="main-content"></div>
  <div class="fix-container"></div>
  <div id="root"></div>
</body>
</html>
```

画面 13:
```javascript
--home.js---
search = (event, data) => {
  let value = data.value ? data.value : this.state.searchKeyword;
  let page = data.page ? data.page : 1;
  let _this = this;
  this.searchHandle();
  axios.get('http://127.0.0.1:18080/search?keyWord=' + value + '&page=' + page).then((data) => {
    this.setState({searchData:data.list, totalPage:data.totalPage, searchKeyword:value});
  });
};

this.state.searchBarFlag = SearchBar hideSearchBar={this.hideSearchBar} searchPage={this.search} totalPage={this.state.totalPage} searchData={this.state.searchData} />
```

画面 14:
```markdown
5、热词搜索
需求：当大数据搜索结果或搜索结果只有一项时，显示搜索热词。最多显示5个热词。
热词：按照用户搜索的关键字以及搜索到的结果数量进行排序，数量越多的越排前面

