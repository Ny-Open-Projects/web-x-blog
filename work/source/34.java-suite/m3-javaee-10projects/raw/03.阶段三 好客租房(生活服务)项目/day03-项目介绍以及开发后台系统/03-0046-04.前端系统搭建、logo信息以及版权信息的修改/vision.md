# 画面线理解：04.前端系统搭建、logo信息以及版权信息的修改

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\04.前端系统搭建、logo信息以及版权信息的修改【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 02:17, 03:33, 05:09, 06:12, 07:16, 08:12, 08:34, 09:07, 10:24, 11:02, 11:26, 11:48, 12:18, 12:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:27:14

1) 这一组画面整体在讲什么（一句话）：
讲解如何修改前端项目中的 Logo 和版权信息，涉及文件路径、组件代码和样式调整。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程大纲，当前章节为“2.1、前端搭建”，并显示项目文件夹结构，其中“用户管理”文件夹被选中。
画面2：展示“itcast-haoke”项目文件夹，其中包含“开发环境相关”、“快捷启动脚本”、“dubbo”等文件夹和文件。
画面3：在 IntelliJ IDEA 中打开项目，终端显示依赖安装警告信息。
画面4：终端显示 Webpack 编译成功，应用运行在 http://localhost:8000。
画面5：展示“2.1.2、修改Logo以及版权信息”章节，指出全局布局文件位于“src/layouts”目录下，选中“BasicLayout.js”。
画面6：在“BasicLayout.js”文件中，导入了多个 React 和 Ant Design 相关模块，包括 logo、Footer、Header 等。
画面7：展示“BasicLayout.js”中包含的 <Authorized> 组件和 <Footer> 组件的嵌套结构。
画面8：展示“BasicLayout.js”中导入的模块列表，包括 logo、Footer、Header 等。
画面9：展示“SideMenu.js”文件中，定义了 isMainMenu 函数和 handleOpenChange 方法。
画面10：展示“SideMenu.js”中 <Sider> 组件的样式配置，包括 width、theme 等属性。
画面11：展示“SideMenu.js”中 <Sider> 组件的样式配置，其中 width 属性被修改为 256。
画面12：展示“BasicLayout.js”中 <div className={styles.logo} id="logo"> 的代码，以及在 Footer.js 中的版权信息。
画面13：展示“Footer.js”文件内容，包含 <GlobalFooter> 组件和版权信息。
画面14：展示“2.1.2、修改Logo以及版权信息”章节，选中“Footer.js”文件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```
全局的布局文件在：
└── src
    ├── assets
    ├── components
    ├── i18n
    ├── layouts
    │   └── BasicLayout.js
    │   └── Footer.js
    │   └── Header.js
    │   └── MenuContext.js
    └── pages
```

画面6：
```javascript
import React from 'react';
import { Layout } from 'antd';
import DocumentTitle from 'react-document-title';
import isEqual from 'lodash/isEqual';
import memoizeOne from 'memoize-one';
import { connect } from 'dva';
import ContainerQuery from 'react-container-query';
import classNames from 'classnames';
import pathToRegexp from 'path-to-regexp';
import { enquireScreen, unenquireScreen } from 'enquire-js';
import FormatMessage from 'umi/locale';
import SideMenu from '@/components/SiderMenu';
import Authorized from '@/utils/Authorized';
import SettingDrawer from '@/components/SettingDrawer';
import logo from '@/assets/logo-heima.png';
import Footer from '@/Footer';
import Header from '@/Header';
import Context from './MenuContext';
import Exception403 from '@/pages/Exception/403';

const { Content } = Layout;

// Conversion router to menu.
function formatter(data, parentAuthority, parentName) {
  return data
    .map(item => {
      let locale = 'menu';
      if (parentName && item.name) {
        locale = `${parentName}.${item.name}`;
      } else if (item.name) {
        locale = item.name;
      }
      return {
        ...item,
        locale,
      };
    })
    .filter(item => item.name);
}
```

画面7：
```javascript
<Content style={this.getContentStyle()}>
  <Authorized authority={routerConfig && routerConfig.authority} noMatch={<Exception403 />}>
    {children}
  </Authorized>
</Content>
<Footer />
</Layout>
return (
  <React.Fragment>
    <DocumentTitle title={this.getPageTitle(pathname)}>
      <ContainerQuery query={query}>
        <Context.Provider value={this.getContext()}>
          <div className={classNames(param)}>{layout}</div>
        </Context.Provider>
      </ContainerQuery>
    </DocumentTitle>
  </React.Fragment>
);
```

画面9：
```javascript
isMainMenu = key => {
  const { menuData } = this.props;
  return menuData.some(item => {
    if (key) {
      return item.key === key || item.path === key;
    }
    return false;
  });
};

handleOpenChange = openKeys => {
```

画面10：
```javascript
[styles.light]: theme === 'light',
return (
  <Sider
    trigger={null}
    collapsible={collapsed}
    breakpoint="lg"
    onCollapse={onCollapse}
    width={256}
    theme={theme}
    className={siderClassName}
  >
    <div className={styles.logo} id="logo">
      <Link to="/">
        {/* <img src={logo} alt="logo" /> */}
        <h1>好客租房 - 管理系统</h1>
      </Link>
    </div>
    <BaseMenu
      {...this.props}
      mode="inline"
      handleOpenChange={this.handleOpenChange}
      onOpenChange={this.handleOpenChange}
      style={{ padding: '16px 0', width: '100%', overflowX: 'hidden' }}
    />
  </Sider>
```

画面12：
```javascript
<div className={styles.logo} id="logo">
  {/* <img src={logo} alt="logo" /> */}
  <h1>好客租房 - 管理系统</h1>
</div>

// 在Footer.js文件中修改版权信息：
import React, { Fragment } from 'react';
import { Layout, Icon } from 'antd';
import GlobalFooter from '@/components/GlobalFooter';

const FooterView = () => {
  <GlobalFooter>
    <Fragment>
      Copyright <Icon type="copyright" /> 2018 黑马程序员 博学谷 出品
    </Fragment>
  </GlobalFooter>
};

export default FooterView;
```

画面13：
```javascript
import React, { Fragment } from 'react';
import { Layout, Icon } from 'antd';
import GlobalFooter from '@/components/GlobalFooter';

const FooterView = () => {
  <GlobalFooter>
    <Fragment>
      Copyright <Icon type="copyright" /> 2018 黑马程序员 博学谷 出品
    </Fragment>
  </GlobalFooter>
};

export default FooterView;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：
标题：“2.1.2、修改Logo以及版权信息”
内容：展示“全局的布局文件在：”目录结构，其中“BasicLayout.js”被选中。

画面14：
标题：“2.1.2、修改Logo以及版权信息”
内容：展示“将logo部分修改为：”按钮，以及“全局的布局文件在：”目录结构，其中“Footer.js”被选中。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
