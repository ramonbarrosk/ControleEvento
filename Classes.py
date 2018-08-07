class Dados:
    valor_total = 0
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
        print("=-="*15)
        evento = None
        for i in Dados.eventos:
            if i.sigla==sigla:
                evento = i
        if evento!=None:
            Dados.eventos.remove(evento)
            print("Evento excluído com sucesso!")
        else:
            print("Sigla não encontrada no sistema!")
        print("=-="*15)
    def removerUsuario(self,cpf):
        print("=-="*15)
        usuario = None
        for i in Dados.usuarios:
            if i.cpf == cpf:
                usuario = i
        if usuario!=None:
            Dados.usuarios.remove(usuario)
            for i in Dados.eventos:
                for x in i.participantes:
                    if x.cpf==cpf:
                        i.participantes.remove(x)
            print("Usuário removido com sucesso")
        else:
            print("CPF não encontrado como cadastrado!")
        print("=-="*15)
    def listarEventos(self):
        for i in Dados.eventos:
            print("=-="*15)
            print("Nome do evento:%s\nSigla:%s"%(i.nome_evento,i.sigla))
            print("=-="*15)
    def relatorioSistema(self):
        participantesEstudantes = 0
        participantesProfissionais = 0
        print("=-="*15)
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
        print("Valor arrecadado no total: %.2f"%Dados.valor_total)
        print("=-="*15)
    def relatorioEvento(self,sigla_evento):
        print("=-="*15)
        evento = None 
        for i in Dados.eventos:
            if i.sigla == sigla_evento:
                evento = i
        if evento!=None:
            print("=-="*15)
            print("Dados do Evento\nNome do evento: %s\nSigla: %s\nDescrição: %s\nLocal: %s"%(evento.nome_evento,evento.sigla,evento.descricao,evento.local))
            print("Data de início: %s\nData de fim: %s\nAdministrador do evento: %s"%(evento.data_inicio,evento.data_fim,evento.administrador_evento.nome))
            print("Valor por estudante: %.2f\nValor por profissional: %.2f"%(evento.valor_estudante,evento.valor_profissional))
            print("Valor arrecadado:%.2f"%evento.valor_arrecadado)
            print("Participantes estudantes")
            for i in evento.participantes:
                if i.tipo == "PARTICIPANTE_ESTUDANTE":
                    print("Nome do participante: %s"%i.nome)
            print("Participantes profissionais")
            for i in evento.participantes:
                if i.tipo=="PARTICIPANTE_PROFISSIONAL":
                    print("Nome do participante: %s"%i.nome)
        else:
            print("Sigla não encontrada no sistema!")
        print("=-="*15)
