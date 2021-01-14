/* criarProduto = (nome, preco) => {
    return {
        nome,
        preco,
    }
}

console.log(criarProduto('Arroz', 23.4))*/


//Classe

class Pessoa {
    constructor(nome){
        this.nome = nome
    }

    falar(){
        console.log(this.nome)
    }
}


const pessoa1 = new Pessoa('João')

pessoa1.falar()