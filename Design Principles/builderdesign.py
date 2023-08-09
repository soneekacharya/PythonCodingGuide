"""  Design a document generator using the Builder Design Pattern. Create a DocumentBuilder that creates documents of various types 
(e.g., PDF, HTML, Plain Text). Implement the builder methods to format the document content and structure according to the chosen type. 
Demonstrate how the Builder Design Pattern allows for the creation of different document formats without tightly coupling the
document generation logic. """

from abc import ABC, abstractmethod

class DocumentBuilder(ABC):
    @abstractmethod
    def add_title(self, title):
        pass

    @abstractmethod
    def add_content(self, content):
        pass

    @abstractmethod
    def get_document(self):
        pass

class PlainTextDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = ""

    def add_title(self, title):
        self.document += f"Title: {title}\n"

    def add_content(self, content):
        self.document += f"Content: {content}\n"

    def get_document(self):
        return self.document

class HTMLDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = ""

class PDFDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = ""

class DocumentGenerator:
    def __init__(self, builder):
        self.builder = builder

    def generate_document(self):
        self.builder.add_title("Plain Document")
        self.builder.add_content("This is the content of plain document.")
        return self.builder.get_document()

def main():
    builder_type = input("Enter builder type (plain/html/pdf): ")
    if builder_type == "plain":
        builder = PlainTextDocumentBuilder()
    elif builder_type == "html":
        builder = HTMLDocumentBuilder()
    elif builder_type == "pdf":
        builder = PDFDocumentBuilder()
    else:
        raise ValueError("Invalid builder type!")

    generator = DocumentGenerator(builder)
    document = generator.generate_document()
    print(document)

if __name__ == "__main__":
    main()
