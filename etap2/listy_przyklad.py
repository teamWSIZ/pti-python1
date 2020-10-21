diamenty = [2, 5, 8, 18, 2, 0.2]  # to jest lista liczb

print(diamenty)  # drukuje listę do konsoli

# przechodzenie przez wszystkie elementy listy `dia`
for diament in diamenty:
    print('rozpoczynam sprawdzanie diamentu')
    print(diament)
    if diament < 6:
        print('diament jest < 10')
        print('-----')
    else:
        print('duzy diament >= 10')
        print('#####')

print('koniec programu')
