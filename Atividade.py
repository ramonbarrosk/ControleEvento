class Usuario(object):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        self.nome = nome
        self.cpf = cpf
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
        self.participantes = []
       
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
class ParticipanteEstudante(Usuario):
    def __init__(self,nome,cpf,endereco,data_nascimento,senha):
        Usuario.__init__(self,nome,cpf,endereco,data_nascimento,senha)
        
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
def validandoUsuario():
    usuario = None
    try:
        nome = input("Informe seu nome:")
        if len(nome)==0:
            raise NameError("Insira um nome por favor!")
        cpf = int(input("Informe seu cpf(Apenas Números):"))
        cpf = str(cpf)
        if len(cpf)!=11:
            raise NameError("Insira um CPF válido")
        endereco = input("Informe seu endereço(Cidade,Bairro,Estado,CEP):")
        data_nascimento =  input("Informe a data de nascimento(DD/MM/AAAA):")
        if len(data_nascimento)!=10:
            raise NameError("Insira a data de nascimento por favor!")
        senha = input("Informe a senha:")
        if len(senha)==0:
            raise NameError("Insira uma senha por favor!")
    except ValueError:
        print("Insira apenas números no CPF!")
    except NameError as ex:
        print(ex.args)
    usuario = Usuario(nome,cpf,endereco,data_nascimento,senha)
    return usuario
def main():
    adm  = AdministradorSistema("ADM","1313","000","08/05/1995","123")
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
                    nome = usuario.nome
                    cpf = usuario.cpf
                    endereco = usuario.endereco
                    data_nascimento = usuario.data_nascimento
                    senha = usuario.senha
                    admSistema = AdministradorSistema(nome,cpf,endereco,data_nascimento,senha)
                    adm.cadastrarAdmSistema(admSistema)
                    print("Administrador Sistema criado com sucesso!")
                    
                    
                
            
            
            
            
            
    
if __name__ == "__main__":
    main()
    
    
        
    
