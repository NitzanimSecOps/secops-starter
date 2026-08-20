from pathlib import Path

from solutions.suite_3_1_0.exercise_1.warehouse_setup import WarehouseSetup
from solutions.suite_3_1_0.exercise_2.warehouse_log import WarehouseLog
from solutions.suite_3_1_0.exercise_3.inventory_db import InventoryDB
from solutions.suite_3_1_0.exercise_4.integrity_checker import IntegrityChecker

class Warehouse:
    def __init__(self, root: str | Path) -> None:
        self.setup = WarehouseSetup(root)
        self.log = WarehouseLog(root / Path("logs") / Path("warehouse.log"))
        self.db = InventoryDB(root / Path("inventory") / Path("inventory.db"))
        self.integrity = IntegrityChecker(root)

