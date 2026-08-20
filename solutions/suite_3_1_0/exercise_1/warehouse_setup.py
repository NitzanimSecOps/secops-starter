from pathlib import Path

class WarehouseSetup:
    def __init__(self, root: str | Path) -> None:
        pass
        
    def get_dir(self, name: str) -> Path | None:
        pass
    
    def stat_report(self) -> list[dict]:
        pass
        
    def _init_dirs(self) -> None:
        pass
    
    