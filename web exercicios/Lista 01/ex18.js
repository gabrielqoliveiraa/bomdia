planoSaude = (idade) => {
    let valor = 100

    if (idade < 10) {
        valor += 80
    } else if ( idade >= 10 && idade <= 30) {
        valor += 50
    } else if ( idade > 30 && idade <= 60) {
        valor += 95
    } else if ( idade > 60 ) {
        valor += 130
    }

    return valor

}


console.log(planoSaude(8))
console.log(planoSaude(15))
console.log(planoSaude(35))
console.log(planoSaude(52))
console.log(planoSaude(80))