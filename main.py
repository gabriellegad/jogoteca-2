from flask import Flask, render_template, request

class Jogo :
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Resident Evil: Village', 'Tiro, Zombie', 'Playstation')
jogo2 = Jogo('God of War', 'Ação', 'Playstation')
jogo3 = Jogo('The last of us', 'Ação, Zombie', 'Playstation')
jogo4 = Jogo('The Dark Pictures Anthology: Man of Medan',
             'Survival horror, Narrativa interativa, Adventure', 'Playstation')
jogo5 = Jogo('Uncharted: The lost legacy', 'Ação, Aventura, Tiro',
             'Playstation')
jogo6 = Jogo('Mortal Kombat', 'Luta, Multiplayer', 'Playstation')
jogo7 = Jogo('Horizon zero Down', 'Exploração, Aventura', 'Playstation')
jogo8 = Jogo('Last day of june',
             ' aventura, independente, quebra-cabeça, Adventure',
             'Playstation')
jogo9 = Jogo('Far Cry: Primal', 'Aventura, Exploração, Mundo aberto',
             'Playstation')

lista = [jogo1, jogo2, jogo3, jogo4, jogo5, jogo6, jogo7, jogo8, jogo9]

app = Flask(__name__)
app.secret_key = 'gad'

@app.route('/')
def ola():
    return render_template('lista.html', titulo='Meus Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Meus Jogos')

@app.route('/sobre')
def sobre():
    return render_template('novo.html', titulo='Meus Jogos')

@app.route('/criar', methods=[
    "post",
])
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo="Jogos", jogos=lista)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']
    senha = request.form['senha']
    usuario = usuarios.buscar(email, senha)
    if usuario is None:
      flash('Usuário/Senha inválidos.')
    else:
      session['usuario_email'] = usuario.email
      session['usuario_email'] = usuario.nome
      return redirect(url_for('index'))
  return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
  session.pop('usuario_email', None)
  session.pop('usuario_nome', None)
  return redirect(url_for('index'))

  
# Esse código é para quando for rodar no Replit
app.run(host='0.0.0.0', debug=True)

# Esse código é para quando for rodar em sua máquina
# app.run(debug=True)
