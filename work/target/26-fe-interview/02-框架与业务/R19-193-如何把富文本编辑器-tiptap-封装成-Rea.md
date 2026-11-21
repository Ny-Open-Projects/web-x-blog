---
title: [R19-193] 如何把富文本编辑器（tiptap）封装成 React 表单友好的组件？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-193：如何把富文本编辑器（tiptap）封装成 React 表单友好的组件？
**答**：
- 边界划分：React 管"受控 value、禁用态、错误提示、工具栏"，tiptap 管"内容模型与选区"；内容同步走 `onUpdate -> onChange(HTML)`，外部 value 变化用 `editor.commands.setContent`（比对避免光标跳变）。
- 受控陷阱：输入过程中外部回写 content 会重置光标——用"内部脏标记 + 仅在非焦点或外部不同才回写"策略。
- 工具栏命令：editor.chain().focus().toggleBold().run() 这类链式命令直接映射按钮，选区状态用 `editor.isActive('bold')` 投影。
- 集成 RHF：包一层 Controller，把 editor 当普通受控输入；粘贴净化（paste 规则）与字数限制用扩展。

```tsx
// RichTextEditor.tsx —— tiptap 的表单友好封装
import { useEditor, EditorContent } from '@tiptap/react';
import StarterKit from '@tiptap/starter-kit';
import { useEffect, useRef } from 'react';
import { Controller, useForm, type Control } from 'react-hook-form';

export function RichTextEditor({ value, onChange, readOnly, maxLength }: {
  value: string;
  onChange: (html: string) => void;
  readOnly?: boolean;
  maxLength?: number;
}) {
  const isInternalChange = useRef(false);

  const editor = useEditor({
    extensions: [
      StarterKit.configure({ heading: { levels: [2, 3] } }),
    ],
    content: value,
    editable: !readOnly,
    onUpdate: ({ editor }) => {
      isInternalChange.current = true;
      onChange(editor.getHTML());        // 编辑 -> 通知外部
    },
    // 粘贴净化：只保留纯文本，防外部脏 HTML
    editorProps: {
      handlePaste: () => {
        // 生产用 tiptap paste rule / prosemirror-transform 清洗
        return false;
      },
    },
  });

  // 外部 value 变化 -> 回写编辑器（防循环：仅外部变更才回写）
  useEffect(() => {
    if (!editor) return;
    if (isInternalChange.current) {
      isInternalChange.current = false;  // 自己触发的更新，跳过回写
      return;
    }
    if (value !== editor.getHTML()) {
      editor.commands.setContent(value, false); // false：不触发 onUpdate
    }
  }, [value, editor]);

  useEffect(() => {
    editor?.setEditable(!readOnly);
  }, [readOnly, editor]);

  if (!editor) return null;

  const charCount = editor.state.doc.textContent.length;

  return (
    <div style={{ border: '1px solid #ddd' }}>
      {/* 工具栏：命令链 + 状态投影 */}
      <div style={{ display: 'flex', gap: 4, borderBottom: '1px solid #ddd' }}>
        <button type="button" onClick={() => editor.chain().focus().toggleBold().run()}
          style={{ fontWeight: editor.isActive('bold') ? 700 : 400 }}>B</button>
        <button type="button" onClick={() => editor.chain().focus().toggleItalic().run()}
          style={{ fontStyle: editor.isActive('italic') ? 'italic' : undefined }}>I</button>
        <button type="button" onClick={() => editor.chain().focus().toggleHeading({ level: 2 }).run()}>
          H2
        </button>
        <button type="button" onClick={() => editor.chain().focus().toggleBulletList().run()}>列表</button>
        <span style={{ marginLeft: 'auto' }}>{maxLength ? `${charCount}/${maxLength}` : charCount}</span>
      </div>
      <EditorContent editor={editor} style={{ minHeight: 200 }} />
    </div>
  );
}

// 与 React Hook Form 集成：一个 Controller 搞定
type FormValues = { body: string };

export function PostForm() {
  const { control, handleSubmit } = useForm<FormValues>({ defaultValues: { body: '' } });
  return (
    <form onSubmit={handleSubmit(v => console.log(v.body))}>
      <Controller
        name="body"
        control={control as Control<FormValues>}
        rules={{ required: '正文不能为空' }}
        render={({ field, fieldState }) => (
          <>
            <RichTextEditor value={field.value} onChange={field.onChange} maxLength={5000} />
            {fieldState.error && <em style={{ color: 'red' }}>{fieldState.error.message}</em>}
          </>
        )}
      />
      <button type="submit">发布</button>
    </form>
  );
}
```
