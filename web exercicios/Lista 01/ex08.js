let pontos = "30, 40, 20, 4, 51, 25, 42, 38, 56, 0"

const points = (pontos) => {
    let pontuacao = pontos.split(", ");
    let records = 0
    let piorjogo = 1 
    let maior = pontuacao[0]
    let menor = pontuacao[0]

    for ( let i = 1; i < pontuacao.length; i++){
        if (pontuacao[i] > maior){
            
            maior = pontuacao[i]
            records++
            
        } else if (pontuacao[i] < menor){
            menor = pontuacao[i]
            piorjogo = i + 1
        }
    }

    return [records, piorjogo]
}

console.log(points(pontos))

