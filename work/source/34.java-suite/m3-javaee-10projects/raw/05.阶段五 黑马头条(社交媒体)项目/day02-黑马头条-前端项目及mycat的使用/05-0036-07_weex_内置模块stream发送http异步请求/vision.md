# 画面线理解：07_weex_内置模块stream发送http异步请求

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\07_weex_内置模块stream发送http异步请求【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:47, 02:22, 02:26, 02:36, 02:50, 03:11, 03:22, 03:32, 03:55, 04:02, 04:05, 04:15, 04:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:50:30

1) 这一组画面整体在讲什么（一句话）：
讲解 WeeX 框架中 stream 模块的 fetch API 使用方法，包括配置选项、回调函数、以及实际的网络请求示例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 WeeX 官方文档中 stream 模块的 fetch API 介绍，重点是 options 配置项中的 method、url、headers、type、body。
画面 2: 保持与画面 1 相同内容，鼠标光标在 method 选项的 GET/POST/PUT/DELETE/PATCH/HEAD 上。
画面 3: 展示 fetch API 的 @callback 和 @progressCallback 回调函数的参数说明。
画面 4: 保持与画面 3 相同内容，鼠标光标在 @progressCallback 的 readyState 参数上。
画面 5: 展示 WeeX Playground 中的 Vue 代码，使用 stream.fetch 发起 GET、POST、PUT、DELETE 请求，右侧手机预览显示请求方法和响应数据。
画面 6: 保持与画面 5 相同内容，鼠标光标在代码中 POST 请求的 type 设置为 json。
画面 7: 保持与画面 5 相同内容，鼠标光标在代码中 PUT 请求的 type 设置为 json。
画面 8: 返回 WeeX 官方文档，展示 fetch API 的 TIP 部分，说明默认 Content-Type 和如何设置 JSON 数据。
画面 9: 展示 WeeX Playground 中的 Vue 代码，用于创建文章，包含 title 和 article 字段。
画面 10: 保持与画面 9 相同内容，鼠标光标在代码中设置 body 为 JSON 字符串，并在 success 回调中更新 article。
画面 11: 浏览器页面空白，无内容。
画面 12: 展示 WeeX Playground 中的 Vue 代码，用于获取热门动漫列表，包含 dom、stream、modal、scroll 等模块。
画面 13: 保持与画面 12 相同内容，鼠标光标在代码中设置 offset 为 0，并在 success 回调中更新 items。
画面 14: 保持与画面 13 相同内容，手机预览显示“Top Airing Anime”列表，包含动漫信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
fetch(options, callback, progressCallback)
  @options,请求的配置选项,支持以下配置
    o method, string, HTTP 请求方法, 值为 GET / POST / PUT / DELETE / PATCH / HEAD
    o url, string, 请求的 URL string
    o headers, string, HTTP 请求头
    o type, string, 编码类型: json 或 text 或 json (在 native 原生实现中其实与 json 相同)
    o body, string, HTTP 请求体
```

画面 3:
```
@callback 应对结果回调，回调函数接收到的 _response 对象：
  o status, number, 返回的状态码
  o ok, boolean, 如果状态码在 200-299 之间则为 true
  o statusText, string, 状态描述文本
  o data, string, 返回的数据，如果接受类型是 json 和 json，则它就是一个 object，否则是一个 string。
  o headers, object, HTTP 响应头

@progressCallback, function, a progress callback. This callback will be invoked before request finished.
  o readyState, number, 当前状态。1：请求连接中；2：返回响应头中；3：正在加载返回数据
  o status, number, 返回的状态码
  o length, number, 已经接受到的数据长度 你可以从响应头中获取长度
  o statusText, string, 状态描述文本
  o headers, object, HTTP 响应头
```

画面 4:
```
TIP
  • 默认的 Content-Type 为 application/x-www-form-urlencoded。fetch 方法中设置的 type 是响应类型。
  • 如果要发送 JSON 数据，需要设置 Content-Type 为 application/json。
