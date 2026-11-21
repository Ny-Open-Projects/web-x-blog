# 画面线理解：09_文章列表前端_页面初始化

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\09_文章列表前端_页面初始化【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:26, 02:17, 03:00, 03:18, 03:56, 04:18, 04:34, 04:51, 05:39, 06:05, 06:16, 07:26, 07:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:52:28

1) 这一组画面整体在讲如何使用 Weex UI 组件库开发一个带标签页的新闻应用首页，包括路由配置、布局结构和数据配置。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示项目结构，选中 `layouts` 文件夹下的 `layout.vue`。
画面 2: 在 `router.js` 中定义路由，将 `/` 路由指向 `Layout` 组件，`/home` 路由指向 `Home` 组件。
画面 3: 查看 `layout_main.vue` 文件，展示其模板结构，包含 `<router-view>` 和 `<div class="main-body">`，并导入 `Menu` 组件。
画面 4: 在 Weex Playground 中查看 `wxc-tab-page` 组件的使用方法和示例效果。
画面 5: 在文档中查看“2.1 创建文件”部分，提到创建 `src/api/home/index.js` 文件用于封装数据请求。
画面 6: 查看 `index.vue` 文件，展示 `wxc-tab-page` 的模板结构，包含 `wxc-pan-item`。
画面 7: 查看 `config.js` 文件，展示导入 `Config` 的代码和 `export default` 的配置对象。
画面 8: 查看 `config.js` 文件，展示 `tabStyles` 对象的样式配置。
画面 9: 查看 `config.js` 文件，展示 `tabTitles` 数组和 `tabStyles` 对象的配置。
画面 10: 查看 `config.js` 文件，展示 `tabTitles` 数组和 `tabStyles` 对象的配置。
画面 11: 查看 `index.vue` 文件，展示 `wxc-tab-page` 的模板结构，包含 `wxc-pan-item`。
画面 12: 查看 `index.vue` 文件，展示 `script` 部分的代码，导入组件并定义数据和方法。
画面 13: 查看 `index.vue` 文件，展示 `wxc-tab-page` 的模板结构，包含 `wxc-pan-item`。
画面 14: 在 Weex Playground 中展示应用的预览效果，包含一个二维码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 2:
```javascript
import Layout from '@/components/layouts/layout_main'
import Home from '@/pages/home/index'
let routes = [
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '/home',
        name: 'Home',
        component: Home
      }
    ]
  }
]
export default routes;
```

画面 3:
```vue
<template>
  <div class="wrapper">
    <div class="router-body"><router-view></router-view></div>
    <div class="main-body"><Menu></Menu></div>
  </div>
</template>

<script>
// 引入底部菜单
import Menu from '@/components/menus/menu'

export default {
  name: 'Weex-Layout-Mian',
  components: {Menu}
}
</script>

<style scoped>
.wrapper {
  flex-direction: column;
  flex-wrap: wrap;
}

.router-body {
  flex: 1;
  flex-direction: column;
  border: 1px solid red;
}
</style>
```

画面 6:
```vue
<template>
  <wxc-tab-page ref="wxc-tab-page"
    :tab-titles="tabTitles"
    :tab-styles="tabStyles"
    title-type="icon"
    tab-page-height="tabPageHeight"
    @wxcTabPageCurrentTabSelected="wxcTabPageCurrentTabSelected"
  >
    <list v-for="(demo, key) in tablist" :key="key">
      <cell v-for="(v, key) in v" :key="key">
        <wxc-pan-item text-id="1" + (v) + '+' + (key)
          url="https://HS.m.taobao.com/trip/ticket/detail/index.html?scnId=2675"
        >
          <div class="content">
            <text>{{(key)}}</text>
          </div>
        </wxc-pan-item>
      </cell>
    </list>
  </wxc-tab-page>
</template>

<style scoped>
.item-container {
  width: 750px;
  background-color: #f2f3f4;
}

.border-cell {
  background-color: #f2f3f4;
  width: 750px;
  height: 24px;
  align-items: center;
  justify-content: center;
  border-bottom-width: 1px;
  border-style: solid;
  border-color: #b8b8b8;
}
</style>
```

