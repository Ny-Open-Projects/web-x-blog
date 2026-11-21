# 07_weex_内置模块stream发送http异步请求

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\07_weex_内置模块stream发送http异步请求【海量资源尽在 666java.com】.mp4
- 时长 4分56秒（音频 296s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下讲刚才呢咱们是把当前的一个这种组件啊大概去介绍了一下然后下面呢是有一个这种内置模块里边大家有一个是必须要掌握的哎嗯这些组件呢其实咱们只要掌握呢有一个就可以啊就是当前的stream那stream里边呢其实呢就是可以啥呢你看读一下啊模块啊stream模块提供了基本的网络请求能力例如get请求post请求
[00:28] 用于在组件寿命周期内与服务端与服务端进行交互那咱们这个文章内容需要去拿到咱们微服务的一些数据是吧所以说咱们在前端的话要去调用后端的请求那用的就是当前这个Stream当前这个内置模块好那里边那怎么去用呢首先有一个FetchFetch里边是有一些参数参数的话大家也能看明白比如看第一个MyThird
[00:56] 你可以去发送什么get post put delete等像这些通用的这种请求呢关于http rest的请求呢咱们都有是吧好url的话咱们就是某一个请求的路径就可以了hiders你可以去设置一个请求头然后type呢到底是json的textjsonp都可以设置还有body咱们在比如说我要去从前台往后的去传一些数据的时候
[01:22] 咱们可以去传Body但是这里边是个String的形状当然传Jason的四股串就可以这里边有些注意事项咱们也可以来读一读说Body才说仅支持String他请勿直接传递Jason不要传对象你直接把Jason转成一个什么转成一个四股串就可以好吧然后还有第二个第二个注意事项说Gate请求不支持Body
[01:48] 方式传递参数你要干嘛呢你要去给它使用UR传参也就是说使用网号的方式拼接到UR上就可以了好吧然后下面还有一下模拟的content type是它这个知道一下它是一个表单然后如果说你使用通过pulse请求发送接载数据需要将当前的content type设置为啥呢application-gis好那这就是注意事项当然那这个设置完之后还有些回调函数那回调函数里边咱们就可以去拿到这些
[02:18] 从后台请求的数据然后再给页面去复制就可以了这样有个callback现在这个咱们现在直接可以看一些例子比如说http master的智力怎么打开在完之后怎么往下翻往下翻就主要看这个单本你看当前有一个stream然后有个feat是吧然后是master的我是get请求这是请求的url然后type是一个jsonp的请求
[02:48] 请求的方式然后下面还有还有啊就是你最终要返回的话呢哎我这个ret就retout是吧就应该去return啊我最终的时候可以拿到一些值是吧成功之后拿到这个值失败之后我要去怎么去提示是吧然后这是get啊当然我可以去改成啊是get没有问题但是还有一个什么type是json的方式也是可以的
[03:11] 然后post请求里边呢咱们也可以去指定是吧在method里边去指定你到底是get post或者是put delete这些都是可以的没问题再往下看这里边还有一个post那post呢重点呢咱们要看一下这个参数或者咱们的这种请求的参数怎么去封装好往下看比如说当前的就是一个post你看当前它是一个body那body的话它本身的是一个啥呢
[03:40] 是一个比如说他本身是一个JSON但是不行啊怎么办怎么办呢你要先从这种JSON转成字符串然后再把body复到这就可以了一定要注意啊他转成一个字符串然后再往后传就行然后这是这是Pulse的请求啊然后下面还有一个就是GET请求好来看一下啊那GET请求的话呢咱们也是看当前的这种请求方式就可以了啊比如最终你看啊GET是吧GET请求UR
[04:10] 然后type是json然后这个并没有传参那咱们下面是是有一个传参的啊传参的话呢你直接去拼接到当前的URL上面就可以了OK啊那这就是get请求的一种方式那这个我就不在这去演示了为啥呢因为呢这个里边呢是咱们是有一个前后端分离开发然后呢这个可能会出现一个跨域的问题啊
[04:36] 所以说咱们要调的话不太好调咱们一会儿再去集成咱们的页面列表展示的时候啊文章列表展示的时候咱们会重点再去说一下好吧呃行啊那这个就是当前的一个这种怎么去用使用vigs啊去发送http的请求好那这个咱们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

