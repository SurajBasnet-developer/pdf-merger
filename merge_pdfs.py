import PyPDF2
import os

def merge_pdfs(pdf_list, output_path):
    """
    Merge multiple PDF files into one.

    Parameters:
    pdf_list (list of str): List of paths to the PDF files to be merged.
    output_path (str): Path to the output merged PDF file.
    """
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        pdf_merger.append(pdf)

    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == "__main__":
    # Example usage
    pdfs_to_merge = ["7.pdf", "unit-7.pdf"]
    output_pdf_path = "merged_output.pdf"
    
    # Check if files exist
    for pdf in pdfs_to_merge:
        if not os.path.isfile(pdf):
            print(f"File {pdf} does not exist.")
            exit(1)

    merge_pdfs(pdfs_to_merge, output_pdf_path)
    print(f"Merged PDF saved to {output_pdf_path}")
