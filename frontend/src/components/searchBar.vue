<template>
  <v-dialog
    v-model="show"
    width="500"
    :overlay-opacity="0.85"
  >
    <v-card>
      <v-card-title primary-title>
        Search | 搜尋
      </v-card-title>
      <v-card-text>
        <v-text-field
          :name="Math.random()"
          label="輸入關鍵字"
          v-model="keyword"
          :loading="isLoading"
          append-icon="mdi-magnify"
          @click:append="search"
        />
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>

export default {
  data() {
    return {
      isLoading: false, 
      show: false, 
      keyword: "", 
    };
  },
  methods: {
    toggle(){
      this.show = !this.show;
    }, 
    async search(){
      this.isLoading = true;
      
      this.isLoading = false;
    }
  },
};
</script>
