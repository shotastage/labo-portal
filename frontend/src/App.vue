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



  <PostField/>

  <v-container grid-list-md>
    <v-layout row>
    </v-layout>
    <v-layout row wrap>
      <TimeLine/>
    </v-layout>
    <v-layout row wrap>
      <TimeLine/>
    </v-layout>
    <v-layout row wrap>
      <TimeLine/>
    </v-layout>
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


export default {
  name: 'App',
  components: {
    HelloWorld,
    PostField,
    AppMenu
  },
  data () {
    return {
      //
    }
  }
}
</script>
