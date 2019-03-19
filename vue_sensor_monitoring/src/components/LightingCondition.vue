<template>
 <div class="highlights-item col-md-4 col-sm-6 col-xs-12 border-left border-right border-top">
   <div>
     <fusioncharts
       :type="type"
       :width="width"
       :height="height"
       :containerbackgroundopacity="containerbackgroundopacity"
       :dataformat="dataformat"
       :datasource="datasource"
     >
     </fusioncharts>
     </div>
 </div>
</template>

<script>
export default {
 props: ["highlights"],
 components: {},
 methods: {},
 computed: {},
 data() {
   return {
     type: "hlineargauge",
     width: "100%",
     height: "100%",
     containerbackgroundopacity: 0,
     dataformat: "json",
     creditLabel: false,
     datasource: {
       chart: {
         caption: "Lighting [Lux]",
         captionFontBold: "0",
         captionFontColor: "#000000",
         baseFont: "Roboto",
         numberSuffix: "",
         lowerLimit: "0",
         upperLimit: "1000",
         showPointerShadow: "1",
         animation: "1",
         transposeAnimation: "1",
         theme: "fusion",
         bgAlpha: "0",
         canvasBgAlpha: "0",
         valueFontSize: "15",
         valueFontColor: "#000000",
         valueFontBold: "1",
         pointerBorderAlpha: "0",
         chartBottomMargin: "40",
         captionPadding: "30",
         chartTopMargin: "30"
       },
       colorRange: {
         color: [
           {
             minValue: "0",
             maxValue: "500",
             label: "Less",
             code: "#D8EDFF"//"#EEF278"
           },
           {
             minValue: "500",
             maxValue: "750",
             label: "Good",
             code: "#7DA9E0"//"#91E572"
           },
           {
<<<<<<< HEAD
             minValue: "750",
             maxValue: "1000",
=======
             minValue: "30",
             maxValue: "4500",
>>>>>>> 3839f3f3ee67f716b957d31e3ecfffd34c36f517
             label: "Too much",
             code: "#6297d9"//"#E89B9B"
           }
         ]
       },
       pointers: {
         pointer: [
           {
//             numberSuffix: " Lux",
             value: this.highlights.visibility.toString()
           }
         ]
       }
     }
   };
 },
 watch: {
   highlights: {
     handler: function() {
       this.datasource.pointers.pointer[0].value = this.highlights.lighting.toString();
     },
     deep: true
   }
 }
};
</script>
