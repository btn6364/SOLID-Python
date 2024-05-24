from abc import ABC, abstractmethod

class Print(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scan(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Print):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class ModernPrinter(Print, Fax, Scan):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


old_printer = OldPrinter() 
old_printer.print("document 1")
old_printer.fax("document 1")

modern_printer = ModernPrinter()
modern_printer.print("document 2")
modern_printer.fax("document 2")
modern_printer.scan("document 2")