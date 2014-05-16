from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input = PdfFileReader(file("c:/scripts/2013 BCAC Membership Directory.pdf", "rb"))

for i in range(7,16,1):
	output.addPage(input.getPage(i))

outputStream = file("list.pdf", "wb")
output.write(outputStream)
outputStream.close()