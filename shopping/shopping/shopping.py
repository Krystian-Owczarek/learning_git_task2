shopping_dict = {}
shopping_dict['piekarnia'] = ["chleb", "bułki", "pączek"]
shopping_dict['warzywniak'] = ["marchew", "seler", "rukola"]
number_of_values = 0

for elem in shopping_dict:
  products = shopping_dict.get(elem)
  products_capitalized = []
  for product in products:
    products_capitalized.append(product.capitalize())
    number_of_values += 1
  print(f'Idę do {elem.title()} i kupuję tam {products_capitalized}')

print(f'W sumie kupuję {number_of_values} produktów')
print('Właśnie dodałem linię')