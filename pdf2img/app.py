# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('Airwings.pdf',1000,poppler_path='C:\Program Files\Poppler\bin')

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')
