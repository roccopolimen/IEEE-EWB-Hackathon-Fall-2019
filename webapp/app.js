const CSVToJSON = require("csvtojson");
const JSONToCSV = require("json2csv").parse;
const FileSystem = require("fs");

var crop = "";
var city = "";
var state = "";
var yield = "";
var profit = "";

var submit = document.getElementById("submit");

submit.onclick = function(){
    var crop = document.getElementById("crop").value;
    var city = document.getElementById("city").value;
    var state = document.getElementById("state").value;
    var yield = document.getElementById("yield").value;
    var profit = document.getElementById("profit").value;


    CSVToJSON().fromFile("./dataset.csv").then(source => {
        console.log(source);
        source.push({
            "crop": crop,
            "city": city,
            "state": state,
            "yield": yield,
            "profit": profit
        });
        const csv = JSONToCSV(source, {fields: ["crop", "city", "state", "yield", "profit"]});
        FileSystem.writeFileSync("./dataset.csv", csv);
    });
}