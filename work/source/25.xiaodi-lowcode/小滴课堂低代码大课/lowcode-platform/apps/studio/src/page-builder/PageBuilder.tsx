import { useState, useCallback } from 'react';
import type {
  PageSchema,
  ComponentNode,
  ComponentType,
  ComponentOption,
} from '@lowcode/shared';
import { pageApi, type PageDefDto } from './pageApi';

type BlockType =
  | 'text'
  | 'image'
  | 'button'
  | 'input'
  | 'textarea'
  | 'select'
  | 'container'
  | 'grid'
  | 'form';

/** 可承载子组件的容器类型（低代码落地里"表单/栅格/容器"是搭建真实业务页面的骨架）。 */
const CONTAINER_TYPES: BlockType[] = ['container', 'grid', 'form'];

const PALETTE: { type: BlockType; label: string; group: '基础' | '容器' }[] = [
  { type: 'text', label: '文本', group: '基础' },
  { type: 'image', label: '图片', group: '基础' },
  { type: 'button', label: '按钮', group: '基础' },
  { type: 'input', label: '输入框', group: '基础' },
  { type: 'textarea', label: '多行文本', group: '基础' },
  { type: 'select', label: '下拉框', group: '基础' },
  { type: 'container', label: '容器', group: '容器' },
  { type: 'grid', label: '栅格', group: '容器' },
  { type: 'form', label: '表单', group: '容器' },
];

function isContainer(t: string): boolean {
  return (CONTAINER_TYPES as string[]).includes(t);
}

function defaultOptions(t: BlockType): ComponentOption {
  switch (t) {
    case 'text':
      return { text: '示例文本' };
    case 'image':
      return { src: 'https://picsum.photos/320/180', label: '图片描述' };
    case 'button':
      return { label: '按钮' };
    case 'input':
      return { label: '输入框', placeholder: '请输入', required: false };
    case 'textarea':
      return { label: '多行文本', placeholder: '请输入' };
    case 'select':
      return {
        label: '下拉框',
        options: [
          { label: '选项一', value: 'a' },
          { label: '选项二', value: 'b' },
        ],
      };
    case 'container':
      return { label: '容器' };
    case 'grid':
      return { columns: 2 };
    case 'form':
      return { submitLabel: '提交', formId: 'form_' + Date.now() };
  }
}

let _seq = 0;
function makeNode(t: BlockType): ComponentNode {
  const node: ComponentNode = {
    id: `c_${Date.now()}_${(++_seq).toString(36)}`,
    type: t as ComponentType,
    options: defaultOptions(t),
  };
  if (isContainer(t)) node.children = [];
  return node;
}

// ---------- 树操作 ----------

function cloneTree(nodes: ComponentNode[]): ComponentNode[] {
  return nodes.map((n) => ({
    ...n,
    options: { ...(n.options ?? {}) },
    ...(n.children ? { children: cloneTree(n.children) } : {}),
  }));
}

function findNode(nodes: ComponentNode[], id: string): ComponentNode | null {
  for (const n of nodes) {
    if (n.id === id) return n;
    if (n.children?.length) {
      const r = findNode(n.children, id);
      if (r) return r;
    }
  }
  return null;
}

/** 返回节点在树中的索引路径（根为 []，其子节点为 [i] ...）。 */
function findPath(nodes: ComponentNode[], id: string, path: number[] = []): number[] | null {
  for (let i = 0; i < nodes.length; i++) {
    if (nodes[i].id === id) return [...path, i];
    if (nodes[i].children?.length) {
      const p = findPath(nodes[i].children!, id, [...path, i]);
      if (p) return p;
    }
  }
  return null;
}

/** 取路径末端的同级数组（节点所在的那一层）。 */
function listAt(nodes: ComponentNode[], path: number[]): ComponentNode[] {
  let list = nodes;
  for (let i = 0; i < path.length - 1; i++) list = list[path[i]].children ?? [];
  return list;
}

