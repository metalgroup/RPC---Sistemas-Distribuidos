import xmlrpc.client as rpc
import os

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            break
        except ValueError:
            print("Por favor, digite um n�mero v�lido.")
    return value

client = rpc.ServerProxy('http://localhost:8080/')

message = input("Digite uma mensagem para enviar ao servidor: ").strip().encode()
response = client.handle_message(message)
print(response)

a = get_float_input("Digite o primeiro n�mero: ")
b = get_float_input("Digite o segundo n�mero: ")

try:
    print("Soma: ", client.add(a, b))
    print("Subtra��o: ", client.subtract(a, b))
    print("Multiplica��o: ", client.multiply(a, b))
    print("Divis�o: ", client.divide(a, b))
except rpc.Fault as e:
    print("Ocorreu um erro no servidor:", e)

os.system("PAUSE")
