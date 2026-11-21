# 画面线理解：10_文章列表前端_http请求后台数据

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\10_文章列表前端_http请求后台数据【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:48, 01:41, 02:34, 03:42, 04:41, 06:07, 06:38, 07:54, 08:36, 09:08, 09:46, 10:47, 11:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:53:25

1) 这一组画面整体在讲如何在 Weex 项目中集成并使用 `wxc-tab-page` 组件，实现标签页功能，并通过自定义请求模块与后端 API 交互。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 WebStorm 中编辑 `src/pages/home/index.vue` 文件，导入 `wxc-tab-page` 组件并配置其属性，如 `tabTitles`、`tabStyles`、`tabList` 和 `tabPageHeight`。
画面 2: 继续编辑 `index.vue`，在 `methods` 中定义 `wxcTabPageCurrentTabSelected` 方法，用于处理标签页切换事件。
画面 3: 在浏览器中打开 Weex Playground 的 `wxc-tab-page` 文档页面，查看其可配置参数表，包括 `tab-titles`、`tab-type`、`tab-page-height` 等。
画面 4: 在 Weex Preview 中预览一个包含二维码的页面，提示使用 Weex playground app 扫码。
画面 5: 在 Typora 中查看文档，内容为“2.2.1 在 src/pages/home/index.vue 中定义 Model”。
画面 6: 在 WebStorm 中编辑 `index.vue`，在 `mounted` 生命周期钩子中调用 `this.$refs['wxc-tab-page'].setPage(1)` 设置默认选中标签页。
画面 7: 在 WebStorm 中编辑 `index.vue`，在 `methods` 中定义 `load` 方法，用于发起数据请求。
画面 8: 在 WebStorm 中编辑 `src/common/request.js` 文件，定义 `post` 和 `get` 方法，用于封装 HTTP 请求。
画面 9: 在 WebStorm 中编辑 `index.vue`，在 `methods` 中定义 `request.get` 方法，用于发起 GET 请求。
画面 10: 在 IDEA 中查看 `ArticleHomeController` 类的源码，其中定义了 `countId`、`maxBhotTime`、`minBhotTime`、`size` 和 `tag` 等属性。
画面 11: 在 WebStorm 中编辑 `index.vue`，在 `methods` 中定义 `request.get` 方法，用于发起 GET 请求。
画面 12: 在 Weex Preview 中显示编译失败的错误信息，提示找不到 `common/request` 模块。
画面 13: 在 WebStorm 中编辑 `index.vue`，在 `template` 中定义 `wxc-pan-item` 组件，并在 `script` 中导入 `request` 模块。
画面 14: 在浏览器的开发者工具中查看网络请求，显示已加载的资源和请求状态。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 1:
```javascript
<script>
import Home_Bar from '@/components/bars/home_bar.vue';
const dom = weex.requireModule('dom');
import { WxcTabPage, WxcPanItem, Utils, BindEnv } from 'weex-ui';
import Config from './config';
export default {
  components: [WxcTabPage, WxcPanItem, Home_Bar],
  data () {
    tabTitles: Config.tabTitles,
    tabStyles: Config.tabStyles,
    tabList: [],
    demoList: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    tabPageHeight: 1334
  },
  created () {
    this.tabPageHeight = Utils.env.getPageHeight();
    this.tabList = [...Array(this.tabTitles.length).keys().map(i => i)];
  },
  methods: {
    wxcTabPageCurrentTabSelected (e) {
      const self = this;
      const index = e.page;
      if (Utils.isNonEmptyArray(self.tabList)) {
        setUtils(() => {
          this.tabList = [...Array(this.tabTitles.length).keys().map(i => i)];
        });
      }
    }
  }
};
</script>
```

画面 3:
```html
<table>
  <thead>
    <tr>
      <th>可配置参数</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>tab-titles</td>
      <td>Array</td>
      <td>Y</td>
      <td>[]</td>
      <td>顶部显示标题</td>
    </tr>
    <tr>
      <td>tab-type</td>
      <td>String</td>
      <td>N</td>
      <td>icon</td>
      <td>显示类型 icon / text / iconFont (注)</td>
    </tr>
    <tr>
      <td>tab-page-height</td>
      <td>Number</td>
      <td>N</td>
      <td>1334</td>
      <td>Tab page 页面的高度</td>
    </tr>
    <tr>
      <td>is-tab-bar</td>
      <td>Boolean</td>
      <td>N</td>
      <td>true</td>
      <td>当设置为 false，同时 tab 配置 url 参数即可出现</td>
    </tr>
  </tbody>
</table>
```

画面 5:
```markdown
2.2.1 在 src/pages/home/index.vue 中定义 Model
```

画面 6:
```javascript
mounted() {
  this.$refs['wxc-tab-page'].setPage(1);
},
```

画面 7:
```javascript
methods: {
  load () {
    // 发送请求，并且获取到数据，把数据展示到页面上
    // url: "",
    // type: ""
  },
  wxcTabPageCurrentTabSelected (e) {
    const self = this;
    const index = e.page;
    alert(e.page);
    this.load();
  },
  wxcPanItemPan (e) {
    if (BindEnv.supportsForAndroid()) {
      this.$refs['wxc-tab-page'].bindExp(e.element);
    }
  }
},
```

画面 8:
```javascript
if (!this.stream) {
  this.stream = weex.requireModule('stream');
  return this.stream;
}

post: function (path, body) {
  let stream = this._check();
  return new Promise((resolve, reject) => {
    stream.fetch({
      method: 'POST',
      url: path,
      type: 'json',
      body: body
    }, (response) => {
      if (response.status == 200) {
        resolve(response.data);
      } else {
        reject(response);
      }
    }, () => {
    });
  }),
  get: function (path, params) {
    let stream = this._check();
    if (params) {
      let tmp = querystring.stringify(params);
      if (path.indexOf('?') == -1) {
        tmp = '?' + tmp;
      } else {
        tmp = '&' + tmp;
      }
      path += tmp;
    }
    return stream.get(path);
  }
```

画面 9:
```javascript
methods: {
  request.get (url, params) {
    const self = this;
    const index = e.page;
    alert(e.page);
    this.load();
  }
},
```

画面 10:
```java
Integer countId;
// 最大时间
Date maxBhotTime;
// 最小时间
Date minBhotTime;
// 分页大小
Integer size;
// 资源范围，比如频道 ID
String tag
```

画面 11:
```javascript
methods: {
  request.get (url, params) {
    const self = this;
    const index = e.page;
    alert(e.page);
    this.load();
  }
},
```

画面 12:
```text
failed to compile.
./node_modules/babel-loader/lib/.node_modules/vue-loader/lib/selector.js?type=script&index=0!./src/pages/home/index.vue
Module not found: Can't resolve 'common/request' in 'D:\heima\leadnews.code\heima-leadnews-app\src\pages\home'
```

画面 13:
```html
<wxc-pan-item text-id="1" + (v) + ' + ' + (key)>
  <div class="content">
    <text>{{key}}</text>
  </div>
</wxc-pan-item>
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 3: 展示了 Weex Playground 中 `wxc-tab-page` 组件的配置参数表，表格包含列：可配置参数、Type、Required、Default、Description。
画面 5: 展示了文档内容，标题为“2.2.1 在 src/pages/home/index.vue 中定义 Model”。

5) 无。
