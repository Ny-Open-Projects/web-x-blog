# 16_app搜索_前后端联调测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\16_app搜索_前后端联调测试【海量资源尽在 666java.com】.mp4
- 时长 11分24秒（音频 684s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好刚才那个接口呢咱们都已经开发完了啊下面呢咱们就来去往前后台都启动完之后呢咱们来测试一下测完之后呢咱们再来去分析一下或者说去讲解一下当前前台的一个流程好吧那你要想去测试的话呢首先呢你得先去把这四个微服务啊都启动起来你看我现在啊为了节省时间我这块已经启动了啊就是article的行为的登录的还有user的啊行那启动完之后呢咱们就可以
[00:29] 去启动前端前端的话这块我也启动了启动完之后咱们可以去刷一下这个页面这个页面它会自动的去弹出来然后咱们就现在就可以登录了登录主要测试的就是当前的搜索这一块好吧好登录完之后咱们去点一下这个上面这个搜索框你看首先这里边是有这么几部分来看一看这块是一个输入框是吧没啥问题然后下面这个就是你的
[01:00] 搜索的记录要去展示当然你也可以去删除但你也可以清空但清空的功能呢咱们并没有做啊但是无所谓能删除就可以是吧然后还有一个就是今日热点词热点词咱们是展示了两个一个是传直播客一个是黑马程序员好吧那下面这东西啊其实下面东西其实都是已经在页面上去那种静态的页面啊静态的东西所以这东西咱们不用管好吧这功能咱们咱们也没有去实现主要去实现的是这些这些内容
[01:29] 好吧当然你也可以去搜索啊可以去搜索比如说啊我想去搜一下面试点一下比如你点一下你的这种记录啊比如你的那个搜索记录点一下点之后呢你看他这边呢就能去把文章那边给展示当然这个文章那边你点进去能不能看呢当然可以是吧啊稍等啊OK那这个文章文章的信息就能展示到这了啊你往回返啊再往回返啊然后再点一下啊点下之后呢你可以去呃
[01:58] 点一下当前的热点比如说我想去搜一下黑马成语言能不能点呢点一下他是不是根据当前那个黑马成语言去搜索了没问题啊好你再往回翻啊什么还有一个功能就是说你可以去输入输入啥呢输入输入完之后呢他会有一个热点的词比如说你去搜搜一个叫做传职播客吧好吧传职播客你搜传职的时候呢他就会去把传职播客给展示出来
[02:26] 你点一下他就能去进行搜索但是这个没有内容其实无所谓啊主要是把这个功能咱们是做出来了好吧行那这个啊这个咱们已经都这个所有的接口啊基本上都测完了啊没有问题那咱们下面呢就来去看一下具体的页面他到底是怎么实现的啊主要是熟悉当前的流程能看明白就可以好吧好来
[02:50] 打开当前的这种前端的工程这里边在配置司里边在配置司里边有两个文件夹一个是search一个是search-withoutsearch其实就是当前的一个页面就是当前这个页面咱们可以看一下打开就只有一个叫index.view这个页面其实比较比较那啥它组件比较多咱们一个一个去看
[03:20] 比如说他这个展示的这一块内容的从这啊我选中的这一块主要是看这块内容就可以了下边都是些静态的数据咱们不用管好吧首先上面是有一个叫做套跑吧是吧这个是是一个是一个标签栏啊这个呢其实是一个组件他是在当前页面去引入了其他的组件这个组件的话呢他也是个点没有的一个页面啊你看当年的组件是谁呢你可以可以往下找找看他引入的是谁
[03:50] 他引入的是当前的一个searchtop在这个searchtop的端端呢在compounds什么bus里边有一个有个这样的一面是吧你可以去找一找啊看他他他然后有一个searchbus啊就是他那这个呢其实就是啥呢就是当前的一个什么搜索框就是搜索框就是一个input的input的搜索框好吧你可以去输入值输入完之后呢咱们可以去什么呢还可以去进行点击
[04:19] 好吧那这是一个啊然后你再往下还有啥吗看看啊往上往上往上呃其实这里边还有一个叫search history啊就这个呢就是你去查询什么呢历史查询历史啊就查询历史的话呢咱们呢也能在这去展示展示的话呢其实他也是引入的其他的组件啊去展示的当然这个里边啊他有一些数据需要填充比如说呃item id是吧item keywords还有什么呢
[04:51] 没有了是吧好没有了其实就是当前的Data History这个呢其实就是你从后台传过来之后复导了当前的这种数据应该是叫模型数据模型上面是吧最终是复导这它呢是再去传到了当前这个组件中这个组件呢你也可以去看一看比如叫Search History是吧你可以看一下它引入的是哪个组件Search History就是当前的什么Search零是吧
[05:22] 我们可以打开啊打开这个路径色指令这块呢其实就是当前的要展示的当前的什么呢当前的搜索记录啊你看不是有title吗是吧还有什么icon就是当前一个图标是吧OK啊那这个呢其实就是展示的当前的一个这种历史记录啊下面呢其实还有一些东西啊比如说但我也看啊下面还有一些就是你可以去显示所有的记录是吧还有吗还有啊再往下
[05:53] 这有个今日热点今日热点的话咱们并没有引入其他组件就是在不引入了啊这引入了就是你循环之后呢这块是有一个号的啊这个呢其实也是去要去展示当前的热点数据它也是引入的其他的组件来看一看吧就这个啊叫色指一啊咱们可以打开色指一看看这个呢其实就是要去展示的当前什么
[06:19] 当前的这种什么热点的数据其实这个gettext其实就是去展示了当前的热点的词热点的词其实默认默认显示的是哪是哪个默认的默认显示的是不是当天当天就是今天的一个这种关键字热搜的关键字OK行这里边还有一些东西还有一些请求咱们还是需要知道的来看一看它这里边是引入了当前的一个什么引入了一个API然后下面是发了一系列的请求哪些请求的
[06:48] 好来看一看啊首先呢是这有一个monkey的monkey的里边呢是调两个方法第一个就是当前的search history就是查询什么历史还有啥呢查询热点的词是吧也就是说他会去默认去打开页面就会去先去加载当前这个方法我选这个方法还有一个方法就是当前的什么哎我这鼠标不太好使啊还有一个加载的是热搜关键字啊热搜关键字啊咱们可以一个个方法去看啊先去看当前这个什么这个方法
[07:20] 先去看这个方法这个方法其实就是根据当前的设备ID设备ID去查询就设备ID你看在这你并不能看到当前的设备ID是吧这怎么办你可以去点进去当前的API跑到当前的API里边其实它真正发请求的时候就是去pause by什么是不是当前设备IDOK它就是在封装的时候已经把这个设备ID给自动带过去了
[07:47] 好吧行那这是一块啊然后这个最终的是对的返回之后呢他又付给了当前的这个模型啊这个模型面量里边啊行那没问题啊再往下看啊然后这块呢还有一个东西就是你要去读色识的话你点一下啊读色识的时候呢你传的是当前的一个keywordskeywordsok当然这个名称的咱们是有一个色识比较好然后再往下看啊还有一个删除删除的话呢其实刚才咱们没有展示是吧
[08:15] 没有演示咱们再演示一下比如说我先去删了OK这个是不是就没了是吧这个其实来看一下这个其实也是你往后传的就是一个ID对ID的话就是当前的什么user search里边的一个ID值因为咱们这个是需要去展示当前的一个历史的所以说你可以把这个历史的所有的数据都拿到其中包含了ID所以把ID传过来之后你就可以根据ID去删除了好吧
[08:44] 那删除完这个东西再重新加载一下当前这个当前这个search history就完事了啊最终咱们这个就能删除成功当然你这还做了个提示刚才大家也看到了啊嗯行那这个呢就是删除就删除啊嗯下面还有一些东西比如说加载热点词是吧热点词啊
[09:02] 热点词的话呢这个内容呢其实也是差不多啊热点词的话就是根据当前的日期其实你不传任何参数都可以啊他根据当前日期的默认他就会去把这个数据给加了进来最终是附到了DataHot里边最终DataHot里边咱们再去页面上去展示当前的传输博客黑马成语言就这样子啊行再往下看啊然后下面还有一个就是用户输入提示联想词你输入的时候呢
[09:30] 他就会自动的去触发这个吧又呢就是一个关键字刚才也看到了然后这时候呢你可以去付一些值是吧当然这个内容的最终的咱们是在这其实也看到效果了比如说你去搜搜东西的时候刚才咱们搜了船只然后他就会自动补全成者博客这个呢就在页面上或者在后台他就是根据当前关键字进行模糊查询是吧行啊那这个呢咱们就就说到这啊
[09:57] 这个流程大家是可以再去熟悉熟悉当然你要是不熟悉的话你可以再去走一遍流程怎么走呢你就是找某一个方法其实方法都类似找某一个方法比如说你找注册纸或者找什么加载什么历史记录都可以你找到它对应的什么对应的API对应的API然后你可以再去翻一下走比如说你再去get看到URL是怎么拿的这个URL我找一找
[10:27] 别找了在这找在这啊在common有一个什么config.js啊就这东西你可以在这去找在这去找比如说有一个article search咱们叫什么来着看一下这啊看一下这叫load search history好loadload search history是不是就是请求的当前的这个方法呀是吧那这个方法之后呢他会把这个前缀给拼上最终他一请求就会被谁拦截啊
[10:57] 就会被咱们的代理拦截是吧打开config.js找到当前的哪个呢就是article它就会被它拦截最终转发到9003去发请求最终把数据给获取到是不是这种流程啊好那这样啊那这个前端呢咱们就说到这这个内容呢再说一遍啊要求不高能够看明白能够看懂流程即可好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个前端搜索功能的实现，包括页面结构、组件逻辑、API调用和配置文件的编写。

