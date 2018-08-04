from Classes import *

def verificandoSigla(sigla):
    siglaExisti = False
    for i in Dados.eventos:
        if i.sigla==sigla:
            siglaExisti = True
def verificandoCPFadm(cpf):
    objeto = None
    for i in Dados.admEventos:
        if i.cpf==cpf:
            objeto = i
    return objeto
def verificandoCPF(cpf):
    cpfExisti = False
    for i in Dados.admSistema:
        if i.cpf==cpf:
            cpfExisti =  True
    for i in Dados.admEventos:
        if i.cpf==cpf:
            cpfExisti = True
    for i in Dados.usuarios:
        if i.cpf==cpf:
            cpfExisti = True
    return cpfExisti
def validandoUsuario():
    usuario = None
    nome = input("Informe seu nome(Mínimo 4 caracteres):")
    while len(nome)<4:
        nome = input("Seu nome deve ter mais que 3 caracteres:")
    verificaCPF = False
    while verificaCPF==False:
        try:
            cpf = int(input("Informe seu cpf(Apenas Números):"))
            cpf = str(cpf)
            while len(cpf)!=11:
                cpf = int(input("Insira um cpf válido:"))
                cpf = str(cpf)
            while verificandoCPF(cpf)==True:
                cpf = int(input("CPF já existi, insira outro:"))
                cpf = str(cpf)
            verificaCPF = True
        except ValueError:
            print("CPF aceita apenas números:")
    endereco = input("Informe seu endereço:")
    data = False
    while data==False:
        try:
            data_nascimento = input("Informe a data de nascimento(DD/MM/AAAA):")
            while len(data_nascimento)!=10:
                data_nascimento = input("Informe uma data de nascimento válida:")
                
            dia,mes,ano = data_nascimento.split("/")
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
            while dia>31:
                print("Insira uma data válida!")
                data_nascimento = input("Informe a data de nascimento(DD/MM/AAAA):")
                dia,mes,ano = data_nascimento.split("/")
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                
            while mes>12:
                print("Insira um mês válido!")
                data_nascimento = input("Informe a data de nascimento(DD/MM/AAAA):")
                dia,mes,ano = data_nascimento.split("/")
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
            data = True
        except ValueError:
            print("Informe uma data válida!")
    senha = input("Informe a senha(Mínimo 4 caracteres):")
    while len(senha)<4:
        senha = input("Senha deve ter mais que 3 caracteres:")
    usuario = Usuario(nome,cpf,endereco,data_nascimento,senha)
    return usuario
def validandoLogin():
    objeto = None
    try:
        cpf = int(input("Insira seu CPF(Apenas Números):"))
        cpf = str(cpf)
        while len(cpf)!=11:
            cpf = int(input("Insira um CPF válido:"))
            cpf = str(cpf)
        senha = input("Insira sua senha:")
        for i in Dados.admSistema:
            if i.cpf==cpf and i.senha==senha:
                objeto = i
        for i in Dados.admEventos:
            if i.cpf==cpf and i.senha==senha:
                objeto = i
        for i in Dados.usuarios:
            if i.cpf==cpf and i.senha==senha:
                objeto = i
    except ValueError:
        print("Insira um cpf válido!")
        validandoLogin()
    return objeto   
