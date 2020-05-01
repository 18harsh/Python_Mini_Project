# merge PDF's without Adobe

import PyPDF2

#def to open a file
def load_pdf(filename):
    f = open(filename, 'rb')
    return PyPDF2.PdfFileReader(f)

def add_to_writer(pdf,writer,start,end):
    for i in range(start-1, end):
        writer.addPage(pdf.getPage(i))
    

print ("Welcome to the pdf merger.")

filename1= input("Please type the filename of the first file: ")
filename2= input("Please type the filename of the second file: ")


pdf1= load_pdf(filename1)
pdf2= load_pdf(filename2)

#get the number of pages
pdf1_pages= pdf1.getNumPages()
pdf2_pages= pdf2.getNumPages()

print("{} has {} pages.".format(filename1,pdf1_pages))
start1= int(input("Start on page: "))
end1= int(input("End on page: "))

print("{} has {} pages.".format(filename2,pdf2_pages))
start2= int(input("Start on page: "))
end2= int(input("End on page: "))

output_filename=input("Save the file as: ")


output_file = open(output_filename,'wb')
#creating document writer object
writer= PyPDF2.PdfFileWriter()

add_to_writer(pdf1,writer,start1, end1)
add_to_writer(pdf2, writer,start2, end2)


writer.write(output_file)

output_file.close()

