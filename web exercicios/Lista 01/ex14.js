const feira = (fruta) =>{

    switch(fruta){
        case 'maçã':
            console.log('Não vendemos esta fruta aqui.')
            break
        case 'Kiwi':
            console.log('Estamos com escassez de kiwi.')
            break
        case 'Melancia':
            console.log('Aqui está, custa R$ 3,00 o quilo.')
            break
        default:
            console.log('Erro, fruta inválida.')
        
    }
}

feira('maçã')
feira('Kiwi')
feira('Melancia')
feira('alcatra')
