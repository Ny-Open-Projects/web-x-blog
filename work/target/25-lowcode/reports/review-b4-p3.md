# 审稿报告 · 第三期（review-b4-p3）

- 审稿范围：`work/target/25-lowcode/posts/03.第三期/` 全 23 篇（11-1~11-8、12-1~12-6、13-1~13-10）
- 审稿基准：`scan3-code.md`（B 工程架构结论）、`scan6-applied.md`（已修点不重报）、`review-eng-b.md`「博客表述风险清单」
- 对照真源：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课/course-reference/lowcode-platform-full`（server/user、server/wechat-login、server/utils、client/store|hooks|api|pages）
- 视角：低代码/NestJS/React 一线专家 · 技术事实与代码可编译性 / 六段结构与互链 / 去 AI 味
- 说明：本期为「注册登录认证期」，不直接涉及组件注册表/发布事务/问卷组件（第四、五期主题），故风险清单 #3/#4/#10/#11/#17 本期多数不适用，仅 #1/#2/#6 有命中点；scan6 已修的 11-5/11-8/13-5/13-8 接口路径已复核，无残留。

---

## 红线与风险清单核查

- 未出现「RBAC 权限体系」「角色权限模型」等夸大表述。✅
- 未把工程 A（工作流/沙箱/AI）内容说成课程原始功能。✅
- 风险 #1（裸 MD5）：**11-2 命中**，见逐篇。11-7/11-8 写「密码加密」未自称安全可靠，属中性描述，不另报。
- 风险 #2（防刷骨架）：11-3/11-6 描述了 60s 限流+图形码门槛，机制属实；11-6 导语「防刷、可校验、能对账」略过满，已在逐篇给 P2 限定建议。
- 风险 #6（MD5(ip+ua) 反代失真）：本期只介绍机制未吹「完整防重体系」，不强制修；11-6 P2 已带一句限定。
- scan6 已修点复核：11-5 `/user/send_code`（L39/L107）、11-8 `/user/password_login` `/user/phone_login`（L77/L78/L82）、13-5（L66/L110）、13-8（L16/L27/L30/L90）均无旧写法残留。✅

## 互链专项（本期系统性问题）

**S1【P1】11-2 改题后 5 处旧题引用全部断链。**
11-2 现标题为《低代码后端接口开发：加密工具与 Redis 动态模块配置》（文件名仍是 `11-2.低代码项目后端接口开发—加密+Redis_模块配置.md`），但以下 5 处仍引用旧题《低代码项目后端接口开发—加密+Redis 模块配置》：
- `11-1` L117（下一步段）
- `11-3` L15（前置知识）
- `11-4` L16（前置知识）
- `11-5` L15（前置知识）
- `11-6` L15（前置知识）
→ 建议二选一并全量统一：a) 引用侧改为现题《低代码后端接口开发：加密工具与 Redis 动态模块配置》；b) 若想保留课程原题口径，把 11-2 frontmatter title/H1 改回《低代码项目后端接口开发—加密+Redis 模块配置》（与文件名、5 处引用对齐）。倾向 b）——本系列其余篇目的标题均与文件名一致，改回成本最低。

**S2【P2】11-3 / 11-6 的 frontmatter title 与全系列引用差一个标点。**
两篇 title 用全角冒号（`低代码项目后端接口开发：图形验证码接口` / `…：手机验证码接口`），而文件名与全部《》引用均用破折号（`低代码项目后端接口开发—图形验证码接口`，见 11-1 L117、11-4 L15、11-5 L15、11-6 L15、11-7 L15、11-8 前置知识等）。
→ 建议：把这两篇 frontmatter title 的「：」改为「—」，与其余 21 篇「title==文件名主干」的口径统一。

**S3【P2】命令写法：`pnpm build share` 不存在。**
根 package.json 的脚本是 `build:share`（`pnpm --filter share run build`）。12-3 L61、13-5 L97、13-8 L43 三处写作 `` `pnpm build share` ``（少冒号、多了空格）。
→ 建议统一改为 `` `pnpm build:share` ``。

---

## 逐篇结论

### 11-1 获取用户信息装饰器配置 — 需修（轻）

1. 【P2】L66-76 控制器示例，原句：「在 `user.controller.ts` 的请求方法参数里使用这两个装饰器」+ `@Get('info')` 示例 + 「启动项目后用 Apifox 请求该接口」。
   → 建议：加一句「这是本节临时加的验证接口（源码 user.controller 并无 info 路由），仅用于验证装饰器注入」，避免读者在最终工程里找不到该接口。另注：示例用 `String(request.ip).match(...)?.[0] ?? ''`，源码（`GetUserMessTool.ts`）是 `request.ip.match(...)?.join('.')`，行为等价，可不改。
2. 【P2】L105，原句：「后端装饰器、前端类型都放在 `share` 里复用，正是低代码平台把 Schema 与 DSL 集中管理的前提。」
   → 建议：改为「前端请求类型放在 `share` 里复用，后端装饰器在 `server/src/utils` 下」——装饰器实际在 server 端（源码 `packages/server/src/utils/GetUserMessTool.ts`），share 只放类型；且「Schema 与 DSL」是自研参考工程（A）的口径，课程工程（B）share 里集中管理的是**组件物料与请求类型**，建议改为「公共类型与组件物料集中管理的前提」。

其余：结构完整；`createParamDecorator`/`ExecutionContext`/`user-agent` 讲法与源码一致；踩坑叙述（拼写错、pnpm install）自然无 AI 腔；互链 11-2 见 S1。

### 11-2 加密+Redis 模块配置 — 需修

1. 【P1】L23 与 L121（小结），原句：「像用户密码、IP、设备这些属于隐私信息，无论存进 MySQL 还是缓存 Redis，都应该先加密，不能直接明文落库」「用户密码、IP、设备等隐私信息一律加密后再存 MySQL 或 Redis。」
   → 建议：改为「IP、设备经 MD5 摘要后作为 Redis key；密码以 MD5 摘要后落库（**教学实现用裸 MD5、无盐无迭代，生产必须换 bcrypt/argon2**）」。理由：对应风险清单 #1——MD5 是单向哈希不是「加密」，且源码 SecretTool 是无盐裸 MD5；博客如实点破反而是好素材，照抄课程说法而不加限定会被内行读者抓。
2. 【P2】L36-40 代码块类名，原句：「在 `utils` 下新建 `secret.ts`」+ `export class Secret`。
   → 建议：类名/文件名对齐源码 `SecretTool.ts` / `class SecretTool`（本系列 11-3 L43、11-7、11-8 也引用了 `SecretTool` 这个名字，本篇叫 `Secret` 会前后打架）。
3. 【P2】L52-69 Redis 模块示意代码 `useValue: new Redis(options)`。已标注「非项目完整源码」，可保留，但建议补半句「源码里 Provider 提供的是 `new RedisModule(options)` 实例、内部持有 Redis 连接」，避免读者对照源码时困惑。
4. 【P2】L80，原句：「`get(key)`：异步取值，从 Redis 拿到的不是字符串，需要转成字符串」。
   → 建议：改为「ioredis 的 `get` 默认已返回 string，源码里的 `value.toString()` 是防御性写法」——原句技术表述不准。
5. 【P2】L96 `export const RedisConfig`：源码 config.ts 是小写 `redisConfig` 且值来自 env（required 校验），本篇硬编码示例可保留，但建议补一句「最终工程已改为从环境变量读取（`REDIS_HOST/PORT/PASSWORD`，启动缺配置直接报错）」。

其余：forRoot/DynamicModule/global 讲解正确，`set` 追加 `EX`、key 设计（IP+设备 MD5）与源码一致；结构完整；互链 11-1 真实。

### 11-3 图形验证码接口 — 需修

1. 【P1】L60 第 4 步、L70 代码块、L82 联调段，原句：「把 `data`（SVG）与 `text`（四位随机验证码）返回给前端」「return { data: svgCaptcha.data, text: svgCaptcha.text };」「响应 `data` 里是 SVG 字符串、`text` 是四位随机验证码」。
   → 建议：补一个安全口径：最终工程里 `getCaptcha` 仅在非生产环境返回 `text`（源码注释原文「安全:验证码答案仅供开发期自测,生产环境绝不返回」，`NODE_ENV !== 'production'` 分支），课程阶段为联调方便直接返回。至少在 L60 步骤 4 后加「（联调期做法；最终工程生产环境不返回答案，见代码注释）」。理由：把「接口返回验证码答案」写成常规行为而不加限定，等于教读者留一个后门。
2. 【P2】L57，原句：「`await this.captchaTool.captcha()` 异步拿到 SVG 数据与四位随机文本」。
   → 建议：注明「源码方法名是 `captche()`（课程拼写笔误），博客统一写作 `captcha()`」或直接沿用 `captche()`；否则读者照源码对照会找不到方法。

其余：`setGlobalPrefix('api')`、CaptchaDto 单字段 type、冒号分层 key（业务/type/key）、providers 误放 RedisModule 的坑复盘均与源码/架构一致；互链 11-1、9-3（《低代码平台项目后端 Nest 项目配置—接口响应+异常拦截器+DTO》）真实存在。

### 11-4 短信平台接入指引 — 合格

纯流程/选型篇：五步业务链路与 11-6 的 Service 六步口径一致；「官方四步 vs 第三方开店」「APP Secret 定时更新」等说法专业无事实硬伤；表格化但信息密度合理，无 AI 腔；互链 11-3（标题标点见 S2）、11-2（见 S1）真实存在。

### 11-5 短信发送封装实战 — 需修（轻）

1. 【P2】L31/L35/L39/L105，原句：「`form` 是接收短信的手机号，第三方接口要求的属性名就叫 `form`，不要自作主张改名」。
   → 建议：保留课程阶段事实（音频原文即 `form`），但补一句「最终工程封装时该参数改名 `phone`，请求体字段为 `phoneNum`（见 `TextMessageTool.ts`）」，否则与系列后文/参考实现对不上，读者分不清哪个才是 API 真实字段名。
2. 【P2】L75，原句：client package.json `"build": "tsc && vite build"`。
   → 建议：与最终 client `package.json`（`"build": "vite build"`）对齐或注明是本阶段快照；无硬伤，仅防对照困惑。

其余：`@Post('send_code')`、Provider 必须 providers 注册、`code===0` 成功、大小写踩坑复盘均与源码/scan6 一致；「课程口播称装饰器、实为 Provider」这个纠偏是加分项；互链 11-4/11-2/11-3/预先课 Providers 篇均真实（11-2 见 S1）。

### 11-6 手机验证码接口 — 需修（P1 最密集的一篇）

1. 【P1】L48 代码块，原句：`@Post('send-code')`。
   → 建议：改为 `@Post('send_code')`。源码 user.controller 即 `@Post('send_code')`，且本系列 11-5（L107）、13-5（L66）经 scan6 修正后均为 `send_code`，本篇用连字符路径会三处打架。
2. 【P1】L65 第 1 步，原句：「用模板字符串拼出 key（type、code、phone 以下划线连接）」。
   → 建议：改为「key 为 `` `${type}:code:${phone}` ``（冒号分层，同图形验证码）；下划线只出现在 **value** 里：`` `${Date.now()}_${randomCode}` `` 的时间戳与验证码之间」——源码用冒号，split('_') 是对 value 的操作，原句把两件事捏在一起了。
3. 【P1】L70 第 6 步，原句：「失败则删除 Redis 中的图形验证码并抛『发送失败，请重试』」。
   → 建议：改为「失败则删除 Redis 中的**短信验证码**（`${type}:code:${phone}`）并抛『发送失败请重试』」——源码失败分支 `this.redis.del(`${type}:code:${phone}`)`；图形验证码在第 5 步发送前就已删除，原句删错了对象。
4. 【P2】L37 代码块，原句：`randomNickname() { return `编程小白${Math.floor(Math.random() * 90000) + 10000}`; }`。
   → 建议：改为源码事实 `` `编程小白${Math.floor(Math.random() * 10000)}` ``（0~9999 后缀）；90000+10000 是博客自行改写，与源码方法名 `randomName` 也建议一并对齐。
5. 【P2】L52 代码块 `encryptIpAndDevice(/* ... */)`：源码控制器是 `@GetUserIp() ip, @GetUserAgent() agent` + `this.secretTool.getSecret(ip + agent)`，无此函数。建议按源码写法展示，或标注「伪代码」。
6. 【P2】L11 导语「读完你能照着写出一个防刷、可校验、能对账的验证码接口」。对应风险 #2/#6：这套 60s 限流+图形码是防刷骨架，仍有「4 位码 + Math.random、比对失败不失效」等已知缺口。建议补一句限定：「防刷骨架成立；验证码位数/随机源与失败失效策略仍是教学实现，生产需加固」。

其余：六步顺序（限流→存在性→忽略大小写比对→发送→删图存码→结果处理）与源码 sendCode 完全一致；dayjs 装法（`pnpm --filter server add dayjs`）属实（server package.json 有 dayjs ^1.11.10）；联调「时间戳_6294」与源码 value 结构一致；互链 11-7/11-8 真实。

### 11-7 注册接口 — 需修

1. 【P1】L15/L62-81/L127（共 4 处），原句：Redis key `request:code:${phone}` / 「`request:code:phone` 三层 key」。
   → 建议：全部改为 `register:code:${phone}`。源码 register 服务校验的是 `` `register:code:${phone}` ``；课程音频确实口播为「request」，但若照博客实现，前端 sendCode 传 `type=register` 写入 `register:code:*`，注册接口却查 `request:code:*`，永远「请先获取短信验证码」。若想保留课程原话，可加注「课程口播为 request，最终实现统一为 register」。
2. 【P1】L111-113 代码块，原句：`this.jwtService.sign(String(user.id), { expiresIn: '7d' })`。
   → 建议：改为源码写法 `this.jwtService.sign({ id: user.id })`（7 天过期由全局 `jwtConfig.signOptions` 提供，无需传第二参）。理由：JwtStrategy 的 validate 读 `data.id`，签字符串 payload 时 validate 拿到的是裸字符串，`data.id` 为 undefined，后续 `findOne({where:{id:undefined}})` 直接出错——这个写法与工程的校验链不兼容。
3. 【P1】L103-105 代码块，原句：`save({ name, headImage: avatar, phone, password: pwd, openId: '' })`。
   → 建议：改为源码字段名 `save({ username: name, head_img: avatar, phone, password: pwd, open_id: '' })`。User 实体列就是 `username/head_img/open_id`，博客写法按 TS 多余属性检查无法通过编译。
4. 【P2】L92-96，`RandomUtil` / `SecretUtil`：源码类名为 `RandomTool` / `SecretTool`（方法名 `randomName`/`randomAvatar` 本篇写对了）。建议统一为 Tool 系命名，避免与 11-2/11-8 打架。
5. 【P2】L108，原句：「签发一个 7 天过期的 token」——属实（config 默认 `'7d'`），建议补一句「过期时间在 config.ts `signOptions.expiresIn` 全局配置，注册/登录共用」以免与第 2 条的显式传参写法互相矛盾。

其余：查重→验证码→二次密码→随机头像昵称→加密→入库→签发的顺序与源码一致；DTO 4 字段表正确；互链 11-8/11-3/11-6 真实。

### 11-8 登录接口 — 需修

1. 【P1】L23-L37 正文代码块与文字，原句：「账号密码登录路径 `password`，手机验证码登录路径 `form`」+ `@Post('password')`、`@Post('form')`、`formLogin`、`FormLoginDto`。
   → 建议：改为 `@Post('password_login')`、`@Post('phone_login')`，服务名 `phoneLogin`，DTO 名 `PhoneLoginDto`。理由：与本篇自己的联调段/小结（L77/L78/L82，scan6 已修为 password_login/phone_login）直接矛盾——同一篇文章正文说路径是 password/form，联调说 /user/password_login，读者无所适从；源码即前者。
2. 【P2】L71 注，原句：「类型参数必须传 `login`（而不是 `request`）」。
   → 建议：改为「而不是 `register`」——图形/短信验证码的 type 取值就是 register/login 两个（CaptchaDto/前端 useSendCode），request 不是合法取值；此句与 11-7 的 `request:code:` 同源，若 11-7 改为 register，此处应同步。
3. 【P2】L47 `SecretUtil.getSecret(password)`：同 11-7 第 4 条，类名建议对齐 `SecretTool`。

其余：两种登录共用「查用户」、验证码登录 key `login:code:${phone}` 与 split('_')[1] 的讲法与源码一致；互链 12-1 真实。

### 12-1 微信登录方式与公众号开发 — 合格

服务号/订阅号对照表（企业资质、每月 4 条群发、订阅号无登录支付能力）与微信平台规则一致；三种登录形态划分清晰；「课程二次封装参数」表述诚实（不冒充读者有服务号）；结构完整、无 AI 腔；互链 12-2 真实。

### 12-2 微信扫码时序图 — 需修

1. 【P1】L35/L38/L40/L44/L49（全篇 5 处），原句：Redis value `{ isScan: false }` → 改为 `true`、「isScan 布尔变量」。
   → 建议：统一改为源码事实：存入 `{ isScan: 'no' }`，扫码回调后置 `{ isScan: 'yes', token }`，轮询判断 `isScan === 'yes'`。理由：最终代码（wechat-login.service.ts login/wechatMessage/checkScan）全用字符串 'no'/'yes'，布尔写法与本系列 12-5/12-6 的代码块互为矛盾根源；读者照布尔版实现、对照源码读代码会对不上。本篇是设计源头，先在此改，12-4/12-5/12-6 同步。
2. 【P2】L36 第 5 步，原句：「微信服务器收到扫码事件，生成 `ticket` 与 `openId`」。
   → 建议：改为「微信服务器收到扫码事件，推送携带 `ticket`（第 3 步已生成）与用户 `openId` 的回调」——ticket 不是扫码时新生成的。
3. 【P2】L36/L50 `user` 表字段写 `openId`：最终实体/schema 是 `open_id`。建议改为 `open_id`（或注明「最终实现为下划线列名 open_id」）。

其余：时序图四要素、轮询而非 WebSocket、ticket 作为会话 key 的讲法专业；互链 12-1/12-3 真实。

### 12-3 微信服务器接入验证 — 需修（轻）

1. 【P2】L91，原句：「新建 `wechat-login-two.module.ts` 动态模块（`forRoot(config)`）」。
   → 建议：改为「`wechat-login-tool.module.ts`（静态方法 `forRootop(config)`，源码即此拼写）」。scan6 A10-2 在 17-1 已把该模块名统一为 `wechat-login-tool.module.ts`，本篇沿用课程口播的 "two" 会与后文脱节；`forRootop` 的拼写笔误值得顺手点一句，防读者以为博客抄错。
2. 【P2】L61，`pnpm build share` → `pnpm build:share`（见 S3）。

其余：GET callback、CallbackInsertRequest 四参数（share/src/types/request/wechat-login.ts 实存）、token+timestamp+nonce 字典序 SHA1、echostr 原样返回、以及响应拦截器 `msg === '微信验证回调'` 直通的兼容讲法，全部与源码逐字吻合，是本系列技术密度较高的一篇；花生壳内网穿透表述合理。

### 12-4 获取二维码配置封装 — 需修

1. 【P1】L39-42 与 L75-77 自相矛盾，原句：`getAccessToken()` 里 `return (await response.json()).access_token;`，而 `getQrCode()` 里 `const token = (await this.getAccessToken()).access_token;`。
   → 建议：二选一统一：a) 对齐源码——`getAccessToken` 返回整个 json 对象，`getOR/getQrCode` 里再 `.access_token` 取值；b) `getAccessToken` 返回 token 字符串，`getQrCode` 直接 `const token = await this.getAccessToken()`。现写法按前者执行会得到 `undefined.access_token`（字符串上取属性为 undefined）→ 拼出 `access_token=undefined` 的请求。源码是 a) 写法，建议对齐。
2. 【P1】L11/L88-99/L103/L109，`isScan: false`：同 12-2 第 1 条，改为 `{ isScan: 'no' }`（P1 源头在 12-2，此处为代码块落点，改法一致）。
3. 【P2】L60，原句：`action_info: { scene: { scene_id: 1 } }`。
   → 建议：与源码对齐为 `scene_id: 123`（或注明示例值）。

其余：临时二维码 expire_seconds 120 / QR_SCENE / qrUrl?ticket= 拼接、「课程域名换官方 api.weixin.qq.com」的说明均与源码及微信文档一致；互链 12-3/12-5 真实。

### 12-5 扫码回调数据处理 — 需修

1. 【P1】L26-29 代码块，原句：`@Post('message')`。
   → 建议：改为 `@Post('callback')`。源码 wechat-login.controller 的 POST 回调路径即 `callback`（与 GET 接入验证同路径不同方法），本篇还特意写了「接入验证是 GET，回调推送是 POST，路径不同」——按源码其实**同路径**、仅方法不同，这句也要顺手修正。
2. 【P1】L63-70 代码块，原句：`save({ headImage: randomAvatar, name: randomName, openId, phone: '', password: '' })`、`findOne({ where: { openId } })`。
   → 建议：字段对齐实体：`save({ head_img, username, open_id, phone: '', password: '' })`、`findOne({ where: { open_id: lastData.FromUserName } })`（理由同 11-7 第 3 条）。
3. 【P1】L72 代码块，原句：`this.jwtService.sign(String(userId))`。
   → 建议：改为 `this.jwtService.sign({ id: userId })`（理由同 11-7 第 2 条）。
4. 【P1】L85-91 代码块 `{ isScan: true, token }`：同 12-2 第 1 条，源码为 `{ isScan: 'yes', token }`（与 12-4/12-6 的代码块同级，均为可被复制的落点）。
5. 【P2】L36-39，原句：「封装 `WechatDataTo` 工具类…`getChannelStr(data)`：通过流 data/end 事件接收原始 XML」。
   → 建议：类名对齐 `WechatDataTool`、方法名对齐 `getXMLStr`（源码方法即 getXMLStr，读 req 的 data/end 事件）；「课程中转版本 getObject + Object.keys(body)[0]」的讲法可保留，正好呼应 review-eng-b P0-8「正式版本被注释」的现状，建议再补一句「最终实现里正式版本（读原始流）仍处于注释状态」。

其余：FromUserName 即 openId、getLastData 拍平、Event==SCAN/subscribe 的回复文案（欢迎回来/感谢关注+讲师微信）均与源码一致；「Redis 存对象必须 JSON.stringify」正确；互链 12-4/12-6 真实。

### 12-6 轮询接口 — 需修

1. 【P1】L41 代码块，原句：`if (redisData && redisData.isScan === true)`。
   → 建议：改为源码 `if (redisData && redisData.isScan === 'yes')`（同 12-2 根因；布尔版与 12-5 的写入值永远对不上）。
2. 【P2】L44 代码块与 L53-54/L62，原句：`return { data: null, msg: '等待用户扫码' };`「返回『等待用户扫码』」。
   → 建议：注明这是**博客补的兜底分支**：源码 checkScan 在未扫码时**不返回任何内容**（函数无 else，经响应拦截器包成 `{code:0, data:undefined}`），docs/API.md #9 也只写「已扫码返回 token」。保留兜底可以，但要加「源码未扫码时返回空 data，本分支为便于前端判断补充」。

其余：GET check_scan + 单参数 ticket、JSON.parse 还原、120 秒有效期提示均正确；「本项目用轮询而非 WebSocket」与 12-2 呼应；互链 13-1 真实。

### 13-1 前端路由配置 — 需修（轻）

1. 【P2】L41-45 代码块与 L87 小结，原句：子路由 `loginOrRegister`、`edit`，页面 `Edit.tsx`。
   → 建议：补一句「最终工程里路径统一为 `/login_or_register` 与 `/editor`（页面文件 `loginOrRegister.tsx`/`editor.tsx`）」——后文 13-6/13-8 的跳转、以及第四期编辑器篇都落在 `/editor`，本篇只用临时命名会让系列内路径对不上。

其余：createHashRouter/RouterProvider/Outlet、Home 守卫（已登录访问登录页跳编辑页、未登录访问权限页跳登录）与源码 pages/index.tsx 逻辑一致；「isLogin 临时写死、下篇接 MobX」的承接自然；互链 13-2 真实。源码守卫函数名 `befoceRouterChange`（拼写笔误）被本篇规范成 beforePathChange，属正向修正，无需动。

### 13-2 公共状态管理+自定义 hooks — 需修

1. 【P1】L23-L33 代码块与 L84 小结，原句：`makeObservable`。
   → 建议：改为 `makeAutoObservable`。MobX 6 的 `makeObservable` 必须给每个成员显式注解，本例对象无任何 annotation，运行即抛「Missing annotations」；源码 store/auth.ts 用的就是 `makeAutoObservable`。这是本篇唯一会直接让代码跑不起来的硬伤。
2. 【P2】L28/L43/L50/L58，`createStoreAuthor` / `useStoreAuthor` / `store/author.ts` / `hooks/author.ts`：源码为 `createStoreAuth` / `useStoreAuth` / `store/auth.ts`（本系列 13-5/13-6/13-8 也统一写 Author）。建议全系列统一 auth 拼写（一次 grep 批改即可）。
3. 【P2】L58-62 代码块，原句：`const isToken = store.token; const isLogin = computed(() => !!isToken).get();`。
   → 建议：对齐源码 `const isLogin = computed(() => !!storeAuth.token);` 并返回计算属性本身。原写法把 token 捕获成普通常量，computed 闭包不再追踪 store.token，所谓「且是响应式的」（L65）不成立——登录后 token 变化不会引发重算。

其余：「手动加 token 刷新后跳编辑页」的验证步骤成立（整页刷新不受闭包影响）；store/hooks 分模块+index 导出讲法与源码一致；互链 13-1/13-3 真实。

### 13-3 注册组件开发《上》 — 需修（轻）

1. 【P2】L40 代码块，原句：`<Register onChange={changeState} /> : <Login onChange={changeState} />`。
   → 建议：与源码对齐为 prop 名 `changeState`（Register/Login 的接口就是 `{ changeState }`，子组件里 `props.changeState` 调用）。本篇 L63 的小结也写「把 changeState 传给它们」，正文示例却用 onChange，前后不一致。
2. 【P2】L49，原句：`useTitle('小滴课堂低代码平台-注册')`。
   → 建议：对齐源码 `useTitle("小滴低代码平台 - 注册")`（产品名少个「课堂」、连字符与空格不同）。

其余：父组件 useState(true) 先注册后登录、Form.useForm、remember+valuePropName="checked"+validator、htmlType="submit" 的结构与源码 RegisterOption 一致；「5 项」清点符合本篇静态阶段口径（验证码项下篇接入）；互链 13-5 真实。

### 13-5 请求二次封装+注册相关接口 — 需修

1. 【P1】L77-91 代码块，原句：`import { PickType } from '@nestjs/mapped-types';`。
   → 建议：删除该行。share 是前后端共用纯类型包，不依赖 Nest；`@nestjs/mapped-types` 是服务端 DTO 继承用的库，share 的类型文件（源码 share/src/types/request/user.ts）用的就是 TS 内置 `Pick`，没有任何 mapped-types import。保留会误导读者给前端包装后端依赖。
2. 【P1】L93，原句：「`IUser` 字段含 `id`、`phone`、`openId`、`headImage`、`name`、`password`」。
   → 建议：改为源码事实「`id`、`phone`、`open_id`、`head_img`、`username`、`password`」。第四期起 share 的 ILowCode 等实体类型（scan6 A9-3）用的就是下划线列名，本篇的字段名清单与之冲突。顺带一提：最终 share 的 IUser 六个字段类型全是 number（源码自带的类型笔误），如成稿提及字段可只列名字不列类型。
3. 【P1】L34-44 代码块，原句：请求拦截器里 `const { token } = useStoreAuthor();`。
   → 建议：对齐源码写法——直接用 store 实例：`import { storeAuth } from '../hooks/useStoreAuth'; ... if (storeAuth.token) config.headers.Authorization = storeAuth.token;`。`useStoreAuth` 内部调了 `useNavigate`（React hook），在 axios 拦截器这种非组件环境里调用会直接违反 Hook 规则报错；源码正是在拦截器里用 `storeAuth` 单例而非 hook。
4. 【P2】L62/L65/L68 与 L84/L88，`IGetCaptchaRequest`/`ISendCodeRequest`/`IRegisterRequest`/`ICaptcha`：源码 share 里的名字是 `CaptchaRequest`/`SendCodeRequest`/`RegisterRequest`（无 I 前缀）。建议对齐或注明「课程阶段带 I 前缀，最终 share 无前缀」。
5. 【P2】L28-31，`baseURL = 'http://127.0.0.1:3000'` 硬编码：可保留课程阶段写法，但建议补一句「最终工程已抽到 `client/.env` 的 `VITE_API_BASE_URL`（request.ts 读取）」。
6. 【P2】L97，`pnpm build share` → `pnpm build:share`（见 S3）。

其余：响应拦截器「code===0 且 msg 存在才提示」与源码一致；makeRequest 返回 res.data 正确；CORS `app.enableCors()` 与源码 main.ts 一致；互链 13-3/13-6 真实。

### 13-6 注册模块联调 — 需修

1. 【P1】L16/L45-51/L58/L99，原句：`ready: true, // 手动触发`、「`ready`（手动触发）」「短信/注册接口设 `ready: true` 手动触发」。
   → 建议：全部改为 `manual: true`。ahooks 语义：`manual: true` 才是「默认不执行、run 手动触发」；`ready` 是「依赖就绪后才允许发起首次请求」（默认即 true），`ready: true` 等于没设——按本篇写法，sendCode/register 的 useRequest 挂载即自动执行，与文中「点击才触发」的描述相反。源码 execSendCode/execRegister 用的都是 `manual: true`。
