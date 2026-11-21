# 画面线理解：08_weex_weexUI介绍及简单使用

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\08_weex_weexUI介绍及简单使用【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:25, 01:29, 02:09, 02:35, 03:03, 03:54, 04:36, 05:34, 06:34, 07:02, 07:43, 08:12, 08:57, 09:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:51:30

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Weex 项目中配置和使用 WxcTabBar 和 WxcTabPage 组件，通过修改配置文件和模板代码实现自定义的 tabBar 和页面内容。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Weex 预览界面，手机模拟器显示“传智播客”应用，右侧有二维码提示使用 Weex playground app 扫描。
画面 2: 在 WebStorm 中打开 Weex 项目，展示 main.vue 文件中定义了列表刷新和加载指示器的模板与脚本部分，包含一个 stream 对象和 onLoading 方法。
画面 3: 在 main.vue 文件中，展示 WxcTabBar 组件的引入和配置，包括 tabTitles 和 tabStyles 的导入，以及计算属性 tabPageHeight。
画面 4: 在 WebStorm 中，右键点击项目目录，弹出“New”菜单，准备创建新文件。
画面 5: 在 GitHub 上查看 weex-ui 仓库中的 tab-bar/config.js 文件，展示 tabIconTitles 数组的配置，包含标题、图标和徽章信息。
画面 6: Weex 预览界面，手机模拟器显示空白页面，底部有五个图标按钮。
画面 7: 在项目中打开 config.js 文件，展示 tabTitles 配置，包含“首页”、“特别推荐”、“消息中心”和“我的主页”等条目，其中“我的主页”设置了 dot: true。
画面 8: 在 config.js 文件中，展示 tabStyles 配置，包括背景色、标题颜色、字体大小、padding 等样式属性。
画面 9: Weex 预览界面，手机模拟器显示“我的主页”页面，底部五个图标按钮。
画面 10: 在 main.vue 文件中，展示 WxcTabBar 组件的 created 生命周期钩子和 methods 中的 wxcTabBarCurrentTabSelected 方法。
画面 11: 在浏览器中打开 GitHub 上的 tab-page/config.js 文件，查看配置内容。
画面 12: 在 main.vue 文件中，展示 tab-page 的样式和模板代码，包括 .cell 和 .item-container 的样式定义。
画面 13: 在 main.vue 文件中，展示 WxcTabPage 的模板代码，包括 v-for 循环渲染列表项，每个项包含一个 wxcPanItem 组件。
画面 14: 在 GitHub 上浏览 weex-ui 仓库，点击“wxc-page-calendar”组件链接，进入其文档页面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```vue
<loading v-if="loading" :display="loading ? 'show' : 'hide'">
  <text>Loading ...</text>
  <loading-indicator></loading-indicator>
</loading>
<cell v-for="num in lists" :key="num">
  <text>{{num}}</text>
</cell>
<refresh @refresh="onRefresh" :display="refreshing ? 'show' : 'hide'">
  <text>Refreshing</text>
  <loading-indicator></loading-indicator>
</refresh>
```
```js
const stream = weex.requireModule('stream') || {};
export default {
  data: () => ({
    lists: ['A', 'B', 'C', 'D', 'E', 'A'],
    refreshing: false,
  }),
  methods: function () {
    this.lists = ['1', '2', '3'];
  }
}
```

画面 3:
```vue
<div class="item-container" :style="contentStyle"><text>我的主页</text></div>
<style scoped>
.item-container {
  width: 750px;
  background-color: #f2f3f4;
  align-items: center;
  justify-content: center;
}
</style>
<script>
import { WxcTabBar, Utils } from 'weex-ui';
// https://github.com/alibaba/weex-ui/blob/master/example/tab-bar/config.js
import Config from './config';
export default {
  components: { WxcTabBar },
  data: () => ({
    tabTitles: Config.tabTitles,
    tabStyles: Config.tabStyles,
  }),
  created () {
    const tabPageHeight = utils.env.getPageHeight();
    // 如果页面高度不固定，可以用下面这个计算高度的方法
    // const tabPageHeight = env.deviceHeight * env.deviceWidth / 750;
    const tabStyles = this;
  }
}
</script>
```

