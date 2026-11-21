import { useState } from 'react';

type FieldKind = 'text' | 'textarea' | 'number' | 'json';

export interface FieldDef {
  key: string;
  label: string;
  kind: FieldKind;
  placeholder?: string;
}

/**
 * 各节点类型的参数面板 Schema（M5）。
 * 后端新增节点类型时，在此登记字段即可在前端自动出现结构化编辑器，
 * 无需改动 WorkflowNode 渲染逻辑。
 */
export const PARAM_SCHEMAS: Record<string, FieldDef[]> = {
  'trigger.formSubmit': [
    { key: 'formId', label: '表单ID', kind: 'text' },
    { key: 'data', label: '初始数据(JSON)', kind: 'json' },
  ],
  'transform.map': [
    { key: 'op', label: '操作', kind: 'text', placeholder: 'setField | pick | pickTo | concat' },
    { key: 'field', label: '目标字段', kind: 'text' },
    { key: 'value', label: '值', kind: 'text' },
    { key: 'from', label: '源字段', kind: 'text' },
    { key: 'to', label: '目标路径', kind: 'text' },
    { key: 'fields', label: '选取字段(JSON数组)', kind: 'json' },
    { key: 'prefix', label: '前缀', kind: 'text' },
    { key: 'suffix', label: '后缀', kind: 'text' },
  ],
  'ui.composePage': [
    { key: 'title', label: '页面标题', kind: 'text' },
    { key: 'components', label: '组件(JSON)', kind: 'json' },
  ],
  'action.sendSms': [
    { key: 'phone', label: '手机号', kind: 'text' },
    { key: 'template', label: '模板码', kind: 'text' },
  ],
  'action.ossUpload': [{ key: 'key', label: 'OSS Key', kind: 'text' }],
  // ---- M4 高风险节点：专用编辑器（代码 / 提示词）----
  'script.eval': [
    {
      key: 'code',
      label: '脚本（沙箱隔离执行）',
      kind: 'textarea',
      placeholder: 'setOutput({ ...data })',
    },
  ],
  'ai.llm': [
    { key: 'prompt', label: '提示词（支持 {{data.x}}）', kind: 'textarea', placeholder: '请处理：{{data}}' },
    { key: 'model', label: '模型', kind: 'text', placeholder: 'gpt-4o-mini / qwen-plus' },
    { key: 'temperature', label: '温度', kind: 'number' },
    { key: 'maxTokens', label: '最大Token', kind: 'number' },
  ],
};

export function ParamEditor({
  schema,
  params,
  onChange,
}: {
  schema: FieldDef[];
  params: Record<string, unknown>;
  onChange: (key: string, value: unknown) => void;
}) {
  // JSON 类字段用本地缓冲区，失焦时解析提交（避免输入中途 JSON 非法）
  const [jsonBuf, setJsonBuf] = useState<Record<string, string>>({});

  return (
    <div style={{ display: 'grid', gap: 4 }}>
      {schema.map((f) => {
        if (f.kind === 'json') {
          const raw = jsonBuf[f.key] ?? JSON.stringify(params[f.key] ?? null, null, 2);
          return (
            <label key={f.key} style={{ display: 'block' }}>
              <span style={{ fontSize: 10, color: '#666' }}>{f.label}</span>
              <textarea
                value={raw}
                onChange={(e) => setJsonBuf((b) => ({ ...b, [f.key]: e.target.value }))}
                onBlur={() => {
                  try {
                    onChange(f.key, JSON.parse(raw));
                  } catch {
                    /* 非法 JSON 暂不提交，保留用户输入 */
                  }
                }}
                rows={3}
                spellCheck={false}
                style={{ width: '100%', fontFamily: 'monospace', fontSize: 10, boxSizing: 'border-box' }}
              />
            </label>
          );
        }
        if (f.kind === 'textarea') {
          return (
            <label key={f.key} style={{ display: 'block' }}>
              <span style={{ fontSize: 10, color: '#666' }}>{f.label}</span>
              <textarea
                value={String(params[f.key] ?? '')}
                onChange={(e) => onChange(f.key, e.target.value)}
                rows={5}
                placeholder={f.placeholder}
                spellCheck={false}
                style={{ width: '100%', fontFamily: 'monospace', fontSize: 10, boxSizing: 'border-box' }}
              />
            </label>
          );
        }
        return (
          <label key={f.key} style={{ display: 'block' }}>
            <span style={{ fontSize: 10, color: '#666' }}>{f.label}</span>
            <input
              type={f.kind === 'number' ? 'number' : 'text'}
              value={String(params[f.key] ?? '')}
              placeholder={f.placeholder}
              onChange={(e) =>
                onChange(f.key, f.kind === 'number' ? Number(e.target.value) : e.target.value)
              }
              style={{ width: '100%', fontSize: 11, boxSizing: 'border-box' }}
            />
          </label>
        );
      })}
    </div>
  );
}
