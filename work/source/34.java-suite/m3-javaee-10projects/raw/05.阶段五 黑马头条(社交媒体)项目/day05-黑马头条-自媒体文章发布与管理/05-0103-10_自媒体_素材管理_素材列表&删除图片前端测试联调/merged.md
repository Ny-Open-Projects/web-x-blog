# 10_自媒体_素材管理_素材列表&删除图片前端测试联调

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\10_自媒体_素材管理_素材列表&删除图片前端测试联调【海量资源尽在 666java.com】.mp4
- 时长 4分33秒（音频 273s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱们继续啊刚才咱们是已经完成了两个接口这两个接口还没有测试啊一个是素材列表接口还有上个接口是删除图片接口啊那咱们下面就来去测试一下顺便把前台也可以去捋一捋好吧那首先呢你要在后台把这个把这个服务给启动启动一下我这已经是启动了当前的微服务其他也没做啊启动完之后呢你这时候就可以到前台这一块再启动一下启动完之后呢就可以登录
[00:30] 比如说我这里登录一下比较张三123好吧登录完之后呢你可以在这去测一下比如说素材管理里边呢你看当前这个图片信息是能够展示的这个列表是吧你也可以去分页那说明当前这个这个素材列表的接口是没问题的那能删除吧咱们也可以删除一个啊好删除一个姑娘啊来你看这个是不是也能删除啊
[00:58] 没问题啊说明咱们刚才开发的那两个接口是都没有问题的那么下面呢就来去捋一下前端的代码啊这代码的话咱们再来看一下还是打开这个vius里边有个什么呢叫myview里边有一个第一个页面这页面里边啊咱们看一下啊往上看首先呢这里边啊咱们直接直接在这看啊这有一个monkey的啊monkey里边呢是去调用了当前的thisload的date然后呢就这个方法
[01:28] 这方法里边他又去调了当前这个方法这个方法呢调流方法的时候呢他又去传了几个参数啊这个参数是谁呢你可以看一下当前什么配置还有什么size还有什么ease就是你是否是收藏了是吧这是都有默认值啊但这个值呢之前学过欧罗姆UI的同学应该是能够清晰的啊其实咱们这块默认值啊应该是在上面啊它是呢是有一个分页的插件并且呢咱们在这也给了一些默认值也给了一些默认值啊比如说
[01:58] 当前页是1当前页的显示条数是15看到了吗这个值就已经传完了但是这个值这个值默认给的是0默认给的是0这个0的话就是没有收藏但你也可以去设置咱们一会去设置设置完之后可以去找到一些收藏的数据好吧那行咱们说完之后最终它是掉了get image date
[02:26] 其实就是下面这个方法这个方法做多少事呢可以看一下它是首先是调了一个API是拿到了一个result这个呢其实就是调去了接口拿到一个数据是吧找到它那其实就是从publish这个方法里边啊好找tjs看看谁啊get all image data其实就是
[02:56] 最上面的东西对吧你看这个是不是通过URL然后是Postal抢求把参数传过来最终是发达抢求啊没问题啊然后这里边啊最终你拿到Redox之后呢咱们分别取出了list和totallist和total啊那这里边你看也可以看一下啊当前这个image date付给他了付给他了然后这个呢是付给了imageimage配置里边一个total其实就是付给了分页的插件
[03:23] 其实咱们主要可以看下这个东西这个呢其实就是数据展示的部分要去循环当前这个集合或者叫数组好吧往上看啊最终循环的时候呢其实是这其实这一块就当前我选中这一块啊你看它这是有一个v刚负啊去循环了当前的image date然后最终呢你去展示了当前的图片是吧然后还有啥呢咱们还去判断了一下你是否是收藏了是吧还有一个
[03:50] 这种点击的事件就是删除的点击事件这个image其实就是当前某一个对象其实咱们可以根据某一个对象去删除可以这样看咱们可以再看下这个方法往下走最终它去调接口的时候其实是拿到了当前的ID因为咱们删除的时候只需要一个ID就可以了删除成功之后咱们会提示删除成功并且会去重新加载一下当前的页面
[04:21] 没问题吧那行那这个流程啊咱们就算是走通了啊这单本啊还是再说一下这前段单本主要能看明白能够知道这个流程即可好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个图片素材管理系统的前端 Vue.js 与后端 Java 的实现细节，包括图片上传、列表展示、分页、收藏和删除功能的代码逻辑。

2) 按时间顺序列出每张画面的要点：
画面1：展示后端 Java 代码，`MaterialManageController` 中定义了 `@PostMapping("/upload")` 和 `@PostMapping("/list")` 两个接口，用于处理图片上传和列表查询。
画面2：展示前端页面，用户在“素材管理”模块中浏览图片列表。
画面3：展示前端 Vue 代码，`Upload.Vue` 组件中定义了图片上传的表单结构和 `onUpload` 方法。
画面4：展示前端 Vue 代码，`material.Vue` 中定义了图片列表的 `el-pagination` 分页组件和 `el-dialog` 对话框结构。
画面5：展示前端 Vue 代码，`material.Vue` 中 `methods` 部分的 `loadData` 方法，用于初始化数据和处理分页变化。
画面6：展示前端 Vue 代码，`material.Vue` 中 `methods` 部分的 `loadData` 方法，光标位于 `this.imgPage.currentPage = newPage` 行。
画面7：展示前端 Vue 代码，`material.Vue` 中 `el-dialog` 对话框的结构和 `upload` 组件的导入。
画面8：展示前端 Vue 代码，`material.Vue` 中 `data` 部分的 `imgPage` 对象初始化，包含 `total`, `currentPage`, `pageCount`, `pageSize` 等属性。
画面9：展示前端 Vue 代码，`material.Vue` 中 `methods` 部分的 `loadData` 方法，光标位于 `this.imgPage.currentPage = newPage` 行。
画面10：展示前端 Vue 代码，`material.Vue` 中 `data` 部分的 `imgPage` 对象初始化，包含 `total`, `currentPage`, `pageCount`, `pageSize` 等属性。
画面11：展示前端 Vue 代码，`material.Vue` 中 `methods` 部分的 `gettingData` 方法，包含获取数据、收藏和删除图片的逻辑。
画面12：展示前端 Vue 代码，`material.Vue` 中 `methods` 部分的 `gettingData` 方法，光标位于 `this.imgPage.total = result.data.total` 行。
画面13：展示前端 Vue 代码，`material.Vue` 中 `template` 部分的 `el-radio-group` 和 `el-button` 组件，用于选择图片和上传。
画面14：展示前端 Vue 代码，`material.Vue` 中 `methods` 部分的 `delImg` 方法，用于删除图片并弹出确认对话框。

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

