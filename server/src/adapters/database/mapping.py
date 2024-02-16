from sqlalchemy.orm import registry

from src.adapters.database.tables import products
from src.application.product import entities

mapper_registry = registry()


mapper_registry.map_imperatively(entities.Product, products)
