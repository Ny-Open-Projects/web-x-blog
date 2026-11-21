# 05_weex_基本组件介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\05_weex_基本组件介绍【海量资源尽在 666java.com】.mp4
- 时长 11分38秒（音频 698s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好各位那咱们就继续往下讲刚才咱们是介绍了一下VIX它是一个什么样的框架是吧它是一个前端的跨中端的框架然后下面咱们就来去说一下具体的一些组件然后这个组件里边其实就是一些它的一些基本的用法首先可以打开这个当前的文档在文档里边之后呢这里边有一些环境变量这个咱们可以先不看主要的是来看一些这种内置的组件
[00:30] 因为它是一个跨终端的这种移动端的这种平台所以说它这个DOM它都是一些自定义的比如说A标签跟咱们之前用过的当前的HTML的一些A标签是差不多的但是也有一些不同有的时候所以说咱们来去具体的来做一些例子来看一眼咱们要主要的来熟悉这几个在项目中比较常用的一些组件比如说A标签DB DIB
[00:58] 还有text image list那还有呢就是咱们的一个上拉和下拉的刷新最终的还有一些比如说这种输入的什么文本域啊还有输入框啊还有就是当前的一些复文本是吧行那这些呢咱们大概了解一下咱们重点呢还是去了解上面这些东西好吧来咱们看一下A标签啊它呢是其中的一个所见说用于实现页面之间的跳转那咱们这样啊在咱们项目中用的其实是呢
[01:27] 并不是太多但是咱们要去做一些例子来看一眼首先这里边你可以去从头到尾去读一下这个咱们直接来做例子来看效果就可以你看它这就有一个例子例子是这样这个咱们也可以看下这个示例示例里边大家可以发现这里边是有一个template这就是标准的这种使用view的一种方式下面是一些样式
[01:54] 那中间呢你也可以去写一些script的咱们这些js的代码啊当然都要基于view去做那好啊那咱们呢可以把它呢给拷贝一下拷到哪呢拷到咱们自己项目中呢有个叫做慢点view这个咱们可以先注调啊counter ray一下然后是注调注调完之后呢把刚才的代码可以拷贝过来那拷过来之后呢那咱们就可以启动项目啊
[02:22] 启动项目之后来看一下这个效果就可以咱们可以手动的去调试一下好稍等啊这个项目正在启动四十五十啊还是挺快的是吧好起完之后呢可以看一下你看这个呢就是一个去主会场这主会场里边呢你主要看A标签啊这里边呢就有一个它是个button是吧它这个就是它的链接当你去点去主会场的时候它就会去跳到这个链接里边啊大家要注意啊
[03:00] 咱们之前写的时候呢就说在A标签中直接去写了当前的去主会场并没有去写text那这里边有要求啊那你要想去使用当前的这种vix这种标签或者组件的话你必须加上text然后text里边呢去写具体的文本内容那好啊那这个咱们就来去点一下看看它能不能跳到这好点去主会场OK那这个呢确实就是访问了某一个页面啊
[03:30] 咱们来刷回来那这个咱们稍微改一改啊咱们不要去主会上咱们就打开传职的官网好吧那这个怎么写呢就是这是传职博客是吧传职博客然后下面这个网址呢咱们稍微改一改啊比如说叫3w.itcast.cin好吧然后呢咱们可以刷一下它会自动刷新啊这时候就是传职博客你点一下
[03:59] 他就去跳到了传知的这种官网的链接对吧没问题啊那当然有的时候啊咱们不需要在哪啊还不需要在这写死对吧咱们应该干嘛呢应该是从后台去可能是要去复制给当前复制怎么复制啊咱们是不是要去用到view的一些绑定变量啊OK那咱们就写一下啊script好然后怎么写啊然后是不是要导出啊到defund
[04:30] 然后写括号啊然后在这里边咱们要去设置modo的话呢怎么设置啊是不是一个date然后呢是一个冒号啊冒号而括号等等哎等于啊哎等于啊应该这样写啊好这里边是一个对象啊然后呢我想把它呢做成活的那怎么办呢那很简单啊咱们在这去设立一个变量叫imageur好吧冒号
[05:04] 谁呢就是当前上面这个地址好controlC controlV然后呢这个地址我想去也让他去展示这个东西那怎么展示在这还是不是写当前的咱们这个变量名叫model名称啊好那这前边一定要加上什么来说一下加上什么东西加一个码号对吧行那这样的话咱们就能从这啊去读取到当前的这个地址来看一下啊当前的效果应该是不变的来看一下
[05:35] 好点传至播客OK那这个地址是不是也跳过来了OK啊那这个呢就是A标签的一些基本的用法就咱们在线目中用到的时候其实也是这么用的啊行那这种方式呢大家应该熟悉你看这块内容呢你就应当先去学习view啊有view的基础知识之后呢你再去学这东西就比较容易了好吧那行Ctrl S一下Ctrl Z一下
[06:01] 好那咱们继续往下讲啊看看还有哪些组件咱们需要去熟悉咱们刷新一下刷回来啊然后下面还有啥呢下面还有一个dbdb呢就是一个通用的容器是吧就这个呢咱们一般情况下都是去包装一些东西咱们可以看一眼啊目前的话呢这个当前的这个a标签的其实外层的就是一个db啊这个给了给了一些样式对吧
[06:25] 那这个呢就是一个db那db里边呢咱们最终呢是不能直接去写这些字的比如说咱们再写一个黑马程序员好那咱们来去刷一下当前的页面啊你看当前这个黑马程序员那个字体都特别小字体特别小他这个呢并没有完全去识别到但是也能展示啊但是这种效果肯定是比较差的一般情况下呢你要想去展示文本的话呢咱们都要去套一个什么呢text
[06:55] 套一个text所以说咱们在这自己改一改比如说Ctrl S一下然后是写一个text然后你把根码重新选放到这里边咱们再来看一下这个效果你看这时候是不是字体就变大了是吧这样的话就算是真正的能够去展示一些文本信息好那这是text咱们一样说两个一个是db一个是text这些东西都比较简单然后下面还有一个image
[07:24] 那image的话就是要去展示单个图片在咱们项目中也有用到那这个呢也比较简单就是当前这一句话比如说咱们还是放到这儿啊比如说咱们就放到了黑马成全的下面好吧然后放到这儿这是一个图片这是一个图片啊那咱们呢下面就可以去看一眼看看这个图片是展示成什么样的一个效果来去直接刷新一下就可以了
[07:52] 好那这个呢就是view的一个这种logo是吧那这个图片呢咱们不想要了想换一个也想做成活的那你跟我说怎么办呢那这块是不是这个地址咱们是不是也去做成活的就可以了比如说我不想要它了我想要传制的官网的logo怎么办呢在w.itcast.in我就想要这个地址那怎么办是右键拷贝下当前的图片的地址是吧然后是怎么办呢
[08:21] 在这去写一个变量写个model是吧比如说叫image.url吧这叫传制吧itcast.url好url啊好直接考到这就可以了啊好那这是这个呢其实就是一个官网的地址图片的地址logo的地址那行把这个呢是设成什么冒号然后呢把后边给删了是吧把后边删了啊然后把它呢
[08:54] 给放上去好放上去之后呢咱们就可以来刷新一下哦那这个出来是出来的但是这个好像不太好看对吧咱们可以简单的去调一下当前的这个格式啊这里边的其实也有你可以看一看一下里边有什么宽度和高度对吧那宽度的话咱们就设置200高度的话咱们设置100好吧咱们再来看一下效果啊好那这个样这个样式呢还是可以的那这样的话就能在这去展示当前的一个
[09:27] 图片的信息是吧那行啊咱们下面继续往下看啊看里边还有什么东西然后这个是image然后下面还有一个叫list那list呢咱们在后期呢要去展示这种文章内表信息的时候啊肯定会去大量的去使用那这个用法呢也比较简单咱们来看一下啊首先呢是有一个list标签在template里边啊有个list标签然后呢咱们就可以去循环你看v-for不就是谁啊
[09:56] 不就是view的一些循环的标签指令吗所以说这个就是你的moduleOK啊那这个呢咱们直接考过来啊list然后咱们就往下放吧好吧然后这是一个list但是list好像是没有是吧那就把它也拿过来啊就是list啊那这样的话呢就能去展示当前的一个ABCDE好咱们可以刷下这个页面啊你看发现了吗ABCDE
[10:30] OK那这样的话就能去展示循环了当然我如果不想显示A或者不想显示B的时候呢咱们也可以去怎么办呢是不是可以在这去加什么东西啊加什么加V-if可以去判断这个值如果说是哪个值的话咱们可以去让它显示或者不显示咱们可以在这去设置一下怎么办呢咱们可以加一个DIB然后呢是这有个text然后呢
[11:02] 然后是v-if怎么写是不是NAM等于A如果说等于A的话我就让它显示那就是让A不显示的话就是不等于A对吧OK咱们再来刷一下你看这样的话A它就不显示了好吧行那这块内容咱们就先介绍到这里然后组件剩下组件咱们一会再去介绍

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Weex 框架中内置组件（如 text、image、list）的使用方法和相关文档查阅。

