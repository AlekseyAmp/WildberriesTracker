from dataclasses import dataclass

from fastapi import HTTPException


@dataclass
class ProductNotFound(HTTPException):
    nm_id: int

    def __post_init__(self) -> None:
        detail = (
            f"Товар с идентификатором номенклатуры "
            f"'{self.nm_id}' не найден"
        )
        super().__init__(status_code=404, detail=detail)


@dataclass
class ProductExsist(HTTPException):
    nm_id: int

    def __post_init__(self) -> None:
        detail = (
            f"Товар с идентификатором номенклатуры"
            f"'{self.nm_id}' уже существует"
        )
        super().__init__(status_code=409, detail=detail)