2) 按时间顺序列出每张画面的要点：
画面1：展示IDE中项目结构，调试器显示Hikari连接池日志，当前在LoginApplication和UserApplication中。
画面2：展示Weex预览界面，包含搜索框、热点推荐列表和一个二维码，提示使用Weex playground app扫描。
画面3：展示index.Vue文件，包含搜索框、热点推荐列表的模板结构，使用v-for循环渲染。
画面4：展示search_top.Vue文件，定义了搜索栏的样式和点击事件，使用了icon组件。
画面5：展示index.Vue文件，定义了搜索框的样式和数据，包括hot和other的图标。
画面6：展示search_0.Vue文件，定义了搜索项的模板和点击事件。
画面7：展示index.Vue文件，展示热点推荐列表的模板结构。
画面8：展示index.Vue文件，定义了doSearch方法，加载搜索历史并处理返回数据。
画面9：展示index.Vue文件，doSearch方法中加载搜索历史并处理返回数据。
画面10：展示index.Vue文件，doSearch方法中加载搜索历史并处理返回数据。
画面11：展示index.Vue文件，定义了load_hot_keywords方法，处理热词数据。
画面12：展示index.Vue文件，定义了onInput方法，处理用户输入并调用Api.associate_search。
画面13：展示Api.js文件，定义了Api类，包含load_search_history、del_search、associate_search、load_hot_keywords等方法。
画面14：展示configs目录下的config.js文件，定义了不同模块的API地址配置，包括server_B5、article、behavior、user、login等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3：
```Vue
<template>
  <div class="art-page">
    <div class="art-top"><TopBar @onBlur="onBlur" @onInput="onInput"/></div>
    <scroller class="scroller" style="height:scrollHeight" show-scrollBar="true">
      <template v-for="item in data.history">
        <a href="1" class="all-search" @onDeleteHistory="onDeleteHistory" :id="item.id">
          <text class="all-search-text">全部搜索记录</text>
        </a>
        <Title title="今日热点" :icon="icon.hot">
          <div class="hot-body">
            <template v-for="k in item">
              <HotCell @onClick="doSearch" :title="k.hot_words" type="k.type"/>
            </template>
          </div>
        </Title>
        <Title title="大家都在搜" :icon="icon.other">
          <div class="hot-body">
            <div class="item">
              <HotCell title="长宁4.8级地震" tips="精"/>
            </div>
            <div class="item">
              <HotCell title="长宁4.8级地震" tips="荐"/>
            </div>
            <div class="item">
              <HotCell title="长宁4.8级地震" tips="热"/>
            </div>
          </div>
        </Title>
      </template>
    </scroller>
  </div>
</template>
```

