#OBJETOS DO PROGRAMA
class Usuario(object):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.senha = senha
class Evento(object):
    def __init__(self,nome_evento,sigla,descricao,local,data_inicio,data_fim,administrador_evento,valor_profissional,valor_estudante):
        self.valor_arrecadado = 0
        self.nome_evento = nome_evento
        self.sigla = sigla
        self.descricao = descricao
        self.local = local
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.administrador_evento = administrador_evento
        self.valor_profissional = valor_profissional
        self.valor_estudante = valor_estudante
        self.participantes = []
class AdministradorSistema(Usuario):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        Usuario.__init__(self,nome,cpf,endereco,data_nascimento,senha)
        self.tipo = None
        self.admEventos = []
        self.admSistema = []
        self.eventos = []
        self.participantes = []
    def cadastrarAdmEvento(self,administrador):
        self.admEventos.append(administrador)
    def cadastrarAdmSistema(self,administrador):
        self.admSistema.append(administrador)
    def cadastrarEvento(self,evento):
        self.eventos.append(evento)
    def removerEvento(self,sigla):
        excluido = False
        for i in self.eventos:
            if i.sigla==sigla:
                self.eventos.remove(evento)
                excluido = True
        if excluido ==True:
            print("Evento excluído com sucesso!")
        else:
            print("Essa sigla não está cadastrada em nenhum evento no nosso sistema!")
    def removerUsuario(self,cpf):
        excluido = False
        for i in self.partc
    def listarEventos(self):
        for i in self.eventos:
            print(i.nome_eventos,"-",i.sigla)
    def relatorioSistema(self):
        print("Número de administradores do sistema: %i"%len(self.admSistema))
        print("Número de administradores de evento: %i"%len(self.admEvento))
        print("Número de participantes Estudantes: %i"%len(self.participantesEstudante))
        print("Número de participantes Profissionais: %i"%len(self.participantesProfissional))
        print("Número de eventos cadastrados: %i"%len(self.eventos))
        
    def relatorioEvento(self,sigla_evento):
        evento = None 
        for i in self.eventos:
            if i.sigla == sigla_evento:
                evento = i
        print("Dados do Eventos:\n %s\n%s\n%s"%(i.nome,i.sigla,i.local))
    def deslogar(self):
        main()
class AdministradorEvento(AdministradorSistema):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        Usuario.__init__(self,nome,cpf,endereco,data_nascimento,senha)
        self.tipo = None
    def alterarDadosPessoais(self,usuario):
        print("O que deseja alterar?\n1-Nome\n2-Endereco\n3-Data de Nascimento\n4-Senha")
        opcao = int(input())
        if opcao==1:
            nome = input("Informe seu novo nome:")
            usuario.nome = nome
        elif opcao==2:
            endereco = input("Informe seu novo endereço:")
            nome.endereco = endereco
        elif opcao==3:
            data_nascimento = input("Informe sua data de nascimento")
            usuario.data_nascimento = data_nascimento
        elif opcao==4:
            senha = input("Informe sua nova senha:")
            usuario.senha = senha
        else:
            print("Opção inválida")
class ParticipanteEstudante(Usuario):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        Usuario.__init__(self,nome,cpf,endereco,data_nascimento,senha)
        self.tipo = None
        
class ParticipanteProfissional(Usuario):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        Usuario.__init__(self,nome,cpf,endereco,data_nascimento,senha)
        self.tipo = None
    def alterarDados(self):
        pass
    def listarEventosInscritos(self):
        pass
    def detalheEvento(self,sigla):
        pass
    def realizarInscricaoEvento(self,sigla):
        pass
    def deslogar(self):
        main()

        
#FUNÇÕES DE VALIDAÇÃO E O MAIN
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
def verificandoCPFadm(adm,cpf):
    adm = None
    for i in adm.admEventos:
        if i.cpf==cpf:
            adm = i
    return adm
def retornaEvento(adm,sigla):
    evento = None
    for i in adm.eventos:
        if i.sigla==sigla:
            evento = i
    return evento
def validandoUsuario(adm):
    usuario = None
    nome = input("Informe seu nome:")
    while len(nome)==0:
        nome = input("Por favor insira seu nome:")
    cpf = int(input("Informe seu cpf(Apenas Números):"))
    cpf = str(cpf)
    while len(cpf)!=11:
        print("Insira um CPF válido")
        cpf = input("Informe seu cpf(Apenas Números):")
    while (verificandoCPF(adm,cpf)):
        print("CPF já existi, insira outro!")
        cpf = input("Informe seu cpf(Apenas Números):")
        
    endereco = input("Informe seu endereço(Cidade,Bairro,Estado,CEP):")
    data_nascimento = input("Informe a data de nascimento(DD/MM/AAAA):")
    while len(data_nascimento)!=10:
        print("Insira a data de nascimento por favor!")
        data_nascimento = input("Informe a data de nascimento(DD/MM/AAAA):")
    senha = input("Informe a senha:")
    while len(senha)==0:
        print("Insira uma senha por favor!")
        senha = input("Informe a senha:")
    usuario = Usuario(nome,cpf,endereco,data_nascimento,senha)
    return usuario
