<script lang="ts">
  import { onMount } from "svelte";
  import Preview from "./Preview.svelte";
  import Upload from "./Upload.svelte";
  import HeaderConf from "./HeaderConf.svelte";
  import Output from "./Output.svelte";

  onMount(async () => {
    // set page tile
    document.title = "PDF Bookmarks Generator";

    // prepend DEV to title if in development mode
    if (import.meta.env.DEV) {
      document.title = "DEV - " + document.title;
    }
  });
</script>

<main>
  <Upload />
  <HeaderConf />
  <Output />
  <Preview />
</main>

<style>
</style>
