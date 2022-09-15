import re


class PaginationHelper:

    def __init__(self, str, items_per_page):
        mas = re.split('[, .!?:;]', str)
        self.mas = mas
        self.items_per_page = int(items_per_page)

    def item_count(self):
        return len(self.mas)

    def page_count(self):
        import math
        return math.ceil(len(self.mas) / self.items_per_page)

    def page_item_count(self, page_index):
        return len(self.mas[
                   page_index * self.items_per_page: page_index * self.items_per_page + self.items_per_page]) if page_index * self.items_per_page <= len(
            self.mas) - 1 else -1

    def page_index(self, item_index):
        import math
        return math.floor(item_index / self.items_per_page) + 1 if item_index <= len(
            self.mas) - 1 and item_index >= 0 else -1
