questions4 = [
    {
        'id':1,
        'text': "2 * 2",
        'answers': [4,6,8,2],
        'right_answer': 1,
        'sum':100
    },
    {
        'id':2,
        'text': "3 * 2",
        'answers': [4,6,8,2],
        'right_answer': 2,
        'sum':500
    },
    {
        'id':3,
        'text': "7 * 6",
        'answers': [42,6,8,2],
        'right_answer': 1,
        'sum':1000
    }
]

money = 0
for item in questions:
    res_text = f"Вопрос: {item['text']} = ?\n"
    for index,answer in enumerate(item['answers'],1):
        res_text += f"{index}) {answer}\n"
    answer = int(input(res_text))
    if answer == item['right_answer']:
        money += item['sum']
    else:
        money = 0
        print("Вы проиграли")
        break
else:
    print("Вы выиграли",money)
