from dataclasses import asdict

import sqlalchemy as sqla

from src.adapters.database.repositories.base_repository import SABaseRepository
from src.adapters.database import tables
from src.application.product import entities, interfaces


class ProductRepository(SABaseRepository, interfaces.IProductRepository):

    async def add_product(self, product: entities.Product) -> int:
        """
        Добавляет товар.

        :param product: Экземпляр сущности Product для добавления.
        :return: Идентификатор добавленного товара.
        """
        table: sqla.Table = tables.products

        query: sqla.Insert = (
            sqla.insert(
                table
            )
            .values(
                **asdict(product)
            )
            .returning(
                table.c.id
            )
        )
        product = self.session.execute(query).mappings().one()
        self.session.commit()

    async def get_product_by_nm_id(
        self,
        nm_id: int
    ) -> entities.ProductResult | None:
        """
        Получает товар по идентификатору номенклатуры.

        :param nm_id: Идентификатор номенклатуры.
        :return: Экземпляр сущности Product,
            если товар найден, в противном случае None.
        """
        table: sqla.Table = tables.products

        query: sqla.Select = (
            sqla.select(
                table
            )
            .filter(
                table.c.nm_id == nm_id
            )
        )
        product = self.session.execute(query).mappings().first()
        return product

    async def get_all_products(self) -> sqla.Sequence[entities.ProductResult]:
        """
        Получает все товары.

        :return: Итерируемый объект, содержащий экземпляры сущности Product.
        """
        table: sqla.Table = tables.products

        query: sqla.Select = (
            sqla.select(
                table
            )
        )
        products = self.session.execute(query).mappings()
        return [entities.ProductResult(**row) for row in products]

    async def delete_product_by_nm_id(self, nm_id: int) -> int:
        """
        Удаляет товар по идентификатору номенклатуры.

        :param nm_id: Идентификатор номенклатуры.
        :return: Идентификатор удаленного товара.
        """
        table: sqla.Table = tables.products

        query: sqla.Delete = sqla.delete(table).filter(
            table.c.nm_id == nm_id,
        )

        result = self.session.execute(query)
        self.session.commit()
        return result.rowcount
