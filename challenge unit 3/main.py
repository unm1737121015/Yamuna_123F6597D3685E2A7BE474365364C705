def linearsearchproduct(productList, targetProduct):
  
  indices = [ ]

  for index , product in enumerate(productList):
   if product == targetProduct:
    indices. append(index)
  return indices

# Example usage:
products=["shoes","boot","loafer","shoes","sandal","shoes"]
target1 ="shoes"
target2 ="apple"
result = linearsearchproduct(products,target1)
print(result)
result = linearsearchproduct(products,target2) 
print(result)
