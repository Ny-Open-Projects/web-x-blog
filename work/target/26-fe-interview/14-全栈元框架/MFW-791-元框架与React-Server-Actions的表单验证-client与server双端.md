---
title: [MFW-791] Server Action 表单验证的双端
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-791：Server Action 表单验证的双端

**答**:
- 表单验证的双端架构：1) **client 验证**（即时反馈——zod schema 的 client 解析（user 看到错误立即修——不发请求）；2) **server 验证**（安全边界——client 验证可绕过（禁 JS/直接 POST——server 必须独立验证 RBL-947）；3) **schema 共享**（zod schema 定义在 shared 目录——client 与 server import 同一 schema（单源验证 RBL-946 推理链的验证维度）；4) **渐进增强**（server 验证兜底——JS 禁用时 server 端 zod 返回错误（useActionState 展示 RBL-512）。
- 验证的时序：client 先验（快反馈——表单 fill 时 onChange/onBlur）→ server 后验（安全——action 内 zod.parse）；「双端一致」= 同一 schema 同一规则（client 通过 → server 一定通过——schema 一致性保证）。
- 追问钩子：为什么「client 验证通过 ≠ server 验证通过」？——client 验证可被绕过（禁 JS/直接 POST/修改 payload——恶意用户的绕过路径）；server 验证 = 独立安全边界（不信任 client——零信任原则 RBL-947）；「双端验证的必要性」：client 验证是 UX（快速反馈减少请求），server 验证是安全（防绕过）——两者缺一不可：只 client = 不安全；只 server = 用户体验差。

```tsx
// shared/schema.ts（单源验证）
import { z } from 'zod';
export const ProfileSchema = z.object({
  name: z.string().min(2, '名称至少 2 字符'),
  email: z.string().email('邮箱格式错误'),
  age: z.number().int().min(0).max(150).optional(),
});
export type Profile = z.infer<typeof ProfileSchema>;     // 类型推导 RBL-926
// server action（安全验证）
'use server';
export async function updateProfile(formData: FormData) {
  const parsed = ProfileSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success)
    return { errors: parsed.error.flatten().fieldErrors };   // server 验证失败
  await db.users.update(session.userId, parsed.data);
  return { ok: true };
}
// client 组件（UX 验证 + server 提交）
'use client';
function ProfileForm({ initial }: { initial: Profile }) {
  const [state, action] = useActionState(updateProfile, null);
  return (
    <form action={action}>
      <input name="name" defaultValue={initial.name} />
      {state?.errors?.name && <p role="alert">{state.errors.name}</p>}
      <input name="email" defaultValue={initial.email} />
      {state?.errors?.email && <p role="alert">{state.errors.email}</p>}
      <button>Save</button>
    </form>
  );
}
```
