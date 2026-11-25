---
title: [V3-198] 设计一个富文本封装（wangEditor / tiptap 集成模式）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-198：设计一个富文本封装（wangEditor / tiptap 集成模式）？
**答**：
- 模式与 Canvas/地图一致（V3-177）：实例在 onMounted 创建，v-model 双向同步（编辑器 input -> model，外部 model 变化 -> setContent），onUnmounted destroy。
- 防循环：内部编辑触发的外部赋值要跳过 setContent（比较内容或加内部标志位）。
- 图片上传：拦截编辑器默认上传，接入自己的 OSS 直传（服务端签名），插入返回的 URL。
- 扩展点：wangEditor 用菜单配置与自定义模块；tiptap 用扩展（extension）体系，ProseMirror 生态可深定制，两种封装层 API 保持一致（v-model + toolbar 配置）。

```vue
<!-- components/RichEditor.vue —— wangEditor 封装 -->
<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from "vue";
import { Editor, Toolbar } from "@wangeditor/editor-for-vue";
import type { IDomEditor, IEditorConfig } from "@wangeditor/editor";

const props = defineProps<{ modelValue: string; placeholder?: string }>();
const emit = defineEmits<{ (e: "update:modelValue", v: string): void }>();

const editorRef = ref<IDomEditor | null>(null);
const htmlValue = ref(props.modelValue);
let inner = false; // 内部编辑标志：防 v-model 循环

const editorConfig: Partial<IEditorConfig> = {
  placeholder: props.placeholder ?? "请输入内容...",
  MENU_CONF: {
    // 图片上传：拦截默认行为，走 OSS 直传
    uploadImage: {
      async customUpload(file: File, insertFn: (url: string) => void) {
        const form = new FormData();
        form.append("file", file);
        // 服务端下发签名，前端直传 OSS
        const { url } = await fetch("/api/oss/sign", { method: "POST" })
          .then((r) => r.json())
          .then(async (sign) => {
            const resp = await fetch(sign.host, { method: "POST", body: form });
            return resp.json();
          });
        insertFn(url); // 插入编辑器
      },
    },
  },
};

// v-model 同步：外部值变化 -> 编辑器（编辑器内部变化不再回写，防循环）
watch(() => props.modelValue, (v) => {
  if (v !== htmlValue.value) htmlValue.value = v;
});
function onChange(editor: IDomEditor) {
  inner = true;
  emit("update:modelValue", editor.getHtml());
  inner = false;
}

onUnmounted(() => {
  editorRef.value?.destroy(); // wangEditor 必须 destroy，否则内存泄漏
});
</script>

<template>
  <div class="rich-editor">
    <Toolbar :editor="editorRef" :default-config="{ toolbarKeys: ['bold', 'italic', 'insertImage', 'insertTable'] }" />
    <Editor v-model="htmlValue" :default-config="editorConfig" @on-created="(e: IDomEditor) => (editorRef = e)"
      @on-change="onChange" style="height: 320px" />
  </div>
</template>

<style>
.rich-editor { border: 1px solid #dcdfe6; border-radius: 4px; }
</style>
```
