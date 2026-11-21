# 画面线理解：04_admin登录-前后端联调测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\04_admin登录-前后端联调测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:39, 00:56, 01:10, 01:35, 01:50, 02:09, 02:16, 02:48, 03:03, 03:46, 04:22, 04:34, 05:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:00:25

1) 这一组画面整体在讲什么（一句话）：
演示一个后台管理系统登录功能的前后端开发实现，包括接口定义、实体类、控制器、服务层、过滤器及前端表单校验等。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，内容为“1.2 登录接口-后端”，包含“1.2.1 接口定义”和“1.2.2 mappser定义”，并列出接口名称 /login/in、请求DTO com.heima.model.admin.pojos.AdUser、响应DTO 返回map(token:xxx, user:{...})。
画面2：展示项目结构，目录为 src/main/java/com/heima/admin，当前选中 views 目录。
画面3：前端项目构建成功，终端显示“Compiled successfully in 17269ms”并提示应用运行在 http://localhost:8080。
画面4：展示后端项目结构，选中 LoginController.java，其中包含 @PostMapping("/in") 方法，调用 userLoginService.login(user)。
画面5：浏览器显示登录页面，提示“用户名和密码不能为空”，输入框内有预设值“wakong”和“...”。
画面6：在 LoginController.java 中，将 @PostMapping("/in") 方法的参数 user 从 AdUser 改为 @RequestBody AdUser。
画面7：浏览器页面空白，表示登录请求未成功或未跳转。
画面8：浏览器显示登录页面，输入框为空。
画面9：在 index.vue 文件中，展示前端登录表单的 submitForm 方法，包含校验逻辑：if(name || password) { this.$message({ message: '用户名和密码不能为空', type: 'warning' }); return; }。
画面10：在 index.vue 文件中，展示登录成功后的跳转逻辑：if(result.code == 0) { this.$router.replace({path: '/index'}) } else { this.$message({ message: result.error_message, type: 'error' }); }。
画面11：在 api.js 文件中，展示 API 常量定义，包括 API_AUTH_PASS、API_AUTH_FAIL 等。
画面12：在项目结构中，选中 heima-leadnews-common 模块，展示其内部结构。
画面13：在 AdminTokenFilter.java 文件中，展示过滤器代码，包含对请求 URL 的判断和响应写入逻辑。
画面14：在 LoginController.java 文件中，展示控制器代码，包含 @RestController、@RequestMapping("/login") 注解和 login 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
spring.application.name=${spring.application.name}
log4j2.xml
(4) 创建包结构com.heima.admin 并在当前包下创建类
(5) 在@com.heima.admin.config中引入配置：jackson, security, mysql
1.2 登录接口-后端
1.2.1 接口定义
参考标准  请参考通用接口规范
接口名称  /login/in
请求DTO  com.heima.model.admin.pojos.AdUser
响应DTO  返回map(token:xxx, user:{...})
1.2.2 mappser定义
(1)admin用户实体类com.heima.model.admin.pojos.AdUser
@Data
public class AdUser {
    private Long id;
    private String name;
    private String password;
}
```
画面4：
```
@Override
@PostMapping("/in")
public ResponseResult login(AdUser user) {
    return userLoginService.login(user);
}
```
画面6：
```
@Override
@PostMapping("/in")
public ResponseResult login(@RequestBody AdUser user) {
    return userLoginService.login(user);
}
```
画面9：
```
methods: {
    async submitForm() {
        let (password , name) = this.ruleForm;
        if(name || password){
            this.$message({
                message: '用户名和密码不能为空',
                type: 'warning'
            });
            return;
        }
```
画面10：
```
methods: {
    async submitForm() {
        let (password , name) = this.ruleForm;
        if(name || password){
            this.$message({
                message: '用户名和密码不能为空',
                type: 'warning'
            });
            return;
        }
        let result = await loginByUsername(name,password)//登录
        if(result.code == 0) {
            this.$router.replace({path: '/index'}) //跳转
        }else{
            this.$message({
                message: result.error_message,
                type: 'error'
            });
        }
    }
}
```
画面11：
```
export const API_MODIFY_IMAGE_CANCEL = '/api/v1/media/material/cancel_collect'
export const API_MODIFY_IMAGE_DELETE = '/api/v1/media/material/del_picture'
export const API_FANS = '/api/v1/user_fans/list' //粉丝列表
export const API_FANS_AVATAR = '/api/v1/user_fans/avatar' //获取粉丝头像
export const API_GET_FANS_FOLLOW_STATE = '/api/v1/user_fans/change_follow_state' //改变粉丝关注状态
export const API_GET_FANS_STATISTIC = '/api/v1/statistics/fans' //粉丝统计
export const API_GET_FANS_STATISTIC_NEWS = '/api/v1/statistics/news' //粉丝新闻统计
export const API_GET_FANS_STATISTIC_PORTAIT = '/api/v1/statistics/portrait' //粉丝头像统计
export const API_WEBSOCKET_AUTH = '/api/v1/websocket/admin' //授权验证
export const API_AUTH_PASS = '/api/v1/admin/auth/list' //授权列表
export const API_AUTH_FAIL = '/api/v1/admin/auth/authfail' //授权失败
export const API_COMMON_UPDATE = '/api/v1/admin/common/update' //通用更新
```
画面13：
```
@Slf4j
@WebFilter(filterName = "adminTokenFilter", urlPatterns = "/*")
public class AdminTokenFilter extends GenericFilterBean {

    Logger logger = LoggerFactory.getLogger(AdminTokenFilter.class);

    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) req;
        HttpServletResponse response = (HttpServletResponse) res;
        String url = request.getRequestURI();
        ResponseResult result = checkToken(request, response);
        if(result != null && result.startsWith("/login")){
            chain.doFilter(req, res);
        }else{
            res.setCharacterEncoding(Contents.CHARSET_NAME);
            res.setContentType("application/json");
            res.getOutputStream().write(JSON.toJSONString(result).getBytes());
        }
    }
}
```
画面14：
```
@RestController
@RequestMapping("/login")
public class LoginController implements LoginControllerApi {

    @Autowired
    private UserLoginService userLoginService;

    @Override
    @PostMapping("/in")
    public ResponseResult login(@RequestBody AdUser user) {
        return userLoginService.login(user);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
