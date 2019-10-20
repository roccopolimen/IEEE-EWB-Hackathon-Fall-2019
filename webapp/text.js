import * as d3 from "d3";
var allCrops = d3.map(data, function(d){return(d.crop)}).keys()