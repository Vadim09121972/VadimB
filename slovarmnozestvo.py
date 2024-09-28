fone_book = {'vadim': 89996662323, 'tania': 85556661234}
fone_book['vadim'] = 56813843849
print(fone_book)
fone_book['anton'] = 4684351384 # добавить номер
print(fone_book)
del fone_book['tania'] #удалить номер
print(fone_book)
fone_book.update({'tom': 23518313813, 'alex': 6816821385}) #внести нескотлько номеров
print(fone_book)