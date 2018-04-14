<template>

  <div id="container">
      <v-toolbar color="blue">
    <v-toolbar-title class="white--text">Undefined</v-toolbar-title>
    <v-spacer></v-spacer>
  </v-toolbar>
 <video id="video"></video>
     <v-btn fab dark large color="purple" @click="snapshot" id="play_btn">
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAIUSURBVGhD7Zg9SkNBFEaDoCgK0dJSsdLCVtyALkALWy1cgLgCswAtLMXCPqAbsFew08IutlYiiCC857lwb0DiT/JyZ+YF58BHhmjmfqdIZpJGJpPJdCmKYpoclGU5oU+NJgg0SYnMA9nUp0cPEzGQafOwqH8eHSj9RURA5o20yJT+W/2hd4+IgUiHh23913pD0R9FDISuyYq+pJ7Q808RAZEPcsJyVl9aLyjWl4iBzDPZYzmmW9QDCg0kYiBzS9Z0m/TQqZKIgIhwTuZ1u3TQp7KIgcgLSXs7YPjQIgYy92RDt44L891EDGTaZEFHxIG57iICInI7OCJxbgfMDCJiINIhWzouHMwKKmIgI7eDZR3rDzOiiAiIyO3gmKX/7YBNo4kYyMjtYJel3+2AzaKLGMjcEJ/bAfslExEQEc5YTmqlarBBapE7sq51qsNeSUQoL++TfZY+7xM2iipCefnkOmXp+8nFhtFEEJCzZFVH+8L+wUUo/0R2dGQYmBNMhPLvpMVyRseFgyFBRBC4JEs6JjzMdBWh/COJ/4sls11EKP9KDlmm+ZbI4KFEKC9ckLTf2+lSWYTyPqeyB/QZWITyvqeyB5TpW4TydirP6cvrA6X6EkEg3KnsAR1/FaF8+FPZA7p+K0L5eKeyBxTtEUHgisQ7lT2gd1eE8mlOZQ/o36R82lPZA8qPI5H+1/RMJvPfaTQ+AfPoJiq5n2/hAAAAAElFTkSuQmCC"></img>
    </v-btn>
      <v-card id="card" v-if="caption">
          {{caption}}
      </v-card>
      <v-card id="card" v-if="translated">
       {{translated}}
        </v-card>


 </div>
</template>

<script>
import api from "../api";

export default {
  name: "HelloWorld",
  data() {
    return {
      text: "",
      translated: "",
      lastOutput: {},
      caption: ""
    };
  },
  mounted() {
    // Grab elements, create settings, etc.
    const video = document.getElementById("video");

    // Get access to the camera!
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      // Not adding `{ audio: true }` since we only want video now
      navigator.mediaDevices.getUserMedia({ video:true }).then(stream => {
        video.src = window.URL.createObjectURL(stream);
        video.play();
      });
    }
  },
  methods: {
    snapshot() {
      const canvas = (this.canvas = document.createElement("canvas"));
      const context = canvas.getContext("2d");
      const video = document.getElementById("video");
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

      this.imageCaption();
    },

    translate() {
      const audio = document.createElement("audio");
      api
        .translate(this.text, "en-zh")
        .then(res => {
          this.lastOutput = res.data;
          this.translated = res.data.translation[0];
          audio.src = res.data.tSpeakUrl;
          audio.play();
        })
        .catch(err => {
          alert(err);
        });
    },

    imageCaption() {
      this.canvas.toBlob(
        data => {
          api.imageCaption(data).then(res => {
            this.caption = res.data.caption;
            this.text = this.caption;
            this.translate();
          });
        },
        "image/jpeg",
        1
      );
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
#container {
  width: 100%;
  display: flex;
  flex-flow: row nowrap;
}
#video {
  width: 100vw;
}
#play_btn {
  position: absolute;
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
#card {
  margin: 1rem;
  padding: 1rem;
  display: flex;
  flex-flow: column wrap;
}
</style>
