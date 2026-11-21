# 22_自媒体文章管理_文章管理前后台测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\22_自媒体文章管理_文章管理前后台测试【海量资源尽在 666java.com】.mp4
- 时长 5分47秒（音频 347s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好文章的相关接口呢咱们都已经开发完了然后下面咱们就来去通过前端来测试一下看看这个接口到底好用不好用是吧那这里边咱们已经开发完的接口呢是第一个是文章列表文章详情还有一个删除文章那这三个咱们一块去调一下那这时候呢你首先呢需要去把当前的Media这个项目呢给启动一下那它的微服务启动了我现在我这已经启动了
[00:27] 启动完之后呢你需要在前端这一块呢需要去把前端的工程也启动了好吧那启动完之后呢这时候啊我就可以去登录到当前的前端的系统123好点登录完成之后呢你在内容管理里边去找到内容列表OK那这时候呢其实你会发现当前这个内容是不是出来了是吧你看刚刚才咱们发布的文章是不是也在这啊没问题啊也就是说咱们
[00:55] 第一个就是文章列表的展示是没事的文章列表但文章列表里边它有一些条件咱们也可以简单看一下比如说可以点一下草稿草稿没有数据是吧再审核有没有再审核是有的是吧你也可以根据频道比如说mysocle有一个是吧jarboard有没有也有是吧有两个它是根据条件进行查询是可以的但你说我想去修改可以吗可以比如我点一下修改修改的话它就跳到了当前的一个修改的页面
[01:25] 让你去修改比如说这个888呀我不想换成222好吧222这时候我点这块是不是就提交成功了提交成功之后呢这块就会自动的去跳到查询看这不就是222吗是吧有问题啊然后呢然后还有啥呢然后还有删除比如说我这个不想要了行吗可以删了你看当前这个数据是不是也没了也就是说咱们刚才开发的三个接口都是没有问题的
[01:56] 那这时候咱们顺便就把当前的前端的代码流程大概去说一说好吧我来看一看咱们首先是打开当前views下面有一个叫contentcontent里边有个index.view这个其实就是要主要是去查询文章的时候用的你可以看一下这里边有一个search article前面这些都是一些参数最终是调用了当前的咱们的接口调用接口之后又重新去复了下值
[02:24] 附给了一个ArticleList最终它会把ArticleList给循环然后是把数据给便利出来展示就可以了但这里边你看好像并没有当前的这种ArticleList虽然这是有但这只是一些Search Without标签里边的就是它是引用了其他的组件那组件是谁呢这组件的话其实就在这这有一个Search Without
[02:50] 它是通过传到这之后你看我选中这这是另外一个页面OK传到这之后它就会循环然后分别去展示当前的数据当展示当前数据的时候你可以看一下首先是图片是吧这是图片信息还有什么还有一个title还有一个title下面还有啥下面还有些状态比如说你的上架下架修改删除修改删除是不是在这当你点击的时候它就会去触发当前的方法
[03:17] 然后比如说修改那就是修改修改需要去调哪个接口删除需要调哪个接口他们都是通过当前这个方法去做的下面还有一些东西比如说草稿它就是一些按钮就是按钮按钮是在这你看这不带审核吗它就根据你后台查询的这个状态来去显示到底显示哪个按钮比如说0是草稿1就是带审核比如说8是带发布怎么还有一个什么比如说100删除2是什么
[03:45] 通过上和前这些东西他们都可以去展示好吧那这个咱们就不再去说了最终的咱们还要再去看下这个东西就是说你当你去点它的时候比如说你点删除和修改的时候它分别是出发了哪些方法咱们可以往下看找到这搜一下搜完之后其实就是这个方法这个方法这里边它就会去设置是啥呢比如说修改的话它就会去跳到路由
[04:15] 跳到这个路由下面OK如果说你要删除的话呢他就会先去提示一下先去提示一下然后再去调接口去删除看到了吗再去调接口去删除就可以了好吧行啊行那这个啊这个咱们就先说到这啊然后下面还有个东西啊就是当前的有一个在indexview里边还有第二部分就是当前的头部分就是search tools在这里边呢它是啥呢它是就是你的搜索的
[04:43] 组件,打开这个看一下这里边其实就是你需要比如说你要去搜索的时候你输入了某些参数的话都是在当前这个组件中去定义的比如说文章的状态是吧状态还有什么频道列表还有什么还有时间还有时间都可以去设置好吧最终它就会封装到当前的一个对象中然后是让你去做选择让你去作为条件进行谈论比如Pyramus
[05:13] 那这个流程咱们大概说到这儿当然还有些其他东西你可以再去熟悉一下比如说对应的API咱们都在这定义是吧咱们之前讲过还有什么对应的这种什么API的接口的机制都在constance API.js里边还有就是你的路由的话都在当前这个Routers去定义Routers
[05:38] 就在router4.js中去定义的好吧这些东西都写完了大家一定要能够看明白这个流程就可以好吧行那关于文章这块呢咱们就说到这里啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个文章管理后台系统的前端页面操作与对应的 Vue.js 代码实现，包括文章列表、搜索、发布、状态筛选和删除功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文章后台接口文档，定义了删除文章接口的请求DTO和响应DTO，以及参数校验规则。
画面2：展示文章管理后台的前端页面，显示文章列表和用户数据统计。
画面3：展示文章列表页面，文章状态为“待审核”。
画面4：展示文章搜索功能，根据关键词“java”搜索到2篇文章。
画面5：展示文章发布页面，填写标题、标签、分类、定时发布和内容。
画面6：展示文章列表页面，文章状态为“待审核”。
画面7：展示前端代码，实现删除文章的逻辑，调用 deleteArticlesById 方法。
画面8：展示前端代码，实现文章列表的渲染，包含“上传”、“修改”、“删除”等操作按钮。
画面9：展示前端代码，实现文章列表的分页功能。
画面10：展示前端代码，实现文章列表的分页功能。
画面11：展示前端代码，实现文章搜索功能，包含搜索框和文章列表。
画面12：展示前端代码，实现文章状态筛选功能，包含下拉框和日期选择器。
画面13：展示前端代码，实现文章状态筛选功能，包含 selectState 数组和 queryData 方法。
画面14：展示前端路由配置，包含文章、评论、素材、粉丝等模块的路由。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
5.5 删除文章后台接口
5.5.1 接口定义
(1) 基本定义
自从对于未发布的文章进行删除操作。
参考标准  请参考通用接口规范
发布接口名称  /api/v1/media/news/del_news
请求DTO  com.heima.model.media.dtos.WmNewsDto
响应DTO  { "host": "", "code": 0, "error_message": "操作成功", "data": [] }
(2) CODE定义
PARAM_INVALID  PARAM_INVALID(501,"无效参数")。
```

画面7：
```
components: {
    SearchTool,
    SearchResult
},
computed: {
},
methods: {
    searchArticle (newParams) {
        this.tempParams = newParams;
        let result = await searchArticle({ ...this.params, key_word: this.searchText, ...this.tempParams });
        if (this.$refs.mySearchResult.resetPage) { // 重置分页
            this.hot = result.hot;
            this.total = result.total; // 总记录数
            this.articleList = result.data; // 当前页文章列表
        }
    },
    // 根据id删除文章
    async deleteArticlesById (Id) {
        let temp = await deleteArticles(Id);
        if (temp.code == 0) {
            this.$message({type: 'success', message: '删除成功！'});
            this.searchArticle();
        } else {
            this.$message({type: 'error', message: temp.error_message});
        }
    }
}
```

画面8：
```
<template>
    <section class="result">
        <header>
            <ul class="result-container">
                <li v-for="(item, index) in articleList" class="articles-item">
                    <img class="article-img" :src="item.cover">
                    <div class="article-content">
                        <a @click="operationBtn(item.id, item.status)" class="article-title">{{item.title}}</a>
                        <div class="article-info">
                            <div data-type="up" v-if="item.enable == '0'" class="el-icon-upload">上传</div>
                            <div data-type="down" v-if="item.enable == '1'" class="el-icon-download">下载</div>
                            <div data-type="modify" v-if="item.status == '9'" class="el-icon-edit">修改</div>
                            <div data-type="del" v-if="item.status == '100'" class="el-icon-delete">删除</div>
                        </div>
                    </div>
                </li>
            </ul>
        </header>
    </section>
