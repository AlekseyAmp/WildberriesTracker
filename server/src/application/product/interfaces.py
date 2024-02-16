from abc import ABC, abstractmethod
from typing import Sequence

from src.application.product import entities


class IProductRepository(ABC):

    @abstractmethod
    async def add_product(self, product: entities.Product) -> int:
        ...

    @abstractmethod
    async def get_product_by_nm_id(
        self,
        nm_id: int
    ) -> entities.ProductResult | None:
        ...

    @abstractmethod
    async def get_all_products(self: int) -> Sequence[entities.ProductResult]:
        ...

    @abstractmethod
    async def delete_product_by_nm_id(self, nm_id: int) -> int:
        ...


class IProductParser(ABC):
    @abstractmethod
    async def fetch_product_data(self, nm_id: int) -> dict | None:
        ...
