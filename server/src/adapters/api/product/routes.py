from fastapi import APIRouter, Depends

from src.adapters.api.product import schemas
from src.adapters.api.product.dependencies import (
    check_product_exsistence,
    check_product_presence,
    get_product_service
)
from src.application.product.services import ProductService

router = APIRouter()


@router.post(
    path="/add_product",
    response_model=dict[str, str]
)
async def add_product(
    nm_id: int = Depends(check_product_exsistence),
    product_service: ProductService = Depends(get_product_service)
) -> dict[str, str]:
    return await product_service.add_product(nm_id)


@router.get(
    path="/get_product/{nm_id}",
    response_model=schemas.ProductResponse,
)
async def get_product_by_nm_id(
    nm_id: int = Depends(check_product_presence),
    product_service: ProductService = Depends(get_product_service)
) -> schemas.ProductResponse:
    return await product_service.get_product_by_nm_id(nm_id)


@router.get(
    path="/get_all_products",
    response_model=list[schemas.ProductResponse],
)
async def get_all_products(
    product_service: ProductService = Depends(get_product_service)
) -> list[schemas.ProductResponse]:
    return await product_service.get_all_products()


@router.delete(
    path="/delete_product/{nm_id}",
    response_model=dict[str, str],
)
async def delete_product_by_nm_id(
    nm_id: int = Depends(check_product_presence),
    product_service: ProductService = Depends(get_product_service)
) -> dict[str, str]:
    return await product_service.delete_product_by_nm_id(nm_id)