</template>
```

画面9：
```
<div class="pagination">
    <el-pagination
        layout="total, prev, pager, next"
        :current-page.sync="listPage.currentPage"
        :page-size="pageSize"
        :total="total">
    </el-pagination>
</div>
```

画面11：
```
<template>
    <div class="search-tool">
        <el-input v-model="searchText" placeholder="请输入搜索关键词" clearable></el-input>
        <el-select v-model="channel_list" placeholder="请选择频道" clearable>
            <el-option
                v-for="item in channel_list"
                :key="item.id"
                :label="item.name"
                :value="item.id">
            </el-option>
        </el-select>
        <el-button type="primary" @click="searchArticle">搜索</el-button>
    </div>
    <search-result
        ref="searchResult"
        :articleList="articleList"
        :host="host"
        :totals="total"
        :pageAge="searchArticle"
        :pageSize="pageSize"
        :deleteArticlesById="deleteArticlesById"
        :upOrDowns="upOrDowns">
    </search-result>
</template>
```

画面12：
```
<el-form-item label="文章状态：" label-width="110px">
    <el-select v-model="selectState.value" @change="changeState">
        <el-option
            v-for="item in selectState"
            :key="item.value"
            :label="item.label"
            :value="item.value">
        </el-option>
    </el-select>
</el-form-item>
<el-form-item label="频道列表：" label-width="110px">
    <el-select v-model="channel_id" @change="queryData">
        <el-option
            v-for="item in channel_list"
            :key="item.id"
            :label="item.name"
            :value="item.id">
        </el-option>
    </el-select>
