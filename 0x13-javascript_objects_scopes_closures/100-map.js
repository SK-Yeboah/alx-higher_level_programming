#!/usr/bin/node

export function converter (base) {
    return function (number) {
        return number.toString(base);
    };
}
