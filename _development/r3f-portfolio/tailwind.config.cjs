// tailwind does not build-in some css in current version
// custom modules
/* 
  boxShadow,
  screens,
  backgroundImage,
  textShadow,
*/

/** @type {import('tailwindcss').Config} */
const plugin = require("tailwindcss/plugin");

module.exports = {
  content: ["./src/**/*.{js,jsx}"],
  mode: "jit",
  theme: {
    extend: {
      colors: {
        primary: "#050816",
        secondary: "#aaa6c3",
        tertiary: "#151030",
        "black-100": "#100d25",
        "black-200": "#090325",
        "white-100": "#f3f3f3",
      },
      borderColor: (theme) => ({
        ...theme("colors"), // inhert all colors from theme
      }),
      backgroundImage: {
        "hero-pattern": "url('/src/assets/herobg.png')",
      },
      boxShadow: {
        card: "0px 35px 120px -15px #211e35",
      },
      screens: {
        xs: "450px",
      },

      textShadow: {
        sm: "0 1px 2px rgba(0, 0, 0, 0.5)",
        DEFAULT: "0 2px 4px rgba(0, 0, 0, 0.5)",
        lg: "2px 4px 8px rgba(0, 0, 0, 0.7)",
      },
    },
  },
  plugins: [
    plugin(function ({ matchUtilities, theme }) {
      matchUtilities(
        {
          "text-shadow": (value) => ({
            textShadow: value,
          }),
        },
        { values: theme("textShadow") }
      );
    }),
    function ({ addUtilities }) {
      addUtilities({
        ".preserve-3d": {
          "transform-style": "preserve-3d",
        },
      });
    },
  ],
};
