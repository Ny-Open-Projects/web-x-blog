# 画面线理解：16_app搜索_前后端联调测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\16_app搜索_前后端联调测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:22, 01:31, 03:14, 04:04, 05:01, 05:26, 06:09, 07:02, 07:18, 08:11, 09:01, 10:06, 10:24, 11:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:38:38

1) 这一组画面整体在讲一个前端搜索功能的实现，包括页面结构、组件逻辑、API调用和配置文件的编写。

2) 按时间顺序列出每张画面的要点：
画面1：展示IDE中项目结构，调试器显示Hikari连接池日志，当前在LoginApplication和UserApplication中。
画面2：展示Weex预览界面，包含搜索框、热点推荐列表和一个二维码，提示使用Weex playground app扫描。
画面3：展示index.vue文件，包含搜索框、热点推荐列表的模板结构，使用v-for循环渲染。
画面4：展示search_top.vue文件，定义了搜索栏的样式和点击事件，使用了icon组件。
画面5：展示index.vue文件，定义了搜索框的样式和数据，包括hot和other的图标。
画面6：展示search_0.vue文件，定义了搜索项的模板和点击事件。
画面7：展示index.vue文件，展示热点推荐列表的模板结构。
画面8：展示index.vue文件，定义了doSearch方法，加载搜索历史并处理返回数据。
画面9：展示index.vue文件，doSearch方法中加载搜索历史并处理返回数据。
画面10：展示index.vue文件，doSearch方法中加载搜索历史并处理返回数据。
画面11：展示index.vue文件，定义了load_hot_keywords方法，处理热词数据。
画面12：展示index.vue文件，定义了onInput方法，处理用户输入并调用Api.associate_search。
画面13：展示Api.js文件，定义了Api类，包含load_search_history、del_search、associate_search、load_hot_keywords等方法。
画面14：展示configs目录下的config.js文件，定义了不同模块的API地址配置，包括server_B5、article、behavior、user、login等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3：
```vue
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
```vue
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
```vue
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
```vue
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
    setVue: function(vue) {
      this.vue = vue;
    },
    load_search_history: function() {
      let url = this.vue.$config.urls.get('load_search_history');
      return this.vue.$request.postBy(url);
    },
    del_search: function(id) {
      let url = this.vue.$config.urls.get('del_search');
      return this.vue.$request.postBy(url);
    },
    associate_search: function(search) {
      let url = this.vue.$config.urls.get('associate_search');
      return this.vue.$request.postBy(url);
    },
    load_hot_keywords: function() {
      let url = this.vue.$config.urls.get('load_hot_keywords');
      return this.vue.$request.postBy(url);
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
