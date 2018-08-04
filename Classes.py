class Dados:
    eventos = []
    usuarios = []
    admEventos = []
    admSistema = []
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
    def cadastrarAdmEvento(self,administrador):
        Dados.admEventos.append(administrador)
    def cadastrarAdmSistema(self,administrador):
        Dados.admSistema.append(administrador)
    def cadastrarEvento(self,evento):
        Dados.eventos.append(evento)
    def removerEvento(self,sigla):
        evento = None
        for i in Dados.eventos:
            if i.sigla==sigla:
                evento = i
        if evento!=None:
            print("Evento excluído com sucesso!")
        else:
            print("Essa sigla não está cadastrada em nenhum evento no nosso sistema!")
    def removerUsuario(self,cpf):
        usuario = None
        for i in Dados.usuarios:
            if i.cpf == cpf:
                usuario = i
        if usuario!=None:
            Dados.usuarios.remove(usuario)
            print("Usuário removido com sucesso")
        else:
            print("CPF não encontrado como cadastrado!")
    def listarEventos(self):
        for i in Dados.eventos:
            print(i.nome_evento,"-",i.sigla)
    def relatorioSistema(self):
        participantesEstudantes = 0
        participantesProfissionais = 0
        for i in Dados.usuarios:
            if i.tipo=="PARTICIPANTE_ESTUDANTE":
                participantesEstudantes+=1
            elif i.tipo=="PARTICIPANTE_PROFISSIONAL":
                participantesProfissionais+=1
        print("Número de administradores do sistema: %i"%len(Dados.admSistema))
        print("Número de administradores de evento: %i"%len(Dados.admEventos))
        print("Número de participantes Estudantes: %i"%participantesEstudantes)
        print("Número de participantes Profissionais: %i"%participantesProfissionais)
        print("Número de eventos cadastrados: %i"%len(Dados.eventos))
    def relatorioEvento(self,sigla_evento):
        evento = None 
        for i in Dados.eventos:
            if i.sigla == sigla_evento:
                evento = i
        if evento!=None:
            print("Dados do Eventos:\n %s\n%s\n%s"%(i.nome_evento,i.sigla,i.local))
        else:
            print("Sigla não encontrado nos eventos cadastrados!")
    def deslogar(self):
        main()
class AdministradorEvento(Usuario):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        Usuario.__init__(self,nome,cpf,endereco,data_nascimento,senha)
        self.tipo = None
    def alterarDadosPessoais(self):
        print("O que deseja alterar?\n1-Nome\n2-Endereco\n3-Data de Nascimento\n4-Senha")
        opcao = int(input())
        if opcao==1:
            nome = input("Informe seu novo nome:")
            self.nome = nome
        elif opcao==2:
            endereco = input("Informe seu novo endereço:")
            self.endereco = endereco
        elif opcao==3:
            data_nascimento = input("Informe sua data de nascimento")
            self.data_nascimento = data_nascimento
        elif opcao==4:
            senha = input("Informe sua nova senha:")
            self.senha = senha
        else:
            print("Opção inválida")
    def listarEventos(self):
        eventos = []
        for i in Dados.eventos:
            if i.administrador_evento.cpf==self.cpf:
                eventos.append(i)
        for i in eventos:
            print("Nome do evento: %s -- Sigla: %s"%(i.nome_evento,i.sigla))
    def desinscreverUsuarioEvento(self,cpf,sigla):
        evento = None
        removido = False
        for i in Dados.eventos:
            if i.sigla==sigla:
                evento = i
        if evento!=None:
            if evento.administrador_evento.cpf==self.cpf:
                for i in Dados.usuarios:
                    if i.cpf==cpf:
                        removido = True
            else:
                print("Administrador não tem permissão nesse evento!")
        else:
            print("Sigla não encontrada no sistema!")
        if removido==True:
            print("Usuário removido com sucesso!")
        else:
            print("CPF não encontrado no sistema!")
    def relatorioEvento(self,sigla):
        evento = None
        for i in Dados.eventos:
            if i.sigla==sigla:
                evento = i
        if evento.administrador_evento.cpf==self.cpf:
           print("%s - %s\nLocal: %s\nDescrição:%s\nData Inicio:%s\nData fim:%s\nAdministrador Evento:%s"%(evento.nome_evento,evento.sigla,evento.descricao,evento.data_inicio,evento.data_fim,self.nome))
           print("CATEGORIA ESTUDANTE:")
           for i in evento.participantes:
               if i.tipo=="PARTICIPANTE_ESTUDANTE":
                   print("Nome: %s"%i.nome)
           print("CATEGORIA ESTUDANTE:")
           for i in evento.participantes:
               if i.tipo=="PARTICIPANTE_PROFISSIONAL":
                   print("Nome: %s"%i.nome)
           print("Valor arrecadado:",evento.valor_arrecadado)
        else:
                 print("Administrador do evento não tem permissão!")
class Participante(Usuario):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        Usuario.__init__(self,nome,cpf,endereco,data_nascimento,senha)
        self.tipo = None
    def alterarDados(self):
        print("O que deseja alterar?\n1-Nome\n2-Endereco\n3-Data de Nascimento\n4-Senha")
        opcao = int(input())
        if opcao==1:
            nome = input("Informe seu novo nome:")
            self.nome = nome
        elif opcao==2:
            endereco = input("Informe seu novo endereço:")
            self.endereco = endereco
        elif opcao==3:
            data_nascimento = input("Informe sua data de nascimento")
            self.data_nascimento = data_nascimento
        elif opcao==4:
            senha = input("Informe sua nova senha:")
            self.senha = senha
        else:
            print("Opção inválida")
    def listarEventosInscritos(self):
        eventos = []
        for i in Dados.eventos:
            for x in i.participantes:
                if x.cpf==self.cpf:
                    eventos.append(i)
        for i in eventos:
            print("Nome evento:%s -- Sigla: %s"%(i.nome_evento,i.sigla))
    def detalheEvento(self,sigla):
        evento = None
        for i in Dados.eventos:
            if i.sigla==sigla:
                evento = i
        if evento!=None:
            print("Detalhe Evento\nNome do evento:%s\nSigla:%s"%(evento.nome_evento,evento.sigla))
        else:
            print("Sigla não encontrada no sistema!")
    def realizarInscricaoEvento(self,sigla):
        usuario = Participante(self.nome,self.cpf,self.endereco,self.data_nascimento,self.senha)
        usuario.tipo = self.tipo
        evento = None
        inscrito = False
        for i in Dados.eventos:
            if i.sigla==sigla:
                evento = i
        for i in evento.participantes:
            if i.cpf==self.cpf:
                inscrito = True
        if evento!=None:
            if inscrito==True:
                print("Você já está inscrito nesse evento!")
            else:
                if self.tipo == "PARTICIPANTE_ESTUDANTE":
                    evento.participantes.append(usuario)
                    evento.valor_arrecadado+=(evento.valor_estudante)
                    print("Participante estudante inscrito com sucesso!")
                elif self.tipo == "PARTICIPANTE_PROFISSIONAL":
                    evento.participantes.append(usuario)
                    evento.valor_arrecadado+=(evento.valor_profissional)
                    print("Participante profissional inscrito com sucesso!")
        else:
            print("Sigla não encontrada no sistema!")
    def deslogar(self):
        main()
