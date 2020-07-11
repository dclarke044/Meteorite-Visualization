// Assign the specification to a local variable vlSpec.
var vlSpec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
    "description": "Mass By Year.",
    "data": {"url": "Meteorite_Landings_WorkingDatavF.csv"},
    "width": 1100,
    "height": 700,
    mark: {
        "type": "bar",
        "tooltip": true
        },
          encoding: {
            x: {field: 'year', type: 'temporal', range: [1700,2000]},
            y: {
              aggregate: 'count',
              field: 'reclass',
              type: 'quantitative',
              axis: {
                title: 'Count by Recclass'
              },
            },
            "color": {"field": "recclass", "type": "nominal"},
            
          }
  
    
  };
  
  
  // Embed the visualization in the container with id `vis`
  vegaEmbed('#vis', vlSpec);