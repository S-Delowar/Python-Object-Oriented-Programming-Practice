# poly means many and morphism means forms.
#  So, polymorphism means various forms

# When some methods are declared multiple times in multiple classes for multiple purposes , then it is called polymorphism

class Document:
    def __init__(self, name):
        self.name = name
    def show(self):
        raise NotImplementedError("Subclass must implement abstruct nethod")

doc1 = Document('doc')
# doc1.show()

class Pdf(Document):
    def show(self):
        print('opening pdf file')

class Excel(Document):
    def show(self):
        print('opening Excel file')

class Word(Document):
    def show(self):
        print('opening word file')

pdf_file = Pdf('pdf_file')
excel_file = Excel('excel_file')
word_file = Word('word_file')

for file in [pdf_file, excel_file, word_file]:
    file.show()
