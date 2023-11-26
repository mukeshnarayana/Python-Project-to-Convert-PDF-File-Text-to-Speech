import pyttsx3
import PyPDF2
book = open('CD.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)
speaker = pyttsx3.init()
for num in range(10,pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
