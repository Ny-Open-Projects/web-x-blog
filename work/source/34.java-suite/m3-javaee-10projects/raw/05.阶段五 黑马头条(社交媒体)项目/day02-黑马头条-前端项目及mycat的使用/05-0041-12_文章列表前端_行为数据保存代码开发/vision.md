# 画面线理解：12_文章列表前端_行为数据保存代码开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\12_文章列表前端_行为数据保存代码开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:12, 01:42, 02:24, 02:57, 04:02, 05:06, 05:56, 07:08, 07:42, 08:28, 08:48, 09:22, 09:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:55:07

1) 这一组画面整体在讲一个前端页面（文章列表页）如何通过 Vue.js 实现分页加载、用户行为记录（如点赞、收藏）以及与后端服务（Spring Boot）交互的完整流程。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程文档目录结构，重点在“6.5 多环境切换”和“7.1 文章列表需求分析”，并附带一个关于“文章首页”功能的流程图，说明用户登录状态影响文章加载，以及“用户点击文章列表进行操作”后会“记录用户行为”。
画面2：展示一个手机端网页预览界面，包含搜索框、文章列表和底部导航栏，右侧有一个二维码，提示使用 Weex playground app 扫描。
画面3：在 WebStorm 中打开 `src/pages/index.vue` 文件，展示 Vue 组件的 `export default` 部分，包含 `components`、`data`、`created`、`mounted`、`methods` 等生命周期钩子和方法，其中 `data` 中定义了 `tabTitles`、`tabStyles`、`tablist`、`loaddir`、`index`、`tag`、`size`、`max_bohot_time`、`min_bohot_time` 等变量。
画面4：展示 `index.vue` 文件中 `<template>` 部分的 HTML 结构，包含一个 `<div>` 包裹的 `<wx-tab-page>` 组件，以及 `<script>` 部分导入了 `Home_Bar`、`request`、`WxcTabPage`、`WxcPanItem`、`Utils`、`BindEnv` 等模块。
画面5：展示 `index.vue` 文件中 `methods` 部分的 `load()` 方法，其中包含 `request.get('/toutiao/api/v1/article/load', this.params).then((res) => { this.tanfer(res.data); })` 用于发起网络请求并处理返回数据。
画面6：展示 `index.vue` 文件中 `methods` 部分的 `show(id)` 方法，其中包含 `if (this.ashow[id] === undefined) { this.ashow[id] = true; }` 用于记录用户行为。
画面7：展示 `index.vue` 文件中 `methods` 部分的 `load()` 方法，其中包含 `this.shownew = true; this.params.loaddir = 0; this.load();` 用于重置加载状态并重新加载数据。
画面8：展示 `index.vue` 文件中 `created()` 钩子中的 `Api.saveShowBehavior(this.ashow)` 调用，用于保存用户行为。
画面9：展示 `index.vue` 文件中 `load()` 方法内部的 `tanfer` 函数，用于将数据转换为 Model 对象，其中包含 `for (let i = 0; i < data.length; i++) { let tmp = { id: data[i].id, title: data[i].title, comment: data[i].comment, }`。
画面10：展示 `index.vue` 文件中 `import Api from '@/apis/home/api.js'`，并展示 `export default` 部分的 `data` 中定义的 `loaddir`、`index`、`tag`、`size`、`max_bohot_time`、`min_bohot_time` 等变量。
画面11：展示浏览器开发者工具中的 Network 面板，显示了多个资源的加载情况，包括 `404` 状态的 `text/html` 和 `200` 状态的 `png` 文件。
画面12：在 WebStorm 中打开 `src/configs/webpack.dev.conf.js` 文件，展示 `proxyTable` 配置，其中包含 `'/toutiao': { target: 'http://api.toutiao.com', changeOrigin: true, pathRewrite: { '^/toutiao': '' } }` 和 `'/behavior': { target: 'http://api.toutiao.com', changeOrigin: true, pathRewrite: { '^/behavior': '' } }`。
画面13：在 IntelliJ IDEA 中打开 `BehaviorController.java` 文件，展示 `saveShowBehavior` 方法，其中包含 `return appShowBehaviorService.saveShowBehavior(dto);`。
画面14：再次展示 `src/configs/webpack.dev.conf.js` 文件中 `proxyTable` 配置，内容与画面12相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```javascript
import Item from '@/components/cells/article_3.vue'
import Config from './config'
export default {
  components: { WxcTabPage, WxcPanItem, Home_Bar, Item0, Item1, Item },
  data () -> {
    tabTitles: Config.tabTitles,
    tabStyles: Config.tabStyles,
    tablist: [],
    showmore: false,
    demolist: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    tabPageHeight: 1334,
    load_more_text: '加载更多...',
    load_new_text: '加载更新...',
    params: {},
  },
  created () {
    this.tabPageHeight = Utils.getPageSize();
    this.tablist = [...Array(this.tabTitles.length).keys()].map(i => {});
  },
  mounted () {
    this.$refs['wxc-tab-page'].setPage(1)
  },
  methods: {
    loaddir: 1,
    index: 0,
    tag: 'all_',
    size: 20,
    max_bohot_time: 1559789043,
    min_bohot_time: 1559789043,
  },
}
```

