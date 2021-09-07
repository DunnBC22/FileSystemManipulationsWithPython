from PyPDF3 import PdfFileMerger
import os
from os import listdir
from tkinter.filedialog import *

# The program appends a single PDF to the end of a list of other individual PDFs


def main():
    folder_location = askdirectory(
        title="What folder of PDF files do you want to append a single PDF to:")

    print("File path to the docx files folder: ", folder_location)
    os.chdir(folder_location)

    PDF_to_merge = askopenfilename(
        title="Please select the PDF to append to the list of files:")

    # select all of the PDF files only
    pdf_only = r'.pdf'
    list_of_files = [x for x in listdir(os.getcwd()) if x.endswith(pdf_only)]

    # Loop to append the file to the end of each of the pdf's in the folder
    for i in range(len(list_of_files)):
        pdf_appender = PdfFileMerger()
        FileInput = open(list_of_files[i], 'rb')
        PDF_Input = open(PDF_to_merge, 'rb')
        pdf_appender.append(FileInput)
        pdf_appender.append(PDF_Input)
        output = open(list_of_files[i], 'wb')
        pdf_appender.write(output)


if __name__ == '__main__':
    main()
    quit()
