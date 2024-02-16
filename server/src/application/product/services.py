from dataclasses import dataclass
from datetime import datetime

import pytz

from src.adapters.api.product import schemas
from src.adapters.database.settings import settings
from src.application import exceptions
from src.application.product import entities, interfaces


@dataclass
class ProductService:
    product_repo: interfaces.IProductRepository
    product_parser: interfaces.IProductParser

    async def add_product(self, nm_id: int) -> dict[str, str]:
        parse_product = self.product_parser.fetch_product_data(
            nm_id
        )

        if parse_product:
            product = entities.Product(
                dt=datetime.now(pytz.timezone(settings.TIMEZONE)),
                **parse_product
            )
            await self.product_repo.add_product(product)

            return {"status": "success"}

        raise exceptions.ProductNotFound(nm_id)

    async def get_product_by_nm_id(
        self,
        nm_id: int
    ) -> schemas.ProductResponse:
        product = await self.product_repo.get_product_by_nm_id(nm_id)
        return product

    async def get_all_products(self: int) -> list[schemas.ProductResponse]:
        products = await self.product_repo.get_all_products()
        return products

    async def delete_product_by_nm_id(self, nm_id: int) -> dict[str, str]:
        await self.product_repo.delete_product_by_nm_id(nm_id)
        return {"status": "success"}
