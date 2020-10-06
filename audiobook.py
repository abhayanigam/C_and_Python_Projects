import pyttsx3
import PyPDF2
book = open('Python Crash Course_ A Hands-On, Project-Based Introduction to Programming ( PDFDrive.com ).pdf', 'rb')
#to read a pdf.
pdfReader = PyPDF2.PdfFileReader(book)

#to know how many pages are thier in a book.
pages = pdfReader.numPages
print(pages)

#to speak.
speaker = pyttsx3.init()

for num in range(28, pages):

    #To read only one page.
    #page = pdfReader.getPage(28)

    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

""""
step 1:- To make over code talking we have to install (pip install pyttsx3) fullform :- python text to speach version 3
step 2:- to test make a simple code
    example:
            import pyttsx3
            speaker = pyttsx3.init() #to intialize this:
            speaker.say('hey i can talk')
            speaker.runAndWait()
step 3:- save the pdf in the same folder
step 4:- To read over pdf install (pip insatll PyPDF2)
"""