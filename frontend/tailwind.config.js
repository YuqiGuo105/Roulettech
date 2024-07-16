/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        blue: {
          10: '#58B2DC'
        },
        red: {
          10: '#B481BB'
        },
        purple: {
          10: '#9B90C2',
          20: '#B28FCE'
        }
      }
    },
  },
  plugins: [],
}