```

画面 5:
```
<script>
  const stream = weex.requireModule('stream');
  export default {
    data: function () {
      return {
        postResult: 'loading...',
        putResult: 'loading...',
        deleteResult: 'loading...',
        get1Result: 'loading...',
        get2Result: 'loading...',
        get3Result: 'loading...',
        get4Result: 'loading...',
        get5Result: 'loading...'
      }
    },
    methods: {
      test: function () {
        var GET_URL = 'http://api.dota2.net/tehe/samp/callback-anything-result-content-type=application/json';
        var POST_URL = 'http://httpbin.org/post';
        var PUT_URL = 'http://httpbin.org/put';
        var DELETE_URL = 'http://httpbin.org/delete/488';
        var PATCH_URL = 'http://httpbin.org/patch';
        stream.fetch({
          method: 'GET',
          url: GET_URL,
          type: 'json'
        }, function (ret) {
          console.log('get1 result: ' + ret.data);
        }, function (ret) {
          console.log('get1 progress: ' + ret.length);
        });
        stream.fetch({
          method: 'POST',
          url: POST_URL,
          type: 'json'
        }, function (ret) {
          console.log('post result: ' + ret.data);
        }, function (ret) {
          console.log('post progress: ' + ret.length);
        });
        stream.fetch({
          method: 'PUT',
          url: PUT_URL,
          type: 'json'
        }, function (ret) {
          console.log('put result: ' + ret.data);
        }, function (ret) {
          console.log('put progress: ' + ret.length);
        });
        stream.fetch({
          method: 'DELETE',
          url: DELETE_URL,
          type: 'json'
        }, function (ret) {
          console.log('delete result: ' + ret.data);
        }, function (ret) {
          console.log('delete progress: ' + ret.length);
        });
        stream.fetch({
          method: 'PATCH',
          url: PATCH_URL,
          type: 'json'
        }, function (ret) {
          console.log('patch result: ' + ret.data);
        }, function (ret) {
          console.log('patch progress: ' + ret.length);
        });
      }
    }
  }
</script>
```

画面 9:
```
<template>
  <div>
    <input type="text" v-model="title" placeholder="请输入文章标题" />
    <textarea v-model="article" placeholder="请输入文章正文"></textarea>
    <button @click="submit">提交</button>
  </div>
</template>

<script>
  const stream = weex.requireModule('stream');
  export default {
    data: function () {
      return {
        title: '',
        article: '',
        loading: false
      }
    },
    methods: {
      submit: function () {
        if (!this.title || !this.article) {
          modal.toast({
            message: '文章标题和正文不能为空。',
            duration: 2
          });
          return;
        }
        this.loading = true;
        stream.fetch({
          method: 'POST',
          url: 'https://api.example.com/articles',
          type: 'json',
          body: JSON.stringify({
            title: this.title,
            article: this.article
          })
        }, function (ret) {
          if (ret.ok) {
            modal.toast({
              message: '提交成功！',
              duration: 2
            });
            this.title = '';
            this.article = '';
            this.loading = false;
          } else {
            modal.toast({
              message: '提交失败！',
              duration: 2
            });
            this.loading = false;
          }
        }, function (ret) {
          console.log('提交中...');
        });
      }
    }
  }
</script>
```

画面 12:
```
<template>
  <div>
    <div class="item-info detail">
      <text class="title">{{item.title}}</text>
      <text class="desc">{{item.desc}}</text>
      <image class="img" :src="item.img"></image>
    </div>
    <div class="loadmore">
      <text class="loadmore-text">加载更多</text>
    </div>
  </div>
</template>

<script>
  const dom = weex.requireModule('dom');
  const stream = weex.requireModule('stream');
  const modal = weex.requireModule('modal');
  const scroll = weex.requireModule('scroll');
  export default {
    data: {
      items: [],
      offset: 0
    },
    methods: {
      loadMore: function (e) {
        const self = this;
        const offset = this.items.length;
        stream.fetch({
          method: 'GET',
          url: 'https://api.example.com/anime?offset=' + offset,
          type: 'json'
        }, function (ret) {
          if (ret.ok) {
            self.items = self.items.concat(ret.data);
          } else {
            modal.toast({
              message
