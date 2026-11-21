import { useState } from 'react';
import { WorkflowCanvas } from './workflow/WorkflowCanvas';
import { PageBuilder } from './page-builder/PageBuilder';

export function App() {
  const [tab, setTab] = useState<'workflow' | 'page'>('workflow');
  return (
    <div
      style={{
        fontFamily: 'system-ui, sans-serif',
        height: '100vh',
        display: 'flex',
        flexDirection: 'column',
      }}
    >
      <header
        style={{
          display: 'flex',
          gap: 8,
          padding: '8px 12px',
          borderBottom: '1px solid #eee',
          alignItems: 'center',
        }}
      >
        <strong style={{ marginRight: 16 }}>LowCode Studio</strong>
        <button onClick={() => setTab('workflow')} style={{ fontWeight: tab === 'workflow' ? 700 : 400 }}>
          工作流编排
        </button>
        <button onClick={() => setTab('page')} style={{ fontWeight: tab === 'page' ? 700 : 400 }}>
          页面搭建
        </button>
      </header>
      <div style={{ flex: 1, minHeight: 0 }}>
        {tab === 'workflow' ? <WorkflowCanvas /> : <PageBuilder />}
      </div>
    </div>
  );
}
