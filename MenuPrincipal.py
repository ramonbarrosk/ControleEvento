from Classes import *
def verificandoCPF(adm,cpf):
    cpfExisti = False
    for i in adm.admSistema:
        if i.cpf==cpf:
            cpfExisti =  True
    for i in adm.admEventos:
        if i.cpf==cpf:
            cpfExisti = True
    for i in adm.participantes:
        if i.cpf==cpf:
            cpfExisti = True
    return cpfExisti
def verificandoCPFadm(cpf):
    adm = None
    for i in Dados.admEventos:
        if i.cpf==cpf:
            adm = i
    return adm
def retornaEvento(adm,sigla):
    evento = None
    for i in adm.eventos:
        if i.sigla==sigla:
            evento = i
    return evento
def validandoUsuario():
    usuario = None
    nome = input("Informe seu nome:")
    cpf = int(input("Informe seu cpf(Apenas Números):"))
    endereco = input("Informe seu endereço(Cidade,Bairro,Estado,CEP):")
    data_nascimento = input("Informe a data de nascimento(DD/MM/AAAA):")
    senha = input("Informe a senha:")
    usuario = Usuario(nome,cpf,endereco,data_nascimento,senha)
    return usuario
def validandoLogin():
    cpf = int(input("Insira seu CPF(Apenas Números):"))
    senha = input("Insira sua senha:")
    objeto = None
    for i in Dados.admSistema:
        if i.cpf==cpf and i.senha==senha:
            objeto = i
            
    for i in Dados.admEventos:
        if i.cpf==cpf and i.senha==senha:
            objeto = i
            
    for i in Dados.usuarios:
        if i.cpf==cpf and i.senha==senha:
            objeto = i
    return objeto   
def validandoEvento():
    evento = None
    nome_evento = input("Insira o nome do evento:")
    sigla = input("Insira a sigla do evento:")
    descricao = input("Insira a descrição do evento:")
    local = input("Insira o local do evento:")
    data_inicio = input("Insira a data do inicio do evento(DD/MM/AAAAA):")
    data_fim = input("Insira a data do fim do evento(DD/MM/AAAAA):")
    cpf = int(input("Informe o cpf do Administrador do evento:"))
    while verificandoCPFadm(cpf)==None:
        print("CPF informado não está cadastrado como administrador de Eventos!")
        cpf = input("Informe o cpf do Administrador do evento::")
    admEvento = verificandoCPFadm(cpf)
    valor_participante_profissional = float(input("Informe o valor do ingresso para participante profissional:"))
    valor_participante_estudante = float(input("Informe o valor do ingresso para participante estudante:"))
    evento = Evento(nome_evento,sigla,descricao,local,data_inicio,data_fim,admEvento,valor_participante_profissional,valor_participante_estudante)
    return evento

