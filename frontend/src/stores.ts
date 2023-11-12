import { writable } from "svelte/store";
import { type PDFFileStatus, type HeaderConfig } from "./lib/types";

export const fileId = writable<string>("");

export const headerConfig = writable<HeaderConfig>({
  bold: true,
  minFontSize: 16,
});

export const pdfFileStatus = writable<PDFFileStatus>({
  filename: "",
  nPages: 0,
  size: 0,
  last_accessed: 0,
  last_modified: 0,
  creation_time: 0,
});
