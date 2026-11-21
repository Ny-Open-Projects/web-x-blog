# 11-部门前端：构造部门树形列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\11-部门前端：构造部门树形列表_【海量资源尽在 ubkz.com】.mp4
- 时长 7分18秒（音频 438s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那其实对于这个页面呢还有一些细节问题需要跟各位简单的来做一个交代啊那比如说这个页面呢我勾到的效果是这样的我们打开浏览器来看一下右边有操作一点击它会让我添加子部门或者可以查看带分配的员工那这个是怎么做到的其实很简单我们打开代码部分来看一下在代码部分当中用的是Elemen UI的一个组件叫做ELdropdown这是它的一个组件
[00:30] 那对于这个组件来说呢各位有兴趣的话可以从ELEMEN UI这个官网上去找一下它的推荐使用方式就是这样那接下来呢我们重点关注的其实不是上面这个企业名称等等的这些内容而我们关注的是底下应该有一棵树那这个树应该从哪去找呢其实不难也是通过ELEMEN UI它提供的一些组件当中去找
[00:59] 那你找一下左边的组件有很多我们找到的是竖形的一个组件tree竖形组件那在竖形组件里面呢其实有很多它提供的一些组件的类型比如说呢对于我来说呢我想要构造的其实跟这个是有点类似的或者跟这个是有点类似的那不管是哪种方式我把它它的原码直接拷贝过来直接拷贝过来我直接把这颗tree拷过来Ctrl C
[01:32] 这边注意写到底下Ctrl VOK那拷过来之后呢有一些问题呢需要我和各位简单的来做一个交代就是这棵树我们来看一下人甲是怎么构造的这棵树的内容首先呢这边有一个Data指的是一个Data 5那我们来看底下是它提供的一些基础数据Data 5其实指的是这一串内容
[02:08] 那各位来看这一串内容不就是一个数组吗不就是一个叫做数组吗只不过呢人家这个数组做了一些基本的一个改造和处理做了一个基本的改造和处理它是以它是以这种负极结构你看这边是一棵树这里面有一个抽准指的是一极下有个二极一杠一一有个三极一杠一三极一杠一杠二我们来看一下是不是一极一杠一一极等等
[02:36] 是不是说明它是一颗构造的是一个带有层级结构的一棵树这么一个数据但是对于我们目前来说这个Data5还没有数据那没有数据不是树形结构的我们只是得到了一个基本的数据那接下来我们应该怎么做呢其实不难不难我已经给各位准备好了一个Common API这个Common API里面它在Utils下的common.js
[03:05] 我写了一个方法就是直接把数组转化成带有层级结构的内容所以我们可以这样res.data.data.dpts这是得到的我们的基本数组那基本数组经过方法转化好了之后就能放到这个类似点dpts当中了那这样一来就是将普通的数组转化为
[03:38] 父子结构结构OK那好了我们接下来再来看一下再来看一下我先把上面删掉因为它会报错啊我们接下来呢调用方法之后再来打印一下看一下这个类似点点DPTS是不是就转化成父子结构了好了打开F2刷新一把OK打开控台好了各位来看第一条它有抽准
[04:22] 好了那接着呢它第二条也有抽准那这样一来是不是咱们把得到的这块内容我们得到的是内容有很多的有很多的我们已经把得到内容给它转化为父子的这种层级结构了那转化成父子层级结构之后我们就可以借助把这些都删掉借助这种形式去构造树那这棵树里面Data部分指的是我们数据模型已经准备好了DEPTS我们刚才打印出来看到了效果
[04:57] 好了这边是不是show checkbox那show checkbox指的是是否显示前面的可选框对于我来说不需要显示就关掉了OK好了这边呢还有node key那node key呢我们指定的就是ID这个也没有什么可说的就用它的默认其实就可以还有defaultand append是否默认展开那你想展开就展开好了这个and append什么select node
[05:27] 这个Supply node呢其实就是说是否定位到你当前展开的节点这个我们也不需要也给它删掉就可以了OK当然了在这里面它还自己构造了几个按钮button我们先来看一下基本的内容究竟有没有啊先来看一下基本内容究竟有没有OK各位来看啊基本的这个构造出来但是只有后半部分前面的这个label标签是不是就是说这棵树究竟叫什么名字是不是还没有啊
[06:01] 那没有很简单是因为它需要一些设置就是指定一下你显示的究竟是哪个内容人家这块设置呢其实在这些基本的案例里面都有可以借助这么一个设置来做就是default props那么可以在这个数上给它加上一个default看一下叫什么这个就叫props冒号props它指的是一个数组
[06:36] 那数组里面呢需要我们指定的来看需要我们指定的是一个label就是说你这个标签究竟用什么label那label其实用的就是我们DPT对象当中的NEM属性其实就可以了OK那我们再来看一下效果OK那这样一来基本的这个样式其实也已经构造出来了并且这边你点击你点击都没什么问题

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Vue 项目中使用 Element UI 的树形组件（el-tree）实现部门组织架构的展示与增删改操作。