画面4：
```html
<div>
  <wx-tab-page>
  </wx-tab-page>
</div>
<script>
import Home_Bar from '@/components/bars/home_bar.vue'
import request from '@/common/request'
const dom = weex.requireModule('dom');
import { WxcTabPage, WxcPanItem, Utils, BindEnv } from 'weex-ui';
import Item0 from '@/components/cells/article_3.vue'
import Item1 from '@/components/cells/article_3.vue'
import Item from '@/components/cells/article_3.vue'
import Config from './config'
import Api from '@/apis/home/api.js'
export default {
  components: { WxcTabPage, WxcPanItem, Home_Bar, Item0, Item1, Item },
  data () -> {
    tabTitles: Config.tabTitles,
    tabStyles: Config.tabStyles,
    tablist: [],
    showmore: false,
    demolist: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    tabPageHeight: 1334,
    load_more_text: '加载更多...',
    load_new_text: '加载更新...',
    params: {},
  },
}
```

画面5：
```javascript
methods: {
  load () {
    this.shownew = true;
    this.params.loaddir = 0;
    this.load();
  },
  load () {
    // 发送请求，并且获取到数据，视频展示到页面上
    request.get('/toutiao/api/v1/article/load', this.params).then((res) => {
      this.tanfer(res.data);
    })
  }
}
```

画面6：
```javascript
methods: {
  show (id) {
    // 没有进行存储id赋值为ture，保存之后的id为false
    if (this.ashow[id] === undefined) {
      this.ashow[id] = true;
    }
  }
}
```

画面7：
```javascript
methods: {
  load () {
    this.shownew = true;
    this.params.loaddir = 0;
    this.load();
  },
  load () {
    // 发送请求，并且获取到数据，视频展示到页面上
    request.get('/toutiao/api/v1/article/load', this.params).then((res) => {
      this.tanfer(res.data);
    })
  }
}
```

画面8：
```javascript
created () {
  this.tabPageHeight = Utils.getPageSize();
  this.tablist = [...Array(this.tabTitles.length).keys()].map(i => {});
  let this = this;
  let timer = setTimeout(function () {
    let result = Api.saveShowBehavior(this.ashow);
    result.then((d) => {
      // 标记已经处理完成
      let ids = d.data;
      for (let i = 0; i < ids.length; i++) {
        this.ashow[ids[i].id] = false;
      }
    });
  }, 5000);
}
```

画面9：
```javascript
tanfer: function (data) {
  for (let i = 0; i < data.length; i++) {
    let tmp = {
      id: data[i].id,
      title: data[i].title,
      comment: data[i].comment,
    }
  }
}
```

画面10：
```javascript
import Api from '@/apis/home/api.js'
export default {
  components: { WxcTabPage, WxcPanItem, Home_Bar, Item0, Item1, Item },
  data () -> {
    loaddir: 1,