画面4：
```Vue
<template>
  <div class="bar_bg">
    <text class="icon" @onClick="iconClick" :left-widths="25" :right-widths="20" placeholder="搜索关键词">
      <text class="icon"></text>
    </text>
  </div>
</template>

<script>
import Search from '@/components/inputs/search_button';
export default {
  name: 'index',
  components: { Search },
  data() {
    return {
      icon: 'uf082'
    }
  },
  mounted() {
    this.backgroundColor = this.$config.style.main_bg;
  },
  methods: {
    onClick() {
      this.$router.push('/search')
    },
    minibarLeftButtonClick() {
    },
    minibarRightButtonClick() {
    }
  }
}
</script>
```

画面5：
```Vue
<script>
import TopBar from '@/components/bars/search_top';
import SearchHistory from '@/components/cells/search_0';
import SearchTip from '@/components/cells/search_tip';
import HotCell from '@/components/cells/search_cell';
import Title from '@/components/titles/title';
import Api from '@/apis/search/api';
import { Modal } from 'weex-ui';
const modal = weex.requireModule('modal');
export default {
  name: 'index',
  components: { TopBar, SearchHistory, Title, HotCell, SearchTip },
  data() {
    return {
      scrollerHeight: '500px',
      showTip: false,
      icon: {
        hot: 'uf06d',
        other: 'uf17d'
      },
      data: {
        keyword: '' //当前输入的关键字
      }
    }
  }
}
</script>
```

