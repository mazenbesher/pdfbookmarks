<script lang="ts">
  import * as api from "../lib/api";
  import { headerConfig, fileId, pdfFileStatus } from "../stores";

  // state
  let loading: boolean = false;

  // preview options
  let pageToPreview: number = 1;
  let previewImgSrc: string = "";

  // when preview button is clicked
  export const preview = async () => {
    if (!$fileId) return;

    loading = true;
    previewImgSrc = await api.getHeaderPreview(
      $fileId,
      pageToPreview,
      $headerConfig
    );
    loading = false;
  };

  // call preview if header config changes
  $: $headerConfig && preview();
</script>

<main>
  <h2>Preview Options</h2>

  <!-- Page to preview -->
  <!-- TODO: max -->
  <label for="pagesToPreview"
    >Page to preview:
    <input
      type="number"
      id="pagesToPreview"
      name="pagesToPreview"
      min="1"
      bind:value={pageToPreview}
    />
  </label>

  <!-- Preview buttons -->
  <div>
    <!-- Preview selected page -->
    <button
      type="button"
      id="preview"
      name="preview"
      disabled={!$fileId || $fileId.length === 0}
      on:click={preview}
    >
      Preview
    </button>

    <!-- Preview previous page -->
    <button
      type="button"
      id="previewPrev"
      name="previewPrev"
      disabled={!$fileId || $fileId.length === 0 || pageToPreview === 1}
      on:click={() => {
        pageToPreview--;
        preview();
      }}
    >
      Previous
    </button>

    <!-- Preview next page -->
    <button
      type="button"
      id="previewNext"
      name="previewNext"
      disabled={!$fileId || $fileId.length === 0 || pageToPreview === $pdfFileStatus.nPages}
      on:click={() => {
        pageToPreview++;
        preview();
      }}
    >
      Next
    </button>
  </div>

  <!-- Preview image -->
  {#if previewImgSrc && !loading}
    <div>
      <img src={previewImgSrc} alt="Preview" />
    </div>
  {:else if loading}
    <div>Loading...</div>
  {:else}
    <div>No preview available</div>
  {/if}
</main>
