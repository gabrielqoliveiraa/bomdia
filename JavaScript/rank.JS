/*Com o conhecimento de objetos em mãos construa um programinha de controle de convidados mais
elaborado, considerando as propriedades:
Nome
Idade
CPF
Permita que o cadastrante digite estas informações em nosso array de convidados.*/



var convidado = [];

while (true){
    var nome = prompt('Digite o nome: ');
    var idade = prompt('Digite o idade: ');
    var cpf = prompt('Digite o cpf: ');
    if (nome == 'N'){
        break
    } else {
        convidado.push({nome: nome, idade: idade, cpf: cpf});
        
    }

}
  


console.log(convidado);





