<template>
  <v-app>
    <menubar v-on:toggleSearch=toggleSearch />
    <searchBar ref="searchBar" />
    <v-main>
      <router-view v-on:searchDone="toggleSearch($event)" class="mt-16" />
    </v-main>
  </v-app>
</template>

<script>
import menubar from "./components/menu"
import searchBar from "./components/searchBar"

export default {
  components:{
    menubar, searchBar
  }, 
  created() {
    console.log("App has been created.");
  },
  methods: {
    toggleSearch(v=undefined){
      console.log("toggleSearch")
      this.$refs.searchBar.toggle(v);
    }
  },
};
</script>
