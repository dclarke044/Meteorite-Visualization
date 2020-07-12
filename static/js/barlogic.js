// Test that data is there and accurate
meteoriteData = d3.json("/raw-data").then(function(data){
  console.log(data);
  var year = data[0].year;
  console.log(year);
})

// Assign chart to variable
vLSpec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "width": 1100, 
  "height": 700,
  "data": {"url": "/raw-data"},
  "mark": {
        "type": "bar",
        "tooltip": true
    },
  "selection": {
    "Meteorite": {
      "type": "single", "fields": ["maincategory"],
      "bind": {"input": "select", "options": [null, "Chondrite", "Achondrite", "Magnetic Iron", "Unknown", "Nonmagnetic Iron", "Mesosiderite", "Pallasite"]}
    }
  },
  "encoding": {
    "x": {
      "field": "year", "type": "temporal",
      "axis": {"domain": false, "format": "%Y", "tickSize": 0}
    },
    "y": {
      "aggregate": "count", 
      "field": "maincategory",
      "type": "quantitative",
      // "stack": "center", "axis": null
    },
    "color": {
      "field":"maincategory", "type": "nominal",
      "scale": {"scheme": "dark2"}
    },
    "opacity": {
      "condition": {"selection": "Meteorite", "value": 1},
      "value": 0.2
    }
  }
}

// Embed the visualization in the container with id `vis2`
vegaEmbed('#vis2', vLSpec);
  

