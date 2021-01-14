// Crie uma função que irá receber dois valores, o dividendo e o divisor. A função deverá imprimir o resultado
// e o resto da divisão destes dois valores.

div = (x, y) => {
    let divisao = Math.floor(x/y) 
    let resto = x % y
    return console.log(`Resultado: ${divisao}`, `Resto: ${resto}`)
}

div(11,4)
    