# 13.Ant Design入门之表格的数据分离

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\13.Ant Design入门之表格的数据分离【海量资源尽在 666java.com】.mp4
- 时长 6分52秒（音频 412s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面我们来看一下将这个数据分离到这个model中那么为什么要分离呢其实前面我们就讲过了就是我们这个页面呢应该和我们的model是两个层就分层做一个开发所以呢我们需要对它做一个分离好那么下面我们来看一下怎么样去做那么首先呢我们在这个model中呢创建一个文件叫做urlistdata.js这个文件
[00:27] 那么找到我们这个models然后呢下面创建一个文件叫做这个urlist date文件然后呢在这个里面呢我们把这个内容靠过来因为这个内容呢前面我们基本的也都讲过啊我们大概是来看一下大家就明白了然后呢我们可以看到首先呢我们是为我们的这个我们的这个model啊给它去设置一个命名空间就是为了做一个区分啊
[00:54] 然后呢给他设置一个状态的一个list现在是一个空的一个数据啊然后呢我们给他设置一个这个effect那么这个呢是用于我们去一步去做一些这种数据这种处理啊然后呢我们设置一个unit data做一个数据初始化那么当我们去拿到这个数据的时候然后呢我们是不是就要去去调用我们的reduce这个的query list这个方法然后呢我们拿到这个数据呢
[01:22] 去把这个数据result这个数据注意是result给他把这个数据是不是给他展开然后呢我们给他return回去啊就可以了那么当我们return回去呢就意味着我们这个state的这个数据是不是发生了变更那么我们React.js框架呢他就会去更新我们这个页面啊把这个页面中的这个run的方法重新执行那么就会更新那么在我们这个
[01:45] 做异步去加载的时候是不是使用到了一个request对象这个对象呢是引用的我们有跳中的request是不是就是我们引用的这个解释中的一个内容他引用的是在这啊哎ok好那么呃这个呢就是我们整个的这个model这一层跟我们前面所写的这个list data啊是一样的啊几乎是一样的
[02:06] 好那么下面我们就对UserList逻辑呢做一个改造啊做一个改造那么我们来看一下这个里面改造了哪些内容呢那么首先呢我们是不是需要给它添加一个连接器啊这给大家应该还有印象吧给它添加一个连接器啊加入进来加一个封号加个连接器啊然后呢加入之后啊我们就需要给它去设置一个命名空间这个命名空间呢就是我们方便我们后面去使用啊
[02:35] 然后呢我们给它添加一个这个修饰器添加一个修饰器加到这个类这个上面好加到这里然后呢我们可以看到是不是我们把这个数据绑定到我们的this.props中的什么呢这个data属性对吧然后呢下面是不是就可以使用到我们这个data属性了哎OK好那么拿到它下面的这个list
[03:00] 然后我们第二个参数是不是把我们的一个函数是不是绑定到我们的一个认识点property中然后去dispatch去调用我们的这个mod中的一个方法叫united data这个方法这个前面我们都讲过了然后下面我们继续往下面看然后我们首先给它做一个当我们的这个组件加载完成之后我们去做一个初始化的一个操作其实在调用这个方法然后我们继续往下面看
[03:29] 下面呢我们要去改造的一个部分呢就是我们这个date就是datasource它呢是不是不能再使用这个date了而是使用什么呢使用的是不是我们这个this.propstone的这个date由于我们是不是已经把它放到外部的这个model这一层所以我们应该使用的是它哎呀OK好这样的一个效果啊那么接下来呢我们是不是就可以来刷新看一下效果
[03:58] 但是你会发现现在呢他并没有任何的数据为什么呢我们来看一下这个他的请求一个network啊刷新来看一下效果那么可以看到他是不是正常的去请求了我们的这个DS下面的urlist这个地址是不是由于我们刚刚在这个位置所写的这个地址对吧但是呢我们现在是不是并没有这个数据啊所以他显示是没有这个数据的啊这个是非常正常的啊
[04:26] 好那么下面我们要做的事情是不是需要给他去mock一下这个数据那么怎么样mock还记得吗是不是我们去进入我们这个mock这个目录在mock这个目录下面呢我们给他创建一个这个JS文件那么在这那么在这个这个文件已经存在了吗已经存在已经存在了那么已经存在了我们再给他添加一个再添加一个我们这个数据就可以了咱们把这个打过来把它打过来把这个逗号考一下
[04:57] 那么原来我们是不是已经有一个mock对吧我们再来加一个mock把这个多了多了一个回车倒上那么我们是不是就在添加一个get的请求第二个下面user list那么返回的数据就是这样的一个数据那么这个数据是不是跟我们原来写到我们这个user list中的页面中的数据是一样的所以我们这个就没有必要了把它就删掉了最终我们的user list页面是不是变成这样的一个页面了OK好然后我们来刷新一下看效果走
[05:27] 有效果吗有那么为了跟我们原来数据区分我们可以来测一下我们的MOOC中的数据我改成MOOC的数据改成张三一李四二王五三为了区分我们刚刚写死的数据刷新一下你可以看到是不是张三一李四二王五三是不是能够正常的显示出来了而且说明我们的什么我们这个MOOC是不是也是OK了来看一下刷新一下那么找到我们这个请求
[05:57] 那么来看一下它请求返回的数据依然是不是我们的所期望所看到这个数据啊没有任何问题好那么关于这个表格的一个基本的一个使用啊我们就讲到这里了那么我们是不是通过去把这个表格的它的数据放到外部的一个model这一层做一个分离然后呢我们又去对它的一个数据的请求做了一个mock的这样的一个操作
[06:22] OK好那么对于表格的我们基本上就已经掌握它的用法当然了我们这个只是一个做一个简单的一个入门那么如果大家需要去看更多的一些这个它的参数或者说它的一些这种用法那么还是需要去看它的官方文档它这个文档的写的还是非常不错的大家都可以看一下它各种案例各种施令的都有OK好那么关于这个表格的用法我们就先讲到这里了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 React 项目中使用 Ant Design 的 Table 组件展示用户列表，并结合 Redux 管理数据状态，同时通过 mock 数据模拟后端接口。

