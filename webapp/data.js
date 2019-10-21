const CSVToJSON = require("csvtojson");
const JSONToCSV = require("json2csv").parse;
const FileSystem = require("fs");

CSVToJSON().fromFile("./dataset.csv").then(source => {
    for(var i=0; i<source.length; i++){
        crop = source[i].crop;
        crop = crop.toLowerCase();
        crops.add(crop);
    }
    console.log(crops);
});

function getAnswer(){
    var crops = new Set(["corn"]);
    a = document.getElementById("crop").value;
    answer = a.toLowerCase();
    console.log(crops.has(answer));
}