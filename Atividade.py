class Usuario(object):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        self.nome = nome
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.senha = senha
        
class Evento(object):
    def __init__(self,nome_evento,sigla,descricao,local,data_inicio,data_fim,administrador_evento,valor_profissional,valor_estudante,participantes):
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
        self.admEventos = []
        self.admSistema = []
        self.eventos = []
        self.participantesEstudante = []
        self.participantesProfissional = []
    def cadastrarAdmEvento(self,administrador):
        self.admEventos.append(administrador)
    def cadastrarAdmSistema(self,administrador):
        self.admSistema.append(administrador)
    def cadastrarEvento(self,evento):
        self.eventos.append(evento)
    def removerEvento(self,evento):
        self.eventos.remove(evento)
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
class ParticipanteProfissional(Usuario):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        Usuario.__init__(self,nome,cpf,endereco,data_nascimento,senha)
        self.tipo_participante = None
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
def validandoConta():
    try:
        nome = input("Informe seu nome:")
        if len(nome)==0:
            raise ValueError("Insira um nome por favor!")
        cpf = int(input("Informe seu cpf(Apenas Números):"))
        if len(cpf)==0:
            raise ValueError("Insira um CPF por favor!")
        endereco = input("Informe seu endereço(Cidade,Bairro,Estado,CEP):")
        data_nascimento =  input("Informe a data de nascimento:")
        if len(data_nascimento)==0:
            raise ValueError("Insira a data de nascimento por favor!")
        senha = input("Informe a senha:")
        if len(senha)==0:
            raise ValueError("Insira uma senha por favor!")
        tipo = input("Você é Participante Profissional ou Estudante?").upper()
        if tipo!="PROFISSIONAL" or tipo!="ESTUDANTE":
            raise ValueError("Apenas PROFISSIONAL OU ESTUDANTE")
    except ValueError as ex:
        print(ex.args())
def main():
    opcao = 4
    while opcao!=3:
        print("Bem vindo ao Sistema de Eventos!\n1-Criar Conta\n2-Realizar Login\n3-Sair do Sistema")
        opcao = int(input("Escolha uma opção->"))
        if opcao==1:
            validandoConta()
            
    
if __name__ == "__main__":
    main()
    
    
        
    
