import pyttsx3
import PyPDF2

book = open('Paulo Coelho - The Alchemist (1993).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)
newVoiceRate = 145
speaker.setProperty('rate', newVoiceRate)
for num in range(pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
