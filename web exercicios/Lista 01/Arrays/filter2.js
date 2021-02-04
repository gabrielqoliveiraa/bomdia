Array.prototype.filter2 = function (callback) {
    const novoArray = [];
    for (let i = 0; i < this.length; i++) {
        if (callback(this[i],i, this)) {
            novoArray.push(this[i]);
        }

    }
    return novoArray;
}





const produtos = [
    {nome: 'Notebook', preco: 2499, fragil: true},
    {nome: 'Ipad Pro', preco: 4199, fragil: true},
    {nome: 'Copo de Vidro', preco: 12.49, fragil: true},
    {nome: 'Copo de Plastico', preco: 18.99, fragil: false},
]


let filterProducts = produtos.filter2(function(e) {
    return e.preco >= 500 && e.fragil
})

console.log(filterProducts)
 