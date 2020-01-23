respuestaUsuario = input("quieres jugar s/n?: ").lower()
while respuestaUsuario != "n":
    print("buenisimo te muestro la app")
    respuestaUsuario = input("quieres jugar s/n?: ").lower()

print("ejecucion de un loop")

amigos = ["ana","eve","franco"]
for amigo in range(5):
    print (f"mi amigo es: {amigo}")