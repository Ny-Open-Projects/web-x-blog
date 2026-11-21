# 20_通用封装-前台逻辑流程说明

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\20_通用封装-前台逻辑流程说明【海量资源尽在 666java.com】.mp4
- 时长 12分22秒（音频 742s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去说一下这个前端的流程啊主要的是参数啊主要是参数看看往后台需要传什么参数啊首先呢咱们还是以谁为例呢以当前的这个敏感词敏感词为例啊因为他这个里边是包含了查询新增修改和删除都包含了啊咱们一块来看一眼好吧首先呢你打开这个sys-tiv当前这个在vius下边啊有一个sys-tiv
[00:28] 然后打开有个intest.Vue这个其实就是它的一个主页面是吧首先咱们可以看一下当前的查询这个查询的话首先就有一个monty的勾字函数是吧是有一个加载的叫什么load date好吧咱们可以看下这个方法往下找这个其实就是load date的方法然后它去干嘛它去调了一个load list这个方法这个方法你看它这个参数是这么多咱们可以看一下这个load list
[00:58] 其实他引用的谁引用的是当前API comment下面的一些这种包应该是他的一个API的接口调用一个地址咱们可以打开当前commentcomment里边其实就这些方法他应该是加载的是load list对吧load list你可以看一下最终加载的就是load list但这参数是谁OK重要的应该就是这个参数可以看一下这个参数在这你看这有一个param
[01:25] Pyro里面有个Name这个Name要注意这个Name就是你要操作的表这个Name就是要操作的表那这个Name要跟谁对应上呢跟你的后端打开打开咱们Controller吧比如说咱们要访问的这个它最终是封装到Common下面有一个Name这个Name其实对应的是一个EnumerEnumer里边是不是咱们之前定义过很多的这种表目前的话咱们只是定义了这几个是吧
[01:55] 但是其中里边就有一个你看他叫ADSysTip是不是当前的敏感词啊没问题啊我看这个必须要在这里边能找着才行如果说你要想去再去设置其他模块的话那你在前台传参数的时候只要是这块啊设置其他表并且呢你需要在当前这个enumer中需要去设置不同的表就可以了我再强调一遍啊
[02:20] 当前的内幕要跟当前你这定义的一模一样要不然它接收不到好吧行这个参数咱们说明白了好再往下看然后这是有一个什么配置是1然后size是10咱们后台其实都有对应的当前的size跟配置去接收有问题吧OK然后再往下看然后这边还有一个where还有一个where是一个数组因为咱们后台接收的时候是啥呢是一个集合看到了吗
[02:50] 是一个集合啊所以说呢他肯定要去与数组去传当然目前的话呢你当你去点击当年敏感词设置的时候应该是什么呢应该是没有条件就是无条件的进行查询那边是查询所有的信息是吧所以说啊他们目前是没有条件当然这块呢他就会去干嘛呢就会去发请求然后呢是这有一个resultresult之后呢这时候他正常返回比如说正常返回了返回之后啊咱们会去拿到
[03:19] data里边有一个list拿到具体数据是吧拿到total拿到total这个是列表这个呢就是他的total好吧host咱们暂时还没用头好吧如果说错误的话他就会返回错误信息行那这个呢就是那个要去查询请求的时候他的一些参数那当然你也可以怎么着呢你也可以按下F12F12的话你可以练咱们
[03:45] 先点一下频道再去点一下敏感词来再去玩清调来看看当前敏感词当前list然后你可以往上拉然后往下走你看这个参数其实在这已经能够展示出来了第一个参数就是当前的表名是吧第二个是配置第三个是size第四个就是ware看明白了吗好了行这个咱们查询咱们就说到这最终你这个数据是怎么展示的这个数据
[04:15] 这个数据展示咱们还要再去看一下他最后是附给了list那肯定是要辨认list去展示当前的数据我给大家看一下这里边你可以往上翻这里边你看最终的你看并没有去某一些词你看这里边也没有什么敏感词创建时间和操作这个是怎么来的好来看一看当前它是引用了色试语道里边是引用了一个my色试语道其实就是当前有一个色试语道
[04:45] 就在当前目录下面compounds组件里边有一个search result怎么可以打开打开当前的它有一个search result你看这里边这里边其实就有什么敏感词是吧它就会把当前这个例子给循环了循环之后比如说它的敏感词创建时间还有操作在这通通都能够展示这能看明白吧当然当前的组件当前组件必须得是让当前的什么当前index去引用
[05:16] 才能用好吧让他引用好这个是查询是查询比如说我现在想去做一个修改或者是或者是新增其实都一样咱们现在就可以看修改和新增打开找到谁还是找到这个search result当你去干嘛当你去点编辑的时候编辑的时候是不是要去修改没问题吧OK这时候他就是去调用了当前这个方法
[05:44] 那可以搜一下当前这个方法OK这个呢你看这个方法呢他又去调了一个this editor item那这个是在哪呢this呢其实就在index.view中去找当前那个editor date就就他其实就是他啊行那这个啊这个的话其实就是当前的某一行数据某一行数据啊
[06:07] 那最终呢咱们就会去呃去展示当前的数据这个数据的话呢其实呢又会去找谁呢你看这个当前这个啊这个咱们去搜搜搜的话好像搜不着是吧你可以再去看一下这个editor是谁这个editor就是在compoints下面有一个common editor看到了吗是不是他呀好可以那咱们去点进去看一看嗯点进去那咱们就在这去找找啊找到当前compoints有一个呃
[06:37] common edit看到了吧其实这个呢就是当前的一个一个弹的一个窗啊应该不是不是弹那个窗啊所以就是个弹那个窗啊就是一个弹窗那这弹窗里边呢就是你传过来的一些参数要去展示当前的这种数据你看啊点一下不就是个弹窗吗是吧当然啊这里边还有些东西你们在我在我在我在我在这看啊那当你去点edit的时候啊他就会去调用当前这个edit你看刚才不说了吗这个他就会干嘛呢
[07:07] 他就会掉editor里边的这个editor看到了吧他就会去掉这个掉这个的时候呢他就会呢把当前这个model给改了改成edit哎改成edit之前咱们做查询的时候啊咱们做查询的时候并没有什么呢并没有咱们的任何这种editor也没有什么model啊没有model啊你看看下这个in sb里边出说出说参数里边是不是没有model啊
[07:35] 这时候他往Pyram里边去加了一个什么加了一个当前的什么这种model加了一个model是edit好当然这样这里边他会有一个提交比如说你在这你点了一下编辑然后我去改了一个改了个东西是吧点确定不点确定的时候会触发一个方法这个方法就是现在的哪个方法叫submit好咱们可以看一下这什么密码好这个就是submit
[08:05] 这个Summit其实我要去解释一下主要的就是能够去拼接参数主要是拼接参数首先他会去把当前那个输入框框弹窗里边的一些值给你循环了因为这个Adj 其实已经改了这时候他就会往set3边去push值这个就是你的field第二个就是你的value
[08:32] Field的Value其实又对应了谁敏感词字段对应的就是Field然后敏感词111就是你的值看明白吧它是一个集合然后集合完之后你看它这块又把这个Param重新附了下值重新附了下值你看这个Model摄制进去Table怎么样Table摄制进去Table的话其实就在哪里就在当前Index.VU从哪里还有这个Value
[08:59] OK那这个WareWare的话他默认的话会去传一个ID然后呢也会传个EQ也会传个EQ因为修改的话肯定是能够拿到这个值的把这ID值好吧然后下面是有一个Sets这个Sets就是一个集合就这个集合那这时候呢咱们就会去调用以前这个值用当前这个的时候呢他就会去Zabomit会把当前的值啊会调用什么呢调用当前的Update
[09:27] OK那这个呢其实你就能够想到啊其实他就是掉的是这一块就在这块啊所以说呢最终呢就会去发生或者叫发送修改的操作发送修改的操作好行那这个啊这个咱们就说到这好吧行那咱们呢咱们就下面就继续往下讲好吧继续往下讲啊下面还有一个是吧还有一个什么还有一个是叫做新增
[09:54] 新增的修改就差不多无非就是在你这在你这到底是往下找在这里边在这里边在这里边上面有一个东西有个东西你当前你调用爱的的时候他这个恩卷是空的修改的时候这个恩卷是为有值的这恩卷你就可以理解为就是一行的数据因为你要是新增的话肯定是没有一行的数据并且这model设置为爱的修改model设置为爱的好
[10:27] 那这个就做完了啊那这里边其实还有一个还有个什么东西还有一个删除还有一个删除啊那删除的时候呢咱们又来看一下啊那删除的时候呢其实就是嗯再往下往下找往下找啊咱们在这找吧在这找啊你看首先呢他往上走啊当你点删除的时候他就会操作这个东西好咱们可以查一下这个方法啊好往下走他就会去掉这个在这时候掉这时候呢他先呢会干嘛呢先去给你
[10:57] 先去给你提示一下是吧你去删除是吧然后咱们再去调用当前this delete好点一下那类似这边这时候你看今天还是拍什么还是拍什么但拍什么首先只有一个table这个table的话就是你的表名就是在index view中在这其实你已经写好的表名然后再往下再往下的话就是你的一个vr条件条件的话咱们都是通过it
[11:26] 就是通过ID去拿的好吧最终呢他就会去调用咱们的接口把这个PARAM转进去啊送转到DTO中然后把这个接口调用完之后呢他就会去真正的去删除好吧那这时候呢这个增传改查呢其实咱们这一块呢就算是说完了啊那当然还有些其他的还有其他的你也可以参考当前这个当前这个敏感词呢去设置其实都是差不多的啊最主要的呢
[11:53] 最主要的就是你要理解当前DTO中你每一个比如新增你要传什么参数修改需要传什么参数是吧然后还有是分别查询是吧还有什么还有删除这个都需要传哪些参数这个参数你都明白了咱们这个前台就好写然后你这个传正确的参数它就能去执行正确的操作好吧行那这个封装的前后台的封装调试咱们就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个敏感词管理功能的前后端实现，包括前端 Vue 组件的编写、数据交互和后端 Java 实体类与枚举的定义。

