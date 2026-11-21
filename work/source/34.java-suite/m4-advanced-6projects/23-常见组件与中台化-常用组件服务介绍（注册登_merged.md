# 23-常见组件与中台化-常用组件服务介绍（注册登 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们注册登录服务,下面我们可以来看一下它的应用场景,它的应用场景其实前面在功能概述的时候也已经提到过了,它是针对我们互联网用户,在互联网用户当中,我们是不是有用户名密码这种登录或注册的需求,那么可以使用,这是我们第一个应用场景,

包括还有什么呢,手机验证码,它的登录注册,还有电子邮箱的登录注册方式,包括微信的,对吧,微博的,QQ的,这几种方式,这就是我们应用场景,所以说呢,大家如果后期开发的一些项目,对吧,那么有这样的需求,对吧,都是针对互联网用户来提供什么呢,注册登录,

那么这个时候呢,你就不用自己再来开发相应的功能了,直接就可以使用我们这个通用的注册登录服务就可以了,然后呢,我们在这呢,提供了多种这种注册登录的方式,当然我们这个地方呢,需要来说明一下,需要给大家来说明一下,是什么呢,就是我们当前这里边,你看啊,用户名密码这种方式能实现,肯定是没有问题的,还有呢,就是咱们这个手机验证码,

登录,

这种方式,因为这个地方呢,会涉及到什么呢,给你的手机是不是来发送短信,而短信发送这块呢,它其实是收费的服务,所以我们当前这一块呢,是有缺失的,也就是说,大家如果想使用我们这个通用的注册登录服务,那么在发短信这块呢,你需要自己去对接短信,比如说你跟这个阿里云进行对接,或者说使用我们前面可能课程里面讲的这个短信平台,

来进行,

对接,

因为这块呢,是收费的服务啊,所以说这块呢,在我们当前这个注册登录,这个服务里边呢,我们其实是,这个地方只是简单模拟了一下,如果后期大家如果真的要进行发短信,对吧,你直接跟这个短信去对接就可以了,那么我们可以来看一下,你看这是不是有注册,这个是手机号注册,对吧,手机号注册,然后呢,我们这个地方,

注册,来看一下,它应该是发送验证码,发送验证码,这块,看不晓得,你看这个是发送手机验证码,对吧,然后要发送手机验证码的话呢,咱们这个地方呢,可以来看一下,这是验证码是不是已经这个生成了,对吧,我们是随机生成了一个6位的验证码,然后生成完之后啊,这个地方,你看,我是不是调用这个client来send sms,是不是要发送这个验证码,因为发短信呢,它是一个收费的,

服务,那么在我们这个系统里面呢,没有直接跟它去真的对接,那这个地方我们是怎么发出去了,其实就是简单模拟了一下,通过熔断的这种方式,最终呢,我们可以看一下,模拟的话呢,你可以从这个控制台输出,这个地方能够看到,对吧,我们生成这个验证码是什么,也就是说,这块它虽然没有真正发出去,但是呢,这个验证码呢,也已经存出起来了,所以说呢,我们再次登录的时候呢,你就拿了这个验证码,

你刚才那个手机号,还有你这个控制台看到的这个验证码,对吧,便于我们测试啊,然后就可以去登录了,如果这个系统你真的要使用的话呢,你只需要把这个地方改造一下,跟我们真正的那个短信平台去对接,然后呢,把这个验证码真的发到他的手机上就可以了,因为这块呢,是这个收费的服务,然后还有一块是什么呢,还有一块啊,就是比如说我们使用这个微信呢,还有微博呀,还有QQ啊,等等,

这些登录方式,这些呢,我们代码都已经提供好了,但是呢,我们需要说明一下,因为你要调微信的接口,或者微博的接口,或者是QQ的接口,这块呢,需要大家去申请什么呢,在他那个公众平台去申请账号,然后他才允许你什么呢,去调用他的接口,因为我们要拿着用户的QQ号,还有密码是不是去进行验证啊,因为我们的程序并不知道他所输入的这个QQ账号密码是否是正确的,对吧,

所以说呢,我们需要去调QQ官方给我们提供的这个认证的接口,而这个你要调他那个接口的话呢,首先你必须到他的这个开放平台去注册成他的这个用户,然后呢,有了相应的权限,你才能够去调他这个接口,所以这块,这些认证的过程呢,需要大家自己去认证,但是呢,我们这块代码呢,其实是全的,已经为大家都提供好了,这里面都已经提供好了,

