# curl http://localhost:8000/pizzas/1 | json_pp

# curl http://localhost:8000/pizzas/999999 | json_pp # NOT FOUND

# Retorna 15 pizzas aleatórias
curl http://localhost:8000/pizzas/random #| json_pp 

