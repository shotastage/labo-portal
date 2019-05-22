<template>
  <v-app>
  <v-toolbar app>
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title>NECO Portal</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat href="/kgl/">KGL</v-btn>
      <v-btn flat href="https://sfc-rg.slack.com/app_redirect?channel=neco">Slack</v-btn>
      <v-btn flat href="/admin/">Admin</v-btn>
    </v-toolbar-items>
  </v-toolbar>

  <div style="height:150px;"></div>


   <v-layout>
    <v-flex xs12 sm6 offset-sm3>
        
        
        
        <div>
              
                <v-textarea
                  outline
                  v-model="post_text"
                  label="Type your question"
                  value=""
                  lazy
                ></v-textarea>
                <v-btn color="info" @click="postArticle(post_text)">投稿</v-btn>
        </div>
            
        

        
    </v-flex>
  </v-layout>


  <PostField/>

  <v-container fluid grid-list-md>

    <div v-for="field in fieldList" :key="field">
      <v-layout row wrap justify-space-around>
        <v-flex>
          <TimeLine v-bind:content="field"/>
        </v-flex>
      </v-layout>
    </div>

   
  </v-container>




    <v-footer class="pa-3">
      <v-spacer></v-spacer>
      <div>&copy; {{ new Date().getFullYear() }} Shota Shimazu</div>
    </v-footer>
  </v-app>
</template>


<script>
import HelloWorld from './components/HelloWorld'
import PostField from './components/PostField'
import TimeLine from './components/TimeLine'
import AppMenu from './components/AppMenu'
import axios from 'axios'


export default {
  name: 'App',
  components: {
    HelloWorld,
    PostField,
    AppMenu,
    TimeLine
  },
  data () {
    return {
      fieldList: []
    }
  },
  mounted: function () {
    console.log('mounted')
    axios.get('/api/fields/')
    .then((response) => {
        this.fieldList = response.data
    })
    .catch((error) => {
        console.log(error)
    })
  }, methods: {
      postArticle: function(article_text) {
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.post('/api/fields/create/', {
          title: "NONE TATILE",
          text: article_text,
          content_type: "html",
          created_by: "匿名"
        }, {
          headers: {'Content-Type': 'application/json'}
        })
        
      }
    }
}
</script>
