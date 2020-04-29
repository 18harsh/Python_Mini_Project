import pyttsx3
import PyPDF2
import keyboard

def extract_text(filename):
	pdf_file = open(filename,"rb")
	pdf_read = PyPDF2.PdfFileReader(pdf_file)
	text=""
	for page in range(pdf_read.getNumPages()):
		pdf_page=pdf_read.getPage(page)
		print(pdf_page.extractText()[0:100])
		text+=pdf_page.extractText() 
		
	return text[0:100]	
def speak(text):
	engine = pyttsx3.init()
	engine.setProperty('rate', 1500)
	engine.setProperty('voice', 'en+m7')
	engine.say(text)
	engine.runAndWait()		

if __name__ =="__main__":
	text = extract_text("C:\\Users\\harsh\\Desktop\\code\\10 python project\\Pdf Voice  Reader\\code11.pdf")
	speak(text)


# speak("knock knock!")
# speak("who's there?")
# speak("thank!")
# speak("thank who")
# speak("you're welcome")
