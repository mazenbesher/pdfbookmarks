# Getting started

Ensure you have `conda`, `tmux`, `make`, `git` and `bun` installed and then run:

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

- [ ] add status while downloading bookmarked pdf
- [ ] limit max of page selector to the number of pages in the pdf
- [ ] add option and preview for nested bookmarks
- [ ] save mapping to pdf file names to download file with original name + 'bookmarked'
- [ ] add docker support
- [ ] add tutorial
- [ ] support detecing multiline bookmark
