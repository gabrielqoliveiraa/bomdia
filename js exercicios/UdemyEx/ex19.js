aunidade = (mes, valor) => {
    let juros = (valor * (Math.pow(1 + 0.05, (mes-1))))

    return `O valor pago deverá ser: ${juros.toFixed(2)}`
}

console.log(aunidade(4, 100))

