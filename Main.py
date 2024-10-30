import pandas as pd

if __name__ == '__main__':
    # Zad 1
    df = pd.read_csv('housing.csv')
    # Liczba rekordów (wierszy)
    print(df.shape[0])
    # Liczba atrybutów (kolumn)
    print(df.shape[1])
    # Typy atrybutów (kolumn)
    print(df.info())
    # Zad 2
    print(df.describe())