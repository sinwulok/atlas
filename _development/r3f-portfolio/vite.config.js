import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import mdx from "@mdx-js/rollup";

export default defineConfig({
  plugins: [
    { enforce: "pre", ...mdx() },
    react({ include: /\.(mdx|js|jsx|ts|tsx)$/ }),
  ],
  assetsInclude: ["**/*.lottie"], // Ensure .lottie files are treated as assets
  build: {
    // sourcemap: true, // 禁用 Source Map 生成
  },
});
