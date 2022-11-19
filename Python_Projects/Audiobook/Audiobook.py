import pyttsx3
import  PyPDF2
Book = open("Fundamentals Of Python Programming.pdf", 'rb')
PdfReader = PyPDF2.PdfFileReader(Book)
Pages = PdfReader.numPages
print(Pages)
#This program is for the audiobook for the pdf. It will read the content.
#Step1 - Install the speech library. Terminal - pip install pyttsx3
#Step2 - Initialize. here.
Reader = pyttsx3.init()
Page = PdfReader.getPage(12)
Text = Page.extractText()
voices = Reader.getProperty('voices')
Reader.setProperty('voice',voices[1].id)
Reader.say(Text)
Reader.runAndWait()
#Step3 - Test  speak.
#Step4 - Download the PDF file and search it here.
#Already downloaded the pdf.
#Step5 - Install PyPDF2
#Already downloaded PyPDF2.
#Step6 - Try to read one of the page

#Step7 - Change the voice
#Step8 - Use for loop to read the whole book.