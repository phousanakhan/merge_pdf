
import PyPDF4 
from PyPDF4 import PdfFileMerger

pdfs = []
done = False
while not done:
    user_input = input("Enter pdf file name you want to merge OR type 'done' when you're done: ")
    if user_input == "done":
        done = True
    else:
        pdfs.append(user_input + ".pdf")

newMergedPdf = input("Enter the new pdf name: ") 
newMergedPdf += ".pdf"

merge_pdfs = PyPDF4.PdfFileMerger()
for pdf in pdfs:
    merge_pdfs.append(open(pdf, 'rb'))
merge_pdfs.write(open(newMergedPdf, 'wb'))