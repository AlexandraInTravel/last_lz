def main():
    L_star = float(input('Введите светимость звезды: '))
    my_star = lambda L_star: ((L_star/(3.86*(10**33)))**0.5)*149_597_870_700
    print('Средний радиус обитаемой зоны',my_star(L_star), 'м')
    
if __name__=='__main__':
    main()

