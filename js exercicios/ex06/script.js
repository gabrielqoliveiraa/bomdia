function verificar() {
    var data = new Date()
    var ano = data.getFullYear() 
    var txtano = document.getElementById('txtano')
    var res = document.getElementById('res')
    if (txtano.value.length == 0 || Number(txtano.value) > ano) {
        window.alert('Verifique os dados novamente')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(txtano.value)
        var genero = ''
        if (fsex[0].checked) {
            genero = 'Homem'
        } else if (fsex[1].checked) {
            genero = 'Mulher'
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Você é ${genero} com ${idade} anos `

    }
    
    




}