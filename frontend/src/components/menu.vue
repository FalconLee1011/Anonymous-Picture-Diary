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
    </v-toolbar>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
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
}
</script>