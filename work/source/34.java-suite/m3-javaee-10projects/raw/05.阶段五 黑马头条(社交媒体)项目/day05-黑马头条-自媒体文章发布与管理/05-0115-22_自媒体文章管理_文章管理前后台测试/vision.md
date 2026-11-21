# 画面线理解：22_自媒体文章管理_文章管理前后台测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\22_自媒体文章管理_文章管理前后台测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:42, 01:00, 01:14, 01:31, 01:49, 02:24, 02:53, 03:27, 04:01, 04:35, 04:56, 05:09, 05:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:57:43

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
    component: () => import ('/views/content/index.vue'),
},
{
    path: '/comment/list',
    component: () => import ('/views/comment/index.vue'),
},
{
    path: '/comment/detail',
    component: () => import ('/views/comment/detail.vue'),
},
{
    path: '/material/list',
    component: () => import ('/views/material/material.vue'),
},
{
    path: '/material/data',
    component: () => import ('/views/content/detail.vue'),
},
{
    path: '/fans/index',
    component: () => import ('/views/fans/index.vue'),
},
{
    path: '/fans/info',
    component: () => import ('/views/fans/info.vue'),
},
{
    path: '/fans/list',
    component: () => import ('/views/fans/list.vue'),
},
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
