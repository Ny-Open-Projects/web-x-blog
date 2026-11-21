# 画面线理解：05.采用GraphQL实现房源列表的查询

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\05.采用GraphQL实现房源列表的查询【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:17, 02:17, 02:34, 02:57, 03:19, 03:53, 04:19, 04:44, 05:15, 05:35, 06:14, 06:28, 06:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:21:03

1) 这一组画面整体在讲如何在 React 前端项目中，通过 GraphQL 查询接口实现房源列表的动态加载与展示。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中“3.1. 编写查询字符串”章节，其中包含 GraphQL 查询语句 `query HouseResourcesList($pageSize: Int, $page: Int) { ... }`，并附带一个房源信息的示意图。
画面2：在 Altair GraphQL 客户端中，执行了上述查询语句，返回了包含房源数据（如 id、title、pic、rent 等）的 JSON 响应。
画面3：前端页面（React App）显示了两个房源卡片，每个卡片包含图片、标题和价格。
画面4：在 IntelliJ IDEA 中，查看 React 组件 `componentDidMount` 方法，使用 `axios.post('/homes/list', { home_type: query.type })` 发起请求。
画面5：在 IntelliJ IDEA 中，查看 React 组件代码，包含 `import React from 'react'; import { withRouter } from 'react-router';` 等导入语句，以及 `goBack = () => { console.log(this.props.history); this.props.history.goBack(); }` 方法。
画面6：在 IntelliJ IDEA 中，查看 GraphQL 查询语句 `query HouseResourcesList($pageSize: Int, $page: Int) { ... }`。
画面7：在 IntelliJ IDEA 中，查看 React 组件 `componentDidMount` 方法，设置状态 `type` 和 `typeName`。
画面8：在 IntelliJ IDEA 中，修改代码，使用 `client.query` 发起 GraphQL 查询，变量为 `{"pageSize":3, "page":1}`。
画面9：前端页面显示三个房源卡片，每个卡片包含图片和标题。
画面10：在 PDF 文档中，展示 GraphQL 查询语句 `client.query(Query: QUERY_LIST, variables: {"pageSize":3, "page":1})`，并显示了前端组件的 `render` 方法。
画面11：在 IntelliJ IDEA 中，查看 React 组件 `render` 方法，返回 `Item` 组件，包含图片、标题、元数据等。
画面12：前端页面显示加载中状态，页面中央有“Loading”字样。
画面13：在 IntelliJ IDEA 中，查看 React 组件 `componentDidMount` 方法，使用 `client.query` 发起 GraphQL 查询。
画面14：在 PDF 文档中，展示“3.2. 改造list.js页面”章节，包含导入语句 `import ApolloClient from 'apollo-boost'; import gql from 'graphql-tag';` 和创建客户端的代码 `const client = new ApolloClient({ ... })`。

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
import gql from 'graphql-tag';

const client = new ApolloClient({
  uri: 'http://127.0.0.1:8000/graphql'
});

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PDF 文档标题为“3. 实现房源列表查询”，子标题“3.1. 编写查询字符串”。
画面14：PDF 文档标题为“3.2. 改造list.js页面”，下方有“黑马程序员”Logo和文字“改变中国IT教育，我们正在行动”，以及“北京市平谷区建新镇金燕路办公楼一层 电话：400-618-9090”。

5) 无。
