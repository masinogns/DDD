from collections import namedtuple

import json
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set
from abc import ABCMeta, abstractmethod


class OutOfStock(Exception):
    pass


def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku {line.sku}")


@dataclass(unsafe_hash=True)
class ObjectSchema():
    id: str
    source: str
    target: str
    attribute: List[tuple]

class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()  # type: Set[ObjectSchema]

    def __repr__(self):
        return f"<Batch {self.reference}>"

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, line: ObjectSchema):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: ObjectSchema):
        if line in self._allocations:
            self._allocations.remove(line)
