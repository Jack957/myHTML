var calc = document.getElementById('calculate');
var result = document.getElementById('result');
calc.onclick = function () {
	var num1 = calc.form.num1.value;
	var num2 = calc.form.num2.value;
	result.textContent = num1 * num2;
	return false;
}