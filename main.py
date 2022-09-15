#Пример вызова программы
from PaginationHelper import PaginationHelper

print('Введите текст и число символов на странице: ')
text = input()
n = input()
helper = PaginationHelper(text, n)
print('Кол-во страниц, необходимое для размещения заданного кол-ва слов, равно {}'.format(helper.page_count()))
print('Всего слов: {}'.format(helper.item_count()))
print('Введите номер страницы для определения кол-ва слов на ней: ')
p_n = int(input())
print('Кол-во слов на странице {0} равно {1}'.format(p_n, helper.page_item_count(p_n)))
print('Введите номер слова для поиска страницы, на котором оно находится: ')
w_n = int(input()) - 1
print('Слово \'{0}\' находится на странице №{1}'.format(helper.mas[w_n], helper.page_index(w_n)))

