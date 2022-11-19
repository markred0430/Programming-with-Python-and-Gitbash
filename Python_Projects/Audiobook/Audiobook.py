import pyttsx3
#This program is for the audiobook for the pdf. It will read the content.
#Step1 - Install the speech library. Terminal - pip install pyttsx3
#Step2 - Initialize. here.
Reader = pyttsx3.init()
#Step3 - Test  speak.
Reader.say("Hello World")
Reader.runAndWait()
#Step4 - Download the PDF file and search it here.

#Step5 - Install PyPDF2
#Step6 - Try to read one of the page
#Step7 - Change the voice
#Step8 - Use for loop to read the whole book.