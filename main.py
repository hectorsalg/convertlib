from convertlib import convertlib as cv

path = './teste.pdf'

converter = cv.convertlib(path)
converter.docx2png()