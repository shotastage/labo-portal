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

  <div style="height:80px;"></div>
  <div>
    <v-btn href="/recent_home/" color="error">以前のバージョンに戻す</v-btn>
  </div>


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
  }
}
</script>
