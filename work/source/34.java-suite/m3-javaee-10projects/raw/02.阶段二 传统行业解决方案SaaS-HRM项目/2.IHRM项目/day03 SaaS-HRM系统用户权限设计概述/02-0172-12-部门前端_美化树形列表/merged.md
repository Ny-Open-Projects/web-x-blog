# 12-部门前端：美化树形列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\12-部门前端：美化树形列表_【海量资源尽在 ubkz.com】.mp4
- 时长 5分39秒（音频 339s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了现在已经把这颗竖形结构呢其实已经给它构造出来了并且可以点击那接下来就是说呢它跟我们的需求还是有点点不相符啊就是说样式上面的一些内容那对于样式上面的内容呢我们这边就快速的把它处理掉其实就可以了那在这边呢我简单的来说一下在这边我已经都给各位准备好了那我就可以一点一点的自己去改造了好了那在这边呢我这回呢用DIV来去替换里面的SPA
[00:34] 也为来去替换里面的span好了这边这个span呢就不要什么样式了OK那我们来看一下OK那现在呢其实这些研发部啊等等等等都已经展示出来了那接下来呢不太理想的就是这个append和这个delete那这些内容append跟delete这些内容OK咱们先把它都删掉没什么用没什么用好了那接下来这些内容我要显示成什么样的效果呢是这样的我准备啊跟上边这个
[01:08] 添加等等这些一样跟它一样所以呢我就从上面这一端直接copy一份下来直接copy一份过来给它放到这边OK那好了我们这回再来看一下效果好了这回效果就好很多了但是呢就是最好啊这每一个什么研发部前面应该有一个小的标签告诉他我这边能打我这边能点击还是不能点击那这些内容呢其实也比较简单了
[01:46] 这些都是美工的一些人员帮助我们做好的那接下来呢我就可以直接在S在S班这边做一个处理比如说呢我可以加上一个爱标签那加上一个爱标签我们再来看一下效果好了前面就一个小人那其实这是我想跟各位说的只有当叶子节点的时候叶子节点它是一个小人的一个标志那这个应该怎么处理呢其实我们可以加一个判断V刚EFV刚EF
[02:21] 那这个微钢衣服的写法其实很简单在人家这棵树里面它已经通过一个slot scope这种形式把我们这个节点里面的所有内容都已经给我们提供好了就是说你当前这个节点其实代表的是一个我们的部门的一个对象那除了部门对象呢它也是一个节点它所以这边是两个属性那这两个属性简单的跟各位做一个介绍啊node它里面包含了是否展开
[02:53] 是否比如说是否叶子节点叶子节点好了那这个data部分呢其实就是我们的部门对象里面包含我们的比如说有ID有NAME等等等等你查询出来的内容所以对于我们来说我刚才的要求是只有是叶子节点的时候让它展示这个小人标志所以我这边判断一下就是根据node来做node.is left好了那这样一来你会发现只有叶子节点它会才加上这个小人标志
[03:23] 那对于非叶子节点我们这边加的是一个爱标签Ctrl C Ctrl V爱标签那好了接着我们再来看那这回你会发现当然非叶子节点的时候让它去显示是吧V-elseOK刷新一把那这样一来呢我们这个基本的就已经勾到好了但是其实还有点细节问题就是说现在这个加号最好呢如果说是
[04:16] 闭合状态假号如果点开之后呢是不是可以让它是一个简号啊那这边呢其实也有办法很简单如何去做各位来看这边加一个冒号代表我要做判断了那判断的依据就是node点它有一个它有一个判断的依据就是看一下当前这玩意儿是否已经展开叫做expandesp没错expand如果当前这个是已经展开的这么一个状态
[04:49] 让它去显示当前这个样式如果没有呢这边也准备好了Ctrl C 靠过来Ctrl V那好了这回我们再来看一下整个的一个效果这个好像正好是写反了是吧正好写反了抱歉做一个修改OK刷新一把那这样一来呢我这个基本的这个竖形结构其实咱们就已经都做好了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Vue.js 中使用 Element UI 的树形组件（el-tree）来实现组织架构的可视化，并通过代码修改节点样式和交互逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 HRM 系统的组织架构页面，显示了“研发部”、“测试部”等部门，鼠标悬停在“研发部”上。
画面 2: 在 VS Code 中编辑 `Index.Vue` 文件，修改了树形组件的节点结构，添加了 `el-button` 用于“Append”和“Delete”操作。
画面 3: 在 VS Code 中编辑 `Index.Vue` 文件，对树形组件的节点结构进行调整，准备添加展开/折叠图标。
画面 4: 在 VS Code 中编辑 `Index.Vue` 文件，对树形组件的节点结构进行调整，准备添加展开/折叠图标。
画面 5: 展示了 HRM 系统的组织架构页面，页面显示“暂无数据”，表示数据未加载或已清空。
画面 6: 在 VS Code 中编辑 `Index.Vue` 文件，为树形组件的节点添加了 `v-if` 和 `v-else` 条件渲染，用于区分父节点和子节点。
画面 7: 展示了 HRM 系统的组织架构页面，显示了“研发部”、“测试部”等部门，鼠标悬停在“测试部”上。
画面 8: 在 VS Code 中编辑 `Index.Vue` 文件，为树形组件的节点添加了 `v-if` 和 `v-else` 条件渲染，用于区分父节点和子节点。
画面 9: 在 VS Code 中编辑 `Index.Vue` 文件，为树形组件的节点添加了 `v-if` 和 `v-else` 条件渲染，用于区分父节点和子节点。
画面 10: 展示了 HRM 系统的组织架构页面，显示了“研发部”、“测试部”等部门，鼠标悬停在“研发部”上。
画面 11: 展示了 HRM 系统的组织架构页面，显示了“研发部”、“测试部”等部门，鼠标悬停在“研发部”上。
画面 12: 在 VS Code 中编辑 `Index.Vue` 文件，为树形组件的节点添加了 `v-if` 和 `v-else` 条件渲染，用于区分父节点和子节点。
画面 13: 展示了 HRM 系统的组织架构页面，显示了“研发部”、“测试部”等部门，鼠标悬停在“研发部”上。
画面 14: 展示了 HRM 系统的组织架构页面，显示了“研发部”、“测试部”等部门，鼠标悬停在“研发部”上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```Vue
<el-tree :props="{label: 'name'}" :data="depts" node-key="id" default-expand-all>
  <div class="generalclass" slot-scope="{ node, data }" style="width:95%">
    <span>{{ node.label }}</span>
  </div>
</el-tree>
```

