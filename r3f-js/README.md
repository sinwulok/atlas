---

# React 3JS Portfolio

A modern, interactive portfolio built with **React**, **Vite**, and **Three.js**, featuring custom 3D graphics, advanced animations, and a smooth user experience. This project showcases not only standard portfolio features but also unique, highly customized sections, including dotLottie-powered animations and responsive design.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Core Implementation](#core-implementation)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- ✨ **Custom 3D Graphics**: Built with Three.js for visually stunning effects.
- 🖼️ **dotLottie Animations**: Unique animated elements in Hero and About sections, going beyond typical templates.
- 🎨 **Responsive Design**: Tailored layouts for desktop, tablet, and mobile.
- ⚡ **Vite-Powered Dev Experience**: Lightning-fast hot reloads and build times.
- 🧩 **Modular Components**: Clean separation of logic, presentation, and assets.
- 🌐 **Modern Styling**: Uses CSS modules and JS-based styles for flexibility.
- 💎 **Smooth Transitions**: Advanced motion and tilt effects in service cards and text sections.

---

## Demo

> (Waitting the .gif)

---

## Getting Started

### Prerequisites

- Node.js (v16+ recommended)
- npm or yarn

### Installation

```bash
git clone https://github.com/BiuwuLOK/react-3js-portfolio.git
cd react-3js-portfolio
npm install
# or
yarn install
```

### Running Locally

```bash
npm run dev
# or
yarn dev
```

The app will be available at `http://localhost:5173/` by default.

---

## Project Structure

Key directories and files in `/src`:

- `App.jsx` / `main.jsx`: Application entry point and global layout.
- `components/`: Main React components including:
  - `Hero.jsx`: Custom intro section with 3D/canvas, dotLottie animation, and device-aware layout.
  - `About.jsx`: Animated about section with service cards and tilt/motion effects.
  - `...`: Other portfolio sections (Contact, Projects, etc.).
- `assets/`: Static images, 3D models, and Lottie animation files.
- `constants/`: Centralized definition of reusable constants (e.g., service list).
- `utils/`: Utility/helper functions.
- `styles.js` / `index.css`: Shared and global styles.

[Browse all components here.](https://github.com/BiuwuLOK/react-3js-portfolio/tree/main/src/components)

---

## Core Implementation

### Hero Section

- Custom React component with:
  - Responsive layout using device detection.
  - 3D/animated elements via Three.js or Lottie.
  - dotLottie integration for rich, lightweight animations.
  - Custom icons and interactive canvas.

### About Section

- Animated service/skills cards using motion and tilt (framer-motion).
- dotLottie or similar animation for section intro.
- Modular, reusable card components.
- Smooth entry/exit transitions and hover effects.

---

## Customization

- **Add/Edit Sections**: Modify or create new components in `/src/components`.
- **Change Animations**: Place new dotLottie files in `/src/assets` and update the relevant sections.
- **Update Content**: Edit text and data in `constants/` or directly in the component files.
- **Styling**: Adjust styles in `styles.js` and CSS modules as needed.

---

## Contributing

Pull requests and stars are always welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## License

[MIT](LICENSE)

---