2. 【P1】L83-88 代码块，原句：`login: action(async (token: string) => { store.token = token; localStorage.setItem('token', token); })`。
   → 建议：对齐源码 `storeAuth.token = `Bearer ${token}`; localStorage.setItem('token', storeAuth.token);`。服务端 passport-jwt 用 `ExtractJwt.fromAuthHeaderAsBearerToken()` 取 `Authorization` 头并要求 `Bearer ` 前缀；照本篇存裸 token，登录后所有带鉴权接口（如发布）都会 401。
3. 【P2】L67/L90，`nav('/edit')`：对齐最终路径 `/editor`（同 13-1 第 1 条）。

其余：图形验证码 useRequest 默认执行一次、成功后写 captchaSrc、失败/finally 刷新验证码、60 秒倒计时+按钮禁用文案，与源码 useSendCode/RegisterOption 一致；互链 13-5/13-7 真实。

### 13-7 登录组件静态页面 — 需修（轻）

1. 【P2】L28-29 代码块，原句：`<Account onChange={setActiveKey} /> <Captcha onChange={setActiveKey} />`「账号密码登录组件接收 setActiveKey 用于互相切换」。
   → 建议：对齐源码——Login 父组件按 `activeKey` 条件渲染 `{!!activeKey && <Account />}` / `{!activeKey && <Captcha />}`，两个子组件**不接收** setActiveKey、也不负责切换（切换只在父组件顶部文字上）。原句描述了源码里不存在的传参结构。