</el-form-item>
<el-form-item label="时间选择：" label-width="110px">
    <el-date-picker
        v-model="date"
        type="daterange"
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期"
        format="yyyy-MM-dd"
        value-format="yyyy-MM-dd">
    </el-date-picker>
</el-form-item>
```

画面13：
```
selectState: [
    {label: '全部', value: 0},
    {label: '待审核', value: 1},
    {label: '审核通过', value: 2},
    {label: '审核失败', value: 3},
],
methods: {
    // 查询文章列表
    queryData () {
        let params = {
            resetPage: true, // 用于分页，不需要重新设置分页器的标记
            channel_id: this.channel_id,
            status: this.selectState.value == 5 ? null : this.selectState.value,
            page: 1,
            begin_update: (this.date && this.date.length > 1) ? this.date[0] : null,
            end_update: (this.date && this.date.length > 1) ? this.date[1] : null
        };
        this.changePage && this.changePage(params); // 调用上层组件的查询方法
    }
}
```

画面14：
```
{
    path: '/article/list',
    component: () => import ('/views/content/index.Vue'),
},
{
    path: '/comment/list',
    component: () => import ('/views/comment/index.Vue'),
},
{
    path: '/comment/detail',
    component: () => import ('/views/comment/detail.Vue'),
},
{
    path: '/material/list',
    component: () => import ('/views/material/material.Vue'),
},
{
    path: '/material/data',
    component: () => import ('/views/content/detail.Vue'),
},
{
    path: '/fans/index',
    component: () => import ('/views/fans/index.Vue'),
},
{
    path: '/fans/info',
    component: () => import ('/views/fans/info.Vue'),
},
{
    path: '/fans/list',
    component: () => import ('/views/fans/list.Vue'),
},
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

