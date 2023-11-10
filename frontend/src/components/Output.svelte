<script lang="ts">
  import { fileId, headerConfig } from "../stores";
  import * as api from "../lib/api";

  let downloading: boolean = false;

  const download = async () => {
    if (!$fileId) return;
    downloading = true;
    await api.downloadFile($fileId, $headerConfig);
    downloading = false;
  };
</script>

<main>
  <h2>Output</h2>

  <!-- Show download button if downloading otherwise show processing message -->
  {#if downloading}
    <p>Processing...</p>
  {:else if $fileId && $fileId.length > 0}
    <!-- Download button -->
    <button
      type="button"
      id="download"
      name="download"
      disabled={!$fileId || $fileId.length === 0 || downloading}
      on:click={download}
    >
      Download
    </button>
  {:else}
    <p>Upload a file to get started</p>
  {/if}
</main>
