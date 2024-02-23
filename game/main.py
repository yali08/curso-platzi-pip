import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
        print('Esa opcion no es valida')
        # continue  
        return None, None
    
    computer_option = random.choice(options)
    
    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option

    def check_rules(user_option, computer_option, user_wins, computer_wins):

        if user_option == computer_option: 
            print('Empate!')
        elif user_option == 'piedra':
            if computer_option == 'tijera':
                print('piedra gana a tijera')
                print('User gano!')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('Computer gano!')
            computer_wins += 1
        
        elif user_option == 'papel': 
            if computer_option == 'piedra':
                print('papel gana a piedra')
                print('User gano!')
                user_wins += 1
            else:
                print('tijeras gana a papel')
                print('Computer gano!')
                computer_wins += 1
        elif user_option == 'tijera':
            if computer_option == 'papel':
                print('tijera gana a papel')
                print('User gano!')
                user_wins += 1
            else:
            print('piedra gana a tijera')
            print('Computer gano!')
            computer_wins += 1
            return user_wins, computer_wins