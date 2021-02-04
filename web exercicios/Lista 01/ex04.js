// Crie uma função que recebe dois parâmetros, base e expoente, e retorne a base elevada ao expoente.

pot = (base, expoente) => {
    let resultado = Math.pow(base, expoente)
    resultado = base ** expoente

    return resultado
}

console.log(pot(2,3))