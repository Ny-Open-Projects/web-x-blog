# 08-分配角色：需求分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\08-分配角色：需求分析_【海量资源尽在 ubkz.com】.mp4
- 时长 5分0秒（音频 300s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 当然了,权限这套页面其实在这Promission里面都有,我们可以简单的来过一下。
[00:07] 跟之前的逻辑一上,首先找Router,在Router里面有我路由的配置,其中呢,首先我点击的是一个Promission-Index,那Promission-Index它访问的是我们配置私下的Index,Promission下,配置私,Index。
[00:25] 在这个页面里面的内容相对来说比较简单都不难,首先第一个,Yard Table。
[00:31] 就是打你查新的书记构造出来那底下呢dialeg就是你添加不是有添加权限吗添加权限或者查看权限不是有一个隐藏域吗或者一个隐藏的一个框框让它显示或者隐藏吧好了底下还有一个就是API的一个权限列表都是一个dialeg然后呢通过对这些不同的链按钮绑定不同的事件让它们显示弹出或者隐藏这个基本上代码都比较简单好了这个我们看过了
[01:00] 权限相关的内容那接下来呢我们继续往下看就是我们今天的第二个点就是分配角色那这个分配角色和我们分配权限呢其实都是大同小异的都差不多那咱们先看一下分配角色那分配角色其实是对某一个用户进行角色的一个分配比如说呢咱们公司新来了一个员工登录到我们系统之后呢登录到录入到我们系统之后呢我们的管理员
[01:30] 会对这个用户角色进行一个划分比如说呢招入过来的是一个普通员工那就是一个员工没有什么角色那如果招入过来的是一个我们的人事经理那可以给他划分成人事经理这个角色那有了角色那接下来呢是不是就可以对角色分配一个权限比如说人事经理可以访问第一个菜单第二个菜单那这个一分配角色一分配权限那张三在登录系统的时候是不是自然而然就能看到第一个和第二个菜单了
[01:59] 所以呢我们分配角色和分配权限是我们比较权限控制里面比较重要的两个点因为他们直接决定了你一个用户能够访问什么内容那我们先来看分配角色那分配角色这边呢已经把这个基本的样式呢已经给各位以截图的形式给各位准备到这边了其实呢这些基本的代码我们在我们的前端工程里面也有体现员工可以分配角色好了
[02:31] 那接下来角色可以对某一个角色分配权限这都是可以的这都是可以的并且呢不管是我现在谈出的这个分配角色的这个框框还是我谈出的这个分配权限的这个框框咱们不需要额外的做太多的工作它就有显示首先跟各位来声明分配角色的时候一点分配角色我就把当前企业下的所有角色给它查出来
[03:01] 当前企业在所有角色查出来角色我们不是做过查询列表吗那这不就是查询列表吗好了那除了分配角色之外呢还有公司的这里面的分配权限那我一点分配权限其实我就是把我们权限相应的所有内容都已经给他查出来那权限相关的那这个时候有朋友就会说呀你权限设置权限列表不是有SaaS企业管理吗那你公司给他分配权限的时候为什么没有呢是因为SaaS企业管理是我们HRM这个系统管理员才能访问啊
[03:32] 那普通的一个小的企业那用我们的一个租户企业它能够有这些权限吗显然没有所以我这边已经把它给屏蔽掉了OK好了这个就是跟各位来看的我们接下来要完成的分配权限分配角色想要做的一些基本的一个需求的一个说明OK那接下来我们一个一个去完成它首先就是我们分配角色的相应内容
[03:59] 那分配角色相应内容这边我们都说过了一个用户可以具备很多的角色一个角色可以分配给普通的用户所以用户和角色之间必然是多得多那这个需求呢我们都知道那接下来其实在我们分配角色我们关注的其实还是API那我们找到这个角色API错了找到用户API给用户分配角色嘛那找到用户API继续往下看这边有一个分配角色的这么一个请求
[04:28] 那前端发送过一个请求它给我们传递的数据呢其实不多一共呢就这么两个类型首先第一个ID那这个ID指的是你要对哪个用户划分权限划分角色它是用户ID那这个Row IDS指的是我一个用户可能有很多个角色啊所以它指的是多个角色的ID
[04:50] 好了这个如果各位都能够接受的话那接下来我们就可以去完成分配角色这个后端代码的一个编写

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 SAAS-HRM 系统中实现用户角色权限分配功能，包括前端界面操作、Vue 代码实现和后端 API 接口定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 SAAS-HRM 系统的“权限管理”页面，列出多个权限模块，如“查看部门”、“员工管理”等，同时在任务栏预览了 Visual Studio Code 中的项目结构。
画面2：在 Visual Studio Code 中展示 `index.Vue` 文件的代码，包含一个弹窗组件，用于分配角色，其中包含 `el-dialog` 和 `el-table` 组件的定义。
画面3：在 Visual Studio Code 中展示 `index.Vue` 文件的代码，继续展示弹窗组件的 `el-dialog` 部分，包含 `el-button` 和 `el-table-column` 的定义。
画面4：在 Visual Studio Code 中展示 `index.Vue` 文件的代码，展示 `handlerApiList` 方法，用于处理 API 请求，以及 `created` 生命周期钩子。
画面5：展示 PPT 页面，标题为“3 分配权限”，子标题“3.1 需求分析”，内容说明完成对角色权限的分配。
画面6：展示 PPT 页面，标题为“2 分配角色”，子标题“2.1 需求分析”，内容说明使用 RBAC 模型进行权限管理，用户与角色是多对多关系。
画面7：展示 SAAS-HRM 系统的“员工”列表页面，显示员工信息，包括姓名、手机号、工号等，并提供“分配角色”操作。
画面8：展示 SAAS-HRM 系统的“员工”页面，点击“公司设置”后，页面跳转到“公司设置”页面。
画面9：展示 SAAS-HRM 系统的“角色管理”页面，显示“为【人事经理】分配权限”的弹窗，列出可分配的权限模块。
画面10：展示 SAAS-HRM 系统的“公司设置”页面，点击“角色管理”后，页面跳转到“角色管理”页面。
画面11：展示 SAAS-HRM 系统的“角色管理”页面，显示“为【人事经理】分配权限”的弹窗，鼠标悬停在“用户管理权限”上。
画面12：展示 PPT 页面，标题为“2 分配角色”，子标题“2.1 需求分析”，内容说明使用 RBAC 模型进行权限管理，用户与角色是多对多关系。
画面13：展示 SAAS-HRM 系统的“API 文档”页面，左侧菜单栏显示“角色”选项。
画面14：展示 SAAS-HRM 系统的“API 文档”页面，显示“PUT /user/assignRoles 分配角色”的接口文档，包含请求参数和示例 JSON 数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```Vue
<template slot-scope="scope">
  <el-table-column fixed prop="code" label="编号" width="200">
    <template slot-scope="scope">
      <el-button @click="handleCreate(scope.row.id,scope.row.type)">编辑</el-button>
    </template>
  </el-table-column>
  <el-table-column fixed prop="description" label="描述" width="280">
    <template slot-scope="scope">
      <el-button @click="handleCreate(scope.row.id,scope.row.type)">编辑</el-button>
    </template>
  </el-table-column>
</template>
```
画面3：
```Vue
<el-dialog title="分配角色" :visible.sync="dialogVisible" style="height:400px;line-height:1px">
  <el-button class="filter-item fr" size="small" style="margin-left: 10px; max-height: 200px" @click="handleCreate(null,1)">新增</el-button>
  <el-table data="split" fit style="width: 100%" :max-height="200">
    <el-table-column fixed prop="code" label="编号" width="200">
      <template slot-scope="scope">
        <el-button @click="handleCreate(scope.row.id,scope.row.type)">编辑</el-button>
      </template>
    </el-table-column>
    <el-table-column fixed prop="description" label="描述" width="280">
      <template slot-scope="scope">
        <el-button @click="handleCreate(scope.row.id,scope.row.type)">编辑</el-button>
      </template>
    </el-table-column>
  </el-table>
  <div slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="saveOrUpdate">确 定</el-button>
  </div>
</el-dialog>
```
画面4：
```javascript
handlerApiList(id) {
  this.pid = id;
  list(type, pid, id).then(res => {
    this.apiList = res.data.data;
    this.apiDialogVisible = true;
  });
},
created () {
  this.getList();
}
```
画面14：
```json
{
  "id": "string",
  "roleId": [
    "string"
  ]
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：
标题：3 分配权限
子标题：3.1 需求分析
内容：完成对角色权限的分配。
画面6：
标题：2 分配角色
子标题：2.1 需求分析
内容：由于使用了RBAC模型对权限进行统一管理，所以每个SAAS-HRM平台的用户都应具有角色的信息。进而通过角色完成对权限的识别。众所周知，一个用户可以具有很多的角色，一个角色可以分配给不同的用户，所以用户和角色之间是多对多关系。
画面12：
标题：2 分配角色
子标题：2.1 需求分析
内容：由于使用了RBAC模型对权限进行统一管理，所以每个SAAS-HRM平台的用户都应具有角色的信息。进而通过角色完成对权限的识别。众所周知，一个用户可以具有很多的角色，一个角色可以分配给不同的用户，所以用户和角色之间是多对多关系。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

