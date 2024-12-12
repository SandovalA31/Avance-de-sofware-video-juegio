'video juego'
while True: 
    a = int(input("jugador 1: 1=piedra, 2=papel, 3=tijera: "))
    b = int(input("jugador 2: 1=piedra, 2=papel, 3=tijera: "))

    if a == 1 and b == 3:
        print('jugador 1 Gana: Piedra gana a tijera')
    elif a == 2 and b == 1: 
        print('jugador 1 Gana: Papel gana a piedra')
    elif a == 3 and b == 2: 
        print('jugador 1 Gana: tijera gana a Papel')
    elif b == 1 and a == 3: 
        print('jugador 2 Gana: piedra gana a tijera')
    elif b == 2 and a == 1: 
        print('jugador 2 Gana: Papel gana a Piedra')
    elif b == 3 and a == 2: 
        print('jugador 2 Gana: Tijera gana a Papel')
    else:
        print('ninguno gana ')
