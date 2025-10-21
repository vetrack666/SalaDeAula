from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Classe base
class ProdutoEletronico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_info(self):
        return f"Produto: {self.nome} | Preço: R${self.preco:.2f}"

# Classe filha - Smartphone
class Smartphone(ProdutoEletronico):
    def __init__(self, nome, preco, sistema):
        super().__init__(nome, preco)
        self.sistema = sistema

    def exibir_info(self):
        return f"{super().exibir_info()} | Sistema: {self.sistema}"

# Classe filha - Notebook
class Notebook(ProdutoEletronico):
    def __init__(self, nome, preco, memoria_ram):
        super().__init__(nome, preco)
        self.memoria_ram = memoria_ram

    def exibir_info(self):
        return f"{super().exibir_info()} | RAM: {self.memoria_ram}GB"

# Lista de produtos cadastrados
produtos = []

@app.route("/")
def index():
    return render_template("index.html", produtos=produtos)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    tipo = request.form["tipo"]
    nome = request.form["nome"]
    preco = float(request.form["preco"])

    if tipo == "smartphone":
        sistema = request.form["sistema"]
        produto = Smartphone(nome, preco, sistema)
    elif tipo == "notebook":
        memoria_ram = int(request.form["ram"])
        produto = Notebook(nome, preco, memoria_ram)
    else:
        produto = ProdutoEletronico(nome, preco)

    produtos.append(produto)
    return redirect("/")

@app.route("/deletar/<int:index>")
def deletar(index):
    if 0 <= index < len(produtos):
        produtos.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
