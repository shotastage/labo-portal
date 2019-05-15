<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <div class="floating_button">
          <v-btn color="error" v-on="on" fab dark>
            <v-icon>fas fa-edit</v-icon>
          </v-btn>
        </div>
      </template>
      
      
      <v-card>
        <v-card-title>
          <span class="headline">New Post</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout column>
                <v-flex>
                  <v-text-field
                    v-model="post_title"
                    placeholder=""
                    label="タイトル"
                    solo
                  ></v-text-field>
                </v-flex>

                <v-textarea
                  v-model="post_text"
                  outline
                  name="input-7-4"
                  label="新しい投稿"
                  value=""
                ></v-textarea>           
            </v-layout>
          </v-container>
          <small>* この機能はテスト中です.</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="dialog = false">キャンセル</v-btn>
          <v-btn color="blue darken-1 warning" @click="dialog = false">投稿</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>



<style scoped>
.floating_button {
  z-index: 10;
  position: fixed;
  bottom: 40px;
  right: 40px;
}
</style>


<script>
import axios from 'axios'


export default {
    data: () => ({
      dialog: false,
      post_title: post_title,
      post_text: post_text
    }),
    mounted: function () {
      axios.post('/api/fields/', {
      title: post_title,
      text: post_text,
      content_type: "html",
      created_by: "unkown"
    });
  }
}
</script>