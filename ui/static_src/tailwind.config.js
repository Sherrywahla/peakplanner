const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  darkMode: 'class',
  content: [
    '../templates/**/*.html',
    '../../templates/**/*.html',
    '../../**/templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#ecfdf5',
          100: '#d1fae5',
          200: '#a7f3d0',
          300: '#6ee7b7',
          400: '#34d399',
          500: '#10b981',
          600: '#059669',
          700: '#047857',
          800: '#065f46',
          900: '#064e3b',
          950: '#022c22'
        }
      }
    },
    fontFamily: {
      body: [
        'Source Sans Pro',
        ...defaultTheme.fontFamily.sans
      // 'ui-sans-serif',
      // 'system-ui',
      // '-apple-system',
      // 'system-ui',
      // 'Segoe UI',
      // 'Roboto',
      // 'Helvetica Neue',
      // 'Arial',
      // 'Noto Sans',
      // 'sans-serif',
      // 'Apple Color Emoji',
      // 'Segoe UI Emoji',
      // 'Segoe UI Symbol',
      // 'Noto Color Emoji'
      ],
      sans: [
        'Source Sans Pro',
        ...defaultTheme.fontFamily.sans
      // 'ui-sans-serif',
      // 'system-ui',
      // '-apple-system',
      // 'system-ui',
      // 'Segoe UI',
      // 'Roboto',
      // 'Helvetica Neue',
      // 'Arial',
      // 'Noto Sans',
      // 'sans-serif',
      // 'Apple Color Emoji',
      // 'Segoe UI Emoji',
      // 'Segoe UI Symbol',
      // 'Noto Color Emoji'
      ]
    },
    plugins: [
      require('@tailwindcss/forms'),
      require('@tailwindcss/typography'),
      require('@tailwindcss/line-clamp'),
      require('@tailwindcss/aspect-ratio'),
      require('flowbite/plugin')
    ]
  }
};
