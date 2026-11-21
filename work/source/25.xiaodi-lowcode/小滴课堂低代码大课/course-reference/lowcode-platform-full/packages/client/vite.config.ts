import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "node:path";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "~": resolve(__dirname, "src"),
    },
  },
  build: {
    // 性能优化:按依赖域拆 chunk,避免单个 3MB+ 大包
    // (antd + react 生态 + echarts 各自独立缓存,业务代码改动不失效 vendor 缓存)
    rollupOptions: {
      output: {
        manualChunks: {
          "vendor-react": ["react", "react-dom", "react-router-dom"],
          "vendor-antd": ["antd", "@ant-design/icons"],
          "vendor-charts": ["echarts", "echarts-for-react"],
          "vendor-editor": ["@dnd-kit/core", "@dnd-kit/sortable", "@dnd-kit/utilities", "mobx", "mobx-react-lite"],
        },
      },
    },
  },
});
