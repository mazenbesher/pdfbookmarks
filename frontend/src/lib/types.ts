// TODO: parity with backend

export interface HeaderConfig {
  bold: boolean;
  minFontSize: number;
}

// TODO: error handling!
export interface PDFFileStatus {
  filename: string;
  nPages: number;
  size: number;
  lastAccessed: number;
  lastModified: number;
  creationTime: number;
}