2) 按时间顺序列出每张画面的要点：
画面1：打开项目根目录，选中 `sensitive` 文件夹，准备进入敏感词管理模块。
画面2：在 `index.Vue` 文件中，定义了搜索表单的 `params`，包含 `AD_SENSITIVE`、分页参数、搜索条件等。
画面3：在 `CommonTableEnum.java` 中定义了 `AD_SENSITIVE` 等枚举值及其权限配置。
画面4：在 `index.Vue` 中，继续编辑 `params`，添加了 `created_time` 字段。
画面5：在浏览器中访问敏感词管理页面，显示了敏感词列表和搜索框。
画面6：在 `index.Vue` 中，定义了 `search-tool`、`search-result` 等组件的引用和数据交互。
画面7：在 `index.Vue` 中，继续编辑 `params`，添加了 `created_time` 字段。
画面8：在 `CommEditor.Vue` 文件中，定义了编辑器组件的 `data` 和 `methods`，包括 `add` 方法。
画面9：在 `CommEditor.Vue` 中，继续编辑 `data`，添加了 `entry` 字段，并定义了 `editData` 方法。
画面10：在 `CommEditor.Vue` 中，定义了 `el-form` 和 `el-radio-group` 等表单元素。
画面11：在浏览器中，弹出“修改-敏感词”对话框，输入框中显示“敏感词11”。
画面12：在 `CommEditor.Vue` 中，继续编辑 `data`，添加了 `entry` 字段。
画面13：在 `CommEditor.Vue` 中，定义了 `deleteData` 方法，包含 `confirmDelete` 确认框。
画面14：在 `CommonDto.java` 中，定义了 `CommonDto` 实体类，包含 `size`、`page`、`model`、`name`、`where`、`sets` 等字段。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2：
```Vue
<template>
  <div>
    <changePage="changePage">
    <deleteData="deleteData">
    <pageSize="params.size">
  </div>
</template>

<script>
import SearchTool from './components/SearchTool.Vue'
import SearchResult from './components/SearchResult.Vue'
import Editor from './components/CommEditor.Vue'
import [loadList] from '@/api/common'
import DateUtil from '@/utils/date'
export default {
  name: 'ChannelManager',
  data() {
    return {
      params: {
        name: 'AD_SENSITIVE',
        page: 1,
        size: 10,
        where: []
      },
      total: 0,
      host: '',
      list: [],
      fields: [
        {
          label: '敏感词', name: 'sensitives', type: 'input', placeholder: '请输入敏感词', rule: [
            { required: true, message: '请输入敏感词', trigger: 'blur' },
            { min: 2, max: 8, message: '敏感词在2-8个字符', trigger: 'blur' }
          ]
        },
        {
          label: '创建时间', name: 'created_time', type: 'hidden', value: DateUtil.format13HH(new Date()).getTime()
        }
      ]
    }
  }
}
</script>
```

