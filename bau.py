while True:
    x = int(input("Insira a coordenada x:"))
    z = int(input("Insira a coordenada z:"))
    xchunck = (x//16)*16
    zchunck = (z//16)*16
    xbau, zbau = xchunck+8, zchunck+8
    print(f"O bau está localizado em ({xbau}, {zbau})")