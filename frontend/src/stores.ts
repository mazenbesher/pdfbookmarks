import { writable } from "svelte/store";
import type { HeaderConfig } from "./lib/types";

export const fileId = writable<string>("");

export const headerConfig = writable<HeaderConfig>({
  bold: true,
  minFontSize: 16,
});
