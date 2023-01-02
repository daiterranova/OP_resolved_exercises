""" En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado. """
f = open("demofile.txt", "w")
f.write("data")
f.write("data_two\n")
f.close()

f = open("demofile.txt", "r+")
f.readline()
f.write("new line\n")
f.seek(0)
print(f.read())
f.close()
