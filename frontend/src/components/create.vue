<template>
  <v-container min-width="80%">
    <v-card class="mt-5">
      <v-progress-linear v-model="progress" v-show="isLoading" />
      <v-card-title primary-title> Create | 新增 </v-card-title>
      <v-tabs v-model="tab">
        <v-tab>JSON</v-tab>
        <v-tab>FormData</v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
        <v-tab-item>
          <v-card-text>
            <v-row>
              <v-col>
                <v-text-field v-model="name" label="Name"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="age" label="Age"></v-text-field>
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
        </v-tab-item>
        <v-tab-item>
          <v-card-text>
            <v-row>
              <v-col>
                <v-text-field v-model="name" label="Name"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="age" label="Age"></v-text-field>
              </v-col>
            </v-row>
            <v-menu
              ref="menu"
              v-model="menu1"
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
            <file-pond
              ref="uploader"
              label-idle="拖曳或點擊上傳..."
              :allow-multiple="false"
              :instantUpload="false"
              v-on:updatefiles="handleFileUpload"
              :rules="[(v) => !!v || '請選擇至少一個檔案']"
            />
          </v-card-text>
        </v-tab-item>
      </v-tabs-items>
      <v-card-actions>
        <v-spacer />
        <v-btn @click="submitData" color="success" outlined>
          <v-icon class="mr-2">mdi-send</v-icon>
          送出
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
// Do this in the components those need this plugin
import vueFilePond from "vue-filepond";
import FilePondPluginImagePreview from "filepond-plugin-image-preview";
import "filepond/dist/filepond.min.css";
import "filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css";

const FilePond = vueFilePond(FilePondPluginImagePreview);

export default {
  components: {
    FilePond,
  },
  data() {
    return {
      // Controls Vue's components
      tab: 1,
      menu: false,
      menu1: false,

      // Form's data
      name: "",
      age: undefined,
      date: "",
      files: [],

      // Loading & progress
      isLoading: false,
      progressTotal: 0,
      progressCurrent: 1,
    };
  },
  computed: {
    progress() {
      if (this.progressCurrent != 0)
        return (this.progressTotal / this.progressCurrent) * 100;
      else return 0;
    },
  },
  methods: {
    handleFileUpload (files) {
      console.log(files);
      this.files = files.map((files) => files.file);
      console.log(this.files);
    },
    async submitData() {
      this.isLoading = true;
      switch (this.tab) {
        case 0:
          await this.submitDataUsingJSON();
          break;
        case 1:
          await this.submitDataUsingFormData();
          break;
        default:
          break;
      }
      this.isLoading = false;
    },
    async submitDataUsingJSON() {
      await this.$axios.post("http://127.0.0.1:9000/create-doc", {
        name: this.name,
        age: this.age,
        date: this.date,
      });
    },
    async submitDataUsingFormData() {
      let payload = new FormData();
      payload.append("name", this.name);
      payload.append("age", this.age);
      payload.append("date", this.date);
      for (let idx = 0; idx < this.files.length; idx++)
        payload.append(`file`, this.files[idx]);

      console.log(payload);
      await this.$axios.post(
        "http://127.0.0.1:9000/create-doc-with-attachment",
        payload,
        {
          onUploadProgress: (e) => {
            this.progressTotal = e.loaded;
            this.progressCurrent = e.total;
          },
        }
      );
    },
  },
};
</script>
