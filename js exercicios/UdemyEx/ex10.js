const isDivisible = (numero) =>{
    if (numero % 3 == 0){
        return true;
    } else {
        return false;
    }
}


console.log(isDivisible(3))
console.log(isDivisible(2))
console.log(isDivisible(150))