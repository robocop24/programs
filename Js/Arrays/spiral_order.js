"use strict";
const prompt = require("prompt-sync")({ sigint: true });
var m = prompt("Rows: ");
var n = prompt("columns: ");
/* m-rows n-columns T-TopMost B-BottomMost L-Leftmost R-RightMost */
var T = 0, B = m - 1, L = 0, R = n - 1;
var arr = new Array(m);

for (var i = 0; i < m; i++) {
    arr[i] = new Array(n);
}

for (var i = 0; i < m; i++) {
    for (var j = 0; j < n; j++) {
        let value = prompt("value: ");
        arr[i][j] = value;
    }
}

var str = '';
for (var i = 0; i < m; i++) {
    for (var j = 0; j < n; j++) {
        str += arr[i][j] + ' ';
    }
}
console.log(str);

str = '';
var dir = 0;
while (T <= B && L <= R) {
    // dir -> 0 ,move left to right
    if (dir == 0) {
        for (var i = L; i <= R; i++) {
            str += arr[T][i] + " ";
        }
        T++;
    }
    // dir -> 1 ,move top to bottom
    else if (dir == 1) {
        for (var i = T; i <= B; i++) {
            str += arr[i][R] + " ";
        }
        R--;
    }
    // dir -> 2 ,move right to left
    else if (dir == 2) {
        for (var i = R; i >= L; i--) {
            str += arr[B][i] + " ";
        }
        B--;
    }
    // dir -> 3 ,move bottom to top
    else if (dir == 3) {
        for (var i = B; i >= T; i--) {
            str += arr[i][L] + " ";
        }
        L++;
    }
    dir = (dir + 1) % 4;
}

console.log(str);