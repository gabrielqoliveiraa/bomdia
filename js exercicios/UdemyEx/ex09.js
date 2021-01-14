const notas = (nota) => {
    if (nota < 38){
        return "Reprovado"
    } else if (nota >= 38){
        let decimal = Math.round(nota / 5)
        let novaNota = decimal * 5
        console.log(`Nota: ${nota}`)
        console.log(`Nota Corrigida: ${novaNota}`)
        console.log("Status: Aprovado")
        

    }
}


//console.log(notas())



