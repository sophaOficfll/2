meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
cat=input("введите непонятное слово")
if cat in meme_dict.keys():
    print(meme_dict[cat])
else:
    print('нет такое слово')
