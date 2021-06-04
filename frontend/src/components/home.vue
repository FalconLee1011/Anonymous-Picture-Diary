<template>
  <v-container style="height: 92vh; overflow: scroll;" @scroll="scrollSpy">
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
          </v-card-title>
          <v-card-subtitle>
            {{post.uploader}}
          </v-card-subtitle>
          <v-card-text>
            <v-img :src="post.url" />
            <div>
              {{post.description}}
            </div>
            <div>
              <span v-for="tag in post.tags" :key="tag"> #{{tag}} </span>
            </div>
          </v-card-text>
        </v-card>
      </v-timeline-item>
      <v-timeline-item v-if="isFetching" >
        <template v-slot:icon>
          <v-progress-circular size="20" width="2" indeterminate></v-progress-circular>
        </template>
      </v-timeline-item>
    </v-timeline>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      posts:[], 
      isFetching: false, 
      currentLoaded: 0, 
    }
  },
  created() {
    // document.addEventListener('scroll', this.scrollSpy);
  },
  destroyed() {
    // document.removeEventListener('scroll', this.scrollSpy);
  },
  mounted() {
    this.fetchPosts();
  },
  methods: {
    scrollSpy(event){
      const el = event.target;
      const scrollTop = el.scrollTop 
      const clientHeight = el.clientHeight
      const scrollHeight = el.scrollHeight
      if((scrollTop + clientHeight >= scrollHeight) && !this.isFetching){
        this.isFetching = true;
        window.setTimeout(this.fetchPosts, Math.random() * 1500);
      }
      // console.log(`offsetHeight -> ${this.$refs.timeline.$el.offsetHeight} \n offsetTop -> ${this.$refs.timeline.$el.offsetTop} \n scrollHeight -> ${this.$refs.timeline.$el.scrollHeight} \n scrollLeft -> ${this.$refs.timeline.$el.scrollLeft} \n scrollTop -> ${this.$refs.timeline.$el.scrollTop} \n scrollWidth -> ${this.$refs.timeline.$el.scrollWidth}`)
    }, 
    fetchPosts(){
      const post = {
        title: "some-title", 
        time: "0", 
        description: "Same Shit Different Day", 
        uploader: "x", 
        tags: ["a", "b"],
        uploaded_at: "2021-04-01T18:30:00.0000Z", 
        taken_at: "2021-04-01T18:30:00.0000Z", 
        url: "http://localhost:9000/get-attachment?uuid=9e5518c8-0fc6-4fa5-9bec-203ef3e608c8", 
      }
      for (let i = 0; i < 5; i++) {
        this.posts.push(post);
      }
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
  },
}
</script>
