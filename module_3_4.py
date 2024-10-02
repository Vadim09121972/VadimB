def single_root_words(*other_words, root_words = 'хлеб'):
    same_words = []                       
    for i in other_words:
        if root_words.lower() in i.lower():
            same_words.append(i)   
          
    return print(same_words)

rezalt_1 = single_root_words( 'хлебный', 'нахлебник', 'хлев', 'похлёбка', 'хлебало')
rezalt_2 = single_root_words('небосклон', 'поднебесье', 'недоросль', 'непогода', 'небожитель', root_words = 'неб')
# rezalt_3 = single_root_words('слон', 'конь', 'бык', 'баран', root_words = 'неб')