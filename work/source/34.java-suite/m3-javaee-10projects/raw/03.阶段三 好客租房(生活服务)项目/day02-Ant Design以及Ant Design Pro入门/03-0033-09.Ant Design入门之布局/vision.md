# 画面线理解：09.Ant Design入门之布局

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\09.Ant Design入门之布局【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:40, 02:18, 03:10, 03:50, 04:19, 05:16, 05:55, 07:03, 08:53, 09:45, 10:33, 11:33, 13:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:18:57

1) 这一组画面整体在讲如何使用 Ant Design Pro 的 Layout 组件构建后台管理系统经典三部分布局，并集成 TabPane 组件实现页面切换。

2) 按时间顺序列出每张画面的要点：
画面1：介绍 Ant Design 布局组件，展示 Header、Sider、Content、Footer 四部分结构图。
画面2：展示项目配置文件 config.js，其中 plugins 配置了 'umi-plugin-react' 并启用了 antd。
画面3：在 Ant Design 官网查看 Layout 组件的组件描述和代码演示。
画面4：在官网展示 Layout 组件的多种布局方式（Header-Sider-Content-Footer、Content-Sider-Footer、Sider-Header-Content）。
画面5：在 IDE 中打开 layouts/index.js 文件，准备编写布局代码。
画面6：在 IDE 中编辑 index.js，开始编写 BasicLayout 组件的类定义。
画面7：在 IDE 中编写 BasicLayout 组件的 render 方法，使用 Layout 组件包裹 Header、Content、Footer。
画面8：在终端看到 Webpack 编译成功，并显示应用运行在 http://localhost:8000。
画面9：在 IDE 中修改 BasicLayout 组件，将 Header、Content、Footer 作为 Layout 的子元素。
画面10：在浏览器中访问 http://localhost:8000/，显示 Header、Sider、Footer，Content 区域为空。
画面11：在 IDE 中打开 pages/MyTabs.js 文件，编写使用 Tabs 组件的 MyTabs 组件。
画面12：在 IDE 中切换到 layouts/index.js，准备在 BasicLayout 中嵌入 MyTabs 组件。
画面13：在 Typora 文档中展示配置文件，配置 routes 以使用 MyTabs 组件。
画面14：在 Typora 文档中展示访问 http://localhost:8000/myTabs 后页面效果，并介绍美化页面。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2：
```javascript
export default {
  plugins: [
    'umi-plugin-react', {
      // 暂时不启用任何功能
      dva: true, // 开启了 dva 功能,
      antd: true
    }
  ]
}
```

画面5：
```javascript
import React from 'react';
```

画面6：
```javascript
export
exports (index.d.ts, node) any
external (lib.dom.d.ts) External
EXT frag_depth (lib.dom.d.ts)
executor(resolve: (value?: PromiseLike< void
expectedClass (... args: any) 'T
expirationTime
EXT texture_filter anisotropic (lib.dom.d.ts.
ExtendableEvent (lib.webworker.d.ts)
ExtendableMessageEvent (lib.webworker.d.ts)
```

画面7：
```javascript
import React from 'react';
import [Layout] from 'antd';
const (Header, Footer, Sider, Content) = Layout;
class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider>Sider</Sider>
        <Layout>
          <Header>Header</Header>
          <Content>Content</Content>
          <Footer>Footer</Footer>
        </Layout>
      </Layout>
    )
  }
}
export default BasicLayout;
```

画面8：
```text
Compiling
success webpack compiled in 7s 525ms
DONE Compiled successfully in 703ms
App running at:
- Local: http://localhost:8000/ (copied to clipboard)
- Network: http://172.16.55.244:8000/
```

画面9：
```javascript
<Header>Header</Header>
<Content>Content</Content>
<Footer>Footer</Footer>
```

画面11：
```javascript
import React from 'react';
import [Tabs] from 'antd'; // 第一步，导入需要使用的组件
function callback(key) {
  console.log(key);
}
class MyTabs extends React.Component{
  render() {
    return (
      <Tabs defaultActiveKey="1" onChange={callback}>
        <TabPane tab="Tab 1" key="1">hello antd wo de 第一个 tab</TabPane>
        <TabPane tab="Tab 2" key="2">Content of Tab Pane 2</TabPane>
        <TabPane tab="Tab 3" key="3">Content of Tab Pane 3</TabPane>
      </Tabs>
    )
  }
}
export default MyTabs;
```

画面13：
```javascript
export default {
  plugins: [
    'umi-plugin-react', {
      dva: true, // 开启 dva 功能
      antd: true // 开启 Ant Design 功能
    }
  ],
  routes: [
    {
      path: '/',
      component: '../layouts',
      routes: [
        {
          path: '/myTabs',
          component: './myTabs'
        }
      ]
    }
  ]
}
```

4) 出现的 PPT 标题、架构图/流程图的结构、表格数据：
画面1：标题为“2.3、布局”，图示中 Header 指向 Layout，Sider 指向 Layout，Content 指向 Layout，Footer 指向 Layout。
画面3：标题为“组件描述”，内容为：
- Header：顶部容器，自带默认样式，其下可嵌套任何元素，只能放在 Layout 中。
- Sider：侧边栏，自带默认样式，其下可嵌套任何元素，只能放在 Layout 中。
- Content：内容容器，自带默认样式，其下可嵌套任何元素，只能放在 Layout 中。
- Footer：底部容器，自带默认样式，其下可嵌套任何元素，只能放在 Layout 中。
画面4：展示 Layout 组件的三种布局结构。
画面14：标题为“2.3.4、美化页面”，图示中展示了 TabPane 组件的使用。

5) 无。
