import pyttsx3
import  PyPDF2
Book = open("Fundamentals Of Python Programming.pdf", 'rb')
PdfReader = PyPDF2.PdfFileReader(Book)
Pages = PdfReader.numPages
#This program is for the audiobook for the pdf. It will read the content.
#Step1 - Install the speech library. Terminal - pip install pyttsx3
#Step2 - Initialize. here.
Reader = pyttsx3.init()
#Step3 - Test  speak.
#Step4 - Download the PDF file and search it here.
#Already downloaded the pdf.
#Step5 - Install PyPDF2.
#Already downloaded PyPDF2.
#Step6 - Try to read one of the page
#Step7 - Change the voice.
voices = Reader.getProperty('voices')
print("=======================================")
print("What voice do you want to read the book?")
print("=======================================")
print("M - Male \n", "F- Female" )
print("=======================================")
Change = str(input("Type here your choices:  ")).lower()
print("=======================================")
while Change != 'm' or Change != 'f':
    Change = str(input("Type here your choices ")).lower()
    print("=======================================")
    if Change == 'm':
        index = 0
        Reader.setProperty('voice',voices[index].id) #Change the index to 1 for female voice.
        break
    elif Change == 'f':
        index = 1
        Reader.setProperty('voice', voices[index].id)  # Change the index to 1 for female voice.
        break
print()
print()
Start = int(input("Enter the Page that you wanna read? ")) - 1
#Step8 - Use for loop to read the whole book.
for i in range(Start,Pages):
    Page = PdfReader.getPage(i)
    Text = Page.extractText()
    Reader.say(Text)
    Reader.runAndWait()