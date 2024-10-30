s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
result = {}
max_fruit = 0
for fruit in s.split():
    result[fruit] = result.get(fruit, 0) + 1
    if result[fruit] > max_fruit:
        max_fruit = result[fruit]
result_fruit = 'zzz'
for key, value in result.items():
    if value == max_fruit and key < result_fruit:
        result_fruit = key
print(result_fruit)
