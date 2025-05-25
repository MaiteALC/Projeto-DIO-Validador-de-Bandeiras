discover = ("65", "6011", "644", "645", "646", "647", "648", "649")

mastercard = ("51", "52", "53", "54", "55", "2221", "2222", "2223", "2224", "2225", "2226", "2227", "2228", "2229", "23", "24", "25", "26", "270", "271", "2720")

# Lista de bandeiras aceitas para validação.
lista_bandeiras = ["Visa", "MasterCard", "Elo", "AmericanExpress", "Discover", "HiperCard", "JCB", "Aura", "Não Identificada"]

numero_cartao = input("Insira o número do seu cartão: ")

qntd_digitos = len(numero_cartao)

if qntd_digitos < 14:
  print("Número do cartão inválido")


# Função que recebe o número do cartão e retorna a bandeira correspondente.
def validador_bandeira(cartao):
  if cartao.startswith("4"):
    bandeira = lista_bandeiras[0]
  elif cartao.startswith((mastercard)):
     bandeira = lista_bandeiras[1]
  elif cartao.startswith(("4011", "4312", "4389")):
    bandeira = lista_bandeiras[2]
  elif cartao.startswith(("34", "37")):
    bandeira = lista_bandeiras[3]
  elif cartao.startswith((discover)):
    bandeira = lista_bandeiras[4]
  elif cartao.startswith("6062"):
    bandeira = lista_bandeiras[5]
  elif cartao.startswith("35"):
    bandeira = lista_bandeiras[6]
  elif cartao.startswith("50"):
    bandeira = lista_bandeiras[7]
  else: 
    bandeira = lista_bandeiras[-1]
  return bandeira

validacao = validador_bandeira(numero_cartao)

print(f"Bandeira do cartão: " + str(validacao))
  
      