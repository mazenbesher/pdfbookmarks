# Getting started

TODO

# Development

> **Warning**
> Tested only on my local machine! Feel free to open an issue if you have any problems.

Ensure you have `conda`, `tmux`, `make`, `git` and `bun` (or compatible cli tools) installed.

```bash
git clone git@github.com:mazenbesher/pdfbookmarks.git
cd pdfbookmarks
make setup dev
```

# Workflow

- upload pdf
- tweak parameters for header detection
- generate image of detected headers based on the passed parameters using `pdfplumber`
- commit to these parameters and generate annotated pdf with bookmarks for all pages using `pypdf`

# TODO

- [ ] add percentage status while downloading bookmarked pdf
- [ ] limit max of page selector to the number of pages in the pdf
- [ ] nested bookmarks support:
    - [ ] add option and preview for nested bookmarks
- [ ] save mapping to pdf file names to download file with original name + 'bookmarked'
- [ ] add docker support
- [ ] add tutorial
- [ ] support detecing multiline bookmark
