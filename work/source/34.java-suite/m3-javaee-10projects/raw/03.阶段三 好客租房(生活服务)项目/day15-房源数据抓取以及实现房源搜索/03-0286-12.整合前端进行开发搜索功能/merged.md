# 12.整合前端进行开发搜索功能

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\12.整合前端进行开发搜索功能【海量资源尽在 ubkz.com】.mp4
- 时长 16分14秒（音频 974s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么接下来呢我们来看一下整合前端的开发那么前面呢我们已经完成了接口的开发所以接下来呢我们就应该去整合我们的前端去做开发那么首先我们来看一下效果那么效果呢是在我们的首页的上方呢会有一个这样的一个搜索框然后呢在这个搜索框内部呢去输入我们一些关键字然后呢下面呢就可以去
[00:24] 显示出我们所匹配的一些房源的一些数据大概就是这样的一个效果那我们参考我们讲义的这个代码吧去做一些这个实现因为这个里面贴的一个代码比较多那我们需要一点一点去分析去做那么首先我们来看一下在我们现有的我们实现的一个这样的一个逻辑中它是实现了什么样的功能可以看到点击这个位置
[00:47] 诶注意点击这个搜索框是会出现一个这样的一个页面那么当我离开的话是不是就这个页面也会这个消失那么呃这样的话是不是我们可以在上面这个位置是不是去做一个搜索那么首先呢我们先找到这个位置然后呢在这个位置呢逐步的去做啊逐步的去写一些这个代码啊那我们来找到我们所对应的这个代码的位置啊那么这个代码的位置呢呃它呢我们找到谁找到home啊在home呢我们home这个里面呢我们会
[01:17] 找到这个runner这个里面然后呢在下面的是在往下面走在这个位置啊在这个位置呢会对我们这个搜索searchbar然后呢去做一个这样的一个呃引用啊这个searchbar呢它呢是在这个位置啊注意你看是在这个位置啊这个导入进来也就是说它呢导入到这啊哎OK呃然后呢我们其实重点改造的内容是不是就是在这个位置啊包括还有它啊然后呢呃需要我们看到的是
[01:45] 这个只是就是这个是这个searchbar它是它是我们点击这个之后所显示的这个空白目前空白这样的一个内容那么当然我们可以测试一下比如说我在searchbar里面随便写一个ok我写一个ok保存一下然后我们等待它刷新一下等待刷新之后我们就来去点一下它你会发现这个里面是不是就这个ok是不是就出来了那么也就是说我们所看到searchbar这个gest中的内容
[02:14] 它仅仅是我们在点击这个搜索框之后显示的空白的这个这个页面然后呢我们其实还有一个重点内容是比较关注于这个输入框啊对不对好那我们来看一下这个里面的它的实现啊那么在这个输入框的下面这个位置有一个input啊有一个这个input然后呢它呢指定了有两个事件一个就是unblueunblue呢就是当我们去这个离开这个焦点的时候那这个呢后面是
[02:42] 去获取焦点那么当我们去获取了焦点的时候他做一件事情就是去做设置一个state中的这个标识让他设置为2然后如果他为设置为2的话那么所对应的我们这个位置他就会去把这个source bar显示出来那么如果是unblow就是我们的焦点所离开的话那么就给他设置一个这个flag是一个force
[03:07] 那么这样的话呢所对应的啊所对应的我们所看到的这个位置呢他呢就会做一个隐藏所以呢就看到我们这样的效果就是我鼠标移到这个里面来哎显示然后呢移走然后呢就隐藏掉其实呢这个呢是就是我们这个操作啊它不太去能够符合我们的一个实际的一个需求为什么大家想一下如果我在这个位置输入
[03:31] 输入内容之后呢我希望下面是不是显示出来那么我肯定要去点击对吧我一点这个里面的内容是不是就代表着我上面的这个这个输入框它是不是就失去我这个焦点那么失去我这个焦点它是不是立刻就隐藏掉了所以我们就没有办法去点到这个里面内容那么这个操作显然是不合适的所以我们需要对它做一些这个改造那么我们来看一下怎么样去做改造好那么我们还是找到关键的一个代码的位置
[04:00] 那么关键代码位置呢我们往下面找啊呃是在是在哪里呢呃是在这个位置啊是不是就在srcbar这个位置啊呃一个是在这里那么一个呢就是下面这个input啊那么可以看到这个位置呢我先吧呃他两个先呃先注释掉然后呢这个里面呢我们其实要去接收的一个啊接收的一个这个事件呢我们应该叫一个onchange这样的一个事件就是当我们在当我们这个
[04:29] 输入框里面内容发生改变的时候我再去触发这样的一个事件再去做一些这个搜索那么当我搜索结束之后呢我再把那个设置办案给它显示出来对吧显示出来之后呢然后在里面把内容显示出来这个才是比较符合我们的一个正常的一个使用所以说呢我们就先把它原来这个代码呢我们简单做一些这个改造因为这个是前端所以直接去写这样的代码那么咱们把这两个就拿走吧
[04:58] 拿到就拿到上面来然后呢我们先给他去做一个注射好嘞那么然后呢我们给他添加一个什么呢添加一个我们这个onchange这样的一个事件把它呢丢过来然后呢我们把它丢到哪里呢这个在这儿啊丢到这个位置来onchange这个事件OK好那么这个搞定之后呢我们可以看到他调用的是this.search
[05:23] 然后是改变它类似的一个指线那么下面我们就是不是需要去把这个设置这个方法去做一个定义那么我们是不是就需要在上面这个位置去定义一个设置这个方法那么咱们就把它就丢到这吧然后我们来看一下讲义中的这个设置这个方法的一个定义它在上面会有一个设置方法的一个定义我们来找一下那么是再再往再往上面一点再往上面一点
[05:51] 这有一个这个search这个方法定义把这个search拷贝过来那么在这里那么在这个search这个是应该是格式的问题把它往上面一丢好这样的话应该就OK了那我们来看一下这个search的这个操作那么search这个操作呢是首先我们去拿到我们这个data的一个value拿到data的一个value那么有了它之后呢就是这个value呢其实就拿到我们输入框的这个内容那么下面这个呢是拿到一个当前ZS这个对象
[06:20] 然后这个操作注意这个操作是不是刚刚我们所看到一个操作就是我们去把空白的给它显示出来然后我们再去做一个我们请求对吧请求然后去拿到数据拿到数据之后我们会把这个数据注意你看是拿到 date 数据那么拿到 date 数据之后我们拿到它一个 date.list然后会把它丢到一个我们的 stash 中的一个 search date
[06:45] 丢到这个里面来然后我们是不是就可以把这个suggest去传递到我们设置吧里面这不传在设置吧里面然后在这个里面去做一些便利是不是就可以了所以我们需要做这样的一个操作那么首先我们需要在我们的states中找一下states在最上面的初始化这个位置那么我先要给它做一个初始化就是我们给它设置什么冒号设置一个
[07:11] 它的默认值是一个空的一个宿主然后我们是不是就需要去给它去给这个srcbar里面去做一个传递对吧那么给它传递过去那么怎么样传递呢我们来找一下那么是不是就可以在这个位置去传递一下叫什么呢叫做srcdate然后等于this.state.srcdate那么这个数据什么时候会发生变更呢是不是就是在我们的这个数据加载完成查询加载完成之后
[07:41] 是不是就会去拿到这个值去在这个里面做一个变更ok好那么这样的话我们是不是就把这个数据是不是就传递到我们社区吧里面了那么接下来我们就需要在社区吧里面去显示出我们这个里面的一些信息那么我们来看一下这个应该怎么去做那么我们找到我们社区吧我们来看一下往下面走这个社区吧那么在这个社区吧里面我们把这个代码我看一下把这个代码我们还是
[08:10] 贴过来吧看一下这个里面那么首先呢他去首先他去引入一些这个组件咱们把这个组件先拿过来然后呢往这这样一丢好把这两个组件拿过来然后呢在这个下面就是在OK的这个位置就是contact的这个位置在这个位置在这个位置呢我们去写一个item group这样的一个这样的一个组件然后呢我们还是拷贝一下吧往这一拷贝
[08:38] 然后呢下面呢这个把它也拷贝过来然后呢一直到一直到这个位置就是item.grip这个位置ok好那么这样的话呢我们看一下是不是格式会有点问题呢我们来看一下啊去格式化一下那么显然这个话应该是会有点问题的那我们还是这一块会有点问题啊就是先把它贴过来
[09:07] 然后是显示这个位置会有点问题当然cn应该我们就扫掉一个横杠cn应该是cncn-青岛扫掉一个横杠然后拿到它之后这样的话应该就回车没有问题了OK来看一下格式化一下好那么这样的话我们就已经去是不是可以把这个数据显示出来了我们来看一下那么在这个位置我们对这个
[09:35] 我们的传入的一个search data去做一个便利去做一个便利然后去便利每个里面的一个item拿这个item然后去把它内容去展现出来那么我们首先先来看一下这个效果会怎么样走然后我们去搜索一下点击它注意你看没有是不是没有显示出来了那比如说我们搜索一个叫什么呢比如说搜索一个1吧
[10:02] 那么可以看到这个时候是不是就你会发现是不是已经有数据是不是就能够展现出来了对吧然后比如说我们搜索12那么你可以看到是不是地铁12号线那么当然了我们现在会发现有些问题就是那么当我们去搜索最后结果你发现不能够滚动也就是它没有滚动条这是第一个问题第二个问题就是当我标题内容比较多的时候你会发现它会折下来对吧这个是一些样式的问题那么所以我们需要给它添加一个
[10:32] 这个样式啊然后在下面呢我们在这个位置给它增加一个增加一个这个滚动条就是home.css下面我们找到这个srcbar它在在原有的我们这个解释中啊这个进它页面中啊我们这个home.css中有这样的一个定义我们来搜一下那就它然后呢我们再去添加一个添加一个我们这样的滚动条让它在这个外轴这个方向上面去
[11:02] 我们去添加一个这个auto就是如果它内容比较多的时候那么就出现一个滚动条是这样的一个意思好那么我们再来刷新一下看它的一个效果会怎么样发现它现在是不是已经有了这个这样滚动条了可以滚动了这个问题就解决了那么下面呢还有一个就是这个文字比较多让它去隐藏的一个问题那么这样的话我们就需要自己去定义一个css就叫search.css咱们把这个呢拷贝过来那么把它拷一下
[11:31] 然后进入到这个里面来然后我们去创建一个文件就叫设施点css然后把它加了加进去好那么我们去设置一个host title那么来看一下那么去做这样的一个超出的话会做一个隐藏然后这个就强制让它在一行就可以了然后定义了一个这样的class我们就需要在srcbar里面是不是在我们标题这个位置找一下找到这个item
[11:59] 找到我们在这个位置可以看到在我们标题这个位置已经指定了class name等于它了我们再来看一下这个效果会怎么样那么我们刷新这个不对我们这个里面还没有我看还没有引用进来还要把 import 引用进来不引用是不能用的当前目录下面的 searchcss好把它引用进来这样的话就ok了
[12:26] 然后我们尝试的去可以刷新一下然后等待它的刷新然后在这个里面来看一下效果一那么你会发现这个滚动依然是OK的对吧然后搜索一个12那么可以看到它后面内容是不是就已经被我们是不是就隐藏掉了这样的话看起来效果是不是就会好一些OK好嘞那么这个我们是不是就基本上已经实现了一个搜索但是现在还有一个小问题就是那么我
[12:54] 这个就是搜索这个这个页面啊结果页面我怎么把它关闭掉呢那么我们前面是把这个on blue就是焦点离开这个事件是不是已经注视掉了对吧那我们应该怎么样去把它关闭掉呢大家可以思考一下那么我们能不能够继续去使用它前面的这个on blue我们分析过肯定是不行的对吧那么应该怎么做呢
[13:15] 因为我们可以给它上面加一个小的一个这个回退的一个小的一个按钮它点击回退把它关闭掉就可以了那么这个怎么做我们来看一下那么在我们这个页面中其实它有一个小的一个这个小的一个这个按钮对吧然后把这个按钮拿过来那么这个按钮我们来看一下是在是在这个位置我们去在contact的上面去添加一个这样的一个icon
[13:40] 这样的一个小按钮然后当我们点击这个icon的时候就是然后我们去执行这样的一个叫handle search bar就是把这个隐藏掉把这个当前这个隐藏掉那么我们怎么样去定义它呢我们来看一下那么我们就需要去在我们的这个runner上面去定义这样的一个函数好那么要注意的是这个函数的内部你看在它是不是去调用执行它然后呢在
[14:08] 这个方法内部他要叫用race.props.handsearchbar那么这个方法是谁传入的呢是不是就需要在我们的这个home中是不是给他去传入进来啊那么找一下我们的那个设置数据的位置在这handsearchbar这个里面是不是已经传递进去了对吧那么传递进去呢那么我们是不是就可以去直接去使用了那么我们来看一下这个效果会怎么样那么点击搜索
[14:35] 12那么上面是不是有一个这个回退的这样的一个小的一个图标我点击这个当我如果查询完毕你看当我查询完毕之后那我就可以去点击这个回退走这样的话是不是就可以关闭掉了OK就是这样的一个效果比如说1那么点击这个回退好那么到这儿是不是基本上我们是不是就已经实现了这样的一个效果比如说我们再去搜一个叫什么东风东风东风明珠有没有看一下东方明珠
[15:03] 是不是也有东方明珠这样的一个附近的一个房子房源信息比方说像新村我们刚刚所搜索的对吧有什么中原新村你看是不是这个是不是都有好嘞好那么这个图片呢是不是就是它呢是不是就是加载着加载着我们的这个我们上传到这个OSS中的这个图片那我们来可以看一下那么这个图片呢在这个奢侈吧里面我们来找一下那么在下面这个位置那么我们去拿到它的图片的一个这个名字
[15:32] 然后去拼接前面的一个URL是不是就可以去做一个加载这张图片了OK就是看到这样的一个效果OK好的我们接着继续往下面看那么把它编解完成之后然后我们是不是就已经基本的实现了一个搜索但是我们会发现这个里面也会存在一些问题什么问题就是那么我们这个高量并没有去做对不对然后我们也没有去做分页对吧你看这个位置应该是把这个
[15:59] 新春这两个给它去变成一个红色然后呢再加一个分页那么我们现在都没有去做那么一会儿呢我们去把这功能呢去进一步的去做一个完善OK好那么关于这个搜索功能这个基本的一个实现呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 React 的房产信息展示与搜索功能的前端开发过程，包括页面结构、组件逻辑、搜索交互和样式实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示课程 PDF 文档目录，当前位于“WebMagic抓取数据”章节下的“1.6.2、文章mapping”部分，底部有黑马程序员的版权信息。
画面 2: 在 IntelliJ IDEA 中查看 `home.js` 文件，展示 `render` 函数中 `ImageGallery` 组件的配置，包括 `autoPlay=true`、`disableSwipe=false`、`showThumbnails=false`。
画面 3: 在 IntelliJ IDEA 中查看 `home.js` 文件，展示 `searchHandle` 函数，用于设置 `searchBarFlag` 状态。
画面 4: 在浏览器中预览移动端页面，显示“一线江景度假洋房”广告页，右侧是开发者工具的 HTML 结构和样式面板。
画面 5: 在 IntelliJ IDEA 中查看 `home.js` 文件，展示 `render` 函数中 `MapHouse`、`Calculator`、`SearchBar` 组件的条件渲染逻辑。
画面 6: 在 IntelliJ IDEA 中查看 `home.js` 文件，展示 `searchHandle` 函数，其中包含一个 `axios.get` 请求，URL 为 `http://127.0.0.1:18080/search?keyWord=+value+&page=1`。
画面 7: 在 IntelliJ IDEA 中查看 `home.js` 文件，展示 `searchHandle` 函数，其中包含一个 `axios.get` 请求，URL 为 `http://127.0.0.1:18080/search?keyWord=+value+&page=1`，并调用 `this.setState` 更新状态。
画面 8: 在 IntelliJ IDEA 中查看 `searchbar.js` 文件，展示 `SearchBar` 组件的 `render` 函数，使用 `Item.Group` 和 `Item.Image` 渲染搜索结果。
画面 9: 在 IntelliJ IDEA 中查看 `searchbar.js` 文件，展示 `Item.Content` 内部的 `Item.Header` 和 `Item.Meta` 结构，包含 `item.title`、`item.orientation`、`item.houseType`、`item.rent` 等属性。
画面 10: 显示课程 PDF 文档，当前位于“3.4、新增search.css”部分，页面上有一个包含多个开发画面缩略图的弹窗。
画面 11: 在浏览器中预览移动端页面，显示搜索结果列表，包含“近12号地铁站”、“精装大一房”等房源信息。
画面 12: 在 IntelliJ IDEA 中查看 `searchbar.js` 文件，展示 `SearchBar` 组件的 `render` 函数，包含 `Icon` 组件和 `Item.Group` 结构。
画面 13: 在浏览器中预览移动端页面，显示搜索结果列表，包含“近12号地铁站”、“精装大一房”等房源信息。
画面 14: 在浏览器中预览移动端页面，显示搜索结果列表，包含“远洋新村1室1厅4600元”、“海澳新村1室1厅2300元”等房源信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```javascript
const swipeLoading = this.state.swipeLoading;
const swipeData = this.state.swipeData;
let swipe = null;
if (swipe = <ImageGallery
  preventDefaultTouchmoveEvent={true}
  autoPlay={true}
  disableSwipe={false}
  showThumbnails={false}
/>
```
画面 3:
```javascript
case 'find':
  this.props.history.push('/home/find', {query: {flag: true}});
  break;
default:
  break;
searchHandle = () => {
  this.setState({
    searchBarFlag: true
  })
}
```
画面 6:
```javascript
searchHandle = () => {
  this.setState({
    searchBarFlag: true
  })
}
search = (event, data) => {
  let value = data.value;
  let this = this;
  this.searchHandle();
  axios.get('http://127.0.0.1:18080/search?keyWord='+value+'&page=1').then((data) => {
    this.setState({searchData: data.list});
  })
}
```
画面 7:
```javascript
searchHandle = () => {
  this.setState({
    searchBarFlag: true
  })
}
search = (event, data) => {
  let value = data.value;
  let this = this;
  this.searchHandle();
  axios.get('http://127.0.0.1:18080/search?keyWord='+value+'&page=1').then((data) => {
    this.setState({searchData: data.list});
  })
}
```
画面 8:
```javascript
import React from 'React';
import { Icon, Item } from 'semantic-ui-React';

class SearchBar extends React.Component {
  render() {
    return (
      <div className="search-bar">
        <Icon onClick={this.hideSearchBar} name='angle left' size='large'/>
        <div className="search-bar-content">
          <Item.Group divided unstackable>
            {this.props.searchData.map(item => {
              return (
                <Item key={item.id}>
                  <Item.Image src={https://itcast-haoke.oss-cn-qingdao.aliyuncs.com/lj/ + item.image}/>
                  <Item.Content>
                    <div className='house-title'>{item.title}</div>
                    <Item.Meta>
                      <span className='cinema'>{item.orientation}({item.houseType})</span>
                    </Item.Meta>
                    <Item.Description>{item.rent}</Item.Description>
                  </Item.Content>
                </Item>
              )
            })}
          </Item.Group>
        </div>
      </div>
    )
  }
}
```
画面 9:
```javascript
<Item.Content>
  <div className='house-title'>{item.title}</div>
  <Item.Meta>
    <span className='cinema'>{item.orientation}({item.houseType})</span>
  </Item.Meta>
  <Item.Description>{item.rent}</Item.Description>
</Item.Content>
```
画面 12:
```javascript
import React from 'React';
import { Icon, Item } from 'semantic-ui-React';
import './search.css';

class SearchBar extends React.Component {
  render() {
    return (
      <div className="search-bar">
        <Icon onClick={this.hideSearchBar} name='angle left' size='large'/>
        <div className="search-bar-content">
          <Item.Group divided unstackable>
            {this.props.searchData.map(item => {
              return (
                <Item key={item.id}>
                  <Item.Image src={https://itcast-haoke.oss-cn-qingdao.aliyuncs.com/lj/ + item.image}/>
                  <Item.Content>
                    <div className='house-title'>{item.title}</div>
                    <Item.Meta>
                      <span className='cinema'>{item.orientation}({item.houseType})</span>
                    </Item.Meta>
                    <Item.Description>{item.rent}</Item.Description>
                  </Item.Content>
                </Item>
              )
            })}
          </Item.Group>
        </div>
      </div>
    )
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“讲义.pdf”，目录结构显示“1. WebMagic抓取数据”、“2. 开发数据接口”、“3. 增加home.js”、“4. 优化搜索功能”等。
画面 10: PPT 标题为“3.4、新增search.css”，页面上有一个包含多个开发画面缩略图的弹窗。
画面 12: PPT 标题为“3.4、新增search.css”，页面上有一个包含多个开发画面缩略图的弹窗。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