def validandoEvento():
    evento = None
    nome_evento = input("Insira o nome do evento(Mínimo 5 caracteres):")
    while len(nome_evento)<5:
        nome_evento = input("Insira o nome do evento(Mínimo 5 caracteres):")
    sigla = input("Insira a sigla do evento(4 caracteres):")
    while len(sigla)!=4:
        sigla = input("Insira a sigla do evento(4 caracteres):")
    descricao = input("Insira a descrição do evento:")
    local = input("Insira o local do evento:")
    data_inicio = input("Insira a data do inicio do evento(DD/MM/AAAAA):")
    data_fim = input("Insira a data do fim do evento(DD/MM/AAAAA):")
    verificaCPF = False
    while verificaCPF==False:
        try:
            cpf = int(input("Informe o cpf do administrador do evento(Apenas Números):"))
            cpf = str(cpf)
            while len(cpf)!=11:
                cpf = int(input("Insira um cpf válido:"))
                cpf = str(cpf)
            while verificandoCPFadm(cpf)==None:
                print("CPF informado não está cadastrado como administrador de Eventos!")
                cpf = input("Informe o cpf do Administrador do evento(Apenas números):")
            
            verificaCPF = True
        except ValueError:
            print("CPF aceita apenas números:")
    
    verificaValor= False
    while verificaValor==False:
        try:
            valor_participante_profissional = float(input("Informe o valor do ingresso para participante profissional:"))
            valor_participante_estudante = float(input("Informe o valor do ingresso para participante estudante:"))
            verificaValor = True
        except ValueError:
            print("Valor informado inválido!")
    admEvento = verificandoCPFadm(cpf)
    evento = Evento(nome_evento,sigla,descricao,local,data_inicio,data_fim,admEvento,valor_participante_profissional,valor_participante_estudante)
    return evento

def main():
    opcao = 4
    while opcao!=3:
        print("=-="*10)
        print("Bem vindo ao Sistema de Eventos!\n1-Criar Conta\n2-Realizar Login\n3-Sair do Sistema")
        try:
            opcao = int(input("Escolha uma opção->"))
        except ValueError:
            print("Opção inválida!")
            main()
            
        if opcao==1:
            opcao=9
            while opcao!=5:
                print("=-="*10)
                print("1-Administrador Sistema\n2-Administrador Evento\n3-Participante Estudante\n4-Participante Profissional\n5-Menu Inicial")
                try:
                    opcao = int(input("Escolha um tipo de usuário->"))
                except ValueError:
                    print("Opção inválida!")
                    
                    
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
                elif opcao==5:
                    main()
                else:
                    print("Opção inválida!")
                        
        elif opcao==2:
            objeto = validandoLogin()
            if objeto==None:
                print("Login inválido")
            else:
                if objeto.tipo=="ADM_SISTEMA":
                    print("=-="*10)
                    opcao=11
                    while opcao!=10:
                        print("MENU DE ADMINISTRADOR DE SISTEMA\n1-Cadastrar Administrador de Sistema\n2-Cadastrar Administrador de Evento\n"
                                  +"3-Cadastrar Evento\n4-Remover Evento\n5-Remover Usuário\n6-Listar Eventos\n7-Exibir Relatório do Sistema\n"
                                  +"8-Exibir relatório por evento\n9-Deslogar\n10-Sair do sistema")
                        try:
                            opcao = int(input("Informe uma opção->"))
                        except ValueError:
                            print("Opção inválida!")
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
                    print("=-="*10)
                    opcao ==11
                    while opcao!=6:
                        print("MENU DE ADMINISTRADOR DE EVENTOS\n1-Alterar dados pessoais\n2-Listar Eventos\n"
                                  +"3-Desinscrever usuário do evento\n4-Exibir relatorio por evento\n5-Deslogar\n6-Sair do sistema")
                        try:
                            opcao = int(input("Insira uma opção->"))
                        except ValueError:
                            print("Opção inválida!")
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
                    print("=-="*10)
                    opcao == 11
                    while opcao!=6:
                        print("MENU DO PARTICIPANTE\n1-Alterar dados pessoais\n2-Listar Eventos inscritos\n3-Detalhar evento\n"
                                  +"4-Realizar Inscrição evento\n5-Deslogar\n6-Sair do sistema")
                        try:
                            opcao = int(input("Escolha uma opção:"))
                        except ValueError:
                            print("Opção inválida1")
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
    
        elif opcao==3:
            print("Volte sempre!")
            break
        else:
            print("Opção inválida!")
if __name__ == "__main__":
    main()
    
    
        
    
