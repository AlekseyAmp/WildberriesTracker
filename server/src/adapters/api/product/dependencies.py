from fastapi import Depends
from sqlalchemy.orm import Session

from src.adapters.database import repositories
from src.adapters.database.sa_session import get_session
from src.adapters.requests import parser
from src.application import exceptions
from src.application.product.services import ProductService


def get_product_repo(
    session: Session = Depends(get_session)
) -> repositories.ProductRepository:
    return repositories.ProductRepository(session)


def get_product_parser() -> parser.WildberriesParser:
    return parser.WildberriesParser()


def get_product_service(
    product_repo: repositories.ProductRepository = Depends(
        get_product_repo
    ),
    product_parser: parser.WildberriesParser = Depends(
        get_product_parser
    )
) -> ProductService:
    return ProductService(product_repo, product_parser)


async def check_product_exsistence(
    nm_id: int,
    product_repo: repositories.ProductRepository = Depends(
        get_product_repo
    )
) -> int:
    """Проверяет наличие товара по его идентификатору номенклатуры."""
    product = await product_repo.get_product_by_nm_id(nm_id)
    if product:
        raise exceptions.ProductExsist(nm_id)

    return nm_id


async def check_product_presence(
    nm_id: int,
    product_repo: repositories.ProductRepository = Depends(
        get_product_repo
    )
) -> int:
    """Проверяет отсутствие товара по его идентификатору номенклатуры."""
    product = await product_repo.get_product_by_nm_id(nm_id)
    if not product:
        raise exceptions.ProductNotFound(nm_id)

    return nm_id
