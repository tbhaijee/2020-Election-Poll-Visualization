    // Fetch the JSON data and console log it


    function readdata(idname) {
        d3.json("../static_state_page/samples.json").then((data) => {
            var id_data = data.metadata;
            var filter_data = id_data.filter(x => x.id == idname);
            filter_data = filter_data[0];
            console.log(filter_data);
            var metadata = d3.select("#sample-metadata");
            metadata.html("");
            Object.entries(filter_data).forEach(([key, value]) => {
                metadata.append("p").text(`${key}: ${value}`);
            });


        });
    }
    // this function reads all state names to built the list in pull down
    function dropdown() {
        var id_dropdown = d3.select("#selDataset");
        d3.json("../static_state_page/samples.json").then((data) => {
            var id_names = data.names;
            id_names.forEach((ids) => {
                id_dropdown.append("option").text(ids).property("value", ids);
            })
        });
    }
    // this function is to get new id on change
    function optionChanged(newid) {
        readdata(newid);
        updatebarPlot(newid);
        updatestateName(newid);

    }
    // this function plots bar chart for present poll for each candidate
    function updatebarPlot(idname) {
        d3.json("../static_state_page/samples.json").then((data) => {
            var id_data = data.samples;
            var filter_data = id_data.filter(x => x.id == idname);
            filter_data = filter_data[0];
            var otuids = filter_data.otu_ids;
            var samplevalue = filter_data.sample_values;
            var yaxisdata = otuids;

            var trace = [{
                    y: yaxisdata,
                    x: samplevalue,
                    type: "bar",
                    orientation: "h"

                }

            ];
            var layout = {
                title: "Election 2020 Poll Data"
            };
            Plotly.newPlot("bar", trace, layout);


        });
    }
    // this function updates the state name
    function updatestateName(idname) {
        d3.json("../static_state_page/samples.json").then((data) => {
            var id_data = data.metadata;
            var filter_data = id_data.filter(x => x.id == idname);
            filter_data = filter_data[0];
            statename = filter_data.id;
            var metadata = d3.select("#state_name");
            metadata.html(statename);
            var img = d3.select("#img");
            img.html("");

            // this function updates the map for the state
            drawListNode(img);

            function drawListNode(parent) {
                var node = parent.append("h5");
                var icon_src = "../images/" + statename + ".jpg";
                var m = node.append("img").attr("src", icon_src);
                node.append("span");
                console.log(m);
                return node;
            }
        });
    }

    // Call function to have default values

    updatestateName("Alabama");
    readdata("Alabama");
    dropdown();
    updatebarPlot("Alabama");
    // updatestateName(state);
    // readdata(state);
    // dropdown();
    // updatebarPlot(state);