2. 【P2】L39 代码块，原句：`useSendCode('login')`。
   → 建议：对齐源码签名 `useSendCode(form, 'login')`（第一个参数是 FormInstance，第二个才是 type）；照本篇写法复制会因缺 form 实例报错。

其余：activeKey 1/0 切换、「去注册」经 changeState、type=login 对应 `login:code:phone` key、微信登录占位，均与源码一致；互链 13-8 真实。

### 13-8 登录模块接口联调 — 需修

1. 【P1】L17/L53/L59/L70-74/L92-93，原句：`ready: true`「手动触发/默认不执行」。
   → 建议：同 13-6 第 1 条，全部改 `manual: true`（源码 Account/Captcha 的 useRequest 即 manual: true）。
2. 【P2】L29/L30/L43/L65，`getLoginWithForm` / `ILoginWithFormRequest` / 「`form` 登录」：源码命名是 `getLoginWithPhone` / `LoginWithPhoneRequest`。本篇接口路径已是 `/user/phone_login`（scan6 已修），函数名再用 "form" 前后不一，建议对齐 phone。
3. 【P2】L43，`pnpm build share` → `pnpm build:share`（见 S3）。
4. 【P2】L54/L72 `login(res.data.token)`：承接 13-6 第 2 条，login 内部需含 Bearer 前缀；本篇不单独立项，修 13-6 时同步。

