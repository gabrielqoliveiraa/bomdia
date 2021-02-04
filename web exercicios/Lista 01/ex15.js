calculadoraSwitch = (x,y,z) => {
    switch (x,y,z) {
        case z = '+': 
            return x+y;
        case z  = '-':
            return x-y;
        case z = '*':
            return x*y;
        case z = '/':
            return x/y;
        default:
            return 'Operação inválida'
    }
}

console.log(calculadoraSwitch(2,3,'+'))
console.log(calculadoraSwitch(2,3,'-'))
console.log(calculadoraSwitch(2,3,'*'))
console.log(calculadoraSwitch(2,3,'/'))

