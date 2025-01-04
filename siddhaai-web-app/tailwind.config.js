/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["node_modules/preline/dist/*.js"],
  darkMode: "class",
  extends: {
  
  },
  theme:{
    extend:{
      fontFamily:{
        sans: ["Montserrat","sans-serif"],
      }
    }
  },
  plugins: [
    require("preline/plugin"),
    require("prettier-plugin-tailwindcss"),
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
  ],
};
