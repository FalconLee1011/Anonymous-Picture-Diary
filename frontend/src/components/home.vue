<template>
  <v-container style="height: 92vh; overflow: scroll;" @scroll="scrollSpy">
    <v-dialog
      v-model="show"
      width="500"
      :overlay-opacity="0.85"
    >
      <v-card>
        <v-card-title primary-title>
          刪除貼文
        </v-card-title>
        <v-card-text>
          <v-text-field
            v-model="secret"
            label="Secret | 密碼"
            :append-icon="showSecreat ? 'mdi-eye-off' : 'mdi-eye'"
            :type="showSecreat ? 'text' : 'password'"
            @click:append="showSecreat = !showSecreat"
            :name="Math.random()"
          />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn @click="deletePost" outlined color="error">Delete | 刪除</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-timeline>
      <v-timeline-item
        v-for="(post, i) in posts"
        :key="i"
        small
      >
        <template v-slot:opposite>
          <span
            :class="`headline font-weight-bold --text`"
            v-text="parseDate(post.uploaded_at)"
          ></span>
        </template>
        <v-card>
          <v-card-title>
            {{post.title}}
            <v-spacer />
            <v-btn @click="toggleDelete(post.filename)" icon color="error">
              <v-icon >mdi-timeline-remove-outline</v-icon>
            </v-btn>
          </v-card-title>
          <v-card-subtitle>
            {{post.uploader}}
          </v-card-subtitle>
          <v-card-text>
            <v-img :src="`http://127.0.0.1:9000/get-attachment?uuid=${post.filename}`" />
            <div>
              {{post.description}}
            </div>
            <div>
              <span v-for="tag in post.tags" :key="`${tag}-${post.filename}`"> #{{tag}} </span>
            </div>
          </v-card-text>
        </v-card>
      </v-timeline-item>
      <v-timeline-item v-if="isFetching && !noMoreToLoad" >
        <template v-slot:icon>
          <v-progress-circular size="20" width="2" indeterminate></v-progress-circular>
        </template>
      </v-timeline-item>
    </v-timeline>
    <v-row class="mt-2" v-if="noMoreToLoad" >
      <v-col style="text-align: center;">
        No more posts | 沒有更多的貼文了
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      posts:[], 
      isFetching: false, 
      noMoreToLoad: false, 
      currentLoaded: 0, 
      show: false, 
      secret: "", 
      showSecreat: false, 
      toBeDeleted: undefined,
    }
  },
  watch:{
    async '$route.params.keyword'(){
      console.log(this.$route.params.keyword);
      if(this.$route.params.keyword === undefined){
        location.reload();
        return;
      }
      await this.search(this.$route.params.keyword);
      this.$emit("searchDone", false);
    }
  }, 
  created() {
    // document.addEventListener('scroll', this.scrollSpy);
  },
  destroyed() {
    // document.removeEventListener('scroll', this.scrollSpy);
  },
  async mounted() {
    const keyword = this.$route.params.keyword;
    if(keyword){
      await this.search(keyword);
      this.$emit("searchDone", false);
    }
    else{
      this.fetchPosts();
    }
  },
  methods: {
    async scrollSpy(event){
      const el = event.target;
      const scrollTop = el.scrollTop 
      const clientHeight = el.clientHeight
      const scrollHeight = el.scrollHeight
      if((scrollTop + clientHeight >= scrollHeight) && !this.isFetching && !this.noMoreToLoad){
        this.isFetching = true;
        await this.fetchPosts(this.currentLoaded, 5);
      }
    }, 
    async fetchPosts(skip=0, limit=5){
      const to = skip + limit;
      const res = await this.$axios.get(`http://127.0.0.1:9000/get-some-doc?begin=${skip}&end=${to}`);
      if(res.data.length < limit){
        this.noMoreToLoad = true;
        return;
      }
      this.posts = [...this.posts, ...res.data];
      this.currentLoaded += limit;
      this.isFetching = false;
    }, 
    loadMorePosts(){
      for (let i = 0; i < 5; i++) {
        this.posts.push(post);
      }
    }, 
    parseDate(ISODate) {
      const date = new Date(ISODate);
      return date.toLocaleString();
    },
    toggleDelete(uuid){
      this.toBeDeleted = uuid;
      this.show = true;
    }, 
    async search(keyword){
      this.isLoading = true;
      const res = await this.$axios.get(`http://localhost:9000/search?keyword=${keyword}`);
      this.posts = res.data;
      this.noMoreToLoad = true;
      this.isLoading = false;
    }, 
    async deletePost(){
      try {
        await this.$axios.delete(`http://127.0.0.1:9000/delete-doc?filename=${this.toBeDeleted}`, {
          headers: {
            secret: this.secret
          }, 
        });
        this.$toast("成功刪除貼文！", {
          type: "success"
        });
        setTimeout(() => {
          location.reload();
        }, 1500);
      } catch (e) {
        this.$toast("密碼錯誤！", {
          type: "error"
        });
      }
    },
  },
}
</script>
