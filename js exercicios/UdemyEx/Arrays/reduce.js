const alunos = [
{nome:'Joao', nota: 7.3, bolsista: false},
{nome:'Maria', nota: 9.2, bolsista: true},
{nome:'Pedro', nota:9.8, bolsista: false},
{nome:'Ana', nota:9.9, bolsista: true},
];


let desafio1 = alunos.map(e => e.bolsista).reduce(function(resultado, atual){
    return resultado && atual
})

console.log(desafio1);