画面 7:
```javascript
// script
const dom = weex.requireModule('dom');
import { WxcTabPage, WxcPanItem, Utils, BindEnv } from 'weex-ui';
import Config from './config'
export default {
  components: { WxcTabPage, WxcPanItem },
  data () {
    return {
      tabTitles: Config.tabTitles,
      tabStyles: Config.tabStyles,
      tablist: [],
      demoList: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      tabPageHeight: 134
    }
  },
  created () {
    this.tabPageHeight = Utils.env.getPageHeight();
    this.tablist = [...Array(this.tabTitles.length).keys()].map(i => i);
    Vue.set(this.tablist, 0, this.demoList);
  },
  methods: {
    wxcTabPageCurrentTabSelected (e) {
      const self = this;
      const index = e.page;
      if (!Utils.isNonEmptyArray(self.tablist[index])) {
        // 未加载数据请求
      }
    }
  }
}
```

画面 8:
```javascript
{
  title: 'JAVA', id: 1,
  title: 'Python', id: 2,
  title: 'VUE', id: 3,
  title: 'WEEX', id: 4,
  title: '大数据', id: 5,
  title: 'Docker', id: 6,
  title: '其它', id: 0
},
tabStyles: {
  bgColor: '#FFFFFF',
  titleColor: '#B6665B',
  activeTitleColor: '#31D3D3',
  inactiveTitleBold: true,
  iconWidth: 70,
  width: 120,
  height: 80,
  fontSize: 24,
  hasActiveButton: true,
  activeBottomColor: '#31D3D3',
  activeBottomHeight: 6,
  textPaddingLeft: 10,
  textPaddingRight: 10,
  normalBottomColor: 'rgba(0,0,0,0.4)',
  normalBottomHeight: 2,
  hasRightIcon: false,
  rightOffset: 100
}
```

画面 9:
```javascript
export default {
  tabTitles: [
    { title: '动态', id: '_dyna_' },
    { title: '推荐', id: '_all_' },
    { title: 'JAVA', id: 1 },
    { title: 'Python', id: 2 },
    { title: 'VUE', id: 3 },
    { title: 'WEEX', id: 4 },
    { title: '大数据', id: 5 },
    { title: 'Docker', id: 6 },
    { title: '其它', id: 0 }
  ],
  tabStyles: {
    bgColor: '#FFFFFF',
    titleColor: '#B6665B',
    activeTitleColor: '#31D3D3',
    inactiveTitleBold: true,
    iconWidth: 70,
    width: 120,
    height: 80,
    fontSize: 24,
    hasActiveButton: true,
    activeBottomColor: '#31D3D3',
    activeBottomHeight: 6,
    textPaddingLeft: 10,
    textPaddingRight: 10,
    normalBottomColor: 'rgba(0,0,0,0.4)',
    normalBottomHeight: 2,
    hasRightIcon: false,
    rightOffset: 100
  }
}
```

画面 11:
```vue
<template>
  <div>
    <wxc-tab-page ref="wxc-tab-page"
      :tab-titles="tabTitles"
      :tab-styles="tabStyles"
      title-type="icon"
      tab-page-height="tabPageHeight"
      @wxcTabPageCurrentTabSelected="wxcTabPageCurrentTabSelected"
    >
      <list v-for="(demo, key) in tablist" :key="key">
        <cell v-for="(v, key) in v" :key="key">
          <wxc-pan-item text-id="1" + (v) + '+' + (key)
            url="https://HS.m.taobao.com/trip/ticket/detail/index.html?scnId=2675"
          >
            <div class="content">
              <text>{{(key)}}</text>
            </div>
          </wxc-pan-item>
        </cell>
      </list>
    </wxc-tab-page>
  </div>
</template>
``
