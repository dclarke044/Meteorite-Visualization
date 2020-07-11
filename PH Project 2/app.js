// Select the button
var button = d3.select("#button");
var reset = d3.select("#reset-button");
// Select the form
var form = d3.select("#form");

// Create event handlers 
button.on("click", runEnter);
form.on("submit",runEnter);
reset.on("click", runReset);
// Get a reference to the table body
var tbody = d3.select("tbody");

console.log(data);

data.forEach((meteorite) => {
  var row = tbody.append("tr");
  Object.entries(meteorite).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
  });
});

function runReset() {
  // Prevent the page from refreshing
  d3.event.preventDefault();
  var tbody = d3.select("tbody");
  tbody.html("");
  data.forEach((meteorite) => {
    var row = tbody.append("tr");
    Object.entries(meteorite).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
};

// Complete the event handler function for the form
function runEnter() {

  // Prevent the page from refreshing
  d3.event.preventDefault();
  
  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#year");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);

  var filteredData = data.filter(data => parseInt(data.year) === parseInt(inputValue));

  var tbody = d3.select("tbody");

  tbody.html("");

  console.log(filteredData);

  filteredData.forEach((meteorite) => {
    var row = tbody.append("tr");
    Object.entries(meteorite).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });

};