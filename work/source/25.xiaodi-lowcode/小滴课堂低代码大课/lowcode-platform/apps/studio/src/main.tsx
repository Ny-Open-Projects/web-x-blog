import React from 'react';
import { createRoot } from 'react-dom/client';
import { ReactFlowProvider } from 'reactflow';
import 'reactflow/dist/style.css';
import { App } from './App';

createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <ReactFlowProvider>
      <App />
    </ReactFlowProvider>
  </React.StrictMode>,
);
