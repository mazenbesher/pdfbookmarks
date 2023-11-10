import path from "path";
import { defineConfig, loadEnv } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

// https://vitejs.dev/config/
export default defineConfig(({ command, mode, ssrBuild }) => {
  // load .env file in parent directory using loadEnv()
  const env = loadEnv(mode, path.dirname(process.cwd()), '');

  // create default config object
  const config = {
    plugins: [
      svelte(),
    ],
    // pass env variables to client
    define: {
      'import.meta.env.BACKEND_URL': JSON.stringify(env.BACKEND_URL),
      'import.meta.env.BACKEND_PORT': JSON.stringify(env.BACKEND_PORT),
    }
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