画面6：
```Vue
<template>
  <div class="cell-body">
    <text class="icon"></text>
    <text class="title" @click="onClickText">{{title}}</text>
    <text class="icon" @click="onDeleteHistory">{{icon}}</text>
  </div>
</template>

<script>
export default {
  name: 'search_0',
  props: {
    id: {
      type: String,
      default: ''
    },
    title: {
      type: String,
      default: '显示字'
    },
    icon: {
      type: String,
      default: 'uf817'
    }
  },
  methods: {
    onDeleteHistory() {
      this.$emit('onDeleteHistory', this.id)
    },
    onClickText() {
      this.$emit('onClickText', this.title)
    }
  }
}
</script>
```

画面8：
```javascript
methods: {
  doSearch: function(val) {
    this.$router.push({name: 'search_result', params: { keyword: val }});
  },
  load_search_history: function() {
    Api.load_search_history().then(data => {
      if (data.code == 0) {
        this.data.history = data.data
      } else {
        modal.toast({message: data.error_message, duration: 3});
      }
    }).catch(e => {
      console.log(e)
    })
  },
  onDeleteHistory: function(id) {
    let this = this;
    modal.confirm({message: '确认要删除吗？'}, function(button) {
      if (button == 'OK') {
        Api.del_search(id).then(data => {
          if (data.code == 0) {
            modal.toast({message: '删除成功', duration: 3});
            this.load_search_history();
          } else {
            modal.toast({message: data.error_message, duration: 3});
          }
        })
      }
    })
  }
}
```

画面11：
```javascript
load_hot_keywords: function() {
  Api.load_hot_keywords().then(data => {
    if (data.code == 0) {
      let newData = [];
      let temp = [];
      for (var i = 0; i < data.data.length; i++) {
        if (i % 2 == 0) {
          temp.push(data.data[i]);
        } else {
          temp.push(data.data[i]);
          newData.push(temp);
          temp = [];
        }
      }
      this.data.hot = newData
    } else {
      modal.toast({message: data.error_message, duration: 3});
    }
  }).catch(e => {
    console.log(e)
  })
}
```

画面13：
```javascript
function Api() {
  Api.prototype = {
    setVue: function(Vue) {
      this.Vue = Vue;
    },
    load_search_history: function() {
      let url = this.Vue.$config.urls.get('load_search_history');
      return this.Vue.$request.postBy(url);
    },
    del_search: function(id) {
      let url = this.Vue.$config.urls.get('del_search');
      return this.Vue.$request.postBy(url);
    },
    associate_search: function(search) {
      let url = this.Vue.$config.urls.get('associate_search');
      return this.Vue.$request.postBy(url);
    },
    load_hot_keywords: function() {
      let url = this.Vue.$config.urls.get('load_hot_keywords');
      return this.Vue.$request.postBy(url);
    }
  }
}
```

画面14：
```javascript
'//server_B5': {
  target: 'http://heima-app-java.research.icast.cn/',
  changeOrigin: true
},
'article': {
  target: 'http://api1:9003/',
  changeOrigin: true,
  pathRewrite: {
    '^/article': ''
  }
},
'behavior': {
  target: 'http://api1:9004/',
  changeOrigin: true,
  pathRewrite: {
    '^/behavior': ''
  }
},
'user': {
  target: 'http://api1:9005/',
  changeOrigin: true,
  pathRewrite: {
    '^/user': ''
  }
},
'login': {
  target: 'http://api1:9001/',
  changeOrigin: true,
  pathRewrite: {
    '^/login': ''
  }
}
```

4) PPT 标题、架构图

