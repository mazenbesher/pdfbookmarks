import type { HeaderConfig, PDFFileStatus } from "./types";

// globals
const serverUrl: string = `http://${import.meta.env.BACKEND_HOST}:${
  import.meta.env.BACKEND_PORT
}`;

// upload file to server and return the file id
export const uploadFile = async (file: File): Promise<string> => {
  // create form data from input file
  const formData = new FormData();
  formData.append("file", file);

  // post input file to api and get the image
  const response = await fetch(`${serverUrl}/api/pdf/upload`, {
    method: "POST",
    body: formData,
  });
  return (await response.json())["file_id"];
};

export const getHeaderPreview = async (
  fileId: string,
  page: number,
  headerConfig: HeaderConfig
): Promise<string> => {
  // post input file to api and get the image
  const response = await fetch(`${serverUrl}/api/pdf/page/preview`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      file_id: fileId,
      page_number: page.toString(),
      header_config: {
        bold: headerConfig.bold,
        min_font_size: headerConfig.minFontSize,
      },
    }),
  });
  const imageBlob = await response.blob();
  return URL.createObjectURL(imageBlob);
};

export const downloadFile = async (
  fileId: string,
  headerConfig: HeaderConfig,
  filename: string
) => {
  const response = await fetch(`${serverUrl}/api/pdf/download/bookmarked`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      file_id: fileId,
      header_config: {
        bold: headerConfig.bold,
        min_font_size: headerConfig.minFontSize,
      },
    }),
  });
  const blob = await response.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename.replace(".pdf", "_bookmarked.pdf");
  a.click();
  URL.revokeObjectURL(url);
};

export const getFileStatus = async (fileId: string): Promise<PDFFileStatus> => {
  const response = await fetch(`${serverUrl}/api/pdf/status/${fileId}`);
  const status = await response.json();
  return {
    filename: status["filename"],
    nPages: status["n_pages"],
    size: status["size"],
    lastAccessed: status["last_accessed"],
    lastModified: status["last_modified"],
    creationTime: status["creation_time"],
  };
};
