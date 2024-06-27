import pyttsx3
import PyPDF2

pdfreader = PyPDF2.PdfFileReader(open("awad.pdf", "rb"))
speaker = pyttsx3.init()

for page_num in range (pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', '')
    print(clean_text)


speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

# speaker.stop()


# import pyttsx3
# import PyPDF2

# # Open the PDF file
# pdf_file = open("awad.pdf", "rb")
# pdfreader = PyPDF2.PdfFileReader(pdf_file)

# # Initialize the TTS engine
# speaker = pyttsx3.init()

# # Initialize an empty string for the text
# full_text = ""

# # Loop through all the pages and extract text
# for page_num in range(pdfreader.numPages):
#     text = pdfreader.getPage(page_num).extractText()
#     clean_text = text.strip().replace('\n', '')
#     full_text += clean_text + " "

# # Save the full text to an audio file
# speaker.save_to_file(full_text, 'story.mp3')
# speaker.runAndWait()

# # Stop the TTS engine
# speaker.stop()

# # Close the PDF file
# pdf_file.close()
