var submit = document.getElementById("submit");

var crop = "";
var city = "";
var state = "";
var yields = "";
var profit = "";

submit.onclick = function(){
    crop = document.getElementById("crop").value;
    city = document.getElementById("city").value;
    state = document.getElementById("state").value;
    yields = document.getElementById("yield").value;
    profit = document.getElementById("profit").value;

}

module.exports.crop = crop;
module.exports.city = city;
module.exports.state = state;
module.exports.yields = yields;
module.exports.profit = profit;