function summarize(n: ComponentNode): string {
  const o = n.options ?? {};
  if (n.type === 'text') return String(o.text ?? '');
  if (n.type === 'image') return String(o.src ?? '');
  if (n.type === 'button' || n.type === 'input' || n.type === 'textarea' || n.type === 'select')
    return String(o.label ?? '');
  if (n.type === 'grid') return `${o.columns ?? 'auto'} 列`;
  if (n.type === 'form') return `提交按钮：${o.submitLabel ?? '提交'}`;
  if (n.type === 'container') return String(o.label ?? '容器');
  return JSON.stringify(o);
}

export function PageBuilder() {
  const [schema, setSchema] = useState<PageSchema>({
    version: 1,
    title: '未命名页面',
    nodes: [],
  });
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [savedId, setSavedId] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [log, setLog] = useState('');
  const [loadOpen, setLoadOpen] = useState(false);
  const [items, setItems] = useState<PageDefDto[]>([]);
  /** 插入目标：null = 根级；否则为某个容器节点 id。 */
  const [insertParentId, setInsertParentId] = useState<string | null>(null);
  const [collapsed, setCollapsed] = useState<Record<string, boolean>>({});

  const selected = selectedId ? findNode(schema.nodes, selectedId) : null;
  const insertParent = insertParentId ? findNode(schema.nodes, insertParentId) : null;

  /** 新增组件：插入到指定父容器（无则根级）。 */
  const addBlock = useCallback(
    (t: BlockType) => {
      setSchema((s) => {
        const node = makeNode(t);
        let nodes: ComponentNode[];
        if (insertParentId) {
          const path = findPath(s.nodes, insertParentId);
          if (!path) {
            nodes = [...s.nodes, node];
          } else {
            const next = cloneTree(s.nodes);
            const parent = findNode(next, insertParentId)!;
            parent.children = [...(parent.children ?? []), node];
            nodes = next;
          }
        } else {
          nodes = [...s.nodes, node];
        }
        setSelectedId(node.id);
        return { ...s, nodes };
      });
      setLog(
        `✓ 已添加${PALETTE.find((p) => p.type === t)?.label ?? t}${
          insertParent ? ` → ${insertParent.type}` : ''
        }`,
      );
    },
    [insertParentId, insertParent],
  );

  const updateOption = useCallback((id: string, key: string, value: unknown) => {
    setSchema((s) => {
      const next = cloneTree(s.nodes);
      const target = findNode(next, id);
      if (!target) return s;
      target.options = { ...(target.options ?? {}), [key]: value };
      return { ...s, nodes: next };
    });
  }, []);

  /** 同级内上下移动（仅在兄弟节点之间移动，跨层级需先改结构）。 */
  const move = useCallback((id: string, dir: -1 | 1) => {
    setSchema((s) => {
      const path = findPath(s.nodes, id);
      if (!path) return s;
      const next = cloneTree(s.nodes);
      const list = listAt(next, path);
      const i = path[path.length - 1];
      const j = i + dir;
      if (j < 0 || j >= list.length) return s;
      [list[i], list[j]] = [list[j], list[i]];
      return { ...s, nodes: next };
    });
  }, []);

  const remove = useCallback((id: string) => {
    setSchema((s) => {
      const next = cloneTree(s.nodes);
      const path = findPath(next, id);
      if (!path) return s;
      const list = listAt(next, path);
      list.splice(path[path.length - 1], 1);
      return { ...s, nodes: next };
    });
    setSelectedId((cur) => (cur === id ? null : cur));
    setInsertParentId((cur) => (cur === id ? null : cur));
  }, []);

  const save = useCallback(async () => {
    setBusy(true);
    try {
      if (savedId) {
        await pageApi.update(savedId, schema.title, schema);
        setLog('✓ 已更新，ID=' + savedId);
      } else {
        const p = await pageApi.create(schema.title, schema);
        setSavedId(p.id);
        setLog('✓ 已保存，ID=' + p.id);
      }
    } catch (e: any) {
      setLog('保存失败: ' + e.message);
    } finally {
      setBusy(false);
    }
  }, [savedId, schema]);

  const preview = useCallback(() => {
    if (!savedId) {
      setLog('请先保存再预览');
      return;
    }
    window.open(pageApi.renderUrl(savedId), '_blank', 'noopener');
  }, [savedId]);

  const reset = useCallback(() => {
    setSchema({ version: 1, title: '未命名页面', nodes: [] });
    setSelectedId(null);
    setSavedId(null);
    setInsertParentId(null);
    setLog('');
  }, []);

  const refreshLoad = useCallback(() => {
    pageApi.list().then(setItems).catch(() => setItems([]));
  }, []);

  const load = useCallback(async (id: string) => {
    try {
      const p = await pageApi.get(id);
      const s = JSON.parse(p.schemaJson ?? '{}') as PageSchema;
      setSchema({ version: s.version ?? 1, title: s.title ?? p.name, nodes: s.nodes ?? [] });
      setSavedId(p.id);
      setSelectedId(null);
      setInsertParentId(null);
      setLoadOpen(false);
      setLog('✓ 已加载 ' + p.id);
    } catch (e: any) {
      setLog('加载失败: ' + e.message);
    }
  }, []);

  /** 递归渲染结构树（容器可展开/折叠）。 */
  const renderTree = (nodes: ComponentNode[], depth: number) =>
    nodes.map((n) => {
      const hasKids = !!n.children?.length;
      const isCollapsed = !!collapsed[n.id];
      return (
        <div key={n.id}>
          <div
            onClick={() => setSelectedId(n.id)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 8,
              padding: '6px 10px',
              marginBottom: 4,
              marginLeft: depth * 16,
              background: n.id === selectedId ? '#e6f4ff' : '#fff',
              border: `1px solid ${n.id === selectedId ? '#1677ff' : '#eee'}`,
              borderRadius: 6,
              cursor: 'pointer',
            }}
          >
            {isContainer(n.type) ? (
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  setCollapsed((c) => ({ ...c, [n.id]: !c[n.id] }));
                }}
                style={{ width: 18, height: 18, lineHeight: '16px', padding: 0, cursor: 'pointer' }}
                title={isCollapsed ? '展开' : '折叠'}
              >
                {isCollapsed ? '▸' : '▾'}
              </button>
            ) : (
              <span style={{ width: 18, display: 'inline-block' }} />
            )}
            <span style={{ fontSize: 11, color: isContainer(n.type) ? '#52c41a' : '#1677ff', minWidth: 64 }}>
              {n.type}
            </span>
            <span
              style={{
                flex: 1,
                overflow: 'hidden',
                textOverflow: 'ellipsis',
                whiteSpace: 'nowrap',
                color: '#333',
              }}
            >
              {summarize(n)}
              {isContainer(n.type) && (
                <em style={{ color: '#999', fontStyle: 'normal', fontSize: 11 }}>
                  （{n.children?.length ?? 0} 个子组件）
                </em>
              )}
            </span>
            {isContainer(n.type) && (
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  setInsertParentId(n.id);
                  setSelectedId(n.id);
                }}
                title="向该容器内添加组件"
              >
                ＋子组件
              </button>
            )}
            <button onClick={(e) => { e.stopPropagation(); move(n.id, -1); }}>↑</button>
            <button onClick={(e) => { e.stopPropagation(); move(n.id, 1); }}>↓</button>
            <button onClick={(e) => { e.stopPropagation(); remove(n.id); }}>✕</button>
          </div>
          {hasKids && !isCollapsed && renderTree(n.children!, depth + 1)}
        </div>
      );
    });

  return (
    <div style={{ display: 'flex', height: '100%' }}>
      {/* 左侧：组件面板 */}
      <div style={{ width: 160, borderRight: '1px solid #eee', padding: 12, overflow: 'auto' }}>
        <div style={{ fontSize: 12, color: '#999', marginBottom: 6 }}>组件</div>
        {insertParent ? (
          <div
            style={{
              marginBottom: 8,
              padding: '6px 8px',
              background: '#f6ffed',
              border: '1px solid #b7eb8f',
              borderRadius: 6,
              fontSize: 12,
            }}
          >
            插入到 <b>{insertParent.type}</b> 内
            <button
              onClick={() => setInsertParentId(null)}
              style={{ display: 'block', marginTop: 4, fontSize: 11, cursor: 'pointer' }}
            >
              ✕ 改为插入到根级
            </button>
          </div>
        ) : (
          <div style={{ marginBottom: 8, fontSize: 12, color: '#999' }}>插入到：根级</div>
        )}
        {(['基础', '容器'] as const).map((g) => (
          <div key={g}>
            <div style={{ fontSize: 11, color: '#bbb', margin: '8px 0 4px' }}>{g}组件</div>
            {PALETTE.filter((p) => p.group === g).map((p) => (
              <button
                key={p.type}
                onClick={() => addBlock(p.type)}
                style={{
                  display: 'block',
                  width: '100%',
                  marginBottom: 6,
                  padding: '6px 8px',
                  cursor: 'pointer',
                  border: isContainer(p.type) ? '1px solid #b7eb8f' : undefined,
                }}
              >
                + {p.label}
              </button>
            ))}
          </div>
        ))}
      </div>

      {/* 中间：结构树 */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', minWidth: 0 }}>
        <div
          style={{
            display: 'flex',
            gap: 8,
            alignItems: 'center',
            padding: '8px 12px',
            borderBottom: '1px solid #eee',
          }}
        >
          <input
            value={schema.title}
            onChange={(e) => setSchema((s) => ({ ...s, title: e.target.value }))}
            placeholder="页面名称"
            style={{ padding: '4px 8px', width: 200 }}
          />
          <button onClick={save} disabled={busy}>
            {savedId ? '更新' : '保存'}
          </button>
          <button onClick={preview} disabled={!savedId}>
            预览
          </button>
          <button onClick={reset}>新建</button>
          <span style={{ position: 'relative' }}>
            <button
              onClick={() => {
                setLoadOpen((v) => !v);
                if (!loadOpen) refreshLoad();
              }}
            >
              加载▾
            </button>
            {loadOpen && (
              <div
                style={{
                  position: 'absolute',
                  top: 28,
                  left: 0,
                  background: '#fff',
                  border: '1px solid #ddd',
                  borderRadius: 6,
                  minWidth: 220,
                  zIndex: 10,
                  maxHeight: 240,
                  overflow: 'auto',
                }}
              >
                {items.length === 0 && (
                  <div style={{ padding: 8, color: '#999', fontSize: 12 }}>暂无</div>
                )}
                {items.map((p) => (
                  <div
                    key={p.id}
                    onClick={() => load(p.id)}
                    style={{ padding: '6px 8px', cursor: 'pointer', borderBottom: '1px solid #f0f0f0' }}
                  >
                    {p.name} <code style={{ fontSize: 10, color: '#888' }}>{p.id}</code>
                  </div>
                ))}
              </div>
            )}
          </span>
          <span style={{ color: '#999', fontSize: 12 }}>
            {savedId ? '已存 ' + savedId : '未保存'}
          </span>
        </div>

        <div style={{ flex: 1, overflow: 'auto', padding: 12, background: '#fafafa' }}>
          {schema.nodes.length === 0 && (
            <div style={{ color: '#999', fontSize: 13 }}>从左侧添加组件开始搭建页面</div>
          )}
          {renderTree(schema.nodes, 0)}
        </div>

        <pre
          style={{
            margin: 0,
            maxHeight: 140,
            overflow: 'auto',
            padding: 12,
            background: '#1e1e1e',
            color: '#0f0',
            fontSize: 11,
            whiteSpace: 'pre-wrap',
          }}
        >
          {log || '就绪'}
        </pre>
      </div>

      {/* 右侧：属性编辑 */}
      <div style={{ width: 280, borderLeft: '1px solid #eee', padding: 12, overflow: 'auto' }}>
        <div style={{ fontSize: 12, color: '#999', marginBottom: 8 }}>属性</div>
        {!selected && <div style={{ color: '#999', fontSize: 13 }}>选中一个组件以编辑属性</div>}
        {selected && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            <div style={{ fontSize: 12, color: '#1677ff' }}>
              {selected.type}
              {isContainer(selected.type) && (
                <em style={{ color: '#999', fontStyle: 'normal', fontSize: 11 }}>
                  （{selected.children?.length ?? 0} 个子组件）
                </em>
              )}
            </div>

            {selected.type === 'text' && (
              <Field label="文本内容">
                <textarea
                  value={String(selected.options.text ?? '')}
                  onChange={(e) => updateOption(selected.id, 'text', e.target.value)}
                  rows={3}
                  style={{ width: '100%' }}
                />
              </Field>
            )}

            {selected.type === 'image' && (
              <>
                <Field label="图片地址">
                  <input
                    value={String(selected.options.src ?? '')}
                    onChange={(e) => updateOption(selected.id, 'src', e.target.value)}
                    style={{ width: '100%' }}
                  />
                </Field>
                <Field label="替代文本(alt)">
                  <input
                    value={String(selected.options.label ?? '')}
                    onChange={(e) => updateOption(selected.id, 'label', e.target.value)}
                    style={{ width: '100%' }}
                  />
                </Field>
              </>
            )}

            {(selected.type === 'button' ||
              selected.type === 'input' ||
              selected.type === 'textarea' ||
              selected.type === 'select') && (
              <Field label="标签/文字">
                <input
                  value={String(selected.options.label ?? '')}
                  onChange={(e) => updateOption(selected.id, 'label', e.target.value)}
                  style={{ width: '100%' }}
                />
              </Field>
            )}

            {(selected.type === 'input' || selected.type === 'textarea') && (
              <>
                <Field label="占位提示">
                  <input
                    value={String(selected.options.placeholder ?? '')}
                    onChange={(e) => updateOption(selected.id, 'placeholder', e.target.value)}
                    style={{ width: '100%' }}
                  />
                </Field>
                {selected.type === 'input' && (
                  <label style={{ fontSize: 13 }}>
                    <input
                      type="checkbox"
                      checked={!!selected.options.required}
                      onChange={(e) => updateOption(selected.id, 'required', e.target.checked)}
                    />{' '}
                    必填
                  </label>
                )}
              </>
            )}

            {selected.type === 'select' && (
              <Field label="选项(JSON 数组)">
                <textarea
                  defaultValue={JSON.stringify(selected.options.options ?? [], null, 2)}
                  onBlur={(e) => {
                    try {
                      const arr = JSON.parse(e.target.value);
                      updateOption(selected.id, 'options', arr);
                      setLog('✓ 选项已更新');
                    } catch {
                      setLog('⚠ 选项 JSON 解析失败，未保存');
                    }
                  }}
                  rows={6}
                  style={{ width: '100%', fontFamily: 'monospace', fontSize: 11 }}
                />
              </Field>
            )}

            {selected.type === 'container' && (
              <Field label="容器标题(仅用于识别)">
                <input
                  value={String(selected.options.label ?? '')}
                  onChange={(e) => updateOption(selected.id, 'label', e.target.value)}
                  style={{ width: '100%' }}
                />
              </Field>
            )}

            {selected.type === 'grid' && (
              <Field label="列数（0=自适应）">
                <input
                  type="number"
                  min={0}
                  max={12}
                  value={Number(selected.options.columns ?? 0)}
                  onChange={(e) => updateOption(selected.id, 'columns', Number(e.target.value))}
                  style={{ width: '100%' }}
                />
              </Field>
            )}

            {selected.type === 'form' && (
              <>
                <Field label="提交按钮文字">
                  <input
                    value={String(selected.options.submitLabel ?? '提交')}
                    onChange={(e) => updateOption(selected.id, 'submitLabel', e.target.value)}
                    style={{ width: '100%' }}
                  />
                </Field>
                <Field label="表单标识(formId)">
                  <input
                    value={String(selected.options.formId ?? '')}
                    onChange={(e) => updateOption(selected.id, 'formId', e.target.value)}
                    style={{ width: '100%' }}
                  />
                </Field>
              </>
            )}

            {isContainer(selected.type) && (
              <button
                onClick={() => {
                  setInsertParentId(selected.id);
                  setLog(`✓ 后续新增组件将插入到 ${selected.type} 内`);
                }}
                style={{ borderColor: '#52c41a', color: '#389e0d' }}
              >
                ＋ 向此容器添加子组件
              </button>
            )}

            <div style={{ borderTop: '1px solid #f0f0f0', paddingTop: 8 }}>
              <button onClick={() => remove(selected.id)} style={{ color: '#cf1322' }}>
                删除该组件
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

function Field({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <label style={{ display: 'block', fontSize: 13 }}>
      <div style={{ marginBottom: 4, color: '#666' }}>{label}</div>
      {children}
    </label>
  );
}
