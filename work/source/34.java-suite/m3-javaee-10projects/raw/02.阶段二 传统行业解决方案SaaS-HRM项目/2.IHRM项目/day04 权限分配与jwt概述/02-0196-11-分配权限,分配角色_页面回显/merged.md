# 11-分配权限，分配角色：页面回显

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\11-分配权限，分配角色：页面回显_【海量资源尽在 ubkz.com】.mp4
- 时长 13分24秒（音频 804s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了那刚才呢有留了一个问题就是说这边有一个回显的这么一个问题那回显呢说这个问题之前呢就有必要跟各位来聊一下我分配员工和分配权限它究竟是如何实现的我在这边以一个分配员工为例那么可以找到我的前端界面在我的前端界面这边前端界面这边在员工这个页面里面有一个index.Vue那其中呢我构造了一个分配角色的这么一个组件
[00:31] 分配角色的这么一个组件那这个组件呢叫做add row那我们给它绑定了一个按钮绑定到分配角色这几个字上面handler row好了handler row我们接下来走下去往下去看执行的方法究竟是什么就是handler rowitm那类似点dollar ifc.add row那这个是不是调用我们子组件的内容那调用子组件的内容我们这子组件
[00:58] add row我们来看一下add row究竟是谁component下的add row那就在这儿那调用的是这个add row里面的什么内容呢我们一起简单的来看是不是就是一个叫做to assignperprem这么一个方法那我们找到这个perm方法就在这边那传递过来的时候会传递一个ID的这么一个参数这个ID的参数其实就是我们当前选中行当前选中行的用户ID
[01:29] 那也就意味着进来之后会把用户ID给我传过来那接着我发送了一个Detail那Detail究竟在哪Detail是不是用户下的Detail那其实就是根据ID去查用户所以这个就比较明确了我首先根据ID查用户那查询出用户之后我再去发送一个查询Findout那这个Findout是肉就是查询所有角色的信息列表那接着把它展示到我们的界面上
[01:58] 这个就是我们这个分配角色界面的一个展示过程那在展示的过程当中我们这边用到了一个小小的组件checkbox那这个checkbox当中这个checkbox当中其中有一个v nodal叫做checked rows就是你选中的你选中的这个角色的ID你选中了谁你就勾上谁就可以了好了这边我抱歉我鼠标连电了OK所以这样一来呢就比较明确了这个checked
[02:33] Rose其实就是我们向后台传递的我们选中的角色的这个ID那这个角色ID我们什么时候用就是CreateData那CreateData发送我们的请求传递一个ID属性传递一个RowID属性跟我们的API分配角色一样分配角色ID RowIDS来看ID RowIDS分配角色好了这个就是我们大致的一个过程那接下来呢我想跟各位来聊的就是说我们要想完成它这个回显工作
[03:04] 那回遣工作我们应该如何去做呢其实不难也比较简单我们只需要给这个check的肉丝是不是给他绑定上一个初始值也就是在我们查询的用户之后给这个check的肉丝绑定一下当前你勾选的这个用户已经具备的角色ID集合或者角色ID的这么一个数组才对
[03:30] 所以呢我们就需要对这个代码进行一个完善进行一个改造我们改造的点在哪就是根据ID查询用户给他添加上角色ID的这么一个数组那这个我们改造很简单找到我们的方法找到根据ID查询的这个方法根据ID查询那根据ID查询现在仿佛是一个user对象那我现在要在user对象的基础之上给他进行扩展
[04:01] 添加一个什么呢添加一个新的属性那这个属性我把它叫做肉ids就是用户已经已经具有的角色id数组那好了我们接下来来看一下如何去做其实这个不难很简单那我们现在要返回的数据呢其实已经跟我们的用户对象不太一样了所以我们返回的数据
[04:32] 就创建一个新的我们叫做直对象放到 respond 当中然后这边呢我们就可以构造一个新的直对象user拿过来右键创建一个 class好了我把它叫做user resultuser resultok 那这个 user result 呢我们需要去实现implements因为要进行数据的一个传输implements 我们叫做 series
[05:07] 好了接下来里面的这些数据都有什么注意和我们的用户一模一样因为我们只是在用户数据的基础之上填充了一个角色的IDS的这么一个数据OK接着里面添加一个数组private比如说我就叫做list死郡类型的我们叫什么来着roidsroids
[05:36] 那接着我写一个public构造方法我个人习惯指对象里面的内容全部都以构造方法传递过来传递给user因为是根据user来进行获取好了这边引一下包那这个代码怎么去实现它呢其实很简单也不难首先binpropertybinproperty.copyproperty那copyproperty主要目的就是说因为我这个指对象和我们用户对象里面大部分的属性都是一模一样的我直接call过来那就比较简单一些
[06:11] 注意它的两个参数第一个参数是你从哪拿数据第二个是你call到哪user是我们查询出来的user对象那根据user对象去拼接出我们的值对象类似就是当前值对象那好了剩下不一样的是不是有一个rowids那rowids如何构造其实很简单那我们可以进行一个iter for循环那么循环的就是user.get rows
[06:38] 那这个ros里面有所有的角色的集合它是它有什么角色它都有所以我们只需要等于new一个array list好了我们只需要rowids打点一个一个的添加过来它的rowid就可以了OK那这样一来那这样一来类似点那这样一来我们这个方法其实就已经写好了这我们的直对象写好了那接着我们user Controller这边呢就不用user了我们可以通过
[07:13] user result等于new一个user result帮着查询的user对象传递过来接着返回即可好了那接下来呢我们可以重新启动一下当前这个服务让它慢慢启动我们打开页面一起静静的去看效果就可以了刷新一把还没有启动成功啊刷新一把好了已经启动成功了我们来看一下张三有没有数据走好了这边呢后台是报了一个错误啊我们来看一下
[07:51] 大致的应该知道了是因为我这边应该少了getter和setter两个方法好了我们把它补充上因为不写的话它就会找不到getset吧好了这边呢再去启动那我们再来看一下刷新一下数据还没启动成功刷新一把好了已经有了内容我们分配角色看一下效果好了先给它分配角色看一下效果这边人事经理勾选上提交好了成功我再查看诶给我来看现在呢已经回显了
[08:25] 那比如说呢再分配一个薪资好了提交再查看OK也已经搞定了那我们员工这个已经搞定了那同理呢我们这边权限进行设置就我们这边角色分配权限呢其中也有这个问题那我们快速的给他搞定出来就可以了好了跟这边的逻辑是一样的全部围绕在角色查询根据ID查询这边好了跟这边逻辑一样我就快速的给他搞定就可以了Ctrl C Ctrl V 靠一个过来
[09:00] 那里面的数据跟我们这个角色是一样OK全部都是一样的好了接着呢里面包含一个permidspermids那好了这边呢开始我们传递的是一个肉传递的是一个肉好了这边呢就根据肉进行拷贝肉进行拷贝拷贝好了之后我们可以通过肉打点getperms进行循环
[09:43] P2MOK那我们这回呢就是ids.getget idOK那这样一来我们这个也构造好了那构造好了之后我们找到根据id查询的这个Controller角色根据id查询的Controller根据id查询根据fund by id好了那跟刚才一样new一个row resultrow result
[10:23] 等于new一个row result把我们的角色补充进来好了这边row result进行返回构建就可以好了那我们这边刷新一下我们重启一下我们的服务ok找到我们的页面部分公司设置刷新ok数据已经显示过来了那我们分配权限看一下那就目前来说分配权限这个页面呢还没有进行改造那我们找到分配权限这个界面
[10:59] setting里面row list它是通过分配权限这个里面来做的为谁谁谁分配权限那为谁谁分配权限这里面呢是一颗竖形结构竖形结构那它默认勾选的是通过一个叫做checked nodes来做的那这个checked nodes呢我们也需要对它进行一个简单的改造其实就可以了好了我们找到需要改造的这个代码稍微有点多啊各位咱们耐心的一起来找一下就可以了
[11:33] 那通过英代斯页面找到我们的roll list那在roll list当中其中有一个分配权限的这么一个按钮分配权限分配按钮找到往下找找过来那这边呢是根据ID去查角色那根据ID去查角色找到了之后注意找到了之后那我在这边呢就开始进行一个构造进行一个构造
[12:03] 好了这个构造呢其实比较简单我们直接就可以通过把这边删掉没用了类似点checked nodes等于res.data.data.data点注意我们可以在页面刷新一把打开F12看一下发送的请求我们得到的数据究竟是什么那发送了一条请求注意发送了一个请求这边全线来各位来看其中呢就有这么一个
[12:40] 抱歉是上面这个啊其中就有这么一个字段叫做什么呢Promission IDS它是一个数组所以我们关注的是返回属性res.data那其中的我们的data部分就是所以再点data那接着我们的Promission IDS给它复制到checked node在默认勾选的这个框框属性上面就可以了好了那接下来呢这个我们代码写的差不多了我们可以验证一下看一下首先呢人事经理哎他已经有了我这边再勾俩确定好了各位来看
[13:11] 也已经有了那接着再去查看一个这个是不是也都已经勾选了并且是不一样的OK那这样一来我们其实就已经完成了整个角色分配和我们权限分配的这个工作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 HRM 系统中为员工分配角色权限，涉及前端 Vue 代码、后端 Java 代码及数据库模型设计。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 HRM 系统的“员工”页面，弹出“分配角色”对话框，用户正在为员工“zhangsan1”选择角色，鼠标悬停在“确定”按钮上。
画面 2: HRM 系统“员工”列表页，显示员工信息，包括姓名、手机号、工号、转正时间、部门等字段。
画面 3: Visual Studio Code 编辑器中打开 `addRole.Vue` 文件，展示前端 Vue 代码，其中包含 `toAssignPrem(id)` 方法，用于处理分配权限的逻辑。
画面 4: 多窗口分屏画面，展示 HRM 系统前端、后端代码（IntelliJ IDEA）、数据库设计工具（PowerDesigner、SQLyog）等开发环境。
画面 5: IntelliJ IDEA 中打开 `UserResult.java` 文件，展示后端 Java 类定义，包含 `private String workingCity;` 等字段。
画面 6: IntelliJ IDEA 中 `UserResult.java` 文件，展示 `UserResult(UserUser)` 构造函数，其中包含 `BeanUtils.copyProperties(user, target_this);` 代码。
画面 7: IntelliJ IDEA 中 `UserResult.java` 文件，展示构造函数内部的 `for (Role role : user.getRoles()) { this.roleIds.add(role.getId()); }` 代码。
画面 8: IntelliJ IDEA 中 `UserResult.java` 文件，展示类的顶部导入语句和 `@RequestMapping` 注解。
画面 9: HRM 系统“分配角色”对话框，用户已勾选“人事经理”、“系统管理员”、“人事专员”角色，鼠标悬停在“确定”按钮上。
画面 10: IntelliJ IDEA 中打开 `RoleResult.java` 文件，展示后端 Java 类定义，包含 `private List<String> p;` 字段。
画面 11: IntelliJ IDEA 中打开 `RoleController.java` 文件，展示控制器类，包含 `@RequestMapping(value = "/role/{id}", method = RequestMethod.GET)` 和 `@RequestMapping(value = "/role/list", method = RequestMethod.GET)` 注解。
画面 12: Visual Studio Code 编辑器中打开 `role-list.Vue` 文件，展示前端 Vue 代码，包含 `import {list, add, update, remove, detail, assignPrem} from '@/api/base/role';` 导入语句。
画面 13: 浏览器开发者工具的“Network”标签页，显示正在记录网络活动。
画面 14: HRM 系统“角色管理”页面，弹出“为【新资专员】分配权限”对话框，列出多个权限选项，鼠标悬停在“取消”按钮上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```Vue
<div slot="footer" class="dialog footer">
  <el-button type="primary" @click="createData">提交</el-button>
  <el-button @click="roleFormVisible=false">取消</el-button>
</div>
```
```javascript
import {findUser} from "@/api/base/users";
import {assignRole, detail} from "@/api/base/users";
export default {
  data () {
    return {
      roleFormVisible: false,
      formBase: {},
      checkedRoles: [],
      rules: []
    };
  },
  methods: {
    toAssignPrem(id) {
      detail({id: id}).then(res => {
        this.checkedRoles = res.data.data.roleIds;
      });
    }
  }
};
```
画面 5:
```java
package com.ihrm.domain.system.response;

public class UserResult implements Serializable {
```
画面 6:
```java
private String workingCity;
private Date correctionTime;
private Integer inServiceStatus;
private String departmentName;
private List<String> roleIds;
```
画面 7:
```java
public UserResult(User user) {
  BeanUtils.copyProperties(user, target_this);
  for (Role role : user.getRoles()) {
    this.roleIds.add(role.getId());
  }
}
```
画面 8:
```java
package com.ihrm.domain.system.response;
import com.ihrm.domain.system.Role;
import com.ihrm.domain.system.User;
import org.springframework.beans.BeanUtils;
import javax.persistence.Id;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
```
画面 10:
```java
private List<String> p;
```
画面 11:
```java
@RequestMapping(value = "/role/{id}", method = RequestMethod.GET)
public Result findRoleById(@PathVariable(name = "id") String id) throws Exception {
  Role role = roleService.findById(id);
  RoleResult roleResult = new RoleResult(role);
  return new Result(ResultCode.SUCCESS, roleResult);
}

@RequestMapping(value = "/role", method = RequestMethod.GET)
public Result findRole(@RequestParam(name = "company_id") String companyId, Pageable pageable) throws Exception {
  Page<Role> pr = new PageResult<>(roleService.findByPage(companyId, pageable));
  return new Result(ResultCode.SUCCESS, pr);
}

@RequestMapping(value = "/role/list", method = RequestMethod.GET)
public Result findAll() throws Exception {
  List<Role> roleList = roleService.findAll(companyId);
  return new Result(ResultCode.SUCCESS, roleList);
}
```
画面 12:
```Vue
<el-tree
  :data="roleList"
  :props="defaultCheckedKeys"
  show-checkbox
  node-key="id"
  ref="tree"
  :default-checked-keys="checkedNodes"
  :default-expand-all="true"
  :expand-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :check-strictly="false"
  :check-on-click-node="false"
  :

