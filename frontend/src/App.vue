<template>
  <v-app>
    <menubar />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import menubar from "./components/menu"

export default {
  components:{
    menubar
  }, 
  created() {
    console.log("App has been created.");
  },
};
</script>
