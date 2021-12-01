const fs = require('fs');

const makeNewAlpha = (s, keyWord, code) => {
    let line = '';

    for (const char of s) {
        if( !(keyWord.includes(char)) ) {
            line += char;
        }
    }

    let alphaCaesar = `${line.slice(line.length - code)}${keyWord}${line.slice(0, line.length - code)}`;
    
    const newAlpha = {};

    for (let i = 1; i <= s.length; i++) {
        newAlpha[s[i - 1]] = alphaCaesar[i - 1]
        newAlpha[s[i - 1].toUpperCase()] = alphaCaesar[i - 1].toUpperCase();
    }

    return newAlpha;
} 

const encrypt = (alpha) => {
    let text = fs.readFileSync('lab-1/War&Peace.txt', 'utf8');
    let result = '';

    for (const char of text) {
        if (char in alpha) {
            result += alpha[char];
        } else {
            result += char;
        }
    }

    fs.writeFileSync('lab-1/War&Peace(encrypt).txt', result);
}

const counter = (text) => {
    return text.split('').reduce((acc, char) => {
        acc[char] = acc[char] ? acc[char] + 1 : 1;
        return acc;
    } ,{})
}

const frequency = (text, alphabet) => {
    let count = Object.entries(counter(text));
    let listFreq = [];

    for (let i = 0; i < count.length; i++) {
        if (alphabet.includes(count[i][0])) {
            listFreq.push(count[i][0]);
        }
    }

    return listFreq;
}

const zip = (arr1, arr2) => {
    let obj = {};

    arr1.forEach((key, i) => obj[key] = arr2[i]);

    return obj;
}

const decrypt = (frequencyAlphabet, alphabet) => {
    let text = fs.readFileSync('lab-1/War&Peace(encrypt).txt', 'utf8');
    let freq = frequency(text, alphabet);
    let d = zip(freq, frequencyAlphabet);
    let result = [];

    for (const char of text) {
        if (frequencyAlphabet.includes(char)) {
            result.push(d[char]);
        } else {
            result.push(char);
        }
    }

    fs.writeFileSync('lab-1/War&Peace(decrypt).txt', result.join(''));
}

let alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя';
let frequency_alphabet = ['о', 'а', 'е', 'и', 'т', 'н', 'л','р', 'с', 'в', 'к', 'м', 'д', 'у', 'п','б', 'г', 'ы', 'ч', 'ь', 'з', 'я', 'й','х', 'ж', 'ш', 'ю', 'ф', 'э', 'щ','ё', 'ц', 'ъ']

let code = 5
let keyWord = 'стол'

let newAlphabet = makeNewAlpha(alphabet, keyWord, code)
encrypt(newAlphabet);
decrypt(frequency_alphabet, alphabet);
