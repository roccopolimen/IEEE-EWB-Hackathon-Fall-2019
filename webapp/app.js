const CSVToJSON = require("csvtojson");
const JSONToCSV = require("json2csv").parse;
const FileSystem = require("fs");
const port = 8080;

var path = require('path');
var express = require("express");
var bodyParser = require("body-parser");
var app = express();

app.use(bodyParser.urlencoded({extended: true}));

app.get('/', (request, response) => {
    //response.sendFile(path.join(__dirname, '../webapp', 'index.html'));
    //response.send("<p>Thank you for submitting!</p><br><a href='google.com'>Go Home</a>");

    CSVToJSON().fromFile("./dataset.csv").then(source => {
        source.push({
            "crop": request.query.crop,
            "cityState": request.query.cityState,
            "yield": request.query.yields,
            "profit": request.query.profit,
            "temperature": request.query.temperature,
            "humidity": request.query.humidity,
            "pressure": request.query.pressure,
            "waterLevel": request.query.waterLevel
        });
        const csv = JSONToCSV(source, {fields: ["crop", "cityState", "yield", "profit", "temperature", "humidity", "pressure", "waterLevel"]});
        FileSystem.writeFileSync("./dataset.csv", csv);
    });

})

app.listen(port, () => console.log(`Listening on Port ${port}`));