2) 按时间顺序列出每张画面的要点：
画面1：
- 编辑器中显示 Vue 组件 `index.Vue` 的模板部分，包含一个 `el-tree` 组件，用于展示部门树形结构。
- 代码片段：
  ```html
  <div style="overflow: scroll;white-space:nowrap" class="treeBox">
    <span class="fa fa-university" aria-hidden="true"></span>
    <span><strong>{{departData.companyName}}</strong></span>
    <span class="fr">
      <span class="departInfo">
        <span class="colGreen" title="在岗人数">...</span>
        <span class="colGreen" title="正式员工">...</span>
      </span>
    </span>
    <div class="treeInfo">
      <div class="treeInfo">
        <span class="el-dropdown-link">
          <span class="el-icon-arrow-down el-icon-right"></span>
          <span class="el-dropdown-menu slot="dropdown">
            <el-dropdown-item @click="handAddD">添加子部门</el-dropdown-item>
            <el-dropdown-item @click="handleListD">查看子部门员工</el-dropdown-item>
          </el-dropdown-menu>
        </span>
      </div>
    </div>
  </div>
  ```

画面2：
- 代码中 `el-dropdown-menu` 的 `slot="dropdown"` 语法被修改为 `slot-scope`，并添加了 `@click` 事件绑定。
- 代码片段：
  ```html
  <span class="el-dropdown-link">
    <span class="el-icon-arrow-down el-icon-right"></span>
    <span class="el-dropdown-menu slot="dropdown">
      <el-dropdown-item @click="handAddD">添加子部门</el-dropdown-item>
      <el-dropdown-item @click="handleListD">查看子部门员工</el-dropdown-item>
    </el-dropdown-menu>
  </span>
  ```

画面3：
- 浏览器地址栏显示 `Swagger UI`，页面为空白，表明正在访问 API 文档页面。

画面4：
- 浏览器中打开 Element UI 官网的 Tree 组件页面，展示了树形结构的使用示例，包含“使用 render-content”和“使用 scoped slot”两种方式。

画面5：
- 编辑器中显示 `el-tree` 组件的 `slot-scope` 语法，用于自定义节点内容。
- 代码片段：
  ```html
  <el-tree
    node-key="id"
    default-expand-all
    expand-on-click-node="false"
    slot-scope="{ node, data }"
  >
    <span class="custom-tree-node">
      <span>{{ node.label }}</span>
      <span>
        <el-button type="text" size="mini" @click="() => append(data)">Append</el-button>
        <el-button type="text" size="mini" @click="() => remove(node, data)">Delete</el-button>
      </span>
    </span>
  </el-tree>
  ```

画面6：
- Element UI 官网 Tree 组件页面，展示了“使用 scoped slot”示例的代码片段。
- 代码片段：
  ```html
  <div class="custom-tree-container">
    <div class="block">
      <el-tree
        :data="data"
        show-checkbox
        node-key="id"
        default-expand-all
        :render-content="renderContent"
      >
      </el-tree>
    </div>
  </div>
  ```

画面7：
- Element UI 官网 Tree 组件页面，展示了“使用 render-content”示例的代码片段。
- 代码片段：
  ```html
  <div class="custom-tree-container">
    <div class="block">
      <el-tree
        :data="data"
        show-checkbox
        node-key="id"
        default-expand-all
        :render-content="renderContent"
      >
      </el-tree>
    </div>
  </div>
  ```

画面8：
- 编辑器中显示 Vue 组件 `index.Vue` 的脚本部分，正在编写 `getList` 方法，用于获取部门数据。
- 代码片段：
  ```js
  import { list } from "@/api/base/dept";
  import commonApi from "@/utils/common";
  export default {
    data() {
      return {
        activeName: 'first',
        departData: {},
        depts: []
      }
    },
    methods: {
      // 不选表格方法
      getList() {
        list().then(res => {
          this.departData = res.data.data;
          this.depts = commonApi.transformFreezFormat(res.data.depts);
        })
      }
    }
  }
  ```

画面9：
- 编辑器中显示 `getList` 方法的代码，正在添加 `transformFreezFormat` 方法对数据进行格式化。
- 代码片段：
  ```js
  this.depts = commonApi.transformFreezFormat(res.data.depts);
  ```

画面10：
- 浏览器中显示 HRM 系统的部门管理页面，页面标题为“组织架构”，显示了公司名称“江苏传智播客教育科技股份有限公司”。

画面11：
- 编辑器中显示 `index.Vue` 的脚本部分，正在编写 `created` 生命周期钩子，用于在组件创建后调用 `getList` 方法。
- 代码片段：
  ```js
  created: function() {
    this.getList();
  }
  ```

画面12：
- Element UI 官网 Tree 组件页面，展示了 `el-tree` 组件的 `data` 数据结构示例。
- 代码片段：
  ```js
  export default {
    data() {
      return {
        data: [
          {
            id: 1,
            label: '一级 1',
            children: [
              {
                id: 4,
                label: '二级 1-1',
                children: [
                  {
                    id: 9,
                    label: '三级 1-1-1'
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  }
  ```

画面13：
- 编辑器中显示 `index.Vue` 的模板部分，使用了 `el-tree` 组件，并设置了 `data` 和 `slot-scope`。
- 代码片段：
  ```html
  <el-tree
    :data="depts"
    node-key="id"
    default-expand-all
    slot-scope="{ node, data }"
    style="width:100%"
  >
    <span class="custom-tree-node slot-scope="{ node, data }">
      <span>{{ node.label }}</span>
      <span>
        <el-button type="text" size="mini" @click="() => append(data)">Append</el-button>
        <el-button type="text" size="mini" @click="() => remove(node, data)">Delete</el-button>
      </span>
    </span>
  </el-tree>
  ```

画面14：
- 浏览器中显示 HRM 系统的部门管理页面，页面标题为“组织架构”，显示了多个部门，如“研发部”、“测试部”、“开发部”等，每个部门旁边有“Append”和“Delete”按钮。

