module.exports = {
  content: ["./templates/**/*.{html,js}"],
  daisyui: {
    themes: [
      {
        stanforteedge: {
          primary: "#033B89",
          secondary: "#CE0101",
          accent: "#37cdbe",
          neutral: "#0f172a",
          "base-100": "#f8fafc",
          "base-200": "#f4f5f7",
          "base-300": "#e5e7eb",

          "--rounded-box": "0rem", // border radius rounded-box utility class, used in card and other large boxes
          "--rounded-btn": "0.3rem", // border radius rounded-btn utility class, used in buttons and similar element
          "--rounded-badge": "1.9rem", // border radius rounded-badge utility class, used in badges and similar
          "--animation-btn": "0.25s", // duration of animation when you click on button
          "--animation-input": "0.2s", // duration of animation for inputs like checkbox, toggle, radio, etc
          "--btn-text-case": "uppercase", // set default text transform for buttons
          "--btn-focus-scale": "0.95", // scale transform of button when you focus on it
          "--border-btn": "1px", // border width of buttons
          "--tab-border": "1px", // border width of tabs
          "--tab-radius": "0.5rem", // border radius of tabs
        },
      },
    ],
  },
  theme: {
    screens: {
      sm: "480px",
      md: "768px",
      lg: "976px",
      xl: "1440px",
    },

    extends: {
     
    },
    
  },

  // daisyUI config (optional)
  plugins: [require("@tailwindcss/line-clamp"), require("daisyui")],
};
