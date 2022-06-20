from functions import JogoDAO

dao = JogoDAO()

def plataform(self):
# Criando as plataformas
    plat1 = 'playstation'
    plat2 = 'pc'
    plat3 = 'xbox'
    plat4 = 'nintendo'

    dao.createPlataforma(plat1)
    dao.createPlataforma(plat2)
    dao.createPlataforma(plat3)
    dao.createPlataforma(plat4)

plataform('1')


print('*'*100, '\n')
print('Bem Vindo a LM Store!!', '\n')

continuar = 's'

while(continuar == 's'):
    
    entrar = input(' Entrar como:\n 1. ADM\n 2. Usuario\n \n ----------> ')
    
    if entrar == '1':
        print('\n')
        print('-'*40, '\n')
        print('    O que gostaria de fazer?', '\n')
        escolha = input(' 1 - Editar preco de jogo\n 2 - Adicionar jogo novo\n 3 - Remover jogo\n 4 - Remover todos jogos \n ------------->  ')

        if escolha == '1':
            print('\n', 'Qual jogo voce deseja atualizar:', '\n')
            name = input('   Name: ')
            preco = input('   Preco: ')
            jogo = {
                'name': name,
                'preco': preco
            }
            
            aux = dao.update_preco(jogo)
            print('\n')
            print('-'*30)
            print('Preco atualizado com sucesso!')
            print('-'*30, '\n')

        elif escolha == '2':
            name = input('   Name: ')
            nomePlataforma = input('   Plataforma: ')
            nomeDesenvolvedora = input('   Desenvolvedora: ')
            preco = input('   Preco:  ')
            jogo = {
                'name': name,
                'nomePlataforma': nomePlataforma,
                'nomeDesenvolvedora': nomeDesenvolvedora,
                'preco': preco
            }
            aux = dao.createJogo(jogo)
            aux2 = dao.createRelacionamentoPlat(jogo)
            aux3 = dao.createDesenvolvedora(jogo)
            aux4 = dao.createRelacionamentoDev(jogo)
            print('\n')
            print('-'*30)
            print('Jogo criado com sucesso!')
            print('-'*30, '\n')

        elif escolha == '3':
            name = input('  Name: ')
            jogo = {
                'name': name
            }
            
            aux = dao.delete(jogo)
            print('\n')
            print('-'*30)
            print('Jogo deletado com sucesso!')
            print('-'*30, '\n')

        elif escolha == '4':
            print('##############################################')
            print('#  TEM CERTEZA QUE DESEJA APAGAR TUDO? [s/n] #')
            print('##############################################')
            certeza = input('-------->  ')
            if certeza == 's':
                aux = dao.deleteTudo()
                print('\n')
                print('-'*30)
                print('Jogos deletado com sucesso!')
                print('-'*30, '\n')
                plataform('1')
            elif certeza == 'n':
                print('')
        
        else:
            print('Comando nao reconhecido', '\n')
        
    elif entrar == '2':      

        print('-'*100)
        print('Catalogo de jogos:')

        aux = dao.readJogos()
        print(aux)

    print('###### Deseja continuar? ######', '\n')
    continuar = input(' s - Sim\n n - Nao\n \n ----------->  ')
