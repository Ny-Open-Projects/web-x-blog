# 画面线理解：10.Ant Design入门之美化布局和引入导航条

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\10.Ant Design入门之美化布局和引入导航条【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:17, 02:01, 02:16, 02:25, 02:37, 02:56, 03:12, 03:23, 03:37, 03:57, 04:15, 04:33, 04:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:19:47

1) 这一组画面整体在讲如何使用 Ant Design 的 Menu 组件构建一个带有侧边导航栏的 React 应用布局。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了在浏览器中运行的前端页面，包含 Tab 1、Tab 2、Tab 3 三个标签页，以及 Header 和 Footer。
画面 2: 展示了浏览器中页面的另一个视图，左侧有深色背景，顶部有 Header，底部有 Footer，页面内容区域显示“hello antd we are 第一个 tabs”。
画面 3: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于定义 BasicLayout 组件。
画面 4: 展示了 Ant Design 官网的组件文档页面，左侧是组件列表，右侧是“Layout”组件的示例，包含 Header、Sider、Content、Footer 的布局结构。
画面 5: 展示了 Ant Design 官网的“Menu”组件文档页面，演示了带子菜单的导航菜单，鼠标悬停在“Navigation One”上。
画面 6: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于引入 Menu 和 SubMenu 组件。
画面 7: 展示了 IntelliJ IDEA 中的 React 代码编辑器，显示了 BasicLayout 组件的代码，其中包含 Layout、Header、Content、Footer 的结构。
画面 8: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于引入 Menu 和 SubMenu 组件。
画面 9: 展示了 IntelliJ IDEA 中的 React 代码编辑器，显示了 BasicLayout 组件的代码，其中包含 Menu 组件的配置，如 defaultSelectedKeys、defaultOpenKeys、mode、theme、inlineCollapsed 等属性。
画面 10: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于定义 Menu 组件的子菜单结构。
画面 11: 展示了 Ant Design 官网的“Menu”组件文档页面，演示了“Menu”组件的使用，包括一个按钮用于切换菜单展开/折叠状态。
画面 12: 展示了 IntelliJ IDEA 中的 React 代码编辑器，显示了 BasicLayout 组件的代码，其中包含 Menu 组件的子菜单结构，包括多个 Menu.Item 和 SubMenu。
画面 13: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于定义 BasicLayout 组件的构造函数。
画面 14: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于定义 BasicLayout 组件的构造函数。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 3:
```jsx
import React from 'react';
import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider width={256} style={{ minHeight: '100vh', color: 'white' }}>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>
          </Header>
          <Content style={{ margin: '24px 16px 0', background: '#fff', minHeight: 360 }}>
            {this.props.children}
          </Content>
          <Footer style={{ textAlign: 'center' }}>后台系统 ©2018 Created by 黑马程序员</Footer>
        </Layout>
      </Layout>
    );
  }
}

export default BasicLayout;
```

画面 6:
```jsx
import React from 'react';
import { Layout, Menu, Icon } from 'antd';

const { Header, Footer, Sider, Content } = Layout;
const SubMenu = Menu.SubMenu;

class BasicLayout extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      collapsed: false,
    };
  }
```

画面 7:
```jsx
import React from 'react';
import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider width={256} style={{ minHeight: '100vh', color: 'white' }}>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>
          </Header>
          <Content style={{ margin: '24px 16px 0', background: '#fff', minHeight: 360 }}>
            {this.props.children}
          </Content>
          <Footer style={{ textAlign: 'center' }}>后台系统 ©2018 Created by 黑马程序员</Footer>
        </Layout>
      </Layout>
    );
  }
}

export default BasicLayout;
```

画面 9:
```jsx
import React from 'react';
import { Layout, Menu, Icon } from 'antd';

const { Header, Footer, Sider, Content } = Layout;
const SubMenu = Menu.SubMenu;

class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider width={256} style={{ minHeight: '100vh', color: 'white' }}>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>
          </Header>
          <Content style={{ margin: '24px 16px 0', background: '#fff', minHeight: 360 }}>
            {this.props.children}
          </Content>
          <Footer style={{ textAlign: 'center' }}>后台系统 ©2018 Created by 黑马程序员</Footer>
        </Layout>
      </Layout>
    );
  }
}

export default BasicLayout;
```

画面 10:
```jsx
import React from 'react';
import { Layout, Menu, Icon } from 'antd';

const { Header, Footer, Sider, Content } = Layout;
const SubMenu = Menu.SubMenu;

class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider width={256} style={{ minHeight: '100vh', color: 'white' }}>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>
          </Header>
          <Content style={{ margin: '24px 16px 0', background: '#fff', minHeight: 360 }}>
            {this.props.children}
          </Content>
          <Footer style={{ textAlign: 'center' }}>后台系统 ©2018 Created by 黑马程序员</Footer>
        </Layout>
      </Layout>
    );
  }
}

export default BasicLayout;
```

画面 12:
```jsx
import React from 'react';
import { Layout, Menu, Icon } from 'antd';

const { Header, Footer, Sider, Content } = Layout;
const SubMenu = Menu.SubMenu;

class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider width={256} style={{ minHeight: '100vh', color: 'white' }}>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>
          </Header>
          <Content style={{ margin: '24px 16px 0', background: '#fff', minHeight: 360 }}>
            {this.props.children}
          </Content>
          <Footer style={{ textAlign: 'center' }}>后台系统 ©2018 Created by 黑马程序员</Footer>
        </Layout>
      </Layout>
    );
  }
}

export default BasicLayout;
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 3: PPT 标题为“2.3.5、引入导航条”，内容为课程大纲。
画面 6: PPT 标题为“2.3.5、引入导航条”，内容为课程大纲。
画面 13: PPT 标题为“2.3.5、引入导航条”，内容为课程大纲。
画面 14: PPT 标题为“2.3.5、引入导航条”，内容为课程大纲。

5) 无。
