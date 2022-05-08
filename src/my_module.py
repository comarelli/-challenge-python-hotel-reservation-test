#Resolução do desafio para o Programa de estágio Syngenta Digital
#Autor: Arthur Araújo Comarelli Salles

def get_cheapest_hotel(number):   #DO NOT change the function's name
    
    Av_lakewood = 3                                              #Define avaliação do hotel
    Av_bridgewood = 4
    Av_ridgewood = 5
    dias_fds = number.count('sat') + number.count('sun')           #contabiliza número de dias no fim de semana
    dias_sem = sum(number.count(j) for j in ['mon','tues','wed','thur','fri'])   #contabiliza número de dias de semana
    
    if 'Rewards' in number:                                   #Preço em cada hotel para fidelidade
        Pr_Lakewood = 80*dias_sem + 80*dias_fds
        Pr_Bridgewood = 110*dias_sem + 50*dias_fds
        Pr_Ridgewood = 100*dias_sem + 40*dias_fds
        
    if 'Regular' in number:                                   #Preço em cada hotel para comum
        Pr_Lakewood = 110*dias_sem + 90*dias_fds
        Pr_Bridgewood = 160*dias_sem + 60*dias_fds
        Pr_Ridgewood = 220*dias_sem + 150*dias_fds
    Pr_list = [Pr_Lakewood, Pr_Bridgewood, Pr_Ridgewood]      #Lista com o preço encontrado
    Pr_list.sort(reverse=False)                               #Ordena de forma crescente a lista
    for i in [Pr_Lakewood, Pr_Bridgewood, Pr_Ridgewood]:      #Encontra qual hotel está na posição 0 da lista
        if Pr_list.index(i) == 0:
            aux = i

    if (Pr_Ridgewood == Pr_Bridgewood and (Pr_Ridgewood == aux or Pr_Bridgewood == aux)) or (Pr_Ridgewood == Pr_Lakewood and (Pr_Ridgewood == aux or Pr_Lakewood == aux)) or (Pr_Bridgewood == Pr_Lakewood and (Pr_Bridgewood == aux or Pr_Lakewood == aux)):     #Confere se dois ou mais hoteis possuem o preço mais barato
        if Pr_Ridgewood == Pr_Lakewood and Pr_Ridgewood == Pr_Bridgewood:
            if Av_ridgewood > Av_lakewood:                    #Condicionais que decidem qual hotel tem a melhor avaliação
                cheapest_hotel = 'Ridgewood'
            elif Av_lakewood >Av_bridgewood:
                cheapest_hotel = 'Lakewood'
            else:
                cheapest_hotel = 'Bridgewood'

        elif Pr_Ridgewood == Pr_Bridgewood:
            if Av_ridgewood > Av_bridgewood:
                cheapest_hotel = 'Ridgewood'
            else:
                cheapest_hotel = 'Bridgewood'

        elif Pr_Bridgewood == Pr_Lakewood:
            if Av_bridgewood > Av_lakewood:
                cheapest_hotel = 'Bridgewood'
            else:
                cheapest_hotel = 'Lakewood'

        elif Pr_Ridgewood == Pr_Lakewood:
            if Av_ridgewood > Av_lakewood:
                cheapest_hotel = 'Ridgewood'
            else:
                cheapest_hotel = 'Lakewood'
        
    else:                                   #caso não tenha hoteis empatados com o menor preço
        if   Pr_Bridgewood == aux:          #condicionais que encontram o hotel com menor preço
                cheapest_hotel = 'Bridgewood'

        elif Pr_Lakewood == aux:
            cheapest_hotel = 'Lakewood'

        else:
            cheapest_hotel = 'Ridgewood'

    return cheapest_hotel

def test_answer():
    assert get_cheapest_hotel('Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)')   == 'Lakewood'
    assert get_cheapest_hotel('Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)')    == 'Bridgewood'
    assert get_cheapest_hotel('Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)')   == 'Ridgewood'