画面3：
```java
package com.heima.model.admin.enums;

import lombok.Getter;

public enum CommonTableEnum {
    AD_CHANNEL("*", true, true, true, true),
    AD_SENSITIVE("*", true, true, true, true),
    //APP用户
    AP_ARTICLE("*", true, false, false, false),
    AP_ARTICLE_CONFIG("*", true, false, true, false),
    AP_USER("*", true, false, true, false);

    String filed;
    boolean list; //开启列表权限？
    boolean add; //开启新增权限？
    boolean update; //开启修改权限？
    boolean delete; //开启删除权限？

    CommonTableEnum(String filed, boolean list, boolean add, boolean update, boolean delete) {
        this.filed = filed;
        this.list = list;
        this.add = add;
        this.update = update;
        this.delete = delete;
    }
}
```

画面4：
```Vue
<template>
  <div>
    <changePage="changePage">
    <deleteData="deleteData">
    <pageSize="params.size">
  </div>
</template>

<script>
import SearchTool from './components/SearchTool.Vue'
import SearchResult from './components/SearchResult.Vue'
import Editor from './components/CommEditor.Vue'
import [loadList] from '@/api/common'
import DateUtil from '@/utils/date'
export default {
  name: 'ChannelManager',
  data() {
    return {
      params: {
        name: 'AD_SENSITIVE',
        page: 1,
        size: 10,
        where: []
      },
      total: 0,
      host: '',
      list: [],
      fields: [
        {
          label: '敏感词', name: 'sensitives', type: 'input', placeholder: '请输入敏感词', rule: [
            { required: true, message: '请输入敏感词', trigger: 'blur' },
            { min: 2, max: 8, message: '敏感词在2-8个字符', trigger: 'blur' }
          ]
        },
        {
          label: '创建时间', name: 'created_time', type: 'hidden', value: DateUtil.format13HH(new Date()).getTime()
        }
      ]
    }
  }
}
</script>
```

