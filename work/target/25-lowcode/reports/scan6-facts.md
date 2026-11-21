# 扫描6：跨篇口径 + 技术事实核实

- 数据源：`work/target/25-lowcode/posts`（229 篇，真源；`work/source/.../blog` 为同步拷贝，两份需同步改）
- 代码基准：`course-reference/lowcode-platform-full`（课程 B 工程，scan3 已核实）+ `lowcode-platform`（A 工程）
- 结论概览：正文整体与代码吻合度高。scan3 判「有出入」的点里，渲染引擎/沙箱/AI 节点在 229 篇中**未被提及**（无需处理）；RBAC 出现 1 处需改；Redis 相关正文与 B 工程实况相符但 30-6 有 5 处细节需修；另发现一批 API 路径/函数名/字段名硬伤共 10 组。

---

## 一、篇级修正清单（可逐条执行）

格式：文件 → 原句（行号）→ 应改为。行号为 target/25-lowcode/posts 下文件当前行号。

### A1. RBAC 夸大（scan3 出入点）

**文件**：`00.预先课 - 低代码大课必备技术/第_2_集__后端接口开发—课程的创建接口开发.md`
- L46 原句：「把鉴权做成可复用的守卫/装饰器，而不是在每个方法里复制一遍校验代码，后面低代码平台的登录态、RBAC 权限体系都是在这个基础上长出来的。」
- 应改为：「……后面低代码平台的登录态、接口权限守卫都是在这个基础上长出来的。」
- 依据：scan3 §6——A/B 两工程均无 RBAC 角色模型（B 无 role 字段，仅 JWT 登录 + account_id 数据归属；A 仅 tenantId 头部预留）。全库 grep 确认「RBAC」仅此一处。

### A2. Redis 缓存篇细节（30-6，5 处）

**文件**：`08.第八期/30-6.Jmeter_压测接口—优化获取低代码组件接口性能.md`

依据（`packages/server/src/utils/modules/redis.module.ts`、`low-code.service.ts`）：
1. 方法实名是 **`getCachedData`**（不是 getCacheData）；
2. `force` 的实现是「置空本地 data 后回源重查并覆盖写回」，**并不先 `del(key)`**（A del 后立即 set，效果等价，但伪代码不应出现 del 步骤）；
3. `set` 签名是 `set(key, value, 'EX', time)`，存的是 `JSON.stringify(data)`；
4. `getReleaseData` 缓存版实参为 `{ ttl: 60 * 10, force: !!user.id }`（TTL 600 秒；带登录态的 `release_with_user` 调用强制刷新）；
5. **最终仓库里缓存版 `getReleaseData` 整体被注释掉**（L122-157），controller 实际走无缓存版本——缓存是课堂演示态。

具体修改：
- L11 导语：「缓存封装 `getCacheData` 的三个参数」→「缓存封装 `getCachedData` 的三个参数」；同句末尾建议补一句：「注意：该缓存版本在最终仓库源码中处于注释状态，课堂演示后未合入主线，线上接口仍走无缓存版。」
- L37-43 代码块：`this.redis.getCacheData(` → `this.redis.getCachedData(`；`{ ttl: 60, force: false }` → `{ ttl: 60 * 10, force: false }`。
- L57-68 伪代码块：方法名改 `getCachedData`；删除 `await this.del(key);` 一行（force 分支只保留 `data = null`）；`await this.set(key, data, options.ttl)` → `await this.set(key, JSON.stringify(data), 'EX', options.ttl)`。
- L119 小结：同 L11/L37 同步改名；`{ ttl, force }` 描述里补「课程示例 TTL 为 600 秒；force 置空后回源覆盖写回，并非显式 del」。
- L89 「其它接口照样可以调用」段：补一句限定「以最终仓库为准，该缓存入口当前仅以注释形式保留在 `low-code.service.ts` 中」。

### A3. dnd-kit 传感器名与激活约束语义（18-4，2 处）

**文件**：`05.第五期/18-4.低代码项目平台编辑模块—页面组件拖拽排序功能开发.md`
- L11 导语：「PointerSensor 与 closestCenter 的配置」→「MouseSensor 与 closestCenter 的配置」。依据：`packages/client/src/components/DragSortable/SortableContainer.tsx` 用的是 `useSensor(MouseSensor, { activationConstraint: { distance: 2 } })`。
- L41 原句：「设置激活约束为移动 2 像素才触发一次监听（官方示例常用 10 像素，这里调小更灵敏）。每移动 2 像素就重新判断一次是否该换位置。」
- 应改为：「设置激活约束 `distance: 2`，即按下后移动 2 像素才真正激活拖拽（官方示例常用 8~10 像素，这里调小更灵敏）——它是区分『点击』与『拖拽』的阈值，不是每 2 像素周期性重判。」
- 依据：dnd-kit 官方文档 activation constraint 的 distance 语义是「激活拖拽前需移动的距离」，非周期采样（见文末来源）。

