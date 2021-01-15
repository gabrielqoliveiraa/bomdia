caixaEletronico = (valorSaque) =>{
    let valorNota = valorNotas(valorSaque)
    let contador100 = 0
    let contador50 = 0
    let contador10 = 0
    let contador5 = 0
    let contador1 = 0


    console.log(`Valor do Saque: R$ ${valorSaque}`)
    while (valorSaque >= valorNota){
        switch (valorNota){
            case 100:
                valorSaque -= 100
                contador100++
                break
            case 50:
                valorSaque -= 50
                contador50++
                break
            case 10:
                valorSaque -= 10
                contador10++
                break
            case 5:
                valorSaque -= 5
                contador5++
                break
            case 1:
                valorSaque -= 1
                contador1++
                break

        }

        valorNota = valorNotas(valorSaque)
    }

    

    
    return resultado(contador100, contador50, contador10, contador5, contador1)
    
}






function valorNotas(valorSaque) {
    if (valorSaque >= 100) {
        return 100
    } else if (valorSaque >= 50) {
        return 50
    } else if (valorSaque >= 10) {
        return 10
    } else if (valorSaque >= 5){
        return 5
    }else if (valorSaque >= 1){
        return 1
    }
}


function resultado (c100, c50, c10, c5, c1){
    let res = ''
    if (c100 >= 1){
        res += `${c100} notas de R$100 \n`
    } 
    if (c50 >= 1){
        res += `${c50} notas de R$50 \n`
    }
    if (c10 >= 1){
        res += `${c10} notas de R$10 \n`
    }
    if (c5 >= 1){
        res += `${c5} notas de R$5 \n`

    } 
    if (c1 >= 1){
        res += `${c1} notas de R$ 1`
    }

    return res
}



         
console.log(caixaEletronico(220))

        
