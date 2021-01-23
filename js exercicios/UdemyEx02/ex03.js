const salario = (horas, valor) => {
    let horario = horas/30 
    let valorRecebido = (horario *valor) * 30
    return valorRecebido
}


console.log(salario(180, 60))