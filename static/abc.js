let name1 = document.getElementsByName('name');
let number = document.getElementsByName('number');
let product = document.getElementsByName('product');
let address = document.getElementsByName('address');
const failed = document.getElementsByName('failed');
const success = document.getElementsByName('success');
function first (name1, number, product, address){
if (name1 ===''|| number ==='' || address === ''){failed.style.display = "block"}else{success.style.display = "block"}}