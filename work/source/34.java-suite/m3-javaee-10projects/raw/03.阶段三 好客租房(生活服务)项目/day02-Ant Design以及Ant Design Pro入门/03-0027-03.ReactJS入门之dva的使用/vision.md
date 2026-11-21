# 画面线理解：03.ReactJS入门之dva的使用

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\03.ReactJS入门之dva的使用【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:16, 04:59, 05:56, 06:49, 07:56, 09:44, 10:32, 14:31, 15:38, 17:03, 17:40, 18:13, 18:54, 21:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:14:35

1) 这一组画面整体在讲如何使用 DvaJS 框架进行数据分层管理，通过创建 model 文件和连接页面组件来实现数据绑定和状态管理。

2) 按时间顺序列出每张画面的要点：
画面1：展示 DvaJS 官网，介绍其基于 React 和 Redux，轻量级且具有 elm 风格。
画面2：在 Typora 编辑器中查看课程文档，内容为“1.1.2. 使用DVA进行数据分层管理”，并展示在 config.js 中配置 dva 插件的代码。
画面3：浏览器新标签页，未显示任何内容。
画面4：展示课程 PPT，标题为“1. ReactJS入门”，子标题“1.1.1. 分层”，图示对比“服务端代码层次”（Controller → Service → Data Access → Database）与“前端代码层次”（Page → Model → Service → Server）。
画面5：在 IntelliJ IDEA 中打开项目，编辑器显示 List 组件的构造函数，其中定义了 this.state.dataList 和 maxNum。
画面6：在 IntelliJ IDEA 中，List 组件的构造函数中，高亮显示了 this.state.dataList 和 maxNum 的定义。
画面7：在 IntelliJ IDEA 中，List 组件的构造函数中，高亮显示了注释和空行。
画面8：在 IntelliJ IDEA 中，打开 models 目录下的 ListData.js 文件，显示了 model 的定义代码。
画面9：在 IntelliJ IDEA 中，编辑器显示了导入 connect 和 dva 的代码，并高亮了 return 语句。
画面10：在 IntelliJ IDEA 中，编辑器显示了 List 组件的 render 方法，高亮了 this.props.dataList.map 语句。
画面11：在 IntelliJ IDEA 中，编辑器显示了 List 组件的 render 方法，高亮了 this.props.dataList 和 maxNum 的赋值语句。
画面12：在 IntelliJ IDEA 中，编辑器显示了 List 组件的 render 方法，高亮了 this.setState 语句，用于更新 dataList 和 maxNum。
画面13：在 IntelliJ IDEA 中，打开 models 目录下的 ListData.js 文件，显示了 model 的定义代码。
画面14：浏览器显示 localhost:8000/list 页面，展示了一个列表和一个“点我”按钮。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2：
```javascript
export default {
  plugins: [
    ['umi-plugin-react', {
      dva: true // 开启dva插件
    }]
  ];
}
```
画面8：
```javascript
export default {
  namespace: 'list',
  state: {
    data: [1, 2, 3],
    maxNum: 3
  }
}
```
画面9：
```javascript
import React from 'react';
import { connect } from 'dva';

// 说明：第一个回调函数，作用：将page与model进行链接，返回model中的数据
// 并且，将返回的数据，绑定到this.props
@connect((state) => {
  return {
  }
})
class List extends React.Component{
  constructor(props) {
    super(props);
  }
}
```
画面10：
```javascript
render() {
  return (
    <div>
      {this.props.dataList.map((value, index) => {
        return <li key={index}>{value}</li>
      })}
    </ul>
  )
}
```
画面11：
```javascript
render() {
  return (
    <div>
      {this.props.dataList.map((value, index) => {
        return <li key={index}>{value}</li>
      })}
    </ul>
  )
}
```
画面12：
```javascript
render() {
  return (
    <div>
      {this.props.dataList.map((value, index) => {
        return <li key={index}>{value}</li>
      })}
      <button onClick={() => {
        let maxNum = this.props.maxNum + 1;
        let nowArr = [...this.props.dataList, maxNum];
        this.setState({
          dataList: nowArr,
          maxNum: maxNum
        });
      }}>点我</button>
    </div>
  );
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面4：
标题：1. ReactJS入门
子标题：1.1.1. 分层
架构图：
- 左侧：服务端代码层次
  - Controller → Service → Data Access → Database
- 右侧：前端代码层次
  - Page → Model → Service → Server
图注：上图中，左侧是服务端代码的层次结构，由 Controller、Service、Data Access 三部分组成服务端系统。

5) 无
