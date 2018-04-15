<template>

  <div id="container">
    <v-toolbar color="blue">
      <v-toolbar-title class="white--text">Undefined</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <video id="video"></video>
    <div id="cards">
      <v-card id="card" v-for="item in cards">
        {{item}}
      </v-card>
    </div>
    <v-btn fab dark large color="purple" @click="snapshot" id="play_btn">
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAIUSURBVGhD7Zg9SkNBFEaDoCgK0dJSsdLCVtyALkALWy1cgLgCswAtLMXCPqAbsFew08IutlYiiCC857lwb0DiT/JyZ+YF58BHhmjmfqdIZpJGJpPJdCmKYpoclGU5oU+NJgg0SYnMA9nUp0cPEzGQafOwqH8eHSj9RURA5o20yJT+W/2hd4+IgUiHh23913pD0R9FDISuyYq+pJ7Q808RAZEPcsJyVl9aLyjWl4iBzDPZYzmmW9QDCg0kYiBzS9Z0m/TQqZKIgIhwTuZ1u3TQp7KIgcgLSXs7YPjQIgYy92RDt44L891EDGTaZEFHxIG57iICInI7OCJxbgfMDCJiINIhWzouHMwKKmIgI7eDZR3rDzOiiAiIyO3gmKX/7YBNo4kYyMjtYJel3+2AzaKLGMjcEJ/bAfslExEQEc5YTmqlarBBapE7sq51qsNeSUQoL++TfZY+7xM2iipCefnkOmXp+8nFhtFEEJCzZFVH+8L+wUUo/0R2dGQYmBNMhPLvpMVyRseFgyFBRBC4JEs6JjzMdBWh/COJ/4sls11EKP9KDlmm+ZbI4KFEKC9ckLTf2+lSWYTyPqeyB/QZWITyvqeyB5TpW4TydirP6cvrA6X6EkEg3KnsAR1/FaF8+FPZA7p+K0L5eKeyBxTtEUHgisQ7lT2gd1eE8mlOZQ/o36R82lPZA8qPI5H+1/RMJvPfaTQ+AfPoJiq5n2/hAAAAAElFTkSuQmCC"/>
    </v-btn>
  </div>
</template>

<script>
import api from '../api';

export default {
  name: 'HelloWorld',
  data() {
    return {
      translated: '',
      cards: [],
      readingList: [],
      curRead: 0,
      playing: false,
    };
  },
  mounted() {
    // Grab elements, create settings, etc.
    const video = document.getElementById('video');

    // Get access to the camera!
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      // Not adding `{ audio: true }` since we only want video now
      navigator.mediaDevices.getUserMedia({ video:true }).then((stream) => {
        video.src = window.URL.createObjectURL(stream);
        video.play();
      });
    }
  },
  methods: {
    snapshot() {
      const canvas = (this.canvas = document.createElement('canvas'));
      const context = canvas.getContext('2d');
      const video = document.getElementById('video');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

      this.playing = false;
      this.curRead = 0;
      this.readingList = [];
      this.imageCaption();
    },

    playCurAudio() {
      const audio = document.createElement('audio');
      if (this.curRead >= this.readingList.length || this.playing) {
        return;
      }
      this.playing = true;
      audio.src = this.readingList[this.curRead++];
      audio.play();

      audio.onended = () => {
        if (this.curRead < this.readingList.length || !this.playing) {
          audio.src = this.readingList[this.curRead++];
          audio.play();
        } else {
          this.playing = false;
        }
      };
    },

    translate(text) {
      api.translate(text, 'en-zh').then((res) => {
        this.translated = res.data.translation[0];
        this.cards.push(res.data.translation[0]);
        this.readingList.push(res.data.tSpeakUrl);
        this.playCurAudio();
      }).catch((err) => {
        alert(err);
      });
    },

    imageCaption() {
      this.canvas.toBlob(
        (data) => {
          api.imageCaption(data).then((res) => {
            this.cards.push(res.data.c.caption);
            this.translate(res.data.c.caption);

            this.cards.push(res.data.d);
            this.translate(res.data.d);
            setTimeout(()=>document.querySelector("#cards").scrollTo(0,10000000000),100);
            console.log(res.data);
          });
        },
        'image/jpeg',
        1,
      );
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  #container {
    display: flex;
    flex-flow: row nowrap;
    height: 100%;
    width: 100%;
    overflow-y: hidden;
  }
  #video {
    width: 100vw;
    max-height: 60vh;
  }
  #play_btn {
    position: absolute;
    z-index: 9999;
    right:10px;
    bottom: 10px;
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
    img {
      width: 50%;
      height: 50%;
    }
  }
  #cards {
    flex-grow: 0;
    overflow-y: auto;
    #card {
      margin: 1rem;
      padding: 1rem;
      display: flex;
      flex-flow: column wrap;
    }
  }
</style>
