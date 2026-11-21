# 05.采用GraphQL实现房源列表的查询

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\05.采用GraphQL实现房源列表的查询【海量资源尽在 ubkz.com】.mp4
- 时长 6分56秒（音频 416s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来实现房源列表查询的这个功能啊那么这个功能呢是在从我们这个首页啊然后我们去点击这个二手房呢租房呢还有这个新房这个按钮去点进去去查询的这个房源的这个列表那么我们去实现啊这样的一个效果OK那么这样咱们先把这个呢先截一个图一会儿呢我们去参考这个图呢我们去来设置它里面一些内容啊
[00:28] OK好那么接下来呢我们就来看一下这个应该怎么去做啊那么首先呢我们先来看一下这个里面呃他所需要一些字段对吧他需要的是图片还有这个房屋这个标题然后呢还有这个平民宿还有朝向就是南北的吧然后呢是楼层然后呢所在的地区然后呢就是租金的价格OK大概呢这么多的一些内容那我们首先我们先来写一下他的一个
[00:57] 查询的语句就是我们的WebQL的一个查询语句那么我们在这个位置来看一下吧那么查询语句呢我就不一点一点去写了咱们就拷贝这个讲义中的这个查询的这个字符创把它拷过来拷过来之后呢做一个格式化OK大概有这么多内容那么我们可以看到在这个查询中呢是不是我们给它设置了一些这个有两个参数一个是配置一个是配置
[01:25] OK那么通过他去做一个查询然后我们设置他的一个查询的一个参数把这个Jason我们也拷过来往这一丢OK好这个就是我们的查询的一个参数好那么下面我们去发送这个请求来看一下他能不能查到数据其实我们会发现他是不是可以查到数据OK好那么查到这个数据是不是我们所需要的就这么几个对吧你可以看到有这个商品这个是
[01:52] 我们房屋的这个ID然后呢还有图片啊然后呢还有房屋的这个标题还有他的这个面积对吧建筑面积然后呢还有他的一个朝向然后呢楼层还有他这个租赁OK大概呢是这么多的一些这个内容哎好嘞那么这个我们已经搞定之后啊那么接下来呢我们就需要找到他所对应的这个页面啊然后呢我们去做一些这个修改那么所对的页面呢我们可以看到是home下面的list
[02:21] 那我们是不是就可以进入到我们的项目中来找到在home目录下面有一个list.js文件那么在这个里面呢我们是不是首先肯定要去改造他这个查询对不对之前是不是他通过这种方式是不是去通过一个post请求去做一个查询那我们现在显然要去通过grabql这种形式是不是去做一个查询啊哎OK那么怎么做呢我们来看一下咱们参考这个讲义吧咱们一点一点来改一下啊
[02:48] 首先我们把这两个先导进来是不是就是我们 QL的一个客户端工具对吧把它导进来导进来之后我们去定义我们的一个clientclient apollo这个client然后定义好之后就这个地址是不变的然后下面我们来看一下下面是不是我们定义我们的一个查询这个查询是不是就刚刚我们所写的一个查询语句把它贴过来来看一下
[03:18] 这样一个查询语句当然了贴进来之后它会有一个报错但是要注意的是这个报错呢我们其实不用太去管它因为这个是编辑器的问题好那么这个搞定之后呢下面我们就要去写一个这个查询那咱们把这个查询呢我们贴过来这个查询所要替换的是不是就是之前我们在下面这个位置的查询啊来看一下那么在查询到结果之后呢我们去给它设置states的值
[03:47] 一个叫做list date还有一个log的flag然后呢这个只给它设置就好了所以呢我们可以先把前面的这个内容对吧在这先把这个内容看一下没问题吧在这没问题把它先注释掉然后呢我们是不是就可以把这个查询的这个逻辑给它贴过来往这一抠好这个是不是就是一个查询的逻辑当然呢这个是
[04:15] 可能是这样这样的话就ok了刚刚是一个回车的问题好那么我们来看一下查询的是不是上面listquery list然后要注意的是那么我们在这个位置是不是是我们在查询语义中是不是有参数所以我们需要给他设置两个参数怎么设置在client中它有一个
[04:38] 这个参数主记名叫做variables然后去给他设置两个参数跟我们刚刚在这个位置设置是一样的variables那么就是这样的一个设置然后设置两个参数一个是配置一个是配置OK好那么设置好之后去做一个请求请求之后拿到数据拿到数据之后把数据丢到states中然后下面在这个位置是不是就要做一个便利OK那么便利的逻辑我们就需要去调一下
[05:07] 因为原来的这个字段它跟我们现在字段名有点不一样所以我把这个逻辑简单的去调一下那么这个我也去拷贝我们的讲义中的代码咱们把这个拷过来就可以了拷这个item然后因为它做循环把这个item拷过来看一下没问题吧item在这然后把它拷到这拷过来之后可能会有一些换行的问题咱们调
[05:36] 简单的调一下就好了然后往后面走然后在这个里面需要大家注意的一点是在这个位置我们图片由于我们数据所反复的图片是有多张图片的是不是有多张图片那么我们在这我给它继续做一个split按照逗号去做一个分割然后获取它的第0个也就是第1个图片然后我们给它做一个显示就OK了我们接下来看一下这个效果
[06:02] 其实这个效果他已经刷新了那么就是这样的一个效果那么这个是不是就是已经变成我们真实的这个数据了对不对OK好那么我们现在是不是就已经实现了这个查询列表但是呢我们可以看到无论点击二手房还是新房还是点击这个租房都是查到这个数据原因是我们在这个位置呢并没有设置我们的一个查询的一个条件那么这个呢就我们就暂时呢就先这么去做啊先去查询这个数据
[06:32] 然后我们后面如果有这个时间的话我们再去针对不同的这个房源我们再去给大家做一些这个设置OK好那么关于我们的这个前端的我们去查询房源的列表使用这个Grabber QL这样的一个这样的一个语言去做一个查询的话那我们就讲到这里OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 React 前端项目中，通过 GraphQL 查询接口实现房源列表的动态加载与展示。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中“3.1. 编写查询字符串”章节，其中包含 GraphQL 查询语句 `query HouseResourcesList($pageSize: Int, $page: Int) { ... }`，并附带一个房源信息的示意图。
画面2：在 Altair GraphQL 客户端中，执行了上述查询语句，返回了包含房源数据（如 id、title、pic、rent 等）的 JSON 响应。
画面3：前端页面（React App）显示了两个房源卡片，每个卡片包含图片、标题和价格。
画面4：在 IntelliJ IDEA 中，查看 React 组件 `componentDidMount` 方法，使用 `axios.post('/homes/list', { home_type: query.type })` 发起请求。
画面5：在 IntelliJ IDEA 中，查看 React 组件代码，包含 `import React from 'React'; import { withRouter } from 'React-router';` 等导入语句，以及 `goBack = () => { console.log(this.props.history); this.props.history.goBack(); }` 方法。
画面6：在 IntelliJ IDEA 中，查看 GraphQL 查询语句 `query HouseResourcesList($pageSize: Int, $page: Int) { ... }`。
画面7：在 IntelliJ IDEA 中，查看 React 组件 `componentDidMount` 方法，设置状态 `type` 和 `typeName`。
画面8：在 IntelliJ IDEA 中，修改代码，使用 `client.query` 发起 GraphQL 查询，变量为 `{"pageSize":3, "page":1}`。
画面9：前端页面显示三个房源卡片，每个卡片包含图片和标题。
画面10：在 PDF 文档中，展示 GraphQL 查询语句 `client.query(Query: QUERY_LIST, variables: {"pageSize":3, "page":1})`，并显示了前端组件的 `render` 方法。
画面11：在 IntelliJ IDEA 中，查看 React 组件 `render` 方法，返回 `Item` 组件，包含图片、标题、元数据等。
画面12：前端页面显示加载中状态，页面中央有“Loading”字样。
画面13：在 IntelliJ IDEA 中，查看 React 组件 `componentDidMount` 方法，使用 `client.query` 发起 GraphQL 查询。
画面14：在 PDF 文档中，展示“3.2. 改造list.js页面”章节，包含导入语句 `import ApolloClient from 'apollo-boost'; import gql from 'GraphQL-tag';` 和创建客户端的代码 `const client = new ApolloClient({ ... })`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
query HouseResourcesList($pageSize: Int, $page: Int) {
  list {
    id
    pic
    title
    coveredArea
    orientation
    floor
    rent
  }
}
画面2：
query HouseResourcesList($pageSize: Int, $page: Int) {
  list {
    id
    pic
    title
    coveredArea
    orientation
    floor
    rent
  }
}
画面4：
axios.post('/homes/list', {
  home_type: query.type
}).then(ret => {
  this.setState({
    listData: ret.data,
    loadFlag: true
  })
})
画面5：
goBack = () => {
  console.log(this.props.history);
  this.props.history.goBack();
}
画面6：
query HouseResourcesList($pageSize: Int, $page: Int) {
  list {
    id
    pic
    title
    coveredArea
    orientation
    floor
    rent
  }
}
画面7：
this.setState({
  typeName: query.name,
  type: query.type
})
画面8：
client.query({query: QUERY_LIST, variables: {"pageSize":3, "page":1}}).then(result => {
  this.setState({
    listData: result.data.HouseResourcesList.list,
    loadFlag: true
  });
})
画面10：
client.query(Query: QUERY_LIST, variables: {"pageSize":3, "page":1})
画面11：
return (
  <Item key={item.id}>
    <Item.Image src={item.pic.split(',')[0]}/>
    <Item.Content>
      <Item.Header>{item.title}</Item.Header>
      <Item.Meta>
        <span className="cinema">{item.coveredArea}㎡/{item.orientation}/{item.floor}</span>
        <Item.Description>
          上海
        </Item.Description>
        <Item.Description>{item.rent}</Item.Description>
      </Item.Meta>
    </Item.Content>
  </Item>
)
画面13：
client.query({query: QUERY_LIST, variables: {"pageSize":3, "page":1}}).then(result => {
  this.setState({
    listData: result.data.HouseResourcesList.list,
    loadFlag: true
  });
})
画面14：
import ApolloClient from 'apollo-boost';
import gql from 'GraphQL-tag';

const client = new ApolloClient({
  uri: 'http://127.0.0.1:8000/GraphQL'
});

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PDF 文档标题为“3. 实现房源列表查询”，子标题“3.1. 编写查询字符串”。
画面14：PDF 文档标题为“3.2. 改造list.js页面”，下方有“黑马程序员”Logo和文字“改变中国IT教育，我们正在行动”，以及“北京市平谷区建新镇金燕路办公楼一层 电话：400-618-9090”。

5) 无。

