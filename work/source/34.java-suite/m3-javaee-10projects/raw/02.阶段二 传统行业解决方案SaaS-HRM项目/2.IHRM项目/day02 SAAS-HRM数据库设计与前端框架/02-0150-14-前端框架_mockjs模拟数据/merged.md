# 14-前端框架：mockjs模拟数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\14-前端框架：mockjs模拟数据_【海量资源尽在 ubkz.com】.mp4
- 时长 6分48秒（音频 409s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 好了我们这个框架的执行逻辑呢做了一个简单的说明那接下来呢其实我们可以把这个页面呢给它打开这个页面给它打开我们来分析一下就是当前这个页面究竟有没有发送请求啊好了那接着在这边呢刷新一把所有的表格都已经帮我们填充起来了那我们来验证一把就是说当我SaaS Client Index它会找到页面
[00:33] 那找到页面执行里面的credit方法credit方法又调用了一个什么是get list就在上面method的部分那获取数据那获取数据里面做了一件事list.这个list方法在哪呢各位来看import进来那import进来从哪里import的我们一起来找一下它从API下exampletable能找到table里面恰巧定义了一个方法叫做list
[01:01] 那这个list它说要去访问某一个地址并且是以get形式请求的好了这个就是它整个的跳准到请求发送请求那发送请求之后再回来再来看zin代表的是你得到请求的响应数据那得到响应数据res.data.item指的是把这个数据格式里面的内容存放到类似点data list里面
[01:32] 好了那list and delist这样一来就已经有了数据列表那这个datalist在上边这不就是我们的数据模型吗那这个datalist那哪还用呢它应该在页面部分也有所以你会发现底下一发生变化页面不就紧接着也做了变化没错吧好了这个我们看过了之后那接下来我想跟各位来聊的就是说呢我们可以在我们的浏览器端F12打开它F12打开它那我这边呢
[02:03] 走demo把这个关掉network走你会发现呀它并没有发送任何请求我再关掉再来它并没有发送任何请求这是为什么呀注意这个就是我要跟各位来聊的就是说呢对于我们前端进行开发的时候有可能你后端代码还没写好那这个时候怎么办呢我们就可以自己构造一点假的数据来进行展示
[02:35] 那我们自己构造假的数据这边借助的是一个叫做moke.js那这个moke.js呢各位可以有兴趣的话百度查一下如果没兴趣的话咱们来看在这个工程里面怎么用其实就可以了那如果各位我没记错的话我们请求的接口地址是一大堆后面有一个table后面有个ganglist没错了那接着在我这个工程原码当中src部分其中有一个moke这个moke里面找到index.js
[03:05] 这里面会有如下这么一些配置其中有一个table-list各位来看各位来看刚才请求我们发送的json在抱歉我要找一下table好了这边我发送的请求不就是table-list而我这边mook里面拦截的注意这配置的是一个它的UIL拦截的一个规则它指的是如果发送请求的发送请求的API路径
[03:42] 匹配的话它会进行拦截拦截到了之后它交给谁处理后面注意前面指的是我们的这边我写一下第一个参数匹配的请求API路径第二个参数指的是匹配请求的方式我们有get post等等第三个参数指的是你拦截到了匹配的路径我这回获取的响应
[04:18] 数据如何替换它指的是获取响应路数响应如何替换那我们替换成什么我们刚才请求的不就是符合它的规则吗table.list符合规则那get也符合那匹配这回它交给谁了它拦截了之后交给table.list那table.list在哪呢注意点杠当前路径里找table那table.list打点它有个例子方法那不就在这吗所以
[04:50] 我们可以简单的理解虽然我API写的都正确但是由于我有MockJS存在它其实并没有发送真正的请求而变成我自己构造或者我自己模拟出来那同理在这里面呢还有其他的一些配置比如说我这边有Login比如说我有Profile那这个Profile我也跟各位简单的解释一下它指的是获取用户信息的获取用户信息的那获取用户信息是我登录成功之后立马获取
[05:22] 登录成功之后立马获取那我请求的路径呢frame pre-profile那这frame pre-profile post这都是我们请求路径那接下来他交给谁profile API点profile那profile API还是点杠里面去找profile找到了那我们得到的是一个叫做profile这么一个方法那这个手机响了我关掉这里面的profile方法那各位来看各位来看我返回的数据里面有电话
[05:56] 有张三一二三四有传辑博客等等等一大堆比如说这边我变成张三OK有NIM那各位来看上面不是也变成叫做张三OK了吧那所以我们前端进行数据模拟是借助MOOC JS来做的当然了MOOC JS也比较简单其实你这样看不就是一个JS对象吗当然了这个JS对象不是我随便构造的它符合我们的API规范
[06:25] 它符合我们的API规范当然了这里面全部都是构造的响应的一些数据OK那这样一来我们整个项目执行流程咱们就已经都说过了其实我这边没有发送请求没有发送请求而是借助我们的MOKS是不是自己模拟的OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Vue 项目中通过 mock.js 模拟 API 请求，以实现前端数据的本地化展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 HRM 系统的登录或首页界面，页面显示“demo页面”，并有“首页”、“demo”等导航项。
画面 2：展示 HRM 系统的“操作日志”列表页，包含“操作类型”、“操作人”、“执行结果”、“操作时间”、“描述”等列。
画面 3：在 Visual Studio Code 中打开 `index.Vue` 文件，展示用于渲染表格的 Vue 模板代码，包含多个 `<el-table-column>` 定义。
画面 4：在浏览器开发者工具中，点击“首页”按钮后，页面跳转至“/dashboard”路径，同时开发者工具显示“[MP] waiting for update signal from HMR...”。
画面 5：在 Visual Studio Code 中，`index.Vue` 文件的编辑器中，光标位于 `<template>` 标签内，显示表格结构代码。
画面 6：在 Visual Studio Code 中，打开 `mock/index.js` 文件，展示 mock.js 的初始化配置和对 `/VtableV1/list`、`/VframeV1/profile`、`/VframeV1/login` 三个接口的模拟。
画面 7：在 `mock/index.js` 文件中，光标位于 `Mock.mock(...)` 的参数位置，输入“1”并选择“1”作为参数。
画面 8：在 `mock/index.js` 文件中，光标位于 `Mock.mock(...)` 的参数位置，输入“1”并选择“1”作为参数。
画面 9：在 `mock/index.js` 文件中，光标位于 `Mock.mock(...)` 的参数位置，输入“1”并选择“1”作为参数。
画面 10：在 Visual Studio Code 中，鼠标悬停在 `index.Vue` 文件标签页上。
画面 11：在 Visual Studio Code 中，鼠标悬停在 `table.js` 文件标签页上。
画面 12：在 Visual Studio Code 中，打开 `table.js` 文件，展示一个用于处理分页和过滤的 JavaScript 函数，包含 `list: config`, `mocklist.filter`, `mocklist.reverse`, `mocklist.filter` 等逻辑。
画面 13：在浏览器开发者工具的 Network 面板中，显示了对 `localhost:8080` 的请求，状态码为 304 和 200，表明页面已成功加载。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3：
```Vue
<template>
  <el-table :data="datalist" fit highlight-current-row style="width: 100%" border>
    <el-table-column align="center" label="table.operationtype">
      <template slot-scope="scope">
        <span>{{scope.row.type}}</span>
      </template>
    </el-table-column>
    <el-table-column align="center" label="table.operator">
      <template slot-scope="scope">
        <span>{{scope.row.author}}</span>
      </template>
    </el-table-column>
    <el-table-column align="center" label="table.results">
      <template slot-scope="scope">
        <span>{{scope.row.title}}</span>
      </template>
    </el-table-column>
    <el-table-column align="center" label="table.operationdate">
      <template slot-scope="scope">
        <span>{{scope.row.display_time}}</span>
      </template>
    </el-table-column>
    <el-table-column align="center" label="table.describe">
      <template slot-scope="scope">
        <span>{{scope.row.forecast}}</span>
      </template>
    </el-table-column>
  </el-table>
</template>
```

画面 6：
```javascript
import Mock from 'mockjs';
import tableAPI from '@/table';
import ProfileAPI from '@/profile';
import LoginAPI from '@/login';

Mock.setup({
  // timeout: 1000
});

Mock.mock(/VtableV1\/list/, 'get', tableAPI.list);
Mock.mock(/VframeV1\/profile/, 'post', ProfileAPI.profile);
Mock.mock(/VframeV1\/login/, 'post', LoginAPI.login);
```

画面 12：
```javascript
export default {
  list: config => {
    const { type, page, limit = 20, sort } = paramObj(config.url);
    let mocklist = list.filter(item => {
      if (type && item.type !== type) return false;
      if (title && item.title.indexOf(title) < 0) return false;
      return true;
    });

    if (sort === '-id') {
      mocklist = mocklist.reverse();
    }

    const pagelist = mocklist.filter((item, index) => index < limit * page && index >= limit * (page - 1));

    return {
      total: mocklist.length,
      items: pagelist
    };
  }
};
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

