from PyPDF2 import PdfReader
import csv

# Get text from pdf
def get_text_pdf(pdf):
    # Read pdf 
    reader = PdfReader(pdf)
    # Get number of pages
    number_of_pages = len(reader.pages)
    text = ""
    for page_num in range(number_of_pages):
        page = reader.pages[page_num]
        text += page.extract_text()
        text = ' '.join(text.split())
    return text

# Save return text to csv file
def save_text_to_csv(text, output_csv):
    with open(output_csv, 'w',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Text'])
        writer.writerow([text])

# text  = get_text_pdf(pdf='Data Science.pdf')
# save_text_to_csv(text=text, output_csv='data_science.csv')

# Find most repeated word
def find_most_repeated_word(csv_file):
    with open(csv_file,'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header row
        text = next(reader)[0]
        words = text.split()
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        most_repeated_word = max(word_counts, key=word_counts.get)
        return most_repeated_word

repeats = find_most_repeated_word(csv_file='data_science.csv')
print(repeats) # 'the' is the most repeated word