其余：两接口参数类型 `Pick<IUser,...>` 派生、phone_login 无 password/password_login 无 sendCode 的差异讲法与源码一致；「图形验证码填 UXAD、Redis 查 1086」的联调叙述具体可信；互链 13-7/13-9 真实。

### 13-9 微信登录前端页面 — 需修（轻）

1. 【P2】L23/L33/L37 与小结，状态名 `richLogin` / `wechatLogin` / `activeQrCode`。
   → 建议：对齐源码 `wechatLoading`（按钮置灰+弹窗开关共用）、`activeQrcode`（二维码有效期）。三个都是本篇自拟名，读者对照 WechatLogin.tsx 时对不上；至少补一句「源码里按钮置灰与弹窗显隐共用同一个 wechatLoading 状态」——这也解释了源码「点按钮后弹窗即开、按钮同时置灰」的行为。

其余：classnames 置灰、120 秒过期+点击刷新、loading 旋转兜底、预留两处接口位置的讲法与源码结构一致；互链 13-10、12-4/12-6 真实。

### 13-10 微信登录接口联调 — 需修

1. 【P1】L54-60/L70-76 代码块，原句：`useRequest(..., { ready: true, ... })`「ready: true（手动触发）」。
   → 建议：改 `manual: true`（同 13-6 第 1 条；源码 execWechatLogin/execCheckScan 均 manual: true）。
