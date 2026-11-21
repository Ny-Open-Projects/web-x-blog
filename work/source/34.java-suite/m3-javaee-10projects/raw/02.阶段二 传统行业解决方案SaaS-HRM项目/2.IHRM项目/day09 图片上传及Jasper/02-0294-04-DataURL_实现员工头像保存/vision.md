# 画面线理解：04-DataURL：实现员工头像保存

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\04-DataURL：实现员工头像保存_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 02:45, 03:37, 04:25, 05:18, 06:04, 07:35, 09:45, 12:09, 13:35, 14:40, 15:23, 16:02, 16:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:24:07

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事管理系统中，通过 Data URL 方式实现用户头像上传，并展示前后端代码实现过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程目录，当前选中“1.3 Data URL实现用户头像上传”，说明本节内容。
画面 2: 在 IntelliJ IDEA 中查看 User.java 类，展示用户实体类中包含的字段，如 username、mobile、deptId 等。
画面 3: 在浏览器地址栏中输入 localhost:8080，准备访问系统。
画面 4: 在文件资源管理器中，展示项目目录结构，选中 components 文件夹下的 imgUpload.vue 文件。
画面 5: 在 IntelliJ IDEA 中，右键点击 User.java 文件，弹出菜单，准备进行操作。
画面 6: 在浏览器中打开 iHRM 系统的员工详情页，显示“请上传图片”提示。
画面 7: 在 IntelliJ IDEA 中，查看 UserController.java 文件，展示 @RequestMapping("/user/upload/{id}") 方法。
画面 8: 在 IntelliJ IDEA 中，为 UserController.java 文件添加 import 导入语句，准备使用 HttpServletResponse。
画面 9: 在 IntelliJ IDEA 中，查看 UserService.java 文件，展示 uploadImage 方法的实现，其中包含 userDao.findById(id).get()。
画面 10: 在 IntelliJ IDEA 中，展示多个窗口的分屏视图，包括项目结构、代码编辑器、数据库工具等。
画面 11: 在 IntelliJ IDEA 中，查看 UserController.java 文件，展示 upload 方法的实现，其中调用 userService.uploadImage。
画面 12: 在浏览器的开发者工具中，查看上传图片的响应，显示图片数据已成功返回。
画面 13: 在 IntelliJ IDEA 中，查看 UserService.java 文件，展示 uploadImage 方法的实现，其中包含 Hibernate SQL 语句。
画面 14: 在浏览器中，显示员工详情页，用户头像已成功上传并显示。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
private Integer inServiceStatus;
private String departmentName;
//level
String
saasAdmin, saas管理员所有权限
coadmin, 企业管理员（建建客户企业的时候添加）
user, 普通用户（需要添加）
private String level;
public User(Object [] values) {
//用户状态 1.在职 2.离职
this.username = values[1].toString();
this.mobile = values[2].toString();
this.workNumber = new DecimalFormat(pattern="#").format(values[3]);
this.timeEntry = (Date) values[6]; //部门编码
this.departmentId = values[6].toString(); //部门编码
}
```

画面 7:
```java
@RequestMapping(value="/sys")
public class UserController extends BaseController {
@Autowired
private UserService userService;
@Autowired
private PermissionService permissionService;
@Autowired
private JwtUtils jwtUtils;
@Autowired
private DepartmentFeignClient departmentFeignClient;
@RequestMapping("/user/upload/{id}")
public Result upload(@PathVariable String id, @RequestParam(name="file") {
}
```

画面 8:
```java
import org.springframework.http.HttpServletResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.commons.CommonsMultipartResolver;
import org.springframework.web.servlet.mvc.method.annotation.MvcUriComponentsBuilder;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
