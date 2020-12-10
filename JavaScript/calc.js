var numeros = []
var soma = 0 

while (true) {
    var usuario = prompt('Digite um numero: ')
    if (usuario == 'S'){
        break
    } else {
        numeros.push(Number(usuario))
    }
}

numeros.forEach(function(num){
    soma += num
})

/* for(i=0; i<numeros.length; i++){
    soma += numeros[i];
}*/ 

var resultado = soma/numeros.length
console.log(resultado)









