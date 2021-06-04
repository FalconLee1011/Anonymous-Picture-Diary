<template>
 <v-card flat tile>
    <v-app-bar
      fixed
      hide-on-scroll
    >
      <v-toolbar-title>匿名照片日記</v-toolbar-title>
        <v-spacer />
      <v-toolbar-items>
        <v-btn @mouseover="showSearch = true" @mouseleave="showSearch = false" @click="$emit('toggleSearch')" >
          <v-icon >mdi-magnify</v-icon>
          <v-expand-x-transition>
            <span v-if="showSearch">Search | 搜尋</span>
          </v-expand-x-transition>
        </v-btn>
        <v-btn @mouseover="showTimeline = true" @mouseleave="showTimeline = false" to="/" >
          <v-icon >mdi-timeline-outline</v-icon>
          <v-expand-x-transition>
            <span v-if="showTimeline">Timeline | 動態</span>
          </v-expand-x-transition>
        </v-btn>
        <v-btn @mouseover="showUpload = true" @mouseleave="showUpload = false" to="/upload" >
          <v-icon >mdi-upload</v-icon>
          <v-expand-x-transition>
            <span v-if="showUpload">Upload | 上傳相片</span>
          </v-expand-x-transition>
        </v-btn>
        <v-btn @mouseover="showThemeChange = true" @mouseleave="showThemeChange = false"  v-if="darkTheme" :icon="!showThemeChange" @click="changeTheme">
          <v-icon>mdi-moon-waxing-crescent</v-icon>
          <v-expand-x-transition>
            <span v-if="showThemeChange">Lights on | 亮色主題</span>
          </v-expand-x-transition>
        </v-btn>
        <v-btn @mouseover="showThemeChange = true" @mouseleave="showThemeChange = false"  v-else :icon="!showThemeChange" @click="changeTheme">
          <v-icon>mdi-white-balance-sunny</v-icon>
          <v-expand-x-transition>
            <span v-if="showThemeChange">Goin' dark | 深色主題</span>
          </v-expand-x-transition>
        </v-btn>
      </v-toolbar-items>
      <!-- <v-toolbar-items> -->
      <!-- </v-toolbar-items> -->
    </v-app-bar>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      darkTheme: false, 
      showSearch: false, 
      showTimeline: false, 
      showUpload: false, 
      showThemeChange: false, 
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
    }, 
  },
  watch: {
  },
}
</script>