### A4. mobx-shallow-undo API 名（18-5，1 处）

**文件**：`05.第五期/18-5.低代码项目平台编辑模块—页面组件键盘操作功能开发.md`
- L75 附近原句：「实现借助 `mobx-shallow-undo` 的 `triggerUndo`」
- 应改为：「实现借助 `mobx-shallow-undo` 的 `trackUndo`」。依据：`packages/client/src/hooks/useStoreComponents.ts` L7 `import { trackUndo } from "mobx-shallow-undo"`，配套 `undo()/redo()/hasUndo/hasRedo`。全库仅此一处提 triggerUndo，其余 10 处只提包名，无需动。

### A5. C 端渲染字段映射（20-6，2 处）

**文件**：`05.第五期/20-6.低代码项目发布页面—获取页面渲染.md`
- L41 及 L51：`getQuestionComponentValueFeed` → **`getQuestionComponentValueField`**。依据：`packages/release/src/components/ComponentRender.tsx` L30。
- L51：「checkbox → `defaultCheckbox`」→「checkbox → **`defaultChecked`**」。依据：ComponentRender.tsx L36-41，switch 返回 `text` / `defaultRadio` / `defaultChecked`。

### A6. 登录接口路径（11-8、13-8，共 6 处）

依据：`packages/server/src/user/user.controller.ts` 路由为 `@Post('password_login')`、`@Post('phone_login')`（全局前缀 /api）。第八期 28-9/30-1 已正确写 `/api/user/password_login`，第三期写法与之矛盾。

**文件**：`03.第三期/11-8.低代码项目后端接口开发—登录接口.md`
- L77：「POST `/user/password`」→「POST `/user/password_login`」（或 `/api/user/password_login`）
- L78：「POST `/user/form`」→「POST `/user/phone_login`」
- L82：「账号密码（`/user/password`）与手机验证码（`/user/form`）」→「账号密码（`/user/password_login`）与手机验证码（`/user/phone_login`）」

**文件**：`03.第三期/13-8.低代码项目前端项目开发—登录模块接口联调.md`
- L16：「后端已有 `/user/password` 与 `/user/form` 接口」→「`/user/password_login` 与 `/user/phone_login`」
- L27：`makeRequest('/user/password', ...)` → `makeRequest('/user/password_login', ...)`
- L30：`makeRequest('/user/form', ...)` → `makeRequest('/user/phone_login', ...)`
- L90：「新增 `/user/password`（phone+password）与 `/user/form`（phone+sendCode）两接口」→「新增 `/user/password_login`（phone+password）与 `/user/phone_login`（phone+sendCode）两接口」

### A7. 短信验证码接口路径（11-5、13-5，共 3 处）

依据：user.controller.ts 为 `@Post('send_code')`。
- `03.第三期/11-5.第三方短信验证码发送装饰器封装实战.md` L39：「路径如 `/user/sendCode`」→「路径如 `/user/send_code`」（此处带「如」字，属示例口吻，但既然最终路由确定，直接写准）。
- `03.第三期/13-5.低代码项目前端项目开发—请求二次封装+注册相关接口.md` L66：`makeRequest('/user/sendCode', ...)` → `makeRequest('/user/send_code', ...)`。
- 同文件 L110：「短信验证码 `/user/sendCode`」→「短信验证码 `/user/send_code`」。

### A8. low_code 控制器路径（19-5、20-2、20-6，共 6 处）

依据：`low-code.controller.ts` `@Controller('low_code')` + main.ts `setGlobalPrefix('api')`；最终路由为 `/api/low_code/release_with_user`、`/api/low_code/release?id=`。正文写的 `/local/...` 是课堂早期命名，与最终代码不符（也是跨期不一致，见二-3）。

- `05.第五期/19-5.低代码项目平台编辑模块—页面组件服务端获取开发.md`
  - L17：「路径为 `GET /local/releaseWithUser`」→「路径为 `GET /low_code/release_with_user`（带全局前缀即 `/api/low_code/release_with_user`）」
  - L36：注释 `// GET /local/releaseWithUser` → `// GET /api/low_code/release_with_user`
  - L70：「调用 `GET /local/releaseWithUser`」→「调用 `GET /api/low_code/release_with_user`」
