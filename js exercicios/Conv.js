/*Adicione em nosso pequeno sistema de controle de convidados as funções de filtro para barrar as pessoas
com menos de 18 anos e mais.

Que possa permitir agrupar entre gêneros para melhorar a organização de cobrança e ordenar por nome, já
que no futuro evento o cliente comentou que "mulher paga meia" e que precisa estar ordenado para
conferência mais rápida de nomes.*/

Array.prototype.groupBy = function (prop){
    var value = this.reduce(function (total, item){
        var key = item[prop];

        total[key] = (total[key] || []).concat(item)

        return total;
    }, {})
    return value;
}

var convidados = [
    {nome: 'Felipe', idade: 37, genero: 'masculino'},
    {nome: 'Amanda', idade: 17, genero: 'feminino'},
    {nome: 'João', idade: 27, genero: 'masculino'},
    {nome: 'Daniel', idade: 21, genero: 'masculino'},
    {nome: 'Helena', idade: 21, genero: 'feminino'}
   ];
   


var convidadosFilrados =  convidados.sort(function(a,b){
    return (a.nome > b.nome) ? 1 : -1
}).filter(function (item){
    return item.idade >= 18
}).groupBy('genero')


console.log(convidadosFilrados)