2) 按时间顺序列出每张画面的要点：
画面 1: 查看 Weex 官方文档，介绍 Weex 页面上下文中的 JS 实例和其属性类型。
画面 2: 在 Weex Playground 中编写一个包含按钮和文本的简单页面，预览效果为“去士会场”。
画面 3: 在 WebStorm 中查看项目结构，终端显示构建过程，正在编译模块。
画面 4: 继续在 WebStorm 中查看构建日志，模块编译进度更新。
画面 5: 在 Weex Playground 中预览一个包含广告和视频的复杂页面。
画面 6: 在 WebStorm 中编辑代码，为按钮添加 href 属性，终端显示应用已运行。
画面 7: 在 WebStorm 中修改代码，将 href 属性值改为 "http://www.itcast.cn"。
画面 8: 在 WebStorm 中继续编辑代码，为 text 标签添加“传智播客”文本。
画面 9: 查看 Weex 官方文档中关于 <text> 组件的说明，包括警告和样式支持。
画面 10: 在 WebStorm 中编辑代码，为 image 标签添加样式和 src 属性。
画面 11: 在 WebStorm 中继续编辑代码，为 image 标签添加样式和 src 属性。
画面 12: 查看 Weex 官方文档中关于 <image> 组件的说明，包括基本用法和注意事项。
画面 13: 在 Weex Playground 中预览一个包含“传智播客”和 logo 的页面。
画面 14: 查看 Weex 官方文档中关于 <list> 组件的说明，包括基本用法和示例。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```typescript
declare type Weex = {
  config: WeexConfigAPI;
  document: WeexDocument;
  requireModule: (name: string) => Object | void;
  supports: (condition: string) => boolean | void;
}
```

