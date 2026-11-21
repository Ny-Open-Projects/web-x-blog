import { PageSchema, ComponentNode } from '@lowcode/shared';

function esc(s: unknown): string {
  return String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

/** 把单个组件渲染为 HTML（支持嵌套 children）。 */
function renderNode(n: ComponentNode): string {
  const opts = n.options ?? {};
  switch (n.type) {
    case 'text':
      return `<p class="lc-text">${esc(opts.text)}</p>`;
    case 'input':
    case 'textarea':
      return `<label class="lc-field"><span>${esc(opts.label)}</span><input name="${esc(n.id)}" placeholder="${esc(opts.placeholder)}"${opts.required ? ' required' : ''}/></label>`;
    case 'select': {
      const items = (opts.options as { label?: string; value?: string }[]) ?? [];
      const optsHtml = items.map((o) => `<option value="${esc(o.value)}">${esc(o.label)}</option>`).join('');
      return `<label class="lc-field"><span>${esc(opts.label)}</span><select name="${esc(n.id)}">${optsHtml}</select></label>`;
    }
    case 'button':
      return `<button type="button" class="lc-btn">${esc(opts.label)}</button>`;
    case 'image':
      return `<img class="lc-img" src="${esc(opts.src)}" alt="${esc(opts.label)}"/>`;
    case 'form':
      return `<form class="lc-form"${opts.formId ? ` data-form-id="${esc(opts.formId)}"` : ''}>${(n.children ?? []).map(renderNode).join('\n')}<button type="submit" class="lc-btn">${esc(opts.submitLabel ?? '提交')}</button></form>`;
    case 'grid': {
      const cols = Number(opts.columns ?? 0);
      const style = cols > 0 ? ` style="grid-template-columns:repeat(${cols},1fr)"` : '';
      return `<div class="lc-grid"${style}>${(n.children ?? []).map(renderNode).join('\n')}</div>`;
    }
    case 'container':
      return `<div class="lc-container"${opts.label ? ` data-label="${esc(opts.label)}"` : ''}>${(n.children ?? []).map(renderNode).join('\n')}</div>`;
    default:
      return `<!-- unsupported component: ${esc(n.type)} -->`;
  }
}

/**
 * 服务端渲染：把工作流产出的 PageSchema 渲染成一份自包含 HTML。
 * 这是"连线即生成页面"闭环的最后一环——前端渲染端未来可复用同一份 PageSchema。
 */
export function renderPageToHtml(schema: PageSchema): string {
  const body = (schema.nodes ?? []).map(renderNode).join('\n');
  return `<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>${esc(schema.title)}</title>
<style>
  body{font-family:system-ui,-apple-system,sans-serif;margin:24px;color:#1f2937}
  label{display:block;margin:10px 0}
  input,select{padding:6px 8px;min-width:240px}
  .lc-btn{padding:6px 14px;cursor:pointer}
  .lc-img{max-width:100%}
  .lc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}
  .lc-container{border:1px dashed #d9d9d9;border-radius:6px;padding:10px;margin:8px 0}
  .lc-form{border:1px solid #f0f0f0;border-radius:6px;padding:12px;margin:8px 0}
</style>
</head>
<body>
<h1>${esc(schema.title)}</h1>
${body}
</body>
</html>`;
}
