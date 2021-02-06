const colors ={
    p: "#388e3c",
    div: '#1565c0',
    span: '#e53935',
    section: '#f67809',
    padrao: '#616161',
    ul: 'purple',
    ol: 'gold',
    get(tag){
        return this[tag] ? this[tag] : this.padrao
    }
}


document.querySelectorAll('.tag').forEach(box => {
    const tagName = box.tagName.toLowerCase();

    box.style.borderColor = colors.get(tagName)

    if (!box.classList.contains('nolabel')){ 
        const label = document.createElement('label')
        label.style.backgroundColor=colors.get(tagName)

        label.innerHTML = tagName
        box.insertBefore(label, box.childNodes[0])
    }
})