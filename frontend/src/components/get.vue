<template>
  <v-container min-width="80%">
    <v-card class="mt-5">
      <v-progress-linear
        indeterminate
        v-show="isLoading"
      />
      <v-card-title primary-title> Read | 讀取 </v-card-title>
      <v-card-text>
        <div v-for="item in data" :key="item">
          {{item}}
        </div>
      </v-card-text>
      <v-card-actions>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
export default {

  data() {
    return {
      menu: false, 
      name: "",
      age: undefined,
      date: "",
      isLoading: false, 
      data: [],
    };
  },
  mounted() {
    this.submitData();
  },
  methods: {
    async submitData(){
      this.isLoading = true;
      const res = await this.$axios.get(
        "http://127.0.0.1:9000/get-doc"
      );
      this.data = res.data
      console.log(this.data);
      this.isLoading = false;
    }
  },
};
</script>
