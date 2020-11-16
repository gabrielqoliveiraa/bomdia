function carregar(){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var agora = data.getHours()
    msg.innerHTML = `São ${agora} horas`
    if (agora >= 0 && agora < 12) {
        msg.innerHTML = 'BOM DIA'
        img.src = 'fotomanha.png'
        document.body.style.background = 'pink'

    } else if (agora >= 12 && agora < 18){
        msg.innerHTML = 'BOA TARDE'
        img.src = 'fototarde.png'
        document.body.style.background = 'orange'

    }else{
        msg.innerHTML = 'BOA NOITE'
        img.src = 'fotonoite.png'
        document.body.style.background = 'blue'
    }



}