export default [
  {
    files: ["**/*.js"],
    ignores: ["node_modules/"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        console: "readonly", // Define console as a global variable
        window: "readonly",
        document: "readonly",
      },
    },
    rules: {
      "no-undef": "error",
      "no-unused-vars": "error",
      "eqeqeq": "error",
      "semi": ["error", "always"],
      "quotes": ["error", "double"]
    },
  },
];
