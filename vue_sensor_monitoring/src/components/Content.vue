<template>
 <div style="position: relative;">
     <temp-var-chart :tempVar="tempVar" :co2Var="co2Var"></temp-var-chart>
     <today-highlights :highlights="highlights"></today-highlights>
 </div>
</template>

<script>
import TempVarChart from './TempVarChart.vue';
import Highlights from './Highlights.vue';

export default {
 props: ['highlights', 'tempVar', 'co2Var'],
 components: {
   'temp-var-chart': TempVarChart,
   'today-highlights': Highlights
 },
}
</script>
