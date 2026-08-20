class InventoryDB:
    def __init__(self, path: str | Path):
        pass

    def open_record(self, record_path: Path) -> InventoryRecord:
        pass
        
    def add_record(self, record: InventoryRecord) -> None:
        pass
            
    def remove_record(self, sku: str) -> None:
        pass
    
    def find_record(self, sku: str) -> InventoryRecord | None:
        pass
  
    @staticmethod
    def detect_file_type(path: str | Path) -> str:
        pass
    