2) 按时间顺序列出每张画面的要点：
画面1：在 UserList.js 中定义了 Table 的列，其中“标签”列使用了 render 函数渲染 Tag 组件，“操作”列包含“编辑”和“删除”链接。
画面2：展示课程笔记中关于“将数据分离到 model 中”的章节，同时显示了 UserListData.js 文件中的部分 Redux reducer 代码。
画面3：在 UserList.js 中导入了 Ant Design 的 Table、Divider、Tag、Pagination 组件，并定义了模拟数据 data。
画面4：在 UserList.js 中继续编写 Table 的列定义，包括“姓名”、“年龄”、“地址”。
画面5：在 UserList.js 中为 Table 组件添加了 pagination 属性，并继续定义列。
画面6：在 UserList.js 中使用 @connect 装饰器连接 Redux，定义了 mapStateToProps 和 mapDispatchToProps。
画面7：浏览器中显示了用户列表页面的空白状态，网络面板显示请求已结束。
画面8：展示课程笔记中 UserList.js 的完整代码结构，以及 mock 数据文件 MockListData.js 的部分内容。
画面9：展示课程笔记中 MockListData.js 文件的完整内容，定义了模拟的用户列表数据。
画面10：在 MockListData.js 中定义了模拟的用户列表数据，包括姓名、年龄、地址、标签等字段。
画面11：浏览器中显示了用户列表页面，包含“姓名”、“年龄”、“地址”、“标签”、“操作”等列，但数据为空。
画面12：浏览器中显示了空白页面，网络面板显示请求已结束。
画面13：在 Ant Design 官网的 Table 组件文档页面，展示了“标签”列和“操作”列的渲染代码。
画面14：展示课程笔记中关于“Ant Design Pro 入门”的章节，介绍了 Ant Design Pro 是基于 Ant Design 的一个开箱即用的企业级中后台前端解决方案。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```jsx
render: (tags) => (
  <span>
    {tags.map(tag => <Tag color="blue" key={tag}>{tag}</Tag>)}
  </span>
)}
```

