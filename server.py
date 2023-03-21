from xmlrpc.server import SimpleXMLRPCServer

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def handle_message(msg):
    print("Mensagem recebida:", msg.decode())
    return "Mensagem recebida com sucesso"

server = SimpleXMLRPCServer(("localhost", 8080))
print("Aguardando conexão...")

server.register_function(add, 'add')
server.register_function(subtract, 'subtract')
server.register_function(multiply, 'multiply')
server.register_function(divide, 'divide')
server.register_function(handle_message, 'handle_message')
server.register_introspection_functions()

server.serve_forever()