- `05.第五期/20-2.低代码项目发布页面—后端接口低代码组件获取.md`
  - L23：「编辑平台获取组件走 `GET /local/releaseWithUser`」→「`GET /api/low_code/release_with_user`」
  - L39：「在 Apifox 中用 `GET /local/release?` 」→「`GET /api/low_code/release?`」
- `05.第五期/20-6.低代码项目发布页面—获取页面渲染.md`
  - L30：`fetch('http://127.0.0.1:3006/api/local/release?id=' + id, ...)` → `fetch('http://127.0.0.1:3006/api/low_code/release?id=' + id, ...)`
  - L58：「`fetch` 请求 `GET /api/local/release?id=`」→「`GET /api/low_code/release?id=`」

### A9. 三张实体表字段（14-2，4 处）

**文件**：`04.第四期/14-2.后端接口开发—低代码项目编辑模块发布接口《上》.md`
依据：`packages/server/src/low-code/entities/low-code.entity.ts`。
- L38（组件表）：「字段包括组件类型（……）、所属配置 ID、所属页面 ID、所属用户 ID，以及 `options`」→「字段包括组件 `type`（默认值 `titleText` 文本标题类型）、`page_id`、`account_id`，以及 `options`」——**实体没有「配置 ID」字段**，删掉。
- L40（组件数据表）：「字段关联到哪个页面、哪个组件、哪个用户，以及 `purpose`——一个数组，每项为对象，记录对应组件的 id 与用户填写的 value」→「字段为 `page_id`、`user`（不关联登录用户，而是对访客的匿名标识：`MD5(ip + ua)`）、`props`——一个 simple-json 数组，每项为 `{ id, value }`，记录对应组件 id 与用户填写的 value」。**字段名 purpose 不存在，实名 props；`user` 不是登录用户**。
- L44 附近：「在 `share/src/lowcode.ts` 中定义三个接口：`ILowcode`（页面表）」→「在 `share/src/types/entity/low-code.ts` 中定义三个接口：`ILowCode`（页面表）」——路径与大小写（`ILowCode` 非 `ILowcode`）均以源码为准。

### A10. OSS 模块位置与并列模块名（17-1，2 处）

**文件**：`05.第五期/17-1.低代码项目平台编辑模块—阿里云_OSS_资源上传配置.md`
依据：实际文件在 `packages/server/src/utils/modules/ali-oss.module.ts`；`src/utils/modules/` 下另有 `redis.module.ts`、`wechat-login-tool.module.ts`；**不存在 `release.module.ts`**（发布逻辑在 `src/low-code/`）。
- L27：「在 server 子项目的 `src/modules` 下」→「在 server 子项目的 `src/utils/modules` 下」。
- L27 同段：「此前的 `release.module.ts`、`wechat-login` 模块都维护在这里」→「此前的 `redis.module.ts`、`wechat-login-tool.module.ts` 等公共模块都维护在这里」。

---

## 二、跨篇口径一致性

1. **登录方式口径：一致，无需改。** 第三期口径统一为「密码 + 手机验证码两种（11-8/13-7 activeKey 双 tab）+ 微信扫码独立成模块」，与代码三接口（password_login/phone_login/wechat_login）相符。
2. **验证码防刷口径：一致，无需改。** 11-3/11-6/13-6/2-4 均为「图形验证码 svg-captcha + Redis 60s + key=MD5(ip+ua) 冒号分层（`${type}:captcha:${key}`）+ 短信码 60s 防重（dayjs diff）」，与 user.service.ts L29-74 完全一致。
3. **low_code 接口路径口径：跨期不一致。** 第三/四/五期正文用 `/local/...`、`/user/password`、`/user/form`、`/user/sendCode`；第六/八期（21-x、28-9、30-x）用 `/low_code/...`、`/api/user/password_login`。最终代码属后者。按一节 A6/A7/A8 逐条修正后即拉平。
4. **组件注册表/store 命名：跨篇一致但与源码不同名（低优先级，二选一）。** 正文 22 处写 `sortableComponentConfig`、14 处 `componentConfigs`、16 处 `currentComponentConfig`；源码实名 `compConfigs` / `sortableCompConfig` / `currentCompConfig`（`store/components.ts` L5-8，另有源码拼写错误 `copyedCompConig`）。正文内部自洽、语义无误，课程讲解口径也可能是这套名字。建议：在 19-5（首次系统介绍 store 结构的篇）加一句「源码变量名为 `compConfigs` / `sortableCompConfig` / `currentCompConfig`，本文行文用语义化写法」即可；不必全局替换 52 处。
5. **schema/存储口径：一致。** 14-2（simple-array components / simple-json options）、14-3（QueryRunner 事务发布）、14-5（components+componentIds 双返回）、19-2（storeTime/releaseTime 草稿发布对比）相互咬合，与 low-code.entity.ts / low-code.service.ts 一致。仅 A9 列出的字段级错误需修。
6. **发布流程口径：一致。** 「存在则更新、不存在则创建 + 事务」在 14-2/14-3/19-4 三处说法统一；14-3 L138「本版为未优化方案，留待 JMeter 压测后优化」与 30-6 缓存篇叙事衔接正确（且 30-6 修改后注明缓存未合入主线，逻辑自洽）。
7. **CI/CD 口径：合规。** 全库只说「云效平台里配置流水线」（24-3/24-4/25-1/26-x），未声称仓库内含 pipeline 代码——符合 scan3「流水线配置不在仓库内」的红线。唯一注意点：31-3 L58「结合 Docker 与 CI/CD 实现 DevOps」属简历语境，可保留。

