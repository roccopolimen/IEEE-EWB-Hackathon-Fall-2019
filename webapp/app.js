const CSVToJSON = require("csvtojson");
const JSONToCSV = require("json2csv").parse;
const FileSystem = require("fs");

const express = require("express");
const bodyParser = require("body-parser");
var app = express();

app.use(bodyParser.urlencoded({extended: true}));

app.post("addRow", function(crop, city, state, yields, profit){
    //var crop = "crop test";
    //var city = "city test";
    //var state = "state test";
    //var yields = "yield test";
    //var profit = "profit test";

    CSVToJSON().fromFile("./dataset.csv").then(source => {
        console.log(source);
        source.push({
            "crop": crop,
            "city": city,
            "state": state,
            "yield": yields,
            "profit": profit
        });
        const csv = JSONToCSV(source, {fields: ["crop", "city", "state", "yield", "profit"]});
        FileSystem.writeFileSync("./dataset.csv", csv);
    });
});

app.listen(5500, function(){
    console.log("Hello World");
});