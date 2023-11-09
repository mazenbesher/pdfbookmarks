import { defineConfig, loadEnv } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

// https://vitejs.dev/config/
export default defineConfig(({ command, mode, ssrBuild }) => {
  // create default config object
  const config = {
    plugins: [svelte()],
    // dev server port
    server: {
      port: 5173,
    },
  };

  if (command === "serve") {
    return {
      // dev specific config
      ...config,
    };
  } else {
    // command === 'build'
    return {
      // build specific config
      ...config,
    };
  }
});
