fatorial = (number) =>{
    let contador = 1
    let num = 1
    if (number == 0) {
        return 1
    }
    
    while(contador <= number){
        num = contador * num
        contador++
    }

    console.log(num)
}


/* function fatorial (numero) {
    if(numero == 0){
        return 1
    } else {
        return numero * fatorial(numero - 1)
    }
}

*/


fatorial(5)
        