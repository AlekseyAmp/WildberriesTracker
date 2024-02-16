from datetime import datetime

from pydantic import BaseModel


class ProductResponse(BaseModel):
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
