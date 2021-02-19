function decimalParaRomano(numero) {
    let r = '';
    let divisao = 0;
    let resto = numero;
    let vetorNumeros = [1000,500,100,50,10];
    let vetorRomanos = ['M','D','C','L','X'];
    let vetorDezena = ['I','II','III','IV','V','VI','VII','VIII','IX'];

    for(let i = 0; i < vetorNumeros.length; i++){
        divisao = parseInt(resto/vetorNumeros[i]);
        resto = numero%vetorNumeros[i];
        if(divisao > 0){
            for(let x = 0; x < divisao; x++){
                r = r+vetorRomanos[i];
            }
        }
        if (resto < 10) {
            r = r+vetorDezena[resto-1];
            break;
        }
    }
    
    return r;
}


let romano = decimalParaRomano(80);//Retorno V

console.log(romano);