const heightChilds = (height1, years1, rateYear1, height2, years2, rateYear2) => {
    const calculate = calculateTime(height1, years1, rateYear1, height2, years2, rateYear2)
    if (height1 === height2 && rateYear1 == rateYear2){
        return `Children's heights will be equal`
    } else if (height1 != height2){
        if (height1 > height2){
            
            if (calculate == 'Child1') {
                return 'Child 1 will remain bigger'
            } else if (calculate == 'Child2'){
                return 'Child 2 will pass '
            }
        } else if (height2 > height1){
            if (calculate == 'Child1'){
                return 'Child 1 will pass'
            } else if(calculate == 'Child2'){
                return 'Child 2 will remain bigger'
            }
        }
    }
    
    
    
        

}

const calculateTime = (height1, years1,rateYear1, height2, years2,rateYear2) => {
    let newHeight1 = (20 - years1) * (rateYear1 + height1)
    let newHeight2 = (20 - years2) * (rateYear2 + height2)
    if (newHeight1 > newHeight2){
        return 'Child1'
    } else {
        return 'Child2'
    }
}



console.log(heightChilds(150, 5, 5,  130, 8 , 4))






        
        



