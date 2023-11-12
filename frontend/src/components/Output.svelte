<script lang="ts">
  import { fileId, headerConfig, pdfFileStatus } from "../stores";
  import * as api from "../lib/api";

  let creatingBookmarks = false;
  let bookmarkedFileReady = false;

  const createBookmarks = async () => {
    if (!$fileId) return;
    creatingBookmarks = true;
    await api.createBookmarks($fileId, $headerConfig, $pdfFileStatus.filename);

    // create a timer to check status every second
    const timer = setInterval(async () => {
      const ready = await api.getBookmarksStatus($fileId);
      if (ready) {
        clearInterval(timer);
        creatingBookmarks = false;
        bookmarkedFileReady = true;
      }
    }, 1000);
  };
</script>

<main>
  <h2>Output</h2>

  <!-- Create bookmarks button -->
  {#if $fileId && $fileId.length > 0}
    <button
      type="button"
      id="createBookmakrs"
      name="createBookmakrs"
      disabled={!$fileId || $fileId.length === 0 || creatingBookmarks}
      on:click={createBookmarks}
    >
      Create Bookmarks
    </button>
  {/if}

  <!-- Download file button -->
  {#if $fileId && $fileId.length > 0 && bookmarkedFileReady}
    <button
      type="button"
      id="downloadFile"
      name="downloadFile"
      disabled={!$fileId || $fileId.length === 0 || creatingBookmarks}
      on:click={async () => {
        await api.downloadBookmarkedFile($fileId, $pdfFileStatus.filename);
      }}
    >
      Download File
    </button>
  {/if}
</main>
