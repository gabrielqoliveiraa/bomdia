const negativeNumbers = (array) =>{
    let contador = 0;
    for (let i = 0; i < array.length; i++) {
        if (array[i] < 0) {
            contador++
        } 
    }
    console.log(contador)
}


negativeNumbers([10, 5, -7, 3, -1, 3, -11, -20, 6, 9])