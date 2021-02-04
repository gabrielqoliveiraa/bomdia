let vetores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

isVector = (vetor) =>{
    let contadorPar = 0
    let contadorImpar = 0
    for (let i of vetores) {
        if (i % 2 == 0){
            contadorPar++
           
        } else if (i % 2 != 0) {
            contadorImpar++
           
        }
    }

    return ` ${contadorPar} VETORES PARES \n ${contadorImpar} VETORES IMPARES`

}


console.log(isVector(vetores))