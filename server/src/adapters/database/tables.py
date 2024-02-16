from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    MetaData,
    String,
    Table
)
from sqlalchemy.dialects.postgresql import ARRAY, JSONB

metadata = MetaData()


products = Table(
    'products', metadata,
    Column(
        'id',
        Integer,
        primary_key=True,
        comment='Уникальный идентификатор товара',
    ),
    Column(
        'dt',
        DateTime,
        comment='Дата добавления товара',
    ),
    Column(
        'nm_id',
        Integer,
        comment='Идентификатор номенклатуры товара',
    ),
    Column(
        'name',
        String,
        comment='Название товара',
    ),
    Column(
        'brand',
        String,
        comment='Бренд товара',
    ),
    Column(
        'brand_id',
        Integer,
        comment='Идентификатор бренда',
    ),
    Column(
        'site_brand_id',
        Integer,
        comment='Идентификатор бренда на сайте',
    ),
    Column(
        'supplier_id',
        Integer,
        comment='Идентификатор поставщика',
    ),
    Column(
        'sale',
        Float,
        comment='Товар находится на распродаже или нет',
    ),
    Column(
        'price',
        Float,
        comment='Цена товара без скидки',
    ),
    Column(
        'sale_price',
        Float,
        comment='Цена товара со скидкой',
    ),
    Column(
        'rating',
        Float,
        comment='Рейтинг товара',
    ),
    Column(
        'feedbacks',
        Integer,
        comment='Количество отзывов о товаре',
    ),
    Column(
        'colors',
        ARRAY(JSONB),
        comment='Список цветов товара',
    ),
    comment='Таблица, содержащая информацию о товарах',
)
