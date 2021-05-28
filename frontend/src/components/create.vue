<template>
  <v-container min-width="80%">
    <v-card class="mt-5">
      <v-progress-linear
        indeterminate
        v-show="isLoading"
      />
      <v-card-title primary-title> Create | 新增 </v-card-title>
      <v-card-text>

        <v-row>
          <v-col>
            <v-text-field v-model="name" label="Name" id="id"></v-text-field>    
          </v-col>
          <v-col>
            <v-text-field v-model="age" label="Age" id="id"></v-text-field>
          </v-col>
        </v-row>

        <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="false"
          :return-value.sync="date"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="date"
              label="Date"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker v-model="date" no-title scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="menu = false"> 取消 </v-btn>
            <v-btn text color="primary" @click="$refs.menu.save(date)">
              確認
            </v-btn>
          </v-date-picker>
        </v-menu>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn @click="submitData" color="success" outlined>
          <v-icon class="ml-2">mdi-send</v-icon>
          送出
        </v-btn>
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
    };
  },
  methods: {
    async submitData(){
      this.isLoading = true;
      await this.$axios.post(
        "http://127.0.0.1:9000/create-doc", 
        {
          name: this.name, 
          age: this.age, 
          date: this.date, 
        }
      );
      this.isLoading = false;
    }
  },
};
</script>
