import requests

from src.application.constants import WB_CARD_URL


class WildberriesParser:
    """Класс для получения данных о продукте из API Wildberries."""

    def fetch_product_data(self, nm_id: int) -> dict | None:
        """
        Получает данные о продукте из внешнего API по предоставленному nm_id.

        :param nm_id: Идентификатор номенклатуры,
            для которого необходимо получить данные.

        :return: Словарь, содержащий информацию о продукте
            в случае успешного выполнения, в противном случае None.
        """

        response = requests.get(WB_CARD_URL + str(nm_id))

        if response.status_code == 200:
            data = response.json()
            products_data = data.get('data').get('products')

            # Парсинг только первого элемента списка продуктов
            if products_data:
                product_data = products_data[0]
                product = {
                    "nm_id": product_data.get("id"),
                    "name": product_data.get("name"),
                    "brand": product_data.get("brand"),
                    "brand_id": product_data.get("brandId"),
                    "site_brand_id": product_data.get("siteBrandId"),
                    "supplier_id": product_data.get("supplierId"),
                    "sale": product_data.get("sale"),
                    "price": product_data.get("priceU"),
                    "sale_price": product_data.get("salePriceU"),
                    "rating": product_data.get("rating"),
                    "feedbacks": product_data.get("feedbacks"),
                    "colors": product_data.get("colors")
                }

                return product

        return None
