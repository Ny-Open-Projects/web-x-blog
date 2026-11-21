# 24-用户管理：构造前端页面-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\24-用户管理：构造前端页面-下_【海量资源尽在 ubkz.com】.mp4
- 时长 3分30秒（音频 210s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好了我们一起来看一下我们刚才的配置好了在我们这个配置这边呢一起来看一下这边这儿有一个问题啊这边应该有一个闭合的大括号这边的加一逗号上面这个逗号不要了好了接下来呢一个一对一对的来找OK那这样一来其实就正确了这样应该就没问题了那好了我们可以一起再来重启一下看一下我这个系统究竟有没有问题
[00:30] 其实这个就是借助它的一个Powertree Table的一个机制我们可以在DEV这边给它添加一个我们的后缀它统一的添加上那接着在它这个Powertree Table里面去针对你添加的这个新的请求后缀进行拼接那拼接了之后如果碰到是当前的这个请求链接它会挂载到你目标请求链接的后面挂载到后面那挂载到后面之后呢它会帮你去检测如果你有了这么一个地址那它会把这个地址给你全部都注释掉或者替换掉
[00:59] 那这就是他的一个执行逻辑那好了我们这回再来看一下刷新OK那各位来看现在呢用户所有数据就已经都有了都有了那么可以这边呢查看一把OK没什么问题这边也可以选择他所属的部门那么试一下能不能更新11测试部走11测试部也没问题那见了呢这边呢可以看一下他的新增员工的一个操作新增员工这边随便写随便写随便写
[01:34] 随便填随便填随便选随便写好了我一提交也没问题但是各位你会发现我这个数据好像有点不太对有点不太对那这个不太对其实跟我们的后台数据有关系了那后台数据我个人推测呢其实是在我们这边查询这边这拼接条件的时候这有点疑问那其实对于我们来说呢没传是不是让他查全部就可以了
[02:01] 默认他没有传这个sdpd我保持疑问所以我这边做一个简单的判断这样就靠谱一点如果你没有传递这个如果传递了让他去判断0或者1如果没传递那就不差把这个条件给他删掉就可以了OK那我们这边再去重新启动一下这个系统的微服务好了这边让他启动我们来刷新一把看一下页面
[02:50] OK那这回显示数据就真是好多了OK那这样一来我们整个的这个前端其实也构造好那构造好了之后呢其实对前端的代码呢我们可以简单的来看一下其实都不难那我考过了来一个API那就是我们之前写的常规的一种做法那好了接下来呢在这里面的有自己user路由的配置那这些都是一模一样的那当然了跳准到index里面
[03:19] 包装了组件这边的基本的card和table我们之前都聊过如果各位有兴趣的话其实仔细去看一下这里面的代码其实就可以了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 后端使用 Criteria API 实现员工信息的动态分页和条件查询，并在前端 Vue.js 中展示和操作这些数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 IntelliJ IDEA 中 UserService.java 文件，其中包含一个用于构建查询条件的 toPredicate 方法，该方法根据前端传入的参数（如 company_id、departmentId、hasDept）动态生成 Criteria 查询条件，并返回一个 Predicate 数组。同时，下方的控制台显示了 Hibernate 生成的 SQL 语句，用于查询用户信息并进行分页。
画面 2: 展示 HRM 系统的员工列表页面，显示了“员工”模块下的员工信息列表，当前无数据。
画面 3: 展示 HRM 系统的员工列表页面，显示了 9 条员工记录，包括姓名、手机号、工号、聘用形式、部门等信息。
画面 4: 展示 HRM 系统的员工详情页面，显示了员工“123”的个人信息，包括姓名、密码、部门，并有一个“更新”按钮。
画面 5: 展示 HRM 系统的员工列表页面，鼠标悬停在第 3 条记录上，显示了员工“a002”的信息。
画面 6: 展示一个空白的浏览器页面，地址栏显示为 localhost:8080/employees/index。
画面 7: 展示 IntelliJ IDEA 中 UserService.java 文件，显示了 toPredicate 方法的代码，用于根据前端传入的参数构建查询条件。
画面 8: 展示 IntelliJ IDEA 中 UserService.java 文件，显示了 toPredicate 方法的代码，其中注释说明了“根据请求的 hasDept 判断，是否分配到部门”。
画面 9: 展示 IntelliJ IDEA 中 UserService.java 文件，显示了 toPredicate 方法的代码，其中注释说明了“根据请求的 hasDept 判断，是否分配到部门”，并显示了 Hibernate 生成的 SQL 语句。
画面 10: 展示 IntelliJ IDEA 中 UserService.java 文件，显示了 toPredicate 方法的代码，其中注释说明了“根据请求的 hasDept 判断，是否分配到部门”，并显示了控制台日志，记录了 Spring Boot 应用启动时的过滤器映射信息。
画面 11: 展示 HRM 系统的员工列表页面，显示了 6 条员工记录，包括姓名、手机号、工号、聘用形式、部门等信息。
画面 12: 展示 IntelliJ IDEA 中 UserService.java 文件，显示了 toPredicate 方法的代码，其中注释说明了“根据请求的 hasDept 判断，是否分配到部门”，并显示了控制台日志，记录了 Spring Boot 应用启动时的过滤器映射信息。
画面 13: 展示 Visual Studio Code 中的 Vue.js 项目结构，显示了 index.Vue 文件，其中包含一个用于员工列表的组件，数据源为 employeesList。
画面 14: 展示 Visual Studio Code 中的 Vue.js 项目结构，显示了 details.Vue 文件，其中包含一个用于员工详情的组件，数据源为 accountInfo。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
if(StringUtils.isEmpty(map.get("companyId"))) {
    list.add(criteriaBuilder.equal(root.get("companyId").as(String.class), (String)map.get("companyId")));
}
if(StringUtils.isEmpty(map.get("departmentId"))) {
    list.add(criteriaBuilder.equal(root.get("departmentId").as(String.class), (String)map.get("departmentId")));
}
if(StringUtils.isEmpty(map.get("hasDept"))) {
    list.add(criteriaBuilder.isNotNull(root.get("departmentId")));
} else {
    list.add(criteriaBuilder.isNull(root.get("departmentId")));
}
return criteriaBuilder.and(list.toArray(new Predicate[list.size()]));
```
画面 7:
```java
public Page findAll(Map<String, Object> map, int page, int size) {
    // 构建查询条件
    Specification<User> spec = new Specification<User>() {
        @Override
        public Predicate toPredicate(Root<User> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
            List<Predicate> list = new ArrayList<>();
            // 根据请求的 companyId 是否为空设置查询条件
            if(StringUtils.isEmpty(map.get("companyId"))) {
                list.add(criteriaBuilder.equal(root.get("companyId").as(String.class), (String)map.get("companyId")));
            }
            // 根据请求的部门 id 设置查询条件
            if(StringUtils.isEmpty(map.get("departmentId"))) {
                list.add(criteriaBuilder.equal(root.get("departmentId").as(String.class), (String)map.get("departmentId")));
            }
            // 根据请求的 hasDept 判断，是否分配到部门
            if(StringUtils.isEmpty(map.get("hasDept"))) {
                if("0".equals((String)map.get("hasDept"))) {
                    list.add(criteriaBuilder.isNull(root.get("departmentId")));
                } else {
                    list.add(criteriaBuilder.isNotNull(root.get("departmentId")));
                }
            }
            return criteriaBuilder.and(list.toArray(new Predicate[list.size()]));
        }
    };
    return pageUser(userDao.findAll(spec, new Pageable(page - 1, size)));
}
```
画面 8:
```java
// 根据请求的 hasDept 判断，是否分配到部门
if(StringUtils.isEmpty(map.get("hasDept"))) {
    if("0".equals((String)map.get("hasDept"))) {
        list.add(criteriaBuilder.isNull(root.get("departmentId")));
    } else {
        list.add(criteriaBuilder.isNotNull(root.get("departmentId")));
    }
}
```
画面 9:
```java
// 根据请求的 hasDept 判断，是否分配到部门
if(StringUtils.isEmpty(map.get("hasDept"))) {
    if("0".equals((String)map.get("hasDept"))) {
        list.add(criteriaBuilder.isNull(root.get("departmentId")));
    } else {
        list.add(criteriaBuilder.isNotNull(root.get("departmentId")));
    }
}
```
画面 10:
```java
// 根据请求的 hasDept 判断，是否分配到部门
if(StringUtils.isEmpty(map.get("hasDept"))) {
    if("0".equals((String)map.get("hasDept"))) {
        list.add(criteriaBuilder.isNull(root.get("departmentId")));
    } else {
        list.add(criteriaBuilder.isNotNull(root.get("departmentId")));
    }
}
```
画面 12:
```java
// 根据请求的 hasDept 判断，是否分配到部门
if(StringUtils.isEmpty(map.get("hasDept"))) {
    if("0".equals((String)map.get("hasDept"))) {
        list.add(criteriaBuilder.isNull(root.get("departmentId")));
    } else {
        list.add(criteriaBuilder.isNotNull(root.get("departmentId")));
    }
}
```
画面 13:
```javascript
<script>
import constantApi from "@/api/constant/employees"
import {list_remove} from "@/api/base/users"
import PageTool from "@/components/page/page-tool"
import employeesAdd from "@/components/add"
export default {
    name: "employeesList",
    components: {
        PageTool,
        employeesAdd
    },
    data() {
        return {
            employeesAdd: 'employeesAdd',
            dataList: [],
            count: '',
        }
    }
}
</script>
```
画面 14:
```javascript
<script>
import accountInfo from "@/components/details-account-info"
export default {
    name: "employeeDetails",
    components: { accountInfo },
    data() {
        return {
            accountInfo: 'accountInfo',
            activeName: 'first',
            accountId: this.$route.params.id,
            dataList: []
        }
    }
}
</script>
```
画面 1 中的 Hibernate SQL:
```sql
Hibernate: select user_id as id1_0, user_company_id as company_2_0, user_company_name as company_3_0, user0_correction_time as co
```
画面 9 中的 Hibernate SQL:
```sql
Hibernate: insert into bs_user (company_id, company_name, correction_time, create_time, department_id, department_name, enable_state, form
Hibernate: select user_id as id1_0, user_company_id as company_2_0, user_company_name as company_3_0, user0_correction_time as co
```
画面 10 中的 Hibernate SQL:
```sql
Hibernate: select user_id as id1_0, user_company_id as company_2_0, user_company_name as company_3_0, user0_correction_time as co
```
画面 12 中的 Hibernate SQL:
```sql
Hibernate: select user_id as id1_0, user_company_id as company_2_0, user_company_name as company_3_0, user0_correction_time as co
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

