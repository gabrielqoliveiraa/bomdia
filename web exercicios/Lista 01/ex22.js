parisTrue = () =>{
    let contador = 0
    for (let i = 1; i <= 100; i++) {
        if (i % 2 == 0) {
            contador++
        }
    }

    return `${contador} Pares entre 1 e 100`
}

console.log(parisTrue(  ))