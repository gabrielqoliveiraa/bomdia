function interval(vetor){
    let contador = 0
    for ( let i of vetor ){
        if (i >= 10 && i <= 20 ){
            contador++
        }
    } 

    return contador
}

let vetor = [ 7, 8, 9, 10, 11, 12, 16, 17, 18, 19, 20, 21]

console.log(interval(vetor))