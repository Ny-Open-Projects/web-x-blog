# 画面线理解：15-部门前端：页面优化以及抽取组件

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\15-部门前端：页面优化以及抽取组件_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 01:36, 02:57, 04:13, 05:13, 06:10, 07:14, 08:09, 08:53, 11:16, 11:43, 12:51, 13:41, 14:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:34:46

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Vue.js 前端项目中使用 Element UI 组件库实现部门管理功能，包括部门列表展示、删除、新增和编辑操作，并涉及后端异常处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 IntelliJ IDEA 中的 Java 异常处理器类 `BaseExceptionHandler`，用于处理 `CommonException` 并返回自定义结果。
画面2：展示 HRM 系统的部门管理页面，显示了部门列表，鼠标悬停在“测试部”上。
画面3：在 Visual Studio Code 中编辑 Vue 组件 `index.vue`，实现删除部门的逻辑，使用 `deleteById` 方法并刷新页面。
画面4：在 Element UI 官网查看 `Message` 组件的文档，说明其用于显示消息提示，可安全地显示 HTML 内容。
画面5：在 Visual Studio Code 中编辑 `index.vue`，使用 `this.$confirm` 弹出确认框，用于删除操作。
画面6：在 Visual Studio Code 中编辑 `index.vue`，导入 API 方法并定义数据结构，用于部门列表展示。
画面7：在 Visual Studio Code 中打开 `add.vue` 组件，准备编写新增部门的逻辑。
画面8：在 Visual Studio Code 中编辑 `add.vue`，定义下拉菜单和图标，用于选择父部门。
画面9：浏览器页面空白，可能为页面加载失败或未正确跳转。
画面10：在 Visual Studio Code 中编辑 `index.vue`，引入 `deptAdd` 组件并绑定到 `ref`。
画面11：在 Visual Studio Code 中编辑 `index.vue`，编写删除部门的确认和处理逻辑。
画面12：在 Visual Studio Code 中编辑 `index.vue`，编写新增部门的逻辑，包括设置父部门 ID 和显示对话框。
画面13：浏览器中显示 HRM 系统的“编辑部门”弹窗，包含部门名称、编码、负责人和介绍字段。
画面14：在 Visual Studio Code 中编辑 `index.vue`，编写更新部门的逻辑，包括调用 `find` 方法获取数据并更新。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@ControllerAdvice
@ResponseBody
public class BaseExceptionHandler {
    @ExceptionHandler(value = Exception.class)
    public Result error(HttpServletRequest request, HttpServletResponse response, Exception e) {
        if (e.getClass() == CommonException.class) {
            CommonException ce = (CommonException) e;
            Result result = new Result(ce.getResultCode());
            return result;
        } else {
            Result result = new Result(ResultCode.SERVER_ERROR);
            return result;
        }
    }
}
```

画面3：
```javascript
handleDelete(id) {
    deleteById(id).then(res => {
        this.Message({
            message: '删除成功',
            type: 'success'
        });
        if (res.data.success) {
            location.reload();
        }
    });
}
```

画面5：
```javascript
this.$confirm('确定删除该部门吗？', '提示', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
}).then(() => {
    this.Message({
        message: '删除成功！'
    });
}).catch(() => {
    this.Message({
        type: 'info',
        message: '已取消删除'
    });
});
```

画面6：
```javascript
import {list, saveOrUpdate, find, deleteById} from "@/api/base/dept"
import commonApi from "@/utils/common"
export default {
    data() {
        return {
            activeName: 'first',
            deptData: [],
            dialogVisible: false,
            dept: {}
        }
    }
}
```

画面7：
```vue
<template>
    <script>
    export default {
    }
    </script>
    <style>
    </style>
```

画面8：
```vue
<el-dropdown class="item">
    <span class="el-icon-arrow-down el-icon-right"></span>
    <el-dropdown-menu slot="dropdown">
        <el-dropdown-item @click="handleList()">查看部门列表</el-dropdown-item>
        <el-dropdown-item @click="handleAdd()">新增部门</el-dropdown-item>
    </el-dropdown-menu>
</el-dropdown>
```

画面10：
```javascript
import deptAdd from "@/components/add"
export default {
    components: (deptAdd),
    data() {
        return {
            deptAdd: 'deptAdd',
            activeName: 'first',
            departData: [],
            depts: []
        }
    }
}
```

画面11：
```javascript
handleDelete(id) {
    this.$confirm('确定删除该部门吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
    }).then(() => {
        deleteById(id).then(res => {
            this.Message({
                message: res.data.message,
                type: res.data.success ? 'success' : 'error'
            });
            if (res.data.success) {
                location.reload();
            }
        });
    }).catch(() => {
        this.Message({
            type: 'info',
            message: '已取消删除'
        });
    });
}
```

画面12：
```javascript
handleAdd(parentId) {
    this.$refs.addDept.parentId = parentId;
    this.$refs.addDept.dialogVisible = true;
}
handleUpdate(id) {
    find(id).then(res => {
        this.$refs.addDept.dept = res.data.data;
        this.$refs.addDept.dialogVisible = true;
    });
}
```

画面14：
```javascript
handleUpdate(id) {
    find(id).then(res => {
        this.$refs.addDept.dept = res.data.data;
        this.$refs.addDept.dialogVisible = true;
    });
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
