from Classes import *
from datetime import *
def verificandoCPFadm(cpf):
    objeto = None
    for i in Dados.admEventos:
        if i.cpf==cpf:
            objeto = i
    return objeto
def validandoData(data):
    data2 = None
    dataBol = False
    while dataBol==False:
        try:
            hoje = datetime.now()
            dia_atual = hoje.day
            mes_atual = hoje.month
            ano_atual = hoje.year
            dia,mes,ano = data.split("/")
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
            while ano<ano_atual or (mes<mes_atual and ano==ano_atual) or (mes==mes_atual and ano==ano_atual and dia<dia_atual):
                data_inicio = input("Por favor, insira uma data válida(DD/MM/AAAA):")
                dia,mes,ano = data_inicio.split("/")
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
            while dia>31:
                print("Insira uma data válida!")
                data_nascimento = input("Informe um dia válido(DD/MM/AAAA):")
                dia,mes,ano = data_nascimento.split("/")
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
            while mes>12:
                print("Insira um mês válido!")
                data_nascimento = input("Informe um mês válido(DD/MM/AAAA):")
                dia,mes,ano = data_nascimento.split("/")
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
        except ValueError:
            print("Insira uma data válida!")
        data2 = data
        dataBol = True
    return data2
    
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
    endereco = input("Informe seu endereço(Opcional):")
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
            while ano>=2003:
                print("Idade mínima: 15 anos")
                data_nascimento = input("Informe a data de nascimento(DD/MM/AAAA):")
                dia,mes,ano = data_nascimento.split("/")
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
            while ano<=1900:
                print("Insira um ano inválido")
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
        if cpf==0:
            main()
        else:
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
                    objeto = id
    except ValueError:
        print("Insira um cpf válido!")
        validandoLogin()
    return objeto
def login():
    print("=-="*15)
    print("Login(Aperte 0 e Enter para voltar pro menu inicial)")
    objeto = validandoLogin()
    if objeto==None:
        print("Login inválido")
    else:
        if objeto.tipo=="ADM_SISTEMA":
            print("=-="*10)
            opcao=11
            while opcao!=9:
                print("MENU DE ADMINISTRADOR DE SISTEMA\n1-Cadastrar Administrador de Sistema\n2-Cadastrar Administrador de Evento\n"
                                  +"3-Cadastrar Evento\n4-Remover Evento\n5-Remover Usuário\n6-Listar Eventos\n7-Exibir Relatório do Sistema\n"
                                  +"8-Exibir relatório por evento\n9-Deslogar")
                try:
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
                        print("=-="*15)
                        evento = validandoEvento()
                        Dados.eventos.append(evento)
                        print("Evento cadastrado com sucesso")
                        print("=-="*15)
                    elif opcao==4:
                        sigla = input("Informe a sigla do evento a ser excluído:").upper()
                        objeto.removerEvento(sigla)
                    elif opcao==5:
                        cpf = input("Informe o cpf do usuario a ser excluído:")
                        objeto.removerUsuario(cpf)
                    elif opcao==6:
                        objeto.listarEventos()
                    elif opcao==7:
                        objeto.relatorioSistema()
                    elif opcao==8:
                        sigla = input("Informe a sigla do evento a ser detalhado:").upper()
                        objeto.relatorioEvento(sigla)
                    elif opcao==9:
                        print("Usuário deslogado")
                        login()
                    else:
                        print("Opção inválida!")
                except ValueError:
                    print("Opção inválida!")
                    
                        
        elif objeto.tipo=="ADM_EVENTO":
            print("=-="*10)
            opcao = 11
            while opcao!=5:
                print("MENU DE ADMINISTRADOR DE EVENTOS\n1-Alterar dados pessoais\n2-Listar Eventos\n"
                                  +"3-Desinscrever usuário do evento\n4-Exibir relatorio por evento\n5-Deslogar")
                try:
                    opcao = int(input("Insira uma opção->"))
                    if opcao==1:
                        objeto.alterarDadosPessoais()
                    elif opcao==2:
                        objeto.listarEventos()
                    elif opcao==3:
                        cpf = input("Informe o cpf do usuário:")
                        sigla = input("Informe a sigla do evento:").upper()
                        objeto.desinscreverUsuarioEvento(cpf,sigla)
                    elif opcao==4:
                        sigla = input("Insira a sigla do evento:").upper()
                        objeto.relatorioEvento(sigla)
                    elif opcao==5:
                        print("Usuário deslogado!")
                        login()
                    else:
                        print("Opção inválida!")
                except ValueError:
                    print("Opção inválida!")
            
        elif objeto.tipo=="PARTICIPANTE_ESTUDANTE" or objeto.tipo=="PARTICIPANTE_PROFISSIONAL":
            print("=-="*10)
            opcao == 11
            while opcao!=5:
                print("MENU DO PARTICIPANTE\n1-Alterar dados pessoais\n2-Listar Eventos inscritos\n3-Detalhar evento\n"
                                  +"4-Realizar Inscrição evento\n5-Deslogar")
                try:
                    opcao = int(input("Escolha uma opção:"))
                except ValueError:
                    print("Opção inválida1")
                if opcao==1:
                    objeto.alterarDadosPessoais()
                elif opcao==2:
                            
                    objeto.listarEventosInscritos()
                elif opcao==3:
                    sigla = input("Insira a sigla do evento a ser detalhado:").upper()
                    objeto.detalheEvento(sigla)
                elif opcao==4:
                    sigla = input("Insira a sigla do evento no qual quer se inscrever:").upper()
                    objeto.realizarInscricaoEvento(sigla)
                elif opcao==5:
                    print("Usuário deslogado!")
                    login()
                        
                else:
                    print("Opção inválida!")
            
def validandoEvento():
    evento = None
    nome_evento = input("Insira o nome do evento(Mínimo 5 caracteres):").upper()
    while len(nome_evento)<5:
        nome_evento = input("Insira o nome do evento(Mínimo 5 caracteres):").upper()
    sigla = input("Insira a sigla do evento(4 caracteres):").upper()
    while len(sigla)!=4:
        sigla = input("Insira a sigla do evento(4 caracteres):")
    descricao = input("Insira a descrição do evento:").upper()
    while len(descricao)==0:
        descricao = input("Por favor, insira alguma descrição do evento:").upper()
    local = input("Insira o local do evento:").upper()
    while len(local)==0:
        local = input("Por favor, insira algum local do evento:").upper()
    data_inicio = input("Insira a data de início do evento(DD/MM/AAAA):")
    while len(data_inicio)!=10:
        data_inicio = input("Insira uma data válida(DD/MM/AAAA):")
    data_inicio = validandoData(data_inicio)
    data_fim = input("Insira a data do fim do evento(DD/MM/AAAA):")
    while len(data_fim)!=10:
        data_fim = input("Insira uma data válida(DD/MM/AAAA):")
    data_fim = validandoData(data_fim)
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
            print("CPF aceita apenas números!")
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
                except ValueError:
                    print("Opção inválida!")
                        
        elif opcao==2:
            login()
        elif opcao==3:
            print("Volte sempre!")
            break
        else:
            print("Opção inválida!")
if __name__ == "__main__":
    main()
    
    
        
    
