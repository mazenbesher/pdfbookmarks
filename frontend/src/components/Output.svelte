<script lang="ts">
  import { fileId, headerConfig } from "../stores";
  import * as api from "../lib/api";

  const download = async () => {
    if (!$fileId) return;
    await api.downloadFile($fileId, $headerConfig);
  };
</script>

<main>
  <h2>Output</h2>

  <!-- Download button -->
  <button
    type="button"
    id="download"
    name="download"
    disabled={!$fileId || $fileId.length === 0}
    on:click={download}
  >
    Download
  </button>
</main>
