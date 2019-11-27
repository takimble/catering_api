def sort_by_price_ascending(json_string):
    data = dict(json_string).sorted('price')
    print(data)
  
    
    

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))