2. 【P2】L59，原句：`debounceWait: 2000, // 每 2 秒轮询一次`。
   → 建议：注释改为「防抖 2 秒：递归调用 execCheckScan 实现轮询，防抖把节奏压到约 2 秒一次」——debounceWait 本身不是定时器，轮询实际靠 onSuccess 里无 data 时再次 run（源码即递归写法）；现注释会让读者以为 debounce 能自动轮询。

其余：未扫码返回空 data（仅 code:0）/扫码返回 token 的响应契约与源码一致；「避免 500 毫秒过快」「120*1000 而非 120 毫秒」两条踩坑具体可信；互链 14-1《低代码项目平台编辑模块后端接口梳理》真实存在（第四期）。

---

## 去 AI 味总体评价

- 23 篇均无「总而言之/值得注意的是/让我们」式套话、无整段加粗堆砌、无排比空转；踩坑叙述（大小写 bug、热更新失效、503 排查、Redis 值肉眼比对）是一线口吻，整体去 AI 味合格。
- 模板感主要集中在「小结 5 条 bullet + 下一步 2 句」的固定形态，属系列既定版式，不算 AI 痕迹，不动。
- 无破折号滥用（每篇 ≤6 处「——」，均为正常破折号用法）。

## 统计

| 维度 | 数量 |
|---|---|
| 总篇数 | 23 |
| 合格 | 2（11-4、12-1） |
| 需修 | 21（其中「需修（轻）」仅 P2 级 7 篇：11-1、11-5、12-3、13-1、13-3、13-7、13-9） |
| P0 | 0 |
| P1 | 26 条（分布：11-2×1、11-3×1、11-6×3、11-7×3、11-8×1、12-2×1、12-4×2、12-5×4、12-6×1、13-2×1、13-5×3、13-6×2、13-8×1、13-10×1，互链 S1×1 系统项） |
| P2 | 39 条（逐篇 37 + 系统项 S2/S3） |

**P1 高频根因（修一处带动多篇）：**
1. 实体/接口字段命名用了博客自拟版（`request:code:`、`name/headImage/openId`、`sign(String(id))`、`FormLoginDto`）→ 全部回源码（11-7/11-8/12-5）。
2. ahooks `ready: true` ≠ 手动触发 → 改 `manual: true`（13-6/13-8/13-10 三篇同一句话）。
3. `isScan` 布尔 vs 源码 `'no'/'yes'` 字符串 → 系列统一字符串（12-2/12-4/12-5/12-6）。
4. 11-2 改题未回改引用 → 5 处断链（S1）。

**建议修复顺序：** 先做 S1/S2/S3 三个系统项（纯查找替换）→ 再清 P1 根因 1-3 → 最后过 13 篇「需修（轻）」的 P2 命名对齐。