def validandoLogin():
    cpf = input("Insira seu CPF(Apenas Números):")
    senha = input("Insira sua senha:")
    objeto = None
    
    for i in adm.admSistema:
        if i.cpf==cpf and i.senha==senha:
            objeto = i
            
    for i in adm.admEventos:
        if i.cpf==cpf and i.senha==senha:
            objeto = i
            
    for i in adm.participantes:
        if i.cpf==cpf and i.senha==senha:
            objeto = i
    return objeto   
def validandoEvento(adm):
    evento = None
    nome_evento = input()
    while len(nome_evento)==0:
        print("Por favor insira o nome do evento!")
        nome_evento = input()
    sigla = input()
    while len(sigla==0):
        print("Por favor insira a sigla do evento!")
        sigla = input()
    descricao = input("Insira a descrição do evento:")
    local = input("Insira o local do evento:")
    data_inicio = input("Insira a data do inicio do evento(DD/MM/AAAAA):")
    while len(data_nascimento)!=10:
        print("Insira a data de nascimento por favor!")
        data_inicio = input("Informe a data de nascimento(DD/MM/AAAA):")
    data_fim = input("Insira a data do fim do evento(DD/MM/AAAAA):")
    while len(data_nascimento)!=10:
        print("Insira a data de nascimento por favor!")
        data_fim = input("Informe a data de nascimento(DD/MM/AAAA):")
    cpf = int(input("Informe o cpf do Administrador do evento:"))
    cpf = str(cpf)
    while len(cpf)!=11:
        print("Insira um CPF válido")
        cpf = input("Informe o cpf do Administrador do evento::")
    while verificandoCPFadm(adm,cpf)==None:
        print("CPF informado não está cadastrado como administrador de Eventos!")
        cpf = input("Informe o cpf do Administrador do evento::")
    admEvento = verificandoCPFadm(adm,cpf)
    valor_participante_profissional = float(input("Informe o valor do ingresso para participante profissional:"))
    valor_participante_estudante = float(input("Informe o valor do ingresso para participante estudante:"))
                                            
    evento = Evento(nome_evento,sigla,descricao,local,data_inicio,data_fim,admEvento,valor_participante_profissional,valor_participante_estudante)
    return evento
    
def admSistema(objeto):
    print("MENU DE ADMINISTRADOR DE SISTEMA\n1-Cadastrar Administrador de Sistema\n2-Cadastrar Administrador de Evento\n3-Cadastrar Evento\n4-Remover Evento\n5-Remover Usuário\n6-Listar Eventos\n7-Exibir Relatório do Sistema\n8-Exibidr relatório por evento\n9-Deslogar")
    if opcao==1:
        usuario = validandoUsuario()
        objeto.cadastrarAdmSistema(usuario)
        print("ADM de Sistema cadastrado com sucesso!")
    elif opcao==2:
        usuario = validandoUsuario()
        objeto.cadastrarAdmEvento(usuario)
        print("AMD de Evento cadastrado com sucesso!")
    elif opcao==3:
        evento = validandoEvento(objeto)
        objeto.cadastrarEvento(evento)
        print("Evento cadastrado com sucesso")
    elif opcao==4:
        sigla = input("Informe a sigla do evento a ser excluído:")
        objeto.removerEvento(sigla)
    elif opcao==5:
        cpf = input("Informe o cpf do usuario a ser excluído:")
        objeto.removerUsuario(cpf)
        
    
def main():
    adm  = AdministradorSistema("ADM_MASTER","11111111111","Indefinido","08/05/1995","ADM_MASTER")
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
                    usuario = validandoUsuario(adm)
                    admSistema = AministradorSistema(usuario.nome,usuario.cpf,usuario.endereco,usuario.data_nascimento,usuario.senha)
                    admSistema.tipo = "ADM_SISTEMA"
                    adm.cadastrarAdmSistema(admSistema)
                    print("Administrador Sistema criado com sucesso!")
                elif opcao==2:
                    usuario = validandoUsuario(adm)
                    admEvento = AdministradorEvento(usuario.nome,usuario.cpf,usuario.endereco,usuario.data_nascimento,usuario.senha)
                    admdEvento.tipo = "ADM_EVENTO"
                    adm.cadastrarAdmEvento(admEvento)
                    print("Administrador Evento criado com sucesso!")
                elif opcao==3:
                    usuario = validandoUsuario(adm)
                    participanteEstudante = ParticipanteEstudante(usuario.nome,usuario.cpf,usuario.endereco,usuario.data_nascimento,usuario.senha)
                    participanteEstudante.tipo = "PARTICIPANTE_ESTUDANTE"
                    adm.participantes.append(participanteEstudante)
                    print("Participante Estudante criado com sucesso!")
                elif opcao==4:
                    usuario = validandoUsuario(adm)
                    participanteProfissional = ParticipanteProfissional(usuario.nome,usuario.cpf,usuario.endereco,usuario.data_nascimento,usuario.senha)
                    participanteProfissional.tipo = "PARTICIPANTE_PROFISSIONAL"
                    adm.participantes.append(participanteProfissional)
                    print("Participante Profissional criado com sucesso!")
        elif opcao==2:
            objeto = validandoLogin()
            if objeto==None:
                print("Login inválido")
            else:
                if objeto.tipo=="ADM_SISTEMA":
                    admSistema(objeto)
                
            
                
if __name__ == "__main__":
    main()
    
    
        
    