---

## 三、版本号 / 数字抽查（对照 package.json 实况）

| 正文写法 | 出现篇目 | 核对结果 |
|---|---|---|
| antd `^5.11.2` | 14-4/14-6/14-7/14-8/14-9/15-4/15-7/16-1/16-2/16-3 等约 12 篇 | ✅ 与 client/release package.json 一致 |
| vite `^5.0.0` / plugin-react `^4.2.0` | 8-3/14-6/16-1/18-3/18-7/19-1 | ✅ 一致 |
| dnd-kit core 6.1.0 / sortable 8.0.0 / utilities 3.2.2 | 18-4/18-5/18-6/18-7/19-1/19-2/23-4 | ✅ 一致 |
| mobx `^6.12.0`、mobx-shallow-undo `^1.1.0` | 18-6/18-7/19-1/19-2/23-4 | ✅ 一致 |
| exceljs `^4.4.0` | 21-9/21-10/23-4 | ✅ 一致 |
| TypeORM `^0.3.17` + mysql2 `3.6.3` + @nestjs/typeorm `^10.0.1` | 10-5/10-8 及预先课 2/3 集 | ✅ 一致（B server 实况） |
| next `14.0.1`（第一期脚手架） | 3-2/3-5/3-6 | ⚠️ 无法从仓库验证（分期快照不在库内）；最终 release 为 14.0.4。属不同阶段的独立学习项目，**不构成矛盾，可保留**；若求稳可在 3-5 加注「课程后期发布子项目升级至 14.0.4」 |
| QPS/RT 数字（30-6：428~440 vs 410、样本 800；29-3：5.5/s@100并发、48.9/s@50并发；30-x 各 RT） | 第八期 | 课堂实测值，代码不可验证，内部口径自洽（如「逐步加压定最优 TPS」方法论统一），**保留** |
| 「15 种组件」类计数 | 全库 grep 无命中 | 正文未硬性写组件总数，无风险 |
| 渲染引擎/沙箱/AI 节点/DAG | 全库 grep 无命中 | 正文未把 A 工程独有能力安到课程 B 上，scan3 红线全部安全 |

---

## 四、关键库事实性核验（WebSearch）

1. **dnd-kit MouseSensor**：官方文档确认激活约束仅 `distance` / `delay` 两类，distance 为「激活拖拽前需移动的像素阈值」——证实 A3 对 18-4 L41「每 2 像素重判一次」的修正必要性；PointerSensor 也是合法组件，但源码用的是 MouseSensor，正文应随代码。
2. **AntD 5 + Next.js App Router**：官方 `use-with-next` 文档确认 `@ant-design/nextjs-registry` 的 `AntdRegistry` 包裹 layout 以完成 SSR 样式注入——20-5 的说法**准确，无需改**。
3. **MobX 6 / mobx-shallow-undo**：MobX 6 `makeAutoObservable` 用法属实；mobx-shallow-undo 无权威中文资料，以仓库源码 `trackUndo` 为准（A4）。

来源：[dnd-kit Mouse Sensor 文档](https://dndkit.com/legacy/api-documentation/sensors/mouse)、[Ant Design 官方 Usage with Next.js](https://ant.design/docs/react/use-with-next)、[AntdRegistry SSR 相关 GitHub Issue](https://github.com/ant-design/ant-design/issues/47122)

---

## 五、执行提示

- 修正共 10 组（A1~A10），涉及 13 个文件、约 30 处行文；target 与 blog 两份拷贝需同步。
- 二-4 的 store 命名项为「建议性」，不执行也不影响事实正确性。
- 修改 A6/A7/A8 后，第三期与第六/八期的接口路径口径自动拉平，无需另改 21-x/28-9/30-x。
