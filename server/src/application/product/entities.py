from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    dt: datetime
    nm_id: int
    name: str
    brand: str
    brand_id: int
    site_brand_id: int
    supplier_id: int
    sale: float
    price: float
    sale_price: float | None
    rating: float
    feedbacks: int
    colors: list[dict]


@dataclass
class ProductResult:
    id: int
    dt: datetime
    nm_id: int
    name: str
    brand: str
    brand_id: int
    site_brand_id: int
    supplier_id: int
    sale: float
    price: float
    sale_price: float | None
    rating: float
    feedbacks: int
    colors: list[dict]
