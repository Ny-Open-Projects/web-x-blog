# 画面线理解：08.Ant Design入门之开始使用

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\08.Ant Design入门之开始使用【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:19, 02:11, 03:01, 03:39, 04:36, 05:15, 05:57, 06:58, 08:14, 09:14, 10:26, 11:30, 12:19, 12:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:18:18

1) 这一组画面整体在讲如何在 React 项目中使用 Ant Design 的 Tabs 组件，并通过代码实践解决组件导入和使用中的错误。

2) 按时间顺序列出每张画面的要点：
画面1: 在 IntelliJ IDEA 中查看项目结构，编辑 `config.js` 文件，其中包含插件配置。
画面2: 浏览 Ant Design 官网的 Button 组件文档页面。
画面3: 浏览 Ant Design 官网的 Menu 组件文档页面，展示下拉菜单效果。
画面4: 浏览 Ant Design 官网的 Rate 组件文档页面。
画面5: 浏览 Ant Design 官网的 Modal 组件文档页面。
画面6: 浏览 Ant Design 官网的 BackTop 组件文档页面，展示代码示例。
画面7: 浏览 Ant Design 官网的 Tabs 组件文档页面。
画面8: 在 IntelliJ IDEA 中编辑 `MyTabs.js` 文件，正在导入 React。
画面9: 在 Ant Design 官网的 Tabs 组件文档页面，展示代码示例。
画面10: 在浏览器中显示错误信息，提示 `ReferenceError: TabPane is not defined`，并展示错误堆栈。
画面11: 在 IntelliJ IDEA 中编辑 `MyTabs.js` 文件，导入 `Tabs` 组件并定义组件结构。
画面12: 在 IntelliJ IDEA 中编辑 `MyTabs.js` 文件，修改 `TabPane` 的标签文本。
画面13: 在 Typora 中查看 Markdown 文档，内容为 Ant Design Tabs 组件的使用说明。
画面14: 在 Typora 中查看 Markdown 文档，内容为 Ant Design Tabs 组件的使用说明，展示代码示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```javascript
// 导出一个对象，暂时设置为空对象，后期再填充内容
export default {
  plugins: [
    'umi-plugin-react', {
      // 暂时不启用任何功能
      dva: true, // 开启了dva功能,
    }
  ]
};
```

画面8:
```javascript
import React from 'react';
```

画面9:
```javascript
import { Tabs } from 'antd';

const callback = (key) => {
  console.log(key);
}

ReactDOM.render(
  <Tabs defaultActiveKey="1" onChange={callback}>
    <TabPane tab="Tab 1" key="1">Content of Tab Pane 1</TabPane>
    <TabPane tab="Tab 2" key="2">Content of Tab Pane 2</TabPane>
    <TabPane tab="Tab 3" key="3">Content of Tab Pane 3</TabPane>
  </Tabs>
  mountNode
);
```

画面11:
```javascript
import React from 'react';
import { Tabs } from 'antd'; // 第一步，导入需要使用的组件

function callback(key) {
  console.log(key);
}

class MyTabs extends React.Component {
  render() {
    return (
      <Tabs defaultActiveKey="1" onChange={callback}>
        <TabPane tab="Tab 1" key="1">Content of Tab Pane 1</TabPane>
        <TabPane tab="Tab 2" key="2">Content of Tab Pane 2</TabPane>
        <TabPane tab="Tab 3" key="3">Content of Tab Pane 3</TabPane>
      </Tabs>
    )
  }
}

export default MyTabs;
```

画面12:
```javascript
import React from 'react';
import { Tabs } from 'antd'; // 第一步，导入需要使用的组件

function callback(key) {
  console.log(key);
}

class MyTabs extends React.Component {
  render() {
    return (
      <Tabs defaultActiveKey="1" onChange={callback}>
        <TabPane tab="Tab 1" key="1">Hello antd wo de 第一个 tab</TabPane>
        <TabPane tab="Tab 2" key="2">Content of Tab Pane 2</TabPane>
        <TabPane tab="Tab 3" key="3">Content of Tab Pane 3</TabPane>
      </Tabs>
    )
  }
}

export default MyTabs;
```

画面13:
```javascript
export default {
  plugins: [
    'umi-plugin-react', {
      dva: true, // 开启dva功能
      antd: true, // 开启Ant Design功能
    }
  ]
};
```

画面14:
```javascript
import React from 'react';
import { Tabs } from 'antd';

const TabPane = Tabs.TabPane;

function callback(key) {
  console.log(key);
}

class MyTabs extends React.Component {
  render() {
    return (
      <Tabs defaultActiveKey="1" onChange={callback}>
        <TabPane tab="Tab 1" key="1">Content of Tab Pane 1</TabPane>
        <TabPane tab="Tab 2" key="2">Content of Tab Pane 2</TabPane>
        <TabPane tab="Tab 3" key="3">Content of Tab Pane 3</TabPane>
      </Tabs>
    )
  }
}

export default MyTabs;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面13: PPT 标题为“2.2.2、小试牛刀”，内容为“接下来，我们开始使用 antd 的组件，以 tabs 组件为例，地址：https://ant.design/components/tabs-cn/”，并附有代码示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
