---
title: [DP-126] 大型 Vue 应用如何治理依赖注入？provide 的 key 有什么规范？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-126：大型 Vue 应用如何治理依赖注入？provide 的 key 有什么规范？（高频）
**答**：
- 治理核心是 InjectionKey 规范：每个可注入服务定义 `InjectionKey<T>` 类型化 Symbol（TS 推断注入类型），key 集中在 `keys.ts` 注册，禁止裸字符串 key（DP-072 的工程化落地）。
- 分层规则：应用级（apiClient、i18n）在入口 provide；模块级（表单上下文）在模块根组件 provide；跨层级取值提供默认值兜底。
- 约束：inject 只读或调用服务方法，不直接改注入对象属性；provide 的服务对象用 readonly/冻结保护写入口。

```vue
<script setup>
// keys.ts：类型化 key 集中注册（唯一允许出现 key 字面量的地方）
import type { InjectionKey } from 'vue';
export interface ApiClient { get<T>(url: string): Promise<T>; post<T>(url: string, body: unknown): Promise<T>; }
export interface I18nService { t(key: string): string; locale: Ref<string>; }
export const ApiKey: InjectionKey<ApiClient> = Symbol('api');
export const I18nKey: InjectionKey<I18nService> = Symbol('i18n');
</script>

<script setup>
// 服务组件层：provide 与消费严格走 key，类型全程可推
import { provide, inject, readonly } from 'vue';
import { ApiKey, I18nKey, defaultApiClient, defaultI18n } from './services';
// 入口组件：应用级服务统一在此装配（组合根）
provide(ApiKey, defaultApiClient);
provide(I18nKey, readonly(defaultI18n));                       // 只读：写操作走服务方法
// 深层消费：带默认值兜底 + 类型自动推断为 I18nService
const i18n = inject(I18nKey, defaultI18n);
const api = inject(ApiKey)!;                                   // 应用级必存在，用 ! 断言
const title = computed(() => i18n.t('order.title'));
onSubmit(() => api.post('/order', form));
</script>
```
