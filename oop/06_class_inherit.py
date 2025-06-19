class Category:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Category: {self.name}"


category = Category("Electronics")
print(category.info())


class SubCategory(Category):
    def __init__(self, name, parent_category_name):
        super().__init__(parent_category_name)
        self.sub_name = name

    def info(self):
        return f"SubCategory: {self.sub_name}, Parent Category: {self.name}"


subcat = SubCategory("Smartphones", "Electronics")
print(subcat.info())
