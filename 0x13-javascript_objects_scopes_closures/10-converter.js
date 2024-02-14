#!/usr/bin/node


// converter.js

export function converter (base) {
    return function (number) {
        return number.toString(base);
    };
}
