from pathlib import Path
from utils.file_manager import FileManager

BASE_DIR = Path(__file__).resolve().parent.parent

class Persistence:
    def __init__(self):
        self.path_sent = BASE_DIR / "patents_ids" / "ids_sent.txt"
        self.path_not_sent = BASE_DIR / "patents_ids" / "ids_not_sent.txt"
        
        self.path_sent.parent.mkdir(parents=True, exist_ok=True)

        self.path_sent.touch(exist_ok=True)
        self.path_not_sent.touch(exist_ok=True)

        self.sent = set(FileManager.read_lines(self.path_sent))
        self.not_sent = set(FileManager.read_lines(self.path_not_sent))


    def is_sent(self, number:str) -> bool:
        return number in self.sent
    
    def is_not_sent(self, number:str) -> bool:
        return number in self.not_sent
    
    def mark_sent(self, number:str):
        self.sent.add(number)
        FileManager.append_line(self.path_sent, number)
        if self.is_not_sent(number):
            self.not_sent.remove(number)
            FileManager.write_lines(self.path_not_sent, list(self.not_sent))

    def mark_not_sent(self, number:str):
        self.not_sent.add(number)
        FileManager.append_line(self.path_not_sent, number)
