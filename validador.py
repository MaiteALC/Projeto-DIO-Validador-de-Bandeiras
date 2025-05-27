discover = ("65", "6011", "644", "645", "646", "647", "648", "649")

mastercard = ("51", "52", "53", "54", "55", "2221", "2222", "2223", "2224", "2225", "2226", "2227", "2228", "2229", "23", "24", "25", "26", "270", "271", "2720")

# Lista de bandeiras aceitas para validação.
lista_bandeiras = ["Visa", "MasterCard", "Elo", "AmericanExpress", "Discover", "HiperCard", "JCB", "Aura", "Não Identificada"]
  
def  converter_digito(digito):
    return int(digito)

numero = input("Insira o número do seu cartão: ")

while len(numero) < 14:
    numero = input("O número deve ter 14 dígitos, tente novamente: ") 

algoritmo_luhn = filter(str.isdigit, numero)

lista_digitos = list(map(converter_digito, algoritmo_luhn))

print(f"Lista dos digitos: {lista_digitos}")

def validador_luhn(lista_num_cartao):
    indices_impares = []
    indices_pares = []
    for indice, elemento in enumerate(lista_num_cartao[::-1]):
        if indice % 2 != 0:
            dobrado = elemento * 2
            if dobrado > 9:
                    indices_pares.append(dobrado - 9)
            else:
                    indices_pares.append(dobrado)
        elif indice % 2 == 0:
            indices_impares.append(elemento)
    soma = sum(indices_pares) + sum(indices_impares)
    return soma 
  
luhn = validador_luhn(lista_digitos)
           
while not luhn % 10 == 0:
    print("Número do cartão inválido.")
    numero = input("Digite novamente: ")

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

bandeira_validada = validador_bandeira(numero)

print(f"Bandeira identificada: {bandeira_validada}")