triangleWhosIs = (x, y, z) => {
    if (isTrue == true) {
        if ( x == y && x == z ){
            console.log('Equilátero')
        } else if ( x == y || y == z ){
            console.log('Isosceles')
        } else {
            console.log('Escaleno')
        }
    }

    else {
        console.log('Esse triangulo não existe')
    }
    
}


function isTrue(x, y, z){
    if ( x < y + z && x > Math.abs(y-z) && ( y < x + z && y > Math.abs(x-z)) && (z < y + z && z > Math.abs(y-z)) ){
        return true;
    }
}
        



        

triangleWhosIs(7,3,5)
    

    