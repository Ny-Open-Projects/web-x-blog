# 画面线理解：20_通用封装-前台逻辑流程说明

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\20_通用封装-前台逻辑流程说明【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:58, 01:48, 03:06, 03:53, 04:42, 05:55, 06:42, 07:06, 07:59, 09:52, 10:30, 11:08, 12:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:12:55

1) 这一组画面整体在讲一个敏感词管理功能的前后端实现，包括前端 Vue 组件的编写、数据交互和后端 Java 实体类与枚举的定义。

2) 按时间顺序列出每张画面的要点：
画面1：打开项目根目录，选中 `sensitive` 文件夹，准备进入敏感词管理模块。
画面2：在 `index.vue` 文件中，定义了搜索表单的 `params`，包含 `AD_SENSITIVE`、分页参数、搜索条件等。
画面3：在 `CommonTableEnum.java` 中定义了 `AD_SENSITIVE` 等枚举值及其权限配置。
画面4：在 `index.vue` 中，继续编辑 `params`，添加了 `created_time` 字段。
画面5：在浏览器中访问敏感词管理页面，显示了敏感词列表和搜索框。
画面6：在 `index.vue` 中，定义了 `search-tool`、`search-result` 等组件的引用和数据交互。
画面7：在 `index.vue` 中，继续编辑 `params`，添加了 `created_time` 字段。
画面8：在 `CommEditor.vue` 文件中，定义了编辑器组件的 `data` 和 `methods`，包括 `add` 方法。
画面9：在 `CommEditor.vue` 中，继续编辑 `data`，添加了 `entry` 字段，并定义了 `editData` 方法。
画面10：在 `CommEditor.vue` 中，定义了 `el-form` 和 `el-radio-group` 等表单元素。
画面11：在浏览器中，弹出“修改-敏感词”对话框，输入框中显示“敏感词11”。
画面12：在 `CommEditor.vue` 中，继续编辑 `data`，添加了 `entry` 字段。
画面13：在 `CommEditor.vue` 中，定义了 `deleteData` 方法，包含 `confirmDelete` 确认框。
画面14：在 `CommonDto.java` 中，定义了 `CommonDto` 实体类，包含 `size`、`page`、`model`、`name`、`where`、`sets` 等字段。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2：
```vue
<template>
  <div>
    <changePage="changePage">
    <deleteData="deleteData">
    <pageSize="params.size">
  </div>
</template>

<script>
import SearchTool from './components/SearchTool.vue'
import SearchResult from './components/SearchResult.vue'
import Editor from './components/CommEditor.vue'
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
```vue
<template>
  <div>
    <changePage="changePage">
    <deleteData="deleteData">
    <pageSize="params.size">
  </div>
</template>

<script>
import SearchTool from './components/SearchTool.vue'
import SearchResult from './components/SearchResult.vue'
import Editor from './components/CommEditor.vue'
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
```vue
<template>
  <div>
    <search-tool changeParams="changeParam" :addData="addData">
    <search-result ref="searchResult" :list="list" :host="host" :total="total" :tables="this.params.name"
      :editData="editData" :deleteData="deleteData" :changePage="changePage" :pageSize="params.size">
    </search-result>
  </div>
</template>

<script>
import SearchTool from './components/SearchTool.vue'
import SearchResult from './components/SearchResult.vue'
import Editor from './components/CommEditor.vue'
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
```vue
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
