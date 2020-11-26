let num = document.getElementById('txtnum') 
let lista = document.querySelector('select#flista')
let res = document.getElementById('res')
let valores = []


function isNumero(n){
    if (Number(n) >= 1 && Number(n) <= 100){
        return true
    } else {
        return false
    }
}


function inLista(n, l){
    if (l.indexOf(Number(n)) != -1) {
        return true
    } else {
        return false
    }
}


function clicar() {
    if (isNumero(num.value) && !inLista(num.value, valores)) {
        valores.push(Number(num.value))
        let item = document.createElement('option')
        item.text = `Valor ${num.value} adicionado`
        lista.appendChild(item)
        res.innerHTML = ' '

    } else {
        window.alert('Valor invalido')
    }
    num.value = ''
    num.focus()
}


function stop(){
    if (valores.length == 0){
        window.alert('DIGITE UM VALOR')
    } else {
        let tot = valores.length
        let maior = valores[0]
        let menor = valores [0]
        let soma = 0 
        for (let pos in valores){
            soma += valores[pos]
            if (valores[pos] > maior)
                maior = valores[pos]
            if (valores[pos] < menor)
                menor = valores[pos]
        }

        res.innerHTML = ' '
        res.innerHTML += `<p>Temos ${tot} itens cadastrados </p>`
        res.innerHTML += `<p>O maiior valor é ${maior}</p>`
        res.innerHTML += `<p>O menor valor é ${menor}</p>`
        res.innerHTML += `<p>A soma é ${soma}</p>`
            
    }
        

}