/*Criar um método dentro do sistema de controle de convidados para que possa clonar objetos aproveitando
os dados de outro convidado.*/ 

var convidado = {id: 123, nome: "Lucas"};
var convidados = [convidado];
novoConvidado = Object.create(convidado);
convidados.push(novoConvidado);


