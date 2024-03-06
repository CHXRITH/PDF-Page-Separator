import PyPDF2
import tkinter as tk
from tkinter import filedialog
import os

class PDFSeparatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Page Separator | CHXRITH")

        self.label = tk.Label(master, text="Select a PDF file to separate pages:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select PDF", command=self.select_pdf)
        self.select_button.pack()

    def select_pdf(self):
        pdf_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_file:
            self.separate_pdf_pages(pdf_file)

    def separate_pdf_pages(self, pdf_file):
        # Open the PDF file
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            # Iterate through each page
            for page_num in range(len(reader.pages)):
                # Create a new PDF writer for each page
                writer = PyPDF2.PdfWriter()
                writer.add_page(reader.pages[page_num])

                # Output file name
                output_filename = f"{os.path.splitext(pdf_file)[0]}_page_{page_num + 1}.pdf"

                # Write the page to a new PDF file
                with open(output_filename, 'wb') as output_file:
                    writer.write(output_file)

                print(f"Page {page_num + 1} extracted and saved as {output_filename}")

                # Show success message
                tk.messagebox.showinfo("Success", f"Page {page_num + 1} extracted and saved as {output_filename}")

def main():
    root = tk.Tk()
    app = PDFSeparatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
