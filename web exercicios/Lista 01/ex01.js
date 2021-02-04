soma = (x, y) => {
    return x + y
};

sub = (x, y) => {
    return x - y
};

mult = (x, y) => {
    return x * y
};

div = (x, y) => {
    return x / y
};

res = (x, y) => {
    return (console.log(`Soma ${soma()} Sub ${sub(x, y)}`))
}

res(10,20)


