boletim = (cod, nota1, nota2, nota3) => {
    let notas = [];
    notas.push(nota1)
    notas.push(nota2)
    notas.push(nota3)
    notas.sort((a, b) => a < b ? 1 : -1)
    
    let media = ((notas[0]*4) + (notas[1]*3) + (notas[2]*3))/10
    return ` Código do Aluno - ${cod} \n Média: ${media} \n ${media < 5 ? 'Reprovado':'Aprovado'}`   

}
    



console.log(boletim(123, 2.8, 6, 3.5));

    



