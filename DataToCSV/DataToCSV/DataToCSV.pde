import processing.serial.*;

int Oven_P1_1 = 8;
int Oven_P1_2 = 9;
int Oven_P5_1 = 10;
int Oven_P5_2 = 11;

Serial myPort;
Table table;

int numReadings = 10;
int readingCounter = 0;

String filename, val;

void setup() {

String portName = Serial.list()[0];
myPort = new Serial(this, portName, 9600);
table = new Table();
table.addColumn("id");
table.addColumn("second");
table.addColumn("Humidity");
table.addColumn("Temperature");
table.addColumn("Water Level");
}

void serialEvent(Serial myPort){
try{
String val = myPort.readStringUntil('\n');
if (val != null) {
println(val);
//int sensorVals[] = int(split(val, ",")); // i dont need floats because I just need high or low input in 4 channel., what other function should I use.

String sensorVals[] = val.split(",");

println(sensorVals[1]);

TableRow newRow = table.addRow();
newRow.setInt("id", table.lastRowIndex());
newRow.setInt("second", second());
//newRow.setInt("Humidity", Integer.parseInt(sensorVals[0]));
//newRow.setInt("Temperature", Integer.parseInt(sensorVals[1]));
//newRow.setInt("Water Level", Integer.parseInt(sensorVals[2]));

readingCounter++;



if (readingCounter %numReadings ==0)
{
saveTable(table, "data/SensorData.csv");
}
}
}catch(RuntimeException e) {
e.printStackTrace();
}finally{}
}

void draw(){

}
