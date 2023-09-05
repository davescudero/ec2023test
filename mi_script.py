import pandas as pd

def saludo():
    print("Hola desde un script con Pandas!")

if __name__ == "__main__":
    saludo()
    # Crear un DataFrame simple como ejemplo
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    print(df)

