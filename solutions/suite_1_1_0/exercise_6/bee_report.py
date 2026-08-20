# Add constants here

class BeeReport:
    def __repr__(self) -> str:
        pass

    def __init__(self, report_byte: int):
        pass

    @staticmethod
    def parse_hive_id(report_byte: int) -> bytes:
        pass
        
    @staticmethod
    def parse_field_id(report_byte: int) -> bytes:
        pass
    
    @staticmethod
    def parse_found_pollen(report_byte: int) -> bytes:
        pass