所以说呢,多种这个认证方式啊,注册方式等等这些,你看,是不是多种方式,这邮箱的,你看,这是电子邮箱的,包括这个登录的话呢,也是多种方式,对吧,是不是QQ的,还有微博的,微信的,这些都代码,从代码层面来说,其实都已经提供,提供完了,比如说我们这个微信登录,对吧,然后呢,你可以可以进来看一下,然后呢,他会请求这个地址,但这个地址呢,是我们从配置文件里面,其实是动态读取出来的,

然后呢,最终其实调的是什么呢,调的是短信,是这个微信的接口,只不过呢,微信你要想调人家微信接口的话呢,你需要去到微信开放平台,去干什么呢,去申请一个什么呢,APP ID,还有什么呢,微信什么secret,其实你可以认为就是什么呢,就是一个用户名密码,这么一对用户名密码,

好,当然要申请这个的话呢,应该是个人用户是没有权限的,一般是,

是企业用户,然后才有相应的这个资质,然后去申请这些账号,所以还有这个包括这个什么open ID等等这些,所以这块的话,作为我们个人用户的话呢,大家可以自己来看一下这个代码,看看是怎么实现的就可以了,要想演示的话呢,其实并不是很容易,就是因为什么呢,我们要去申请这些东西啊,申请这些资质,比较困难,好,这是我们说明了一下,但是一会儿呢,我们可以使用这种手机验证,

这种方式呢,来测试一下,因为这种方式呢,相对来说呢,是比较好测试的,好,这是咱们先说了一下,它的应用场景,以及呢,对我们来说一些约束条件,

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一节关于“微服务中台”架构下，实现多渠道用户认证与注册功能的技术课程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 Spring Boot 项目中，使用 Redis 缓存、微信 OAuth2.0 接口等技术，实现手机号注册、短信验证码、微信登录、微博登录和 QQ 登录等多种登录/注册场景。课程重点在于展示后端服务的代码实现逻辑，包括控制器（Controller）的接口定义、服务层（Service）的业务处理，以及如何与第三方平台（如微信）进行交互。整个过程旨在为开发者提供一个可复用的、功能完整的用户认证服务模块。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:10**: 视频开场，展示项目结构。讲师在 IntelliJ IDEA 中打开名为 `cust-auth` 的项目，展示了其目录结构，包括 `src/main/java` 下的 `controller`、`service`、`dto` 等包，以及 `pom.xml` 文件，说明这是一个标准的 Spring Boot 项目。
*   **00:10 - 00:30**: 讲解手机号注册功能。讲师聚焦于 `RegController.java` 文件，演示了 `regMobile` 方法的实现。该方法首先获取前端传入的手机号和验证码，然后通过 Redis 检查验证码是否正确，接着检查手机号是否已存在，最后调用 `authService.regMobile` 方法完成注册。
*   **00:30 - 00:50**: 讲解短信验证码发送逻辑。讲师切换到 `CaptchaController.java` 文件，演示了 `sendMobile` 方法。该方法通过 Redis 记录手机号的发送次数，判断是否超过限制（如24小时内只能发送一次），并设置过期时间。
*   **00:50 - 01:10**: 讲解微信登录功能。讲师切换到 `LoginController.java` 文件，演示了 `wbLogin` 和 `wxLogin` 方法。这两个方法分别用于处理微博和微信的登录请求，最终都调用 `authService.login` 方法进行处理。
*   **01:10 - 01:30**: 讲解微信登录的详细实现。讲师聚焦于 `AuthService.java` 文件中的 `loginWx` 方法。该方法首先构造微信 OAuth2.0 的授权请求 URL，发送请求获取 `access_token` 和 `openid`，然后根据 `openid` 查询用户是否存在，如果存在则更新最后登录时间，如果不存在则创建新用户。
*   **01:30 - 01:50**: 讲解用户注册与绑定逻辑。讲师继续在 `AuthService.java` 中演示，如果用户未登录（`authId` 为空），则创建新用户实体并调用 `wxInfoService.lambdaUpdate` 方法将微信的 `access_token` 绑定到用户信息中。
*   **01:50 - 02:10**: 讲解其他登录方式。讲师展示了 `LoginController.java` 中的 `logout` 方法，用于处理用户登出，并演示了 `wxLogin` 和 `wxLogout` 方法的实现。
*   **02:10 - 02:30**: 讲解项目应用场景。讲师切换到 PPT 页面，展示了本项目支持的多种登录/注册方式，包括：用户名密码、手机验证码、邮箱验证码、微信、微博、QQ。并说明了项目的依赖环境，如 MySQL、Redis、Nacos。
*   **02:30 - 02:50**: 讲解项目部署与使用。讲师在 PPT 上展示了如何部署服务，并提供了服务列表和端口信息，说明了如何通过前端调用后端服务。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容**:
    *   **项目依赖环境**: MySQL, Redis, Nacos。
    *   **应用场景**: 用户名密码登录/注册、手机验证码登录/注册、邮箱验证码登录/注册、微信登录/注册、微博登录/注册、QQ登录/注册。
    *   **使用说明**: 部署网关服务和注册登录服务并成功启动。
    *   **服务列表**: `cust-auth` 服务，IP地址为 `16a44c82-7a92-4ff8-a431-239a93498245`。

