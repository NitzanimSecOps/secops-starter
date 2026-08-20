class InventoryRecord:
    def __init__(self, data: bytes):
        pass
    
    @staticmethod
    def get_bytes(sku: str, quantity: int, price: float, timestamp: datetime) -> bytes:
        pass

    def to_bytes(self) -> bytes:
        pass