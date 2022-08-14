import abc

class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document():
        pass
    
    @abc.abstractmethod
    def get_scanner_status():
        pass

class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document():
        pass
    
    @abc.abstractmethod
    def get_printer_status():
        pass

class MFD1(Scanner, Printer):
    def __init__(self, resol, sn):
        self.max_resolution = resol
        self.serial_number = sn
    
    def scan_document(self):
        print("Cheap scanner")
        return "The document has been scanned."
        
    def get_scanner_status(self):
        print("Low resolution scanner")
        return f"Max. resolution: {self.max_resolution}, Serial Number: {self.serial_number}"
    
    def print_document(self):
        print("Cheap printer.")
        return "The document has been printed."
    
    def get_printer_status(self):
        print("Low resolution printer.")
        return f"Max. resolution: {self.max_resolution}, Serial Number: {self.serial_number}"

class MFD2(Scanner, Printer):
    def __init__(self, resol, sn):
        self.max_resolution = resol
        self.serial_number = sn
    
    def scan_document(self):
        print("Medium-priced scanner")
        return "The document has been scanned."
        
    def get_scanner_status(self):
        print("Medium resolution scanner.")
        return f"Max. resolution: {self.max_resolution}, Serial Number: {self.serial_number}"
    
    def print_document(self):
        print("Medium-priced printer.")
        return "The document has been printed."
    
    def get_printer_status(self):
        print("Medium resolution printer")
        return f"Max. resolution: {self.max_resolution}, Serial Number: {self.serial_number}"


class MFD3(Scanner, Printer):
    def __init__(self, resol, sn):
        self.max_resolution = resol
        self.serial_number = sn
    
    def scan_document(self):
        print("Premium scanner.")
        return "The document has been scanned."
        
    def get_scanner_status(self):
        print("High resolution scanner.")
        return f"Max. resolution: {self.max_resolution}, Serial Number: {self.serial_number}"
    
    def print_document(self):
        print("Premium printer.")
        return "The document has been printed."
    
    def get_printer_status(self):
        print("High resolution printer.")
        return f"Max. resolution: {self.max_resolution}, Serial Number: {self.serial_number}"

mdf1 = MFD1(360, 12345)
mdf2 = MFD2(720, 123456)
mdf3 = MFD3(1048, 1234567)
