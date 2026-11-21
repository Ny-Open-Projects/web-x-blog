# 画面线理解：10_自媒体_素材管理_素材列表&删除图片前端测试联调

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\10_自媒体_素材管理_素材列表&删除图片前端测试联调【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:39, 01:06, 01:16, 01:21, 01:35, 01:53, 02:04, 02:21, 02:41, 02:53, 03:31, 03:37, 04:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:46:54

1) 这一组画面整体在讲一个图片素材管理系统的前端 Vue.js 与后端 Java 的实现细节，包括图片上传、列表展示、分页、收藏和删除功能的代码逻辑。

2) 按时间顺序列出每张画面的要点：
画面1：展示后端 Java 代码，`MaterialManageController` 中定义了 `@PostMapping("/upload")` 和 `@PostMapping("/list")` 两个接口，用于处理图片上传和列表查询。
画面2：展示前端页面，用户在“素材管理”模块中浏览图片列表。
画面3：展示前端 Vue 代码，`Upload.vue` 组件中定义了图片上传的表单结构和 `onUpload` 方法。
画面4：展示前端 Vue 代码，`material.vue` 中定义了图片列表的 `el-pagination` 分页组件和 `el-dialog` 对话框结构。
画面5：展示前端 Vue 代码，`material.vue` 中 `methods` 部分的 `loadData` 方法，用于初始化数据和处理分页变化。
画面6：展示前端 Vue 代码，`material.vue` 中 `methods` 部分的 `loadData` 方法，光标位于 `this.imgPage.currentPage = newPage` 行。
画面7：展示前端 Vue 代码，`material.vue` 中 `el-dialog` 对话框的结构和 `upload` 组件的导入。
画面8：展示前端 Vue 代码，`material.vue` 中 `data` 部分的 `imgPage` 对象初始化，包含 `total`, `currentPage`, `pageCount`, `pageSize` 等属性。
画面9：展示前端 Vue 代码，`material.vue` 中 `methods` 部分的 `loadData` 方法，光标位于 `this.imgPage.currentPage = newPage` 行。
画面10：展示前端 Vue 代码，`material.vue` 中 `data` 部分的 `imgPage` 对象初始化，包含 `total`, `currentPage`, `pageCount`, `pageSize` 等属性。
画面11：展示前端 Vue 代码，`material.vue` 中 `methods` 部分的 `gettingData` 方法，包含获取数据、收藏和删除图片的逻辑。
画面12：展示前端 Vue 代码，`material.vue` 中 `methods` 部分的 `gettingData` 方法，光标位于 `this.imgPage.total = result.data.total` 行。
画面13：展示前端 Vue 代码，`material.vue` 中 `template` 部分的 `el-radio-group` 和 `el-button` 组件，用于选择图片和上传。
画面14：展示前端 Vue 代码，`material.vue` 中 `methods` 部分的 `delImg` 方法，用于删除图片并弹出确认对话框。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
public ResponseResult delPicture(@RequestBody @ModelAttribute dto) {
    return materialService.delPicture(dto);
}

@Override
@PostMapping("/list")
public ResponseResult list(@RequestBody MaterialListDto dto) {
    return materialService.findList(dto);
}
```

画面3：
```html
<template>
  <div class="upload_pic" label-width="100px">
    <img src="upload_img_url" class="upload_pic_show" />
    <el-form-item label="用户图片" prop="logo">
      <el-upload ref="myUpload" action="" auto-upload="false">
        <el-button size="small" type="primary">点击选择图片</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onUpload" size="small">开始上传</el-button>
      </el-form-item>
    </el-upload>
  </div>
</template>

<script>
import { uploading } from '@/api/publish'
export default {
  name: 'upload',
  props: {
    imgChange: ''
  },
  data () {
    return {
      upload_img_url: require('@/assets/pic_bg.png'),
    }
  },
  methods: {
    onUpload () {
      let files = document.querySelector('.el-upload .el-upload_input').files;
    }
  }
}
</script>
```

画面4：
```html
<div class="img_list">
  <div class="img_list_item" v-for="img in imgData" :key="img.id">
    <img @click="collectOrCancel(img)" :src="img.url" />
    <div v-if="activeSelect == '0'" class="operate">
      <img @click="collectOrCancel(img)" :src="img.is_collection ? collectSelectedIcon : collectIcon" alt="">
      <img @click="delImg(img)" :src="delIcon" alt="">
    </div>
  </div>
</div>

<el-pagination
  background
  layout="prev, pager, next, jumper"
  :total="imgPage.total"
  :page-count="imgPage.pageCount"
  :page-size="imgPage.pageSize"
  :current-page="imgPage.currentPage"
  @current-change="pageChange"
/>
```

画面5：
```javascript
methods: {
  loadData: function() {
    // 初始化加载数据
    this.getImgData({
      page: this.imgPage.currentPage,
      size: this.imgPage.pageSize,
      is_collected: this.activeSelect
    });
  },
  pageChange (newPage) {
    this.imgPage.currentPage = newPage;
    this.loadData();
  },
  // 获取图片素材
  async gettingData (params) {
    let result = await getALLImgData(params);
    this.imgData = result.data.list;
    this.imgPage.total = result.data.total;
    this.imgPage.pageCount = Math.ceil(this.imgPage.total / this.imgPage.pageSize);
  },
  // 点击收藏或取消收藏图片
  async collectOrCancel (img) {
    let isCollected = img.is_collection;
    if (isCollected == 1) {
      isCollected = 0;
    } else {
      isCollected = 1;
    }
    await collectOrCancel(img.id, isCollected);
    this.$message({ type: 'success', message: '操作成功！' });
  },
  // 删除图片
  async delImg (img) {
    let result = await this.$confirm('确认删除该素材？');
    if (result) {
      await delImg(img.id);
      this.$message({ type: 'success', message: '删除成功！' });
      this.loadData();
    }
  },
  // 重置图片状态
  imgChange: false,
  // 是否上传图片导致图片数据变化，此次未用未控制是否在关闭后要重新加载
  showPicDialog: false,
  activeSelect: '0',
  imgData: [],
  // 存储图片数据，同时作为收藏数据和全部数据的引用
}
```

画面11：
```javascript
// 获取图片素材
async gettingData (params) {
  let result = await getALLImgData(params);
  this.imgData = result.data.list;
  this.imgPage.total = result.data.total;
  this.imgPage.pageCount = Math.ceil(this.imgPage.total / this.imgPage.pageSize);
},
// 点击收藏或取消收藏图片
async collectOrCancel (img) {
  let isCollected = img.is_collection;
  if (isCollected == 1) {
    isCollected = 0;
  } else {
    isCollected = 1;
  }
  await collectOrCancel(img.id, isCollected);
  this.$message({ type: 'success', message: '操作成功！' });
},
// 删除图片
async delImg (img) {
  let result = await this.$confirm('确认删除该素材？');
  if (result) {
    await delImg(img.id);
    this.$message({ type: 'success', message: '删除成功！' });
    this.loadData();
  }
},
// 重置图片状态
imgChange: false,
// 是否上传图片导致图片数据变化，此次未用未控制是否在关闭后要重新加载
showPicDialog: false,
activeSelect: '0',
imgData: [],
// 存储图片数据，同时作为收藏数据和全部数据的引用
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
