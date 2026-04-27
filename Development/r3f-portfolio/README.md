# r3f-portfolio

React Three Fiber 3D 互動式作品集網站，包含動畫與互動功能。  
React Three Fiber portfolio with 3D visuals, animations, and interactive sections.

---

## 概述 | Overview

一個以 React、Vite 與 Three.js 建構的現代互動式作品集網站，具有自訂 3D 圖形、進階動畫與流暢的使用者體驗，並整合 dotLottie 動畫與響應式設計。  
A modern, interactive portfolio built with React, Vite, and Three.js, featuring custom 3D graphics, advanced animations, and a smooth user experience. This project showcases standard portfolio features plus unique, highly customized sections including dotLottie-powered animations and responsive design.

---

## 類別與狀態 | Category and Lifecycle

- **類別 | Category**：Development
- **類型 | Type**：Frontend | R3F | Portfolio
- **生命週期 | Lifecycle**：stable
- **標籤 | Tags**：frontend, react, three-fiber, portfolio

---

## 結構 | Structure

`/src` 主要目錄與檔案 | Key directories and files in `/src`:

- `App.jsx` / `main.jsx`：應用程式進入點與全域版面。Application entry point and global layout.
- `components/`：主要 React 元件，包含：Main React components including:
  - `Hero.jsx`：整合 3D/canvas、dotLottie 動畫與裝置感知版面的介紹區塊。Custom intro section with 3D/canvas, dotLottie animation, and device-aware layout.
  - `About.jsx`：帶有服務卡片、傾斜與動態效果的動畫介紹區塊。Animated about section with service cards and tilt/motion effects.
  - 其他作品集區塊（Contact、Projects 等）。Other portfolio sections (Contact, Projects, etc.).
- `assets/`：靜態圖片、3D 模型與 Lottie 動畫檔案。Static images, 3D models, and Lottie animation files.
- `constants/`：可重用常數的集中定義（例如服務列表）。Centralized definition of reusable constants.
- `utils/`：工具函式。Utility/helper functions.
- `styles.js` / `index.css`：共用與全域樣式。Shared and global styles.

---

## 如何執行 | How to Run

**前置需求 | Prerequisites**：Node.js（建議 v16+）、npm 或 yarn

```bash
git clone https://github.com/BiuwuLOK/react-3js-portfolio.git
cd react-3js-portfolio
npm install
npm run dev
```

應用程式預設在 `http://localhost:5173/` 啟動。  
The app will be available at `http://localhost:5173/` by default.

---

## 相依項目 | Dependencies

- React + Vite
- Three.js / React Three Fiber
- framer-motion（動態與傾斜效果 | motion and tilt effects）
- dotLottie（動畫整合 | animation integration）

---

## 輸出與展示 | Outputs and Demos

> Demo 影片（準備中）。Demo GIF (in preparation).

---

## 注意事項 | Notes and Limitations

- 自訂功能：於 `/src/components` 中新增或修改元件。Add/Edit Sections: Modify or create new components in `/src/components`.
- 動畫更換：將新的 dotLottie 檔案放至 `/src/assets` 並更新對應區塊。Place new dotLottie files in `/src/assets` and update the relevant sections.
- 內容更新：編輯 `constants/` 中的文字與資料。Edit text and data in `constants/`.

---

## 相關連結 | Related Links

- [Browse all components](https://github.com/BiuwuLOK/react-3js-portfolio/tree/main/src/components)
- [專案 Catalog | Project Catalog](../../catalog/index.md)
- [Repository 根目錄 | Repository Root](../../README.md)
