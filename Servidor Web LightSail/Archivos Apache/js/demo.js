DevExpress.viz.currentTheme("generic.light");
$(function(){
    var gauge = $("#gauge").dxCircularGauge({
        scale: {
            startValue: 10,
            endValue: 40,
            tickInterval: 5,
            label: {
                customizeText: function (arg) {
                    return arg.valueText + " °C";
                }
            }
        },
        rangeContainer: {
            ranges: [
                { startValue: 10, endValue: 20, color: "#0077BE" },
                { startValue: 20, endValue: 30, color: "#E6E200" },
                { startValue: 30, endValue: 40, color: "#77DD77" }
            ]
        },
        tooltip: { enabled: true },
        title: {
            text: "Temperature in the Greenhouse",
            font: { size: 28 }
        },
        value : dataSource[0].mean,
        subvalues : [dataSource[0].min, dataSource[0].max]
    }).dxCircularGauge("instance");
    
    $("#seasons").dxSelectBox({
        width: 150,
        dataSource: dataSource,
        displayExpr: "name",
        value: dataSource[0],
        onSelectionChanged: function(e) {
            gauge.option("value", e.selectedItem.mean);
            gauge.option("subvalues", [e.selectedItem.min, e.selectedItem.max]);
        }
    });
});

var dataSource = [{
    name: 'Summer',
    mean: 35,
    min: 28,
    max: 38
}, {
    name: 'Autumn',
    mean: 24,
    min: 20,
    max: 32
}, {
    name: 'Winter',
    mean: 18,
    min: 16,
    max: 23
}, {
    name: 'Spring',
    mean: 27,
    min: 18,
    max: 31
}];