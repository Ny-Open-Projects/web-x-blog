# 画面线理解：15.优化搜索功能之分页查询

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\15.优化搜索功能之分页查询【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:50, 01:49, 02:15, 02:39, 03:36, 04:14, 04:41, 05:31, 06:37, 07:32, 08:10, 08:57, 09:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:10:30

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
import { Icon, Item, Pagination } from 'semantic-ui-react';

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
