jurosSimples = (capital, i, tempo) => {
    let juros = capital * i * tempo
    let montante = capital + juros
    return montante.toFixed(2)
}




jurosComposto = (capital, i, tempo) => {
    let montante = capital*Math.pow(( 1 + i), tempo)
    return montante.toFixed(2)
}

console.log(jurosComposto(100, 10/100, 2))
console.log(jurosSimples(100, 10/100, 2))


