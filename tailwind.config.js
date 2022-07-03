module.exports = {
  content: ["./templates/**/*.{html,js,css}"],
  important: true,
    theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["garden"],
  },
}
