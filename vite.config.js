import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8001',  // 你的 FastAPI 后端地址
        changeOrigin: true,               // 更改请求源，避免跨域问题
        rewrite: (path) => path.replace(/^\/api/, '')  // 去掉 /api 前缀
      }
    }
  }
})