画面 2:
```html
<template>
  <div class="wrapper">
    <a class="button" href="http://g.tbcdn.cn/amte-resource/0.0.8/fast/show_1.js">
      <text class="text">去士会场</text>
    </a>
  </div>
</template>

<style scoped>
.wrapper {
  align-items: center;
  justify-content: center;
}

button {
  width: 350px;
  padding-top: 20px;
  padding-bottom: 20px;
  border-radius: 4px;
}

.text {
  font-size: 40px;
  color: #fff;
  text-align: center;
}
</style>
```

画面 3:
```html
<template>
  <div class="wrapper">
    <a class="button" href="http://g.tbcdn.cn/amte-resource/0.0.8/fast/show_1.js">
      <text class="text">去士会场</text>
    </a>
  </div>
</template>

<style scoped>
.wrapper {
  align-items: center;
  justify-content: center;
}

button {
  width: 350px;
  padding-top: 20px;
  padding-bottom: 20px;
  border-radius: 4px;
}

.text {
  font-size: 40px;
  color: #fff;
  text-align: center;
}
</style>
```

画面 6:
```html
<template>
  <div class="wrapper">
    <a class="button" href="http://www.itcast.cn">
      <text class="text">传智播客</text>
    </a>
  </div>
</template>

<script>
export default {
  data: () => {
  }
}
</script>

<style scoped>
.wrapper {
  align-items: center;
  justify-content: center;
}
</style>
```

画面 7:
```html
<template>
  <div class="wrapper">
    <a class="button" :href="image_url">
      <text class="text">传智播客</text>
    </a>
  </div>
</template>

<script>
export default {
  data: () => {
    image_url: "http://www.itcast.cn"
  }
}
</script>

<style scoped>
.wrapper {
  align-items: center;
  justify-content: center;
}
</style>
```

画面 10:
```html
<template>
  <div class="wrapper">
    <a class="button" :href="image_url">
      <text class="text">传智播客</text>
    </a>
  </div>
</template>

<script>
export default {
  data: () => {
    image_url: "http://www.itcast.cn"
  }
}
</script>

<style scoped>
.wrapper {
  align-items: center;
  justify-content: center;
}
</style>
```

画面 12:
```html
<image style="width:500px;height:500px" src="https://vuejs.org/images/logo.png"/>
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 9: 文档标题为“<text>”，内容包括“简介”、“样式”、“属性”等部分。
画面 12: 文档标题为“<image>”，内容包括“基本用法”、“子组件”、“样式”等部分。
画面 14: 文档标题为“<list>”，内容包括“简介”、“子组件”、“属性”、“扩展”、“示例”等部分。

5) 无。

