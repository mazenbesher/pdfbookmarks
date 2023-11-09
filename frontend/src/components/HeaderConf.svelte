<script lang="ts">
  import { headerConfig } from "../stores";
</script>

<main>
  <h2>Header Configurations</h2>

  <!-- Are headers bold? -->
  <label for="bold"
    >Are headers bold?
    <input
      type="checkbox"
      id="bold"
      name="bold"
      value="bold"
      bind:checked={$headerConfig.bold}
    />
  </label>

  <!-- Minimum font size -->
  <label for="minFontSize"
    >Minimum font size:
    <input
      type="number"
      id="minFontSize"
      name="minFontSize"
      min="0"
      max="100"
      step="1"
      bind:value={$headerConfig.minFontSize}
    />
  </label>
</main>
