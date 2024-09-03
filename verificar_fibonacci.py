verificar_numero = int(input());

def verificar_fibonacci(numero):
    sequencia = [0,1]

    while True:
        sequencia.append(sequencia[-2] + sequencia[-1])
        if sequencia[-1] == numero:
            return "Número está na sequencia"
        elif sequencia[-1] > numero:
            return "Número não está na sequencia"

print(verificar_fibonacci(verificar_numero))