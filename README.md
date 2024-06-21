# PDF Merger Script

This is a Python script for merging multiple PDF files into a single PDF.

## Requirements

- Python 3.x
- `PyPDF2` library

## Installation

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Install the `PyPDF2` library using pip:

    ```bash
    pip install PyPDF2
    ```

## Usage

1. Place the PDF files you want to merge in the same directory as the script, or provide the full path to each file in the `pdfs_to_merge` list.

2. Edit the `pdfs_to_merge` list in the script to include the paths to your PDF files:

    ```python
    pdfs_to_merge = ["file1.pdf", "file2.pdf", "file3.pdf"]
    ```

3. Run the script:

    ```bash
    python merge_pdfs.py
    ```

4. The merged PDF will be saved as `merged_output.pdf` in the same directory.

## Thanks for Reading!!
