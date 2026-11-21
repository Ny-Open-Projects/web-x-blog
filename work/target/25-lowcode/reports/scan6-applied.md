# 扫描6 修正落地报告（scan6-applied）

- 依据：`scan6-facts.md` A1~A10（13 个文件、约 30 处）
- 真源：`work/target/25-lowcode/posts/` 已改；已整体 rm + cp -R 同步到 `work/blog/source/_posts/xiaodi-lowcode/`（diff -rq 校验一致）
- `work/source/` 未改动（红线）
- 全部修正已逐条 grep 复核，无残留旧写法（清单范围内）

## 逐条结果

| 组 | 文件 | 修改前 → 修改后 | 结果 |
|---|---|---|---|
| A1 | 00.预先课/第_2_集__后端接口开发—课程的创建接口开发.md (L46) | 「登录态、RBAC 权限体系」→「登录态、接口权限守卫」 | 成功 |
| A2-1 | 08.第八期/30-6 (L11 导语) | `getCacheData`→`getCachedData`；句末补「注意：该缓存版本在最终仓库源码中处于注释状态……线上接口仍走无缓存版。」 | 成功 |
| A2-2 | 30-6 (代码块 L37/L42) | `this.redis.getCacheData(`→`getCachedData(`；`{ ttl: 60, force: false }`→`{ ttl: 60 * 10, force: false }` | 成功 |
| A2-3 | 30-6 (伪代码块) | 方法名→`getCachedData`；删除 `await this.del(key);` 行；`set(key, data, options.ttl)`→`set(key, JSON.stringify(data), 'EX', options.ttl)` | 成功 |
| A2-4 | 30-6 (小结 L119) | 改名 + 补「课程示例 TTL 为 600 秒；force 置空后回源覆盖写回，并非显式 del」 | 成功 |
| A2-5 | 30-6 (L89 推广段) | 补「以最终仓库为准，该缓存入口当前仅以注释形式保留在 `low-code.service.ts` 中」 | 成功 |
| A3-1 | 05.第五期/18-4 (L11 导语) | 「PointerSensor 与 closestCenter」→「MouseSensor 与 closestCenter」 | 成功 |
| A3-2 | 18-4 (L41) | 「移动 2 像素才触发一次监听……每移动 2 像素重新判断」→「激活约束 `distance: 2`……区分『点击』与『拖拽』的阈值，不是周期性重判」 | 成功 |
| A4 | 05.第五期/18-5 (L75) | `triggerUndo`→`trackUndo` | 成功 |
| A5-1 | 05.第五期/20-6 (L51/L60) | `getQuestionComponentValueFeed`→`getQuestionComponentValueField`（全文 2 处） | 成功 |
| A5-2 | 20-6 (L51) | `defaultCheckbox`→`defaultChecked` | 成功 |
| A6-1 | 03.第三期/11-8 (L77/L78/L82) | `/user/password`→`/user/password_login`；`/user/form`→`/user/phone_login` | 成功 |
| A6-2 | 03.第三期/13-8 (L16/L27/L30/L90) | 同上两条路径替换（含 makeRequest 代码 2 处） | 成功 |
| A7-1 | 03.第三期/11-5 (L39) | 「路径如 `/user/sendCode`」→「`/user/send_code`」 | 成功 |
| A7-2 | 03.第三期/13-5 (L66/L110) | `makeRequest('/user/sendCode')`→`('/user/send_code')`；小结同步 | 成功 |
| A8-1 | 05.第五期/19-5 (L17/L36/L70) | `/local/releaseWithUser`→`/low_code/release_with_user`（L17 带 /api 前缀说明；L36/L70 注释与正文用 `/api/low_code/release_with_user`） | 成功 |
| A8-2 | 05.第五期/20-2 (L23/L39) | `GET /local/releaseWithUser`→`GET /api/low_code/release_with_user`；`GET /local/release?`→`GET /api/low_code/release?` | 成功 |
| A8-3 | 05.第五期/20-6 (L30/L58) | fetch URL `/api/local/release?id=`→`/api/low_code/release?id=`；小结同步 | 成功 |
| A9-1 | 04.第四期/14-2 (L38 组件表) | 删「所属配置 ID」；改为「组件 `type`（默认值 `titleText`）、`page_id`、`account_id`、`options`」 | 成功 |
| A9-2 | 14-2 (L40 组件数据表) | `purpose`→`props`（simple-json 数组 `{ id, value }`）；补「`user` 为访客匿名标识 MD5(ip+ua)，非登录用户」 | 成功 |
| A9-3 | 14-2 (L44) | `share/src/lowcode.ts`→`share/src/types/entity/low-code.ts`；`ILowcode`→`ILowCode` | 成功 |
| A10-1 | 05.第五期/17-1 (L27) | `src/modules`→`src/utils/modules` | 成功 |
| A10-2 | 17-1 (L27 同段) | 「`release.module.ts`、`wechat-login` 模块」→「`redis.module.ts`、`wechat-login-tool.module.ts` 等公共模块」 | 成功 |

## 清单外连带修正（同文件内与已改项直接矛盾，避免改后自相矛盾）

| 文件 | 修改 | 原因 |
|---|---|---|
| 30-6 L48（参数三 options 说明） | 「force 为 true 时把 Redis 里对应的数据清掉」→「置空 data 后回源重查并覆盖写回（并非显式 del）」 | 同文件伪代码已删 del，原句与之直接矛盾 |
| 11-5 L107 | `@Post('sendCode')`→`@Post('send_code')` | 同文件 L39 路径已改为 send_code，装饰器须一致（源码即 `@Post('send_code')`） |
| 17-1 L15 | 「沿用此前 `release.module.ts`、`wechat-login` 等模块」→「`redis.module.ts`、`wechat-login-tool.module.ts` 等模块」 | 同文件 L27 已改，L15 原句与之直接矛盾 |

## 清单外、未改动的相关残留（供后续扫描参考）

以下与 A5/A8 同类问题出现在清单未列的篇目中，本轮按「只执行清单」未动：

- `05.第五期/20-8.低代码项目发布页面—发布页面提交问卷.md`：3 处 `getQuestionComponentValueFeed`、2 处 `defaultCheckbox`（与 A5 同源），以及 `/api/local/questionDataPost` 路径。
- `/local/...` 旧路径仍存在于：14-3（3 处 POST /local/release）、19-4（2 处）、20-3（isQuestionDataPost）、20-7（2 处）、27-5（3 处 /api/local/release）；19-5 L39 还有「控制器中的 `releaseWithUser`」方法名表述。
- 二-4 store 命名建议项（19-5 加注源码变量名）按清单「建议性」未执行。
