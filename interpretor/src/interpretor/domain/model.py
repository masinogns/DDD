from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set


class OutOfStock(Exception):
    pass


def allocate(line: Content, batches: List[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku {line.sku}")
    
@dataclass
class Content:
    orderid: str
    sku: str
    
    
class Batch:
    def __init__(self, ref: str, sku: str, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._allocations = set()  # type: Set[Content]

    def allocate(self, row: Content):
        if self.can_allocate(row):
            self._allocations.add(row)

    def can_allocate(self, row: Content) -> bool:
        return self.sku == row.sku
