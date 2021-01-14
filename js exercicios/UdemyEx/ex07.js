bhaskara = (a, b, c) => {
    const vetorVazio = []
    const delta = (b**2) - 4 *a*c
    if (delta < 0) {
        return 'Delta negativo'
    } else {
        let x1 = (-b + Math.sqrt(delta)) / 2 * a
        let x2 = (-b - Math.sqrt(delta)) / 2 * a
        vetorVazio.push(x1)
        vetorVazio.push(x2)
        return vetorVazio
    }
    
}

console.log(bhaskara(3, 1, 2))