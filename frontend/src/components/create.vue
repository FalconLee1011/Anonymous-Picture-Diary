<template>
  <v-container min-width="80%">
    <v-card class="mt-5">
      <v-progress-linear v-model="progress" v-show="isLoading" />
      <v-card-title primary-title> Upload | 上傳照片 </v-card-title>
      <v-card-text>
        資訊
        <v-divider />
        <v-row>
          <v-col>
            <v-text-field
              v-model="uplodaer"
              :name="Math.random()"
              label="Uplodaer | 上傳者"
              hint="Keep blank to stay anonymously. | 留白以抱持匿名身份。"
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              v-model="title"
              :name="Math.random()"
              label="Title | 相片標題"
              hint="Brief about the photo | 簡要說明相片。"
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
              v-model="secret"
              label="Secret | 密碼"
              :append-icon="showSecreat ? 'mdi-eye-off' : 'mdi-eye'"
              :type="showSecreat ? 'text' : 'password'"
              @click:append="showSecreat = !showSecreat"
              :name="Math.random()"
              hint="The secret is the key to delete this post. | 此密碼是刪除貼文必備的資訊。"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-textarea
              v-model="description"
              :name="Math.random()"
              rows="1"
              auto-grow
              hint="Multi-line is supported. | 支援多行"
              label="Description | 相片說明"
            ></v-textarea>
          </v-col>
        </v-row>
        <v-row class="mb-3">
          <v-col>
            <v-text-field
              v-model="tags"
              label="Tags | 標籤"
              :name="Math.random()"
              hint="Split'em with comma | 使用逗號 ',' 將多個標籤分開。"
            ></v-text-field>
          </v-col>
        </v-row>
        照片
        <v-divider class="mb-5" />
        <v-row>
          <v-col>
            <file-pond
              ref="uploader"
              label-idle="Drag & drop to upload | 拖曳並放開以上傳"
              :allow-multiple="false"
              :instantUpload="false"
              v-on:updatefiles="handleFileUpload"
              :rules="[(v) => !!v || '請選擇至少一個檔案']"
            />
          </v-col>
        </v-row>
      </v-card-text>
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
      showSecreat: false,

      // Form's data
      uplodaer: "",
      title: "", 
      secret: "",
      description: "",
      tags: "",
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
    handleFileUpload(files) {
      this.files = files.map((files) => files.file);
    },
    async submitData() {
      this.isLoading = true;
      let payload = new FormData();
      let tags = [];
      
      this.tags.split(",").forEach( tag => {
        const _tag = tag.replace(" ", "")
        if(tag.length != 0)
          tags.push(tag);
      })
      payload.append( "uploader", this.uplodaer )
      payload.append( "title", this.title )
      payload.append( "secret", this.secret )
      payload.append( "description", this.description )
      payload.append( "tags", tags )
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
      this.$toast("成功新增貼文！", {
        type: "success"
      });
      this.isLoading = false;
    },
  },
};
</script>
