<template>
 <v-card flat tile>
    <v-toolbar>
        <v-toolbar-title>DEMO</v-toolbar-title>
        <v-spacer />
      <v-toolbar-items>
        <v-btn v-for="menuItem in menuItems" :key="menuItem.icon" :to="menuItem.link" :disabled="!menuItem.link">
          <v-icon class="mr-2">{{menuItem.icon}}</v-icon>
          {{menuItem.text}}
        </v-btn>
      </v-toolbar-items>
      <!-- <v-toolbar-items> -->
        <v-expand-transition>
          <v-btn v-if="darkTheme" class="ml-3 mr-1" icon @click="changeTheme">
            <v-icon>mdi-moon-waxing-crescent</v-icon>
          </v-btn>
          <v-btn v-else class="ml-3 mr-1" icon @click="changeTheme">
            <v-icon>mdi-white-balance-sunny</v-icon>
          </v-btn>
        </v-expand-transition>
      <!-- </v-toolbar-items> -->
    </v-toolbar>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      darkTheme: false, 
      menuItems:[
        {
          text: "Home | 首頁", 
          icon: "mdi-home-outline", 
          link: "/"
        },
        {
          text: "Create | 新增", 
          icon: "mdi-plus", 
          link: "create"
        },
        {
          text: "Update | 修改", 
          icon: "mdi-pencil-outline", 
          link: undefined
        },
        {
          text: "Read | 讀取", 
          icon: "mdi-book-open", 
          link: "get"
        },
        {
          text: "Delete | 刪除", 
          icon: "mdi-delete-outline", 
          link: undefined
        },
      ]
    }
  },
  created() {
    let theme = localStorage.getItem("theme");    
    if(theme === undefined || theme === null){
      localStorage.setItem("theme", this.$vuetify.theme.dark);
      theme = this.$vuetify.theme.dark;
    }
    this.$vuetify.theme.dark = (theme == "true" || theme === true) ? true : false;
    this.darkTheme = this.$vuetify.theme.dark;
  },
  methods: {
    changeTheme(){
      this.darkTheme = !this.darkTheme;
      this.$vuetify.theme.dark = this.darkTheme;
      localStorage.setItem("theme", this.$vuetify.theme.dark);
    }
  },
  watch: {
  },
}
</script>