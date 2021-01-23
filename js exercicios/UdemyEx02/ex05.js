invertParam = (param) =>{
    if (typeof param == 'string') {
        return 'Booleano ou Numero esperado'
    } else if(typeof param == 'boolean') {
        return param = true ? true : false
    } else {
        return -param
    }
}


console.log(invertParam(200))