画面 5:
```js
// tabIconTitles 配置
tabIconTitles: [
  {
    title: '首页',
    codePoint: 'ue001',
  },
  {
    title: '特别推荐',
    codePoint: 'ue002',
  },
  {
    title: '消息中心',
    codePoint: 'ue003',
    badge: 5,
  },
  {
    title: '我的主页',
    codePoint: 'ue004',
    dot: true,
  }
]
```

画面 7:
```js
export default {
  // 正常模式 tab title 配置
  tabTitles: [
    {
      title: '首页',
      icon: 'https://gw.alicdn.com/tfs/TB1HudSpxXXXXXcXXXXXXXXXX-72-72.png',
      activeIcon: 'https://gw.alicdn.com/tfs/TB1kCk1XkXXXXXcXXXXXXXXXX-72-72.png',
    },
    {
      title: '特别推荐',
      icon: 'https://gw.alicdn.com/tfs/TB1ARoKsXXXXXcXXXXXXXXXX-72-72.png',
      activeIcon: 'https://gw.alicdn.com/tfs/TB1kCk1XkXXXXXcXXXXXXXXXX-72-72.png',
    },
    {
      title: '消息中心',
      icon: 'https://gw.alicdn.com/tfs/TB1VMK5sXXXXXcXXXXXXXXXX-72-72.png',
      activeIcon: 'https://gw.alicdn.com/tfs/TB1aTg2SXkXXXXXcXXXXXXXXXX-72-72.png',
      badge: 5,
    },
    {
      title: '我的主页',
      icon: 'https://gw.alicdn.com/tfs/TB1o3tSXXXXXcXXXXXXXXXX-72-72.png',
      activeIcon: 'https://gw.alicdn.com/tfs/TB1LhMhSpXXXXXcXXXXXXXXXX-72-72.png',
      dot: true,
    }
  ],
  tabStyles: {
    bgColor: '#FFFFFF',
    titleColor: '#666666',
    activeTitleColor: '#303030',
    activeBgColor: '#FFFFFF',
    isActiveTitleBold: true,
    iconId: 70,
    iconHeight: 70,
    width: 160,
    height: 170,
    fontSize: 24,
    textPaddingLeft: 10,
    textPaddingRight: 10,
  }
}
```

画面 8:
```js
tabStyles: {
  bgColor: '#FFFFFF',
  titleColor: '#666666',
  activeTitleColor: '#303030',
  activeBgColor: '#FFFFFF',
  isActiveTitleBold: true,
  iconId: 70,
  iconHeight: 70,
  width: 160,
  height: 170,
  fontSize: 24,
  textPaddingLeft: 10,
  textPaddingRight: 10,
  // 使用 iconfont 模式的 tab title 配置
  tabIconTitles: [
    {
      title: '首页',
      codePoint: 'ue001',
    },
    {
      title: '特别推荐',
      codePoint: 'ue002',
    },
    {
      title: '消息中心',
      codePoint: 'ue003',
      badge: 5,
    },
    {
      title: '我的主页',
      codePoint: 'ue004',
      dot: true,
    }
  ]
}
```

画面 10:
```js
const tabPageHeight = utils.env.getPageHeight();
// 如果页面高度不固定，可以用下面这个计算高度的方法
// const tabPageHeight = env.deviceHeight * env.deviceWidth / 750;
const tabStyles = this;
methods: {
  wxcTabBarCurrentTabSelected (e) {
    const index = e.page;
    // console.log(index);
    alert(e.page);
  }
}
```

画面 12:
```css
.cell {
  background-color: #ffffff;
}
.cell {
  width: 750px;
  height: 300px;
  border-bottom-width: 1px;
  border-style: solid;
  border-color: #e8e8e8;
}
```

画面 13:
```vue
<template>
  <wxc-tab-page :tab-style="tabStyles"
                :tab-page-height="tabPageHeight"
                @wxcTabPageCurrentTabSelected="wxcTabPageCurrentTabSelected">
    <list v-for="(item, key) in tabList"
