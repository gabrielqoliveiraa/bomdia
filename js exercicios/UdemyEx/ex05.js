formatarValor = (valorDecimal) => {
    let valor = `R$ ${valorDecimal.toFixed(2).toString().replace('.',',')}`
    return valor
}

console.log(formatarValor(0.1 + 0.2))