def main():
    opcao = 4
    while opcao!=3:
        print("Bem vindo ao Sistema de Eventos!\n1-Criar Conta\n2-Realizar Login\n3-Sair do Sistema")
        opcao = int(input("Escolha uma opção->"))
        if opcao==1:
            opcao=9
            while opcao!=5:
                print("1-Administrador Sistema\n2-Administrador Evento\n3-Participante Estudante\n4-Participante Profissional\n5-Menu Inicial")
                opcao = int(input("Escolha um tipo de usuário->"))
                if opcao==1:
                    usuario = validandoUsuario()
                    admSistema = AdministradorSistema(usuario.nome,usuario.cpf,usuario.endereco,usuario.data_nascimento,usuario.senha)
                    admSistema.tipo = "ADM_SISTEMA"
                    Dados.admSistema.append(admSistema)
                    print("Administrador Sistema criado com sucesso!")
                elif opcao==2:
                    usuario = validandoUsuario()
                    admEvento = AdministradorEvento(usuario.nome,usuario.cpf,usuario.endereco,usuario.data_nascimento,usuario.senha)
                    admEvento.tipo = "ADM_EVENTO"
                    Dados.admEventos.append(admEvento)
                    print("Administrador Evento criado com sucesso!")
                elif opcao==3:
                    usuario = validandoUsuario()
                    participanteEstudante = Participante(usuario.nome,usuario.cpf,usuario.endereco,usuario.data_nascimento,usuario.senha)
                    participanteEstudante.tipo = "PARTICIPANTE_ESTUDANTE"
                    Dados.usuarios.append(participanteEstudante)
                    print("Participante Estudante criado com sucesso!")
                elif opcao==4:
                    usuario = validandoUsuario()
                    participanteProfissional = Participante(usuario.nome,usuario.cpf,usuario.endereco,usuario.data_nascimento,usuario.senha)
                    participanteProfissional.tipo = "PARTICIPANTE_PROFISSIONAL"
                    Dados.usuarios.append(participanteProfissional)
                    print("Participante Profissional criado com sucesso!")
        elif opcao==2:
            objeto = validandoLogin()
            if objeto==None:
                print("Login inválido")
            else:
                if objeto.tipo=="ADM_SISTEMA":
                    
                    
                    opcao=11
                    while opcao!=10:
                        print("MENU DE ADMINISTRADOR DE SISTEMA\n1-Cadastrar Administrador de Sistema\n2-Cadastrar Administrador de Evento\n3-Cadastrar Evento\n4-Remover Evento\n5-Remover Usuário\n6-Listar Eventos\n7-Exibir Relatório do Sistema\n8-Exibir relatório por evento\n9-Deslogar\n10-Sair do sistema")
                        opcao = int(input("Informe uma opção->"))
                        if opcao==1:
                            usuario = validandoUsuario()
                            Dados.admSistema.append(usuario)
                            print("ADM de Sistema cadastrado com sucesso!")
                        elif opcao==2:
                            usuario = validandoUsuario()
                            Dados.admEventos.append(usuario)
                            print("ADM de Evento cadastrado com sucesso!")
                        elif opcao==3:
                            evento = validandoEvento()
                            Dados.eventos.append(evento)
                            print("Evento cadastrado com sucesso")
                        elif opcao==4:
                            sigla = input("Informe a sigla do evento a ser excluído:")
                            objeto.removerEvento(sigla)
                        elif opcao==5:
                            cpf = input("Informe o cpf do usuario a ser excluído:")
                            objeto.removerUsuario(cpf)
                        elif opcao==6:
                            objeto.listarEventos()
                        elif opcao==7:
                            objeto.relatorioSistema()
                        elif opcao==8:
                            sigla = input("Informe a sigla do evento a ser detalhado:")
                            objeto.relatorioEvento(sigla)
                        elif opcao==9:
                            print("Usuário deslogado!")
                            main()
                elif objeto.tipo=="ADM_EVENTO":
                    opcao ==11
                    while opcao!=6:
                        print("MENU DE ADMINISTRADOR DE EVENTOS\n1-Alterar dados pessoais\n2-Listar Eventos\n3-Desinscrever usuário do evento\n4-Exibir relatorio por evento\n5-Deslogar\n6-Sair do sistema")
                        opcao = int(input("Insira uma opção->"))
                        if opcao==1:
                            print("O que deseja alterar?\n1-Nome\n2-Data de nascimento\n3-Endereço\n4-Senha\n")
                            if opcao==1:
                                nome = input("Informe seu nome:")
                                objeto.nome = nome
                            elif opcao==2:
                                data_nascimento = input("Informe sua data de nascimento:")
                                objeto.data_nascimento = data_nascimento
                            elif opcao==3:
                                endereco = input("Insira seu novo endereço:")
                                objeto.endereco = endereco
                            elif opcao==4:
                                senha = input("Insira sua senha:")
                                objeto.senha = senha
                        elif opcao==2:
                                 objeto.listarEventos()
                        elif opcao==3:
                                 cpf = input("Informe o cpf do usuário:")
                                 sigla = input("Informe a sigla do evento:")
                                 objeto.desinscreverUsuarioEvento(cpf,sigla)
                        elif opcao==4:
                                 sigla = input("Insira a sigla do evento:")
                                 objeto.relatorioEvento(sigla)
                        elif opcao==5:
                                 print("Usuário deslogado!")
                                 main()
                elif objeto.tipo=="PARTICIPANTE_ESTUDANTE" or objeto.tipo=="PARTICIPANTE_PROFISSIONAL":
                    opcao == 11
                    while opcao!=6:
                        print("MENU DO PARTICIPANTE\n1-Alterar dados pessoais\n2-Listar Eventos inscritos\n3-Detalhar evento\n4-Realizar Inscrição evento\n5-Deslogar\n6-Sair do sistema")
                        opcao = int(input("Escolha uma opção:"))
                        if opcao==1:
                            print("O que deseja alterar?\n1-Nome\n2-Data de nascimento\n3-Endereço\n4-Senha\n")
                            opcao = int(input("Escolha uma opção:"))
                            if opcao==1:
                                nome = input("Informe seu nome:")
                                objeto.nome = nome
                            elif opcao==2:
                                data_nascimento = input("Informe sua data de nascimento:")
                                objeto.data_nascimento = data_nascimento
                            elif opcao==3:
                                endereco = input("Insira seu novo endereço:")
                                objeto.endereco = endereco
                            elif opcao==4:
                                senha = input("Insira sua senha:")
                                objeto.senha = senha
                        elif opcao==2:
                            objeto.listarEventosInscritos()
                        elif opcao==3:
                            sigla = input("Insira a sigla do evento a ser detalhado:")
                            objeto.detalheEvento(sigla)
                        elif opcao==4:
                            sigla = input("Insira a sigla do evento no qual quer se inscrever:")
                            objeto.realizarInscricaoEvento(sigla)
                        elif opcao==5:
                            main()
if __name__ == "__main__":
    main()
    
    
        
    
