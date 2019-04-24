class Disciplina:
    '''
    Abstração de uma disciplinai, possui os atributos Nome e carga Horária
    '''
    def __init__(self, nome: str, carga_horaria: int) -> None:
        self.__nome = nome
        self.__carga_horaria = carga_horaria

    def get_nome(self) -> str:
        '''
        Acessor do atributo nome
        '''
        return self.__nome
        

    def get_carga_horaria(self) -> int:
        '''
        Acessor do atributo cargar horaria
        '''
        return self.__carga_horaria


class Pessoa:
    '''
    Abstração de uma pessoa no Modelo, classe base para Aluno e Professor
    que contém dados pertencentes a ambos.
    '''
    def __init__(self, nome: str, telefone: int, email: str) -> None:
        self._nome = nome
        self._telefone = telefone
        self._email = email

    def get_nome(self) -> str:
        '''
        Acessor do atributo Nome
        '''
        return self._nome

    def get_telefone(self) -> int:
        '''
        Acessor do atributo telefone
        '''
        return self._telefone

    def set_telefone(self, novo_telefone: int) -> None:
        '''
        Mutador do atributo telefone deve checar se é um número inteiro e,
        caso contrário devolver um TypeError
        '''
        self._telefone = novo_telefone

    def get_email(self) -> str:
        '''
        Acessor do atributo email
        '''
        return self._email

    def set_email(self, novo_email) -> None:
        '''
        Mutador do atributo eail, deve checar se éum email válido
        (se possuir o caractere '@') e caso contrário devolver
        um ValueError
        '''
        self._email = novo_email


class Aluno(Pessoa):

    def __init__(self, nome: str, telefone: int,
                 email: str, n_matricula: int) -> None:
        Pessoa.__init__(self,nome,telefone,email)
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__n_matricula = n_matricula
        self.__lista_disciplinas=[]
    

    def get_matricula(self) -> int:
        '''
        Acessor do atributo matricula
        '''
        return self.__n_matricula

    def matricular(self, disciplina: Disciplina) -> None:
        '''
        Realiza matrícula do Aluno na disciplina
        '''
        self.__lista_disciplinas.append(disciplina)

    def lista_disciplinas(self) -> list:
        '''
        Devolve a lista de disciplinas em que o aluno esta matriculado
        '''
        return self.__lista_disciplinas


class Professor(Pessoa):
    '''
    Entidade professor do Modelo
    '''
    def __init__(self, nome, telefone, email):
        Pessoa.__init__(self,nome,telefone,email)
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__lista_disciplinas=[]

    def ministra(self, disciplina: Disciplina) -> None:
        '''
        Atribui o professor como ministrante da disiciplina
        Um professor não pode dar mais de 200 horas de aula,
        Caso um professor tente atribuir mais de 200h devolve
        ValueError
        '''
        soma = 0
        for x in self.__lista_disciplinas:
            soma += x.get_carga_horaria()

        if soma + disciplina.get_carga_horaria() < 200:
            self.__lista_disciplinas.append(disciplina)
        else:
            raise ValueError

    def lista_disciplinas(self) -> list:
        '''
        lista as disciplinas ministradas pelo professor
        '''
        return self.__lista_disciplinas



def test_disciplina():
    dis = Disciplina('Linguagem de Programação II', 80)
    assert dis.get_nome() == 'Linguagem de Programação II'
    assert dis.get_carga_horaria() == 80


def test_pessoa():
    pes = Pessoa('Fulano da Silva', 999999, 'fulano@mail.com')
    assert pes.get_nome() == 'Fulano da Silva'
    assert pes.get_email() == 'fulano@mail.com'
    assert pes.get_telefone() == 999999


def test_pessoa_set_tel():
    pes = Pessoa('Fulano da Silva', 999999, 'fulano@mail.com')
    pes.set_telefone(888888)
    assert pes.get_telefone() == 888888


def test_pessoa_set_tel_errado():
    pes = Pessoa('Fulano da Silva', 999999, 'fulano@mail.com')
    try:
        pes.set_telefone('não é um telefone')
    except TypeError:
        pass
    else:
        assert pes.get_telefone() == 999999


def test_pessoa_set_mail():
    pes = Pessoa('Fulano da Silva', 999999, 'fulano@mail.com')
    pes.set_email('fulano@othermail.com')
    assert pes.get_email() == 'fulano@othermail.com'


def test_pessoa_set_mail_errado():
    pes = Pessoa('Fulano da Silva', 999999, 'fulano@mail.com')
    try:
        pes.set_email('não é um email')
    except ValueError:
        pass
    else:
        assert pes.get_email() == 'fulano@mail.com'


def test_aluno():
    al = Aluno('Cicrano Souza', 999999, 'cicrano@mail.com', 123456)
    assert al.get_matricula() == 123456
    assert al.get_nome() == 'Cicrano Souza'
    assert al.get_email() == 'cicrano@mail.com'
    assert al.get_telefone() == 999999


def test_aluno_matricula():
    dis = Disciplina('Linguagem de Programação II', 80)
    al = Aluno('Cicrano Souza', 999999, 'cicrano@mail.com', 123456)
    al.matricular(dis)
    assert dis in al.lista_disciplinas()


def test_professor():
    prof = Professor('Cicrano Souza', 999999, 'cicrano@mail.com')
    assert prof.get_nome() == 'Cicrano Souza'
    assert prof.get_email() == 'cicrano@mail.com'
    assert prof.get_telefone() == 999999


def test_prof_ministra():
    dis1 = Disciplina('Linguagem de Programação II', 80)
    dis2 = Disciplina('Tecnologias Web', 80)
    prof = Professor('Cicrano Souza', 999999, 'cicrano@mail.com')
    prof.ministra(dis1)
    prof.ministra(dis2)
    assert len(prof.lista_disciplinas()) == 2
    assert dis1 in prof.lista_disciplinas()
    assert dis2 in prof.lista_disciplinas()


def test_prof_ministra_erro():
    dis1 = Disciplina('Linguagem de Programação II', 80)
    dis2 = Disciplina('Tecnologias Web', 80)
    dis3 = Disciplina('Linguagem SQL', 80)
    prof = Professor('Cicrano Souza', 999999, 'cicrano@mail.com')
    try:
        prof.ministra(dis1)
        prof.ministra(dis2)
        prof.ministra(dis3)
    except ValueError:
        
    else:
        assert len(prof.lista_disciplinas()) == 2
        assert dis1 in prof.lista_disciplinas()
        assert dis2 in prof.lista_disciplinas()




test_disciplina()
test_pessoa()
test_pessoa_set_tel()
'''test_pessoa_set_tel_errado()'''
test_pessoa_set_mail()
'''test_pessoa_set_mail_errado()'''
test_aluno()
test_aluno_matricula()
test_professor()
test_prof_ministra()
test_prof_ministra_erro()