画面6：
```Vue
<template>
  <div>
    <search-tool changeParams="changeParam" :addData="addData">
    <search-result ref="searchResult" :list="list" :host="host" :total="total" :tables="this.params.name"
      :editData="editData" :deleteData="deleteData" :changePage="changePage" :pageSize="params.size">
    </search-result>
  </div>
</template>

<script>
import SearchTool from './components/SearchTool.Vue'
import SearchResult from './components/SearchResult.Vue'
import Editor from './components/CommEditor.Vue'
import [loadList] from '@/api/common'
import DateUtil from '@/utils/date'
export default {
  name: 'ChannelManager',
  data() {
    return {
      params: {
        name: 'AD_SENSITIVE',
        page: 1,
        size: 10,
        where: []
      },
      total: 0,
      host: '',
      list: [],
      fields: [
        {
          label: '敏感词', name: 'sensitives', type: 'input', placeholder: '请输入敏感词', rule: [
            { required: true, message: '请输入敏感词', trigger: 'blur' },
            { min: 2, max: 8, message: '敏感词在2-8个字符', trigger: 'blur' }
          ]
        },
        {
          label: '创建时间', name: 'created_time', type: 'hidden', value: DateUtil.format13HH(new Date()).getTime()
        }
      ]
    }
  }
}
</script>
```

画面8：
```Vue
<template>
  <div>
    <el-button v-if="!disable" @click="dialogFormVisible = true">编辑</el-button>
    <el-dialog :title="title" :visible.sync="dialogFormVisible" width="50%">
      <el-form :model="form" :rules="rules" ref="form">
        <el-form-item label="敏感词" prop="sensitives">
          <el-input v-model="form.sensitives" placeholder="请输入敏感词"></el-input>
        </el-form-item>
        <el-form-item label="创建时间" prop="created_time">
          <el-input v-model="form.created_time" placeholder="请输入创建时间"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="submitForm">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { updateData } from '@/api/common'
export default {
  name: 'comm-editor',
  props: ['title', 'fields', 'table', 'submitSuccess'],
  data() {
    return {
      disable: false,
      dialogFormVisible: false,
      formLabelWidth: '86px',
      entry: {},
      rules: {}
    }
  },
  methods: {
    add: function() {
      this.dialogFormVisible = true
      this.entry = {}
    },
    submitForm: function() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          updateData(this.entry).then(res => {
            this.$message({ type: 'success', message: '操作成功！' })
            this.dialogFormVisible = false
            this.submitSuccess()
          }).catch(err => {
            this.$message({ type: 'error', message:

