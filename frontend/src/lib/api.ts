import type { HeaderConfig } from "./types";

// globals
const serverUrl: string = "http://localhost:9113"; // TODO: get port from .env

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
  const response = await fetch(`${serverUrl}/api/pdf/preview/headers`, {
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

export const downloadFile = async (fileId: string, headerConfig: HeaderConfig) => {
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
  a.download = "bookmarked.pdf";
  a.click();
  URL.revokeObjectURL(url);
};
