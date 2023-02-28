from Lampada import Lampada

# Cria um objeto Lampada com a lâmpada ligada
lampada = Lampada(True)

# Liga a lâmpada
lampada.liga()

# Verifica se a lâmpada está ligada
print("A lâmpada está ligada?", lampada.esta_ligada())

# Desliga a lâmpada
lampada.desliga()

# Verifica se a lâmpada está ligada
print("A lâmpada ainda está ligada?", lampada.esta_ligada())
