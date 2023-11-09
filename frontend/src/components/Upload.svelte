<script lang="ts">
  import * as api from "../lib/api";
  import { fileId } from "../stores";

  let inputFiles: FileList | null = null;

  const onUpload = async () => {
    if (!inputFiles) return;
    if (inputFiles.length > 1) return;
    $fileId = await api.uploadFile(inputFiles[0]);
  };
</script>

<main>
  <h2>File Configurations</h2>

  <!-- Input path -->
  <label for="inputPath"
    >Input path:
    <input
      type="file"
      id="inputPath"
      name="inputPath"
      accept="application/pdf"
      bind:files={inputFiles}
    />

    <!-- Upload button -->
    <button
      type="button"
      id="upload"
      name="upload"
      disabled={!inputFiles || inputFiles.length > 1}
      on:click={onUpload}>Upload</button
    >
  </label>
</main>
