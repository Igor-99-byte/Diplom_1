
class TestDatabase:
    """Тесты для класса Database"""

    def test_available_buns(self, database):
        """Тестирование получения списка булочек"""
        buns = database.available_buns()
        
        assert len(buns) == 3
        assert all(bun.get_name() in ["black bun", "white bun", "red bun"] for bun in buns)

    def test_available_ingredients(self, database):
        """Тестирование получения списка ингредиентов"""
        ingredients = database.available_ingredients()
        
        assert len(ingredients) == 6
        # Проверяем, что есть и соусы и начинки
        sauce_count = sum(1 for ing in ingredients if ing.get_type() == "SAUCE")
        filling_count = sum(1 for ing in ingredients if ing.get_type() == "FILLING")
        assert sauce_count == 3
        assert filling_count == 3