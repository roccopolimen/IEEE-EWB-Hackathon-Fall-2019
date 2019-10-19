const CSVToJSON = require("csvtojson");
const JSONToCSV = require("json2csv").parse;
const FileSystem = require("fs");

var express = require("express");
var bodyParser = require("body-parser");
var app = express();

app.use(bodyParser.urlencoded({extended: true}));

app.get("addRow", function(request, response){
    //var crop = "crop test";
    //var city = "city test";
    //var state = "state test";
    //var yields = "yield test";
    //var profit = "profit test";

    CSVToJSON().fromFile("./dataset.csv").then(source => {
        //console.log(source);
        source.push({
            "crop": request.body.crop,
            "city": request.body.city,
            "state": request.body.state,
            "yield": request.body.yields,
            "profit": request.body.profit
        });
        const csv = JSONToCSV(source, {fields: ["crop", "city", "state", "yield", "profit"]});
        FileSystem.writeFileSync("./dataset.csv", csv);
    });
});

// app.listen(8080, function(){
//     console.log("Hello World");
// });