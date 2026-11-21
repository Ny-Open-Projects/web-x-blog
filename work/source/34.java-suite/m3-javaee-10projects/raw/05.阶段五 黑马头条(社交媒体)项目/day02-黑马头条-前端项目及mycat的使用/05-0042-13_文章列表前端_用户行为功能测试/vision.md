# 画面线理解：13_文章列表前端_用户行为功能测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\13_文章列表前端_用户行为功能测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:29, 01:08, 01:48, 02:28, 02:51, 03:14, 04:16, 04:33, 05:33, 06:20, 06:57, 07:21, 08:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:56:05

1) 这一组画面整体在讲一个基于 Weex 的前端应用如何通过 Vue.js 实现分页加载和行为数据保存功能，并在后端通过 Spring Boot + MyBatis 实现数据持久化。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Vue.js 配置文件中 proxyTable 的设置，用于代理请求到后端接口。
画面2：展示 MyBatis 的 XML 映射文件，定义了保存用户行为数据的 SQL 插入语句。
画面3：展示 Vue.js 中用于保存行为数据的 JavaScript 逻辑，包含 Promise 和 AJAX 请求。
画面4：展示 Spring Boot 后端的 Controller 层代码，接收前端请求并调用 Service 层。
画面5：展示 Spring Boot 后端的 Controller 层代码，方法签名和注解。
画面6：展示 Weex 预览界面，显示一个搜索页面，包含一个二维码。
画面7：展示 Weex 预览界面的 Network 面板，显示一个 500 Internal Server Error。
画面8：展示 MyBatis 的 XML 映射文件，定义了保存用户行为数据的 SQL 插入语句。
画面9：展示 Spring Boot 后端的 Controller 层代码，方法签名和注解。
画面10：展示 Vue.js 中用于加载数据的 JavaScript 逻辑，包含 AJAX 请求和数据处理。
画面11：展示 Vue.js 中用于加载数据的 JavaScript 逻辑，包含 AJAX 请求和数据处理。
画面12：展示 Vue.js 中用于加载数据的 JavaScript 逻辑，包含 AJAX 请求和数据处理。
画面13：展示 Vue.js 中用于加载数据的 JavaScript 逻辑，包含 AJAX 请求和数据处理。
画面14：展示 Weex 预览界面，显示一个搜索页面，包含一个二维码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```javascript
// with this option, according to the CSS-loader README
// (https://github.com/webpack/css-loader#source-map)
// (In my experience, they generally work as expected,
//  just be aware of this issue when enabling this option.
cssSourceMap: false,
proxyTable: {
  '/toutiao': {
    target: 'http://ip:9803/', //源地址
    changeOrigin: true, //改变源
    pathRewrite: {
      '^/toutiao': ''
    }
  },
  '/behavior': {
    target: 'http://ip:9804/', //源地址
    changeOrigin: true, //改变源
    pathRewrite: {
      '^/behavior': ''
    }
  }
},
autoOpenBrowser: false,
errorOverlay: true,
notifyOnErrors: true,
htmlOptions: {
  devScripts: '<script>
window.addEventListener('load', function () {
  // 代码省略
</script>'
}
```

画面2：
```xml
<select>
  <insert id="saveShowBehavior">
    insert into ap_show_behavior (id, entry_id, article_id, is_click, show_time, created_time) values
    <foreach collection="articleIds" item="item" separator=",">
      #{item.id}, #{item.new}, #{item.old}, #{item.time}, #{item.createdTime}
    </foreach>
  </insert>
</select>
```

画面3：
```javascript
// 保存行为数据
function (params) {
  let ids = [];
  for(let k in params){
    if(params[k]){
      ids.push({id:k});
    }
  }
  console.log(params);
  if(ids.length > 0){
    let url = this.vue.config.urls.get('show_behavior');
    return new Promise(resolve, reject) => {
      this.vue.$request.post(url, JSON.stringify({equipmentId:1, articleIds:ids})).then(d=>{
        d.data = ids;
        resolve(d);
      }).catch(e=>{
        reject(e);
      });
    }
  }
}

// 获取请求的URL
function (dir) {
  let url = this.vue.config.urls.get('load');
  if(dir === 'behavior'){
    url = this.vue.config.urls.get('behavior');
  }
  return url;
}
```

画面4：
```java
@Autowired
private AppShowBehaviorService appShowBehaviorService;

@Override
public String saveShowBehavior(ShowBehaviorDto dto) {
  return appShowBehaviorService.saveBehavior(dto);
}
```

画面5：
```java
@Autowired
private AppShowBehaviorService appShowBehaviorService;

@PostMapping("/save_behavior")
public ResponseResult saveShowBehavior(@RequestBody ShowBehaviorDto dto) {
  return appShowBehaviorService.saveBehavior(dto);
}
```

画面6：
无代码或配置。

画面7：
无代码或配置。

画面8：
```xml
<select>
  <insert id="saveShowBehavior">
    insert into ap_show_behavior (id, entry_id, article_id, is_click, show_time, created_time) values
    <foreach collection="articleIds" item="item" separator=",">
      #{item.id}, #{item.new}, #{item.old}, #{item.time}, #{item.createdTime}
    </foreach>
  </insert>
</select>
```

画面9：
```java
@Autowired
private AppShowBehaviorService appShowBehaviorService;

@PostMapping("/save_behavior")
public ResponseResult saveShowBehavior(@RequestBody ShowBehaviorDto dto) {
  return appShowBehaviorService.saveBehavior(dto);
}
```

画面10：
```javascript
// 列表数据
load() {
  // 发送请求，并且获取到数据，把数据展示到页面上
  request.get('/toutiao/api/v1/article/load', this.params).then((res) => {
    this.tanfer(res.data);
  });
}

tanfer: function (data) {
  let arr = [];
  for (let i = 0; i < data.length; i++) {
    let tmp = {
      id: data[i].id,
      title: data[i].title,
      comment: data[i].comment,
      source: data[i].authorName,
      date: data[i].publishTime,
      type: data[i].layout
    };
    arr.push(tmp);
  }
  this.data = arr;
}
```

画面11：
```html
<cell>
  <!-- 上来加载更多 -->
  <loading :loading="load" :display="showmore" :show="hide" class="loading">
    <loading-indicator class="loading-icon"></loading-indicator>
    <text class="loading-text">{{load_more_text}}</text>
  </loading>
</cell>
```

画面12：
```javascript
import Home_Bar from '@/components/bars/home_bar.vue';
import request from '@/common/request';
const dom = weex.requireModule('dom');
import { WxcTabPage, WxcPanItem, Utils, BindEnv } from 'weex-ui';
import Item0 from '@/components/cells/article_0.vue';
import Item1 from '@/components/cells/article_1.vue';
import Item2 from '@/components/cells/article_2.vue';
import Item3 from '@/components/cells/article_3.vue';
import Config from '@/apis/home/api';
import Api from '@/apis/home/api';
const modal = weex.requireModule('modal');
```

画面13：
```javascript
tabStyles: Config.tabStyles, // 样式
tabPageHeight: 134, // 外表高度
params: {
  loadId: 1,
  index: 0,
  tag: "_all_",
  size: 10,
  min_behot_time: 0,
  max_behot_time: 200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
