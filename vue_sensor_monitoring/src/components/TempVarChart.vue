<template>
<div class="row">
  <div class="col-6 p-1">
    <div class="custom-card header-card card">
      <div class="card-body pt-0">
        <fusioncharts
          type="spline"
          width="100%"
          height="100%"
          dataformat="json"       dataEmptyMessage="i-https://i.postimg.cc/R0QCk9vV/Rolling-0-9s-99px.gif"
          dataEmptyMessageImageScale=39
          :datasource="tempChartData"
        >
        </fusioncharts>
      </div>
    </div>
  </div>
  <div class="col-6 p-1">
    <div class="custom-card header-card card">
      <div class="card-body pt-0">
        <fusioncharts
          type="spline"
          width="100%"
          height="100%"
          dataformat="json"       dataEmptyMessage="i-https://i.postimg.cc/R0QCk9vV/Rolling-0-9s-99px.gif"
          dataEmptyMessageImageScale=39
          :datasource="CO2ChartData"
        >
        </fusioncharts>
      </div>
    </div>
  </div>  
</div>
</template>

<script>
export default {
 props: ["tempVar", "co2Var"],
 components: {},
 data() {
   return {
     tempChartData: {
       chart: {
         caption: "Hourly Temperature",
         captionFontBold: "0",
         captionFontColor: "#000000",
         captionPadding: "30",
         baseFont: "Roboto",
         chartTopMargin: "30",
         showHoverEffect: "1",
         theme: "fusion",
         showaxislines: "1",
         numberSuffix: "°C",
         anchorBgColor: "#6297d9",
         paletteColors: "#6297d9",
         drawCrossLine: "1",
         plotToolText: "$label<br><hr><b>$dataValue</b>",
         showAxisLines: "1",
         "showXAxisLine": "1",
         showYAxisValues: "1",
         anchorRadius: "4",
         divLineAlpha: "0",
         labelFontSize: "13",
         labelAlpha: "65",
         labelFontBold: "0",
         rotateLabels: "1",
         slantLabels: "1",
         canvasPadding: "20"
       },
       data: [],
     },
     CO2ChartData: {
       chart: {
         caption: "Hourly CO2",
         captionFontBold: "0",
         captionFontColor: "#000000",
         captionPadding: "30",
         baseFont: "Roboto",
         chartTopMargin: "30",
         showHoverEffect: "1",
         theme: "fusion",
         showaxislines: "1",
         numberSuffix: "ppm",
         anchorBgColor: "#6297d9",
         paletteColors: "#6297d9",
         drawCrossLine: "1",
         plotToolText: "$label<br><hr><b>$dataValue</b>",
         showAxisLines: "1",
         "showXAxisLine": "1",
         showYAxisValues: "1",
         anchorRadius: "4",
         divLineAlpha: "0",
         labelFontSize: "13",
         labelAlpha: "65",
         labelFontBold: "0",
         rotateLabels: "1",
         slantLabels: "1",
         canvasPadding: "20"
       },
       data: [],
     },
   };
 },
 methods: {
   setChartData: function() {
     var data = [];
     for (var i = 0; i < this.tempVar.tempToday.length; i++) {
       var dataObject = {
         label: this.tempVar.tempToday[i].hour,
         value: this.tempVar.tempToday[i].temp
       };
       data.push(dataObject);
     }
     this.tempChartData.data = data;
   },
   setChartData1: function() {
     var data = [];
     for (var i = 0; i < this.co2Var.tempToday.length; i++) {
       var dataObject = {
         label: this.co2Var.tempToday[i].hour,
         value: this.co2Var.tempToday[i].co2
       };
       data.push(dataObject);
     }
     this.CO2ChartData.data = data;
   },
 },
 mounted: function() {
   this.setChartData();
   this.setChartData1();
 },
 watch: {
   tempVar: {
     handler: function() {
       this.setChartData();  
     },
     deep: true
   },
   co2Var: {
     handler: function() {
       this.setChartData1();
		console.log(this.CO2ChartData)                                  
     },
     deep: true
   },
 },
};
</script>

<style>
</style>
