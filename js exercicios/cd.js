function solution(number){ 
    var contador = 0 
    
    for (var i = 3; i < number; i++){
      if ( i % 3 == 0 || i % 5 == 0 ){
        var contador = i + contador
      } 
    }
    
    return contador;
    
}


solution(10)