class AdministradorEvento(AdministradorSistema):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        Usuario.__init__(self,nome,cpf,endereco,data_nascimento,senha)
        self.tipo = None
    def alterarDadosPessoais(self):
        print("=-="*15)
        print("O que deseja alterar?\n1-Nome\n2-Endereco\n3-Data de Nascimento\n4-Senha")
        try:
            opcao = int(input("Insira uma opção:"))
            if opcao==1:
                nome = input("Informe seu novo nome:")
                self.nome = nome
                print("Nome alterado com sucesso!")
            elif opcao==2:
                endereco = input("Informe seu novo endereço:")
                self.endereco = endereco
                print("Endereço alterado com sucesso!")
            elif opcao==3:
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
                self.data_nascimento = data_nascimento
                print("Data de nascimento alterada com sucesso!")
            elif opcao==4:
                senha = input("Informe sua nova senha:")
                while len(senha)<4:
                    senha = input("Senha deve ter mais que 3 caracteres::")
                    
                self.senha = senha
                print("Senha alterada com sucesso!")
            else:
                print("Opção inválida")
            
        except ValueError:
            print("Opção inválida!")
        print("=-="*15)
    def relatorioEvento(self,sigla_evento):
        print("=-="*15)
        evento = None 
        for i in Dados.eventos:
            if i.sigla == sigla_evento:
                evento = i
        if evento!=None:
            if evento.administrador_evento.cpf==self.cpf:
                print("=-="*15)
                print("Dados do Evento\nNome do evento: %s\nSigla: %s\nDescrição: %s\nLocal: %s"%(evento.nome_evento,evento.sigla,evento.descricao,evento.local))
                print("Data de início: %s\nData de fim: %s\nAdministrador do evento: %s"%(evento.data_inicio,evento.data_fim,evento.administrador_evento.nome))
                print("Valor por estudante: %.2f\nValor por profissional: %.2f"%(evento.valor_estudante,evento.valor_profissional))
                print("Valor arrecadado:%.2f"%evento.valor_arrecadado)
                print("Participantes estudantes")
                for i in evento.participantes:
                    if i.tipo == "PARTICIPANTE_ESTUDANTE":
                        print("Nome do participante: %s"%i.nome)
                print("Participantes profissionais")
                for i in evento.participantes:
                    if i.tipo=="PARTICIPANTE_PROFISSIONAL":
                        print("Nome do participante: %s"%i.nome)
            else:
                print("Você não tem permissão para ver esse evento!")
        else:
            print("Sigla não encontrada no sistema!")
        print("=-="*15)
    def listarEventos(self):
        print("=-="*15)
        eventos = []
        for i in Dados.eventos:
            if i.administrador_evento.cpf==self.cpf:
                eventos.append(i)
        for i in eventos:
            print("Nome do evento: %s -- Sigla: %s"%(i.nome_evento,i.sigla))
        print("=-="*15)
    def desinscreverUsuarioEvento(self,cpf,sigla):
        print("=-="*15)
        evento = None
        removido = False
        for i in Dados.eventos:
            if i.sigla==sigla:
                evento = i
        if evento!=None:
            if evento.administrador_evento.cpf==self.cpf:
                for i in Dados.usuarios:
                    if i.cpf==cpf:
                        Dados.usuarios.remove(i)
                        removido = True
            else:
                print("Administrador não tem permissão nesse evento!")
        else:
            print("Sigla não encontrada no sistema!")
        if removido==True:
            print("Usuário removido com sucesso!")
        else:
            print("CPF não encontrado no sistema!")
        print("=-="*15)
class Participante(AdministradorEvento):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        Usuario.__init__(self,nome,cpf,endereco,data_nascimento,senha)
        self.tipo = None
    def listarEventosInscritos(self):
        print("=-="*15)
        eventos = []
        for i in Dados.eventos:
            for x in i.participantes:
                if x.cpf==self.cpf:
                    eventos.append(i)
        for i in eventos:
            print("Nome evento: %s  Sigla: %s"%(i.nome_evento,i.sigla))
        print("=-="*15)
    def detalheEvento(self,sigla):
        print("=-="*15)
        evento = None
        for i in Dados.eventos:
            if i.sigla==sigla:
                evento = i
        if evento!=None:
            print("Dados do Evento\nNome do evento: %s\nSigla: %s\nDescrição: %s\nLocal: %s"%(evento.nome_evento,evento.sigla,evento.descricao,evento.local))
            print("Data de início: %s\nData de fim: %s\nAdministrador do evento: %s"%(evento.data_inicio,evento.data_fim,evento.administrador_evento.nome))
            print("Valor por estudante: %.2f\nValor por profissional: %.2f"%(evento.valor_estudante,evento.valor_profissional))
        else:
            print("Sigla não encontrada no sistema!")
        print("=-="*15)
    def realizarInscricaoEvento(self,sigla):
        print("=-="*15)
        usuario = Participante(self.nome,self.cpf,self.endereco,self.data_nascimento,self.senha)
        usuario.tipo = self.tipo
        evento = None
        inscrito = False
        for i in Dados.eventos:
            if i.sigla==sigla:
                evento = i
        
        if evento!=None:
            for i in evento.participantes:
                if i.cpf==self.cpf:
                    inscrito = True
            if inscrito==True:
                print("Você já está inscrito nesse evento!")
            else:
                
                if self.tipo == "PARTICIPANTE_ESTUDANTE":
                    evento.participantes.append(usuario)
                    evento.valor_arrecadado+=(evento.valor_estudante)
                    Dados.valor_total+=(evento.valor_estudante)
                    print("Participante estudante inscrito com sucesso!")
                elif self.tipo == "PARTICIPANTE_PROFISSIONAL":
                    evento.participantes.append(usuario)
                    evento.valor_arrecadado+=(evento.valor_profissional)
                    Dados.valor_total+=(evento.valor_profissional)
                    print("Participante profissional inscrito com sucesso!")
        else:
            print("Sigla não encontrada no sistema!")
        print("=-="*15)
    