*   **代码关键内容**:
    *   **`RegController.java` 中的 `regMobile` 方法**:
        ```java
        @PostMapping(value = "mobile")
        public Result regMobile(@Validated(ValidMobile.class) @RequestBody RegDto regDto) {
            String mobile = regDto.getMobile();
            String redisCode = redisUtil.get(RedisKey.getCaptchaMobile(mobile));
            if (!redisCode.equals(regDto.getCode())) {
                return Result.error(ResultCode.BAD_REQUEST, "验证码错误");
            }
            if (authService.existMobile(mobile)) {
                return Result.error(ResultCode.BAD_REQUEST, "手机号已经存在");
            }
            return authService.regMobile(regDto);
        }
        ```
    *   **`CaptchaController.java` 中的 `sendMobile` 方法**:
        ```java
        @PostMapping(value = "send")
        public Result sendMobile(@NotBlank(message = "用户手机号不能为空") String mobile) {
            String count = redisUtil.get(RedisKey.getCaptchaCount(mobile));
            if (StringUtils.isBlank(count)) {
                redisUtil.set(RedisKey.getCaptchaCount(mobile), "1", 60 * 60 * 24);
            } else {
                if (Integer.parseInt(count) >= RedisKey.captchaCount) {
                    return Result.error("24小时内，手机验证码只能发送" + RedisKey.captchaCount + "次");
                }
                long expire = redisUtil.getExpire(RedisKey.getCaptchaExpire(mobile));
                if (expire > RedisKey.captchaInterval) {
                    return Result.error("一分钟内，手机短信验证码只能发送一次");
                }
            }
        }
        ```
    *   **`AuthService.java` 中的 `loginWx` 方法**:
        ```java
        @Transactional
        @Override
        public Result loginWx(LoginDto loginDto, String authId) {
            String atUrl = wxAccessTokenUrl + "?code=" + loginDto.getCode() + "&appid=" + wxAppid + "&secret=" + wxSecret + "&grant_type=authorization_code";
            Map<String, Object> atMap = HttpUtil.sendGet(atUrl);
            Object access_token = atMap.get("access_token");
            Object openid = atMap.get("openid");
            if (access_token == null || openid == null) {
                return Result.error("微信扫码失败");
            }
            Auth auth = lambdaQuery().eq(Auth::getWeixin, openid.toString()).one();
            if (auth != null) {
                baseMapper.updateLastDate(auth.getAuthId());
            } else {
                auth = Auth.builder()
                    .weixin(openid.toString())
                    .weixinBindDate(new Date())
                    .status(1)
                    .createDate(new Date())
                    .lastDate(new Date())
                    .build();
            }
            wxInfoService.lambdaUpdate().eq(Weixin::getOpenid, openid.toString())
                .set(Weixin::getAccessToken, access_token.toString())
                .update();
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与结构展示** (00:00-00:10)
    *   **描述**: 讲师在 IntelliJ IDEA 中打开项目，通过项目导航栏展示了 `src/main/java` 下的 `controller`、`service`、`dto` 等包，以及 `pom.xml` 文件，说明了项目的结构和依赖。

*   **场景二：手机号注册功能演示** (00:10-00:30)
    *   **描述**: 讲师在 `RegController.java` 文件中，通过鼠标高亮和滚动，展示了 `regMobile` 方法的代码。他解释了方法的执行流程：获取手机号和验证码，验证验证码，检查手机号是否存在，最后调用服务层方法完成注册。

*   **场景三：短信验证码发送逻辑演示** (00:30-00:50)
    *   **描述**: 讲师切换到 `CaptchaController.java` 文件，高亮了 `sendMobile` 方法。他解释了该方法如何通过 Redis 记录发送次数，判断是否超过限制，并设置过期时间。

*   **场景四：微信登录功能演示** (00:50-01:10)
    *   **描述**: 讲师在 `LoginController.java` 文件中，展示了 `wbLogin` 和 `wxLogin` 方法。他解释了这两个方法如何接收前端请求，并调用 `authService.login` 方法进行处理。

*   **场景五：微信登录详细实现演示** (01:10-01:30)
    *   **描述**: 讲师聚焦于 `AuthService.java` 文件中的 `loginWx` 方法。他通过高亮和滚动，展示了如何构造微信
