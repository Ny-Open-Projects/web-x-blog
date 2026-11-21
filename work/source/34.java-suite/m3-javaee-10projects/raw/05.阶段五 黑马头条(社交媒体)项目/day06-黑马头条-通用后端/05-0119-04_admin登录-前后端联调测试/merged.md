# 04_admin登录-前后端联调测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\04_admin登录-前后端联调测试【海量资源尽在 666java.com】.mp4
- 时长 5分19秒（音频 319s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好登录的接手后端咱们定义完了然后下面咱们就来去开发前端这个前端的话今天还会再去导入一个新的项目这个项目就是它你可以打开今天的资料今天的资料就是它你把它解压完之后用用外部这么打开我这已经打开了这个结构其实跟咱们之前那个media就是自媒体其实是一样的只是稍微改了改它这个套路或者说里边的代码的结构都一模一样
[00:30] 我就不再去说了好吧然后这个打开之后呢你可以去启动啊可以启动啊启动完之后呢咱们可以来登录一下试一试看看当前这个效果怎么样啊稍等当然你这块啊你这个后台啊你也要启动啊后台我把它关了这时候你可以直接去点一下debug啊debug啊这样的话咱们就是把前后台都启动了启动完之后呢你可以在这啊去用浏览器打开稍等
[01:03] 你看这个界面这个界面是不是跟当前的自媒体是不是类似类似的先看我这启动了没好这一块好像是也启动完了启动完之后你可以去看一下数据库里边有什么数据打开当前的AD user我里边有个数据叫名称叫悟空密码是123所以说咱们在这直接去登录的时候用谁悟空密码是123好
[01:32] 用户名称密码不能为空啊包错了是吧我看看啊嗯包错了咱们在这打在这打个脸啊看看到底哪错好吧点登录来了是吧可以看一下这个好像没有接收到是吧那这样啊嗯少东西是吧先停掉啊在这去加一个什么request about it好吧这个忘了啊我们再启动一下启动完之后呢咱们可以一会再去试一试稍等一下啊刷新一下这个页面
[02:10] 好这个前端工程是没问题的啊看一下启动完了没有好启动完了启动完之后呢你可以在这去写叫悟空密码是123好点通路这个样是不是就通进来了这个界面呢大家应该熟啊这个界面跟咱们那个自媒体是差不多的看到了吗我讲的这些东西呢咱们一会儿会再一说目前的话咱们登录算登录模块算是没有问题的啊当然你也可以去看一下当前这个代码
[02:40] 这个代码的话跟自媒体是一样的我刚才说了是吧所以你打开当前这有个loginlogin里边有个index.view这个呢其实就是登录的页面里边呢你可以去输入用户名和密码它也可以去验证然后呢然后下面的是可以发请求发请求之前呢咱们可以先做一个验证先做验证好你看这个呢其实就是真正的去发请求根据用户名和密码好了看到了吧最终你成功之后呢
[03:10] 比如说你登录成功了这时候它就可以跳到当前的intex路由也就是跳到了当前的主页关于当前这个流程你可以打开这个看看是不是引用了当前用API login可以打开当前的API login是不是这有一个API user author就是去验证用户好啊那这是个poster请求你也可以打开当前这个东西这用途是怎样
[03:40] 大家都知道在当前的constance里边有一个api.js你可以去找到当前的api user author就它看到了吗这个就是login这个其实跟你后台的接口是要完全对应上的没问题吧那这东西我建议大家是不要随便定义比如说我想去分模块比如说我这想加一个admin可以吗可以是可以这就麻烦了会不会麻烦呢
[04:10] 咱们再去登录的时候咱们需要把用户放到当前的现成中你再去打开当前的comment这个comment里边是不是他首先会过一个谁会过当前外包里边有一个叫做admin有一个叫做token的验证过滤这里边其实他去拿到的URL的时候他是看一下当前URI是否是以哪个开头的
[04:41] 你login开头才行如果说你再去写Controller的时候打开如果前面是加了admin的话那这个token可能就过不了如果说他过不了的话他就直接往下走了他就不会去执行其他内容了包括哪些包括你的就是你的用户是吧你的用户有可能不会放到哪不会放到当前的现场装所以说这个你最好是跟老师保持一致就叫login
[05:09] 硬就可以了当然包括咱们上次讲那个自媒体那个也是一样的道理好吧行那当前的登录模块啊咱们就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面9：在 index.Vue 文件中，展示前端登录表单的 submitForm 方法，包含校验逻辑：if(name || password) { this.$message({ message: '用户名和密码不能为空', type: 'warning' }); return; }。
画面10：在 index.Vue 文件中，展示登录成功后的跳转逻辑：if(result.code == 0) { this.$router.replace({path: '/index'}) } else { this.$message({ message: result.error_message, type: 'error' }); }。
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
export const API_WEBSOCKET_AUTH = '/api/v1/WebSocket/admin' //授权验证
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