画面 3:
```Vue
<el-tree :props="{label: 'name'}" :data="depts" node-key="id" default-expand-all>
  <div class="generalclass" slot-scope="{ node, data }" style="width:95%">
    <span>{{ node.label }}</span>
  </div>
</el-tree>
```

画面 4:
```Vue
<el-tree :props="{label: 'name'}" :data="depts" node-key="id" default-expand-all>
  <div class="generalclass" slot-scope="{ node, data }" style="width:95%">
    <span>{{ node.label }}</span>
  </div>
</el-tree>
```

画面 6:
```Vue
<el-tree :props="{label: 'name'}" :data="depts" node-key="id" default-expand-all>
  <div class="generalclass" slot-scope="{ node, data }" style="width:95%">
    <span>{{ node.label }}</span>
  </div>
</el-tree>
```

画面 8:
```Vue
<el-tree :props="{label: 'name'}" :data="depts" node-key="id" default-expand-all>
  <div class="generalclass" slot-scope="{ node, data }" style="width:95%">
    <span>{{ node.label }}</span>
  </div>
</el-tree>
```

画面 9:
```Vue
<el-tree :props="{label: 'name'}" :data="depts" node-key="id" default-expand-all>
  <div class="generalclass" slot-scope="{ node, data }" style="width:95%">
    <span>{{ node.label }}</span>
  </div>
</el-tree>
```

画面 12:
```Vue
<el-tree :props="{label: 'name'}" :data="depts" node-key="id" default-expand-all>
  <div class="generalclass" slot-scope="{ node, data }" style="width:95%">
    <span>{{ node.label }}</span>
  </div>
</el-tree>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

