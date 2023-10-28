def main():
    NUM = int(input("CUANTAS TABLAS: "))
    
    T = 1
    while T <= NUM:
        I = 10
        
        while I >= 1:
            RESUL = T * I
            print(f"{T} x {I} = {RESUL}")
            I = I - 1
        
        T = T + 1
    
    input("Pulse una Tecla :")

if __name__ == "__main__":
    main()

