from models import Session, Profissao, Livro, create_tables


create_tables()


def salvar_profissao(nome, salario):

    try:

        salario_float = float(salario)
        

        session = Session()
        

        nova_profissao = Profissao(nome=nome, salario=salario_float)
        

        session.add(nova_profissao)
        session.commit()
        

        session.close()
        
        return True
    except Exception as e:
        print(f"Erro ao salvar profissão: {e}")
        return False

def listar_profissoes():

    try:

        session = Session()
        

        profissoes = session.query(Profissao).all()
        

        session.close()
        
        return profissoes
    except Exception as e:
        print(f"Erro ao listar profissões: {e}")
        return []


def salvar_livro(titulo, autor, ano=""):

    try:

        session = Session()
        

        novo_livro = Livro(titulo=titulo, autor=autor, ano=ano)
        

        session.add(novo_livro)
        session.commit()
        

        session.close()
        
        return True
    except Exception as e:
        print(f"Erro ao salvar livro: {e}")
        return False

def listar_livros():

    try:

        session = Session()
        

        livros = session.query(Livro).all()
        

        session.close()
        
        return livros
    except Exception as e:
        print(f"Erro ao listar livros: {e}")
        return []

def obter_livro_por_id(livro_id):

    try:

        session = Session()
        

        livro = session.query(Livro).filter(Livro.id == livro_id).first()
        

        session.close()
        
        return livro
    except Exception as e:
        print(f"Erro ao obter livro: {e}")
        return None