画面2：
```js
reducers: {
  queryList(state, result) {
    let data = [...result.data];
    return { //业务状态
      list: data
    }
  }
}
```

画面3：
```js
import React from 'React';
import (Table, Divider, Tag, Pagination ) from 'antd';
const [Column] = Table;
const data = [
  {
    key: '1',
    name: '张三',
    age: 32,
    address: '上海市',
    tags: ['程序员', '帅气'],
  },
  {
    key: '2',
    name: '李四',
    age: 42,
    address: '北京市',
    tags: ['屌丝'],
  },
  {
    key: '3',
    name: '王五',
    age: 32,
    address: '杭州市',
    tags: ['高富帅', '富二代'],
  }
];
class UserList extends React.Component {
```

画面4：
```jsx
<Table dataSource={data} pagination={{position: "bottom", total: 50}}>
  <Column
    title="姓名"
    dataIndex="name"
    key="name"
  />
  <Column
    title="年龄"
    dataIndex="age"
    key="age"
  />
  <Column
    title="地址"
    dataIndex="address"
    key="address"
  />
</Table>
```

画面5：
```jsx
<Table dataSource={data} pagination={{position: "bottom", total: 50}}>
  <Column
    title="姓名"
    dataIndex="name"
    key="name"
  />
  <Column
    title="年龄"
    dataIndex="age"
    key="age"
  />
  <Column
    title="地址"
    dataIndex="address"
    key="address"
  />
</Table>
```

画面6：
```js
@connect ((state) => {
  return {
    data: state[namespace].list
  }
}, (dispatch) => {
  return {
    initData: () => {
      dispatch({
        type: namespace + "/initData"
      });
    }
  }
})
class UserList extends React.Component {
```

画面8：
```js
export default UserList;
```

画面9：
```js
export default {
  'get /ds/list': function (req, res) {
    res.json({
      data: [1, 2, 3, 4],
      maxNum: 4
    });
  },
  'get /ds/user/list': function (req, res) {
    res.json([
      {
        key: '1',
        name: '张三',
        age: 32,
        address: '上海市',
        tags: ['程序员', '帅气'],
      },
      {
        key: '2',
        name: '李四',
        age: 42,
        address: '北京市',
        tags: ['屌丝'],
      },
      {
        key: '3',
        name: '王五',
        age: 32,
        address: '杭州市',
        tags: ['高富帅', '富二代'],
      }
    ]);
  }
};
```

画面10：
```js
'get /ds/user/list': function (req, res) {
  res.json([
    {
      key: '1',
      name: '张三',
      age: 32,
      address: '上海市',
      tags: ['程序员', '帅气'],
    },
    {
      key: '2',
      name: '李四',
      age: 42,
      address: '北京市',
      tags: ['屌丝'],
    },
    {
      key: '3',
      name: '王五',
      age: 32,
      address: '杭州市',
      tags: ['高富帅', '富二代'],
    }
  ]);
};
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT 标题为“2.4.2. 将数据分离到model中”，下方有“model的实例：UserListData.js”的说明。
画面8：PPT 标题为“mock数据：MockListData.js”，下方有“export default”的代码。
画面14：PPT 标题为“3、Ant Design Pro入门”，子标题为“3.1、了解Ant Design Pro”，下方有“Ant Design Pro 是基于Ant Design 的一个开箱即用的企业级中后台前端解决方案。”的说明。

5) 不要评价画面美观，不要输出与课程无关的内容。

